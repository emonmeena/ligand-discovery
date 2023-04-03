import pandas as pd

search_term = "NLR"

df = pd.read_excel('TargetIDXTargetName.xlsx')


for ind in df.index:
    curr_lin = df['TargetName'][ind]
    print(curr_lin)
    if search_term in curr_lin:
        print(curr_lin, df['TargetID'][ind])
        
