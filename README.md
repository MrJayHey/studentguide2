# Запуск на удаленном сервере:


1. [Установите Docker на сервер](https://docs.docker.com/engine/install/ubuntu/), если он еще не установлен;
2. Клонируйте репозиторий:
```bash
git clone <ссылка-на-репозиторий-гит>
cd studentguide2
```
>Не забудьте выбрать нужную ветку, если развертка происходит не с основной ветки
3. **здесь будет пункт про работу с .env файлами**
4. Укажите IP сервера в `ALLOWED_HOSTS` в файле `settings.py`
4. Выполните команду сборки:
```bash
sudo docker-compose up -d --build
```
5. Выполните команду создания суперпользователя:
```bash
sudo docker exec -it studentguide2-backend python manage.py createsuperuser
```
