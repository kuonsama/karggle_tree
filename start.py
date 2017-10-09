# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 10:43:00 2017

@author: kuoncat
"""
from func import t_func
from sqlinput import sqlin
import pylab as p
import numpy as np

'''
inp = sqlin.sqlhelp(user='kuon',pwd='340881',db='world',ip='localhost',table='train')
data = inp.data_to()


x= t_func.lis_in(data)
ori_mat = t_func.mat(x)
num = t_func.da_num(data)

da_df = t_func.da_df(ori_mat)
'''
rank = 0
tar_list = []
import pandas as pd
from pandas import Series
import sqlalchemy as sa
engine = sa.create_engine('mysql+pymysql://kuon:340881@localhost/world')


txt = pd.read_sql('train',engine)
u=txt['survived'].value_counts()

ent = t_func.calc_data_gini(txt,'survived')
#print (ent)
txt1 = txt.drop(['name','ticket','cabin','embarked','age','parch'],axis =1)
txt2 = txt1.fillna({'age':28})
c = t_func.get_data_cols(txt2)
c.remove('survived')
c.remove('id')
#print (txt2[txt2['sex']=='male'])
res = t_func.create_tree(txt2,'survived',c,tar_list,rank)
print (res)