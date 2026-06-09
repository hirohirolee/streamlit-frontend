import streamlit as st
import requests
import os

# Page configuration
st.set_page_config(
    page_title="Streamlit Prediction Portal",
    page_icon="🚀",
    layout="centered"
)

# Custom Styling / UI Header
st.title("🚀 Prediction Service Frontend")
st.markdown("""
This is a decoupled Streamlit frontend. It does not calculate any algorithm logic locally;
instead, it delegates all computations to a FastAPI backend.
""")

# Load the Backend API URL from environment variables, defaulting to localhost:8000
API_BASE_URL = os.getenv("BACKEND_API_URL", "http://localhost:8000")

st.caption(f"Backend Target URL: `{API_BASE_URL}`")

# Divider line
st.markdown("---")

# Section header
st.subheader("Mathematical Transformation Portal")

# 1. Number input box
num_input = st.number_input("Enter a feature value for matrix transformation:", value=1.0, step=0.5)

# 2. "開始計算" Button
if st.button("開始計算", type="primary"):
    with st.spinner("Sending payload to backend server..."):
        # Wrap single number value inside a float list to match API schema (List[float])
        payload = {"features": [float(num_input)]}
        
        try:
            url = f"{API_BASE_URL}/calculate"
            response = requests.post(url, json=payload, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "success":
                    st.success("🎉 Calculation finished successfully!")
                    st.subheader("Calculation Result (from Backend)")
                    # Render result in a beautiful format
                    st.write(data.get("result"))
                else:
                    st.error("Backend error: Request did not report success.")
                    st.json(data)
            else:
                st.error(f"HTTP Error {response.status_code}: Received response from backend but request failed.")
                st.text(response.text)
                
        except requests.exceptions.ConnectionError:
            st.error("❌ Connection Error: Could not connect to the backend server. Is FastAPI running?")
        except Exception as e:
            st.error(f"❌ An unexpected error occurred: {str(e)}")
