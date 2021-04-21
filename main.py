import os

from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return "<b>Миссия Колонизация Марса </b>"


@app.route('/index')
def index1():
    return '<b>И на Марсе будут яблони цвести! </b>'


@app.route('/promotion')
def promotion():
    return '<b> Человечество вырастает из детства.<br>Человечеству мала одна планета.' \
           '<br>Мы сделаем обитаемыми безжизненные пока планеты.<br>И начнем с Марса!' \
           '<br>Присоединяйся! </b>'


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" alt="не появилось(" width="300" height="300">
                    <p>Вот она какая, красная планета</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src={url_for('static', filename='img/mars.png')} width="300", height="300">
                        <div class="alert alert-dark" role="alert">
                          <b>Человечество вырастает из детства.</b>
                        </div>
                        <div class="alert alert-success" role="alert">
                          <b>Человечеству мала одна планета.</b>
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          <b>Мы сделаем обитаемыми безжизненные пока планеты.</b>
                        </div>
                        <div class="alert alert-warning" role="alert">
                          <b>И начнем с Марса!</b>
                        </div>
                        <div class="alert alert-danger" role="alert">
                          <b>Присоединяйся!</b>
                        </div>
                      </body>
                    </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <h1 style="text-align:center;">Анкета претендента</h1>
                                <h2 style="text-align:center;">на участие в миссии</h2>
                                <div>
                                    <form class="login_form" method="post">
                                        <input class="form-control"  placeholder="Введите фамилию">
                                        <input class="form-control" placeholder="Введите имя"">
                                        <div class="form-group">
                                            <input name="email" class="form-control" type="email" placeholder="Введите адрес почты">
                                        </div>
                                        <div class="form-group">
                                            <label for="classSelect">Какое у Вас образование?</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>Начальное</option>
                                              <option>Среднее</option>
                                              <option>Высшее</option>
                                            </select>
                                         </div>
                                        <div class="form-group">
                                            <label for="form-check">Какие у Вас есть профессии?</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox">
                                              <label class="form-check-label">
                                                Инженер-исследователь
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox">
                                              <label class="form-check-label">
                                                Инженер-строитель
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox">
                                              <label class="form-check-label">
                                                Пилот
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox">
                                              <label class="form-check-label">
                                                Метеоролог
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox">
                                              <label class="form-check-label">
                                                Инженер по жизнеобеспечению
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox">
                                              <label class="form-check-label">
                                                Инженер по радиационной защите
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox">
                                              <label class="form-check-label">
                                                Врач
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox">
                                              <label class="form-check-label">
                                                Экзобиолог
                                              </label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                        </div>
                                        <div class="form-group">
                                            <label>
                                                Почему Вы хотите принять участие в миссии?
                                            </label>
                                            <textarea class="form-control" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label>Приложите фотографию</label>
                                            <input type="file" class="form-control-file" name="file">
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossorigin="anonymous">
    <title>Варианты выбора</title>
</head>
<body>
<h1>Мое преложение: {planet_name}</h1>
<h2>Эта планета близка к земле;</h2>
<div class="alert alert-success">На ней много необходимых ресурсов;</div>
<div class="alert alert-secondary">На ней есть вода и атмосфера;</div>
<div class="alert alert-warning">На ней есть небольшое магнитное поле;</div>
<div class="alert alert-danger">Наконец, она просто красива!</div>
</body>
</html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level: int, rating: float):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossorigin="anonymous">
    <title>Варианты выбора</title>
</head>
<body>
<h1>Результаты отбора</h1>
<h2>Претендента на участие в миссии {nickname}:</h2>
<div class="alert alert-success">Поздравляем! Ваш рейтинг после {level} этапа отбора</div>
<div>составляет {rating}</div>
<div class="alert alert-warning">Желаем удачи!</div>
</body>
</html>"""


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    s = ''
    if request.method == 'GET':
        if os.path.isfile('static/img/picture.jpg'):
            s += f'<img src="{url_for("static", filename="img/picture.jpg")}">'
        return f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
            <link rel="stylesheet"
                  href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                  integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                  crossorigin="anonymous">
            <title>Отбор астронавтов</title>
        </head>
        <body>
        <h1 style="text-align:center;">Загрузка фотографии</h1>
        <h2 style="text-align:center;">для участия в миссии</h2>
        <form class="login_form" method="post" enctype="multipart/form-data">
            <div class="form-group">
            <label>Приложите фотографию</label>
            <input type="file" class="form-control-file" name="file">
            </div> """ + s if s else '' + """<button type="submit" class="btn btn-primary">Отправить</button>
        </form>
        </body>
        </html>"""
    elif request.method == 'POST':
        f = request.files['file']
        with open('static/img/picture.jpg', 'wb') as file:
            file.write(f.read())
        return f"""<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                    <link rel="stylesheet"
                          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                          crossorigin="anonymous">
                    <title>Отбор астронавтов</title>
                </head>
                <body>
                <h1 style="text-align:center;">Загрузка фотографии</h1>
                <h2 style="text-align:center;">для участия в миссии</h2>
                <form class="login_form" method="post" enctype="multipart/form-data">
                    <div class="form-group">
                    <label>Приложите фотографию</label>
                    <input type="file" class="form-control-file" name="file">
                    </div>
                    <img src="{url_for('static', filename='img/picture.jpg')}">
                    <button type="submit" class="btn btn-primary">Отправить</button>
                </form>
                </body>
                </html>"""


@app.route('/carousel')
def carousel():
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet"
              href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
              integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
              crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
        <title>Варианты выбора</title>
    </head>
    <body>
<h1 style="text-align:center;">Пейзажи Марса</h1>
<div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner d-block">
        <div class="carousel-item active">
            <img src="{url_for('static', filename='img/land1.jpg')}" class="d-block w-100">
        </div>
        <div class="carousel-item">
            <img src="{url_for('static', filename='img/land2.jpg')}" class="d-block w-100">
        </div>
        <div class="carousel-item">
            <img src="{url_for('static', filename='img/land3.jpg')}" class="d-block w-100">
        </div>
    </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.6.0/dist/umd/popper.min.js" integrity="sha384-KsvD1yqQ1/1+IA7gi3P0tyJcT3vR+NdBTt13hSJ2lnve8agRGXTTyNaBYmCR/Nwi" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.min.js" integrity="sha384-nsg8ua9HAw1y0W1btsyWgBklPnCUAFLuTMS2G72MMONqmOymq585AcH49TLBQObG" crossorigin="anonymous"></script>
    </body>
    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
