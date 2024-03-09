#import pygal.maps.world

import time
from tracemalloc import start

import numpy as np

from pandas import Series, DataFrame

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.backends.backend_agg import FigureCanvas  # not needed for mpl >= 3.1

import mplleaflet
from IPython.display import IFrame

import base64
from PIL import Image
import io

import hvplot.pandas

import requests # Pour effectuer la requête
import pandas as pd # Pour manipuler les données
import datetime as dt

import param
import panel as pn

import plotly.express as px

import mysql.connector

import dash
#from sklearn.datasets import load_wine
from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

from alpha_vantage.timeseries import TimeSeries

from dash.dash_table import DataTable

#########################################################################################################################################################################

df_soixante_quinze_plus_done = pd.read_csv("soixante_quinze_plus.csv")

values_region_name_unique = df_soixante_quinze_plus_done['Region Name'].unique()
values_year_unique   = df_soixante_quinze_plus_done['Year'].unique()
values_country_name_unique  = df_soixante_quinze_plus_done['Country Name'].unique()


def create_country_chart(values_region_name_unique='Europe', values_year_unique=1987):
    filtered_df = df_soixante_quinze_plus_done[(df_soixante_quinze_plus_done['Region Name']== values_region_name_unique) & (df_soixante_quinze_plus_done['Year']==values_year_unique)]
    filtered_df = filtered_df.sort_values(by="Death rate per 100 000 population", ascending=False).head(100)

    bar_fig = px.bar(filtered_df, x="Country Code", y='Death rate per 100 000 population', color="Age Group", 
    template="seaborn", title=f"{values_region_name_unique} vs {values_year_unique}", text_auto=True)
    bar_fig.update_layout(paper_bgcolor='#e5ecf6', height=600)
    
    return bar_fig

multi_select_region_name = dcc.Dropdown(id='multi_select_region_name', options=values_region_name_unique, value='Europe', clearable=False)
multi_select_country_name = dcc.Dropdown(id='multi_select_country_name', options=values_country_name_unique, value='South Africa', clearable=False)

multi_select_year = dcc.Dropdown(id='multi_select_year', options=values_year_unique, value=1987, clearable=False)

#########################################################################################################################################################################

df_soixante_quinze_plus_done = pd.read_csv("soixante_quinze_plus.csv")

values_region_name_unique = df_soixante_quinze_plus_done['Region Name'].unique()
values_year_region_unique   = df_soixante_quinze_plus_done['Year'].unique()
values_country_name_unique  = df_soixante_quinze_plus_done['Country Name'].unique()


def create_region_chart(values_region_name_unique='Europe', values_year_region_unique=1987):
    filtered_df = df_soixante_quinze_plus_done[(df_soixante_quinze_plus_done['Region Name']== values_region_name_unique) & (df_soixante_quinze_plus_done['Year']==values_year_region_unique)]
    filtered_df = filtered_df.sort_values(by="Death rate per 100 000 population", ascending=False).head(20)

    bar_fig = px.bar(filtered_df, x="Country Code", y='Death rate per 100 000 population', color="Age Group", 
    template="seaborn", title=f"{values_region_name_unique} vs {values_year_region_unique}", text_auto=True)
    bar_fig.update_layout(paper_bgcolor='#e5ecf6', height=600)
    
    return bar_fig

select_region_name = dcc.Dropdown(id='select_region_name', options=values_region_name_unique, value='Europe', clearable=False)
select_country_name = dcc.Dropdown(id='select_country_name', options=values_country_name_unique, value='Mauritius', clearable=False)

select_year_region = dcc.Dropdown(id='select_year_region', options=values_year_region_unique, value=1987, clearable=False)

#########################################################################################################################################################################

df_soixante_quinze_plus_done = pd.read_csv("soixante_quinze_plus.csv")

values_region_name_unique = df_soixante_quinze_plus_done['Region Name'].unique()
values_year_region_unique   = df_soixante_quinze_plus_done['Year'].unique()
values_country_name_unique  = df_soixante_quinze_plus_done['Country Name'].unique()

numeric_values_density_heatmap = ['Death rate per 100 000 population', 'Percentage of cause-specific deaths out of total deaths', 'Age-standardized death rate per 100 000 standard population']

