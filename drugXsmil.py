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

with open("drug_smil.txt") as file:

    row_drugXdisease = 0

    workbook = xlsxwriter.Workbook('23.xlsx')
    worksheet = workbook.add_worksheet()


    col = 0
    headings = ["DrugUID", "DrugSMIL"]

    for item in headings:
        worksheet.write(row_drugXdisease, col, item)
        col +=1

    row_drugXdisease +=1

    
    DrugUID = "D00AAU"
    DrugSMIL = "CCC(C1=CC(=CC=C1)O)C(CC)C2=CC(=CC=C2)O"

    for line_ in file:
        splits = line_.split()

        if splits == []:
            
            DrugUID = ""
            DrugSMIL = ""
            continue

        # print(splits)  

        l1 = splits[0]
        l2 = splits[1]

        DrugUID = l1
        DrugSMIL = ""
        if l2  == "DRUGSMIL":
           DrugSMIL = splits[2]
           content = [DrugUID, DrugSMIL]
           print(content)

           col = 0

           for item in content:
                worksheet.write(row_drugXdisease, col, item)
                col +=1

           row_drugXdisease +=1
           

        # if l1 == DrugUID:
        #    DrugUID = l1
        #    print(DrugUID, DrugSMIL)
        #    content = [DrugUID, DrugSMIL]
        #    col = 0

        #    for item in content:
        #         worksheet.write(row_drugXdisease, col, item)
        #         col +=1

        #    row_drugXdisease +=1




        # if l2 == "DRUGSMIL":
        #     DrugSMIL = splits[2]


        #     col = 0

        #     for item in content:
        #         worksheet.write(row_drugXdisease, col, item)
        #         col +=1

        # l1 = splits[0]
        # l2 = splits[1]

       
        # DiseaseName = ""
        
        # if l1 == "":
            # DrugUID = l2.strip()

        # if l1 == "DRUGNAME":
        #     DrugName = l2.strip()

        # if l1 == "INDICATI":
        #     DiseaseName = l2.strip()
        #     DiseaseID = splits[4]
        #     ClinicalStatus = splits[6].strip()

        #     # print(DrugUID, DrugName, DiseaseName, DiseaseID, ClinicalStatus)
        #     content = [DrugUID, DrugName, DiseaseName, DiseaseID, ClinicalStatus]

        #     col = 0

        #     for item in content:
        #         worksheet.write(row_drugXdisease, col, item)
        #         col +=1

        #     row_drugXdisease +=1

        # l2 = l2.strip()


        # print(l1, l2)
        
        # print(splits)

    workbook.close()
