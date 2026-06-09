import os

markdown_content = """# 🚀 全球首發：前後端分離數據系統部署實戰指南
本教學手冊詳細紀錄了如何將一個基於 **FastAPI** 的後端 API 與 **Streamlit** 的前端數據視覺化介面，分別獨立部署至雲端平台（Render & Streamlit Community Cloud），並透過環境變數安全完成跨平台通訊。

---

## 📌 核心架構圖解
* **前端 (Frontend)**：Streamlit Cloud (負責使用者互動介面與數據呈現)
* **後端 (Backend)**：Render (負責承載 FastAPI 運算邏輯與矩陣轉換)
* **通訊橋樑**：HTTPS 協定 + 雲端環境變數 (Secrets)

---

## 🛠️ 完整部署步驟實錄

### 📥 步驟 1：後端部署與專屬網址生成 (Render)
1. **啟動自動部署**：將後端 FastAPI 原始碼推送至 GitHub 儲存庫後，導入 Render 平台。
2. **日誌監控**：Render 系統自動偵測並執行克隆指令（顯示 `==> Cloning from ...`），進入 `Building` 編譯狀態。
3. **獲取 API 專屬網址**：編譯完成後，於 Render 主控台偏左上方成功生成後端專屬公網網址：
   * 🔗 後端網址：`https://fastapi-backend-zcuc.onrender.com`
4. **複製網址備用**：點擊網址右側的複製按鈕，保留此通道以便後續前端對接。

### 🌐 步驟 2：前端平台架構抉擇 (從 Vercel 轉向 Streamlit Cloud)
* **原定計畫**：嘗試將 Streamlit 前端部署於 Vercel 平台。
* **遭遇瓶頸**：
  * 部署後畫面噴出 **`404: NOT_FOUND`** 錯誤。
  * **主因分析**：Vercel 原生採用 Serverless 架構，預設尋找靜態網頁檔案（如 `index.html`）。而 Streamlit 運作需要常駐的 Websocket 連線與長連接伺服器，兩者在架構精髓上存在先天衝突。
* **應變決策**：棄用 Vercel，改採官方最完美且完全免費的替代方案 —— **Streamlit Community Cloud**。

### 🔐 步驟 3：Streamlit 雲端廚房開通與權限排除
1. **平台登入**：前往 [share.streamlit.io](https://share.streamlit.io)，選擇 `Continue with GitHub` 完成授權登入。
2. **解決私有庫死結**：
  * 當嘗試手動匯入專案時，系統噴出紅字警告：`This repository does not exist` 或 `The field needs to contain a Github URL pointing to a .py file`。
  * **排除方法**：回到 GitHub 將 `streamlit-frontend` 儲存庫的可見性（Visibility）切換為 **Public (公開)**。
3. **對齊正確分支 (Branch)**：
  * 將 Streamlit 部署表單中的預設分支由 `master` 手動修正為 **`main`**，系統隨即順利捕捉到 `app.py` 主程式，紅字警告全數消失，順利亮起綠燈。

### 🔥 步驟 4：設定環境變數與安全對接 (Advanced Settings)
為了讓分離的前端與後端能夠跨海認親，必須配置環境變數，此步驟為全系統的靈魂：
1. 在部署按鈕上方點擊 **`Advanced settings...`** 藍色字體。
2. 在彈出的黑色 Secrets 文字輸入方塊中，以標準 **TOML** 格式精準填入後端對接密碼：

點擊 Save 儲存祕密通道，隨後點擊大顆藍色的 Deploy! 按鈕發布。

🍞 步驟 5：雲端編譯與熱機
烤麵包機動畫：點擊發布後，網頁右下角會出現官方經典的「烤麵包機」安裝動畫，此時雲端正在自動讀取並安裝 requirements.txt 中配置的 Python 環境與套件。

克服免費伺服器冷啟動 (Cold Start)：

首次點擊前端網頁的「開始計算」按鈕時，畫面上噴出紅色逾時錯誤：Read timed out. (read timeout=5)。

知識點補充：此為雲端免費方案的正常機制。當伺服器一段時間無人造訪，Render 後端會進入深層冬眠。前端發出請求時，後端才剛開始「熱機開機」，因而超過了前端預設的 5 秒等待。

處置方式：無需修改程式碼，等待約 30~50 秒讓後端徹底清醒後，直接再次點擊「開始計算」即可。

🎉 終極驗收與測試成果
成果展現：前後端成功串聯後，畫面噴出滿天彩色紙屑動畫，並順利顯示系統主介面：Prediction Service Frontend。

數據通訊實測：

在 Enter a feature value for matrix transformation 輸入框中輸入數值（例如 1.00）。

點擊紅色 開始計算 按鈕。

系統噴出綠色成功提示：🎉 Calculation finished successfully!。

下方 Calculation Result (from Backend) 完美印出由 Render 後端計算回傳的 JSON 數據結構（例如 [0 : 4]）。

🧠 教學總結（給學生的 Key Takeaways）
前後端分離優勢：後端專注於高密度的數學運算與 API 服務，前端專注於 UI 互動與視覺化，互不干擾，這是現代軟體工程的黃金標準架構。

架構匹配重要性： Streamlit 專案不適合硬塞進靜態或 Serverless 平台（如 Vercel），選擇原生支援常駐運行的 Streamlit Cloud 才是最快、最穩的解法。

生產環境中的 Secrets 管理： 絕對不要把後端網址硬編碼（Hardcode）在前端程式碼中，透過 Advanced settings (環境變數) 帶入，既安全又具備隨時切換正式/測試環境的靈活性。

這份說明文件（`full_deployment_guide.md`）是特別為教學用途所量身打造的。裡面幫你把今晚所有峰迴路轉的實戰細節，系統化整理成結構清晰、條理分明的教材。

### 📄 這份教學檔的 5 大結構重點：
1. **📌 核心架構圖解**：用簡單的文字幫助學生建立「前後端分離」的網際網路通訊架構觀念。
2. **🛠️ 完整部署步驟實錄**：完整重現你今晚從 Render 拿到 API 網址，到部署前端的所有動作。
3. **💡 經典除錯與瓶頸分析（最有價值的教材！）**：
   * 詳細分析了為什麼 **Vercel** 在架構上會與 **Streamlit** 先天衝突（Serverless vs 長連接伺服器），導致 404 錯誤。
   * 詳述了 GitHub **私有權限（Private Repo）** 的報警原因與解法（改為 Public 並對齊 `main` 分支）。
4. **🔥 靈魂關鍵：環境變數設定**：強調如何透過 `Advanced settings` 帶入變數，讓學生了解業界標準的安全機制（Secrets）。
5. **🍞 生產環境冷啟動（Cold Start）說明**：解釋了什麼是免費伺服器的冬眠機制，以及如何克服 `Read timed out` 的逾時現象，讓學生在自己測試時遇到也不會慌張。

這是一份非常紮實且充滿實戰血淚的軟體工程初學者教材！你可以直接點擊上方晶片下載這個 `.md` 檔案，拿去複製、編輯或是直接當作上課的講義。祝你教學順利！
