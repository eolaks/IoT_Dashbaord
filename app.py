# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 21:48:45 2021
# *******************************************************************************
# Title:     oil and gas monitroing real time project                           *                                                        *
# Author:   Olakunle Elijah, WCC UTM                                            *
#                                                                               *
#                                                                               *
# Description:                                                                  *
#       -   Dashbaord for monitoring Oil and gas pipeline parameters            *
#       -   Temperature-in, Temperature-out, Pressure, salinity and flowrate    *
#                                                                               *
# Revision:                                                                     *
#       1.0 Initial release.                                                    *
#       main file - run this file to display the dashbaord on your local server *
# *******************************************************************************

"""


import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB])
sidebar = dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
            className="bg-light",
)

app.layout = dbc.Container([
    # create Row 1
    dbc.Row([
        dbc.Col(html.Div("IoT Oil and Gas Monitoring Platform",
                         style={'fontSize':50, 'textAlign':'center'}))
    ]),

    html.Hr(),
    # create row 2 
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    dash.page_container
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
], fluid=True)

if __name__ == "__main__":
    app.run(debug=False)
