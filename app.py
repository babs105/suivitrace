import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
# import locale
# locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

# Fonction pour générer des données simulées

month_order = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
def generate_trace_data():
    # month_names = [
    # 'janvier', 'février', 'mars', 'avril', 'mai', 'juin',
    # 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'
    # ]
    patmai=pd.read_excel('data/PAT/PAT-MAI-2024.xlsx')
    patjuin=pd.read_excel('data/PAT/PAT-JUIN-2024.xlsx')
    pat = pd.concat([patmai,patjuin])
    
    pat[pat.isna()] = 0
    # pat['DATE_FR'] = pd.to_datetime(pat['DATE'], format='%d/%m/%Y')
    # pat['DATE_FR']= pat['DATE'].dt.strftime('%d/%m/%Y')
    pat['MOIS'] = pat['DATE'].dt.month.apply(lambda x: month_order[x-1])
    


    # print("test",tracemai)
    # tracejuin = pd.read_excel('data/TRACE/EVENT-JUIN-2024.xlsx')
    eventmai = pd.read_excel('data/TRACE/EVENT-MAI-2024.xlsx')
    tracejuin_dict = pd.read_excel('data/TRACE/SUIVI-TRACE-JUIN-2024.xlsx',sheet_name=None)
    eventjuin = tracejuin_dict.get('evenement')

    event = pd.concat([eventmai,eventjuin])

    # event['DATE_FR'] = event['DATE'].dt.strftime('%d/%m/%Y')
    event['MOIS'] = event['DATE'].dt.month.apply(lambda x: month_order[x-1])



    accidentmai=pd.read_excel('data/TRACE/ACCI-MAI-2024.xlsx')
    accidentjuin=tracejuin_dict.get('accident')
    # accidentjuin['DATE_FR'] = accidentjuin['DATE'].dt.strftime('%d/%m/%Y')
   
    
    accident = pd.concat([accidentmai,accidentjuin])
    accident['MOIS'] = accident['DATE'].dt.month.apply(lambda x: month_order[x-1])

    return pat,event,accident

def generate_carburant_data():

    carbu241 = pd.read_excel('data/CARBURANT/2024/RAPPORT-01-2024.xlsx')
    carbu242 = pd.read_excel('data/CARBURANT/2024/RAPPORT-02-2024.xlsx')
    carbu243 = pd.read_excel('data/CARBURANT/2024/RAPPORT-03-2024.xlsx')
    carbu244 = pd.read_excel('data/CARBURANT/2024/RAPPORT-04-2024.xlsx')
    carbu245 = pd.read_excel('data/CARBURANT/2024/RAPPORT-05-2024.xlsx')
    carbu246 = pd.read_excel('data/CARBURANT/2024/RAPPORT-06-2024.xlsx')

    carbu231=pd.read_excel('data/CARBURANT/2023/RAPPORT-01-2023.xlsx')
    carbu232=pd.read_excel('data/CARBURANT/2023/RAPPORT-02-2023.xlsx')
    carbu233=pd.read_excel('data/CARBURANT/2023/RAPPORT-03-2023.xlsx')
    carbu234=pd.read_excel('data/CARBURANT/2023/RAPPORT-04-2023.xlsx')
    carbu235=pd.read_excel('data/CARBURANT/2023/RAPPORT-05-2023.xlsx')
    carbu236=pd.read_excel('data/CARBURANT/2023/RAPPORT-06-2023.xlsx')
    carbu237=pd.read_excel('data/CARBURANT/2023/RAPPORT-07-2023.xlsx')
    carbu238 =pd.read_excel('data/CARBURANT/2023/RAPPORT-08-2023.xlsx')
    carbu239 = pd.read_excel('data/CARBURANT/2023/RAPPORT-09-2023.xlsx')
    carbu2310 = pd.read_excel('data/CARBURANT/2023/RAPPORT-10-2023.xlsx')
    carbu2311 = pd.read_excel('data/CARBURANT/2023/RAPPORT-11-2023.xlsx')
    carbu2312 = pd.read_excel('data/CARBURANT/2023/RAPPORT-12-2023.xlsx')

    carbu221 = pd.read_excel('data/CARBURANT/2022/RAPPORT-01-2022.xlsx')
    carbu222 = pd.read_excel('data/CARBURANT/2022/RAPPORT-02-2022.xlsx')
    carbu223 = pd.read_excel('data/CARBURANT/2022/RAPPORT-03-2022.xlsx')
    carbu224 = pd.read_excel('data/CARBURANT/2022/RAPPORT-04-2022.xlsx')
    carbu225 = pd.read_excel('data/CARBURANT/2022/RAPPORT-05-2022.xlsx')
    carbu226 = pd.read_excel('data/CARBURANT/2022/RAPPORT-06-2022.xlsx')
    carbu227 = pd.read_excel('data/CARBURANT/2022/RAPPORT-07-2022.xlsx')
    carbu228 = pd.read_excel('data/CARBURANT/2022/RAPPORT-08-2022.xlsx')
    carbu229 = pd.read_excel('data/CARBURANT/2022/RAPPORT-09-2022.xlsx')
    carbu2210 = pd.read_excel('data/CARBURANT/2022/RAPPORT-10-2022.xlsx')
    carbu2211 = pd.read_excel('data/CARBURANT/2022/RAPPORT-11-2022.xlsx')
    carbu2212 = pd.read_excel('data/CARBURANT/2022/RAPPORT-12-2022.xlsx')

    carburant = pd.concat([carbu241,carbu242,carbu243,carbu244,carbu245,carbu246,
    carbu231,carbu232,carbu233,carbu234,carbu235,carbu236,carbu237,carbu238,carbu239,carbu2310,carbu2311,carbu2312,
    carbu221,carbu222,carbu223,carbu224,carbu225,carbu226,carbu227,carbu228,carbu229,carbu2210,carbu2211,carbu2212
    ])
    carburant['Date']=pd.to_datetime(carburant['Date'], format='%d/%m/%Y')
    carburant['ANNEE'] = carburant['Date'].dt.strftime('%Y')

# Extraire le mois en tant que colonne séparée avec les noms des mois en français
    month_names = [
    'janvier', 'février', 'mars', 'avril', 'mai', 'juin',
    'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'
]
    carburant['MOIS'] = carburant['Date'].dt.month.apply(lambda x: month_names[x-1])
    # carburant['MOIS'] = carburant['Date'].dt.strftime('%B')


    return carburant


# Charger les données hy
pat,event,accident = generate_trace_data()
carburant = generate_carburant_data()
# Ajouter une colonne avec les dates formatées en français

# print(trace.head())

# Configuration de la page
st.set_page_config(page_title="Tableau de Bord ",layout="wide")

# Titre principal
st.title("RAPPORT AUTOROUTE A PEAGE")

# Barre latérale pour la navigation et les filtres
st.sidebar.title("Navigation")
# page = st.sidebar.radio("Aller à", ["Vue d'ensemble", "Analyse par tronçon", "Données brutes"])
page = st.sidebar.radio("Aller à", ["Suivi Tracé","Carburant",""])

   

# print("test",filtered_trace.head())
# Page: Vue d'ensemble
if page == "Suivi Tracé":
    st.sidebar.title("Filtres")
    troncon_filter = st.sidebar.multiselect("Sélectionnez le tronçon", options=pat["SECTEUR"].unique(), default=pat["SECTEUR"].unique())
    date_filter = st.sidebar.multiselect("Sélectionnez la période",options=event['MOIS'].unique(),default=event["MOIS"].unique())

