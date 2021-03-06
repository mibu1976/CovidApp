# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

df = pd.read_csv("owid-covid-data.csv")




app.layout = html.Div([
    
        
    html.H1("Covid-19 Dashboard with Dash", style = {'text-align': 'center'}),
    html.H4("Numbers and facts about Covid-19", style = {'text-align': 'left'}),

    dcc.Dropdown(id='location',
                 options = [
                     {"label": "Germany", "value": 'Germany'},
                     {"label": "France", "value": 'France'},
                     {"label": "Austria", "value": 'Austria'},
                     {"label": "Slovenia", "value": 'Slovenia'},
                     {"label": "Netherlands", "value": 'Netherlands'},
                     {"label": "Nigeria", "value": 'Nigeria'},
                     {"label": "Switzerland", "value": 'Switzerland'}],
                 multi = False,
                 value='Germany',
                 style = {"width": "40%"}),
    
        
    dcc.Graph(id='covidplot', figure = {}),
    html.Br(),
    
    dcc.Graph(id='covidplot2', figure = {})
])

@app.callback(
    [Output(component_id='covidplot', component_property='figure'),
     Output(component_id='covidplot2', component_property='figure')],
    [Input(component_id='location', component_property='value')]
)




def update_graph(option_slctd):
    #print(option_slctd)
    #print(type(option_slctd))

    

    dff = df.copy()
    dff = dff[dff["location"] == option_slctd]
    

    
# Plotly Express
    fig = px.line(dff, x='date', y='new_cases')

    fig2 = px.scatter(dff, x="new_cases", y="new_deaths", 
                     color = "new_tests", size = "tests_per_case",
                     marginal_x = "box", marginal_y = "violin", trendline = "ols")


    return fig, fig2


if __name__ == '__main__':
    app.run_server(debug=True)
