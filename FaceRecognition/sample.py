if Result_department[i] == "IT":
            if Result_section[i] == "A":
                sheetname ="IT_A"
                wb.write(row,col, Result_rollno[i])
                wb.write(row,col+1, Result_name[i])
                wb.write(row,col+2,Result_status[i])
