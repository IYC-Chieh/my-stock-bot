import twstock
from twstock import BestFourPoint
import time

# 設定要分析的股票代碼 (可自行修改，例如 '0050')
target_stock = '2330' 

print(f"開始分析股票代碼: {target_stock}")

# 獲取股票數據
stock = twstock.Stock(target_stock)

# 使用 BestFourPoint 演算法分析 (這是 twstock 內建的策略分析)
bfp = BestFourPoint(stock)
analysis = bfp.best_four_point()

# 顯示結果
if analysis:
    print(f"-------------- 分析報告 --------------")
    print(f"股票: {target_stock}")
    print(f"收盤價: {stock.price[-1]}")
    print(f"AI 訊號: {analysis}") # 顯示買進或賣出建議
    print(f"------------------------------------")
else:
    print("目前無明顯買賣訊號，或資料獲取失敗。")
4. 點擊頁面右上角的 Commit changes (綠色按鈕)，再點一次 Commit changes 確認存檔。

--------------------------------------------------------------------------------
