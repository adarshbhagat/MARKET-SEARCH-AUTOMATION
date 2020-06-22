import numpy as np
import pandas as pd
import subprocess
import difflib
df=pd.read_csv("C:\\Users\\KIIT\\Desktop\\MARKET\\COMPANY_NAME_MAPPING.csv")
while(1):
    x=input("enter the name of companies:-").split(',',)
    company_names=list(df['company name'])
    for i in x:
        m=difflib.get_close_matches(i,company_names)
        #print(company_names)
        if len(m)==0:
            continue
        #print(m[0])
        t=df[df['company name']==m[0]]
        #print(t['nfs'].values[0])
        
        
        #provide the location of the web browser
        subprocess.Popen(['C:\\Program Files\\Mozilla Firefox\\firefox.exe',t['nfs'].values[0]])
