import pandas as pd

query = "D00ACL"

df = pd.read_excel('23.xlsx')

# df = pd.DataFrame(df, columns=['DrugUID', 'DrugName', 
#                                  'DiseaseName', 'DiseaseID', "ClinicalStatus"])

Drugs = []
Targets = []

for ind in df.index:
    # if df['DiseaseName'][ind] == query:

        DrugUID = df['DrugUID'][ind]
        if DrugUID == query:
                print(df['DrugSMIL'][ind])
                break
        
        # print("\n")
        # Drugs.append({"DrugUID": df['DrugUID'][ind], "DrugName": df['DrugName'][ind]})
        # print(df['DiseaseName'][ind], df['DrugName'][ind])

# print("Drugs for the Disease:", query)

# print(df)
