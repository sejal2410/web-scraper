{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww35340\viewh21540\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import re\
import numpy as np\
from selenium import webdriver\
from bs4 import BeautifulSoup\
import pandas as pd\
import matplotlib.pyplot as plt\
import seaborn as sns\
def get_data():  \
    headers = \{"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",\
               "Accept-Encoding":"gzip, deflate, br", \
               "Accept":"*/*", \
               "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"\}\
\
    r = requests.get('https://www.amazon.in/s?rh=n%3A1375425031&fs=true', headers=headers)#, proxies=proxies)\
    content = r.content\
    soup = BeautifulSoup(content)\
\
    alls = []\
    for d in soup.findAll('div', attrs=\{'class':'a-section a-spacing-small s-padding-left-small s-padding-right-small'\}):\
        name = d.find('span', attrs=\{'class':'a-size-base-plus a-color-base a-text-normal'\})\
        users_rated = d.find('span', attrs=\{'class':'a-icon-alt'\})\
        price = d.find('span', attrs=\{'class':'a-price-whole'\}) \
        #print(users_rated.text)\
\
        all1=[]\
\
        if name is not None:\
            #print(n[0]['alt'])\
            all1.append(name.text)\
        else:\
            all1.append("unknown-product")\
        if users_rated is not None:\
            #print(price.text)\
            all1.append(users_rated.text.split(" ")[0])\
        else:\
            all1.append('0')     \
\
        if price is not None:\
            #print(price.text)\
            all1.append(price.text)\
        else:\
            all1.append('0')\
        alls.append(all1)    \
    return alls\
l = get_data()\
df = pd.DataFrame(l, columns=["product","rating","price"])\
df['brand']=df["product"].apply(lambda x:re.split("\\s|(?<!\\d)[-.](?!\\d)", str(x))[0])\
df.rating = pd.to_numeric(df.rating, errors='coerce')\
df['rating'] = np.floor(df['rating'])\
print(df)\
sns.catplot(x='brand', y='price', data=df, linewidth = 0.5, \
             aspect = 2.5)\
\
plt.show()}