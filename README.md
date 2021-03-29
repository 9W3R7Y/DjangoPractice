# Djangoなんもわからん

なんもわからんので真面目に勉強する



## プロジェクトの作成

プロジェクトのディレクトリを作成し，ターミナルで以下のコマンドを実行．設定用のファイルは`config`に保存される．

`> django-admin startproject config . `



## サーバーの起動

ターミナルでコマンドを入力

`> python manage.py runserver`



## 管理ユーザー(admin)の作成

ターミナルでコマンドを入力し指示に従う．http://127.0.0.1:8000/admin/ にアクセスし，登録したアカウントでログインする．

`> python manage.py createsuperuser`



## アプリの作成

ターミナルでコマンド入力．hogeはアプリの名前
`> python manage.py startapp hoge`



## 初歩的なViewとURLconf

### Viewとは

リクエストを受け取って処理し．レスポンスを返す．各ページの機能．



### Viewの場所

`hoge/viwes.py`



### Viewの書き方

 関数を定義し，HttpResponceを返す．（クラスのメソッドとすることもできる）

``` python
#from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the index page of App")
```



### URLディスパッチャとは

URLconfをもとに，リクエストされたURLと対応するViewを呼びだす



### URLconfに記述するもの

`urls.py`の`urlpatterns`にURLのパターン, 対応するview，nameを記述する．また，`app_name`を設定し，名前空間を設定する．



### URLconfの場所

* ルートのURLconf…`config\urls.py`

* アプリのURLconf...`hoge\urls.py`



### **アプリのURLconfの書き方**

```python
#from django.urls import path
# from . import views

app_name = 'hoge'
urlpatterns = [
    path('', views.index, name='index'),
]
```



### ルートのURLconfの書き方

アプリのURLconfを認識させる．基本的に`include()`を使う．

```python
# from django.contrib import admin
# from django.urls import include, path

urlpatterns = [
    path('hoge/', include('hoge.urls')),
    path('admin/', admin.site.urls),
]
```



### URLディスパッチャの動き

この状態で`>python manage.py runserver `を実行し，http://127.0.0.1:8000/hoge/ にアクセスすると以下のような流れでページが表示される

1. URLディスパッチャがルートのURLconfを参照

2. リクエストされたURLが`hoge/`とマッチ

   → `include()`の引数である`hoge.urls`に飛ぶ

3. リクエストされたURLが`''`とマッチ

   →`viwes.index`が呼び出される

4. `viwes.index()`が`HttpResponse()`を返す．

5. `This is the index page of App`と表示される．



### パスコンバータの利用

リクエストされたURL内の文字列情報をViewに受け渡す．`<int:<変数名>>` などが利用可能

```python
urlpatterns = [
    path('path_converter/<int:num>', views.PathConverterExample, name='Path Converter'),
]
```

上記の設定では変数`num`がViewに受け渡される．それに合わせて，View関数も変数`num`を受け取れるようにする

```python
def PathConverterExample(request, num):
    return HttpResponse(num)
```

この状態で http://127.0.0.1:8000/hoge/path_converter/100 にアクセスすると．`num`＝100となるため，100と表示される．



## テンプレートの利用とRender()

### テンプレートとは

コンテキスト（変数名と値がペアとなった辞書）を参照し，単純なロジックを実行することのできるHTMLコンテンツ．



### テンプレートの場所

テンプレートは`hoge/templates/hoge/huga.html`に置く．ディレクトリ構造は以下のようになる．

```
ROOT:.
|
略
|
\---hoge
    |
    略
    |
    \---templates
        \---hoge
                huga.html
```



### テンプレートの機能

* `{{ <変数名> }}`でコンテキストに渡された変数を参照．

* `{% <タグ名> "<引数>" %}`でテンプレートタグを用いる．ロジックを実行．

  例）

  * `{% if <条件>%}` ... `{% elif <条件>%}` ... `{% else %}` ... `{% endif %}`
  * `{% for <要素> in <リスト>%}` ... `{% endfor %}`
  * `{% url 'アプリ名:View名' %}`



### テンプレートの詳細

 https://djangoproject.jp/doc/ja/1.0/topics/templates.html



### Render()

 View関数内で作成されたコンテキストをテンプレートに渡し，HttpResponceを返す．例えば以下のViewを用意し，

```python
# from django.shortcuts import render

def RenderTemplateExample(request):
    context = {'text': "Hello, world."}
    return render(request, 'hoge/huga.html', context)
```

`hoge/huga.html`を以下のようにしたとする．

```html	
{{text}}
```

この状態で`RenderTemplateExample`が呼び出されると，"Hello, world"という値をもつ変数`text`を持つ`context`がテンプレートである`hoge/huga.html`に受け渡される．テンプレートは`{{text}}`を参照しそれを表示する．



