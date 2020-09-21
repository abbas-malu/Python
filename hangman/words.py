import random
import xlrd
def word():
    wb = xlrd.open_workbook("wordlist.xlsx") 
    sheet = wb.sheet_by_index(0) 
    rnd_no = random.randrange(0,854)
    wrd = sheet.cell_value(rnd_no,0)
    return wrd

    
