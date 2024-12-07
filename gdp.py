import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

dash.register_page(__name__, path="/gdp", name="GDP Per Capita")

gapminder_df = px.data.gapminder()
years = gapminder_df["year"].unique()
continents = gapminder_df["continent"].unique()

layout = html.Div(
    [
        html.H2("GDP Per Capita Analysis", className="text-center mb-4"),
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dcc.Dropdown(
                                id="cont_gdp",
                                options=[{"label": c, "value": c} for c in continents],
                                value="Asia",
                                clearable=False,
                                className="mb-3",
                            ),
                            width=6,
                        ),
                        dbc.Col(
                            dcc.Dropdown(
                                id="year_gdp",
                                options=[{"label": y, "value": y} for y in years],
                                value=1952,
                                clearable=False,
                                className="mb-3",
                            ),
                            width=6,
                        ),
                    ],
                ),
                dbc.Row(
                    dcc.Graph(id="gdp_chart"),
                    className="mt-4",
                ),
            ]
        ),
    ]
)


@dash.get_app().callback(
    Output("gdp_chart", "figure"),
    [Input("cont_gdp", "value"), Input("year_gdp", "value")],
)
def update_gdp_chart(continent, year):
    filtered_df = gapminder_df[
        (gapminder_df["continent"] == continent) & (gapminder_df["year"] == year)
    ]
    fig = make_subplots(rows=1, cols=2, subplot_titles=["GDP Per Capita", "Population"])
    fig.add_trace(
        go.Bar(
            x=filtered_df["country"], y=filtered_df["gdpPercap"], name="GDP Per Capita"
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            x=filtered_df["country"],
            y=filtered_df["pop"],
            mode="markers",
            name="Population",
        ),
        row=1,
        col=2,
    )
    fig.update_layout(title=f"GDP and Population in {continent}, {year}")
    return fig
