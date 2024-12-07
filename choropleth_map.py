import dash
from dash import html, dcc
import dash_bootstrap_components as dbc  # Added import
import plotly.express as px

dash.register_page(__name__, path="/choropleth-map", name="Choropleth Map")

gapminder_df = px.data.gapminder()

layout = html.Div(
    [
        html.H2("Choropleth Map of Life Expectancy", className="text-center mb-4"),
        dbc.Container(
            [
                dcc.Graph(
                    id="choropleth_map",
                    figure=px.choropleth(
                        gapminder_df,
                        locations="iso_alpha",
                        color="lifeExp",
                        hover_name="country",
                        animation_frame="year",
                        title="Life Expectancy Over Time (1952-2007)",
                        color_continuous_scale=px.colors.sequential.Plasma,
                    ).update_layout(title_x=0.5),
                )
            ],
            fluid=True,
        ),
    ]
)