## フォームの作成とリダイレクト

### フォームとは

ユーザーの入力をPOSTできる．



###  フォームの作成

1. フォームの機能を持つテンプレートを作成．`method`をpostaにする．submitされるとactionで指定したURLに飛ぶ．`{% csrf_token %}`をつけないとエラーになる．

   ```html
   Form
   <form method="post" action="{% url 'hoge:submit' %}">
       {% csrf_token %}
       <p><input type="text" name="form_value" size="30"></p>
       <p><input type="submit" value="submit"></p>
   </form>
   ```
   
2. フォームのテンプレートを呼び出すViewを作成

   ```python
   def FormExample(request):
       return render(request, 'hoge/form.html)
   ```

3. submitの遷移先のViewを作成．`request.POST['<変数名>']`テンプレートと変数名を合わせる必要がある．`@csrf_protect`をつけないとエラーになる．POSTの時は`HttpResponseRedirect()`を使う．`reverse()`を使ってリダイレクト先を決める．`args`の値はパスコンバータの値に受け渡される．

   ```python
   # from django.http import HttpResponseRedirect
   # from django.views.decorators.csrf import csrf_protect
   # from django.urls import reverse
   
   @csrf_protect
   def SubmitExample(request):
       form_value = request.POST['form_value']
       return HttpResponseRedirect(reverse('hoge:submitted', kwargs={'form_value': form_value}))
   ```
   
4. リダイレクト先のviewを作成．上の`kwargs`の値はパスコンバータの値として受け渡されるの．

   ```python
   def SubmittedExample(request, form_value):
       return HttpResponse(form_value)
   ```

5. アプリのURLconfを設定．リダイレクト先のURLにはパスコンバータを用意する

   ```python
   app_name = "hoge"
   urlpatterns = [
       # ...
       path('form', views.FormExample, name='from'),
       path('submit', views.SubmitExample, name='submit'),
       path('submitted/<str:form_value>', views.SubmittedExample, name='submitted'),
   ]
   ```

   

## アプリのインストール

`config/settings.py`の`INSTALLED_APPS`に作成したアプリを追加．`hoge\apps.py`に存在する`HogeConfig`クラスをドット繋ぎのPathとして渡す．

```python
INSTALLED_APPS = [
    'hoge.apps.HogeConfig'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



## Databaseとモデルの作成

### Database とは

字のごとく．デフォルトでSQLiteを使用できる．



### モデルとは

データベースのレイアウトやメタデータ．どのようなデータをDatabeseに格納するのかを明示．



### TIME_ZONEの設定

`config/settings.py`内で`TIME_ZONE`を設定．

```python
TIME_ZONE = 'Asia/Tokyo'
```



### モデルの作成

 `app/models.py`を作成しモデルの設定を行う．各モデルはmodels.Modelを継承したクラスとなる．データベースフィールドは`hoge=models.hugaField(options)`という構文で追加できる．

```python
# from django.db import models

class modelA(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField('data published')
```

[Django: モデルフィールドリファレンスの一覧](https://qiita.com/nachashin/items/f768f0d437e0042dd4b3)



### リレーションシップ

  `models.ForeignKey()`を追加すると複数のモデルの要素を紐づけられる．引数にはmodelと`on_delete`の設定を記述．

```python
class modelB(models.Model):
    modelA = models.ForeignKey(modelA, on_delete=models.CASCADE)
```

[Django2.0から必須になったon_deleteの使い方](https://djangobrothers.com/blogs/on_delete/)



### モデルの適用

1. モデルの変更点を抽出してmigrationファイルを作成．

   `> python manage.py makemigrations hoge`

2. マイグレーションする．モデルの変更がデータベースに適用される．

   `> python manage.py migrate`



### クラスメソッドの追加

メソッドを作成できる

```python
class modelA(models.Model):
    #...
    def method(self):
        return hoge
```



### \__str__()メソッド

オブジェクトの表示方法を設定できる

```python	
class modelA(models.Model):
	#...
    def __str__(self):
        return self.text
```



### データベースの操作

[モデル (Model) - データアクセスの基礎](https://python.keicode.com/django/model-data-access-basics.php)



### adminから操作

 `hoge/admin.py`で`admin.site.register(model)`と記述すると，管理者アカウントのトップページにモデルが表示されるようになる．

```python
# from django.contrib import admin
# from .models import modelA

admin.site.register(modelA)
```



## 参考文献

1. [Django ドキュメント](https://docs.djangoproject.com/ja/3.1/)
2. 横瀬 明仁, 現場で使えるDjangoの教科書

