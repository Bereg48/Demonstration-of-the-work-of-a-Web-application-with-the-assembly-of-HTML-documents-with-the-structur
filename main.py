from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from urllib.parse import urlparse, parse_qs

# Для начала определим настройки запуска
hostName = "localhost" # Адрес для доступа по сети
serverPort = 8080 # Порт для доступа по сети

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def __get_html_content(self):
        return """
        <!doctype html>
<html lang="ar" dir="rtl">
<head>
    <h1><center>Контакты</center></h1>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css"
          integrity="sha384-PJsj/BTMqILvmcej7ulplguok8ag4xFTPryRq8xevL7eBYSmpXKcbNVuy+P0RMgq" crossorigin="anonymous">

    <title>Контакты</title>
</head>

<body>
<div class="container" >
    <div class="row mt-5 " style="position: relative; top: -20px; left: -20px;">
<ul class="nav flex-column text-white" >
  <li class="nav-item bg-primary border-bottom border-bottom-dark text-white" style="position: relative; top: -20px; left: -1500px;">
    <a class="nav-link active text-white" aria-current="page" href="http://localhost:63342/Home_work_19_1/main.html?_ijt=quu5g9eg010b8u9rhi1l5nimuk&_ij_reload=RELOAD_ON_SAVE">Главная</a>
  </li>
  <li class="nav-item bg-primary border-bottom border-bottom-dark text-white" style="position: relative; top: -20px; left: -1500px;">
    <a class="nav-link active text-white" aria-current="page" href="http://localhost:63342/Home_work_19_1/catalog.html?_ijt=quu5g9eg010b8u9rhi1l5nimuk&_ij_reload=RELOAD_ON_SAVE">Каталог</a>
  </li>
  <li class="nav-item bg-primary border-bottom border-bottom-dark text-white" style="position: relative; top: -20px; left: -1500px;">
    <a class="nav-link active text-white" aria-current="page" href="http://localhost:63342/Home_work_19_1/Contacts.html?_ijt=quu5g9eg010b8u9rhi1l5nimuk&_ij_reload=RELOAD_ON_SAVE">Контакты</a>
  </li>
</ul>
        </div>
    </div>
    <div class="container" >
    <div class="row mt-5">
        <div class="col-4">
            <div class="card bg-primary" style="position: relative; top: -200px; left: -700px;">
                <div class="card-body text-white">
                    <h3 class="card-title"><center>Контактная информация</center></h3>
                    <div class="row"></div>
                    <center>
                    <div class="col-3">г.Москва</div>
                    </center>
                    <div class="p-2"><center>Солнцевский проспект, 4</center></div>
                </div>
</div>
          </div>
                  <div class="col-4">
            <div class="card" style="position: relative; top: -200px; left: 250px;">
                <div class="card-body">
                    <h3 class="card-title"><center>Оставьте заявку</center></h3>
                  <form>
  <div class="mb-3">
    <input name="name" type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Имя">
  </div>
  <div class="mb-3">
    <input name="email" type="email" class="form-control" id="exampleInputEmail1" placeholder="email">
  </div>
  <div class="mb-3">
    <textarea class="form-control" placeholder="Сообщение" id="exampleFormControlTextarea1" rows="3"></textarea>
  </div>
  <button name="message" type="submit" class="btn btn-primary">Отправить</button>
</form>

  </body>
</html>"""
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        query_components = parse_qs(urlparse(self.path).query)
        page_content = self.__get_html_content()
        self.send_response(200) # Отправка кода ответа
        self.send_header("Content-type", "text/html") # Отправка типа данных, который будет передаваться
        self.end_headers() # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page_content, "utf-8")) # Тело ответа

if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрам в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
