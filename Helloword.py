import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from io import BytesIO
from pathlib import Path
import altair as alt
import datetime as dt
import xlsxwriter




st.sidebar.image(r"C:\Users\Utente\Desktop\Mattia\logo_questlab.png", use_container_width=True, width=5)
# Creazione delle Calendario (dal 10 novembre 2024 al 31 dicembre 2024)
start_Calendario = dt.datetime(2025, 4, 14)  # Inizio 10 novembre
end_Calendario = dt.datetime(2025, 5, 10)  # Fine 31 dicembre 2024

# Generare tutte le Calendario
Calendarios = pd.date_range(start=start_Calendario, end=end_Calendario, freq='D')  # Frequenza 'D' per ogni giorno


# Creare una lista di attività con i colori associati
#activities = ['LM','CV','TB','ER','TC','PM','PT1']
activities = ['ER','PM']
Legenda = ['Partenza','Field aperto','Solleciti', 'Solleciti deboli', 'INVIO MAIL SOLLECITO', 'Cambio data', 'Elaborazioni', 'Scarico dati']
colors = {
    'Partenza':'green',
    'Field aperto': '#8FE388',
    'Solleciti': 'blue',
    'Solleciti deboli': '#648CD5',
    'Invio mail sollecito': '#4F359B',  # Blu scuro per "Invio mail sollecito"
    'Cambio data': '#D54718',  # Verde chiaro per "Cambio data"
    'Elaborazioni': '#F3B700',  # Giallo scuro per "Elaborazioni"
    'Scarico dati': 'red'  # Rosso per "Scarico dati"
}

# Creare un elenco vuoto per i dati
data = []

