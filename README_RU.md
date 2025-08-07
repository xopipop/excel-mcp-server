# PC Control MCP Server

Безопасный и мощный сервер управления системой, построенный на Model Context Protocol (MCP).

## 🚀 Возможности

- **Системная информация**: Получение детальной информации об оборудовании, ОС, сети
- **Управление процессами**: Список, мониторинг и управление системными процессами
- **Файловые операции**: Безопасные операции чтения/записи/удаления файлов
- **Сетевые инструменты**: Сканирование портов, пинг, DNS запросы, сетевая статистика
- **Управление службами**: Запуск, остановка, перезапуск системных служб
- **Реестр Windows**: Чтение и изменение реестра Windows
- **GUI автоматизация**: Управление мышью, клавиатурой, создание скриншотов
- **Мониторинг и алерты**: Сбор метрик в реальном времени с настраиваемыми алертами
- **Безопасность корпоративного уровня**: Аутентификация, авторизация, аудит

## 📋 Требования

- Python 3.8+
- Windows/Linux/macOS
- Права администратора для некоторых операций

## 🛠 Установка

### 1. Клонирование репозитория

```bash
git clone https://github.com/your-username/pc-control-mcp.git
cd pc-control-mcp
```

### 2. Создание виртуального окружения

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка конфигурации

Скопируйте и отредактируйте файлы конфигурации:

```bash
cp config/default.yaml config/local.yaml
cp config/security.yaml config/security.local.yaml
```

## 🚀 Быстрый запуск

### Использование скрипта быстрого запуска (рекомендуется)

```bash
# Windows
quickstart.bat

# Linux/macOS
./quickstart.sh
```

### Ручной запуск

```bash
python main.py
```

### Запуск с пользовательской конфигурацией

```bash
# Через переменные окружения
export PC_CONTROL_SERVER__PORT=8080
export PC_CONTROL_SECURITY__ENABLED=true
python main.py
```

## ⚙️ Конфигурация

### Основная конфигурация (`config/default.yaml`)

```yaml
server:
  name: "PC Control MCP Server"
  version: "2.0.0"
  host: "localhost"
  port: 3000
  
logging:
  level: "INFO"
  format: "json"
  
security:
  enabled: true
  authentication:
    type: "basic"  # basic, token, none
```

### Безопасность (`config/security.yaml`)

```yaml
authentication:
  type: "basic"
  basic:
    users:
      - username: "admin"
        password_hash: "$2b$12$..."
        role: "admin"

authorization:
  default_role: "user"
  roles:
    admin:
      - "*"  # Все операции
    user:
      - "system:read"
      - "process:read"
      - "file:read"
```

## 📚 Использование

### Примеры команд

#### Получение системной информации
```python
result = await system_tools.get_system_info(info_type="all")
```

#### Список процессов
```python
processes = await process_tools.list_processes(
    filters={"min_cpu": 5.0, "limit": 10}
)
```

#### Пинг хоста
```python
ping_result = await network_tools.ping_host(
    host="google.com",
    count=4
)
```

#### Создание скриншота
```python
screenshot = await automation_tools.take_screenshot(
    region=[0, 0, 1920, 1080],
    save_path="screenshot.png"
)
```

## 🛡️ Безопасность

### Встроенные механизмы защиты

1. **Валидация входных данных**: Все входные данные проверяются
2. **Защита от path traversal**: Блокировка доступа к родительским директориям
3. **Ограничение команд**: Белый/черный список команд
4. **Аудит логирование**: Все операции записываются
5. **Rate limiting**: Защита от DDoS

### Рекомендации по безопасности

- Используйте сильные пароли
- Включите аутентификацию в production
- Регулярно проверяйте логи аудита
- Ограничьте сетевой доступ файрволом
- Запускайте с минимальными привилегиями

## 🧪 Тестирование

### Запуск всех тестов

```bash
pytest
```

### Запуск с покрытием

```bash
pytest --cov=src --cov-report=html
```

### Запуск конкретных тестов

```bash
pytest tests/unit/test_security.py -v
```

## 📊 Мониторинг

### Настройка алертов

```python
from src.monitoring import AlertRule

# Создание правила для высокого CPU
cpu_alert = AlertRule(
    name="high_cpu",
    metric="cpu.percent",
    condition="gt",
    threshold=80.0,
    duration=timedelta(minutes=5)
)

alert_manager.add_rule(cpu_alert)
```

### Пользовательские метрики

```python
# Регистрация коллектора
def custom_metric():
    return get_custom_value()

metrics_collector.register_collector("custom.metric", custom_metric)
```

## 🔧 Расширение функциональности

### Добавление нового инструмента

1. Создайте файл в `src/tools/`:
```python
class MyTool:
    def __init__(self, security_manager):
        self.security = security_manager
    
    async def my_operation(self, param: str) -> Dict[str, Any]:
        # Валидация
        param = self.security.validate_input('command', param)
        
        # Операция
        result = perform_operation(param)
        
        # Возврат
        return {"result": result}
```

2. Зарегистрируйте в `main.py`
3. Добавьте тесты

## 🐛 Известные проблемы

- GUI автоматизация требует активного дисплея
- Некоторые операции требуют прав администратора
- Registry tools доступны только на Windows

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку функции (`git checkout -b feature/AmazingFeature`)
3. Закоммитьте изменения (`git commit -m 'Add AmazingFeature'`)
4. Запушьте в ветку (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

## 📄 Лицензия

Распространяется под лицензией MIT. См. `LICENSE` для подробностей.

## ⚠️ Отказ от ответственности

Этот инструмент предоставляет мощные возможности управления системой. Используйте ответственно и только на системах, где у вас есть разрешение. Авторы не несут ответственности за любой ущерб или неправильное использование.

## 📞 Поддержка

- Документация: [docs/](docs/)
- Проблемы: [GitHub Issues](https://github.com/your-username/pc-control-mcp/issues)
- Email: support@example.com