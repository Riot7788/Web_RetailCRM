## RetailCRM API Integration

Веб-приложение на FastAPI для интеграции с RetailCRM API.
Приложение реализует базовые операции: работы с клиентами, заказами и платежами.

## Возможности
- Создание нового клиента
- Получение списка клиентов
- Фильтрация клиентов по имени, email и дате регистрации
- Создание заказа
- Получение заказов клиента
- Добавление платежа к заказу
- Запуск приложения в Docker-контейнере

## Используемые технологии
- Python 3.11+
- FastAPI
- Pydantic
- HTTPX
- Uvicorn
- Docker
- Docker Compose
- API ключ от RetailCRM

## Настройка

1. Клонируйте репозиторий: git clone https://github.com/Riot7788/Web_RetailCRM
2. Создайте файл `.env` в корневой директории:

```env
RETAILCRM_SITE=ваш_сайт_код
RETAILCRM_URL=https://ваш-домен.retailcrm.ru
RETAILCRM_API_KEY=ваш_api_ключ
```

3. В корне проекта выполните команду:
```bash
docker-compose up --build
```

4. Переходим по адресу:
```bash
http://localhost:8001/docs
```