# Esempio di dati da inserire manualmente per ciascun giorno
manual_entries = [
    {'Calendario': dt.datetime(2025, 4, 11),  'Indagini': 'ER',   'Legenda': 'Partenza'             },
    {'Calendario': dt.datetime(2025, 4, 14),  'Indagini': 'ER',   'Legenda': 'Field aperto'     },
    {'Calendario': dt.datetime(2025, 4, 15),  'Indagini': 'ER',   'Legenda': 'Field aperto'     },
    {'Calendario': dt.datetime(2025, 4, 16),  'Indagini': 'ER',   'Legenda': 'Solleciti'     },
    {'Calendario': dt.datetime(2025, 4, 16),  'Indagini': 'ER',   'Legenda': 'Invio mail sollecito'     },
    {'Calendario': dt.datetime(2025, 4, 17),  'Indagini': 'ER',   'Legenda': 'Solleciti'     },
    {'Calendario': dt.datetime(2025, 4, 18),   'Indagini': 'ER',   'Legenda': 'Solleciti deboli'            },
    {'Calendario': dt.datetime(2025, 4, 21),   'Indagini': 'ER',   'Legenda': 'Field aperto'            },
    {'Calendario': dt.datetime(2025, 4, 22),   'Indagini': 'ER',   'Legenda': 'Invio mail sollecito'            },
    {'Calendario': dt.datetime(2025, 4, 23),   'Indagini': 'ER',   'Legenda': 'Solleciti'            },
    {'Calendario': dt.datetime(2025, 4, 24),   'Indagini': 'ER',   'Legenda': 'Solleciti' },
    {'Calendario': dt.datetime(2025, 4, 25),   'Indagini': 'ER',   'Legenda': 'Field aperto'            },
    {'Calendario': dt.datetime(2025, 4, 28),  'Indagini': 'ER',   'Legenda': 'Solleciti'     },
    {'Calendario': dt.datetime(2025, 4, 29),  'Indagini': 'ER',   'Legenda': 'Solleciti'     },
    {'Calendario': dt.datetime(2025, 4, 29),  'Indagini': 'ER',   'Legenda': 'Cambio data'     },
    {'Calendario': dt.datetime(2025, 4, 30),  'Indagini': 'ER',   'Legenda': 'Solleciti'          },
    {'Calendario': dt.datetime(2025, 5, 1),  'Indagini': 'ER',   'Legenda': 'Field aperto'     },
    {'Calendario': dt.datetime(2025, 5, 2),  'Indagini': 'ER',   'Legenda': 'Field aperto'     },
    {'Calendario': dt.datetime(2025, 5, 5),  'Indagini': 'ER',   'Legenda': 'Solleciti'     },
    {'Calendario': dt.datetime(2025, 5, 6),  'Indagini': 'ER',   'Legenda': 'Scarico dati'     },
    {'Calendario': dt.datetime(2025, 4, 14),  'Indagini': 'PM',   'Legenda': 'Partenza'     },
    {'Calendario': dt.datetime(2025, 4, 15),  'Indagini': 'PM',   'Legenda': 'Field aperto'     },
    {'Calendario': dt.datetime(2025, 4, 16),  'Indagini': 'PM',   'Legenda': 'Field aperto'     },
    {'Calendario': dt.datetime(2025, 4, 17),  'Indagini': 'PM',   'Legenda': 'Solleciti'     },
    {'Calendario': dt.datetime(2025, 4, 18),   'Indagini': 'PM',   'Legenda': 'Solleciti deboli'            },
    {'Calendario': dt.datetime(2025, 4, 21),   'Indagini': 'PM',   'Legenda': 'Field aperto'            },
    {'Calendario': dt.datetime(2025, 4, 22),   'Indagini': 'PM',   'Legenda': 'Solleciti'            },
    {'Calendario': dt.datetime(2025, 4, 22),   'Indagini': 'PM',   'Legenda': 'Invio mail sollecito'            },
    {'Calendario': dt.datetime(2025, 4, 23),   'Indagini': 'PM',   'Legenda': 'Solleciti'            },
    {'Calendario': dt.datetime(2025, 4, 24),   'Indagini': 'PM',   'Legenda': 'Solleciti' },
    {'Calendario': dt.datetime(2025, 4, 25),   'Indagini': 'PM',   'Legenda': 'Field aperto'            },
    {'Calendario': dt.datetime(2025, 4, 28),  'Indagini': 'PM',   'Legenda': 'Solleciti'     },
    {'Calendario': dt.datetime(2025, 4, 29),  'Indagini': 'PM',   'Legenda': 'Solleciti'     },
    {'Calendario': dt.datetime(2025, 4, 29),  'Indagini': 'PM',   'Legenda': 'Cambio data'     },
    {'Calendario': dt.datetime(2025, 4, 30),  'Indagini': 'PM',   'Legenda': 'Solleciti'          },
    {'Calendario': dt.datetime(2025, 5, 1),  'Indagini': 'PM',   'Legenda': 'Field aperto'     },
    {'Calendario': dt.datetime(2025, 5, 2),  'Indagini': 'PM',   'Legenda': 'Field aperto'     },
    {'Calendario': dt.datetime(2025, 5, 5),  'Indagini': 'PM',   'Legenda': 'Solleciti'     },
    {'Calendario': dt.datetime(2025, 5, 6),  'Indagini': 'PM',   'Legenda': 'Solleciti'     },
    {'Calendario': dt.datetime(2025, 5, 6),  'Indagini': 'PM',   'Legenda': 'Invio mail sollecito'     },
    {'Calendario': dt.datetime(2025, 5, 7),  'Indagini': 'PM',   'Legenda': 'Solleciti'     },
    {'Calendario': dt.datetime(2025, 5, 8),  'Indagini': 'PM',   'Legenda': 'Solleciti'     },
    {'Calendario': dt.datetime(2025, 5, 9),  'Indagini': 'PM',   'Legenda': 'Scarico dati'     },
]

# Aggiungere i dati manualmente
for entry in manual_entries:
    selected_Calendario = entry['Calendario']
    selected_Indagini = entry['Indagini']
    selected_Legenda = entry['Legenda']
    
    # Verifica se la data è la data odierna
    is_today = selected_Calendario.date() == dt.datetime.today().date()
    
    # Aggiungi i dati al DataFrame
    data.append({
        'Calendario': selected_Calendario,
        'Indagini': selected_Indagini,
        'Legenda': selected_Legenda,
        'color': colors[selected_Legenda],
        'is_today': is_today  # Aggiungi colonna che verifica se la data è oggi
    })
# Creare il DataFrame con i dati aggiunti
df = pd.DataFrame(data)

