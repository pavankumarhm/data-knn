# K-Nearest-Neighbors

## Download the dataset

The dataset is available [here](https://wagon-public-datasets.s3.amazonaws.com/Machine%20Learning%20Datasets/ML_Houses_clean.csv). Let's download it and store it in the `data` folder in the `01-KNN` directory with the following commands:

``` bash
cd ~/code/<user.github_nickname>/{{local_path_to("05-ML/03-Performance-metrics/01-KNN")}}
curl https://wagon-public-datasets.s3.amazonaws.com/Machine%20Learning%20Datasets/ML_Houses_clean.csv > data/houses_clean.csv
```

## The dataset

- The dataset is a selection of features of the Houses dataset.
- Most features have already been preprocessed
- The target is the sale price of the houses

## Exercise

The exercise decomposes the KNN algorithm and its mechanics. You will:

- Discover its sensitivity to scale
- Voluntarily make it overfit
- Fine tune its parameter K

Finally, you will compare its performance to the one of a Linear Regression, and choose the model most suited for the task.

To start the exercise, open `KNN.ipynb` in `jupyter notebook` and follow the instructions.

🚀 Your turn!
