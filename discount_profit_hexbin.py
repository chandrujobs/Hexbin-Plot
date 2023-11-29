import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load the dataset
data = pd.read_excel("C:/Users/Chandru/OneDrive/Desktop/Python Visuals/Sample - Superstore.xls", sheet_name="Orders")

# Create a Dash application
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    dcc.Dropdown(
        id='region-dropdown',
        options=[{'label': region, 'value': region} for region in data['Region'].unique()],
        value=data['Region'].unique(),
        multi=True
    ),
    dcc.Graph(id='hexbin-chart')
])

# Define callback to update graph
@app.callback(
    Output('hexbin-chart', 'figure'),
    [Input('region-dropdown', 'value')]
)
def update_graph(selected_regions):
    filtered_data = data[data['Region'].isin(selected_regions)]
    fig = px.density_heatmap(filtered_data, x='Discount', y='Profit', nbinsx=20, nbinsy=20, title='Discount vs. Profit Hexbin Plot')

    # Update plot layout for hexbin color and background
    fig.update_traces(
        colorscale='Greys'
    )
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white'
    )

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8063)
