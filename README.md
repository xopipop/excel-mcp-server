# PC Control MCP Server v2.0 (RU)

Надёжный MCP‑сервер (Model Context Protocol) для удалённого управления ПК через стандартный интерфейс. Интегрируется с Cursor IDE и другими MCP‑клиентами.

## 🚀 Возможности

### Система
- Аппаратная информация: CPU, память, диски, сети
- Детали ОС: версия, платформа, дистрибутив
- Переменные окружения (секреты маскируются)
- Аптайм системы

### Процессы
- Список с фильтрами/сортировкой
- Запуск/остановка/пауза/возобновление
- Ресурсы процесса: CPU, память, I/O
- Поиск по имени, управление приоритетом

### Файлы
- Чтение/запись/копирование/перемещение/удаление
- Листинг директорий, создание
- Поиск по маске/regex
- Метаданные, использование диска

### Безопасность
- Валидация команд и путей, блок‑листы
- Аудит‑логирование
- Ограничение частоты запросов

## 📋 Требования

- Windows (рекомендовано), также Linux/macOS
- Python 3.8+ (проверено на 3.13)
- Для части операций нужны права администратора

## 🛠️ Установка

### Через pip
```bash
pip install -r requirements.txt
python setup.py install
```

### Виртуальное окружение (рекомендуется)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🔧 Конфигурация

Файлы YAML‑конфигурации находятся в `config/`:

- `default.yaml`: основная конфигурация
- переопределения через переменные окружения (`PC_CONTROL_*`)

### Пример (фрагмент)
```yaml
server:
  name: "pc-control-mcp"
  version: "2.0.0"
  log_level: "INFO"
  
security:
  enabled: true
  authentication:
    type: "none"  # none, basic, token
```

### Политики безопасности
Пример блок‑листов:
```yaml
file_operations:
  blocked_paths:
    - "/etc"
    - "C:\\Windows\\System32"
  blocked_extensions: [".exe", ".dll", ".sys"]
  
process_management:
  blocked_processes: ["systemd", "init", "kernel"]
```

## 🚀 Запуск

### Запуск сервера
```bash
python main.py
```

### Подключение MCP‑клиента (Cursor)
Транспорт stdio. Проектный `.cursor/mcp.json` уже настроен на `.venv`:

```json
{
  "mcpServers": {
    "pc-control-mcp": {
      "command": ".\\.venv\\Scripts\\python.exe",
      "args": ["-u", "main.py"],
      "env": { "PYTHONUNBUFFERED": "1" }
    }
  }
}
```

## 📚 Инструменты

### Система
- `get_system_info`, `get_hardware_info`, `get_os_info`
- `get_environment_variables`, `get_system_uptime`, `execute_command`

### Процессы
- `list_processes`, `get_process_info`, `kill_process`, `start_process`
- `suspend_process`, `resume_process`, `get_process_resources`
- `find_processes_by_name`, `set_process_priority`, `limit_process_resources`

### Файлы
- `read_file`, `write_file`, `delete_file`, `copy_file`, `move_file`
- `list_directory`, `create_directory`, `get_file_info`, `search_files`, `get_disk_usage`

## 🔒 Безопасность

### Контроль доступа
- Блок‑листы путей и процессов
- Валидация и санитизация входных данных

### Аудит‑логирование
Фиксируются: время, тип операции, пользователь/сессия, результат, ошибки.

### Рекомендации
1. Минимально необходимые привилегии
2. Строгие блок‑листы
3. Включённый аудит
4. Аутентификация в проде
5. Регулярный пересмотр логов

## 🧪 Тестирование

Запуск тестов:
```bash
pytest tests/
```

Покрытие:
```bash
pytest --cov=src tests/
```

## 📈 Производительность

- Асинхронные операции
- Эффективная работа с большими файлами
- Кэширование данных процессов
- Настраиваемые таймауты и лимиты

## 🤝 Вклад

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## 📝 Лицензия

MIT — см. `LICENSE`.

## ⚠️ Дисклеймер

Сервер предоставляет мощные операции по управлению системой. Используйте с осторожностью и только при корректно настроенной безопасности.

## 📞 Поддержка

- Issues на GitHub
- Документация — директория `docs/`

## 🔄 Изменения

### v2.0.0 (2024)
- Упрощённый запуск: один `main.py`, `run.bat`
- Совместимость с разными версиями MCP
- Улучшенное логирование и обработка ошибок

### v1.0.0
- Базовые операции управления системой
- Файловые операции
- Управление процессами