def create_country_name_density_heatmap(values_region_name_unique='Europe', values_year_region_unique=1987, numeric_values_density_heatmap = ['Death rate per 100 000 population', 
'Percentage of cause-specific deaths out of total deaths']):
    filtered_df_density_heatmap = df_soixante_quinze_plus_done[(df_soixante_quinze_plus_done['Region Name']== values_region_name_unique) 
    & (df_soixante_quinze_plus_done['Year']== values_year_region_unique)]
    filtered_df_density_heatmap = filtered_df_density_heatmap.sort_values(by="Death rate per 100 000 population", ascending=False).head(20)
    bar_fig = px.density_heatmap(filtered_df_density_heatmap, x="Country Name", y=numeric_values_density_heatmap, z='Number', template="seaborn",
    color_continuous_scale="Viridis", title=f"{values_region_name_unique} vs {values_year_region_unique} / {numeric_values_density_heatmap}", text_auto=True)
    bar_fig.update_layout(paper_bgcolor='#e5ecf6', height=600)
    
    return bar_fig
    

multi_select_region_name_density_heatmap = dcc.Dropdown(id='multi_select_region_name_density_heatmap', options=values_region_name_unique, value='Europe', clearable=False)
multi_select_country_name_density_heatmap = dcc.Dropdown(id='multi_select_country_name_density_heatmap', options=values_country_name_unique, value='South Europe', clearable=False)
multi_select_year_density_heatmap = dcc.Dropdown(id='multi_select_year_density_heatmap', options=values_year_region_unique, value=1987, clearable=False)
multi_select_numeric_density_heatmap = dcc.Dropdown(id='multi_select_numeric_density_heatmap', options=numeric_values_density_heatmap, 
value='Death rate per 100 000 population', clearable=False)

#########################################################################################################################################################################

df_soixante_quinze_plus_done = pd.read_csv("soixante_quinze_plus.csv")

region_name_unique = df_soixante_quinze_plus_done['Region Name'].unique()
year_unique   = df_soixante_quinze_plus_done['Year'].unique()
country_name_unique  = df_soixante_quinze_plus_done['Country Name'].unique()

numeric_values_map = ['Death rate per 100 000 population', 'Percentage of cause-specific deaths out of total deaths', 'Age-standardized death rate per 100 000 standard population']

def create_country_choropleth_map(region_name_unique="Europe", year_unique=1987, numeric_values_map='Death rate per 100 000 population'):
    filtered_df_map = df_soixante_quinze_plus_done[(df_soixante_quinze_plus_done['Region Name'] == region_name_unique) 
    & (df_soixante_quinze_plus_done['Year'] == year_unique)]
    filtered_df_map = filtered_df_map.sort_values(by="Death rate per 100 000 population", ascending=False).head(20)

    fig = px.choropleth(filtered_df_map, color='Age Group', locations='Country Name', locationmode='ISO-3', color_continuous_scale='RdYlBu',
                        title=f"{region_name_unique} vs {year_unique} / {numeric_values_map}")
                        
    fig.update_layout(dragmode=False, paper_bgcolor='#e5ecf6', height=600, margin={"l":0, "r":0})
    return fig


multi_select_region_name_choropleth_map = dcc.Dropdown(id='multi_select_region_name_choropleth_map', options=region_name_unique, value='Europe', clearable=False)
multi_select_year_choropleth_map = dcc.Dropdown(id='multi_select_year_choropleth_map', options=year_unique, value=1987, clearable=False)
multi_select_numeric_choropleth_map = dcc.Dropdown(id='multi_select_numeric_choropleth_map', options=numeric_values_map, 
value='Death rate per 100 000 population', clearable=False)

#########################################################################################################################################################################

df_soixante_quinze_plus_done = pd.read_csv("soixante_quinze_plus.csv")

region_name_unique_pie = df_soixante_quinze_plus_done['Region Name'].unique()
year_unique_pie   = df_soixante_quinze_plus_done['Year'].unique()
country_name_unique_pie  = df_soixante_quinze_plus_done['Country Name'].unique()

numeric_values_pie = ['Death rate per 100 000 population', 'Percentage of cause-specific deaths out of total deaths', 'Age-standardized death rate per 100 000 standard population']


def create_region_name_pie(region_name_unique_pie='Europe', year_unique_pie=1987):

    filtered_df_region_name_pie = df_soixante_quinze_plus_done[(df_soixante_quinze_plus_done['Region Name'] == region_name_unique_pie) 
    & (df_soixante_quinze_plus_done['Year'] == year_unique_pie)]
    filtered_df_region_name_pie = filtered_df_region_name_pie.sort_values(by="Death rate per 100 000 population", ascending=False).head(20)

    pie_fig = px.pie(filtered_df_region_name_pie, values="Death rate per 100 000 population", names="Country Name", template="seaborn",
    hover_data="Country Name", custom_data="Country Name", title=f"{region_name_unique_pie} vs {year_unique_pie}")
    pie_fig.update_layout(paper_bgcolor='#e5ecf6', height=600)

    return pie_fig

