import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/life-expectancy", name="Life Expectancy")

gapminder_df = px.data.gapminder()
years = gapminder_df["year"].unique()
continents = gapminder_df["continent"].unique()

layout = html.Div(
    [
        html.H2("Life Expectancy Analysis", className="text-center mb-4"),
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dcc.Dropdown(
                                id="cont_life",
                                options=[{"label": c, "value": c} for c in continents],
                                value="Asia",
                                clearable=False,
                                className="mb-3",
                            ),
                            width=6,
                        ),
                        dbc.Col(
                            dcc.Dropdown(
                                id="year_life",
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
                    dcc.Graph(id="life_chart"),
                    className="mt-4",
                ),
            ]
        ),
    ]
)


@dash.get_app().callback(
    Output("life_chart", "figure"),
    [Input("cont_life", "value"), Input("year_life", "value")],
)
def update_life_chart(continent, year):
    filtered_df = gapminder_df[
        (gapminder_df["continent"] == continent) & (gapminder_df["year"] == year)
    ]
    fig = px.line(
        filtered_df,
        x="country",
        y="lifeExp",
        color="country",
        title=f"Life Expectancy in {continent}, {year}",
        markers=True,
    )
    fig.update_traces(line_shape="spline", marker=dict(size=8))
    fig.update_layout(
        xaxis_title="Country",
        yaxis_title="Life Expectancy",
        title_x=0.5,
    )
    return fig
