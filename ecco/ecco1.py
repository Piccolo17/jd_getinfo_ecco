# 爬取数据
def ecco(page):
    from selenium import webdriver
    import re
    import time
    import pandas as pd
    browser = webdriver.Chrome()
    url = 'https://search.jd.com/Search?keyword=ecco&page='+str(page)
    browser.get(url=url)
    time.sleep(3)

    #将滚动条移动到页面的底部
    js="var q=document.documentElement.scrollTop=100000"  
    browser.execute_script(js)  
    time.sleep(2)
    data = browser.page_source

    # 价格
    p_price = '<i data-price=".*?">(.*?)</i>'
    price = re.findall(p_price,data)

    #店名
    p_shopname='<a target="_blank" class="curr-shop hd-shopname" onclick="searchlog.*?" href=".*?" title=".*?">(.*?)</a>'
    shopname = re.findall(p_shopname,data)

    # 评论数
    p_comment_num = '<a id=".*?" target="_blank" href=".*?" onclick="searchlog.*?;">(.*?)</a>'
    comment_num = re.findall(p_comment_num,data)
    df_data = {
        'price':price,
        'shopname':shopname,
        'comment_num':comment_num
    }
    #3.保存到本地excel文件
    df = pd.DataFrame(df_data)
    df.to_csv(r'D:\vscode\download\test\test01.csv', mode='a', header=False,encoding='utf_8_sig')


for i in range(100):
    ecco(i+1)
    print("第"+str(i+1)+'网页爬去成功')