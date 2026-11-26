import requests

class Check:
    def get_all_posts(self):
      responce = requests.get('https://dummyjson.com/posts')
      assert responce.status_code == 200, 'Ошибка - статус 200'
      data = responce.json()
      assert len(data['posts']) == 30, 'Ошибка, постов не 30'
      print('Получены все посты')

    def get_a_single_posts(self):
       responce = requests.get('https://dummyjson.com/posts/1')
       assert responce.status_code == 200, 'Ошибка - статус 200'
       data = responce.json()
       assert data['id'] == 1, 'id не равен 1'
       print('Проверка ID прошла успешно')

    def search_posts(self):
      responce = requests.get('https://dummyjson.com/posts/search?q=love')
      assert responce.status_code == 200, 'Ошибка - статус 200'
      data = responce.json()
      for post in data['posts']:
         assert 'love' in post['title'].lower() or 'love' in post['body'].lower(), 'Нет слова love'      
      print('Поиск поста успешно завершен') 

    def limit_and_skip_posts(self):
      #params = {
             #  'limit':10,
            #   'skip':10,
           #    'select':'title, reaction, userID'
          #  }
      responce = requests.get('https://dummyjson.com/posts?limit=10&skip=10&select=title,reactions,userId')
      assert responce.status_code == 200, 'Ошибка - статус 200'
      data = responce.json()
      if data['posts']:
        print('Проверка лимитов завершена успешно')

    def sort_posts(self):
       responce = requests.get('https://dummyjson.com/posts?sortBy=title&order=asc')
       assert responce.status_code == 200, 'Ошибка - статус 200'
       data = responce.json() 
       titles = [post['title'] for post in data['posts']]
       assert titles == sorted(titles), 'Список отсортирован не по возрастанию'
       print('Проверка сортировки прошла успешно')
       # тут я спросил нейронку подсказать все таки с этим

    def get_all_posts_tags(self):
        response = requests.get('https://dummyjson.com/posts/tags')
        assert response.status_code == 200, 'Ошибка - статус 200'
        data = response.json()
        tag_names = []
        for tag in data:
            tag_names.append(tag['name'])
        expected_tags = ['History', 'American', 'Crime', 'French', 'Fiction', 'English']
        for expected in expected_tags:
            assert expected in tag_names, f'Нет нужного тега: {expected}'
        print('Получены все теги')
        #тут про два цткла также нейронка подсказала

    def get_posts_tag_list(self):
        responce = requests.get('https://dummyjson.com/posts/tag-list')
        assert responce.status_code == 200, 'Ошибка - статус 200'
        data = responce.json()
        assert data != [], 'Пустой список'
        example_tags = ["history",
            "american",
            "crime",
            "french",
            "fiction",
            "english",
            "magical",
            "mystery",
            "love",
            "classic",
            "memory",
            "nostalgia",
            "nature",
            "tranquility",
            "life",
            "books"]
        for tag in example_tags:
           assert tag in data, 'Нет нужного тега'#Я тут не очень понял, что именно нужно
        print('Тег был получен')      
           
    def get_posts_by_a_tag(self):
       responce = requests.get('https://dummyjson.com/posts/tag/life')
       assert responce.status_code == 200, 'Ошибка - статус 200'
       data = responce.json()
       for posts in data['posts']:
          assert 'life' in [tag.lower() for tag in posts['tags']], 'Ошибка. Тэг должен быть life'#тут мне уже нейронка подсказала
       print('Тэг был получен. Проверка завершена')

    def get_all_posts_by_user_id(self):
       responce = requests.get('https://dummyjson.com/posts/user/5')
       assert responce.status_code == 200, 'Ошибка - статус 200'
       data = responce.json()
       for id in data['posts']:
          assert id['userId'] == 5, 'Нет user_id'
       print('Все посты user_id проверны успешно')


    def get_posts_comments(self):
        responce = requests.get('https://dummyjson.com/posts/1/comments')
        assert responce.status_code == 200, 'Ошибка - статус 200'
        data = responce.json()
        for comment in data['comments']:
           assert comment['postId'] == 1, 'Неверн указан postId'
        print('Проверка получения postId была завершена успешно')

    def add_a_new_post(self):
       pass

    def update_a_post(self):
        pass

    def delete_a_post(self):
        pass










n = Check()
n.get_all_posts()
n.get_a_single_posts()
n.search_posts()
n.limit_and_skip_posts()
n.sort_posts()
n.get_all_posts_tags()
n.get_posts_tag_list()
n.get_posts_by_a_tag()
n.get_all_posts_by_user_id()
n.get_posts_comments()