multi_select_region_pie = dcc.Dropdown(id='multi_select_region_pie', options=region_name_unique_pie, value='Europe', clearable=False)
multi_select_year_pie = dcc.Dropdown(id='multi_select_year_pie', options=year_unique_pie, value=1987, clearable=False)

#########################################################################################################################################################################

df_soixante_quinze_plus_done = pd.read_csv("soixante_quinze_plus.csv")

region_name_unique_pie = df_soixante_quinze_plus_done['Region Name'].unique()
year_unique_pie   = df_soixante_quinze_plus_done['Year'].unique()
country_name_unique_pie  = df_soixante_quinze_plus_done['Country Name'].unique()

numeric_values_pie = ['Death rate per 100 000 population', 'Percentage of cause-specific deaths out of total deaths', 'Age-standardized death rate per 100 000 standard population']


def create_country_name_pie(region_name_unique_pie='Europe', year_unique_pie=1987):

    filtered_df_country_name_pie = df_soixante_quinze_plus_done[(df_soixante_quinze_plus_done['Region Name'] == region_name_unique_pie) 
    & (df_soixante_quinze_plus_done['Year'] == year_unique_pie)]
    filtered_df_country_name_pie = filtered_df_country_name_pie.sort_values(by="Death rate per 100 000 population", ascending=False).head(20)

    pie_fig = px.pie(filtered_df_country_name_pie, values="Death rate per 100 000 population", names="Age Group", template="seaborn",
    hover_data="Age Group", custom_data="Age Group", title=f"{region_name_unique_pie} vs {year_unique_pie}")
    pie_fig.update_layout(paper_bgcolor='#e5ecf6', height=600)

    return pie_fig

multi_select_region_name_pie = dcc.Dropdown(id='multi_select_region_name_pie', options=region_name_unique_pie, value='Europe', clearable=False)
multi_select_year_country_pie = dcc.Dropdown(id='multi_select_year_country_pie', options=year_unique_pie, value=1987, clearable=False)

#########################################################################################################################################################################

indicator_sum = go.FigureWidget(
    go.Indicator(
        mode="gauge+number",
        value=df_soixante_quinze_plus_done['Death rate per 100 000 population'].sum(),
        title={'text':'Total Death Rate'},
    )
)
indicator_sum.update_layout(title="", height=250)

indicator_max = go.FigureWidget(
    go.Indicator(
        mode="gauge+number",    
        value=df_soixante_quinze_plus_done['Death rate per 100 000 population'].max(),                                                         
        title={'text':'Maximum Death Rate'},
    )
)
indicator_max.update_layout(title="", height=250)

indicator_avg = go.FigureWidget(
    go.Indicator(
        mode="gauge+number",
        value=df_soixante_quinze_plus_done['Death rate per 100 000 population'].mean(),
        title={'text':'Average Death Rate'},
    )
)
indicator_avg.update_layout(title="", height=250)

indicator_min = go.FigureWidget(
    go.Indicator(
        mode="gauge+number",
        value=df_soixante_quinze_plus_done['Death rate per 100 000 population'].min(),
        title={'text':'Minimum Death Rate'},
    )
)
indicator_min.update_layout(title="", height=250)

#########################################################################################################################################################################

df_soixante_quinze_plus_done = pd.read_csv("soixante_quinze_plus.csv")

values_region_name_unique = df_soixante_quinze_plus_done['Region Name'].unique()
values_year_unique   = df_soixante_quinze_plus_done['Year'].unique()
values_country_name_unique  = df_soixante_quinze_plus_done['Country Name'].unique()

fig = px.line(x=df_soixante_quinze_plus_done['Region Name'], y=df_soixante_quinze_plus_done['Death rate per 100 000 population'], height=600)

multi_select_region_radio = dcc.Dropdown(id='multi_select_region_radio', options=values_region_name_unique, value='Europe', clearable=False)
multi_select_country_radio = dcc.Dropdown(id='multi_select_country_radio', options=values_country_name_unique, value='South Europe', clearable=False)

multi_select_year_name_radio = dcc.Dropdown(id='multi_select_year_radio', options=values_year_unique, value=1987, clearable=False)

#########################################################################################################################################################################


df_soixante_quinze_plus_done = pd.read_csv("soixante_quinze_plus.csv")

values_region_name_unique = df_soixante_quinze_plus_done['Region Name'].unique()
values_year_unique   = df_soixante_quinze_plus_done['Year'].unique()
values_country_name_unique  = df_soixante_quinze_plus_done['Country Name'].unique()


