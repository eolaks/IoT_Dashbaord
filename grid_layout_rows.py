import dash 
import dash_bootstrap_components as dbc
import dash_html_components as html
# create dash app
app = dash.Dash(__name__, external_stylesheets= [dbc.themes.BOOTSTRAP], 
                meta_tags = [{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])

# Create your grid layout 
app.layout = dbc.Container([   
    # divide into rows
    dbc.Row(html.H1(" Row - one ")),
    dbc.Row(html.H1(" Row - two ")),
    dbc.Row(html.H1(" Row - three "))   
    ]) 
if __name__ == " __main__":
    app.run_server(debug=True)
