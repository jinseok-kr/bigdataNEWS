from django.shortcuts import render, HttpResponse

from .models import User, News, Interest, Scrap

# Create your views here.

# 맨 처음 화면
## 클라우드(가운데), 회원가입|로그인(우측상단)->Mypage|로그아웃(우측상단), 클라우드 대표뉴스목록(우측), 스크랩 목록(하단)
def index(request):
    return render(request, 'index.html')


# def index2(request):
#     datas = User.objects.all()
#     datas2 = News.objects.get(pk=1)
#     datas3 = Scrap.objects.filter(news_id=1)
#     return
# 회원가입 페이지
## email입력, pw입력, pw다시확인 입력 -> DB 등록
### 가능하면 이메일인증 가능토록

# Mypage 페이지
## 비밀번호 변경, 스크랩 목록, 키워드 직접 편집(인당 30개정도는)

# Scrap 페이지
## 스크랩한 뉴스 목록(좌측), 뉴스기사(가운데), 편집기능(우측)

# 뉴스 페이지
## 보여줄 뉴스 전체


#####장고 워드클라우드 생성 관련

# <div style="margin-bottom:20px;"> {{ wordcloud }} </div>
# &nbsp;<span id="clipboard-movie"></span><br />
#
# #from django.shortcuts import render
# #from django.http import HttpResponse
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from .models import ArticleData, Category, Keyword
#
# import requests
# from urllib.parse import urlparse
# from newspaper import Article# Newspaper
# import matplotlib.pyplot as plt
#
# import numpy as np
# from PIL import Image
# from wordcloud import STOPWORDS
#
# def word_cloud(text):
#     whale_mask = np.array(Image.open("PK_t.png"))
#     stopwords ={'은','입니다'}
#     plt.figure(figsize = (20,5))
#     #plt.imshow(whale_mask , cmap = plt.cm.gray , interpolation = 'bilinear')
#     font_path = 'C:/Users/Jeong Suji/NanumBarunGothic.ttf'
#     wc = WordCloud(font_path=font_path,background_color = 'white', max_words=2000, mask = whale_mask,
#               stopwords = stopwords)
#     wc= wc.generate(text)
#     plt.figure(figsize= (10,5))
#     plt.imshow(wc,interpolation= 'bilinear')
#     plt.axis("off")
#     image = io.BytesIO()
#     plt.savefig(image, format='png')
#     image.seek(0)  # rewind the data
#     string = base64.b64encode(image.read())
#
#     image_64 = 'data:image/png;base64,' + urllib.parse.quote(string)
#     return image_64
#
# def cloud_gen(request):
#     text = ''
#     for i in News.objects.all():
#         if __name__ == '__main__':
#             text += i.text
#     wordcloud = word_cloud(text)
#     return render(request, 'articles/index.html', {'wordcloud':wordcloud})
#
#
#
# # Display the generated image:
# import matplotlib.pyplot as plt
# import io
# import urllib, base64
# def word_cloud():
#     '''your code'''
#     plt.imshow(wc, interpolation='bilinear')
#     plt.axis("off")
#
#     image = io.BytesIO()
#     plt.savefig(image, format='png')
#     image.seek(0)  # rewind the data
#     string = base64.b64encode(image.read())
#
#     image_64 = 'data:image/png;base64,' + urllib.parse.quote(string)
#     return image_64