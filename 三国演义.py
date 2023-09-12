import jieba
# ---------- 变量excludes含排除的分词，根据输出，可以将不是人名的分词加进去 -------
excludes={"将军", "却说", "荆州", "二人", "不可", "不能", "如此", "商议","左右","军士","军马","主公","如何","次日","引兵","大喜","东吴","天下","魏兵","今日","不敢","于是","陛下","人马","都督","一人","不知","汉中","众将","只见","后主","蜀兵"} 
txt = open("C:\\Users\\Lenovo\\Desktop\\三国演义 (1).txt",mode='r',encoding='utf-8').read() 
words = jieba.lcut(txt)                                                     # 精确模式分词，返回的words为一个列表变量
counts = {}
for word in words:                                                          # 通过迭代，处理同一个人物出现多个名字的
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
for word in excludes:                                          # 从字典中，删除不是人名的词
    del(counts[word])
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)    # 按出现次数，降序排
for i in range(13):                                                  #  只显示前13个   
    word, count = items[i]
    print("(",i+1,")",word, count)
