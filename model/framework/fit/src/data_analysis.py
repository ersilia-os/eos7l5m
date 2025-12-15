import os
import pandas as pd
from rdkit import Chem
from standardiser import standardise
import numpy as np

def standardise_smiles(smiles):
    st_smiles = []
    for smi in smiles:
        if smi is None:
            st_smi = np.nan
            st_smiles += [st_smi]
            continue
        smi = str(smi)
        smi = smi.strip()
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            st_smi = np.nan
            st_smiles += [st_smi]
            continue
        try:
            std_mol = standardise.run(mol)
            st_smi = Chem.MolToSmiles(std_mol, canonical=True)
            st_smiles += [st_smi]
        except:
            st_smi = Chem.MolToSmiles(mol, canonical=True)
            st_smiles += [st_smi]
        if std_mol is None:
            st_smi = Chem.MolToSmiles(mol, canonical=True)
            st_smiles += [st_smi]
            continue
    return st_smiles

root = os.path.dirname(os.path.abspath(__file__))

pumped = pd.read_csv(os.path.join(root, "..","data", "elzahed_pumped_vs_nonpumped.csv"))

pumped["st_smiles"] = standardise_smiles(pumped["smiles"].tolist())
pumped=pumped[~pumped["st_smiles"].isna()]
pumped.drop(columns = ["smiles"], inplace=True)

print("Total mols pumped data:", len(pumped))
print("Pumped:", len(pumped[pumped["pumped"]==1]), "Non pumped:", len(pumped[pumped["pumped"]==0]))
print("Active proportion:",  len(pumped[pumped["pumped"]==1])/len(pumped))
pumped.to_csv(os.path.join(root, "..","data", "elzahed_pumped_vs_nonpumped_standard.csv"), index=False)

efflux = pd.read_csv(os.path.join(root, "..","data", "elzahed_efflux_dependent_actives_vs_inactives.csv"))
efflux["st_smiles"] = standardise_smiles(efflux["smiles"].tolist())
efflux=efflux[~efflux["st_smiles"].isna()]
efflux.drop(columns = ["smiles"], inplace=True)
print("Total mols Efflux data:", len(efflux))
print("Effluxed:", len(efflux[efflux["efflux_dependent_active"]==1]), "Non effluxed:", len(efflux[efflux["efflux_dependent_active"]==0]))
print("Active proportion:",  len(efflux[efflux["efflux_dependent_active"]==1])/len(efflux))

efflux_negs = efflux[efflux["efflux_dependent_active"]==0]
efflux_pos = efflux[efflux["efflux_dependent_active"]==1]
random_negs = int((len(efflux_pos)/0.1)-len(efflux_pos))
print(random_negs)

efflux_neg_sub = efflux_negs.sample(
    n=random_negs,
    random_state=42
)
efflux_sub = pd.concat(
    [efflux_pos, efflux_neg_sub],
    ignore_index=True
)
efflux_sub = efflux_sub.sample(frac=1, random_state=42).reset_index(drop=True)

print("Subset size:", len(efflux_sub))
print("Final active proportion:", len(efflux_sub[efflux_sub["efflux_dependent_active"] == 1]) / len(efflux_sub))

efflux_sub.to_csv(os.path.join(root, "..","data", "elzahed_efflux_dependent_subset.csv"), index=False)