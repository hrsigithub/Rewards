from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Chromeのオプションを設定
chrome_options = Options()
# 自動化検出を回避するフラグを追加
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
# 情報バー（"Chrome is being controlled by automated test software"）を非表示にする試み
chrome_options.add_argument('--disable-infobars')

# Serviceオブジェクトを作成（ChromeDriverのパスを自動設定するなら以下のようにします）
service = Service()

# WebDriverを初期化
driver = webdriver.Chrome(service=service, options=chrome_options)

# JavaScriptを使ってnavigator.webdriverを削除
driver.execute_cdp_cmd(
    'Page.addScriptToEvaluateOnNewDocument',
    {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'}
)

# テストページを開く
driver.get("https://www.google.com")

# 確認のために待機
time.sleep(100)

# ブラウザを閉じる
# driver.quit()
