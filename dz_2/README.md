## Образ
> docker build ./ --tag djangoMyTest:0.0.1
## Запуск контейнера
> docker run --name test_djangoMyTest -d -p 8000:8000 djangoMyTest:0.0.1