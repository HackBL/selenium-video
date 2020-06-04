import xlrd
import xlsxwriter
import os


def readLinks(): # All products links
	links = []

	loc = ("./midea_goods_list2.xlsx") # Read Excel

	wb = xlrd.open_workbook(loc)
	sheet = wb.sheet_by_index(0)
	sheet.cell_value(0, 0)

	for i in range(1, sheet.nrows):
		links.append(sheet.cell_value(i, 4))

	return links

for i in range(len(readLinks())): # Execute all links
	# print(readLinks()[i])
	os.system("Python3 Video.py " + readLinks()[i])




