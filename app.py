import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import folium_static

# Title
st.title("🎨 Cultural Canvas of India")
st.markdown("Explore India's rich and diverse cultural heritage through art, traditions, and responsible travel.")

# Sidebar Navigation
menu = st.sidebar.selectbox(
    "Navigate",
    ["Home", "Traditional Art Forms", "Cultural Experiences", "Tourism Insights", "Responsible Tourism"]
)

if menu == "Home":
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/India_2018_National_Emblem.png/1200px-India_2018_National_Emblem.png ", use_column_width=True)
    st.write("Welcome to the journey through India's vibrant culture!")

elif menu == "Traditional Art Forms":
    df_art = pd.read_csv("data/art_forms.csv")
    state = st.selectbox("Select State", df_art['state'].unique())
    filtered = df_art[df_art['state'] == state]
    st.write(filtered[['art_form', 'description']])
    
elif menu == "Cultural Experiences":
    df_culture = pd.read_csv("data/cultural_hotspots.csv")
    st.subheader("Map of Cultural Hotspots")
    # Map display
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
    for _, row in df_culture.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=f"{row['name']} - {row['type']}",
            tooltip=row['name']
        ).add_to(m)
    folium_static(m)

    st.dataframe(df_culture[['name', 'type', 'best_time_to_visit']])

elif menu == "Tourism Insights":
    df_tourism = pd.read_csv("data/tourism_trends.csv")
    fig = px.line(df_tourism, x='month', y='visitors', color='location', title="Tourism Trends Across Cultural Hotspots")
    st.plotly_chart(fig)

    df_unvisited = pd.read_csv("data/under_visited.csv")
    st.subheader("Under-Visited Cultural Destinations")
    fig_bar = px.bar(df_unvisited, x='location', y='visits', color='state', title="Visits to Under-Visited Places")
    st.plotly_chart(fig_bar)

elif menu == "Responsible Tourism":
    st.markdown("""
    ### Tips for Responsible Tourism:
    - Respect local customs and traditions.
    - Avoid littering at heritage sites.
    - Support local artisans.
    - Visit during off-seasons to reduce overcrowding.
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Responsible_Tourism.jpg/1200px-Responsible_Tourism.jpg ", use_column_width=True)
