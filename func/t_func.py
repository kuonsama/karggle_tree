# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 10:43:23 2017

@author: kuoncat
"""
import numpy as np
import pandas as pd
import math as ma
def lis_in(data):
    x=[]
    for row in data:
        x.append(row)
    return x

def mat(data):
    x = np.mat(data)
    return x

def da_num(data):
    x = len(data)
    return x

def da_df(data):
    x = pd.DataFrame(data)
    return x

def num_data_char(data,col):
    return len(data[col].unique())

def cont_data_char(data,col):
    return data[col].unique()



def calc_data_gini(data,col):
   
    x = data[col].value_counts()
    s = x.sum()
    return (1-(np.square(x/s)).sum())

def spilt_data(data,col):
    list_data = {}
    cont = cont_data_char(data,col)
    for i in cont:
        list_data[str(i)]=data[(data[col]==i)]#(data.query(('%s == %s'%(col,str(i)))))
    return list_data

def get_data_cols(data):
    return list(data.columns.values) 
   
def calc_meta_gini(meta_data,col):
     list_data = []
     list_num = [] 
     num=0
     gini = 0
     for i  in meta_data.keys():
         list_data.append(calc_data_gini(meta_data[i],col))
         list_num.append(meta_data[i]['id'].count())
         num += list_num[-1]
     arry_data = np.array(list_data)
     arry_num  = np.array(list_num)
     #return arry_num
     gini = (arry_data*(arry_num/num)).sum()  
     return gini
 
def create_tree(data,tar_col,col_i_list,tar_list,rank):
         if col_i_list ==[]:return ''
         rank+=1
         meta_i_list = []
         gini_list =[]
         data_1 =[]
         tar_dic={}
         if type(data)==dict:
             data_1 = data.values()
         else:
             data_1.append(data)
           
    
         for sets in data_1:
             for co_l in col_i_list:
                 meta_i_list.append(spilt_data(sets,co_l))
               
             for meta in meta_i_list:
                 gini_list.append(calc_meta_gini(meta,tar_col))
            
             if col_i_list!=[]:      
                 ii = gini_list.index(min(gini_list))
                 tar_list.append(col_i_list[ii]+str(rank))
                
                
                 data = meta_i_list[ii]
                 col_i_list.remove(col_i_list[ii])
    #             return col_i_list
                 for key in data.keys():
                   tar_dic[key] = create_tree(data,tar_col,col_i_list,tar_list,rank)
                 return tar_dic,tar_list
                 #return create_tree(data,tar_col,col_i_list,tar_list,rank)
 
          

     
     
     
     