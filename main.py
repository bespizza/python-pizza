from flask import Flask #載入 Flask
app=Flask(__name__ )    #建立  Application 物件 __name__ 代表目前執行的模組

#  建立網站首頁的回應方式
@app.route("/") # 函式的裝飾 (Decorator): 以函式為基礎, 提供附加的功能
def index():                #用來回應網站首頁連線的函式
    return "Hello Flask"    #回傳網站首頁的內容

@app.route("/test") # 代表我們要處理的網站路徑  /:網站根目錄
def test():
    return "This is Test"

if __name__=="__main__": # 如果以主程式執行
    app.run()   # 啟動網站伺服器

