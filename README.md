# Efflux susceptibility of small molecule inhibitors in gram-negative bacteria

Actives in efflux-compromised Escherichia coli were compared with wild-type strains to estimate efflux susceptibility of small molecules. An initial screen of over 300000 molecules was performed in an efflux-deficient (tolC mutant) strain. About 4500 hits (E.coli growth inhibitors) were identified, of which ca. 3, 780 were efflux-dependent (meaning they do not inhibit the WT). In addition, from the 4500 subset, two more refined datasets were created classifying 1061 molecules as pumped out and 404 as non-pumped.



## Information
### Identifiers
- **Ersilia Identifier:** `eos7l5m`
- **Slug:** `efflux-susceptibility-gram-negative`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Antimicrobial resistance`
- **Target Organism:** `Escherichia coli`, `Gram-negative bacteria`
- **Tags:** `Antimicrobial activity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `2`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of the compound being effluxed out of E.coli cells.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| pumped_proba | float | high | Probability of the molecule being pumped out of E.coli |
| effluxed_proba | float | high | Probability of the molecule being effluxed out of E.coli |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`

### Resource Consumption


### References
- **Source Code**: [https://github.com/sfrench007/serf](https://github.com/sfrench007/serf)
- **Publication**: [https://journals.asm.org/doi/10.1128/aac.01925-20](https://journals.asm.org/doi/10.1128/aac.01925-20)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2025`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-or-later](LICENSE) license.

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
