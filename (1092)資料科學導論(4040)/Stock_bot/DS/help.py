class Help(object):
    def __init__(self, req):
        self.type = req.get("queryResult").get("parameters").get("serviceterm")
        self.chat_id = req.get("user").get("chat").get("id")
        
    def help(self):
        
        x = '請試著輸入股票代碼或名稱喔'
        
        return x