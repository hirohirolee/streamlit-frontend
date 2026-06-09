import streamlit as st

# 1. 頁面視覺風格與設定
st.set_page_config(
    page_title="Hiro's AI & Data Hub",
    page_icon="🚀",
    layout="wide"
)

# 2. 門面大標題
st.title("🚀 Hiro's AI & 數據實戰展示中心")

# 3. 優雅的歡迎詞
st.markdown("""
歡迎來到我的雲端作品集。本站採用前後端分離（Decoupled Architecture）架構開發，前端展示層常駐於 Streamlit Cloud，核心運算層則委託於遠端高效能伺服器。
""")

# 4. 觀看指南引導
st.info("""
🎯 **【觀看指南】**
請翻開網頁的 **「左側邊欄選單（Sidebar）」**。我已經將每日的實戰課程與 AI 專案依日期整齊排列，您可以自由點擊切換，體驗與雲端後端即時通訊的數據魅力！
""")
