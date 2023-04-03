targets_for_disease = [
        {
            "TargetName": "Tyrosine-protein kinase ABL1 (ABL)"
        },
        {
            "TargetName": "Fms-like tyrosine kinase 3 (FLT-3)"
        },
        {
            "TargetName": "Fibroblast growth factor receptor 1 (FGFR1)"
        },
        {
            "TargetName": "Polo-like kinase 1 (PLK1)"
        },
        {
            "TargetName": "Interleukin 3 receptor alpha (IL3RA)"
        },
        {
            "TargetName": "Myeloid inhibitory C-type lectin-like receptor (CD371)"
        },
        {
            "TargetName": "MHC class I NK cell receptor 2DL2 (CD158b1)"
        },
        {
            "TargetName": "MHC class I NK cell receptor 2DL3 (CD158b2)"
        },
        {
            "TargetName": "MHC class I NK cell receptor 2DL1 (CD158A)"
        },
        {
            "TargetName": "Translationally-controlled tumor protein (TPT1)"
        },
        {
            "TargetName": "Myeloid cell surface antigen CD33 (CD33)"
        },
        {
            "TargetName": "DNA replication (DNA repli)"
        },
        {
            "TargetName": "Kinesin-like protein KIF11 (KIF11)"
        },
        {
            "TargetName": "Cell differentiation (CD)"
        },
        {
            "TargetName": "Bromodomain-containing protein 2 (BRD2)"
        },
        {
            "TargetName": "Lysine-specific histone demethylase 1 (LSD)"
        },
        {
            "TargetName": "Neural cell adhesion molecule 1 (NCAM1)"
        },
        {
            "TargetName": "Prominin-1 (PROM1)"
        },
        {
            "TargetName": "Tau protein aggregation (TauA)"
        },
        {
            "TargetName": "TAR DNA binding protein 43 (TARDBP)"
        },
        {
            "TargetName": "Multidrug resistance protein 3 (ABCB4)"
        },
        {
            "TargetName": "Oxalosuccinate decarboxylase (IDH1)"
        },
        {
            "TargetName": "Alpha-ketoglutarate dehydrogenase (OGDH)"
        },
        {
            "TargetName": "Hematopoietic progenitor cell antigen CD34 (CD34)"
        },
        {
            "TargetName": "Ephrin type-A receptor 3 (EPHA3)"
        },
        {
            "TargetName": "Calcium-activated potassium channel KCa4.2 (KCNT2)"
        },
        {
            "TargetName": "Calcium-activated potassium channel KCa4.1 (KCNT1)"
        },
        {
            "TargetName": "Inward rectifier potassium channel Kir3.4 (KCNJ5)"
        },
        {
            "TargetName": "Mutated oxalosuccinate decarboxylase (mIDH1)"
        },
        {
            "TargetName": "Puromycin-sensitive aminopeptidase (NPEPPS)"
        },
        {
            "TargetName": "Aminopeptidase (AMP)"
        },
        {
            "TargetName": "RAS-like protein KIR (GEM)"
        },
        {
            "TargetName": "Lymphocyte activation antigen 4F2 (SLC3A2)"
        },
        {
            "TargetName": "Membrane glycoprotein OX2 (CD200)"
        },
        {
            "TargetName": "Gastric carcinoma-associated antigen MG7 (MG7)"
        },
        {
            "TargetName": "Small ubiquitin-related modifier (SUMO)"
        },
        {
            "TargetName": "Platelet factor 4 (PF4)"
        },
        {
            "TargetName": "Leukocyte immunoglobulin-like receptor B4 (LILRB4)"
        },
        {
            "TargetName": "Cyclin-dependent kinase 19 (CDK19)"
        },
        {
            "TargetName": "Bromodomain-containing protein 9 (BRD9)"
        }
    ]


listvar = []
listind = []
i=1

for target in targets_for_disease:
    listvar.append(target["TargetName"])
    listind.append(i)
    i+=1

# print(listind)    


import pandas as pd

# dataframe Name and Age columns
df = pd.DataFrame({'id': listind, 'name': listvar})

print(df.head())

df.to_csv('target_prots_aml.csv')

# Create a Pandas Excel writer using XlsxWriter as the engine.
# writer = pd.to_c('aml_target_proteins.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
# df.to_excel(writer, sheet_name='Sheet1', index=False)

# Close the Pandas Excel writer and output the Excel file.
# writer.close()