chart = alt.Chart(df).mark_bar(size=15).encode(
    x='Calendario:T',  # L'asse X conterrà le date del Calendario (come variabile temporale)
    y='Indagini:N',  # L'asse Y conterrà le attività (BS e CX)
    color=alt.Color('Legenda:N', 
                    scale=alt.Scale(domain=['Partenza','Field aperto', 'Solleciti','Solleciti deboli', 'Invio mail sollecito', 'Cambio data', 'Elaborazioni', 'Scarico dati'], 
                                    range=['green','#8FE388', 'blue','#648CD5', '#4F359B', '#D54718', '#F3B700', 'red']),
                    legend=alt.Legend(orient='top', title='Legenda', labelFontSize=12)),  # Posiziona la legenda sopra
    stroke=alt.condition(
        alt.datum.is_today == True,  # Condizione per la data odierna
        alt.value('black'),  # Bordo nero
        alt.value('transparent')  # Nessun bordo per le altre Calendario
    ),
     strokeWidth=alt.condition(
        alt.datum.is_today == True,  # Condizione per la data odierna
        alt.value(4),  # Spessore del bordo più spesso per oggi
        alt.value(1)  # Spessore del bordo normale per le altre date
    ),
    tooltip=['Calendario:T', 'Indagini:N', 'Legenda:N']  # Aggiungere il tooltip per maggiore chiarezza
).properties(
    width=10000,  # Larghezza del grafico
    height=400  # Altezza del grafico
)

# Visualizzare il grafico in Streamlit

st.title("Gestione Indagini")
st.markdown("**CRONOGRAMMA**", unsafe_allow_html=True)
st.altair_chart(chart, use_container_width=True)


###############################################################################################################################################################################

# Filtrare solo le righe che hanno "Solleciti" o "Solleciti deboli" nella colonna 'Legenda'
solleciti_df = df[df['Legenda'].isin(['Solleciti', 'Solleciti deboli'])]

# Creare una colonna per il tipo di sollecito (Solleciti o Solleciti deboli)
solleciti_df['Tipo Sollecito'] = solleciti_df['Legenda'].apply(lambda x: 'Solleciti' if x == 'Solleciti' else 'Solleciti deboli')

# Raggruppare per 'Indagini' e 'Tipo Sollecito' e contare le occorrenze
solleciti_count = solleciti_df.groupby(['Indagini', 'Tipo Sollecito']).size().unstack(fill_value=0)

# Aggiungere le colonne per le ore obiettivo e ore fatte in base all'indagine (AGGIUNGERE A MANO SE CI SONO ALTRE INDAGINI)
solleciti_count['Ore Obiettivo'] = solleciti_count.index.map({'ER': 266,'PM':200})
solleciti_count['Ore Fatte'] = solleciti_count.index.map({'ER': 0,'PM':0})

# Visualizzare la tabella in Streamlit
#st.write("ALLOCAZIONE GESTIONE INDAGINI", solleciti_count)



# Filtrare i dati solo per l'indagine "LM"
solleciti_bs = solleciti_count.loc['ER']
# Calcolare il totale per "Solleciti" e "Solleciti deboli" per l'indagine "LM"
totale_bs = solleciti_bs[['Solleciti', 'Solleciti deboli']].sum()

# Filtrare i dati solo per l'indagine "LM"
solleciti_ta = solleciti_count.loc['PM']
# Calcolare il totale per "Solleciti" e "Solleciti deboli" per l'indagine "LM"
totale_ta = solleciti_ta[['Solleciti', 'Solleciti deboli']].sum()

# Filtrare i dati solo per l'indagine "LM"
#solleciti_lm = solleciti_count.loc['LM']
# Calcolare il totale per "Solleciti" e "Solleciti deboli" per l'indagine "LM"
#totale_lm = solleciti_lm[['Solleciti', 'Solleciti deboli']].sum()

# Filtrare i dati solo per l'indagine "CV"
#solleciti_cv = solleciti_count.loc['CV']
# Calcolare il totale per "Solleciti" e "Solleciti deboli" per l'indagine "CV"
#totale_cv = solleciti_cv[['Solleciti', 'Solleciti deboli']].sum()

