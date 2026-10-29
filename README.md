# Efflux susceptibility in gram-negative bacteria

Flags small molecules likely to be expelled by Escherichia coli efflux pumps, the barrier that most often strips Gram-negative antibacterials of whole-cell activity. El Zahed and colleagues screened some 314,000 compounds against an efflux-deficient tolC mutant, recovered about 4,500 growth inhibitors, 84% of which lost potency in the wild type, and separated roughly 1,070 pumped from 410 non-pumped actives. Ersilia retrained classifiers on those sets with LazyQSAR instead of serving the published SERF random forest.

This model was incorporated on 2025-12-12.Last packaged on 2026-10-29.

## Information
### Identifiers
- **Ersilia Identifier:** `eos7l5m`
- **Slug:** `efflux-gram-negative`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Antimicrobial resistance`, `Diarrheal diseases`
- **Target Organism:** `Escherichia coli`
- **Tags:** `Antimicrobial activity`, `Gram-negative bacteria`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `2`
- **Output Consistency:** `Fixed`
- **Interpretation:** Two rank scores calibrated against the Ersilia reference library of 50K compounds, where 0.65 beats 99% of it. The first is how likely Escherichia coli is to pump the compound out; the second how likely it is to inhibit growth only when efflux is disabled. Trained on a tolC-mutant screen.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| pumped_rank | float | high | Rank score of how likely Escherichia coli efflux pumps are to expel the compound. Calibrated against 50K compounds from the Ersilia reference library so that a score of 0.65 is better than 99% of them. Recommended threshold: 0.65. |
| effluxed_rank | float | high | Rank score of how likely the compound is to inhibit Escherichia coli growth only when TolC-dependent efflux is disabled. Calibrated against 50K compounds from the Ersilia reference library so that a score of 0.65 is better than 99% of them. Recommended threshold: 0.65. |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos7l5m](https://hub.docker.com/r/ersiliaos/eos7l5m)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7l5m.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7l5m.zip)

### Resource Consumption
- **Model Size (Mb):** `89`
- **Environment Size (Mb):** `7463`
- **Image Size (Mb):** `7621.45`

**Computational Performance (seconds):**
- 10 inputs: `41.46`
- 100 inputs: `35.29`
- 10000 inputs: `957.88`

### References
- **Source Code**: [https://github.com/sfrench007/serf](https://github.com/sfrench007/serf)
- **Publication**: [https://doi.org/10.1128/AAC.01925-20](https://doi.org/10.1128/AAC.01925-20)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2021`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [BSD-3-Clause](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos7l5m
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos7l5m
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
