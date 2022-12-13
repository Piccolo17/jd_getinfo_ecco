from selenium import webdriver
import re
import time
browser = webdriver.Chrome()
url = 'https://item.jd.com/10058650800128.html#comment'
browser.get(url=url)
time.sleep(3)
browser.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[5]').click()
time.sleep(3)
all = []
for i in range(7):
    try:
        data = browser.page_source
        p_comment = '<p class="comment-con">(.*?)</p>'
        comment = re.findall(p_comment,data)
        all.append(comment)
        # 点击下一页
        browser.find_element_by_xpath('//*[@id="comment-0"]/div[12]/div/div/a['+str(i+3)+']').click()
        time.sleep(3)
    except Exception:
        print("fail")

comment = sum(all,[])

# 词云图绘制
import jieba
from wordcloud import WordCloud
from collections import Counter

# 评论数据清洗
for i in range(len(comment)):
    comment[i] = re.sub('<br>',",",comment[i])

# 评论数据写入txt
with open(file =r'D:\vscode\download\test\test1.txt',mode='a') as f1: #意为file文件夹就相当于f1
    for i in range(len(comment)):
        data = f1.write(comment[i]+'\n')
	

text = open(r'D:\vscode\download\test\test1.txt').read()  # 标明文本路径，打开
words = jieba.cut(text)
#2.通过for循环来提取words列表中的3个字以上的词语
report_words = []
for word in words:
    if len(word)>=3:
        report_words.append(word)  #将3个字以上的词语放入到列表
print(report_words)

#3.获取打印输出高频词的出现次数
result = Counter(report_words).most_common(10)
print(result)

#4.绘制词云图
content = " ".join(report_words)  #通过join（）函数把列表转换成字符串（通过‘ ’连接表中的元素）
wc = WordCloud(font_path='simhei.ttf',background_color='white',width=1000,height=600).generate(content)#字体，simhei是黑体，simhei.ttf是黑体字体文件，背景颜色，宽度，高度。根据刚刚生成的content，generate成词云图
wc.to_file(r'D:\vscode\download\test\a.png') #导出为png图片