import xlsxwriter 
import xcel_2
import xlrd



name1 = []

sheetNames = [
    "IT-A",
    "IT-B",
    "IT-C",
    "CSE-A",
    "CSE-B",
    "CSE-C",
    "ECE-A",
    "ECE-B",
    "ECE-C",
    "ECE-D"

]

tempList = []

Input_rollno =[]
Input_department =[]
Input_section = []
Input_name = []

Output_department= []
Output_rollno= []
Output_section = []
Output_name = []

Result_rollno =[]
Result_name = []
Result_department =[]
Result_section = []
Result_status =[]


IT_workbook = xlsxwriter.Workbook('./Result/IT.xlsx')
CSE_workbook = xlsxwriter.Workbook('./Result/CSE.xlsx')
ECE_workbook = xlsxwriter.Workbook('./Result/ECE.xlsx')
EEE_workbook = xlsxwriter.Workbook('./Result/EEE.xlsx')

IT_A = IT_workbook.add_worksheet("IT_A")
IT_B = IT_workbook.add_worksheet("IT_B")
IT_C = IT_workbook.add_worksheet("IT_C")

CSE_A = CSE_workbook.add_worksheet("CSE_A")
CSE_B = CSE_workbook.add_worksheet("CSE_B")
CSE_C = CSE_workbook.add_worksheet("CSE_C")

ECE_A = ECE_workbook.add_worksheet("ECE_A")
ECE_B = ECE_workbook.add_worksheet("ECE_B")
ECE_C = ECE_workbook.add_worksheet("ECE_C")

def add_data(result_name):
    if result_name in name1:
        return
    else:
        name1.append(result_name)

def read_Ouptut_list():
    for val in  name1:
        str = val.split("-")
        Output_rollno.append(str[0])
        Output_name.append(str[1])
        Output_section.append(str[3])
        Output_department.append(str[2])
        print(str)
    print(Output_rollno,Output_name,Output_department, Output_section)

def Diff(list1, list2): 
    return (list(list(set(list1)-set(list2)) + list(set(list2)-set(list1)))) 

def read_xcel_file():
    loc = "Event.xlsx" 
    # To open Workbook 
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0) 
    sheet.cell_value(0, 0) 
    n = sheet.nrows
    i=2
    while i < n :
        #print(sheet.cell_value(i, 3),sheet.cell_value(i, 4),sheet.cell_value(i, 5),sheet.cell_value(i, 6)) 
        str1 = str(sheet.cell_value(i, 0))
        value = str1.replace(".0","")
        Input_name.append(sheet.cell_value(i, 1))
        Input_department.append(sheet.cell_value(i, 2))
        print(Input_department)
        Input_section.append(sheet.cell_value(i, 3))
        Input_rollno.append(value)
        i=i+1
    print(Input_rollno,Input_department,Input_name, Input_section)
    print(Diff(Input_rollno,name1))

def compareAndWriteData():
    for i in range(len(Input_rollno)): 
        check = checkAndWriteData(Input_rollno[i])
        if check == False:
            Result_name.append(Input_name[i])
            Result_rollno.append(Input_rollno[i])
            Result_department.append(Input_department[i])
            Result_section.append(Input_section[i])
            Result_status.append("absent")


def checkAndWriteData(input_rollno):
    for i in range(len(Output_rollno)): 
        if Output_rollno[i] == input_rollno :
            Result_rollno.append(Output_rollno[i])
            Result_name.append(Output_name[i])
            Result_department.append(Output_department[i])
            Result_section.append(Output_section[i])
            Result_status.append("Present")
            return True
    return False
            

