#  Flask + Docker: CI/CD пайплайн

Этот проект демонстрирует простой CI/CD пайплайн с использованием **GitHub Actions**, **Docker** и **Python Flask**.

## 🚀 Возможности

- Простое Flask-приложение  
- Тестирование с помощью `pytest`  
- `Dockerfile` для сборки образа  
- GitHub Actions workflow для:  
  - запуска тестов  
  - сборки образа  
  - отправки образа на Docker Hub  

## ⚙️ Настройка

1. Создай репозиторий на GitHub и загрузи туда этот проект.  
2. Создай аккаунт на [Docker Hub](https://hub.docker.com/), если ещё нет.  
3. Создай **Docker Hub Access Token**:
   - Перейди в Docker Hub → Settings → Security → **New Access Token**  
4. В настройках GitHub-репозитория (`Settings → Secrets and variables → Actions → New repository secret`) добавь два секрета:
   - `DOCKERHUB_USERNAME` — твой логин на Docker Hub  
   - `DOCKERHUB_TOKEN` — сгенерированный Access Token  
5. Сделай `push` в ветку `main` — пайплайн CI/CD автоматически запустится.

## 🔁 Как это работает

Каждый раз при `push` в ветку `main` GitHub Actions:

1. Запускает тесты с `pytest`  
2. Собирает Docker-образ  
3. Публикует образ на Docker Hub под твоим логином  

## 🖥 Локальный запуск

```bash
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```

Открой в браузере: [http://localhost:5000]