# Filtrare i dati solo per l'indagine "TB"
#solleciti_tb = solleciti_count.loc['TB']
# Calcolare il totale per "Solleciti" e "Solleciti deboli" per l'indagine "TB"
#totale_tb = solleciti_tb[['Solleciti', 'Solleciti deboli']].sum()
#
## Filtrare i dati solo per l'indagine "HE"
#solleciti_he = solleciti_count.loc['HE']
## Calcolare il totale per "Solleciti" e "Solleciti deboli" per l'indagine "HE"
#totale_he = solleciti_he[['Solleciti', 'Solleciti deboli']].sum()
#
## Filtrare i dati solo per l'indagine "ER"
#solleciti_er = solleciti_count.loc['ER']
## Calcolare il totale per "Solleciti" e "Solleciti deboli" per l'indagine "ER"
#totale_er = solleciti_er[['Solleciti', 'Solleciti deboli']].sum()
#
## Filtrare i dati solo per l'indagine "TC"
#solleciti_tc = solleciti_count.loc['TC']
## Calcolare il totale per "Solleciti" e "Solleciti deboli" per l'indagine "TC"
#totale_tc = solleciti_tc[['Solleciti', 'Solleciti deboli']].sum()
#
## Filtrare i dati solo per l'indagine "PM"
#solleciti_pm = solleciti_count.loc['PM']
## Calcolare il totale per "Solleciti" e "Solleciti deboli" per l'indagine "PM"
#totale_pm = solleciti_pm[['Solleciti', 'Solleciti deboli']].sum()
#
## Filtrare i dati solo per l'indagine "PT1"
#solleciti_pt1 = solleciti_count.loc['PT1']
## Calcolare il totale per "Solleciti" e "Solleciti deboli" per l'indagine "PM"
#totale_pt1 = solleciti_pt1[['Solleciti', 'Solleciti deboli']].sum()


#################################################################################################################################################################################




# Creare una tabella vuota con le righe per i giorni e le colonne per le indagini
calendar_dates = pd.date_range(start=start_Calendario, end=end_Calendario, freq='D')

# Aggiungere una colonna per le ore obiettivo e le ore fatte in base all'indagine
#ore_obiettivo = {'LM': 468, 'CV': 69, 'TB': 340,'HE': 100,'ER': 284,'TC': 4,'PM': 216,'PT1': 80}
#ore_fatte = {'LM': 0, 'CV': 0, 'TB': 0,'HE': 0,'ER': 0,'TC': 0,'PM': 0, 'PT1':0}

ore_obiettivo = {'ER': 266,'PM':200}
ore_fatte = {'ER': 0,'PM':0}

#n_solleciti_tot= {'LM': totale_lm, 'CV': totale_cv, 'TB': totale_tb,'HE': totale_he,'ER': totale_er,'TC': totale_tc,'PM': totale_pm, 'PT1': totale_pt1}
#n_solleciti= {'LM': solleciti_count.loc['LM', 'Solleciti'], 'CV': solleciti_count.loc['CV', 'Solleciti'],
#              'TB': solleciti_count.loc['TB', 'Solleciti'],'HE': solleciti_count.loc['HE', 'Solleciti'],'ER': solleciti_count.loc['ER', 'Solleciti'],
#              'TC': solleciti_count.loc['TC', 'Solleciti'],'PM': solleciti_count.loc['PM', 'Solleciti'], 'PT1': solleciti_count.loc['PT1', 'Solleciti']} 
#n_solleciti_deboli= {'LM': solleciti_count.loc['LM', 'Solleciti deboli'], 'CV': solleciti_count.loc['CV', 'Solleciti deboli'],
#              'TB': solleciti_count.loc['TB', 'Solleciti deboli'],'HE': solleciti_count.loc['HE', 'Solleciti deboli'],'ER': solleciti_count.loc['ER', 'Solleciti deboli'],
#              'TC': solleciti_count.loc['TC', 'Solleciti deboli'],'PM': solleciti_count.loc['PM', 'Solleciti deboli'], 'PT1': solleciti_count.loc['PT1', 'Solleciti deboli']} 

n_solleciti_tot= {'ER': totale_bs,'PM': totale_ta}
n_solleciti= {'ER': solleciti_count.loc['ER', 'Solleciti'],'PM': solleciti_count.loc['PM', 'Solleciti'],} 
n_solleciti_deboli= {'ER': solleciti_count.loc['ER', 'Solleciti deboli'],'PM': solleciti_count.loc['PM', 'Solleciti deboli']}

# Creare una lista per memorizzare i risultati
results_1 = []