def create_country_name_chart(values_region_name_unique='Europe', values_year_unique=1987):
    filtered_df_name = df_soixante_quinze_plus_done[(df_soixante_quinze_plus_done['Region Name']== values_region_name_unique) & (df_soixante_quinze_plus_done['Year']==values_year_unique)]
    filtered_df_name = filtered_df_name.sort_values(by="Death rate per 100 000 population", ascending=False).head(20)

    bar_fig = px.bar(filtered_df_name, x="Country Name", y='Death rate per 100 000 population', color="Age Group", 
    template="seaborn", title=f"{values_region_name_unique} vs {values_year_unique}", text_auto=True)
    bar_fig.update_layout(paper_bgcolor='#e5ecf6', height=600)
    
    return bar_fig

multi_select_region = dcc.Dropdown(id='multi_select_region', options=values_region_name_unique, value='Europe', clearable=False)
multi_select_country = dcc.Dropdown(id='multi_select_country', options=values_country_name_unique, value='South Europe', clearable=False)

multi_select_year_name = dcc.Dropdown(id='multi_select_year', options=values_year_unique, value=1987, clearable=False)

#########################################################################################################################################################################


app = Dash(title="World Health Organization")

app.layout = html.Div(
        children=[
            html.H1("World Health Organization Dashboard Visualization Report", style={"text-align":"center"}),
            html.P("Death Rate per 100 000 of the Population (Total, Maximum, Average and Minimum)", style={"text-align":"center"}),

            # html.Div
            # ( 
            #     children=
            #     [
            #         dcc.Graph(figure=indicator_sum),
            #     ],
            
            #     style={"display": "inline-block", "width": "24%"} 
            # ),

            html.Div
            ( 
                children=
                [
                    dcc.Graph(figure=indicator_max),
                ],
            
                style={"display": "inline-block", "width": "33%"} 
            ),

            html.Div
            ( 
                children=
                [
                    dcc.Graph(figure=indicator_avg),
                ],
            
                style={"display": "inline-block", "width": "33%"} 
            ),

            html.Div
            ( 
                children=
                [
                    dcc.Graph(figure=indicator_min),
                ],
            
                style={"display": "inline-block", "width": "33%"} 
            ),

            # html.Br(),

            # html.Div
            # (
            #     children=
            #     [
            #         dcc.RadioItems(id='radio_1', options=values_region_name_unique)
            #     ],
            #     style={"display": "inline-block", "width": "24%"} 
            # ), 

            # html.Div
            # (
            #     children=
            #     [
            #         dcc.RadioItems(id='radio_2', options=values_region_name_unique)
            #     ],
            #     style={"display": "inline-block", "width": "24%"} 
            # ), 

            # html.Div
            # (
            #     children=
            #     [
            #         dcc.RadioItems(id='radio_3', options=values_region_name_unique)
            #     ],
            #     style={"display": "inline-block", "width": "24%"} 
            # ), 

            # html.Div
            # (
            #     children=
            #     [
            #         dcc.RadioItems(id='radio_4', options=values_region_name_unique)
            #     ],
            #     style={"display": "inline-block", "width": "24%"} 
            # ), 

            # html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),

            dcc.Tabs
            ([

                # dcc.Tab(label="TOP 20 of Region vs Country Name vs Numerical Values",
                #     children=
                #     [
                #         html.Br(),
                #         # html.Br(),
                #         # html.Br(),

                #         # html.Div
                #         # (
                #         #     children=
                #         #     [
                #         #         dcc.Graph(figure=fig)
                #         #     ],
                #         #     style={"display": "inline-block", "width": "70%"} 
                #         # ), 

                #         # html.Div
                #         # (
                #         #     children=
                #         #     [
                #         #         # multi_select_region_radio, multi_select_year_name_radio,
                #         #         dcc.RadioItems(id='radio', options=values_region_name_unique)
                #         #     ],
                #         #     style={"display": "inline-block", "width": "100%"} 
                #         # ), 

                #         # html.Div
                #         # (
                #         #     children=
                #         #     [
                #         #         multi_select_region, multi_select_year_name,
                #         #         dcc.Graph(id='country_name_chart', figure=create_country_name_chart())
                #         #     ],
                #         #     style={"display": "inline-block", "width": "100%"} 
                #         # ),
                #     ],
                # ),

                dcc.Tab(label="TOP 100 of Region vs Country Name vs Numerical Values",
                    children=
                    [
                        html.Br(),

                        html.Div
                        (
                            children=
                            [
                                multi_select_region_name, multi_select_year,
                                dcc.Graph(id='country_chart', figure=create_country_chart())
                            ],
                            style={"display": "inline-block", "width": "100%"} 
                        ),

                        # html.Div
                        # (
                        #     children=
                        #     [
                        #         select_region_name, select_year_region,
                        #         dcc.Graph(id='region_chart', figure=create_region_chart())
                        #     ],
                        #     style={"display": "inline-block", "width": "50%"} 
                        # ),
                    ],
                ),

                dcc.Tab(label="TOP 20 of Region vs Country Name vs Numerical Values",
                    children=
                    [
                        html.Br(),

                        html.Div
                        (
                            children=
                            [
                                multi_select_region_pie, multi_select_year_pie,
                                dcc.Graph(id='region_name_pie', figure=create_region_name_pie())
                            ],
                            style={"display": "inline-block", "width": "50%"} 
                        ), 

                        html.Div
                        (
                            children=
                            [
                                multi_select_region_name_pie, multi_select_year_country_pie,
                                dcc.Graph(id='country_name_pie', figure=create_country_name_pie())
                            ],
                            style={"display": "inline-block", "width": "50%"} 
                        ), 
                    ],
                ),

                dcc.Tab(label="TOP 20 of Region vs Country Name vs Numerical Values",
                    children=
                    [
                        html.Br(),

                        html.Div
                        (
                            children=
                            [
                                multi_select_region_name_density_heatmap, multi_select_year_density_heatmap, multi_select_numeric_density_heatmap,
                                dcc.Graph(id='country_name_density_heatmap', figure=create_country_name_density_heatmap())
                            ],
                            style={"display": "inline-block", "width": "50%"} 
                        ), 

                        html.Div
                        (
                            children=
                            [
                                multi_select_region_name_choropleth_map, multi_select_year_choropleth_map, multi_select_numeric_choropleth_map,
                                dcc.Graph(id='country_choropleth_map', figure=create_country_choropleth_map())
                            ],
                            style={"display": "inline-block", "width": "50%"} 
                        ), 
                    ],
                ),
        ]),
    ],
    style={"padding":"50px"}
)

