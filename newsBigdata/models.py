from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

# PRIMARY KEY 설정 안하면 자동으로 id 항목의 요소 생성 (1->increase)

# class Users(models.Model):
#     # auto_increase id
#     username = models.CharField(max_length=10)
#     password = models.CharField(max_length=16)
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Users.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

class News(models.Model):
    # auto_increase
    ## news_id = models.CharField(max_lange=50) // 네이버뉴스 기준 sid(정치,경제,문화 등), oid(언론사구분), aid(기사 구분)의 조합으로 id생성하기
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    main_contents = models.TextField(default='')
    press = models.CharField(max_length=20)
    create_date = models.CharField(max_length=20)
    keywords = models.TextField(default='')

class Scrap(models.Model):
    # auto_increase
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) #유저 id가 9999라고하면 얘는 게스트라서 scrap을 못함? / 로그인 안되있으면 바로 반환?
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    scrap_contents = models.TextField(default='') #news_id를 통해 News테이블의 main_contents를 복사해올것

# 1. scrap 버튼 클릭하면 Scrap table에서 user_id, news_id 가 같은 데이터가 있는지 검사
# 2-1. 없으면 데이터 추가
# 2-2. 있으면 데이터 삭제

class Interest(models.Model):
    # auto_increase
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    interest_key = models.CharField(max_length=20)

# 관심 키워드 분리를 어떻게 해야될까??

# 삭제할듯...
# class Mypage(models.Model):
#     # auto_increase
#     user = models.ForeignKey(User, on_delete=models.CASCADE) #이거 애매함.... onetoone 고민해야한다.
#     interest_key = models.CharField(max_length=200)
#     scrap_DB = models.IntegerField(default=0) #???






