import dash
import dash_bootstrap_components as dbc
import plotly.express as px

# Initialize Dash app with Bootstrap theme
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Load dataset
gapminder_df = px.data.gapminder()
years = gapminder_df["year"].unique()
continents = gapminder_df["continent"].unique()

# Main layout
app.layout = dbc.Container(
    fluid=True,
    children=[
        # Header with navbar
        dbc.Navbar(
            dbc.Container(
                [
                    dbc.NavbarBrand("Gapminder Dashboard", className="ms-2", href="/"),
                    dbc.Nav(
                        [
                            dbc.NavLink("Home", href="/", active="exact", className="me-2"),
                            dbc.NavLink("GDP", href="/gdp", active="exact", className="me-2"),
                            dbc.NavLink("Population", href="/population", active="exact", className="me-2"),
                            dbc.NavLink("Life Expectancy", href="/life-expectancy", active="exact", className="me-2"),
                            dbc.NavLink("Choropleth Map", href="/choropleth-map", active="exact", className="me-2"),
                        ],
                        className="ms-auto",
                        navbar=True,
                    ),
                ]
            ),
            color="dark",
            dark=True,
            className="mb-4",
        ),
        # Page container
        dash.page_container,
    ],
)
if __name__ == "__main__":
    app.run(debug=True)
