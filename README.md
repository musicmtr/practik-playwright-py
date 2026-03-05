# practik-playwright-py
learning playwright with python and pytest
1. git clone новой репы, проверка гит соединения
https://github.com/musicmtr/practik-playwright-py
2. создать структуру проекта и сборку окружения
3. установка внутри проекта
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install
```
4. уже можно проверить запуск тестов
```
pytest --headed --slowmo 50 -s 
```

``` используемые технолоджи python 3.12 playwright pytest POM подход```
5. структура проекта
```
tests->api and ui 
test_data - со списком данных для тестов, пример который 
использовал это содержимое карусели на страницы доступных сервисов
pages - pom практика у каждой страницы свой функционал свои классы, 
там же наследование от бэейс пейдж
locators - выделение локаторов в одно место и обращение как к константе
omponents - для сложных 
```