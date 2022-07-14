from datetime import date
import json
goodslist_=[]
buylist=[]
totallist=[]
discountlist=[]
#列出商品列表
def goodslist():
    with open("goodslist.json","r",encoding="utf-8") as list_:
        goodlist=json.loads(list_.read())
        goodsnum =0        
        print("\n"+"商品序號    "+"商品種類    "+"商品名稱    "+"商品價格")
        for x in goodlist :
            for y in x["item"]:
                data={}      
                data["商品序號"] = goodsnum
                data["商品種類"] = x["type"]
                data["商品名稱"] = y["name"]
                data["商品價格"] = y["price"]
                goodsnum +=1
                print("%d             %s          %s      %s" %(data["商品序號"],data["商品種類"],data["商品名稱"],data["商品價格"]))               
                goodslist_.append(data)

#選擇服務與購買商品
def services():
    dot = True
    while dot:
        choose=input("請輸入您要購買的商品序號(t:結算 q:退出)：")   
        if choose == "t":
            dot=False
        elif choose == "q":
            print("謝謝,歡迎下次光臨！")
            return "q"            
        else:
            global goodsnum_
            goodsnum_=int(input("請輸入您要購買的數量："))       
        def buyitem(n):
            if str(n["商品序號"])==choose:
                return( n["商品種類"],n["商品名稱"],n["商品價格"])        
        thing=map(buyitem,goodslist_)
        list_=list(thing)
        for obj in list_:
            if obj == None:
                pass
            else:
                buylist_="%d*%s:%s" %(goodsnum_,obj[1],obj[-1])
                buylist.append(buylist_)
                if str(obj[0])=="電子":
                    totallist_=0
                    totallist_+=goodsnum_*obj[-1]*0.7
                    totallist.append(totallist_)
                    discountlist.append(1)
                else:
                    totallist_=0
                    totallist_+=goodsnum_*obj[-1]
                    totallist.append(totallist_)               
#購物車清單
def shoppingcart():
    if len(buylist)<1:
        print("您的購物車沒有東西")
    else:
        #折扣信息
        if len(discountlist)>0:
            print("2015.11.11|0.7|電子")
        print("\n")
        for k in buylist:
            print(k)
        print("      ")
        print(date.today()) 
#結算
def total():
    total_=sum(totallist)
    if total_>1000:
        total_=total_-int(200)
        print("2016.3.2 1000 2000")
        print("%.2f"%total_)
    else:
        b=sum(totallist)
        print("%.2f"%b)
    
goodslist()
star=services()
if star == "q":
    exit()
shoppingcart()
total()

