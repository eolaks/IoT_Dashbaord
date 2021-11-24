import dash 
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# create dash app
app = dash.Dash(__name__, external_stylesheets= [dbc.themes.BOOTSTRAP], 
                meta_tags = [{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])
# Create your grid layout 
app.layout = dbc.Container([
    # divide  rows into columns
    # Row 1
    dbc.Row(       
        dbc.Col(html.H1("Industrial IoT Mixer DASHBAORD", className = 'text-center text-primary mb-4'), width = 12)),
    # Row 2
    dbc.Row([ 
        # Column 1
        dbc.Col([
            # add a text area to display machine status         
            html.H3("Machine Status"),
            # add a text area
            dcc.Textarea()                  
            ]),  
        # column 2
        dbc.Col([
            # add a dropdown menu 
            dcc.Dropdown(id='drop_down_menu_1'), 
            # add a Graph
            dcc.Graph(id = 'graph_1')         
            ]),
        # column 3
        dbc.Col([
            # Add text area for label
            html.H3("Operation Cycle"),
            # add a text area to display operation cycle 
            dcc.Textarea(),         
            ])
        ]),
    # Row 3
    dbc.Row([
        # column 1
        dbc.Col(html.H1(" grid - five"), width = 4),    
        # Column 2
        dbc.Col(html.H1(" grid - six"), width = 4),      
        # Column 3
        dbc.Col(html.H1(" grid - seven"), width = 4)
        ]),  
    # Row 4 
    dbc.Row([
        # column 1
        dbc.Col(html.H6("Designed by O. Elijah Ver 1.0", className = 'text-center text-primary mb-3'), width = 5),        
        # column 2     
        dbc.Col(html.H6("Status", className = 'text-center text-primary mb-3'), width = 3),
        # Column 3     
        dbc.Col(html.H6("Offline", className = 'text-center text-primary mb-3'), width = 3)     
        ])
    ]) 
if __name__ == " __main__":
    app.run_server(debug=True)
