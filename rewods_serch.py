import pyautogui
import time
import random
import string

pyautogui.FAILSAFE = True

# 少し待機してからSpotlightを開く
time.sleep(2)

# Cmd + SpaceでSpotlightを開く
pyautogui.keyDown('command')
pyautogui.press('space')


pyautogui.keyUp('command')


# 少し待機
time.sleep(1)

# "Chrome"と入力
pyautogui.typewrite('Chrome')

# Enterキーを押してChromeを起動
pyautogui.press('enter')

# Chromeが開くまで待機
time.sleep(3)

# 10回の検索を実行
for _ in range(90):
    # アドレスバーにフォーカスする
    pyautogui.hotkey('command', 'l')

    # Googleのページが開くまで待機
    time.sleep(3)

    # ランダムな検索文字列を生成
    search_text = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    # 検索ワードを入力
    pyautogui.typewrite(search_text)

    # Enterキーで検索を実行
    pyautogui.press('enter')

    # 次の検索まで少し待機
    time.sleep(3)
