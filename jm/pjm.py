# -*- coding:utf-8 -*-

import xlrd
import xlwt
import os
import hashlib
import md5
import pandas as pd
dir_path = os.path.dirname(__file__)
excle_path = os.path.join(dir_path, '360z.xlsx')
res_path= os.path.join(dir_path, '360z_res.xlsx')
wb = xlwt.Workbook()
ws = wb.add_sheet('res')
def to_hash(st):
    m = hashlib.sha256()
    m.update(st)
    sha = m.hexdigest()
    return sha

def to_md5(st):
    import hashlib
    m = hashlib.md5()   
    m.update(st)
    return m.hexdigest()

def read_to_excle():
    phone=[]
    id_card = []
    df = pd.read_excel(excle_path)
    for i in df['mobile']:
        a = to_md5(str(int(i)))
        phone.append(a)
    for j in df['id_card']:
        b = to_md5(str(j))
        id_card.append(b)
    df['mobile'] = phone
    df['id_card'] = id_card
    df.to_excel(res_path,encoding='utf-8')
    
if __name__ == "__main__":
    read_to_excle()
    

    
