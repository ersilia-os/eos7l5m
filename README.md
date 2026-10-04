# Efflux susceptibility in gram-negative bacteria

Reports both whether a compound inhibits Escherichia coli and whether efflux pumps expel it, two properties that together determine if antibacterial activity survives in an intact cell. El Zahed and colleagues screened small-molecule inhibitors against wild-type and efflux-deficient strains, letting intrinsic potency be separated from susceptibility to export, and related the difference to physicochemical character. A compound can therefore be genuinely active yet ineffective because it is pumped out.

This model was incorporated on 2025-12-12.Last packaged on 2026-07-06.

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
- **Interpretation:** Probability of Escherichia coli growth inhibition and probability of susceptibility to efflux.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| pumped_proba | float | high | Probability of the molecule being pumped out of E.coli |
| effluxed_proba | float | high | Probability of the molecule being effluxed out of E.coli |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos7l5m](https://hub.docker.com/r/ersiliaos/eos7l5m)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7l5m.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7l5m.zip)

### Resource Consumption
- **Model Size (Mb):** `47`
- **Environment Size (Mb):** `1924`
- **Image Size (Mb):** `2043.59`

**Computational Performance (seconds):**
- 10 inputs: `41.25`
- 100 inputs: `38.59`
- 10000 inputs: `882.16`

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
