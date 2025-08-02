import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt

# ------------------- Page Setup -------------------
st.set_page_config(page_title="Smart Irrigation System", layout="wide")

# ------------------- Load Model -------------------
try:
    model = joblib.load("Farm_Irrigation_System.pkl")
except Exception as e:
    st.error("❌ Failed to load model. Please check the path or format.")
    st.stop()

# ------------------- Sidebar Navigation -------------------
st.sidebar.title("🚀 Navigation")
menu = st.sidebar.radio("Go to", ["🏠 Home", "📊 Summary", "ℹ️ About"])

# Store prediction and sensor values across pages
if 'sensor_values' not in st.session_state:
    st.session_state.sensor_values = [0.5] * 20
if 'prediction' not in st.session_state:
    st.session_state.prediction = None

# ------------------- Home Page -------------------
if menu == "🏠 Home":
    st.title("🌾 Smart Irrigation System")
    st.markdown("Predict ON/OFF status of 20 sprinklers using sensor data.")

    cols = st.columns(2)
    for i in range(20):
        st.session_state.sensor_values[i] = cols[i % 2].slider(
            f"Sensor {i}", 0.0, 1.0, st.session_state.sensor_values[i], step=0.01
        )

    if st.button("🔍 Predict Sprinklers"):
        input_array = np.array(st.session_state.sensor_values).reshape(1, -1)
        try:
            st.session_state.prediction = model.predict(input_array)[0]
            st.success("✅ Prediction complete!")

            st.markdown("### 🌿 Sprinkler Status")
            spr_cols = st.columns(4)
            for i, status in enumerate(st.session_state.prediction):
                color = "green" if status == 1 else "red"
                emoji = "🌧️" if status == 1 else "🚫"
                spr_cols[i % 4].markdown(
                    f"<div style='color:{color}; font-weight:bold;'>Sprinkler {i}: {emoji} {'ON' if status == 1 else 'OFF'}</div>",
                    unsafe_allow_html=True
                )
        except Exception as e:
            st.error(f"Prediction failed: {e}")

# ------------------- Summary Page -------------------
elif menu == "📊 Summary":
    st.title("📊 Sprinkler Summary")

    if st.session_state.prediction is None:
        st.warning("⚠️ No predictions yet. Go to **Home** and click **Predict Sprinklers**.")
    else:
        on_count = int(np.sum(st.session_state.prediction))
        off_count = 20 - on_count

        st.write(f"🔵 **Sprinklers ON**: {on_count} &nbsp;&nbsp;&nbsp;&nbsp; 🔴 **OFF**: {off_count}")

        # --- Bar Chart ---
        st.markdown("#### 📊 Bar Chart: ON vs OFF Count")
        fig_bar, ax_bar = plt.subplots()
        ax_bar.bar(["ON", "OFF"], [on_count, off_count], color=["green", "red"])
        ax_bar.set_ylabel("Number of Sprinklers")
        ax_bar.set_title("Sprinklers ON vs OFF")
        st.pyplot(fig_bar)

        # --- Line Chart ---
        st.markdown("#### 📈 Line Chart: Per-Sprinkler Status")
        fig_line, ax_line = plt.subplots(figsize=(10, 4))
        ax_line.plot(range(len(st.session_state.prediction)),
                     st.session_state.prediction,
                     marker='o', linestyle='-', color='blue')
        ax_line.set_title("Sprinkler Status Over 20 Parcels")
        ax_line.set_xlabel("Sprinkler Number (Parcel ID)")
        ax_line.set_ylabel("Status")
        ax_line.set_yticks([0, 1])
        ax_line.set_yticklabels(['OFF', 'ON'])
        ax_line.grid(True)
        st.pyplot(fig_line)

# ------------------- About Page -------------------
elif menu == "ℹ️ About":
    st.title("ℹ️ About This Project")
    st.markdown("""
    **🧪 Project Title:** Farm Irrigation System Using Machine Learning  
    **🎯 Objective:** Automate sprinkler control using real-time sensor values.

    **🔧 Technologies Used:**
    - Python, Pandas, NumPy
    - Scikit-learn for ML modeling
    - Joblib for model saving/loading
    - Streamlit for web UI
    - Matplotlib for charting

    **📈 Workflow:**
    - Input 20 scaled sensor readings
    - ML model predicts ON/OFF status for each sprinkler
    - Results shown with emojis and color highlights
    - Includes bar + line chart summaries of sprinklers

    **🌱 Benefits:**
    - Optimized water usage
    - Reduces manual labor
    - Improves farm productivity
    - Scalable for real-time agricultural use
    """)