# Iterare attraverso le date del calendario
for date in calendar_dates:
    row = {'Giorno': date.strftime('%d-%m')}  # Formattare la data come giorno-mese
    
    for indagine in ['ER','PM']:
        # Filtrare i dati per la data e l'indagine corrente
        daily_data = df[(df['Calendario'] == date) & (df['Indagini'] == indagine)]
        
        # Conteggiare i solleciti e i solleciti deboli
        solleciti = len(daily_data[daily_data['Legenda'] == 'Solleciti'])
        solleciti_deboli = len(daily_data[daily_data['Legenda'] == 'Solleciti deboli'])
         
     
        # Sommare i solleciti e i solleciti deboli per calcolare il totale
        
        #if indagine == 'LM':
        #    p1 = 0.40
        #else:
        p1 = 0.50
        # Calcolare il risultato
        if solleciti_deboli > 0:
            result = ((((ore_obiettivo[indagine] - ore_fatte[indagine]) / 7.5) / ((n_solleciti_deboli[indagine] * p1) + n_solleciti[indagine]) * p1))
        elif solleciti > 0:
            result = ((((ore_obiettivo[indagine] - ore_fatte[indagine]) / 7.5) / ((n_solleciti_deboli[indagine] * p1) + n_solleciti[indagine])))
        else:
            result = 0
        
        # Aggiungere il risultato con una sola cifra decimale
        row[indagine] = round(result, 1)
    
    # Aggiungere la riga alla lista dei risultati
    results_1.append(row)

# Creare un DataFrame dalla lista di risultati
results_1_df = pd.DataFrame(results_1)

# Calcolare i totali per ogni riga (somma di 'BS' e 'CX')
results_1_df['Totale'] = results_1_df[['ER','PM']].sum(axis=1)

# Impostare la colonna 'Giorno' come indice
results_1_df.set_index('Giorno', inplace=True)

# Visualizzare la tabella in Streamlit
#st.write("ALLOCAZIONE PROPORZIONALE", results_df)



############################################################################################################################################################
import math
def arrotonda_personalizzato(val):
  """
  Arrotonda un numero secondo le seguenti regole:
  - Numeri di mezzo (0.5, 1.5, ...) rimangono invariati.
  - Numeri minori di 0.5 vengono arrotondati per difetto.
  - Numeri maggiori di 0.5 vengono arrotondati per eccesso.

  Args:
    val: Il numero da arrotondare.

  Returns:
    Il numero arrotondato secondo le regole specificate.
  """

  if val % 1 == 0.5:
    return val  # Lascia invariato il numero di mezzo
  elif val % 1 < 0.5:
    return math.floor(val)  # Arrotonda per difetto
  else:
    return math.ceil(val) 

def arrotonda_a_mezzo(numero):
  """
  Arrotonda un numero al valore di mezzo più vicino se è compreso tra 0.4 e 0.6.

  Args:
    numero: Il numero da arrotondare.

  Returns:
    Il numero arrotondato al valore di mezzo più vicino, oppure il numero originale.
  """

  parte_decimale = numero % 1

  if 0.35 <= parte_decimale <= 0.65:
      # Se il numero è compreso tra 0.4 e 0.6, arrotonda al mezzo più vicino
      return math.floor(numero) + 0.5
  else:
      # Altrimenti, restituisci il numero originale
      return numero


# Creare una tabella vuota con le righe per i giorni e le colonne per le indagini
calendar_dates = pd.date_range(start=start_Calendario, end=end_Calendario, freq='D')

# Aggiungere una colonna per le ore obiettivo e le ore fatte in base all'indagine
ore_obiettivo = {'ER': 266, 'PM':200}
ore_fatte = {'ER': 0,'PM':0}
n_solleciti_tot= {'ER': totale_bs,'PM': totale_ta}
n_solleciti= {'ER': solleciti_count.loc['ER', 'Solleciti'], 'PM': solleciti_count.loc['PM', 'Solleciti']} 
n_solleciti_deboli= {'ER': solleciti_count.loc['ER', 'Solleciti deboli'],'PM': solleciti_count.loc['PM', 'Solleciti deboli']} 


# Creare una lista per memorizzare i risultati
results = []

