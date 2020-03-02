
## Summary
This project uses product review_body and verfied_purchase columns from Amazon Review Dataset to train machine learning models, Simple RNN,Long Short Term Memory Unit (LSTM) and Gated Recurrent Unit(GRU) and test predictions, on Tensorflow platform. 

## Business Application
- The project has the potential to provide benefit to users beyond just being interesting. (Is this project useful?) 
I am interested in verified purchase because a review without a verified purchase may or may not from a real customer. 
- Practical use is well articulated and demonstrated by project and project notes. (How well is this being explained as useful?) 
A practical use of the project will be display product review strategically. As the platform owner, Amazon, display reviews more likely to increase sales or attracts .
## Directory
```
root
├── Capstone 3
│   ├── README.md
│   ├── eda.ipynb
│   ├── results
│   │   ├── roc.png
│   │   └── clean_data_frame.p
│   ├── task.log
│   └── task_runner.py
├── LICENSE
├── README.md
├── libs
│   ├── __init__.py
│   └── utils.py
├── scripts
│   ├── data_migration.ps
│   └── etl.sh
├── templates
│   ├── load_data.py
│   └── load_libs.py
└── tests
    ├── sample_us.tsv
    └── benchmark.ipynb
```
## Assumptions
- Data on the storage server are mounted
- A symbolic link, Data, is to the mounted data
- Data is pre-processed, html tags removed and text cases lowered using ../scripts/[etl.sh](https://github.com/0xd5dc/amazon-review-validator/blob/master/scripts/etl.sh)
- Tensorflow 2.0.1 stable version installed
- latest Pandas, Numpy, pickle, sklearn, matplotlib is properly installed via pip

## Data Preparation
### Data Source
Amazon Customer Reviews (a.k.a. Product Reviews) is one of Amazon’s iconic products. In a period of over two decades since the first review in 1995, millions of Amazon customers have contributed over a hundred million reviews to express opinions and describe their experiences regarding products on the Amazon.com website. 

### Access data 
1. Copy data from AWS S3 to Azure 
    ```
    azcopy cp "https://s3.amazonaws.com/mybucket/" "https://mystorageaccount.blob.core.windows.net/mycontainer<SAS>" --recursive
    ```
    For complete guide check [AWS S3 to Azure](https://azure.microsoft.com/en-us/blog/move-your-data-from-aws-s3-to-azure-storage-using-azcopy/)
    > ../scripts/[data_migration.ps](https://github.com/0xd5dc/amazon-review-validator/blob/master/scripts/data_migration.ps) copies the entire Amazon review dataset to Azure storage account once the credential is provided.
2.  Create fuse_connection.cfg
    ```
    # fuse_connection.cfg
    accountName <my azure storage account>
    accountKey <my password>
    containerName s3bucket
    ```

3.  In terminal
    ```
    sudo blobfuse ~/blobs/mycontainer --tmp-path=/mnt/resource/blobfusetmp  --config-file=/home/azureuser/blobs/fuse_connection.cfg -o attr_timeout=240 -o entry_timeout=240 -o negative_timeout=120 -o allow_other
    
    sudo ln -s ~/blobs/mycontainer /path/to/project/data
    ```

4. Data used in eda.ipynb is amazon_reviews_us_Apparel_v1_00 
> For more detail check [Data Index](https://s3.amazonaws.com/amazon-reviews-pds/tsv/index.txt)
>
> Sample Data is in ../tests/[sample.tsv](https://github.com/0xd5dc/amazon-review-validator/blob/master/tests/sample_us.tsv)
## Development Objectives
1. Prepare data for models
    - [x] select text and a label
    - [x] lower the text cases
    - [x] remove not words
    - [x] re-sample the data by undersampling
    - [x] split data into train, test set
2. Build models
    - [x] train and test with Simple RNN
    - [x] train and test with LSTM
    - [x] train and test with GRU
    - [x] compare the results
3. Output formatted data for visual aids
    - [x] generate c curves
    - [x] make presentation slides
4. Deploy to the Spark Cluster
    - [x] create spark clusters
## Results
final products answers the business questions

### Metrics
- Accuracy
    - Calculates how often predictions matches labels.
- Precision
    - Computes the precision of the predictions with respect to the labels.
- Recall
    - Computes the recall of the predictions with respect to the labels.

# Evaluations
![ROC](https://github.com/0xd5dc/amazon-review-validator/blob/master/Capstone%203/results/roc.png)


## REFERENCES
- [Amazon Customer Reviews](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)
- [TensorFlow On Spark: Scalable TensorFlow Learning on Spark Clusters](https://databricks.com/session/tensorflow-on-spark-scalable-tensorflow-learning-on-spark-clusters)
- [TensorFlow On Spark Github](https://github.com/yahoo/TensorFlowOnSpark)
- [Tensorflow on Databricks](https://docs.databricks.com/applications/deep-learning/single-node-training/tensorflow.html)
- [Azure Databricks tutorial for TensorFlow developers](https://tsmatz.wordpress.com/2018/05/09/databricks-tensorflowonspark-example/)
## SHORTCUTS
[Index](https://github.com/0xd5dc/amazon-review-validator/)

[Capstone 1](https://github.com/0xd5dc/amazon-review-validator/blob/master/Capstone%201/README.md)

[Capstone 2](https://github.com/0xd5dc/amazon-review-validator/blob/master/Capstone%202/README.md)

[Capstone 3](https://github.com/0xd5dc/amazon-review-validator/blob/master/Capstone%203/README.md)