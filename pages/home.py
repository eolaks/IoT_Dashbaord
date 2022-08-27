# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 08:18:17 2022

@author: User
"""

import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', name='Home') # '/' is home page



# Create Layout for the home page


layout = html.Div(
    [
        
        # First row   
        dbc.Row([
            dbc.Col(
                [
                    html.Img(src='assets/Fig1.jpg')
                ], xs=10, sm=10, md=8, lg=4, xl=4, xxl=4
            )
        
        ])
        
        
    ]
)


