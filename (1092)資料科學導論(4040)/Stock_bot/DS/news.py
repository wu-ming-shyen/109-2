import requests
from bs4 import BeautifulSoup

class News(object):
    def __init__(self, req):
        self.type = req.get("queryResult").get("parameters").get("serviceterm")
        self.chat_id = req.get("user").get("chat").get("id")
        
    def yahoo(self):
        url = 'https://tw.news.yahoo.com/stock'
        session = requests.Session()
        response = session.get(url,verify=False)
        soup     = BeautifulSoup(response.text, 'html.parser')
        selects = soup.select("h3.Mb\(5px\) a") 
        
        content = ""
        for idx,select in enumerate(selects):
            if idx == 10:
                return content
            title = select.text
            link = url + select["href"]
            content += '{}\n{}\n\n'.format(title,link)
        return content