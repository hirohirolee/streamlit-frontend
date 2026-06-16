import streamlit as st
import requests

# 1. 統一頁面風格設定
st.set_page_config(
    page_title="Matrix Portal - Hiro's AI & Data Hub",
    page_icon="🚀",
    layout="wide"
)

# 標題與介紹
st.title("🚀 Prediction Service Frontend")
st.markdown("### Mathematical Transformation Portal")

# 2. 安全讀取後端通道 (優先選取 Streamlit Secrets，備選為 Render 實體網址)
if "BACKEND_API_URL" in st.secrets:
    API_BASE_URL = st.secrets["BACKEND_API_URL"]
else:
    API_BASE_URL = "https://fastapi-backend-zcuc.onrender.com"

# 3. 綠色高亮顯示當前對接的後端網址
st.markdown(f"**Backend Target URL:** :green[{API_BASE_URL}]")

st.markdown("---")

# 4. 互動式輸入介面
num_input = st.number_input("Enter a feature value for matrix transformation:", value=1.00, step=0.5)

# 5. 主要行動按鈕（紅色主要按鈕）
if st.button("開始計算", type="primary"):
    # 打包特徵值為 float 清單
    payload = {"features": [float(num_input)]}
    
    with st.spinner("🚀 正在與雲端後端伺服器通訊中，請稍候..."):
        try:
            # 發送 POST 請求，設定適當的 timeout 以便在伺服器冬眠時能及時捕獲
            url = f"{API_BASE_URL}/calculate"
            response = requests.post(url, json=payload, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "success":
                    # 成功通訊特效與回饋
                    st.balloons()
                    st.success("🎉 Calculation finished successfully!")
                    
                    # 漂亮呈現後端回傳的數據
                    st.subheader("📊 運算結果 (Matrix Output)")
                    st.json(data)
                else:
                    st.error("後端回傳格式不正確或運算失敗。")
                    st.json(data)
            else:
                st.error(f"HTTP Error {response.status_code}: 伺服器回應錯誤。")
                st.text(response.text)
                
        except requests.exceptions.RequestException as e:
            # 捕獲連線逾時/冬眠例外並顯示溫暖的中文提示
            st.warning("""
            ⚠️ **偵測到網頁冷啟動中！**
            由於 Render 免費伺服器正處於深度冬眠狀態，大廚房正在生火開機，請您耐心等待 30~50 秒後，再次點選『開始計算』按鈕即可順暢連線！
            """)
            # 提供詳細錯誤訊息以供開發除錯參考
            with st.expander("🔍 技術除錯資訊 (Technical Debugging Info)"):
                st.code(str(e))
