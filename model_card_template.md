# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

A classification model that takes publicly available data from the Census Bureau. The model used for this project is Random Forest Classifier.

## Intended Use

This model is intended for datasets that use categorical and numerical data. It also does well with missing inputs within the dataset. It wouldn't be suitable for projects that use real-time predictions,
or very large datasets because it would not run at optimal speeds.

## Training Data

80% of the data is used for the training data, 20% is using train_test_split. The source is UCI Adult Census Income dataset.

## Evaluation Data

The data used is available for public use and from the Census Bureau. It is processed using One Hot Encoders for the categorical features and label binarizer for the labels.

## Metrics
_Please include the metrics used and your model's performance on those metrics._

F1 Score 0.6416
Precision 0.7962
Recall 0.5372

## Ethical Considerations

This dataset used in the project is pubicly available from the Census Bureau and doesn't have any PPI or sensitive data.

## Caveats and Recommendations

This is not refined enough for production, only for personal projects and demonstration.
