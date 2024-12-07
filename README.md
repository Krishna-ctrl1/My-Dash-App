# 🌍 **GDP Per Capita Analysis Dashboard**

An interactive web application built using [Dash](https://plotly.com/dash/), [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/), and [Plotly](https://plotly.com/) to visualize GDP per capita data by continent and year. This project leverages responsive design and dynamic filtering to provide an engaging user experience.

---

## 🚀 **Features**

- **Interactive Dropdowns**: Select continent and year to dynamically update the visualization.
- **Dynamic Bar Chart**: Displays GDP per capita for countries in the selected continent and year.
- **Responsive Design**: Optimized layout for different screen sizes using Bootstrap.
- **Multi-Page App**: Easily integrated into larger Dash applications.

---

## 🛠️ **Tech Stack**

- **Dash**: Framework for building analytical web apps.
- **Plotly Express**: For creating interactive visualizations.
- **Dash Bootstrap Components (DBC)**: For responsive and sleek UI.

---

## 📂 **File Structure**

```plaintext
project-root/
│
├── app.py               # Main Dash application file
│
├── pages/               # Folder containing individual pages
|   ├── home.py          # Home page of Dashboard
│   ├── gdp.py           # Page for GDP per capita analysis
│   ├── population.py    # Page for population data
│   ├── life_expectancy.py # Page for life expectancy trends
│   ├── choropleth_map.py # Page for life expectancy map visualizations
│
```

## 📊 **Dashboard Overview**

-🏠 **Home Page:** Hero section welcomes users and provides a quick overview.
-🌎 **GDP Analysis Page:** Displays a bar chart of GDP per capita filtered by continent and year.
-👥 **Population Analysis Page:** Bar chart visualizing population filtered by continent and year.
-📈 **Life Expectancy Trends Page:** Line chart for life expectancy trends, filterable by continent and year.
-🗺️ **Choropleth Map Page:** Dynamic map showcasing life expectancy over time with animations by year.
