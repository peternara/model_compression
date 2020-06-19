# -*- coding: utf-8 -*-
"""Configurations for naive lottery ticket hypothesis.

- Author: Curt-Park
- Email: jwpark@jmarple.ai
"""

import os

config = {
    "SEED": 777,
    "AUG_TRAIN": "simple_augment_train_cifar100",
    "AUG_TEST": "simple_augment_test_cifar100",
    "DATASET": "CIFAR100",
    "MODEL_NAME": "densenet",
    "MODEL_PARAMS": dict(depth=100, num_classes=100, growthRate=12, compressionRate=2),
    "BATCH_SIZE": 128,
    "START_LR": 1e-5,
    "LR": 0.1,
    "MOMENTUM": 0.9,
    "WEIGHT_DECAY": 1e-4,
    "WARMUP_EPOCHS": 10,
    "EPOCHS": 200,
    "N_PRUNING_ITER": 20,
    "PRUNE_AMOUNT": 0.2,
    "STORE_PARAM_BEFORE": 0,  # final weights: EPOCHS
    "PRUNE_START_FROM": 0,
    "N_WORKERS": os.cpu_count(),
}