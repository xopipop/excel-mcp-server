# 🚀 Быстрый старт PC Control MCP Server

## 1️⃣ Самый быстрый способ (для разработки)

```bash
# Запуск в режиме разработки (без безопасности)
python dev.py
```

## 2️⃣ Автоматический запуск с установкой

### Windows
```cmd
quickstart.bat
```

### Linux/macOS
```bash
./quickstart.sh
```

Скрипты автоматически:
- ✅ Проверят наличие Python
- ✅ Создадут виртуальное окружение
- ✅ Установят зависимости
- ✅ Создадут конфигурацию
- ✅ Запустят сервер

## 3️⃣ Ручная установка

```bash
# 1. Создание виртуального окружения
python -m venv venv

# 2. Активация
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 3. Установка зависимостей
pip install -r requirements.txt

# 4. Запуск
python main.py
```

## ⚙️ Конфигурация

### Переменные окружения

```bash
# Отключить безопасность (только для разработки!)
export PC_CONTROL_SECURITY__ENABLED=false

# Изменить порт
export PC_CONTROL_SERVER__PORT=8080

# Уровень логирования
export PC_CONTROL_LOGGING__LEVEL=DEBUG
```

### Файлы конфигурации

1. `config/default.yaml` - базовая конфигурация
2. `config/local.yaml` - ваши локальные настройки (создается автоматически)
3. `config/security.yaml` - настройки безопасности

## 🔧 Режимы запуска

### Режим разработки (небезопасный)
```bash
python dev.py
```
- ❌ Безопасность отключена
- 📝 Debug логирование
- 🚀 Быстрый старт

### Production режим
```bash
# С правами администратора/sudo
sudo python main.py
```
- ✅ Полная безопасность
- ✅ Все функции доступны
- ✅ Аудит логирование

## 📋 Проверка работы

После запуска сервер будет доступен через MCP протокол. Вы увидите:

```
PC Control MCP Server v2.0.0 initialized
Starting stdio transport...
Server ready
```

## ❓ Проблемы?

### Python не найден
- Windows: Скачайте с [python.org](https://python.org)
- Ubuntu: `sudo apt install python3 python3-pip python3-venv`
- macOS: `brew install python3`

### Ошибка импорта модулей
```bash
pip install -r requirements.txt
```

### Нужны права администратора
- Windows: Запустите от имени администратора
- Linux/macOS: Используйте `sudo`

## 🎯 Что дальше?

1. Изучите [документацию API](docs/API_RU.md)
2. Настройте [безопасность](config/security.yaml)
3. Попробуйте [примеры использования](README_RU.md#-использование)

---

💡 **Совет**: Для быстрого теста используйте `python dev.py`!