# @callback(Output('country_name_chart', "figure"), [Input('multi_select_region_radio', "value"), ], [Input('multi_select_year_name_radio', "value"),],)
# def update_country_name_chart(values_region_name_unique, values_year_unique):
#     return create_country_name_chart(values_region_name_unique, values_year_unique)


@callback(Output('country_chart', "figure"), [Input('multi_select_region_name', "value"), ], [Input('multi_select_year', "value"),],)
def update_country_chart(values_region_name_unique, values_year_unique):
    return create_country_chart(values_region_name_unique, values_year_unique)


# @callback(Output('region_chart', "figure"), [Input('select_region_name', "value"), ], [Input('select_year_region', "value"),],)
# def update_region_chart(values_region_name_unique, values_year_region_unique):
#     return create_region_chart(values_region_name_unique, values_year_region_unique)



@callback(Output('country_name_density_heatmap', "figure"), [Input('multi_select_region_name_density_heatmap', "value"), ], [Input('multi_select_year_density_heatmap', "value"),], [Input('multi_select_numeric_density_heatmap', "value"),],)
def update_country_name_density_heatmap(values_region_name_unique, values_year_region_unique, numeric_values_density_heatmap):
    return create_country_name_density_heatmap(values_region_name_unique, values_year_region_unique, numeric_values_density_heatmap) 



@callback(Output('country_choropleth_map', 'figure'), [Input('multi_select_region_name_choropleth_map', 'value'),], [Input('multi_select_year_choropleth_map', 'value'),], [Input('multi_select_numeric_choropleth_map', 'value'),],)
def update_country_choropleth_map(region_name_unique, year_unique, numeric_values_map):
    return create_country_choropleth_map(region_name_unique, year_unique, numeric_values_map)



@callback(Output('region_name_pie', "figure"), [Input('multi_select_region_pie', "value"), ], [Input('multi_select_year_pie', "value"), ], )
def update_region_name_pie(region_name_unique_pie, year_unique_pie):
    return create_region_name_pie(region_name_unique_pie, year_unique_pie)


@callback(Output('country_name_pie', "figure"), [Input('multi_select_region_name_pie', "value"), ], [Input('multi_select_year_country_pie', "value"), ], )
def update_country_name_pie(region_name_unique_pie, year_unique_pie):
    return create_country_name_pie(region_name_unique_pie, year_unique_pie)

if __name__ == "__main__":
    app.run_server(debug=True)