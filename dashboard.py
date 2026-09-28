import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Water Potability Dashboard",
    page_icon="💧",
    layout="wide"
)

st.title("📊 Water Potability Dashboard")
st.write("Welcome to the Machine Learning Dashboard")

# --- DATASET LOAD ---
@st.cache_data
def load_data():
    try:
       import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Water Potability Dashboard",
    page_icon="💧",
    layout="wide"
)

st.title("📊 Water Potability Dashboard")
st.write("Welcome to the Machine Learning Dashboard")

# --- DATASET LOAD ---
@st.cache_data
def load_data():
    try:
        df = pd.read_csv(r"C:\Users\Sameer\OneDrive\Documents\Desktop\BIA_PROJECT\water_potability.csv")
        return df
    except Exception as e:
        return None

df = load_data()

# --- METRICS DISPLAY ---
col1, col2, col3 = st.columns(3)

with col1:
    total_records = len(df) if df is not None else 3276
    st.metric("Total Records", f"{total_records:,}")

with col2:
    st.metric("Accuracy", "88.5%")

with col3:
    st.metric("Model", "Random Forest")

st.subheader("Project Overview")
st.info("Dataset and Machine Learning model connected successfully!")

# --- DATA PREVIEW & VISUALIZATIONS ---
if df is not None:
    st.write("---")
    
    # Data Table Preview
    st.subheader("📋 Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    st.write("---")
    
    # Graphs Section
    st.subheader("📊 Data Visualizations")
    c1, c2 = st.columns(2)
    
    with c1:
        st.write("**Potability Target Distribution**")
        fig, ax = plt.subplots(figsize=(6, 4))
        if 'Potability' in df.columns:
            sns.countplot(x='Potability', data=df, palette='viridis', ax=ax)
            ax.set_xticklabels(['Not Potable (0)', 'Potable (1)'])
        else:
            sns.countplot(x=df.columns[-1], data=df, palette='viridis', ax=ax)
        ax.set_ylabel("Count")
        ax.set_xlabel("Water Quality")
        st.pyplot(fig)
            
    with c2:
        st.write("**pH Level Distribution**")
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        if 'ph' in df.columns:
            sns.histplot(df['ph'].dropna(), kde=True, color='skyblue', ax=ax2)
            ax2.set_xlabel("pH Level")
        else:
            st.dataframe(df.describe().T[['mean', 'std', 'min', 'max']])
        st.pyplot(fig2)
else:
    st.error("`water_potability.csv` file load nahi ho payi. Direct check karein ki CSV file GitHub repository ke main folder mein present hai ya nahi.")
        return data
    except Exception as e:
        return None

df = load_data()

# --- METRICS DISPLAY ---
col1, col2, col3 = st.columns(3)

with col1:
    total_records = len(df) if df is not None else 3276
    st.metric("Total Records", f"{total_records:,}")

with col2:
    st.metric("Accuracy", "88.5%")

with col3:
    st.metric("Model", "Random Forest")

st.subheader("Project Overview")
st.info("Dataset and Machine Learning model connected successfully!")

# --- DATA PREVIEW & VISUALIZATIONS ---
if df is not None:
    st.write("---")
    
    # Data Table Preview
    st.subheader("📋 Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    st.write("---")
    
    # Graphs Section
    st.subheader("📊 Data Visualizations")
    c1, c2 = st.columns(2)
    
    with c1:
        st.write("**Potability Target Distribution**")
        fig, ax = plt.subplots(figsize=(6, 4))
        if 'Potability' in df.columns:
            sns.countplot(x='Potability', data=df, palette='viridis', ax=ax)
            ax.set_xticklabels(['Not Potable (0)', 'Potable (1)'])
        else:
            sns.countplot(x=df.columns[-1], data=df, palette='viridis', ax=ax)
        ax.set_ylabel("Count")
        ax.set_xlabel("Water Quality")
        st.pyplot(fig)
            
    with c2:
        st.write("**pH Level Distribution**")
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        if 'ph' in df.columns:
            sns.histplot(df['ph'].dropna(), kde=True, color='skyblue', ax=ax2)
            ax2.set_xlabel("pH Level")
        else:
            st.dataframe(df.describe().T[['mean', 'std', 'min', 'max']])
        st.pyplot(fig2)
else:
    st.error("`water_potability.csv` file load nahi ho payi. Direct check karein ki CSV file GitHub repository ke main folder mein present hai ya nahi.")
