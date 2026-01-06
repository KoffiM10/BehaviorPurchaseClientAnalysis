# 🛍️ Dashboard Streamlit d'analyse du comportement d'achat

# 🔹 Import des modules
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# DOIT ÊTRE LA PREMIÈRE COMMANDE STREAMLIT
st.set_page_config(
    page_title="Online_sales", 
    page_icon="🛍️", 
    layout="wide",
    initial_sidebar_state="expanded"
)


# 🔹 Chargement et nettoyage des données
DATA_PATH = "../Data/shopping_trends.csv"

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    df.dropna(inplace=True)
    df["Season"] = pd.to_datetime(df["Season"], errors="coerce").dt.year
    df["Purchase Amount (USD)"] = pd.to_numeric(df["Purchase Amount (USD)"], errors="coerce")
    df["Previous Purchases"] = pd.to_numeric(df["Previous Purchases"], errors="coerce")
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    return df

df = load_data(DATA_PATH)

# 🔹 Titre principal
st.title("🛍️ Dashboard d'analyse du comportement d'achat")

# 🔹 Filtres interactifs
st.sidebar.header("🎛️ Filtres")
selected_type = st.sidebar.multiselect("Type d'article :", options=df["Category"].unique())
selected_gender = st.sidebar.multiselect("Genre :", options=df["Gender"].unique())

filtered_df = df.copy()
if selected_type:
    filtered_df = filtered_df[filtered_df["Category"].isin(selected_type)]
if selected_gender:
    filtered_df = filtered_df[filtered_df["Gender"].isin(selected_gender)]

# 🔹 Statistiques descriptives
st.subheader("📊 Statistiques descriptives")
col1, col2, col3 = st.columns(3)
col1.metric("Moyenne achat", f"{filtered_df['Purchase Amount (USD)'].mean():.2f}")
col2.metric("Médiane", f"{filtered_df['Purchase Amount (USD)'].median():.2f}")
col3.metric("Mode", f"{filtered_df['Purchase Amount (USD)'].mode()[0]:.2f}")

# 🔹 Mesures de dispersion
st.subheader("📐 Dispersion des achats")
ecart = filtered_df["Purchase Amount (USD)"].max() - filtered_df["Purchase Amount (USD)"].min()
ecart_type = filtered_df["Purchase Amount (USD)"].std()
iqr = filtered_df["Purchase Amount (USD)"].quantile(0.75) - filtered_df["Purchase Amount (USD)"].quantile(0.25)

st.write(f"Écart : {ecart:.2f}")
st.write(f"Écart-type : {ecart_type:.2f}")
st.write(f"IQR : {iqr:.2f}")

# 🔹 Visualisation : histogramme des achats
st.subheader("📈 Distribution des montants d'achat")
fig1, ax1 = plt.subplots()
sns.histplot(filtered_df["Purchase Amount (USD)"], kde=True, ax=ax1, color="skyblue")
ax1.set_xlabel("Montant d'achat")
st.pyplot(fig1)

# 🔹 Visualisation : boîte à moustaches par genre
st.subheader("📦 Répartition des achats par genre")
fig2, ax2 = plt.subplots()
sns.boxplot(x="Gender", y="Purchase Amount (USD)", data=filtered_df, ax=ax2)
st.pyplot(fig2)

# 🔹 Visualisation : volume de transactions par jour
st.subheader("📅 Volume de transactions par saison")
st.bar_chart(filtered_df["Season"].value_counts())

# 🔹 Corrélations entre variables
st.subheader("🔗 Corrélations entre variables")
corr = filtered_df[["Purchase Amount (USD)", "Previous Purchases", "Season", "Age"]].corr()
st.dataframe(corr.style.background_gradient(cmap="coolwarm"))

# 🔹 Footer
st.markdown("---")
st.caption("📊 Projet d'analyse des ventes en ligne — Streamlit | Données : shopping_trends.csv")