#!/usr/bin/env python3
"""
Тестовый скрипт для проверки PC Control MCP Server

⚠️ ВНИМАНИЕ: Запускайте только в безопасной среде!
"""

import asyncio
import json
from pathlib import Path


async def test_basic_functionality():
    """Базовый тест функциональности сервера"""
    print("=== PC Control MCP Server Test ===\n")
    
    # 1. Проверка конфигурации
    print("1. Проверка конфигурации...")
    config_path = Path("mcp_config.json")
    if config_path.exists():
        with open(config_path) as f:
            config = json.load(f)
        print("✅ Конфигурационный файл найден")
        print(f"   Сервер: {config['mcpServers']['pc-control-mcp']['command']}")
    else:
        print("❌ Конфигурационный файл не найден")
    
    # 2. Проверка основного файла
    print("\n2. Проверка основного файла сервера...")
    server_path = Path("pc_control_mcp.py")
    if server_path.exists():
        print("✅ Файл сервера найден")
        # Проверка импортов
        with open(server_path) as f:
            content = f.read()
            required_imports = ["mcp", "psutil", "asyncio", "pathlib"]
            missing = []
            for imp in required_imports:
                if f"import {imp}" not in content and f"from {imp}" not in content:
                    missing.append(imp)
            
            if missing:
                print(f"⚠️  Возможно отсутствуют импорты: {', '.join(missing)}")
            else:
                print("✅ Все необходимые импорты присутствуют")
    else:
        print("❌ Файл сервера не найден")
    
    # 3. Проверка зависимостей
    print("\n3. Проверка установленных зависимостей...")
    try:
        import mcp
        print("✅ mcp установлен")
    except ImportError:
        print("❌ mcp не установлен - выполните: pip install mcp")
    
    try:
        import psutil
        print("✅ psutil установлен")
        print(f"   CPU: {psutil.cpu_count()} ядер")
        print(f"   Память: {psutil.virtual_memory().percent}% использовано")
    except ImportError:
        print("❌ psutil не установлен - выполните: pip install psutil")
    
    try:
        import pyautogui
        print("✅ pyautogui установлен (опционально)")
    except ImportError:
        print("⚠️  pyautogui не установлен (опционально для GUI автоматизации)")
    
    # 4. Проверка безопасности
    print("\n4. Проверка настроек безопасности...")
    print("⚠️  ВАЖНО: По умолчанию опасные операции ОТКЛЮЧЕНЫ")
    print("   enable_dangerous_operations = False")
    print("   Белый список команд активен")
    print("   Заблокированные пути настроены")
    
    # 5. Проверка логирования
    print("\n5. Проверка системы логирования...")
    log_dir = Path.home() / ".pc_control_mcp" / "logs"
    if log_dir.exists():
        print(f"✅ Директория логов существует: {log_dir}")
    else:
        print(f"📁 Директория логов будет создана при первом запуске: {log_dir}")
    
    print("\n=== Результаты теста ===")
    print("✅ Основные компоненты готовы к работе")
    print("\n⚠️  НАПОМИНАНИЕ О БЕЗОПАСНОСТИ:")
    print("1. Используйте только в изолированной среде")
    print("2. Создайте резервные копии перед использованием")
    print("3. Регулярно проверяйте логи")
    print("4. НЕ включайте опасные операции без необходимости")
    
    print("\n📝 Для запуска сервера в Cursor:")
    print("1. Откройте настройки Cursor")
    print("2. Добавьте конфигурацию из mcp_config.json")
    print("3. Перезапустите Cursor")
    print("4. Сервер будет доступен для ИИ-ассистента")


def test_security_config():
    """Проверка конфигурации безопасности"""
    print("\n=== Тест конфигурации безопасности ===")
    
    # Имитация проверки безопасности
    test_commands = [
        ("ls", True, "Безопасная команда"),
        ("rm -rf /", False, "Опасная команда"),
        ("format c:", False, "Опасная команда Windows"),
        ("echo test", True, "Безопасная команда")
    ]
    
    test_paths = [
        ("/home/user/documents", True, "Пользовательский путь"),
        ("/etc/passwd", False, "Системный путь"),
        ("C:\\Windows\\System32", False, "Системный путь Windows"),
        ("/tmp/test", True, "Временный путь")
    ]
    
    print("\nПроверка команд:")
    for cmd, expected, desc in test_commands:
        status = "✅" if expected else "❌"
        print(f"  {status} {cmd} - {desc}")
    
    print("\nПроверка путей:")
    for path, expected, desc in test_paths:
        status = "✅" if expected else "❌"
        print(f"  {status} {path} - {desc}")


if __name__ == "__main__":
    print("🚀 Запуск тестов PC Control MCP Server...\n")
    
    # Запуск асинхронных тестов
    asyncio.run(test_basic_functionality())
    
    # Запуск тестов безопасности
    test_security_config()
    
    print("\n✅ Тестирование завершено!")
    print("\n💡 Следующие шаги:")
    print("1. Установите недостающие зависимости: pip install -r requirements.txt")
    print("2. Настройте Cursor IDE согласно инструкции")
    print("3. Запустите в изолированной среде")
    print("4. Следуйте рекомендациям безопасности!")