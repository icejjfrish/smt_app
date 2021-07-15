import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output
import pandas as pd
import plotly.express as px
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors = {
    'background': '#33363E',  # dark blue
    'text': '#7FDBFF',  # blue
    'graph': '#FFFE00',  # black
    'plot': '#26282C'  # yellow
}
#graph stuff
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
html.H1(children = 'Stanton Murillo Transport Application', style={'color': colors['text'], 'padding': '10px 15px','font-family': 'serif',
                                         'textAlign': 'center', 'font-size':'100px', 'text-decoration': 'underline'}),
#download button
html.Button("PDF DOWNLOAD", id="btn_txt", style={'color': colors['text']}), dcc.Download(id="download-text"),
html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])
])
#callback for PDF download button
@app.callback(
    Output("download-text", "data"),
    Input("btn_txt", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file(
        "smt_app/stanton16.pdf"
    )
if __name__=='__main__':
   app.run_server(debug=True)
