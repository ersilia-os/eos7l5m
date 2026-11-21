# Fit folder: efflux-gram-negative (eos7l5m)

This folder holds the data, code and results needed to rebuild the model. It is stored with
[eosvc](https://github.com/ersilia-os/eosvc) in the **public** bucket; only this README is
tracked in git.

## Data processing

`src/data_analysis.py` standardises both source files. The pumped task uses `data/elzahed_pumped_vs_nonpumped_standard.csv`. For the efflux task it keeps all efflux-dependent actives and a random sample of inactives (seed 42) so that actives make up 10% of `data/elzahed_efflux_dependent_subset.csv`.

## Model building

`src/01_fit_oof.py` builds one LazyQSAR 3.9.3 classifier per task, in slow mode. For each task
it runs five-fold stratified out-of-fold (OOF) cross-validation (seed 42), so every compound
gets one prediction from a model that never saw it. It writes the OOF predictions and metrics to
`results/`, then trains the final model on all compounds into `model/checkpoints/<task>/`.
`src/02_performance.py` plots the OOF ROC curve and the OOF rank of actives and inactives per
task, and collects all metrics in `results/oof_metrics.json`.

```bash
cd src
OMP_NUM_THREADS=1 python 01_fit_oof.py        # or one task: python 01_fit_oof.py pump
python 02_performance.py
```

| Task | Output column | Training file | Compounds | Actives | OOF AUROC | Descriptors in final model |
|---|---|---|---|---|---|---|
| `pump` | `pumped_rank` | `data/elzahed_pumped_vs_nonpumped_standard.csv` | 1,465 | 1,061 | 0.923 | chemeleon, clamp, morgan |
| `efflux` | `effluxed_rank` | `data/elzahed_efflux_dependent_subset.csv` | 37,470 | 3,747 | 0.916 | chemeleon, clamp, rdkit |