def writeDataTosheet():
    it_a_row_number =1
    it_b_row_number =1
    it_c_row_number =1

    cse_a_row_number=1
    cse_b_row_number=1
    cse_c_row_number=1

    ece_a_row_number=1
    ece_b_row_number=1
    ece_c_row_number=1

    i=0
    n = len(Result_rollno)
    print("number = ", n)
    for i in range(len(Result_rollno)):
        col =0
        print(Result_department[0])
        if Result_department[i] == "IT":
            if Result_section[i] == "A":
                sheetname ="IT_A"
                IT_A.write(it_a_row_number,col, Result_rollno[i])
                IT_A.write(it_a_row_number,col+1, Result_name[i])
                IT_A.write(it_a_row_number,col+2,Result_status[i])
                it_a_row_number = it_a_row_number+1
        if Result_department[i] == "IT":
            if Result_section[i] == "B":
                IT_B.write(it_b_row_number,col, Result_rollno[i])
                IT_B.write(it_b_row_number,col+1, Result_name[i])
                IT_B.write(it_b_row_number,col+2,Result_status[i])
                it_b_row_number = it_b_row_number + 1
        if Result_department[i] == "IT":
            if Result_section[i] == "C":
                IT_C.write(it_c_row_number,col, Result_rollno[i])
                IT_C.write(it_c_row_number,col+1, Result_name[i])
                IT_C.write(it_c_row_number,col+2,Result_status[i])
                it_c_row_number = it_c_row_number + 1
        if Result_department[i] == "CSE":
            if Result_section[i] == "A":
                CSE_A.write(cse_a_row_number,col, Result_rollno[i])
                CSE_A.write(cse_a_row_number,col+1, Result_name[i])
                CSE_A.write(cse_a_row_number,col+2,Result_status[i])
                cse_a_row_number = cse_a_row_number + 1
        if Result_department[i] == "CSE":
            if Result_section[i] == "B":
                CSE_B.write(cse_b_row_number,col, Result_rollno[i])
                CSE_B.write(cse_b_row_number,col+1, Result_name[i])
                CSE_B.write(cse_b_row_number,col+2,Result_status[i])
                cse_b_row_number = cse_b_row_number + 1
        if Result_department[i] == "CSE":
            if Result_section[i] == "C":
                CSE_C.write(cse_c_row_number,col, Result_rollno[i])
                CSE_C.write(cse_c_row_number,col+1, Result_name[i])
                CSE_C.write(cse_c_row_number,col+2,Result_status[i])
                cse_c_row_number = cse_c_row_number + 1
        if Result_department[i] == "ECE":
            if Result_section[i] == "A":
                ECE_A.write(ece_a_row_number,col, Result_rollno[i])
                ECE_A.write(ece_a_row_number,col+1, Result_name[i])
                ECE_A.write(ece_a_row_number,col+2,Result_status[i])
                ece_a_row_number = ece_a_row_number + 1
        if Result_department[i] == "ECE":
            if Result_section[i] == "B":
                ECE_B.write(ece_b_row_number,col, Result_rollno[i])
                ECE_B.write(ece_b_row_number,col+1, Result_name[i])
                ECE_B.write(ece_b_row_number,col+2,Result_status[i])
                ece_b_row_number = ece_b_row_number + 1
        if Result_department[i] == "ECE":
            if Result_section[i] == "C":
                ECE_C.write(ece_c_row_number,col, Result_rollno[i])
                ECE_C.write(ece_c_row_number,col+1, Result_name[i])
                ECE_C.write(ece_c_row_number,col+2,Result_status[i])
                ece_c_row_number = ece_c_row_number + 1

def getSheet(sheetname):
    wb2 = xlsxwriter.Workbook('Example3.xlsx')    
    if sheetname in wb2.worksheets():
        sheet = wb2.get_worksheet_by_name(sheetname)
        print("I'm here")
    else:
        sheet = wb2.add_worksheet(sheetname)
        print("I'm")
    return sheet

def write_data_to_xcel():
    workbook = xlsxwriter.Workbook('Example3.xlsx') 
    worksheet = workbook.add_worksheet("My sheet") 
    row = 0
    col = 0
    for key in students:
        row += 1
        worksheet.write(row, col,     key)
        i =1
        item = students[key]
        worksheet.write(row, col + i, item)
    workbook.close()

def worksheet_init():
    read_xcel_file()
    read_Ouptut_list()
    compareAndWriteData()
    print("final consolidate result")
    n1 = len(Result_rollno)
    for i in range(len(Result_rollno)):
        print("i= ",i)
        print("name = ",Result_name[i])
        print("rollno = ",Result_rollno[i])
        print("status = ",Result_status[i])
        print("Department = ",Result_department[i])
        print("Section = ",Result_section[i])

    writeDataTosheet()
    IT_workbook.close()
    CSE_workbook.close()
    ECE_workbook.close()