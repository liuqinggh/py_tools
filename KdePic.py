# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 15:25:15 2016

@author: user
"""
import pyodbc
import pandas as pd
import numpy as np
from pandas.io.sql import read_frame
import matplotlib.font_manager as fm
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


myfont = fm.FontProperties(fname='C:/Windows/Fonts/msyhbd.ttf', size = 18)

class Get_DBData: 
    def get_txt(self, pth):
        txt = open(pth).readlines()
        sql = []
        for line in txt:
            sql.extend(line.split('\n'))
        sql = str(' '.join(sql)).decode('utf-8').encode('gbk')
        return sql
        
    def get_verdb_db(self):
        conn = pyodbc.connect("DSN=Verticaodbc;UID=XXX;PWD=XXX")
        cursor = conn.cursor()
        return cursor
    
    def get_data(self, sql):
        cursor = self.get_verdb_db()
        cursor.execute(sql)
        res = cursor.fetchall()  # 获取数据
        title = [i[0].decode('gb2312') for i in cursor.description]    # 获取列名
        data_res = np.array(res)
        df = pd.DataFrame(data_res, columns = title)  # 将数据装入pandas 的 DataFrame 进行处理
        return df 

    def get_pic(self, df, i):
        line = df.astype('float64', raise_on_error = False)
        if line.shape[0] > 50:
            line_std = line.std()
            line_mean = line.mean()
            sig2 = line_mean + 2*line_std
            sig2_ = line_mean - 2*line_std
            sns.kdeplot(line.values, shade=True)
            plt.axvline(x=sig2_, label = u'left_2σ %2.1f'%(sig2_), color = 'g')
            plt.axvline(x=sig2, label = u'right_2σ %2.1f'%(sig2), color = 'r')
            plt.title(i, fontproperties=myfont)
            plt.legend(loc = 'upper right')
            plt.savefig(r'C:\Users\biuser\Desktop\job\hgq_pic\\'+ i +'.png')
            plt.close()
        else:
            pass
        
        
"""
if __name__ == '__main__': 
    oper = Get_DBData()
    sql = oper.get_txt(sql_pth_test)
    df = oper.get_data(sql)
    oper.get_pic(df, 'SKU')
"""