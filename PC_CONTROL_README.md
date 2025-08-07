# PC Control MCP Server - Полный контроль над компьютером через Cursor IDE

## ⚠️ КРИТИЧЕСКОЕ ПРЕДУПРЕЖДЕНИЕ БЕЗОПАСНОСТИ ⚠️

**ЭТОТ СЕРВЕР ПРЕДОСТАВЛЯЕТ ПОЛНЫЙ ДОСТУП К ВАШЕЙ СИСТЕМЕ!**

- 🔴 **НИКОГДА** не используйте на продакшн-системах
- 🔴 **ВСЕГДА** используйте в изолированной среде (VM, Docker)
- 🔴 **ОБЯЗАТЕЛЬНО** создайте полные резервные копии перед использованием
- 🔴 **РЕГУЛЯРНО** проверяйте логи всех операций

## Описание

PC Control MCP Server - это мощный MCP-сервер, который предоставляет ИИ-ассистенту в Cursor IDE возможность полного управления компьютером. Сервер позволяет выполнять системные команды, управлять файлами, процессами, службами, сетью и многим другим.

## Возможности

### 🖥️ Системное управление
- **execute_command** - Выполнение любых системных команд
- **system_info** - Получение информации о CPU, памяти, дисках, сети
- **process_management** - Управление процессами (список, завершение, информация)
- **service_management** - Управление системными службами

### 📁 Файловые операции
- **file_operations** - Чтение, запись, удаление, копирование файлов
- **backup_operations** - Создание и восстановление резервных копий

### 🌐 Сетевые функции
- **network_operations** - Ping, сканирование портов, DNS lookup
- Просмотр активных соединений

### ⚙️ Системная конфигурация
- **registry_operations** (Windows) - Работа с реестром
- **environment_management** - Управление переменными окружения
- **scheduled_tasks** - Создание запланированных задач

### 🤖 Автоматизация
- **automation_tools** - GUI автоматизация (движение мыши, клики, ввод текста)
- Создание скриншотов

## Установка

### 1. Требования

- Python 3.8 или выше
- Cursor IDE с поддержкой MCP
- Операционная система: Windows, Linux или macOS

### 2. Клонирование репозитория

```bash
git clone https://github.com/your-repo/pc-control-mcp.git
cd pc-control-mcp
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

Необходимые зависимости:
- `mcp` - MCP SDK
- `psutil` - Системный мониторинг
- `pyautogui` - GUI автоматизация (опционально)

### 4. Настройка в Cursor IDE

1. Откройте настройки Cursor (Ctrl+,)
2. Найдите раздел "MCP Servers"
3. Добавьте новый сервер:

```json
{
  "pc-control-mcp": {
    "command": "python",
    "args": ["путь/к/pc_control_mcp.py"],
    "env": {
      "PYTHONPATH": "путь/к/директории"
    }
  }
}
```

Или используйте готовый `mcp_config.json` из репозитория.

## Безопасная конфигурация

По умолчанию сервер работает в безопасном режиме. Для включения опасных операций отредактируйте `SECURITY_CONFIG` в `pc_control_mcp.py`:

```python
SECURITY_CONFIG = {
    "allowed_commands": ["ls", "dir", "echo", "cat"],  # Белый список команд
    "blocked_paths": ["/", "C:\\Windows"],  # Заблокированные пути
    "max_file_size": 100 * 1024 * 1024,  # Максимальный размер файла
    "command_timeout": 30,  # Таймаут команд
    "enable_dangerous_operations": False  # НЕ ВКЛЮЧАЙТЕ без необходимости!
}
```

## Примеры использования

### Пример 1: Создание файла

```python
# ИИ-ассистент может использовать:
tool: file_operations
parameters: {
  "operation": "write",
  "path": "/home/user/test.txt",
  "content": "Hello, World!"
}
```

### Пример 2: Мониторинг системы

```python
# Получить информацию о CPU
tool: system_info
parameters: {
  "info_type": "cpu"
}

# Список процессов
tool: process_management
parameters: {
  "action": "list"
}
```

### Пример 3: Сетевая диагностика

```python
# Пинг сервера
tool: network_operations
parameters: {
  "operation": "ping",
  "target": "google.com",
  "count": 4
}
```

## Логирование

Все операции логируются в:
- Linux/macOS: `~/.pc_control_mcp/logs/`
- Windows: `%USERPROFILE%\.pc_control_mcp\logs\`

Формат лога:
```
2024-01-15 10:30:45 - pc_control_mcp - INFO - Operation logged: execute_command
```

## Архитектура

```
pc_control_mcp.py
├── PCControlMCP (основной класс)
│   ├── SecurityManager (управление безопасностью)
│   └── Инструменты (tools)
│       ├── execute_command
│       ├── file_operations
│       ├── system_info
│       ├── process_management
│       ├── network_operations
│       ├── registry_operations
│       ├── service_management
│       ├── environment_management
│       ├── scheduled_tasks
│       ├── backup_operations
│       └── automation_tools
```

## Рекомендации по безопасности

### ✅ ДЕЛАЙТЕ:
1. Используйте в виртуальной машине
2. Создавайте резервные копии
3. Проверяйте логи операций
4. Ограничивайте доступные команды
5. Используйте белые списки путей

### ❌ НЕ ДЕЛАЙТЕ:
1. Не запускайте на основной системе
2. Не включайте `enable_dangerous_operations` без крайней необходимости
3. Не давайте доступ к критическим системным файлам
4. Не используйте с важными данными

## Устранение неполадок

### Проблема: Сервер не запускается
```bash
# Проверьте установку зависимостей
pip install -r requirements.txt

# Проверьте версию Python
python --version
```

### Проблема: Команды блокируются
- Проверьте `SECURITY_CONFIG`
- Убедитесь, что команда в белом списке
- Проверьте логи для деталей

### Проблема: Нет доступа к файлам
- Проверьте права доступа
- Убедитесь, что путь не в `blocked_paths`

## Поддержка платформ

| Функция | Windows | Linux | macOS |
|---------|---------|--------|--------|
| execute_command | ✅ PowerShell | ✅ Bash | ✅ Bash |
| file_operations | ✅ | ✅ | ✅ |
| system_info | ✅ | ✅ | ✅ |
| process_management | ✅ | ✅ | ✅ |
| network_operations | ✅ | ✅ | ✅ |
| registry_operations | ✅ | ❌ | ❌ |
| service_management | ✅ | ✅ systemd | ✅ launchd |
| scheduled_tasks | ✅ schtasks | ✅ cron | ✅ cron |

## Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для функции (`git checkout -b feature/NewFeature`)
3. Commit изменения (`git commit -m 'Add NewFeature'`)
4. Push в ветку (`git push origin feature/NewFeature`)
5. Создайте Pull Request

## Лицензия

Этот проект распространяется под лицензией MIT. См. файл `LICENSE` для деталей.

## Отказ от ответственности

Этот инструмент предоставляется "как есть" без каких-либо гарантий. Авторы не несут ответственности за любой ущерб, причиненный использованием этого программного обеспечения. Используйте на свой страх и риск!

## Контакты

- Создатель: [Ваше имя]
- Email: [Ваш email]
- GitHub: [Ваш GitHub]

---

**Помните: с большой силой приходит большая ответственность. Используйте этот инструмент мудро!**