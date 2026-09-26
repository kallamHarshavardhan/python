import openpyxl

inv.file = openpyxl.load_workbook("inventory.xlsx")
product_list = inv.file["Sheet1"]

product_per_supplier = {}

print(product_list.max_row)