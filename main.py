import streamlit as st
import pandas as pd
st.title("Análise das Músicas Mais Reproduzidas no Spotify em 2024")

st.header("Explorando os Dados de Streaming")

st.subheader("Uma Visão Geral")

st.markdown("""
**músicas mais reproduzidas no Spotify em 2024.** 
Você pode visualizar diferentes estatísticas e gráficos interativos.
""")

df = pd.read_csv("Most Streamed Spotify Songs 2024.csv", encoding='latin1')

st.dataframe(df)

st.table(df.head())

musica_1 = df.loc[df['Track'] == "MILLION DOLLAR BABY"].iloc[0]
musica_2 = df.loc[df['Track'] == "Not Like Us"].iloc[0]
musica_3 = df.loc[df['Track'] == "i like the way you kiss me"].iloc[0]


st.metric(label=f"Música: {musica_1['Track']}", value=f"Artista: {musica_1['Artist']}", delta=f"Streams: {musica_1['Spotify Streams']}")
st.metric(label=f"Música: {musica_2['Track']}", value=f"Artista: {musica_2['Artist']}", delta=f"Streams: {musica_2['Spotify Streams']}")
st.metric(label=f"Música: {musica_3['Track']}", value=f"Artista: {musica_3['Artist']}", delta=f"Streams: {musica_3['Spotify Streams']}")


st.write(df.head())

st.write("### Análise das Músicas Mais Reproduzidas")

st.write([str(musica_1['Track']), str(musica_2['Track']), str(musica_3['Track'])])

f'''
# Top Musicas

-{musica_1['Track']}\n
-{musica_2['Track']}\n
-{musica_3['Track']}\n
'''

df


st.image("image.png")

st.video("Kendrick Lamar - Not Like Us.mp4")

st.audio("Kendrick Lamar - Not Like Us.mp3")



st.markdown("🎉 🚀 **Streamlit é incrível!**")


st.image("XOsX.gif")