# date_filter = st.sidebar.date_input("Sélectionnez la période", value=[data["date"].min(), data["date"].max()])
    # start_date = pd.to_datetime(date_filter[0])
    # end_date = pd.to_datetime(date_filter[1])
    # Filtrer les données
    # filtered_pat = pat[(pat["SECTEUR"].isin(troncon_filter)) & (pat["DATE"].between(start_date, end_date))]
    filtered_pat = pat[(pat["SECTEUR"].isin(troncon_filter)) & (pat["MOIS"].isin(date_filter))]
    distance_totale = filtered_pat["DISTANCE PARCOURUE"].sum()
    # filtered_trace = trace[(trace["SECTEUR LIEU"].isin(troncon_filter)) & (trace["DATE"].between(start_date, end_date))]

    filtered_trace = event[(event["SECTEUR LIEU"].isin(troncon_filter)) & (event["MOIS"].isin(date_filter))]
    filtered_trace["NATURE EVENEMENT"] = filtered_trace["NATURE EVENEMENT"].where(filtered_trace["NATURE EVENEMENT"].isin(['ACCIDENT', 'PANNE','INCIDENT','VEHICULE EN FEU']),other="AUTRES")

    nbre_total_event = filtered_trace["SECTEUR LIEU"].count()
    filtered_trace_rom = filtered_trace[filtered_trace['STATUT REMORQUAGE OU PATROUILLE']=="remorqué"]
    nbre_total_rom = filtered_trace.loc[filtered_trace['STATUT REMORQUAGE OU PATROUILLE']=="remorqué","STATUT REMORQUAGE OU PATROUILLE"].count()

    # filtered_accident = accident[(accident["TRONÇON"].isin(troncon_filter)) & (accident["DATE"].between(start_date, end_date))]
    filtered_accident = accident[(accident["TRONÇON"].isin(troncon_filter)) & (accident["MOIS"].isin(date_filter))]
    nbre_total_acci = filtered_accident['TRONÇON'].count()


    # Vérifier que la liste des filtres contient les éléments nécessaires
    if len(troncon_filter) == 3:
        # Créer un en-tête dynamique
        secteur=f" {troncon_filter[0]} - {troncon_filter[1]} - {troncon_filter[2]}"
        st.header(f"Vue d'ensemble : {secteur}")
    elif len(troncon_filter) == 2:
        secteur=f" {troncon_filter[0]} - {troncon_filter[1]}"
        st.header(f"Vue d'ensemble : {troncon_filter[0]}-{troncon_filter[1]}")
    elif len(troncon_filter) == 1:
        st.header(f"Vue d'ensemble : {troncon_filter[0]}")
        secteur=f" {troncon_filter[0]}"
    else:
        st.header("Vue d'ensemble : Tronçons non spécifiés correctement")
        secteur=""
    # st.write("Aperçu des données filtrées:")
    st.write("LA PATROUILLE : 🛣️ 🚗")
    st.write(f" Distance totale parcourue: :red[{distance_totale} Km ] sur {secteur}")

    #--------------------- ------------------------------------
    distance_chart = filtered_pat.groupby("MOIS")["DISTANCE PARCOURUE"].sum().reset_index()
    distance_chart['MOIS'] = pd.Categorical(distance_chart['MOIS'], categories=month_order, ordered=True)
    distance_chart = distance_chart.sort_values('MOIS')
       # Calculer la variation d'une année à l'autre

    distance_chart['Variation'] = distance_chart['DISTANCE PARCOURUE'].diff()
    distance_chart['Variation %'] = distance_chart['DISTANCE PARCOURUE'].pct_change() * 100
    print("rr",distance_chart)

    # Ajouter une colonne pour les flèches, les couleurs et les variations en pourcentage
    def add_arrow_and_color(value, percent):
        if pd.isna(value):
            return '', 'black', ''
        elif value > 0:
            return f'↑ {percent:.0f}%', 'red', f'{percent:.0f}%'
        elif value < 0:
            return f'↓ {percent:.0f}%', 'green', f'{percent:.0f}%'
        else:
            return '→ 0.0%', 'gray', '0.0%'

    distance_chart[['Flèche', 'Couleur', 'Variation %']] = distance_chart.apply(
        lambda row: pd.Series(add_arrow_and_color(row['Variation'], row['Variation %'])),
        axis=1
    )
     # Créer le bar chart avec Altair
    bars = alt.Chart(distance_chart).mark_bar().encode(
    x=alt.X('MOIS', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('DISTANCE PARCOURUE', axis=alt.Axis(format='~d')),
    # color='DATE'
    ).properties(
    title='Distance Parcourue en (km) par mois:'
    ) 
    text = bars.mark_text(
    align='center',
    baseline='middle',
    dy=-25,  # Déplace l'étiquette au-dessus de la barre
    color='yellow',
    fontSize=14
    ).encode(
        text=alt.Text('DISTANCE PARCOURUE:Q', format='.0f',)
    )
         # Ajouter les flèches de variation
    arrows = bars.mark_text(
        align='center',
        baseline='middle',
        # Déplace l'étiquette avec la flèche au-dessus de l'étiquette de texte
        dy=-10,
        fontSize=16,
    ).encode(
        text='Flèche:N',
        color=alt.Color('Couleur:N', scale=None)  # Utiliser la couleur définie dans la colonne 'Couleur'
    )
    distparmois=bars+text+arrows

    st.altair_chart(distparmois, use_container_width=True)

#--------------------------------------------------------------

    distance_chart = filtered_pat.groupby(["SECTEUR","MOIS"])["DISTANCE PARCOURUE"].sum().reset_index()

    distance_chart['MOIS'] = pd.Categorical(distance_chart['MOIS'], categories=month_order, ordered=True)
    distance_chart = distance_chart.sort_values(['SECTEUR','MOIS'])
       # Calculer la variation d'une année à l'autre

    distance_chart['Variation'] = distance_chart.groupby(['SECTEUR'])['DISTANCE PARCOURUE'].diff()
    distance_chart['Variation %'] = distance_chart.groupby(['SECTEUR'])['DISTANCE PARCOURUE'].pct_change() * 100
   

    # Ajouter une colonne pour les flèches, les couleurs et les variations en pourcentage
    def add_arrow_and_color(value, percent):
        if pd.isna(value):
            return '', 'black', ''
        elif value > 0:
            return f'↑ {percent:.0f}%', 'red', f'{percent:.0f}%'
        elif value < 0:
            return f'↓ {percent:.0f}%', 'green', f'{percent:.0f}%'
        else:
            return '→ 0.0%', 'gray', '0.0%'

    distance_chart[['Flèche', 'Couleur', 'Variation %']] = distance_chart.apply(
        lambda row: pd.Series(add_arrow_and_color(row['Variation'], row['Variation %'])),
        axis=1
    )
     # Créer le bar chart avec Altair
    bars = alt.Chart(distance_chart).mark_bar().encode(
    x=alt.X('SECTEUR', axis=alt.Axis(labelAngle=90),title=""),
    y=alt.Y('DISTANCE PARCOURUE', axis=alt.Axis(format='~d')),
    color=alt.Color('SECTEUR:N')
    ).properties(
    width=85,
    title='Distance Parcourue en (km) par mois par TRONÇON:'
    ) 
    text = bars.mark_text(
    align='center',
    baseline='middle',
    dy=-25,  # Déplace l'étiquette au-dessus de la barre
    color='yellow',
    fontSize=14
    ).encode(
        text=alt.Text('DISTANCE PARCOURUE:Q', format='.0f',)
    )
         # Ajouter les flèches de variation
    arrows = bars.mark_text(
        align='center',
        baseline='middle',
        # Déplace l'étiquette avec la flèche au-dessus de l'étiquette de texte
        dy=-10,
        fontSize=16,
    ).encode(
        text='Flèche:N',
        color=alt.Color('Couleur:N', scale=None)  # Utiliser la couleur définie dans la colonne 'Couleur'
    )
    distparmois = bars + text + arrows

    dist_par_secteur = distparmois.facet(
        facet=alt.Facet('MOIS', title="VARIATION DISTANCE PARCOURUE PAR TRONCON PAR MOIS"),  # Séparer les graphiques par mois
        columns=12 # Nombre de colonnes dans la grille de facettes
    )
    st.altair_chart(dist_par_secteur, use_container_width=True)
#------------------------------------------

#---------------------------------------------------------------------------------------
   
    distance_chart = filtered_pat.groupby("DATE")["DISTANCE PARCOURUE"].sum().reset_index()
    # Identifier les valeurs minimales et maximales

    min_value = distance_chart['DISTANCE PARCOURUE'].min()
    max_value = distance_chart['DISTANCE PARCOURUE'].max()

    # Ajouter une colonne pour la couleur
    def color_code(row):
        if row['DISTANCE PARCOURUE'] == min_value:
            return 'Min'
        elif row['DISTANCE PARCOURUE'] == max_value:
            return 'Max'
     

    distance_chart['distance'] = distance_chart.apply(color_code, axis=1)

    line_chart = alt.Chart(distance_chart).mark_line().encode(
    x=alt.X('DATE:T', axis=alt.Axis(labelAngle=0, title='Date', format='%d/%m/%Y')),
    y=alt.Y('DISTANCE PARCOURUE:Q', axis=alt.Axis(format='~d')),
   
    # color='DATE'
    tooltip=['DATE', 'DISTANCE PARCOURUE']
    ).properties(
    title='Evolution Distance Parcourue en (km):'
    ) 

    points_chart = alt.Chart(distance_chart).mark_point(size=150,filled=True).encode(
    x='DATE:T',
    y='DISTANCE PARCOURUE:Q',
    color=alt.Color('distance:N', scale=alt.Scale(domain=['Min', 'Max'], range=['red', 'green'])),
    tooltip=['DATE', 'DISTANCE PARCOURUE']
    )
     # Filtrer les données pour les étiquettes Min et Max
    min_label_data = distance_chart[distance_chart['distance'] == 'Min']
    max_label_data = distance_chart[distance_chart['distance'] == 'Max']

    # Ajouter les étiquettes pour Min
    min_labels = alt.Chart(min_label_data).mark_text(
        align='center',
        baseline='middle',
        dy=10  # Décalage horizontal pour éviter de superposer les points
    ).encode(
        x='DATE:T',
        y='DISTANCE PARCOURUE:Q',
        text=alt.Text('DISTANCE PARCOURUE:Q', format='.0f'),  # Formater le texte pour la distance
        color=alt.value('red')  # Couleur de l'étiquette Min
    )

    # Ajouter les étiquettes pour Max
    max_labels = alt.Chart(max_label_data).mark_text(
        align='center',
        baseline='middle',
        dy=-10  # Décalage horizontal pour éviter de superposer les points
    ).encode(
        x='DATE:T',
        y='DISTANCE PARCOURUE:Q',
        text=alt.Text('DISTANCE PARCOURUE:Q', format='.0f'),  # Formater le texte pour la distance
        color=alt.value('green')  # Couleur de l'étiquette Max
    )

    chart1 = line_chart + points_chart + min_labels + max_labels
    st.altair_chart(chart1, use_container_width=True)





 

  
    #### **** event *** ############ **** event **** ####### **** #####
    ########################################### **** event **** #######################################
    st.write("LES EVENEMENTS: 🚨🚨")
    st.write(f" Nombre Total Evenement: :red[{nbre_total_event}]  sur  {secteur}")

    event_secteur_chart = filtered_trace.groupby("MOIS")["SECTEUR LIEU"].count().reset_index(name='NOMBRE')
    event_secteur_chart['MOIS'] = pd.Categorical(event_secteur_chart['MOIS'], categories=month_order, ordered=True)
    event_secteur_chart = event_secteur_chart.sort_values('MOIS')
       # Calculer la variation d'une année à l'autre

    event_secteur_chart['Variation'] = event_secteur_chart['NOMBRE'].diff()
    event_secteur_chart['Variation %'] = event_secteur_chart['NOMBRE'].pct_change() * 100

    # Ajouter une colonne pour les flèches, les couleurs et les variations en pourcentage
    def add_arrow_and_color(value, percent):
        if pd.isna(value):
            return '', 'black', ''
        elif value > 0:
            return f'↑ {percent:.1f}%', 'red', f'{percent:.1f}%'
        elif value < 0:
            return f'↓ {percent:.1f}%', 'green', f'{percent:.1f}%'
        else:
            return '→ 0.0%', 'gray', '0.0%'

    event_secteur_chart[['Flèche', 'Couleur', 'Variation %']] = event_secteur_chart.apply(
        lambda row: pd.Series(add_arrow_and_color(row['Variation'], row['Variation %'])),
        axis=1
    )
      # Créer le bar chart avec Altair
    bars = alt.Chart(event_secteur_chart).mark_bar().encode(
    x=alt.X('MOIS', axis=alt.Axis(labelAngle=0),scale=alt.Scale(paddingInner=0.5)),
    y=alt.Y('NOMBRE', axis=alt.Axis(format='~d')),
    
    ).properties(
    title='NOMBRE EVENEMENT PAR MOIS'
    ) 
    text = bars.mark_text(
    align='center',
    baseline='middle',
    dy=-25,  # Déplace l'étiquette au-dessus de la barre
    color='yellow',
    fontSize=14
    ).encode(
        text=alt.Text('NOMBRE:Q', format='.0f',)
    )
           # Ajouter les flèches de variation
    arrows = bars.mark_text(
        align='center',
        baseline='middle',
        # Déplace l'étiquette avec la flèche au-dessus de l'étiquette de texte
        dy=-10,
        fontSize=16,
    ).encode(
        text='Flèche:N',
        color=alt.Color('Couleur:N', scale=None)  # Utiliser la couleur définie dans la colonne 'Couleur'
    )
    chart2=bars+text+arrows
    # Afficher le chart dans Streamlit
    st.altair_chart(chart2, use_container_width=True)
    #--------------NOMBRE EVENT PAR TRONCON PAR MOIS-----------

    event_secteur_chart = filtered_trace.groupby(["SECTEUR LIEU",'MOIS'])["SECTEUR LIEU"].count().reset_index(name='NOMBRE')
    event_secteur_chart['MOIS'] = pd.Categorical(event_secteur_chart['MOIS'], categories=month_order, ordered=True)
    event_secteur_chart = event_secteur_chart.sort_values(['SECTEUR LIEU','MOIS'])
       # Calculer la variation d'une année à l'autre

    event_secteur_chart['Variation'] = event_secteur_chart.groupby(['SECTEUR LIEU'])['NOMBRE'].diff()
    event_secteur_chart['Variation %'] = event_secteur_chart.groupby(['SECTEUR LIEU'])['NOMBRE'].pct_change() * 100

    print("nbrevent",event_secteur_chart)

    # Ajouter une colonne pour les flèches, les couleurs et les variations en pourcentage
    def add_arrow_and_color(value, percent):
        if pd.isna(value):
            return '', 'black', ''
        elif value > 0:
            return f'↑ {percent:.1f}%', 'red', f'{percent:.1f}%'
        elif value < 0:
            return f'↓ {percent:.1f}%', 'green', f'{percent:.1f}%'
        else:
            return '→ 0.0%', 'gray', '0.0%'

    event_secteur_chart[['Flèche', 'Couleur', 'Variation %']] = event_secteur_chart.apply(
        lambda row: pd.Series(add_arrow_and_color(row['Variation'], row['Variation %'])),
        axis=1
    )
      # Créer le bar chart avec Altair
    bars = alt.Chart(event_secteur_chart).mark_bar().encode(
    x=alt.X('SECTEUR LIEU', axis=alt.Axis(labelAngle=90),scale=alt.Scale(paddingInner=0.5)),
    y=alt.Y('NOMBRE', axis=alt.Axis(format='~d')),
    color=alt.Color('SECTEUR LIEU')
    ).properties(
    width=100,
    title='NOMBRE EVENEMENT PAR MOIS'
    ) 
    text = bars.mark_text(
    align='center',
    baseline='middle',
    dy=-25,  # Déplace l'étiquette au-dessus de la barre
    color='yellow',
    fontSize=14
    ).encode(
        text=alt.Text('NOMBRE:Q', format='.0f',)
    )
           # Ajouter les flèches de variation
    arrows = bars.mark_text(
        align='center',
        baseline='middle',
        # Déplace l'étiquette avec la flèche au-dessus de l'étiquette de texte
        dy=-10,
        fontSize=12,
    ).encode(
        text='Flèche:N',
        color=alt.Color('Couleur:N', scale=None)  # Utiliser la couleur définie dans la colonne 'Couleur'
    )
    chart2=bars+text+arrows

    nbrevt_secteur_mois = chart2.facet(
        facet=alt.Facet('MOIS', title="VARIATION NBRE EVENEMENT PAR TRONCON PAR MOIS"),  # Séparer les graphiques par mois
        columns=12 # Nombre de colonnes dans la grille de facettes
    )
    # Afficher le chart dans Streamlit
    st.altair_chart(nbrevt_secteur_mois, use_container_width=True)
    #-------------------------------- evolution des event --------------

    st.write(f"")
  

    evolu_chart = filtered_trace.groupby("DATE")["SECTEUR LIEU"].count().reset_index(name='NOMBRE')

     # Identifier les valeurs minimales et maximales

    min_value = evolu_chart['NOMBRE'].min()
    max_value = evolu_chart['NOMBRE'].max()

    # Ajouter une colonne pour la couleur
    def color_code(row):
        if row['NOMBRE'] == min_value:
            return 'Min'
        elif row['NOMBRE'] == max_value:
            return 'Max'
     

    evolu_chart['Nbre Evenement'] = evolu_chart.apply(color_code, axis=1)
    line_chart = alt.Chart(evolu_chart).mark_line().encode(
    x=alt.X('DATE:T', axis=alt.Axis(labelAngle=0, title='Date', format='%d/%m/%Y')),
    y=alt.Y('NOMBRE', axis=alt.Axis(format='~s')),
    # color=alt.Color('SECTEUR LIEU', scale=alt.Scale(scheme='tableau10'))
    ).properties(
    title=f"Evolution  Nombre  evénèments  :{secteur}"
    ) 
    points_chart = alt.Chart(evolu_chart).mark_point(size=150,filled=True).encode(
    x='DATE:T',
    y='NOMBRE:Q',
    color=alt.Color('Nbre Evenement:N', scale=alt.Scale(domain=['Min', 'Max'], range=['red', 'green'])),
    tooltip=['DATE', 'NOMBRE']
    )
     # Filtrer les données pour les étiquettes Min et Max
    min_label_data = evolu_chart[evolu_chart['Nbre Evenement'] == 'Min']
    max_label_data = evolu_chart[evolu_chart['Nbre Evenement'] == 'Max']

    # Ajouter les étiquettes pour Min
    min_labels = alt.Chart(min_label_data).mark_text(
        align='center',
        baseline='middle',
        dy=12  # Décalage horizontal pour éviter de superposer les points
    ).encode(
        x='DATE:T',
        y='NOMBRE:Q',
        text=alt.Text('NOMBRE:Q', format='.0f'),  # Formater le texte pour la distance
        color=alt.value('red')  # Couleur de l'étiquette Min
    )

    # Ajouter les étiquettes pour Max
    max_labels = alt.Chart(max_label_data).mark_text(
        align='center',
        baseline='middle',
        dy=-12  # Décalage horizontal pour éviter de superposer les points
    ).encode(
        x='DATE:T',
        y='NOMBRE:Q',
        text=alt.Text('NOMBRE:Q', format='.0f'),  # Formater le texte pour la distance
        color=alt.value('green')  # Couleur de l'étiquette Max
    )
    chart6 =line_chart + points_chart + min_labels + max_labels
    st.altair_chart(chart6, use_container_width=True)
    
    event_secteur_chart = filtered_trace.groupby("SECTEUR LIEU")["SECTEUR LIEU"].count().reset_index(name='NOMBRE')
      # Créer le bar chart avec Altair
    bars = alt.Chart(event_secteur_chart).mark_bar().encode(
    x=alt.X('SECTEUR LIEU', axis=alt.Axis(labelAngle=0),scale=alt.Scale(paddingInner=0.5)),
    y=alt.Y('NOMBRE', axis=alt.Axis(format='~s')),
    color=alt.Color('SECTEUR LIEU')
    ).properties(
    title='NOMBRE EVENEMENT PAR SECTEUR'
    ) 
    text= bars.mark_text(
    align='center',
    baseline='middle',
    dy=-10,  # Déplace l'étiquette au-dessus de la barre
    # color='red',
    fontSize=12
    ).encode(
        text=alt.Text('NOMBRE:Q', format='.0f',)
    )
    chart2 = bars +  text 
    # Afficher le chart dans Streamlit
    st.altair_chart(chart2, use_container_width=True)

    #------------------------- les ordinateurs de bureau pour vous servir --------------------------------------
    #-------------------------------------------------------nature EVENT-----------------------------------------
    st.write(f"Nature Evenement :")
    
    nature_event_secteur_chart1 = filtered_trace.groupby("NATURE EVENEMENT")["NATURE EVENEMENT"].count().reset_index(name="NOMBRE")

        # Créer le graphique à barres côte à côte
    bars = alt.Chart(nature_event_secteur_chart1).mark_bar().encode(
        x=alt.X('NATURE EVENEMENT:N', axis=alt.Axis(labelAngle=0,title=f"Nature Evenement"),scale=alt.Scale(paddingInner=0)),
        y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre',format='~d')),
        color=alt.Color('NATURE EVENEMENT:N'),
        # column=alt.Column('SECTEUR LIEU:N', title='Secteur')
    ).properties(
        title='Répartition des événements par Nature'
    )

    text= bars.mark_text(
        align='center',
        baseline='middle',
        dy=-10  # Décalage horizontal pour éviter de superposer les points
    ).encode(
        text=alt.Text('NOMBRE:Q', format='.0f'),  # Formater le texte pour la distance
    )
    chart10 = bars + text
    st.altair_chart(chart10, use_container_width=True)
    #--------------------
    st.write(f"Evolution Nature Evenement :")

    nature_event_secteur_chart = filtered_trace.groupby(['DATE','NATURE EVENEMENT'])["NATURE EVENEMENT"].count().reset_index(name="NOMBRE")
    nature_event_panne = nature_event_secteur_chart[nature_event_secteur_chart['NATURE EVENEMENT'] == "PANNE"]
    nature_event_accident = nature_event_secteur_chart[nature_event_secteur_chart['NATURE EVENEMENT'] == "ACCIDENT"]
    nature_event_vhl_feu = nature_event_secteur_chart[nature_event_secteur_chart['NATURE EVENEMENT'] == "VEHICULE EN FEU"]

    def min(df):
        return df['NOMBRE'].min()

    def max(df):
        return df['NOMBRE'].max()
    
    min_panne = min(nature_event_panne)
    max_panne = max(nature_event_panne)
    min_acci = min(nature_event_accident)
    max_acci = max(nature_event_accident)
    min_vhlfeu = min(nature_event_vhl_feu)
    max_vhlfeu = max(nature_event_vhl_feu)
    

    # Ajouter une colonne pour la couleur
    def color_panne(row):
        if row['NOMBRE'] == min_panne:
            return 'Min'
        elif row['NOMBRE'] == max_panne:
            return 'Max'
        # else :
        #     return 'Normal'

    def color_accident(row):
        if row['NOMBRE'] == min_acci:
            return 'Min'
        elif row['NOMBRE'] == max_acci:
            return 'Max'
        # else :
        #     return 'Normal'
    
    def color_vhl_feu(row):
        if row['NOMBRE'] == min_vhlfeu:
            return 'Min'
        elif row['NOMBRE'] == max_vhlfeu:
            return 'Max'
        # else :
        #     return 'Normal'

    nature_event_panne['Panne'] = nature_event_panne.apply(color_panne, axis=1)
    nature_event_accident['Accident'] = nature_event_accident.apply(color_accident, axis=1)
    nature_event_vhl_feu['Vehicule en Feu'] = nature_event_vhl_feu.apply(color_vhl_feu, axis=1)

    # Créer le graphique à barres côte à côte
    panne_chart = alt.Chart(nature_event_panne).mark_line(color='pink').encode(
        x=alt.X('DATE:T', axis=alt.Axis(labelAngle = 0, title='Date', format='%d/%m/%Y')),
        y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre',format='~d')),
    ).properties(
     title=f"Evolution Panne: {secteur}"
    )

    acci_chart = alt.Chart(nature_event_accident).mark_line(color="steelblue").encode(
        x=alt.X('DATE:T', axis=alt.Axis(labelAngle=0, title='Date', format='%d/%m/%Y')),
        y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre',format='~d')),
    ).properties(
     title=f"Evolution Accident: {secteur}"
    )


    print("VHL FEU",nature_event_vhl_feu)
    vhlfeu_chart = alt.Chart(nature_event_vhl_feu).mark_line(color='white').encode(
        x=alt.X('DATE:T', axis=alt.Axis(labelAngle=0, title='Date', format='%d/%m/%Y')),
        y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre',format='~d'))
    ).properties(
     title=f"Evolution Vehicule en Feu: {secteur}"
    )


    panne_points_chart = alt.Chart(nature_event_panne).mark_point(size=100,filled=True).encode(
    x='DATE:T',
    y='NOMBRE:Q',
    color=alt.Color('Panne:N',scale=alt.Scale(domain=['Min', 'Max','Normal'], range=['green','red',"pink"]))
    )

    acci_points_chart = alt.Chart(nature_event_accident).mark_point(size=100,filled=True).encode(
    x='DATE:T',
    y='NOMBRE:Q',
    color=alt.Color('Accident:N',scale=alt.Scale(domain=['Min', 'Max','Normal'], range=['green','red',"steelblue"]))
    )
    
    vhlfeu_points_chart = alt.Chart(nature_event_vhl_feu).mark_point(size=100,filled=True).encode(
    x='DATE:T',
    y='NOMBRE:Q',
    color=alt.Color('Vehicule en Feu:N',scale=alt.Scale(domain=['Min', 'Max','Normal'], range=['green','red','white']))
   )
   
    
    # Filtrer les données pour les étiquettes Min et Max
    min_panne_data = nature_event_panne[nature_event_panne['Panne'] == 'Min']
    max_panne_data = nature_event_panne[nature_event_panne['Panne'] == 'Max']
    min_acci_data = nature_event_accident[nature_event_accident['Accident'] == 'Min']
    max_acci_data = nature_event_accident[nature_event_accident['Accident'] == 'Max']
    min_vhlfeu_data = nature_event_vhl_feu[nature_event_vhl_feu['Vehicule en Feu'] == 'Min']
    max_vhlfeu_data = nature_event_vhl_feu[nature_event_vhl_feu['Vehicule en Feu']== 'Max']

    # Ajouter les étiquettes pour Min
    min_label_panne = alt.Chart(min_panne_data).mark_text(
        align='center',
        baseline='middle',
        dy=12  # Décalage horizontal pour éviter de superposer les points
    ).encode(
        x='DATE:T',
        y='NOMBRE:Q',
        text=alt.Text('NOMBRE:Q', format='.0f'),  # Formater le texte pour la distance
        color=alt.value('green')  # Couleur de l'étiquette Min
    )

    # Ajouter les étiquettes pour Max
    max_label_panne = alt.Chart(max_panne_data).mark_text(
        align='center',
        baseline='middle',
        dy=-12  # Décalage horizontal pour éviter de superposer les points
    ).encode(
        x='DATE:T',
        y='NOMBRE:Q',
        text=alt.Text('NOMBRE:Q', format='.0f'),  # Formater le texte pour la distance
        color=alt.value('red')  # Couleur de l'étiquette Max
    )

    # Ajouter les étiquettes pour Min accident
    min_label_acci = alt.Chart(min_acci_data).mark_text(
        align='center',
        baseline='middle',
        dy=12  # Décalage horizontal pour éviter de superposer les points
    ).encode(
        x='DATE:T',
        y='NOMBRE:Q',
        text=alt.Text('NOMBRE:Q', format='.0f'),  # Formater le texte pour la distance
        color=alt.value('red')  # Couleur de l'étiquette Min
    )

    # Ajouter les étiquettes pour Max
    max_label_acci = alt.Chart(max_acci_data).mark_text(
        align='center',
        baseline='middle',
        dy=-12  # Décalage horizontal pour éviter de superposer les points
    ).encode(
        x='DATE:T',
        y='NOMBRE:Q',
        text=alt.Text('NOMBRE:Q', format='.0f'),  # Formater le texte pour la distance
        color=alt.value('green')  # Couleur de l'étiquette Max
    )
    
     # Ajouter les étiquettes pour Min accident
    min_label_vhlfeu = alt.Chart(min_vhlfeu_data).mark_text(
        align='center',
        baseline='middle',
        dy=12  # Décalage horizontal pour éviter de superposer les points
    ).encode(
        x='DATE:T',
        y='NOMBRE:Q',
        text=alt.Text('NOMBRE:Q', format='.0f'),  # Formater le texte pour la distance
        color=alt.value('red')  # Couleur de l'étiquette Min
    )

    # Ajouter les étiquettes pour Max
    max_label_vhlfeu= alt.Chart(max_vhlfeu_data).mark_text(
        align='center',
        baseline='middle',
        dy=-12  # Décalage horizontal pour éviter de superposer les points
    ).encode(
        x='DATE:T',
        y='NOMBRE:Q',
        text=alt.Text('NOMBRE:Q', format='.0f'),  # Formater le texte pour la distance
        color=alt.value('green')  # Couleur de l'étiquette Max
    )

    panne_line = panne_chart + panne_points_chart + min_label_panne + max_label_panne 
    acci_line = acci_chart + acci_points_chart + min_label_acci + max_label_acci 
    vhlfeu_line =vhlfeu_chart + vhlfeu_points_chart + min_label_vhlfeu + max_label_vhlfeu 

    # chart3 = panne_line + acci_line #+ vhlfeu_line 
    
    st.altair_chart(panne_line, use_container_width=True)
    st.altair_chart(acci_line, use_container_width=True)
    st.altair_chart(vhlfeu_line, use_container_width=True)



    #-------------------------------------------------------------------------------------------------
    #-------------------------------------les gens sont bien organisés pour les détails ---------------------------------------

    #-------------------------------------------------------- statut event -----------------------------
    st.write(f"Statut Evenement:")

    event_statut_secteur_chart = filtered_trace.groupby("STATUT REMORQUAGE OU PATROUILLE")["NATURE EVENEMENT"].count().reset_index(name="NOMBRE")
        # Créer le graphique à barres côte à côte
    bars = alt.Chart(event_statut_secteur_chart).mark_bar().encode(
        x=alt.X('STATUT REMORQUAGE OU PATROUILLE:N', axis=alt.Axis(title=f"Statut",labelAngle=0),scale=alt.Scale(paddingInner=0)),
        y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre',format="~d")),
        color=alt.Color('STATUT REMORQUAGE OU PATROUILLE:N'),
    ).properties(
        title=f'Répartition des evenements par statut : {secteur}'
    )
    
    text = bars.mark_text(
    align='center',
    baseline='middle',
    dy=-15,  # Déplace l'étiquette au-dessus de la barre
    color='yellow',
    fontSize=14
    ).encode(
        text=alt.Text('NOMBRE:Q', format='.0f')
    )

    chart4 = bars + text
    # Afficher le chart dans Streamlit
    st.altair_chart(chart4, use_container_width=True)

  #--------------------------------------------------------
 #-------------------------------------------------------- statut event -----------------------------

    event_statut_secteur_chart = filtered_trace.groupby(["SECTEUR LIEU","STATUT REMORQUAGE OU PATROUILLE"])["NATURE EVENEMENT"].count().reset_index(name="NOMBRE")
        # Créer le graphique à barres côte à côte
    bars = alt.Chart(event_statut_secteur_chart).mark_bar().encode(
        x=alt.X('STATUT REMORQUAGE OU PATROUILLE:N', axis=alt.Axis(title="",labelAngle=90),scale=alt.Scale(paddingInner=0)),
        y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre',format="~d")),
        color=alt.Color('STATUT REMORQUAGE OU PATROUILLE:N'),
    ).properties(
        width=250,
        title=f'Répartition des evenements par statut :'
    )
    
    text = bars.mark_text(
    align='center',
    baseline='middle',
    dy=-15,  # Déplace l'étiquette au-dessus de la barre
    color='yellow',
    fontSize=14
    ).encode(
        text=alt.Text('NOMBRE:Q', format='.0f')
    )

    chart4 = bars + text
    statut_event_secteur = chart4.facet(
        facet=alt.Facet('SECTEUR LIEU:N', title="STATUT EVENEMENT PAR TRONCON"),  # Séparer les graphiques par mois
        columns=10 # Nombre de colonnes dans la grille de facettes
    )
    # Afficher le chart dans Streamlit
    st.altair_chart(statut_event_secteur, use_container_width=True)

  #--------------------------------------------------------
    st.write(f"Remorquage:")
    st.write(f"Nombre Total de Véhicule Remorqués: :red[{nbre_total_rom}] ")

    rom_by_month = filtered_trace_rom.groupby("MOIS")["TYPES DE VEHICULE"].count().reset_index(name="NOMBRE")

    rom_by_month['MOIS'] = pd.Categorical(rom_by_month['MOIS'], categories=month_order, ordered=True)
    rom_by_month = rom_by_month.sort_values('MOIS')
     # Calculer la variation d'une année à l'autre
    rom_by_month['Variation'] = rom_by_month['NOMBRE'].diff()
    rom_by_month['Variation %'] = rom_by_month['NOMBRE'].pct_change() * 100
   

    # Ajouter une colonne pour les flèches, les couleurs et les variations en pourcentage
    def add_arrow_and_color(value, percent):
        if pd.isna(value):
            return '', 'black', ''
        elif value > 0:
            return f'↑ {percent:.1f}%', 'red', f'{percent:.1f}%'
        elif value < 0:
            return f'↓ {percent:.1f}%', 'green', f'{percent:.1f}%'
        else:
            return '→ 0.0%', 'gray', '0.0%'

    rom_by_month[['Flèche', 'Couleur', 'Variation %']] = rom_by_month.apply(
        lambda row: pd.Series(add_arrow_and_color(row['Variation'], row['Variation %'])),
        axis=1
    )  
    bars = alt.Chart(rom_by_month).mark_bar().encode(
        x=alt.X('MOIS', axis=alt.Axis(labelAngle=0,title='MOIS'),scale=alt.Scale(paddingInner=0)),
        y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre',format="~d")),
        # color=alt.Color('TYPES DE VEHICULE:N'),
       
    ).properties(
        title='Nombre de Remorquage par MOIS'
    )
    text = bars.mark_text(
    align='center',
    baseline='middle',
    dy=-25,  # Déplace l'étiquette au-dessus de la barre
    color='yellow',
    fontSize=14
    ).encode(
        text=alt.Text('NOMBRE:Q', format='.0f',)
    )
      # Ajouter les flèches de variation
    arrows = bars.mark_text(
        align='center',
        baseline='middle',
        # dx=-40,  # Déplace l'étiquette avec la flèche au-dessus de l'étiquette de texte
        dy=-10,
        fontSize=16,
        # dx=5,
        # color='red'
    ).encode(
        text='Flèche:N',
        color=alt.Color('Couleur:N', scale=None)  # Utiliser la couleur définie dans la colonne 'Couleur'
    )
    rom_mois=bars+text+arrows

    # Afficher le chart dans Streamlit
    st.altair_chart(rom_mois, use_container_width=True)

    #----------------------------------------- TYPES DE VEHICULE-------------------------------------------------------

    rom_secteur_chart = filtered_trace_rom.groupby("TYPES DE VEHICULE")["TYPES DE VEHICULE"].count().reset_index(name="NOMBRE")
    bars = alt.Chart(rom_secteur_chart).mark_bar().encode(
        x=alt.X('TYPES DE VEHICULE:N', axis=alt.Axis(title='TYPE VEHICULE',labelAngle=0),scale=alt.Scale(paddingInner=0)),
        y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre',format="~d")),
        color=alt.Color('TYPES DE VEHICULE:N'),
       
    ).properties(
        title='Répartition des Types de Vehicule remorqué'
    )
    text = bars.mark_text(
    align='center',
    baseline='middle',
    dy=-15,  # Déplace l'étiquette au-dessus de la barre
    color='yellow',
    fontSize=14
    ).encode(
        text=alt.Text('NOMBRE:Q', format='.0f',)
    )

    # Afficher le chart dans Streamlit
    chart5 = bars + text
    st.altair_chart(chart5, use_container_width=True)
    #-----------------------------------------------------------
    #----------------------------------------- TYPES DE VEHICULE-------------------------------------------------------

    rom_secteur_chart = filtered_trace_rom.groupby(["SECTEUR LIEU","TYPES DE VEHICULE"])["TYPES DE VEHICULE"].count().reset_index(name="NOMBRE")
    bars = alt.Chart(rom_secteur_chart).mark_bar().encode(
        # x=alt.X('TYPES DE VEHICULE:N', axis=alt.Axis(title='TYPE VEHICULE',labelAngle=0),scale=alt.Scale(paddingInner=0)),
        x=alt.X('TYPES DE VEHICULE:N', axis=alt.Axis(title='',labelAngle=0),scale=alt.Scale(paddingInner=0)),
        
        y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre',format="~d")),
        color=alt.Color('TYPES DE VEHICULE:N'),
       
    ).properties(
        width=250,
        title='Types de Vehicule remorqué par TRONÇON'
    )
    text = bars.mark_text(
    align='center',
    baseline='middle',
    dy=-15,  # Déplace l'étiquette au-dessus de la barre
    color='yellow',
    fontSize=14
    ).encode(
        text=alt.Text('NOMBRE:Q', format='.0f',)
    )

    # Afficher le chart dans Streamlit
    chart5 = bars + text

    type_vhl_secteur = chart5.facet(
        facet=alt.Facet('SECTEUR LIEU:N', sort=month_order, title="TYPES DE VEHICULE REMORQUES PAR TRONCON"),  # Séparer les graphiques par mois
        columns=6 # Nombre de colonnes dans la grille de facettes
    )
    st.altair_chart(type_vhl_secteur, use_container_width=True)
    ############################################## accident #########################################################


    st.write(f"Accident:")
    st.write(f" Nombre Total d'Accident: :red[{nbre_total_acci}] ")
    

    accident_chart = filtered_accident.groupby("MOIS")["TRONÇON"].count().reset_index(name="NOMBRE")

    accident_chart['MOIS'] = pd.Categorical(accident_chart['MOIS'], categories=month_order, ordered=True)
    accident_chart = accident_chart.sort_values('MOIS')
    # Calculer la variation d'une année à l'autre
    accident_chart['Variation'] = accident_chart['NOMBRE'].diff()
    accident_chart['Variation %'] = accident_chart['NOMBRE'].pct_change() * 100

    # Ajouter une colonne pour les flèches, les couleurs et les variations en pourcentage
    def add_arrow_and_color(value, percent):
        if pd.isna(value):
            return '', 'black', ''
        elif value > 0:
            return f'↑ {percent:.1f}%', 'red', f'{percent:.1f}%'
        elif value < 0:
            return f'↓ {percent:.1f}%', 'green', f'{percent:.1f}%'
        else:
            return '→ 0.0%', 'gray', '0.0%'

    accident_chart[['Flèche', 'Couleur', 'Variation %']] = accident_chart.apply(
        lambda row: pd.Series(add_arrow_and_color(row['Variation'], row['Variation %'])),
        axis=1
    )  
    # Créer le graphique à barres côte à côte
    bars = alt.Chart(accident_chart).mark_bar().encode(
        x=alt.X('MOIS', axis=alt.Axis(title='MOIS',labelAngle=0),scale=alt.Scale(paddingInner=0)),
        y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre')),
        # color=alt.Color('TRONÇON:N'),
    ).properties(
        title="Nombre d'accident par MOIS"
    )
    text = bars.mark_text(
        align='center',
        baseline='middle',
        dy=-24,  # Déplace l'étiquette au-dessus de la barre
        color='yellow',
        fontSize=14
    ).encode(
        text=alt.Text('NOMBRE:Q', format='.0f',)
    )
      # Ajouter les flèches de variation
    arrows = bars.mark_text(
        align='center',
        baseline='middle',
        # dx=-40,  # Déplace l'étiquette avec la flèche au-dessus de l'étiquette de texte
        dy=-10,
        fontSize=14,
        # dx=5,
        # color='red'
    ).encode(
        text='Flèche:N',
        color=alt.Color('Couleur:N', scale=None)  # Utiliser la couleur définie dans la colonne 'Couleur'
    )
    acci_mois = bars + text + arrows
    # Afficher le chart dans Streamlit
    st.altair_chart(acci_mois, use_container_width=True)
    
   #--------------------------------------------------------------------------------------------------

    accident_chart = filtered_accident.groupby("TRONÇON")["TRONÇON"].count().reset_index(name="NOMBRE")
    

    # Créer le graphique à barres côte à côte
    bars = alt.Chart(accident_chart).mark_bar().encode(
        x=alt.X('TRONÇON:N', axis=alt.Axis(title='Secteur',labelAngle=0),scale=alt.Scale(paddingInner=0)),
        y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre')),
        color=alt.Color('TRONÇON:N'),
       
    ).properties(
        title="Nombre d'accident par SECTEUR"
    )

    text = bars.mark_text(
    align='center',
    baseline='middle',
    dy=-10,  # Déplace l'étiquette au-dessus de la barre
    color='yellow',
    fontSize=14
    ).encode(
        text=alt.Text('NOMBRE:Q', format='.0f',)
    )
    chart7 = bars + text

    # Afficher le chart dans Streamlit
    st.altair_chart(chart7, use_container_width=True)
    #-------------------------------------------------------type accident ------------------
    # st.write("Type d'accident")

    type_accident_chart = filtered_accident.groupby("TYPES ACCIDENTS")["TYPES ACCIDENTS"].count().reset_index(name="NOMBRE")

    #     # Créer le graphique à barres côte à côte
    bars = alt.Chart(type_accident_chart).mark_bar().encode(
        x=alt.X("TYPES ACCIDENTS:N", axis=alt.Axis(title='TYPE',labelAngle=0),scale=alt.Scale(paddingInner=0)),
        y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre',format="~d")),
        color=alt.Color('TYPES ACCIDENTS:N'),
       
    ).properties(
        title="Les Types d'accident"
    )

    text = bars.mark_text(
    align='center',
    baseline='middle',
    dy=-10,  # Déplace l'étiquette au-dessus de la barre
    color='yellow',
    fontSize=14
    ).encode(
        text=alt.Text('NOMBRE:Q', format='.0f',)
    )
    chart8 = bars + text

    # # Afficher le chart dans Streamlit
    st.altair_chart(chart8, use_container_width=True)


    #-------------------------------------------------------type accident ------------------
    # st.write("Type d'accident par secteur")

    type_accident_chart = filtered_accident.groupby(["TRONÇON","TYPES ACCIDENTS"])["TYPES ACCIDENTS"].count().reset_index(name="NOMBRE")

    #     # Créer le graphique à barres côte à côte
    bars = alt.Chart(type_accident_chart).mark_bar().encode(
        x=alt.X("TYPES ACCIDENTS:N", axis=alt.Axis(title='',labelAngle=0),scale=alt.Scale(paddingInner=0)),
        y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre',format="~d")),
        color=alt.Color('TYPES ACCIDENTS:N'),
       
    ).properties(
        width=350,
        title="Les Types d'accident par TRONÇON"
    )

    text = bars.mark_text(
    align='center',
    baseline='middle',
    dy=-10,  # Déplace l'étiquette au-dessus de la barre
    color='yellow',
    fontSize=14
    ).encode(
        text=alt.Text('NOMBRE:Q', format='.0f',)
    )
    chart8 = bars + text

    type_acci_secteur = chart8.facet(
        facet=alt.Facet('TRONÇON:N', title="TYPES D'ACCIDENT PAR TRONCON"),  # Séparer les graphiques par mois
        columns=10 # Nombre de colonnes dans la grille de facettes
    )

    # # Afficher le chart dans Streamlit
    st.altair_chart(type_acci_secteur, use_container_width=True)
        #-------------------------------------------------------type Victimes ------------------
    # st.write("Type de Victimes")

    # victimes_accident_chart = filtered_accident.groupby(["TRONÇON"])[["BLESSES LEGERS","BLESSES GRAVES","MORTS"]].sum().stack().reset_index(name="NOMBRE")
    
    # # Renommer la colonne level_1 en TYPE DE VICTIMES
    # victimes_accident_chart = victimes_accident_chart.rename(columns={"level_1": "TYPE DE VICTIMES"})
    # #     # Créer le graphique à barres côte à côte
    # chart8 = alt.Chart(victimes_accident_chart).mark_bar().encode(
    #     x=alt.X("TYPE DE VICTIMES:N", axis=alt.Axis(title='TYPE'),scale=alt.Scale(paddingInner=0)),
    #     y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre')),
    #     color=alt.Color('TYPE DE VICTIMES:N'),
       
    # ).properties(
    #     title="Les Victimes"
    # ).configure_axis(
    #     labelAngle=0,
    # )

    # # # Afficher le chart dans Streamlit
    # st.altair_chart(chart8, use_container_width=True)
    #####################################################################################################



# Page: Analyse par tronçon
elif page == "Carburant":
    st.header("Carburant")
    st.sidebar.title("Filtres")
    annee_filter = st.sidebar.multiselect("Sélectionnez l'année",options=carburant['ANNEE'].unique(),default=carburant["ANNEE"].unique())
    # troncon_filter = st.sidebar.multiselect("Sélectionnez le tronçon", options=pat["SECTEUR"].unique(), default=pat["SECTEUR"].unique())
    mois_filter = st.sidebar.multiselect("Sélectionnez la période",options=carburant['MOIS'].unique(),default=carburant["MOIS"].unique())
    # Ordre des mois
    month_order = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
    # carburant['MOIS'] = pd.Categorical(carburant['MOIS'], categories=month_order, ordered=True)
    
    filtered_carburant = carburant[(carburant["ANNEE"].isin(annee_filter)) & (carburant["MOIS"].isin(mois_filter))]
   
    carbu_chart = filtered_carburant.groupby(["ANNEE"])["Quantite"].sum().reset_index()


    # Calculer la variation d'une année à l'autre
    carbu_chart['Variation'] = carbu_chart['Quantite'].diff()
    carbu_chart['Variation %'] = carbu_chart['Quantite'].pct_change() * 100

    # Ajouter une colonne pour les flèches, les couleurs et les variations en pourcentage
    def add_arrow_and_color(value, percent):
        if pd.isna(value):
            return '', 'black', ''
        elif value > 0:
            return f'↑ {percent:.0f}%', 'red', f'{percent:.0f}%'
        elif value < 0:
            return f'↓ {percent:.0f}%', 'green', f'{percent:.0f}%'
        else:
            return '→ 0.0%', 'gray', '0.0%'

    carbu_chart[['Flèche', 'Couleur', 'Variation %']] = carbu_chart.apply(
        lambda row: pd.Series(add_arrow_and_color(row['Variation'], row['Variation %'])),
        axis=1
    )

    print("CONSO BY ANNEE",carbu_chart)
     # Créer le bar chart avec Altair
    bars = alt.Chart(carbu_chart).mark_bar().encode(
    x=alt.X('ANNEE',axis=alt.Axis(labelAngle=0)),
    y=alt.Y('Quantite', axis=alt.Axis(format='~d')),
    # color=alt.Color('ANNEE:N', scale=alt.Scale(scheme='tableau10')),
    # column=alt.Column('ANNEE:N', title='Année')
   ).properties(
   
    title='Evolution Consommation Carburant en (L) par Année et Mois',

    )
    text = bars.mark_text(
    align='center',
    baseline='middle',
    dy=-25,  # Déplace l'étiquette au-dessus de la barre
    color='yellow',
    fontSize=14
    ).encode(
        text=alt.Text('Quantite:Q', format='.0f',)
    )
      # Ajouter les flèches de variation
    arrows = bars.mark_text(
        align='center',
        baseline='middle',
        # dx=-40,  # Déplace l'étiquette avec la flèche au-dessus de l'étiquette de texte
        dy=-10,
        fontSize=16,
        # dx=5,
        # color='red'
    ).encode(
        text='Flèche:N',
        color=alt.Color('Couleur:N', scale=None)  # Utiliser la couleur définie dans la colonne 'Couleur'
    )
    carbuparyear1 = bars + text + arrows

    st.altair_chart(carbuparyear1, use_container_width=True)

   #----------------------------------------------------- annee mois  -----------------------------------------------------------------------  #
    
    carbu_chart = filtered_carburant.groupby(["MOIS","ANNEE"])["Quantite"].sum().reset_index()
    carbu_chart['MOIS'] = pd.Categorical(carbu_chart['MOIS'], categories=month_order, ordered=True)
    carbu_chart['ANNEE'] = pd.Categorical(carbu_chart['ANNEE'], categories=['2022','2023','2024'], ordered=True)
    carbu_chart = carbu_chart.sort_values(['MOIS','ANNEE'])
   
    carbu_chart['Variation'] = carbu_chart.groupby('MOIS')['Quantite'].diff()
    carbu_chart['Variation %'] = carbu_chart.groupby('MOIS')['Quantite'].pct_change() * 100



     # Déterminer les valeurs min et max
    min_value = carbu_chart['Quantite'].min()
    max_value = carbu_chart['Quantite'].max()

  
    def add_arrow_and_color(value, percent):
        if pd.isna(value):
            return '', 'black', ''
        elif value > 0:
            return f'↑ {percent:.0f}%', 'red', f'{percent:.0f}%'
        elif value < 0:
            return f'↓ {percent:.0f}%', 'green', f'{percent:.0f}%'
        else:
            return '→ 0%', 'gray', '0%'

     # # Ajouter une colonne pour la couleur
    def color_code(row):
        if row['Quantite'] == min_value:
            return 'Min'
        elif row['Quantite'] == max_value:
            return 'Max'
        else:
            return str(row['ANNEE'])
    
    carbu_chart['Conso'] = carbu_chart.apply(color_code, axis=1)
    carbu_chart[['Flèche', 'Couleur', 'Variation %']] = carbu_chart.apply(
        lambda row: pd.Series(add_arrow_and_color(row['Variation'], row['Variation %'])),
        axis=1
    )

    color_scale = alt.Scale(domain=[
        'Min', 'Max','2022','2023','2024'
    ], range=[
        'green', 'red', 'steelblue','azure','pink'

    ])
    
    bars = alt.Chart(carbu_chart).mark_bar().encode(
        x=alt.X('ANNEE',axis=alt.Axis(labelAngle=90)),
        y=alt.Y('Quantite', axis=alt.Axis(format='~d')),
        # color=alt.Color('ANNEE:N'),
        # color=alt.Color('Conso:N', scale=color_scale)  # Couleur des barres par combinaison année et consommation
        # column=alt.Column('ANNEE:N', title='Année')
        color=alt.Color('Conso:N', scale=color_scale,)  # Utiliser la couleur définie dans la colonne 'Couleur'
    
    ).properties(
        width=60,  # Largeur des graphiques individuels
        height=300,  # Hauteur des graphiques individuels
        title='Évolution de la Consommation de Carburant (L) par Année et Mois'  # Titre du graphique
    )

    
    # Ajouter des étiquettes de texte aux barres
    text = bars.mark_text(
        align='center',  # Aligner le texte au centre de la barre
        dy=-15,  # Déplacer l'étiquette au-dessus de la barre
        fontSize=10  # Taille de la police
    ).encode(
        text=alt.Text('Quantite:Q', format='.0f')  # Texte de l'étiquette avec formatage sans décimales
    )
       # Ajouter les flèches de variation
    arrows = bars.mark_text(
        align='center',
        baseline='middle',
        # Déplace l'étiquette avec la flèche au-dessus de l'étiquette de texte
        dy=-5,
        fontSize=10,
    ).encode(
        text='Flèche:N',
        color=alt.Color('Couleur:N', scale=None)  # Utiliser la couleur définie dans la colonne 'Couleur'
    )
    # Combiner les barres et les étiquettes de texte
    bars_with_text = bars + text + arrows

    # Appliquer la facette
    carbuparyear = bars_with_text.facet(
        facet=alt.Facet('MOIS:N', sort=month_order, title='MOIS'),  # Séparer les graphiques par mois
        columns=12  # Nombre de colonnes dans la grille de facettes
    )

    st.altair_chart(carbuparyear, use_container_width=True)

 #-----------  by mois ----------   #

    carbu_chart =filtered_carburant.groupby(["MOIS"])["Quantite"].sum().reset_index()
    carbu_chart['MOIS'] = pd.Categorical(carbu_chart['MOIS'], categories=month_order, ordered=True)
    carbu_chart = carbu_chart.sort_values('MOIS')
    carbu_chart['Variation'] = carbu_chart['Quantite'].diff()
    carbu_chart['Variation %'] = carbu_chart['Quantite'].pct_change() * 100
    # Déterminer les valeurs min et max
    min_value = carbu_chart['Quantite'].min()
    max_value = carbu_chart['Quantite'].max()

    print("mois by",carbu_chart)
    # Ajouter une colonne pour les flèches, les couleurs et les variations en pourcentage
    def add_arrow_and_color(value, percent):
        if pd.isna(value):
            return '', 'black', ''
        elif value > 0:
            return f'↑ {percent:.1f}%', 'red', f'{percent:.1f}%'
        elif value < 0:
            return f'↓ {percent:.1f}%', 'green', f'{percent:.1f}%'
        else:
            return '→ 0.0%', 'gray', '0.0%'


    # # Ajouter une colonne pour la couleur
    def color_code(row):
        if row['Quantite'] == min_value:
            return 'Min'
        elif row['Quantite'] == max_value:
            return 'Max'
        else:
            return 'Normal'

    carbu_chart['Conso'] = carbu_chart.apply(color_code, axis=1)
    carbu_chart[['Flèche', 'Couleur', 'Variation %']] = carbu_chart.apply(
        lambda row: pd.Series(add_arrow_and_color(row['Variation'], row['Variation %'])),
        axis=1
    )
     # Créer le bar chart avec Altair
    bars = alt.Chart(carbu_chart).mark_bar().encode(
    x=alt.X('MOIS',sort=month_order,axis=alt.Axis(labelAngle=0)),
    y=alt.Y('Quantite', axis=alt.Axis(format='~d')),
    color=alt.Color('Conso', scale=alt.Scale(domain=['Min', 'Max', 'Normal'], range=['green', 'red', 'steelblue']))
    # column=alt.Column('ANNEE', title='ANNEE')
    ).properties(
    title='Evolution Consommation Carburant en (L) par mois:'
    ) 
    text= alt.Chart(carbu_chart).mark_text(
    align='center',
    baseline='middle',
    dy=-25,  # Déplace l'étiquette au-dessus de la barre
    # color='red',
    fontSize=12
    ).encode(
        text=alt.Text('Quantite:Q', format='.0f',)
    )
      # Ajouter les flèches de variation
    arrows = bars.mark_text(
        align='center',
        baseline='middle',
        # Déplace l'étiquette avec la flèche au-dessus de l'étiquette de texte
        dy=-10,
        fontSize=16,
    ).encode(
        text='Flèche:N',
        color=alt.Color('Couleur:N', scale=None)  # Utiliser la couleur définie dans la colonne 'Couleur'
    )
    carbuparmois = bars + text + arrows
    st.altair_chart(carbuparmois, use_container_width=True)
    
    # Graphiques par tronçon
    # for troncon in troncon_filter:
    #     st.subheader(f"Tronçon {troncon}")
    #     troncon_data = filtered_data[filtered_data["troncon"] == troncon]
        
    #     fig, ax = plt.subplots(figsize=(10, 6))
    #     sns.lineplot(x="date", y="vehicles", data=troncon_data, ax=ax)
    #     ax.set_title(f"Trafic des véhicules pour {troncon}")
    #     st.pyplot(fig)
        
    #     fig, ax = plt.subplots(figsize=(10, 6))
    #     sns.lineplot(x="date", y="revenue", data=troncon_data, ax=ax)
    #     ax.set_title(f"Revenus générés pour {troncon}")
    #     st.pyplot(fig)

# Page: Données brutes
# else:
#     st.header("Données brutes")
#     st.write("Afficher toutes les données non filtrées:")
#     st.dataframe(data)

# Pied de page
st.sidebar.markdown("## - MSA SERVICES 2024")

# import streamlit as st
# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Fonction pour générer des données simulées
# def generate_data():
#     np.random.seed(42)
#     dates = pd.date_range("20230101", periods=100)
#     data = pd.DataFrame(np.random.randn(100, 4), index=dates, columns=list("ABCD"))
#     data["category"] = np.random.choice(["Category 1", "Category 2", "Category 3"], size=100)
#     return data

# # Charger les données
# data = generate_data()

# # Configuration de la page
# st.set_page_config(
#     page_title="Tableau de Bord Streamlit",
#     layout="wide",
# )

# # Titre principal
# st.title("Tableau de Bord Streamlit")

# # Barre latérale pour la navigation et les filtres
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Aller à", ["Vue d'ensemble", "Analyse détaillée", "Données brutes"])

# # Filtres
# st.sidebar.title("Filtres")
# category_filter = st.sidebar.multiselect("Sélectionnez la catégorie", options=data["category"].unique(), default=data["category"].unique())

# # Filtrer les données
# filtered_data = data[data["category"].isin(category_filter)]

# # Page: Vue d'ensemble
# if page == "Vue d'ensemble":
#     st.header("Vue d'ensemble")
    
#     st.write("Aperçu des données filtrées:")
#     st.dataframe(filtered_data)
    
#     st.write("Graphique des données:")
#     st.line_chart(filtered_data[["A", "B", "C", "D"]])

# # Page: Analyse détaillée
# elif page == "Analyse détaillée":
#     st.header("Analyse détaillée")
    
#     # Graphiques
#     fig, ax = plt.subplots(figsize=(10, 6))
#     sns.histplot(filtered_data["A"], bins=30, ax=ax, kde=True)
#     ax.set_title("Distribution de la colonne A")
#     st.pyplot(fig)
    
#     fig, ax = plt.subplots(figsize=(10, 6))
#     sns.boxplot(x="category", y="B", data=filtered_data, ax=ax)
#     ax.set_title("Boxplot de la colonne B par catégorie")
#     st.pyplot(fig)

# # Page: Données brutes
# else:
#     st.header("Données brutes")
#     st.write("Afficher toutes les données non filtrées:")
#     st.dataframe(data)

# # Pied de page
# st.sidebar.markdown("Créé avec Streamlit")


# st.sidebar.header("Options")
# texte_sidebar = st.sidebar.text_input("Entrez du texte","Abraham")


# header=st.container()
# pat=st.container()
# event=st.container()




# with header:
#     title=st.title("Rapport du Tracé JUIN 2024")
#     st.text("Ce rapport couvre la periode du 1 au 30 juin 2024 pour le tronçon AMT TT et PONT FOUNDIOUGNE")


# with pat:
#     st.header("La Patrouille")
#     st.text("Pour la patrouille la distance parcourue est")
#     st.markdown("* **TT :**")
#     st.markdown("* **AMT :**")
#     st.markdown("* **FOUNDIOUGNE :**")




# with event:
#     st.header("Les Evenements du tracé")
#     col1,_,col2=st.columns([2,1,2])
#     nbre = col1.slider('Nombre: ',10,100,20,5)
#     # tr = col1.selectbox('TRONÇON: ',options=['AMT','TT','FOUNDIOUGNE'],index=0)
#     tr=col1.selectbox('TRONÇON: ',['AMT','TT','FOUNDIOUGNE'])
#     mois = col1.text_input("Le mois du rapport :")
#     col2.subheader("Le Tronçon")
#     col2.write(tr)
#     col2.subheader("Le mois")
#     col2.write(mois)