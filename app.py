#main app for practice
from dash import Dash, html, dash_table, dcc, callback,Output, Input
import pandas as pd
import plotly.express as px

# incorporate data (df - data frame?)
# read how csv should be constructed, newline at end also
# seems key
df = pd.read_csv(
   'https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# initalize the app
app = Dash(__name__)

# app layout will contain a div of div's
# the div has a few propeties such as children tp
# add text ot page (look up doc on html library
#  would it be better to use actual html?)

# app layout
app.layout = html.Div([
   html.Div(children='My First App with Data'),
   html.Hr(),
   dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'),
   dash_table.DataTable(data=df.to_dict('records'), page_size=6),
   dcc.Graph(figure={}, id='controls-and-graph')
])

# Add controls to build the interaction
# NOTICE: the function must immediatley follow the callback
# decorator for the update function to work correctly
# the input and output are the properies of a particular
# compoment that has the necessary id's
@callback(
   Output(component_id='controls-and-graph', component_property='figure'),
   Input(component_id='controls-and-radio-item', component_property='value')
) # that col_ chosen efers to the component property of the input lifeExp (why ???)
def update_graph(col_chosen):
   fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
   return fig

# run the app
if __name__ == '__main__': 
   app.run(debug=True)