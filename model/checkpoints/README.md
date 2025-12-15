# Model pretrained parameters

These models have been trained using the [LazyQSAR package](https://github.com/ersilia-os/lazy-qsar) v2.2.0, default parameters. The efflux subset has been constructed by subsampling the inactive class to obtain a 10% active class.
Upon 5-fold crossvalidation on train test splits (80-20%) with balanced classes, we obtain the following performance:


| **Model**       | **Data** | **Frac Actives (%)** | **AUROC ± STDev** |
|-----------------|----------|------------------|-------------------|
| pumped   | 1475   | 72.33   |  0.887 ± 0.014 |
| efflux   | 37640   | 10   |  0.88 ± 0.005 |
