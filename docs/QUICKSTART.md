# Как пользоваться Cortex CLI

## Установка

```bash
cd "C:\Users\tw1nz\Documents\AI CLI"
venv\Scripts\activate
pip install -e .
```

Или используй уже готовое окружение:
```bash
venv\Scripts\activate
```

## Быстрый старт

### 1. Настройка ключей

**Вариант A** — через переменные окружения:
```bash
set OPENAI_API_KEY="sk-..."
set GEMINI_API_KEY="AIza..."
set GROQ_API_KEY="gsk_..."
```

**Вариант B** — через config файл:
```bash
python -c "from ai_cli.config import set_api_key; set_api_key('openai', 'sk-...')"
```

### 2. Основные команды

```bash
# Статус — показывает версию, провайдер, модели
cortex status

# Список моделей
cortex models

# Одно сообщение
cortex chat --message "Привет, как дела?"

# Чат с конкретной моделью
cortex chat --model gpt-4 --message "Объясни рекурсию"

# Интерактивный чат
cortex chat
# Пиши сообщения, exit — выход

# История
cortex history
cortex history --limit 20
```

### 3. Смена провайдера

```bash
# OpenAI (по умолчанию)
set CORTEX_PROVIDER=openai

# Gemini
set CORTEX_PROVIDER=gemini
cortex chat --message "Эй, Gemini!"

# Groq
set CORTEX_PROVIDER=groq
cortex chat --message "Привет, Groq!"

# Mercury
set CORTEX_PROVIDER=mercury

# Локальная модель (Ollama)
set CORTEX_PROVIDER=local
set CORTEX_BASE_URL=http://localhost:11434
```

## Провайдеры

| Провайдер | Ключ | Команда |
|-----------|------|---------|
| OpenAI | `OPENAI_API_KEY` | По умолчанию |
| Anthropic | `ANTHROPIC_API_KEY` | `set CORTEX_PROVIDER=anthropic` |
| Gemini | `GEMINI_API_KEY` | `set CORTEX_PROVIDER=gemini` |
| Groq | `GROQ_API_KEY` | `set CORTEX_PROVIDER=groq` |
| Mercury | `MERCURY_API_KEY` | `set CORTEX_PROVIDER=mercury` |
| Local | `CORTEX_BASE_URL` | `set CORTEX_PROVIDER=local` |

## Примеры

```bash
# Простой вопрос
cortex chat --message "Что такое Python?"

# Системное сообщение через env
set CORTEX_MODEL=gemini-1.5-flash
cortex chat --message "Привет!"

# Смотреть что доступно
cortex models
cortex status

# История переписки
cortex history --limit 50
```

## Тесты

```bash
venv\Scripts\pytest -v
```

## Справка

```bash
cortex --help
cortex chat --help
cortex models --help
cortex status --help
cortex history --help
```
