import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/population", name="Population")

gapminder_df = px.data.gapminder()
years = gapminder_df["year"].unique()
continents = gapminder_df["continent"].unique()

layout = html.Div(
    [
        html.H2("Population Analysis", className="text-center mb-4"),
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dcc.Dropdown(
                                id="cont_population",
                                options=[{"label": c, "value": c} for c in continents],
                                value="Asia",
                                clearable=False,
                                className="mb-3",
                            ),
                            width=6,
                        ),
                        dbc.Col(
                            dcc.Dropdown(
                                id="year_population",
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
                    dcc.Graph(id="population_chart"),
                    className="mt-4",
                ),
            ]
        ),
    ]
)


@dash.get_app().callback(
    Output("population_chart", "figure"),
    [Input("cont_population", "value"), Input("year_population", "value")],
)
def update_population_chart(continent, year):
    filtered_df = gapminder_df[
        (gapminder_df["continent"] == continent) & (gapminder_df["year"] == year)
    ]
    fig = px.bar(
        filtered_df,
        x="country",
        y="pop",
        color="country",
        title=f"Population in {continent}, {year}",
        text="pop",
    )
    fig.update_traces(texttemplate="%{text:.2s}", textposition="outside")
    fig.update_layout(
        xaxis_title="Country",
        yaxis_title="Population",
        showlegend=False,
        title_x=0.5,
    )
    return fig
