# import xlsxwriter
# book = xlsxwriter.Workbook('/Users/Andarisa/Desktop/Purwadhika/Modul 2/Kurs_BI.xlsx')
# sheet = book.add_worksheet('Data')

# sheet.write(0,0,"Mata Uang")
# sheet.write(0,1,"Satuan Uang")
# sheet.write(0,2,"Kurs Jual")
# sheet.write(0,3,"Kurs Beli")

# row = 1
# col = 0
Var = soup.find_all('td')

# for i,data in enumerate(Var[10:135]):
#     if data.text == '\n\n':
#         col = 0
#         row+=1
#         continue

#     sheet.write(row,col,data.text)
#     col+=1

# book.close()