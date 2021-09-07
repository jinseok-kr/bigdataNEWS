from django.db import models

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

class User(models.Model):
    # auto_increase id
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class News(models.Model):
    # auto_increase
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    main_contents = models.TextField()
    press = models.CharField(max_length=20)
    create_date = models.CharField(max_length=20)
    keywords = models.TextField()

class Scrap(models.Model):
    # auto_increase
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) #유저 id가 9999라고하면 얘는 게스트라서 scrap을 못함? / 로그인 안되있으면 바로 반환?
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    scrap_contents = models.TextField() #news_id를 통해 News테이블의 main_contents를 복사해올것

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






