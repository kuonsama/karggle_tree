# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 13:24:55 2017

@author: kuoncat
"""
import pymysql as sql

class sqlhelp(object):
    def __init__(self,user,pwd,db,table,ip):
        self.__user = user
        self.__pwd = pwd
        self.__db = db
        self.__table = table
        self.__host = ip
    def conec(self):
        con = sql.connect(user=self.__user,password = self.__pwd,host = self.__host,database = self.__db)
        return con
    def data_to(self):
        sql = 'select * from %s'%self.__table
        con = self.conec()
        cons = con.cursor()
        cons.execute(sql)
        
        try:
            data = cons.fetchall()
            con.close()
            return data
        except:
            con.rollback()
            print('wrong,rollback!')
            con.close()
        
        
            