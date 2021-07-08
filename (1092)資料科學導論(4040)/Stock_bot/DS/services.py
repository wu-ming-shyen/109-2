from telegram import InlineKeyboardButton, InlineKeyboardMarkup

class Services(object):
    def __init__(self, req):
        self.type = req.get("queryResult").get("parameters").get("Service")
        self.chat_id = None
    
    def inlineList(self, req, bot):
        self.chat_id = req.get("user").get("chat").get("id")
        keyboard = [
            [
                InlineKeyboardButton("股票新聞", callback_data='news')
                
            ],
            [
                InlineKeyboardButton("Help", callback_data='/help')
                
            ]
        ]

        replyMarkup = InlineKeyboardMarkup(keyboard)
        bot.sendMessage(chat_id=self.chat_id, text='請選擇以下服務：', reply_markup=replyMarkup)
        speech = "已直接在 telegram 回應"
        return { 
            "textToSpeech": speech,
            "ssml": speech,
            "displayText": speech
            }