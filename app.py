import streamlit as st, pandas as pd

st.set_page_config(page_title="LT Analyzer (starter)")
st.title("LT Analyzer (starter)")

st.write("Upload a CSV with columns like: `time_min, hr, lactate`.")
file = st.file_uploader("CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)
else:
    df = pd.DataFrame({"time_min":[0,10,20,30], "hr":[120,135,148,158], "lactate":[1.2,1.6,2.2,3.8]})
    st.info("Using sample data. Upload your own to replace it.")

st.dataframe(df.head())

if "hr" in df.columns:
    st.subheader("Heart rate")
    st.line_chart(df[["hr"]])

if "lactate" in df.columns:
    st.subheader("Lactate")
    st.line_chart(df[["lactate"]])

def threshold_time(df, target=2.0):
    if "lactate" not in df: return None
    s = df["lactate"] - target
    for i in range(1, len(s)):
        if s.iloc[i] >= 0 and s.iloc[i-1] < 0:
            x0,x1 = df["time_min"].iloc[i-1], df["time_min"].iloc[i]
            y0,y1 = s.iloc[i-1], s.iloc[i]
            return float(x0 + (x1-x0)*(-y0)/(y1-y0)) if y1!=y0 else float(x1)
    return None

lt1 = threshold_time(df, 2.0)
lt2 = threshold_time(df, 4.0)

st.subheader("Estimated thresholds")
st.write(f"LT1 (≈2 mmol): {lt1 if lt1 is not None else 'not found'}")
st.write(f"LT2 (≈4 mmol): {lt2 if lt2 is not None else 'not found'}")
