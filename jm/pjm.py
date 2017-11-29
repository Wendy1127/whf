# -*- coding:utf-8 -*-

import xlrd
import xlwt
import os
import hashlib
import pandas as pd
import openpyxl
dir_path = os.path.dirname(__file__)
excle_path = os.path.join(dir_path, '360z.xlsx')
res_path= os.path.join(dir_path, '360z_res1.xlsx')
wb = xlwt.Workbook()
ws = wb.add_sheet('res')
def to_hash(st):
    m = hashlib.sha256()
    m.update(st)
    sha = m.hexdigest()
    return sha
def read_to_excle():
    phone=[]
    id_card = []
    df = pd.read_excel(excle_path)
    for i in df['mobile']:
        a = to_hash(str(int(i)))
        phone.append(a)
    for j in df['id_card']:
        b = to_hash(str(j))
        id_card.append(b)
    df['mobile'] = phone
    df['id_card'] = id_card
    df.to_excel(res_path,encoding='utf-8')
    
if __name__ == "__main__":
    read_to_excle()
	11111111111111
    

    
