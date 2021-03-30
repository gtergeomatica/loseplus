# Descrizione

Script per importare i dati dai WS di TEAS su geoDB Lose+

## Dipendenze 

sudo pip3 install psycopg2


## Note di installazione 

Le specifiche dei WS di TEAS sono illustrate nel file *Lose+Interfaccia_WS_CodiciADR_v1_3.pdf*

Va creato file accessorio credenziali.py contiene credenziali di accesso a DB e WS TEAS

```
ip='localhost'
db='XXXXXXX'
user='XXXXXXX'
	@@ -15,5 +15,5 @@ port='5432'
ws_user='XXXXXXX'
ws_pwd='XXXXXXX'
```

## Inserimento a crontab per esecuzione pianificata

Aggiunta riga sul crontab che esegue ogni ora XX:10' lo script per per i 7 giorni precedenti

```
10 *    * * *  omdusr   /usr/bin/python3 /home/omdusr/loseplus/ws_telecamere.py  > /dev/null 2>&1
```