# Iterare attraverso le date del calendario
for date in calendar_dates:
    row = {'Giorno': date.strftime('%d-%m')}  # Formattare la data come giorno-mese
    
    for indagine in ['ER','PM']:
        # Filtrare i dati per la data e l'indagine corrente
        daily_data = df[(df['Calendario'] == date) & (df['Indagini'] == indagine)]
        
        # Conteggiare i solleciti e i solleciti deboli
        solleciti = len(daily_data[daily_data['Legenda'] == 'Solleciti'])
        solleciti_deboli = len(daily_data[daily_data['Legenda'] == 'Solleciti deboli'])
         
     
        # Sommare i solleciti e i solleciti deboli per calcolare il totale
        
        #if indagine == 'LM':
        #    p1 = 0.40
        #else:
        p1 = 0.50
        # Calcolare il risultato
        if solleciti_deboli > 0:
            result = ((((ore_obiettivo[indagine] - ore_fatte[indagine]) / 7.5) / ((n_solleciti_deboli[indagine] * p1) + n_solleciti[indagine]) * p1))
        elif solleciti > 0:
            result = ((((ore_obiettivo[indagine] - ore_fatte[indagine]) / 7.5) / ((n_solleciti_deboli[indagine] * p1) + n_solleciti[indagine])))
        else:
            result = 0
        

        numero=arrotonda_a_mezzo(result)
        # Aggiungere il risultato con una sola cifra decimale
        row[indagine] = arrotonda_personalizzato(numero)
    
    # Aggiungere la riga alla lista dei risultati
    results.append(row)

# Creare un DataFrame dalla lista di risultati
results_df = pd.DataFrame(results)

# Calcolare i totali per ogni riga (somma di 'BS' e 'CX')
results_df['Totale'] = results_df[['ER','PM']].sum(axis=1)

# Impostare la colonna 'Giorno' come indice
results_df.set_index('Giorno', inplace=True)

# Visualizzare la tabella in Streamlit
#st.write("ALLOCAZIONE EFFETTIVA", results_df)

############################################################################################################################################################

# Lista di rilevatori (quelli disponibili)
rilevatori = [
    "PaoloT", "Stefania", "Michela", "MkIvan", "Francesco", "Francesca", 
    "Debora", "DeborahC", "Cristina", "NelloS", "Pietro", "Chiara", 
    "Valentina", "FrancescaF", "Luigi", "Marina", "Simone"
]

# Disponibilità rilev (True = disponibile, False = non disponibile) 14/1
disponibilita = {
    "PaoloT":      {"Mattina": True, "Pomeriggio":  False},
    "Stefania":    {"Mattina": True, "Pomeriggio":  True },
    "Michela":     {"Mattina": True, "Pomeriggio":  True },
    "MkIvan":      {"Mattina": True, "Pomeriggio":  True },
    "Francesco":   {"Mattina": True, "Pomeriggio":  True },
    "Francesca":   {"Mattina": True, "Pomeriggio":  False},
    "Debora":      {"Mattina": False, "Pomeriggio":  True },
    "DeborahC":    {"Mattina": True, "Pomeriggio":  True },
    "Cristina":    {"Mattina": True, "Pomeriggio": True },
    "NelloS":      {"Mattina": True, "Pomeriggio":  True},
    "Pietro":      {"Mattina": True, "Pomeriggio": True },
    "Chiara":      {"Mattina": True, "Pomeriggio":  False },
    "Valentina":   {"Mattina": True, "Pomeriggio": False},
    "FrancescaF":  {"Mattina": True, "Pomeriggio":  True },
    "Luigi":       {"Mattina": True, "Pomeriggio":  True},
    "Marina":      {"Mattina": False, "Pomeriggio": True },
    "Simone":      {"Mattina": True, "Pomeriggio":  True }
}
disp = "ok"  # ATTENZIONE: SE HAI AGGIORNATO LA TABELLA DELLE DISPONIBILITA' ALLORA disp='ok', altrimenti disp='no'
data_aggior_disp = "15-01" # ATTENZIONE: SE HAI AGGIORNATO LA TABELLA DELLE DISPONIBILITA' ALLORA data_aggior_disp = "giorno-mese" (ad es. 11-01)

from datetime import datetime, timedelta

# Ottieni la data di domani
domani = datetime.now() + timedelta(days=1)
# Formatta la data come "giorno-mese"
data_domani = domani.strftime("%d-%m")
# Impostare la data specifica (26 novembre)
#specific_date = "14-01"
specific_date=data_domani


# Esegui il reset dell'indice (presumibilmente hai già un DataFrame 'results_df' da un file o da altro)
results_df = results_df.reset_index()
specific_row = results_df[results_df['Giorno'] == specific_date].iloc[0]

# Calcolare i rilevatori necessari per ciascuna indagine, usando la funzione di arrotondamento personalizzata
rilevatori_needed_bs = (specific_row['ER'])*2
rilevatori_needed_ta = (specific_row['PM'])*2


