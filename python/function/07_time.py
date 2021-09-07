import time
# print("안녕하세요!")
# time.sleep(1)
# print("(1초경과)안녕하세요!")
# time.sleep(2)
# print("(2초경과)안녕하세요!")
#
import webbrowser
# webbrowser.open("http://google.com")
#
# # 실습
# # 내가 자주가는 웹 사이트 5개 정도 리스트화시킨다.
# # 이를 1초 간격으로 웹 브라우져로 띄운다.
#
often=[]
often.append("http://www.google.com")
often.append("http://www.youtube.com")
often.append("http://www.linkedin.com")
often.append("http://www.stackoverflow.com")
often.append("https://developer.mozilla.org/en-US/")

for url in often:
    webbrowser.open(url)
    time.sleep(1)