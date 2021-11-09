import streamlit as st
import pandas as pd
import folium
import plotly_express as px

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_and_transform_data():
    df = pd.read_csv('data_coordinates/lat_lon_os.csv', decimal='.', delimiter=',', parse_dates=True)
    df['HOUR'] = df['CREATED_AT'].apply(lambda x: pd.to_datetime(x).hour)
    df.dropna(inplace=True)
    return df

def plot_map():
    df = load_and_transform_data()
    df.dropna(inplace=True)
    slider_value = st.slider('Select an Hour of the day', min_value=float(df.HOUR.min()), max_value=float(df.HOUR.max()), value=None, step=1.0, format=None, key=None, help=None, on_change=None, args=None, kwargs=None)

    df_to_show = df[df['HOUR'] == slider_value]
    mean_lat = df_to_show.LAT.mean()
    mean_lon = df_to_show.LNG.mean() 
    df_to_show = df_to_show[~((df_to_show['LAT'] == 'nan') | (df_to_show['LNG'] == 'nan'))]

    m = folium.Map(location=[mean_lat, mean_lon], zoom_start=15)
    
    try:
        for i in range(len(df_to_show)):
            tooltip = list(df_to_show.iloc[i][['PAYMENT_METHOD', 'OS']].values)
            Lat_del = float(df_to_show.iloc[i]['LAT'])
            Lon_del = float(df_to_show.iloc[i]['LNG'])
            if df_to_show.iloc[i]['OS'] == 'IOS':
                color = 'red'
                folium.Marker([Lat_del, Lon_del], tooltip=tooltip, icon=folium.Icon(color=color, icon="exclamation", prefix='fa')).add_to(m)
            else:
                color = 'blue'
                folium.Marker([Lat_del, Lon_del], tooltip=tooltip, icon=folium.Icon(color=color, icon='exclamation', prefix='fa')).add_to(m)
        return m 
    except:
        pass

def orders_histogram():
    df = load_and_transform_data()
    plot = px.histogram(df, x='HOUR', color="OS", barmode='group')
    return plot

def plot_treemap():
    df = load_and_transform_data()
    fig = px.treemap(df, path=['HOUR', 'PAYMENT_METHOD', 'OS'], values='TOTAL_VALUE')
    fig.update_traces(root_color="lightgrey")
    return fig