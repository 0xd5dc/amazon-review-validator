# Amazon Review Validator
My data science project to guess if an amazon review is helpful for galvanize DSI. 
## Directory

    .
    ├── src     
    │    ├── data_migration.ps          # data migration from aws s3 to Azure blob
    │    └── etl.sh                     # clean data
    └── README.md

## Automation Pipeline
- create crontab jobs
    - ETL data
    - run spark job to train and test model with the cleaned data
    - save formatted output
- creat visual aids
### Planning and Reasoning
Amazon Customer Review dataset is on AWS S3, but I have a few Azure VMs, which utlized around 20%, and decided to use my Azure VMs instead of AWS S3.

I am going to deploy Spark docker containers to perform data analysis, may create a spark cluster in production stage.

### Data Migration AWS S3 Bucket -> Azure Blob Storage
Steps for data migrate check [this Powershell scripts]()
>Azure Documentations are outdated but its staff responded to my questions within a reasonable time frame.

```
sudo apt-get install blobfuse -y
mkdir ~/data
vim ~/fuse_connection.cfg
sudo blobfuse ~/data --tmp-path=/mnt/resource/blobfusetmp  --config-file=/home/azureuser/fuse_connection.cfg -o attr_timeout=240 -o entry_timeout=240 -o negative_timeout=120 -o allow_other
```
>save credentials in fuse_connection.cfg
>
>mount azure blob to ~/data
### Data Preparation
I don't need all the columns to perform analysis.
1. convert reviews to lowercase and remove html tags
2. select meaningful columns as features
3. optional - convert csv to parquet in order to optimize performance

## EDA
## Hypothesis
 In reviews with rating>4 and <2, people found reviews with words top 50 occurances are more helpful
 More frequently used words are more helpful or less frequently used words are more helpful?
 1)
 - [ ] H0: the helpfulness mean of most used 100 words > the helpfulness mean of the population
 - [x] H1: the helpfulness mean of most used 100 words < the helpfulness mean of the population
 2) 
- [x] H0: the helpfulness mean of least used 100 words > the helpfulness mean of the population
- [ ] H1: the helpfulness mean of least used 100 words < the helpfulness mean of the population
 
### How about ratings?
  Higher rating reviews or lower rating reviews are more helpful?
 1)
 H0: the helpfulness mean of Higher rating reviews > the helpfulness mean of the population
 H1: the helpfulness mean of Higher rating reviews < the helpfulness mean of the population
 
 2) 
 H0: the helpfulness mean of lower rating reviews > the helpfulness mean of the population
 H1: the helpfulness mean of lower rating reviews < the helpfulness mean of the population
 

## SHORTCUTS
[Index](https://github.com/0xd5dc/amazon-review-validator/)

[Capstone 1](https://github.com/0xd5dc/amazon-review-validator/blob/master/Capstone%201/README.md)

[Capstone 2](https://github.com/0xd5dc/amazon-review-validator/blob/master/Capstone%202/README.md)

[Capstone 3](https://github.com/0xd5dc/amazon-review-validator/blob/master/Capstone%203/README.md)