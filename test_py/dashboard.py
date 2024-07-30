import pandas as pd
import json
import matplotlib.pyplot as plt
import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objs as go
from dash.dependencies import Input, Output


df = pd.read_csv('X_train_update.csv', index_col = 0)
df2 = pd.read_csv('Y_train_CVw08PX.csv', index_col = 0)

with open('../shared_volume/data/code2type.json', 'r') as jf:
    code2type_json = json.load(jf)

#print(code2type_json)

code2type = code2type_json[0]
df = pd.concat([df, df2], axis = 1)

prdtypecode_counts = df.groupby('prdtypecode').size()



prdtypecode_counts = df.groupby('prdtypecode').size().reset_index(name='counts')
prdtypecode_counts['prdtypecode'] = prdtypecode_counts['prdtypecode'].astype(str)
prdtypecode_counts['type'] = prdtypecode_counts['prdtypecode'].map(code2type)

app = dash.Dash(__name__)

# Définir la mise en page de l'application
app.layout = html.Div(children=[
    # Première section
    html.Div(children=[
        html.H1(children="Données d'entrainement - Histogramme prdtypecode"),
        
        dcc.Graph(
            id='histogram',
            figure={
                'data': [
                    go.Bar(
                        x=prdtypecode_counts['type'],
                        y=prdtypecode_counts['counts'],
                        text=prdtypecode_counts['counts'],
                        textposition='auto',  # Affiche les valeurs au-dessus des barres
                        insidetextanchor='end',  # Ajuste l'ancrage du texte
                        marker=dict(color='skyblue', line=dict(color='black', width=1))
                    )
                ],
                'layout': go.Layout(
                    title='Nombre de produits par prdtypecode',
                    xaxis={'title': 'prdtypecode', 'tickangle': 270, 'automargin': True, 'title_standoff': 10},
                    yaxis={'title': 'Nombre de produits'},
                    bargap=0.2,  # Pour espacer les barres
                    plot_bgcolor='white',
                    yaxis_gridcolor='lightgray',  # Couleur de la grille
                    yaxis_gridwidth=0.7,  # Largeur de la grille
                )
            }
        )
    ]),

    # Deuxième section
    html.Div(children=[
        html.H1(children="Nouvelles données - Histogramme prdtypecode"),

        dcc.Graph(
            id='histogram2',
            figure={
                'data': [
                    go.Bar(
                        x=prdtypecode_counts['type'],
                        y=prdtypecode_counts['counts']/10,
                        text=prdtypecode_counts['counts']/10,
                        textposition='outside',  # Affiche les valeurs au-dessus des barres
                        marker=dict(color='orange', line=dict(color='black', width=1))
                    )
                ],
                'layout': go.Layout(
                    title='Nombre de produits par prdtypecode',
                    xaxis={'title': 'prdtypecode', 'tickangle': 270, 'automargin': True, 'title_standoff': 10},
                    yaxis={'title': 'Nombre de produits'},
                    bargap=0.2,  # Pour espacer les barres
                    plot_bgcolor='white',
                    yaxis_gridcolor='lightgray',  # Couleur de la grille
                    yaxis_gridwidth=0.7,  # Largeur de la grille
                )
            }
        )
    ])
])

# Exécuter l'application
if __name__ == '__main__':
    app.run_server(debug=True)