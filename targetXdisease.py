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

with open("target_to_disease.txt") as file:
    DrugUID = ""
    DrugName = ""

    row_drugXdisease = 0

    workbook = xlsxwriter.Workbook('TargetXDiseaseMapping.xlsx')
    worksheet = workbook.add_worksheet()


    col = 0
    headings = ["TargetID", "TargetName"]

    for item in headings:
        worksheet.write(row_drugXdisease, col, item)
        col +=1

    row_drugXdisease +=1



    for line_ in file:
        splits = line_.split("|")

        # print(line_)

        if line_=="\t\t\n":
            
            DrugUID = ""
            DrugName = ""
            continue
        


        l1 = splits[1]
        l2 = splits[2]

       
        DiseaseName = ""
        
        if l1 == "TARGETID":
            DrugUID = l2.strip()

        if l1 == "TARGNAME":
            DrugName = l2.strip()
            content = [DrugUID, DrugName]   
            col = 0

            for item in content:
                worksheet.write(row_drugXdisease, col, item)
                col +=1 

            row_drugXdisease +=1    

            # print(content)
        

        if l1 == "INDICATI":
            continue

        

        #     DiseaseName = l2.strip()
        #     DiseaseID = splits[4]
        #     ClinicalStatus = splits[6].strip()

        #     # print(DrugUID, DrugName, DiseaseName, DiseaseID, ClinicalStatus)
            # content = [DrugUID, DrugName, DiseaseName, DiseaseID, ClinicalStatus]

        #     col = 0

        #     for item in content:
        #         worksheet.write(row_drugXdisease, col, item)
        #         col +=1


        # l2 = l2.strip()


        # print(l1, l2)
        
        # print(splits)

    workbook.close()
