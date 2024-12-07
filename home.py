import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/")

layout = html.Div(
    children=[
        # Hero Section
        dbc.Container(
            fluid=True,
            children=[
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                [
                                    html.H1("Welcome to the Gapminder Dashboard 🎥", className="text-center mb-4"),
                                    html.P(
                                        "Dive into data visualizations with a cinematic touch. "
                                        "Navigate through GDP, Population, and Life Expectancy insights.",
                                        className="text-center lead",
                                    ),
                                    dbc.Button(
                                        "Explore Now",
                                        color="primary",
                                        size="lg",
                                        href="/gdp",
                                        className="d-block mx-auto mt-3",
                                    ),
                                ]
                            ),
                            width=12,
                        )
                    ]
                )
            ],
            className="p-5 bg-light rounded-3 shadow-sm",
        ),
        # Dashboard Overview Section
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H4("GDP Insights", className="card-title"),
                                            html.P(
                                                "Analyze global GDP trends and data with advanced visualizations.",
                                                className="card-text",
                                            ),
                                            dbc.Button("Learn More", href="/gdp", color="success", outline=True),
                                        ]
                                    )
                                ],
                                className="shadow-sm",
                            ),
                            width=6,
                            lg=3,
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H4("Population Analysis", className="card-title"),
                                            html.P(
                                                "Explore population changes over time across continents.",
                                                className="card-text",
                                            ),
                                            dbc.Button(
                                                "Learn More",
                                                href="/population",
                                                color="info",
                                                outline=True,
                                            ),
                                        ]
                                    )
                                ],
                                className="shadow-sm",
                            ),
                            width=6,
                            lg=3,
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H4("Life Expectancy", className="card-title"),
                                            html.P(
                                                "Discover key factors impacting life expectancy globally.",
                                                className="card-text",
                                            ),
                                            dbc.Button(
                                                "Learn More",
                                                href="/life-expectancy",
                                                color="warning",
                                                outline=True,
                                            ),
                                        ]
                                    )
                                ],
                                className="shadow-sm",
                            ),
                            width=6,
                            lg=3,
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H4("Choropleth Maps", className="card-title"),
                                            html.P(
                                                "Visualize data distribution with dynamic maps.",
                                                className="card-text",
                                            ),
                                            dbc.Button(
                                                "Learn More",
                                                href="/choropleth-map",
                                                color="danger",
                                                outline=True,
                                            ),
                                        ]
                                    )
                                ],
                                className="shadow-sm",
                            ),
                            width=6,
                            lg=3,
                        ),
                    ],
                    className="g-3",
                )
            ],
            className="my-5",
        ),
    ]
)
