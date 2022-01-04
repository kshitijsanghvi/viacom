import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import sys
import cx_Oracle

connection = cx_Oracle.connect(
    user="KSHITIJ",
    password="1",
    dsn="localhost:1521")
print("Successfully connected to Oracle Database")
cursor = connection.cursor()



#read_file = pd.read_excel("""C:\\Users\\kshit\\Downloads\\q6.xlsx""")
#read_file.to_csv ("""C:\\Users\\kshit\\Downloads\\q6.xlsx""", index = None,header=False)

d = pd.read_csv("""C:\\Users\\kshit\\Downloads\\q6.csv""",header = None)
def check(current_line):
    for i in current_line:
        if i is not np.nan:
            return True
    return False

n = len(d)
current_line_number = 0;
current_line = d.iloc[current_line_number].tolist()

for i in range(3):
    current_country = current_line[0].split()[0]    
    current_line_number += 1
    current_line = d.iloc[current_line_number].tolist()
    while current_line[0] is np.nan:
        current_line_number += 1
        current_line = d.iloc[current_line_number].tolist()
    current_line = d.iloc[current_line_number].tolist()
    date = current_line[1]
    current_line_number += 1
    current_line = d.iloc[current_line_number].tolist()
    while current_line[0] is np.nan:
        current_line_number += 1
        current_line = d.iloc[current_line_number].tolist()
    for i,v in enumerate(current_line):
        if i in range(3,18):
            current_line[i] = "C"+v
    #Table Exchange_Rate
    current_table = "EXCHANGE_RATE"
    prefix = """INSERT INTO """ + current_table +"""(Country,REPORT_DATE,""" +','.join(i.replace(" / ","") for i in current_line)+""") VALUES"""
    current_line_number += 1
    current_line = d.iloc[current_line_number].tolist()
    
    while check(current_line):
        line_size = len(current_line)
        for i,v in enumerate(current_line):
            if v is np.nan:
                current_line[i]="""''"""
                continue
            if i in [0,1,2]:
                current_line[i] = "'"+v+"'"
            elif i != line_size-1:
                v = v.replace(",",".")
                v = v.replace("%","")
                current_line[i]= v            
        if current_line[-1] != """''""":
            current_line[-1] = """TO_DATE('"""+ current_line[-1]+"""','YY-MON')"""
        suffix = """ ('""" + current_country + """',TO_DATE('""" + date + """','MM/DD/YYYY'),""" +','.join(current_line) + """);"""
        query = prefix + suffix
        print(query)
        cursor.execute(query)
        current_line_number += 1
        current_line = d.iloc[current_line_number].tolist()
    while current_line[0] is np.nan:
        current_line_number += 1
        current_line = d.iloc[current_line_number].tolist()
    for i,v in enumerate(current_line):
        if i in range(3,18):
            current_line[i] = "C"+v
    #Table Exchange_Rate
    current_table = "INFLATION_RATE"
    prefix = """INSERT INTO """ + current_table +"""(Country,REPORT_DATE,""" +','.join(i.replace(" / ","") for i in current_line)+""") VALUES"""
    current_line_number += 1
    current_line = d.iloc[current_line_number].tolist()
   
    while check(current_line):
        line_size = len(current_line)
        for i,v in enumerate(current_line):
            if v is np.nan:
                current_line[i]="""''"""
                continue
            if i in [0,1,2]:
                current_line[i] = "'"+v+"'"
            elif i != line_size-1:
                v = v.replace(",",".")
                v = v.replace("%","")
                current_line[i]= v
        if current_line[-1] != """''""":
            current_line[-1] = """TO_DATE('"""+ current_line[-1]+"""','YY-MON')"""
        suffix = """ ('""" + current_country + """',TO_DATE('""" + date + """','MM/DD/YYYY'),""" +','.join(current_line) + """);"""
        query = prefix + suffix
        print(query)
        cursor.execute(query)
        current_line_number += 1
        current_line = d.iloc[current_line_number].tolist()

    while current_line[0] is np.nan:
        current_line_number += 1
        current_line = d.iloc[current_line_number].tolist()
    for i,v in enumerate(current_line):
        if i in range(3,18):
            current_line[i] = "C"+v
    #Table Exchange_Rate
    current_table = "REAL_PRIVATE_CONSUMPTION"
    prefix = """INSERT INTO """ + current_table +"""(Country,REPORT_DATE,""" +','.join(i.replace(" / ","") for i in current_line)+""") VALUES"""
    current_line_number += 1
    current_line = d.iloc[current_line_number].tolist()
    
    while check(current_line):
        line_size = len(current_line)
        for i,v in enumerate(current_line):
            if v is np.nan:
                current_line[i]="""''"""
                continue
            if i in [0,1,2]:
                current_line[i] = "'"+v+"'"
            elif i != line_size-1:
                v = v.replace(",",".")
                v = v.replace("%","")
                current_line[i]= v
        if current_line[-1] != """''""":
            current_line[-1] = """TO_DATE('"""+ current_line[-1]+"""','YY-MON')"""
        suffix = """ ('""" + current_country + """',TO_DATE('""" + date + """','MM/DD/YYYY'),""" +','.join(current_line) + """);"""
        query = prefix + suffix
        print(query)
        cursor.execute(query)
        current_line_number += 1
        if current_line_number == len(d):
            sys.exit()
        current_line = d.iloc[current_line_number].tolist()
    while current_line_number < len(d) and current_line[0] is  np.nan:
        current_line_number += 1
        current_line = d.iloc[current_line_number].tolist()
    if current_line_number == len(d):
        break