# Funzione per assegnare i rilevatori in base alla disponibilità, considerando già quelli assegnati
def assign_rilevatori_per_disponibilita(rilevatori_needed, disponibilita, tipo_indagine, rilevatori_assegnati_mattina, rilevatori_assegnati_pomeriggio):
    # Lista di rilevatori disponibili per mattina e pomeriggio, che non siano già stati assegnati
    disponibili_mattina = [r for r, v in disponibilita.items() if v["Mattina"] and r not in rilevatori_assegnati_mattina]
    disponibili_pomeriggio = [r for r, v in disponibilita.items() if v["Pomeriggio"] and r not in rilevatori_assegnati_pomeriggio]
    
      # Calcolare la quantità di rilevatori da assegnare alla mattina e al pomeriggio
    half_needed = math.ceil(rilevatori_needed) // 2  # Arrotonda all'intero superiore e divide per 2
    rest_needed = math.ceil(rilevatori_needed) - half_needed

    # Se la parte decimale di rilevatori_needed era 0.5, aggiungi un rilevatore al pomeriggio
    if rilevatori_needed - math.floor(rilevatori_needed) == 0.5:
        rest_needed += 1

    # Assegna i rilevatori alla mattina
    rilevatori_mattina = disponibili_mattina[:half_needed]

    # Assegna i rilevatori al pomeriggio
    rilevatori_pomeriggio = disponibili_pomeriggio[:rest_needed]
    
    # Restituisci i rilevatori assegnati per mattina e pomeriggio
    return rilevatori_mattina, rilevatori_pomeriggio


# Variabili per tenere traccia dei rilevatori già assegnati
rilevatori_assegnati_mattina = []
rilevatori_assegnati_pomeriggio = []


# Assegnare i rilevatori per LM, CV, TB, HE, ER, TC e PM (dove sono richiesti)
bs_morning, bs_afternoon = assign_rilevatori_per_disponibilita(rilevatori_needed_bs, disponibilita, "ER", rilevatori_assegnati_mattina, rilevatori_assegnati_pomeriggio)
rilevatori_assegnati_mattina.extend(bs_morning)
rilevatori_assegnati_pomeriggio.extend(bs_afternoon)



# Assegnare i rilevatori per LM, CV, TB, HE, ER, TC e PM (dove sono richiesti)
ta_morning, ta_afternoon = assign_rilevatori_per_disponibilita(rilevatori_needed_ta, disponibilita, "PM", rilevatori_assegnati_mattina, rilevatori_assegnati_pomeriggio)
rilevatori_assegnati_mattina.extend(ta_morning)
rilevatori_assegnati_pomeriggio.extend(ta_afternoon)





# Creazione della tabella con le assegnazioni
rilevatori_table = []

# Assegna l'indagine (BS o CX) alla mattina e pomeriggio
for rilevatore in rilevatori:
    row = {
        'Rilevatore': rilevatore,
        'Mattina': '',
        'Pomeriggio': ''
    }

    if rilevatore in bs_morning:
        row['Mattina'] = 'ER solleciti'
    if rilevatore in bs_afternoon:
        row['Pomeriggio'] = 'ER solleciti'   
    if rilevatore in ta_morning:
        row['Mattina'] = 'PM solleciti'
    if rilevatore in ta_afternoon:
        row['Pomeriggio'] = 'PM solleciti' 
    
    rilevatori_table.append(row)

# Convertire in DataFrame
rilevatori_df = pd.DataFrame(rilevatori_table)

# Funzione per colorare le celle in base al valore
def color_cells(val):
    color = ''
    if val == 'BS solleciti':
        color = 'background-color: #DB504A'  # Colore per 'LM'   
    if val == 'LM solleciti':
        color = 'background-color: #DB504A'  # Colore per 'LM'
    if val == 'CV solleciti':
        color = 'background-color: #AF9B46'  # Colore per 'CV'
    if val == 'TB solleciti':
        color = 'background-color: #44CF6C'  # Colore per 'TB'
    if val == 'HE solleciti':
        color = 'background-color: #57467B'  # Colore per 'HE'
    if val == 'ER solleciti':
        color = 'background-color: #FFA5A5'  # Colore per 'ER'
    if val == 'TC solleciti':
        color = 'background-color: #EE6123'  # Colore per 'TC'
    if val == 'PM solleciti': 
        color = 'background-color: #85C7F2'  # Colore per 'PM'
    if val == 'PT1 solleciti': 
        color = 'background-color: #613F75'  # Colore per 'PM'
    if val == 'TA solleciti': 
        color = 'background-color: #fb8500'  # Colore per 'TA'
    return color 

