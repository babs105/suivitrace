import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt


# Paramétrer la locale en français pour formater les dates
# locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

# Fonction pour générer des données simulées

def generate_toll_data():
    data=pd.read_excel('data/PAT/PAT-JUIN-2024.xlsx')
    data[data.isna()]=0
    trace=pd.read_excel('data/TRACE/EVENT-JUIN-2024.xlsx')
    accident=pd.read_excel('data/TRACE/ACCI-JUIN-2024.xlsx')
    
    return data,trace,accident



# Charger les données
data,trace,accident = generate_toll_data()
# Ajouter une colonne avec les dates formatées en français
data['DATE_FR'] = data['DATE'].dt.strftime('%d/%m/%Y')
trace['DATE_FR'] = trace['DATE'].dt.strftime('%d/%m/%Y')
accident['DATE_FR'] = accident['DATE'].dt.strftime('%d/%m/%Y')
# print(trace.head())

# Configuration de la page
st.set_page_config(
    page_title="Tableau de Bord ",
    layout="wide",
)

# Titre principal
st.title("RAPPORT MOIS DE JUIN AUTOROUTE A PEAGE")

# Barre latérale pour la navigation et les filtres
st.sidebar.title("Navigation")
# page = st.sidebar.radio("Aller à", ["Vue d'ensemble", "Analyse par tronçon", "Données brutes"])
page = st.sidebar.radio("Aller à", ["Vue d'ensemble",])

# Filtres
st.sidebar.title("Filtres")
troncon_filter = st.sidebar.multiselect("Sélectionnez le tronçon", options=data["SECTEUR"].unique(), default=data["SECTEUR"].unique())
date_filter = st.sidebar.date_input("Sélectionnez la période", value=[data["DATE"].min(), data["DATE"].max()])
# date_filter = st.sidebar.date_input("Sélectionnez la période", value=[data["date"].min(), data["date"].max()])
start_date = pd.to_datetime(date_filter[0])
end_date = pd.to_datetime(date_filter[1])
# Filtrer les données
filtered_data = data[(data["SECTEUR"].isin(troncon_filter)) & (data["DATE"].between(start_date, end_date))]
distance_totale = filtered_data["DISTANCE PARCOURUE"].sum()


filtered_trace = trace[(trace["SECTEUR LIEU"].isin(troncon_filter)) & (trace["DATE"].between(start_date, end_date))]
filtered_trace["NATURE EVENEMENT"] = filtered_trace["NATURE EVENEMENT"].where(filtered_trace["NATURE EVENEMENT"].isin(['ACCIDENT', 'PANNE','INCIDENT','VEHICULE EN FEU']),other="AUTRES")

nbre_total_event = filtered_trace["SECTEUR LIEU"].count()
filtered_trace_rom = filtered_trace[filtered_trace['STATUT REMORQUAGE OU PATROUILLE']=="remorqué"]
nbre_total_rom = filtered_trace.loc[filtered_trace['STATUT REMORQUAGE OU PATROUILLE']=="remorqué","STATUT REMORQUAGE OU PATROUILLE"].count()

filtered_accident = accident[(accident["TRONÇON"].isin(troncon_filter)) & (accident["DATE"].between(start_date, end_date))]
nbre_total_acci = filtered_accident['TRONÇON'].count()

