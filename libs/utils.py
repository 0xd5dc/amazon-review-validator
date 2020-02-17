from pyspark.ml.classification import LogisticRegression, NaiveBayes, DecisionTreeClassifier, GBTClassifier, \
    RandomForestClassifier
from pyspark.ml.feature import VectorAssembler
from pyspark.mllib.evaluation import BinaryClassificationMetrics
from pyspark.sql.functions import current_date, expr, datediff, to_date, lit, coalesce, length, regexp_replace, count, \
    isnan, col, when

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

import re


# Testing function
def hello():
    """
    test if the module is accessible
    :rtype: None
    """
    print('libs imported properly!')


# ETL function
def get_null_columns(df, cols=['review_date', 'review_length']):
    for column in cols:
        df.select(['review_id', column]).where('{0} is NULL'.format(column)).show()


def get_unique_values(df):
    for column in df.columns:
        print("{0}: {1} unique values".format(column, df.select(column).distinct().count()))


def get_correlation_target_col_length(spark, target, col, table):
    spark.sql("select {0}, avg(length({1})) from {2} group by {0} order by {0}".format(target, col, table)).show()


def fill_na_mean(df, column):
    return df.fillna(df.selectExpr('avg({0}) as mean'.format(column)).first().asDict()['mean'], subset=[column])


def get_null_counts(df):
    df.select([count(when(isnan(c) | col(c).isNull(), c)).alias(c) for c in df.columns]).show()


def get_distribution_col(spark, col_a, col_b):
    """
    show the distribution of col_b in each group of col_a
    :param spark: current spark instance
    :param col_a: the column has finite groups
    :param col_b: the column to count
    """
    spark.sql('select {0}, sum({1}) as {1} from df group by {0} order by {0}'.format(col_a, col_b)).show()


# NLP function
def get_kv_pairs(row, exclusions=[]):
    # get the text from the row entry
    text = str(row.review_body).lower()
    # create blacklist of words
    blacklist = set(stopwords.words('english'))
    # add explicit words
    [blacklist.add(i) for i in exclusions]
    # extract all words
    words = re.findall(r'([^\w+])', text)
    # for each word, send back a count of 1
    # send a list of lists
    return [[w, 1] for w in words if w not in blacklist]


def get_word_counts(texts, exclusions=[]):
    mapped_rdd = texts.rdd.flatMap(lambda row: get_kv_pairs(row, exclusions))
    counts_rdd = mapped_rdd.reduceByKey(lambda a, b: a + b).sortBy(lambda a: a[1])
    return counts_rdd.collect()


def convert_str_to_int(df, col='verified_purchase', type_='int'):
    return df.select((df[col] == 'Y').cast(type_))


def get_review_age(df):
    return df.select(datediff(current_date(), to_date(df['review_date'])))


# Classifier function
def prepare_features(df):
    df = df.withColumn('exclam', length('review_body') - length(regexp_replace('review_body', '\!', '')))
    df = df.withColumn('age', datediff(current_date(), to_date(df['review_date'])))
    df = df.withColumn('review_length', length(df['review_body']))
    df = df.withColumn('helfulness', coalesce(df['helpful_votes'] / df['total_votes'], lit(0.0)))
    df = df.withColumn('label', expr("CAST(verified_purchase='Y' As INT)"))
    select_cols = df.select(['star_rating', 'helfulness', 'age', 'review_length', 'label']).na.fill(0)
    return select_cols


def split_data(df, rate=.9):
    training = df.sampleBy("label", fractions={0: rate, 1: rate}, seed=12)
    return training, df.subtract(training)


def get_auc_roc(classifier, training, test):
    model = classifier.fit(training)
    out = model.transform(test) \
        .select("prediction", "label") \
        .rdd.map(lambda x: (float(x[0]), float(x[1])))
    metrics = BinaryClassificationMetrics(out)
    print("Model: {1}. Area under ROC: {0:2f}".format(metrics.areaUnderROC, clf.__class__))
    return model, out, metrics


def get_vectorized_features(df, cols=['star_rating']):
    va = VectorAssembler().setInputCols(cols).setOutputCol(
        'features')
    return va.transform(df)

# Hypothesis function
