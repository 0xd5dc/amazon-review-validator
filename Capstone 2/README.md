# Objectives
1. Prepare data for models
    - [x] select features and a label
    - [x] vectorize features
2. Run classification models
    - [x] train and test with LogisticRegression
    - [x] train and test with NaiveBayes
    - [x] train and test with DecisionTreeClassifier
    - [x] train and test with RandomForestClassifier
    - [x] train and test with GBTClassifier
    - [x] compare the accuracies from the tested models
3. Output formatted data for visual aids
    - [ ] make presentation slides
    
# Directory

### A typical top-level directory layout

    .
    ├── src     
    │    ├── eda.ipynb              # EDA notebook
    │    ├── environment.py         # spark environment configs
    │    ├── helpers.py             # helper functions used in pyspark
    │    ├── nlp.ipynb              # natural language process notebook
    │    └── prediction.ipynb       # prediction notebook
    └── README.md


> `Error` import errors caused by missing init.py 
>
> `Fix` use %load to work around