import pandas as pd


def stat_gen(acc_no):
    excel_file = pd.ExcelFile('account\{}.xlsx'.format(acc_no))
    state_sheet = excel_file.parse('statement')
    print(state_sheet)