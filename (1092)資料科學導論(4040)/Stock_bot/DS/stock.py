import os
from datetime import datetime
import requests
import numpy as np
import plotly.graph_objects as go
import plotly.offline as py
from plotly.graph_objs import Scatter, Layout
import pandas as pd
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

class Stock(object):
    def __init__(self, req):
        self.type = req.get("queryResult").get("parameters").get("Service")
        self.chat_id = req.get("user").get("chat").get("id")

    def idvStock(self, req):
        stockNo = req.get("queryResult").get("parameters").get("Stock")
        url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY'
        params = dict(
            response='json',
            date=datetime.today().strftime("%Y%m%d"),
            stockNo=req.get("queryResult").get("parameters").get("Stock")
        )
        res = requests.get(url=url, params=params)
        jsonData = res.json()
        print(jsonData)
        #轉換 list 變 numpy 陣列
        nData = np.array(jsonData.get('data'))
        return '今日:{}\r\n{}:{},{}:{},\r\n{}:{},{}:{}'.format(
            params.get("date"), 
            jsonData.get('fields')[3], nData[0,3],
            jsonData.get('fields')[6], nData[0,6],
            jsonData.get('fields')[4], nData[0,4],
            jsonData.get('fields')[5], nData[0,5],    
        )

    def inlineList(self, req, bot):
        self.chat_id = req.get("user").get("chat").get("id")
        keyboard = [
            
            [
                InlineKeyboardButton("日成交統計", callback_data='day statistic'),
                InlineKeyboardButton("月成交統計", callback_data='month statistic'),
                InlineKeyboardButton("年成交統計", callback_data='year statistic')
            ],
            [
                InlineKeyboardButton("T法人籌碼圖", callback_data='Corporat')
            ]
            
        ]

        replyMarkup = InlineKeyboardMarkup(keyboard)
        bot.sendMessage(chat_id=self.chat_id, text='成交資訊統計圖：', reply_markup=replyMarkup)
        speech = "已直接在 telegram 回應"
        return { 
            "textToSpeech": speech,
            "ssml": speech,
            "displayText": speech
            }
    
    #個股日成交資訊
    #https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html
    def day(self, req, bot):
        self.chat_id = req.get("user").get("chat").get("id")
        context = req.get("queryResult").get("outputContexts")[0].get("parameters")
        print(context.get("Stock_Statistic"))
        
        
        url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY'
        params = dict(
            response='json',
            date=datetime.today().strftime("%Y%m%d"),
            stockNo=context.get("Stock")
        )
        res = requests.get(url=url, params=params)
        jsonData = res.json()
        #轉換 list 變 numpy 陣列
        nData = np.array(jsonData.get('data'))

        fig = go.Figure(data=[go.Candlestick(x=nData[:,0],
            open=nData[:,3],
            high=nData[:,4],
            low=nData[:,5],
            close=nData[:,6])])

        if not os.path.exists("images"):
              os.mkdir("images")
        img = "images/{}-{}.png".format(context.get('Stock_Statistic'),context.get("Stock"))
        fig.write_image(img)

        req.get("queryResult").get("outputContexts")[0].get("parameters").get("Stock")
        #https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#working-with-files-and-media
        bot.sendPhoto(chat_id=self.chat_id, photo=open(img, 'rb'), caption=context.get('Stock.original'))
        speech = context.get('Stock.original') + "個股成交資訊-{}".format(context.get('Stock.original'))
        return { 
            "textToSpeech": speech,
            "ssml": speech,
            "displayText": speech
            }
    def month(self, req, bot):
        self.chat_id = req.get("user").get("chat").get("id")
        context = req.get("queryResult").get("outputContexts")[0].get("parameters")
        print(context.get("Stock_Statistic"))
        url = 'https://www.twse.com.tw/exchangeReport/FMSRFK'
        params = dict(
            response='json',
            date=datetime.today().strftime("%Y%m%d"),
            stockNo=context.get("Stock")
        )
       
        res = requests.get(url=url, params=params)
        print(res)
        jsonData = res.json()
        #轉換 list 變 numpy 陣列
        nData = np.array(jsonData.get('data'))
        y=nData[:,2]
        y[y == ''] = 0.0 
        y = y.astype(np.float64)
        y = y.tolist() 

        trace1=go.Scatter(
        name="high",
        x=nData[:,1],
        y=y
        )
        trace2=go.Scatter(
        name="low",
        x=nData[:,1],
        y=nData[:,3]
        )
        trace3=go.Scatter(
        name="VWAP",
        x=nData[:,1],
        y=nData[:,4]
        )
        
        layout=go.Layout(
        showlegend=True,
        # 设置图例相对于左下角的位置
        legend=dict(
        x=0.9,
        y=1.1
        )
        )
        data=[trace1, trace2,trace3]
        fig=go.Figure(data=data, layout=layout)
        fig.update_yaxes( dtick=20)
        if not os.path.exists("images"):
              os.mkdir("images")
        img = "images/{}-{}.png".format(context.get('Stock_Statistic'),context.get("Stock"))
        fig.write_image(img)

        req.get("queryResult").get("outputContexts")[0].get("parameters").get("Stock")
        #https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#working-with-files-and-media
        bot.sendPhoto(chat_id=self.chat_id, photo=open(img, 'rb'), caption=context.get('Stock.original'))
        speech = context.get('Stock.original') + "個股成交資訊-{}".format(context.get('Stock.original'))
        return { 
            "textToSpeech": speech,
            "ssml": speech,
            "displayText": speech
            }    
    def year(self, req, bot):
        self.chat_id = req.get("user").get("chat").get("id")
        context = req.get("queryResult").get("outputContexts")[0].get("parameters")
        print(context.get("Stock_Statistic"))
        
        url = 'https://www.twse.com.tw/exchangeReport/FMNPTK'
        params = dict(response='json',stockNo=context.get("Stock"))
        res = requests.get(url=url, params=params)
        jsonData = res.json()

        nData = np.array(jsonData.get('data'))
        x = list(nData[:,0])
        x1 = []
        for i in x:
            x1.append('第{}年'.format(i))

        y=nData[:,4]
        y[y == ''] = 0.0 
        y = y.astype(np.float64)
        y = y.tolist() 

        trace1=go.Scatter(
        name="high",
        x=x1,
        y=y
        )
        trace2=go.Scatter(
        name="low",
        x=x1,
        y=nData[:,6]
        )
        trace3=go.Scatter(
        name="VWAP",
        x=x1,
        y=nData[:,8]
        )
        
        layout=go.Layout(
        showlegend=True,
        # 设置图例相对于左下角的位置
        legend=dict(
        x=0.9,
        y=1.1
        )
        )
        data=[trace1, trace2,trace3]
        fig=go.Figure(data=data, layout=layout)
        fig.update_yaxes( dtick=50)
        fig.update_xaxes(tickangle=45)
        if not os.path.exists("images"):
              os.mkdir("images")
        img = "images/{}-{}.png".format(context.get('Stock_Statistic'),context.get("Stock"))
        fig.write_image(img)

        req.get("queryResult").get("outputContexts")[0].get("parameters").get("Stock")
        #https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#working-with-files-and-media
        bot.sendPhoto(chat_id=self.chat_id, photo=open(img, 'rb'), caption=context.get('Stock.original'))
        speech = context.get('Stock.original') + "個股成交資訊-{}".format(context.get('Stock.original'))
        return { 
            "textToSpeech": speech,
            "ssml": speech,
            "displayText": speech
            }    
    def Corporat(self, req, bot):
        self.chat_id = req.get("user").get("chat").get("id")
        context = req.get("queryResult").get("outputContexts")[0].get("parameters")
        print(context.get("Stock_Statistic"))
        
        a= context.get("Stock")
        url = 'http://jsjustweb.jihsun.com.tw/z/zc/zcl/zcl.djhtm?a={}&b=4'.format(a)
        df = pd.read_html(url)
        df2 = df[2][7:46][::-1][[0,4]].values
        years = df2[:,0]

        y=df2[:,1]
        y[y == ''] = 0.0 
        y = y.astype(np.float64).tolist() 
        z=[]
        for i in y:
            if i>=0:
                z.append('red')
            else:
                z.append('green')
        
        fig = go.Figure()

        fig.add_trace(go.Bar(x=years, y=y,
                            marker_color=z,
                            name='expenses'))

        fig.update_xaxes(tickangle=50)
        if not os.path.exists("images"):
              os.mkdir("images")
        img = "images/{}-{}.png".format(context.get('Stock_Statistic'),context.get("Stock"))
        fig.write_image(img)

        req.get("queryResult").get("outputContexts")[0].get("parameters").get("Stock")
        #https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#working-with-files-and-media
        bot.sendPhoto(chat_id=self.chat_id, photo=open(img, 'rb'), caption=context.get('Stock.original'))
        speech = context.get('Stock.original') + "個股成交資訊-{}".format(context.get('Stock.original'))
        return { 
            "textToSpeech": speech,
            "ssml": speech,
            "displayText": speech
            }    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

        