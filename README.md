# Amazon Review Validator

## Introduction
This data science project is for my galvanize data science immersive, was divided into 3 capstones. Each capstone was completed within one week. Capstone 1 studies the dataset and concludes a few finds. Capstone 2 uses supervised learning methods to make predictions. Capstone 3 implements unsupervised learning methods, Neural Network models, to make predictions. The project uses python initially, and part 1 and 2 also use Spark, capstone 3 uses Tensorflow. I found python was inadequate with Spark, decided to re-write the project with scala to run at full potential.

## Directory
```
.
├── Capstone 1   
│    ├── src     
│    │    ├── data_migration.ps          # data migration from aws s3 to Azure blob
│    │    └── etl.sh                     # clean data
│    └── README.md  
├── Capstone 2          
│    ├── src     
│    │    ├── eda.ipynb                 # EDA notebook
│    │    ├── environment.py            # spark environment configs
│    │    ├── helpers.py                # helper functions used in pyspark
│    │    ├── nlp.ipynb                 # natural language process notebook
│    │    └── prediction.ipynb          # prediction notebook
│    └── README.md                      # clean data
├── Capstone 3   
│    ├── src     
│    │    ├── placeholder               # placeholder
│    │    └── placeholder               # placeholder
│    └── README.md  
└── README.md
```
   
## [Capstone 1](https://github.com/0xd5dc/amazon-review-validator/blob/master/Capstone%201/README.md)
   
In this capstone, I explored the dataset, extracted features, studied the relationships between label and features, proposed and tested my hypothesis.

## [Capstone 2](https://github.com/0xd5dc/amazon-review-validator/blob/master/Capstone%202/README.md)
  
In this capstone, I used engineered features and label to train a few supervised machine learning models, and evaluated the model performance in order to find the best model.

## [Capstone 3](https://github.com/0xd5dc/amazon-review-validator/blob/master/Capstone%203/README.md)
    
In this capstone, I used review text and label to train a few neural network machine learning models, and evaluated the model performance in order to find the best model.

## Business Application
- Review validation is important to both vendors and customers because vendors want constructive feedback to improve their products and customers want to learn customer feedback before purchases.
- This project could identify the hidden actual users, who bought the product from any store other than Amazon because a review without a verified purchase may or may not be a valid review from an actual user, but a review with a verified purchase is from an actual user. 
- The practical use of the project will be displaying product reviews strategically to increase sales ethically. 
    - For example, many users only read reviews from uses with verified purchases. So the verified purchase information can be displayed passively, namely, a user has to click a button to show the verified purchase information. 
    
## Assumptions
- The world is not perfect that there are fake reviews in the dataset.
- Amazon has business ethics that Amazon didn't systematically fabric fake reviews, namely, true reviews are more than fakes.
- The cost of fake review creation is more for reviews with a verified purchase than reviews without a verified purchase.

## Data 
Amazon Customer Reviews (a.k.a. Product Reviews) is one of Amazon’s iconic products. In a period of over two decades since the first review in 1995, millions of Amazon customers have contributed over a hundred million reviews to express opinions and describe their experiences regarding products on the Amazon.com website. 
> [Official Documentation: Amazon Customer Reviews ](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)


## SHORTCUTS
[Index](https://github.com/0xd5dc/amazon-review-validator/)

[Capstone 1](https://github.com/0xd5dc/amazon-review-validator/blob/master/Capstone%201/README.md)

[Capstone 2](https://github.com/0xd5dc/amazon-review-validator/blob/master/Capstone%202/README.md)

[Capstone 3](https://github.com/0xd5dc/amazon-review-validator/blob/master/Capstone%203/README.md)