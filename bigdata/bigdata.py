#-*- coding:utf-8 -*-

from pyhive import hive

def export_excel(sql,filename):
    hql='select * from {}'.format(sql)
    print(hql)

if __name__ == "__main__":
    export_excel('a','c')