# print("test",filtered_trace.head())
# Page: Vue d'ensemble
if page == "Vue d'ensemble":
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
    st.write("LA PATROUILLE:")
    st.write(f" Distance totale parcourue: :red[{distance_totale}] Km sur {secteur}")
    distance_secteur_chart = filtered_data.groupby("SECTEUR")["DISTANCE PARCOURUE"].sum().reset_index()
    # Trier les données par ordre décroissant de 'NOMBRE'
    distance_secteur_chart_sorted = distance_secteur_chart.sort_values(by='DISTANCE PARCOURUE', ascending=False)

    # Créer le bar chart avec Altair
    chart = alt.Chart(distance_secteur_chart_sorted).mark_bar().encode(
    x=alt.X('SECTEUR', axis=alt.Axis(labelAngle=0),scale=alt.Scale(paddingInner=0.5)),
    y=alt.Y('DISTANCE PARCOURUE', axis=alt.Axis(format='~s')),
    color=alt.Color('SECTEUR')
    ).properties(
    title='Distance Parcourue en (km) par Secteur'
    ) 
    st.altair_chart(chart, use_container_width=True)

    distance_chart = filtered_data.groupby("DATE_FR")["DISTANCE PARCOURUE"].sum().reset_index()
     # Créer le bar chart avec Altair
    chart1 = alt.Chart(distance_chart).mark_line().encode(
    x=alt.X('DATE_FR', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('DISTANCE PARCOURUE', axis=alt.Axis(format='~s')),
    # color='DATE'
    ).properties(
    title='Evolution Distance Parcourue en (km):'
    ) 
    st.altair_chart(chart1, use_container_width=True)
    
    ################################################# event ###############################################
    st.write("LES EVENEMENTS:")
    st.write(f" Nombre Total Evenement: :red[{nbre_total_event}]  sur  {secteur}")

    event_secteur_chart = filtered_trace.groupby("SECTEUR LIEU")["SECTEUR LIEU"].count().reset_index(name='NOMBRE')
      # Créer le bar chart avec Altair
    chart2 = alt.Chart(event_secteur_chart).mark_bar().encode(
    x=alt.X('SECTEUR LIEU', axis=alt.Axis(labelAngle=0),scale=alt.Scale(paddingInner=0.5)),
    y=alt.Y('NOMBRE', axis=alt.Axis(format='~s')),
    color=alt.Color('SECTEUR LIEU', scale=alt.Scale(scheme='tableau10'))
    ).properties(
    title='EVENEMENT PAR SECTEUR'
    ) 
    # Afficher le chart dans Streamlit
    st.altair_chart(chart2, use_container_width=True)
    #-------------------------------- evolution des event --------------

    st.write(f"")
  

    evolu_chart = filtered_trace.groupby("DATE_FR")["SECTEUR LIEU"].count().reset_index(name='NOMBRE')
     # Créer le bar chart avec Altair
    # print("evo",evolu_chart)
    chart6 = alt.Chart(evolu_chart).mark_line().encode(
    x=alt.X('DATE_FR', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('NOMBRE', axis=alt.Axis(format='~s')),
    # color=alt.Color('SECTEUR LIEU', scale=alt.Scale(scheme='tableau10'))
    ).properties(
    title=f"Evolution  Nombre  evénèments  :{secteur}"
    ) 
    st.altair_chart(chart6, use_container_width=True)



    #-------------------------------------------------------nature EVENT-----------------------------------------
    st.write(f"Nature Evenement :")

    nature_event_secteur_chart = filtered_trace.groupby(['DATE_FR',"NATURE EVENEMENT"])["NATURE EVENEMENT"].count().reset_index(name="NOMBRE")

    print(nature_event_secteur_chart)
        # Créer le graphique à barres côte à côte
    chart3 = alt.Chart(nature_event_secteur_chart).mark_line().encode(
        # x=alt.X('NATURE EVENEMENT:N', axis=alt.Axis(title='Secteur'),scale=alt.Scale(paddingInner=0)),
        x=alt.X('DATE_FR', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre')),
        color=alt.Color('NATURE EVENEMENT:N'),
        # column=alt.Column('SECTEUR LIEU:N', title='Secteur')
    ).properties(
        title=f"Evolution Nature des Evènements : {secteur}"
    ).configure_axis(
        labelAngle=0,
    )
    st.altair_chart(chart3, use_container_width=True)

    st.write(f"Nature Evenement :")

    nature_event_secteur_chart1 = filtered_trace.groupby("NATURE EVENEMENT")["NATURE EVENEMENT"].count().reset_index(name="NOMBRE")

    print(nature_event_secteur_chart1)
        # Créer le graphique à barres côte à côte
    chart10 = alt.Chart(nature_event_secteur_chart1).mark_bar().encode(
        x=alt.X('NATURE EVENEMENT:N', axis=alt.Axis(title=f"Secteur {secteur}"),scale=alt.Scale(paddingInner=0)),
        y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre')),
        color=alt.Color('NATURE EVENEMENT:N'),
        # column=alt.Column('SECTEUR LIEU:N', title='Secteur')
    ).properties(
        title='Répartition des événements par Nature'
    ).configure_axis(
        labelAngle=0,
    )
    st.altair_chart(chart10, use_container_width=True)
    #-------------------------------------------------------------------------------------------------



    #-------------------------------------------------------- statut event -----------------------------
    st.write(f"Statut Evenement:")

    event_statut_secteur_chart = filtered_trace.groupby("STATUT REMORQUAGE OU PATROUILLE")["NATURE EVENEMENT"].count().reset_index(name="NOMBRE")

        # Créer le graphique à barres côte à côte
    chart4 = alt.Chart(event_statut_secteur_chart).mark_bar().encode(
        x=alt.X('STATUT REMORQUAGE OU PATROUILLE:N', axis=alt.Axis(title=f"Secteur {secteur}"),scale=alt.Scale(paddingInner=0)),
        y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre')),
        color=alt.Color('STATUT REMORQUAGE OU PATROUILLE:N'),
        # column=alt.Column('SECTEUR LIEU:N', title='SECTEUR')
    ).properties(
        width=100,
        title=f'Répartition des evenements par statut : {secteur}'
    ).configure_axis(
        labelAngle=0,
    )


    # Afficher le chart dans Streamlit
    st.altair_chart(chart4, use_container_width=True)

        #--------------------------------------------------------
    st.write(f"Remorquage:")
    st.write(f" Nombre Total de Véhicule Remorqués: :red[{nbre_total_rom}] ")

    

    rom_secteur_chart = filtered_trace_rom.groupby("TYPES DE VEHICULE")["TYPES DE VEHICULE"].count().reset_index(name="NOMBRE")
    chart5 = alt.Chart(rom_secteur_chart).mark_bar().encode(
        x=alt.X('TYPES DE VEHICULE:N', axis=alt.Axis(title='TYPE VEHICULE'),scale=alt.Scale(paddingInner=0)),
        y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre')),
        color=alt.Color('TYPES DE VEHICULE:N'),
       
    ).properties(
        title='Répartition des Types de Vehicule remorqué'
    ).configure_axis(
        labelAngle=0,
    )

    # Afficher le chart dans Streamlit
    st.altair_chart(chart5, use_container_width=True)
    ############################################## accident #########################################################
    st.write(f"Accident:")
    st.write(f" Nombre Total d'Accident: :red[{nbre_total_acci}] ")

    

    accident_chart = filtered_accident.groupby("TRONÇON")["TRONÇON"].count().reset_index(name="NOMBRE")

    # Créer le graphique à barres côte à côte
    chart7 = alt.Chart(accident_chart).mark_bar().encode(
        x=alt.X('TRONÇON:N', axis=alt.Axis(title='Secteur'),scale=alt.Scale(paddingInner=0)),
        y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre')),
        color=alt.Color('TRONÇON:N'),
       
    ).properties(
        title="Nombre d'accident"
    ).configure_axis(
        labelAngle=0,
    )

    # Afficher le chart dans Streamlit
    st.altair_chart(chart7, use_container_width=True)
    #-------------------------------------------------------type accident ------------------
    st.write("Type d'accident")

    type_accident_chart = filtered_accident.groupby("TYPES ACCIDENTS")["TYPES ACCIDENTS"].count().reset_index(name="NOMBRE")

    #     # Créer le graphique à barres côte à côte
    chart8 = alt.Chart(type_accident_chart).mark_bar().encode(
        x=alt.X("TYPES ACCIDENTS:N", axis=alt.Axis(title='TYPE'),scale=alt.Scale(paddingInner=0)),
        y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre')),
        color=alt.Color('TYPES ACCIDENTS:N'),
       
    ).properties(
        title="Les Types d'accident"
    ).configure_axis(
        labelAngle=0,
    )

    # # Afficher le chart dans Streamlit
    st.altair_chart(chart8, use_container_width=True)
        #-------------------------------------------------------type Victimes ------------------
    st.write("Type de Victimes")

    victimes_accident_chart = filtered_accident.groupby(["TRONÇON"])[["BLESSES LEGERS","BLESSES GRAVES","MORTS"]].sum().stack().reset_index(name="NOMBRE")
    
    print(victimes_accident_chart)
    # Renommer la colonne level_1 en TYPE DE VICTIMES
    victimes_accident_chart = victimes_accident_chart.rename(columns={"level_1": "TYPE DE VICTIMES"})
    print(victimes_accident_chart)
    #     # Créer le graphique à barres côte à côte
    chart8 = alt.Chart(victimes_accident_chart).mark_bar().encode(
        x=alt.X("TYPE DE VICTIMES:N", axis=alt.Axis(title='TYPE'),scale=alt.Scale(paddingInner=0)),
        y=alt.Y('NOMBRE:Q', axis=alt.Axis(title='Nombre')),
        color=alt.Color('TYPE DE VICTIMES:N'),
       
    ).properties(
        title="Les Victimes"
    ).configure_axis(
        labelAngle=0,
    )

    # # Afficher le chart dans Streamlit
    st.altair_chart(chart8, use_container_width=True)
    #####################################################################################################



# Page: Analyse par tronçon
elif page == "Analyse par tronçon":
    st.header("Analyse par tronçon")
    
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