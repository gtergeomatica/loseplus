#!/usr/bin/env python

"""ws_telecamere.py: script python che:
    - legge i WS di TEAS 
    - trasferisce i dati sul DB PostgresSQL/PostGIS."""

__author__      = "Roberto Marzocchi"
__copyright__   = "Gter srl"

import os    # standard library
import sys

import requests  # 3rd party packages
import json

import psycopg2
from credenziali import *
conn = psycopg2.connect("dbname={} user={} password={} host={}".format(db, user, pwd, ip))




# recupero il percorso allo script python 
spath=os.path.dirname(os.path.realpath(__file__)) 
# la sottocartella log deve esserci e possibilmente inseritanel file .gitignore 

# libreria per gestione log
import logging
# inserire riferimento a data e schema 


logging.basicConfig(     
    format='%(asctime)s\t%(levelname)s\t%(message)s',
    filemode='w', # overwrite or append 
    filename='{}/log/lettura_WS_TEAS.log'.format(spath),  # nome file (commentandolo viene stampato a schermo
    level=logging.DEBUG
    )


from datetime import date, timedelta

oggi=date.today().strftime('%Y-%m-%d')
settimana_prima=(date.today() - timedelta(days=7)).strftime('%Y-%m-%d')

logging.debug(oggi)
logging.debug(settimana_prima)

url0='https://losews.comune.genova.it/IPViewVisualAnalytics/lose.asmx/transits'
url= '{}?date_start={}&time_start=000000&date_end={}&time_end=235959&gates=25;26;27;28;29;30;31;32'.format(url0, settimana_prima, oggi)

  
r = requests.get(url, auth=(ws_user, ws_pwd))
data=r.json()
#print(data)
# Open a cursor to perform database operations
cur = conn.cursor()
k=0
kk=0
for i in data['data']:
    #print(i)
    data_ora=str(i['data_ora'])
    gate=str(i['id'])
    targa=str(i['targa'])
    if i['tipo_veicolo']=='':
        tipo_veicolo='nd'
    else: 
        tipo_veicolo=str(i['tipo_veicolo'])
    #print(tipo_veicolo)
    descr=str(i['descrizione_merce_pericolosa'])
    #exit
    query1=u'INSERT INTO terra.transiti (data_ora, id_gate, targa, tipo_veicolo, descrizione_merce_pericolosa) VALUES(%s,%s , %s, %s, %s);'
    vars1=data_ora, gate, targa, tipo_veicolo, descr
    try:
        #print(query1)
        cur.execute(query1,vars1)
        conn.commit()
        k+=1
    except Exception as e1:
        query2=u'UPDATE terra.transiti SET tipo_veicolo=%s, descrizione_merce_pericolosa=%s WHERE data_ora=%s AND id_gate=%s AND targa=%s;'
        vars2=tipo_veicolo, descr, data_ora, gate, targa
        conn.rollback()
        try:
            #cur = conn.cursor()
            cur.execute(query2, vars2)
            conn.commit()
            kk+=1
        except Exception as e2:
            logging.error(e2)
            logging.error(query2)


cur.close()
conn.close()
    

# qua c'è da mettere la parte in psycopg2
logging.info('Ho finito. Inseriti {} nuovi transiti, aggiornati {} sui 7 giorni precedenti'.format(k, kk))
#print(r.status_code)
#print(r.headers['content-type'])

#print('***********************************')


#print(r.encoding)
#print(r.json())