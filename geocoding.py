# Exécute le code suivant :
import requests
link = 'https://api-adresse.data.gouv.fr/search/?q=728+Route+de+Villerest&postcode=42155'
r = requests.get(link).json()
r


# Crée ici une fonction qui transforme une adresse postale en URL de requête pour l'API Adresse,
# puis effectue la requête et retourne les coordonnées :


def API_adresse(adresse):
  #adresse=''
  adresse=adresse.replace(' ','+')
  link_main = 'https://api-adresse.data.gouv.fr/search/?q='
  link = link_main + adresse
  import requests

  r = requests.get(link).json()

  point = r['features'][0]['geometry']['coordinates'][::-1]


  return point



#CHALLENGE
import pandas as pd
restaurants = pd.DataFrame([["Polypode","6 place du Champgil, Clermont-Ferrand, 63000"],
                            ["Jean-Claude Leclerc", "12 rue St-Adjutor, Clermont-Ferrand, 63000"],
                            ["L'Écureuil", "18 rue St-Adjutor, Clermont-Ferrand, 63000"],
                            ["Le Saint-Eutrope", "4 rue St-Eutrope, Clermont-Ferrand, 63000"]],
                           columns = ["nom", "adresse"])

restaurants




restaurants['adresse'].info()
restaurants['coordonnees']=restaurants['adresse'].convert_dtypes('string')

restaurants['coordonnees'].info()

restaurants['coordonnees']=restaurants['coordonnees'].apply(API_adresse)

import folium

m = folium.Map(location=restaurants['coordonnees'][0],zoom_start=7)

for index, ligne in restaurants.iterrows():



  folium.Marker(
     location=ligne['coordonnees'],
     popup=ligne['nom']
      ).add_to(m)
m