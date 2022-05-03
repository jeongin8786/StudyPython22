#네이버 웹페이지 긁어오기
from ast import Import
from tkinter.tix import InputOnly
from urllib import request


Import request as req

res =req.get('https://www.googl.com')
#print(res.status_code)
print(res.content)