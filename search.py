import pandas as pd

query = "Acute myeloid leukemia"

df = pd.read_excel('DrugXDiseaseMapping.xlsx')
df2 = pd.read_excel('TargetXDrug.xlsx')
df3 = pd.read_excel('TargetIDXTargetName.xlsx')

# df = pd.DataFrame(df, columns=['DrugUID', 'DrugName', 
#                                  'DiseaseName', 'DiseaseID', "ClinicalStatus"])

Drugs = []
Targets = []

for ind in df.index:
    # if df['DiseaseName'][ind] == query:

        DrugUID = df['DrugUID'][ind]
        for ind2 in df2.index:
            # print(DrugUID)
            if df2['DrugID'][ind2] == DrugUID:
                for ind3 in df3.index:

                    if df3['TargetID'][ind3] == df2['TargetID'][ind2]:

                        DrugUID = df['DrugUID'][ind]
                        print("DiseaseName:", df['DiseaseName'][ind], "\tDrugUID:", df['DrugUID'][ind], "\tDrugName:", df['DrugName'][ind])
                        print("TargetName:", df3['TargetName'][ind3])
        
        print("\n")
        # Drugs.append({"DrugUID": df['DrugUID'][ind], "DrugName": df['DrugName'][ind]})
        # print(df['DiseaseName'][ind], df['DrugName'][ind])

# print("Drugs for the Disease:", query)

# print(df)
