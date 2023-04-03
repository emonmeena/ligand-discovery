import xlsxwriter

# import sqlite3

# conn = sqlite3.connect('test.db')

# print ("Opened database successfully")

# conn.execute('''CREATE TABLE COMPANY
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL);''')

# print ("Table created successfully")

# conn.close()

class DiseaseTable:
  def __init__(self, m, p, n):
    self.diseaseName = m
    self.icd11 = p
    self.phase = n
    self.drugs = []

class DrugTable:
  def __init__(self, m, p, n):
    self.drugName = m
    self.ttddruid = p
    self.targets = []

class TargetTable:
  def __init__(self, m, p):
    self.model = m
    self.price = p        

with open("drug_to_disease.txt") as file:
    DrugUID = ""
    DrugName = ""

    row_drugXdisease = 0

    workbook = xlsxwriter.Workbook('DrugXDiseaseMapping.xlsx')
    worksheet = workbook.add_worksheet()


    col = 0
    headings = ["DrugUID", "DrugName", "DiseaseName", "DiseaseID", "ClinicalStatus", "DrugSMIL"]

    for item in headings:
        worksheet.write(row_drugXdisease, col, item)
        col +=1

    row_drugXdisease +=1



    for line_ in file:
        if line_=="\t\n":
            DrugUID = ""
            DrugName = ""
            continue
        splits = line_.split("|")

        l1 = splits[0]
        l2 = splits[1]

       
        DiseaseName = ""
        
        if l1 == "TTDDRUID":
            DrugUID = l2.strip()

        if l1 == "DRUGNAME":
            DrugName = l2.strip()

        if l1 == "INDICATI":
            DiseaseName = l2.strip()
            DiseaseID = splits[4]
            ClinicalStatus = splits[6].strip()

            # print(DrugUID, DrugName, DiseaseName, DiseaseID, ClinicalStatus)
            content = [DrugUID, DrugName, DiseaseName, DiseaseID, ClinicalStatus]

            col = 0

            for item in content:
                worksheet.write(row_drugXdisease, col, item)
                col +=1

            row_drugXdisease +=1

        # l2 = l2.strip()


        # print(l1, l2)
        
        # print(splits)

    workbook.close()
