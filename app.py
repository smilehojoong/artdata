
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Virtual Art Exhibition", layout="wide")
st.title("🎨 My Virtual Art Exhibition")
st.caption("Powered by The Met Open Access API")

theme = "flowers"
st.subheader(f"Curated Theme: {theme.capitalize()}")

df = pd.read_csv("artworks.csv")

for i, row in df.iterrows():
    st.image(row["image"], width=300)
    st.markdown(f"**{row['title']}** by *{row['artist']}*")
    st.caption(f"{row['year']} · {row['medium']}")
    st.markdown("---")

st.markdown("📝 _This exhibition explores the symbolic use of flowers in art history..._")
