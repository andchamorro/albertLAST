---
language:
- en
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
- recall
- precision
- f1
model-index:
- name: trc2_5x_mutireads
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE TRC2
      type: glue
      args: trc2
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.996826171875
    - name: Recall
      type: recall
      value: 0.998046875
    - name: Precision
      type: precision
      value: 0.9956161714564052
    - name: F1
      type: f1
      value: 0.9968300414533041
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# trc2_5x_mutireads

This model is a fine-tuned version of [run/albert_k15_v138648_ml512_multireads](https://huggingface.co/run/albert_k15_v138648_ml512_multireads) on the GLUE TRC2 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0265
- Accuracy: 0.9968
- Recall: 0.9980
- Precision: 0.9956
- F1: 0.9968
- Combined Score: 0.9968

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 8.64491338167939e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | Recall | Precision | F1     | Combined Score |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|:---------:|:------:|:--------------:|
| 0.0451        | 1.0   | 7680  | 0.0290          | 0.9932   | 0.9961 | 0.9903    | 0.9932 | 0.9932         |
| 0.0295        | 2.0   | 15360 | 0.0379          | 0.9932   | 0.9912 | 0.9951    | 0.9932 | 0.9932         |
| 0.0143        | 3.0   | 23040 | 0.0169          | 0.9951   | 0.9976 | 0.9927    | 0.9951 | 0.9951         |
| 0.006         | 4.0   | 30720 | 0.0206          | 0.9958   | 0.9985 | 0.9932    | 0.9959 | 0.9959         |
| 0.0           | 5.0   | 38400 | 0.0265          | 0.9968   | 0.9980 | 0.9956    | 0.9968 | 0.9968         |


### Framework versions

- Transformers 4.23.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.4.0
- Tokenizers 0.13.2
