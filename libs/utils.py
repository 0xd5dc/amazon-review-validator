def fill_na_mean(df, column):
    print("fill_na_mean")
    # return df.fillna(df.selectExpr('avg({0}) as mean'.format(column)).first().asDict()['mean'], subset=[column])


def get_null_counts(df):
    print("get_null_counts")
    # df.select([count(when(isnan(c) | col(c).isNull(), c)).alias(c) for c in df.columns]).show()
