import pyautogui
import time
import random
import string
import subprocess
from datetime import datetime

# -------------------
# 設定
# -------------------
WAIT_BEFORE_START = 2      # 最初の待機秒数
WAIT_AFTER_SPOTLIGHT = 1   # Spotlight起動後の待機
WAIT_AFTER_CHROME = 3      # Chrome起動待機
WAIT_AFTER_SEARCH = 3      # 検索後の待機
SEARCH_COUNT = 5           # 検索回数
USE_JAPANESE = False       # True にすると日本語検索
ALERT_SOUND = "lvup1.mp3"

# 日本語文字リスト
JAPANESE_CHARS = 'あいうえおかきくけこさしすせそたちつてとなにぬねの' \
                 'はひふへほまみむめもやゆよらりるれろわをん' \
                 'アイウエオカキクケコサシスセソタチツテトナニヌネノ' \
                 'ハヒフヘホマミムメモヤユヨラリルレロワヲン一二三四五六七八九十'

# -------------------
# 関数定義
# -------------------
def open_spotlight():
    """Spotlightを開く"""
    pyautogui.keyDown('command')
    pyautogui.press('space')
    pyautogui.keyUp('command')

def launch_chrome():
    """Chromeを起動"""
    pyautogui.typewrite('Chrome')
    pyautogui.press('enter')

def random_search_text(length=10, japanese=False):
    """ランダムな検索文字列を生成"""
    if japanese:
        return ''.join(random.choices(JAPANESE_CHARS, k=length))
    else:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def search_in_chrome(text):
    """Chromeで検索"""
    pyautogui.hotkey('command', 'l')   # アドレスバーへ
    time.sleep(1)
    pyautogui.typewrite(text)
    pyautogui.press('enter')

def play_sound(file_path):
    """終了時に音を鳴らす"""
    try:
        subprocess.run(["afplay", file_path])
    except Exception as e:
        print(f"音声再生失敗: {e}")

# -------------------
# メイン処理
# -------------------
if __name__ == "__main__":
    pyautogui.FAILSAFE = True

    # 初期待機
    time.sleep(WAIT_BEFORE_START)

    # Spotlight → Chrome 起動
    open_spotlight()
    time.sleep(WAIT_AFTER_SPOTLIGHT)
    launch_chrome()
    time.sleep(WAIT_AFTER_CHROME)

    # 検索ループ
    for _ in range(SEARCH_COUNT):
        text = random_search_text(10, USE_JAPANESE)
        search_in_chrome(text)
        time.sleep(WAIT_AFTER_SEARCH)

# 終了時刻の表示
    end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"終了時刻: {end_time}")

    # 終了音
    # play_sound(ALERT_SOUND)