# Applicare il colore alle celle
styled_df = rilevatori_df.style.applymap(color_cells, subset=['Mattina', 'Pomeriggio'])

# Visualizzare la tabella con colori
#st.write(f"BACHECA {specific_date}", styled_df, use_container_width=True)


import io

# Funzione per esportare in Excel
def export_to_excel(df):
    # Crea un buffer in memoria
    output = io.BytesIO()
    # Scrivi il DataFrame in Excel usando 'XlsxWriter' come motore
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name=f'Bacheca {specific_date}')
        # Non è necessario chiamare writer.save(), si gestisce automaticamente
    # Ritorna i dati in formato binario
    return output.getvalue()

# Aggiungere un bottone per il download
excel_data = export_to_excel(rilevatori_df)


# Creare due colonne per affiancare le tabelle
#col1, col2 = st.columns(2)
col1, col2 = st.columns([4, 4])  
# Colonna 1: Visualizza la tabella "ALLOCAZIONE EFFETTIVA"
with col1:
    st.markdown("**ALLOCAZIONE GESTIONE INDAGINI**", unsafe_allow_html=True)
    st.write(solleciti_count)

# Colonna 2: Visualizza la tabella "BACHECA" (con colori)
with col2:
    st.markdown("**ALLOCAZIONE PROPORZIONALE**", unsafe_allow_html=True)
    st.write(results_1_df)
    

# Creare due colonne per affiancare le tabelle
#col1, col2 = st.columns(2)
col3, col4 = st.columns([4, 4])  
# Colonna 1: Visualizza la tabella "ALLOCAZIONE EFFETTIVA"
with col3:
    st.markdown("**ALLOCAZIONE EFFETTIVA**", unsafe_allow_html=True)
    st.write(results_df)

## Colonna 2: Visualizza la tabella "BACHECA" (con colori)
#with col4:
#    st.markdown(f"**BACHECA {specific_date}**", unsafe_allow_html=True)
#    st.write(styled_df, use_container_width=True)
#    # Bottone per il download del file Excel
#    st.download_button(
#    label="Scarica la Bacheca in formato Excel",
#    data=excel_data,
#    file_name=f"bacheca_{specific_date}.xlsx",
#    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#)
#
#
#
#
## Funzione per aggiornare 'disp' al passaggio del giorno
#def aggiorna_disp(data_attuale, data_aggior_disp, disp):
#    if data_attuale == data_aggior_disp:
#        return disp
#    return "no"
## Ottieni la data attuale
#data_attuale = datetime.now()
#data_attuale = data_attuale.strftime("%d-%m")
## Aggiorna 'disp' al passaggio al giorno successivo
#disp = aggiorna_disp(data_attuale, data_aggior_disp, disp)
#totale_giorno_successivo = results_df.loc[results_df['Giorno'] == data_domani, 'Totale'].values[0]  # Totale del giorno successivo
## Condizione per mostrare l'alert
#if totale_giorno_successivo > 0 and disp == "ok":
#    message = "La tabella delle disponibilità dei rilevatori è stata aggiornata"
#    message_color = "#ECF0F1"  # Colore verde per il successo
#    icon = "✅"  # Icona di successo
#elif totale_giorno_successivo > 0 and disp == "no":
#    message = "La tabella delle disponibilità dei rilevatori non è stata aggiornata"
#    message_color = "#ECF0F1"  # Colore rosso per l'errore
#    icon = "❌"  # Icona di errore
#else:
#    message = None
#
#
#
## Mostra l'alert nella barra laterale con un messaggio stilizzato e lo stesso stile
#if message:
#    st.sidebar.markdown(f"""
#    <div style='padding: 30px; background-color: #2C3E50; color: #BDC3C7; border-radius: 15px; 
#    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; 
#    text-align: center; min-height: 50px; margin-top: 20px;'>
#        <h3 style='color: {message_color};'>{icon} <strong>{message}</strong></h3>
#    </div>
#    """, unsafe_allow_html=True)
#
#
#
