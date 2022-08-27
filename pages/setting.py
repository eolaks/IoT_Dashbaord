# -*- coding: utf-8 -*-
"""

Created on Thu Dec  10 15:48:45 2021
#   code to create a submission form for setting the threshold for parameters

@author: User
"""

import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

device_id = dbc.Row(
    [
        dbc.Label("Device ID.", html_for="example-email-row", width=4),
        dbc.Col(
            dbc.Input(
                type="text", id="device-id-row", placeholder="Enter Device ID"
            ),
            width=6,
        ),
    ],
    className="mb-3",
)

Temp_in_thres = dbc.Row(
    [
        dbc.Label("Temp-in Threshold.", html_for="example-password-row", width=4),
        dbc.Col(
            dbc.Input(
                type="text",
                id="temp-in-row",
                placeholder="Enter temp-in threshold value.",
            ),
            width=6,
        ),
    ],
    className="mb-3",
)

Temp_out_thres = dbc.Row(
    [
        dbc.Label("Temp-out Threshold.", html_for="example-password-row", width=4),
        dbc.Col(
            dbc.Input(
                type="text",
                id="temp-in-row",
                placeholder="Enter temp-out threshold value.",
            ),
            width=6,
        ),
    ],
    className="mb-3",
)

pressure_in_thres = dbc.Row(
    [
        dbc.Label("Pressure Threshold.", html_for="example-password-row", width=4),
        dbc.Col(
            dbc.Input(
                type="text",
                id="temp-in-row",
                placeholder="Enter Pressure threshold value.",
            ),
            width=6,
        ),
    ],
    className="mb-3",
)



flowrate_in_thres = dbc.Row(
    [
        dbc.Label("Flowrate Threshold.", html_for="example-password-row", width=4),
        dbc.Col(
            dbc.Input(
                type="text",
                id="flowrate-in-row",
                placeholder="Enter Flowrate threshold value.",
            ),
            width=6,
        ),
    ],
    className="mb-3",
)

salinity = dbc.Row(
    [
        dbc.Label("Salainity Threshold.", html_for="example-password-row", width=4),
        dbc.Col(
            dbc.Input(
                type="text",
                id="salinity-row",
                placeholder="Enter Salainity threshold value.",
            ),
            width=6,
        ),
    ],
    className="mb-3",
)

button = dbc.Row(
    dbc.Col(dbc.Button("Submit", color="primary"), width="auto")
    
    )

form = dbc.Form([device_id, Temp_in_thres, Temp_out_thres, pressure_in_thres,  flowrate_in_thres, salinity, button])


dash.register_page(__name__, name='Device Setting')

layout = html.Div(
    [
    dbc.Row([ 
        dcc.Markdown('# Device Setting Page'),
        ]), 
    dbc.Row([
        form
        ])
        
    ]
)

