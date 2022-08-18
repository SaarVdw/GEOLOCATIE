import pandas as pd
import plotly.express as px

#dataframe maken met info uit csv
df_straten = pd.read_csv(r"C:\Users\vandewsa\Downloads\Fotocollectie Industriemuseum- Beluiken.csv")

#kaart creeëren
fig = px.scatter_mapbox(df_straten, lat="lat", lon="lon", hover_name="straat", hover_data=["wijk", "aantal"],
                        color_discrete_sequence=["#E8BE19"], size="aantal", zoom=11, height=800)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
