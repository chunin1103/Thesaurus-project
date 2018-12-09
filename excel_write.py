import xlsxwriter
from crawl_thesaurus import google_api, tu_dong_nghia
from word import ini_word
from crawl_data_Onelook import ds_tu_dong_nghia, gg_translate_free

# Setting up sheet
workbook = xlsxwriter.Workbook('demo1.xlsx')
worksheet = workbook.add_worksheet('Trans Free vs Paid')
bold   = workbook.add_format({'bold': True})
center = workbook.add_format({'align': 'center'})

worksheet.write('A1', ini_word, bold)

# Google Api
worksheet.set_column('A:A', 30)
worksheet.set_column('B:B', 9.5)
worksheet.set_column('C:C', 10)
worksheet.write_column('A3', google_api)
worksheet.write('C3', 'Total')
worksheet.write('C4', '=COUNTA(B3:B25)')
worksheet.write('C6', 'Probability')
worksheet.write('C7', '=COUNTIF(B3:B15, TRUE)/C4')

# GG Api Free
worksheet.set_column('D:D', 30)
worksheet.write_column('D3', tu_dong_nghia)
worksheet.set_column('E:E', 9.5)
worksheet.set_column('F:F', 10)
worksheet.write('F3', 'Total')
worksheet.write('F4', '=COUNTA(E3:E25)')
worksheet.write('F6', 'Probability')
worksheet.write('F7', '=COUNTIF(E3:E15, TRUE)/F4')

# Onelook gg api legit
worksheet.set_column('G:G', 30)
worksheet.write_column('G3', gg_translate_free)
worksheet.set_column('H:H', 9.5)
worksheet.set_column('I:I', 10)
worksheet.write('I3', 'Total')
worksheet.write('I4', '=COUNTA(H3:H25)')
worksheet.write('I6', 'Probability')
worksheet.write('I7', '=COUNTIF(H3:H15, TRUE)/I4')

# Onelook gg api free
worksheet.set_column('L:L', 30)
worksheet.write_column('L3', ds_tu_dong_nghia)
worksheet.set_column('M:M', 9.5)
worksheet.set_column('N:N', 10)
worksheet.write('N3', 'Total')
worksheet.write('N4', '=COUNTA(H3:H25)')
worksheet.write('N6', 'Probability')
worksheet.write('N7', '=COUNTIF(M3:M15, TRUE)/N4')


worksheet = workbook.add_worksheet('Dicts compare')