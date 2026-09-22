# Cortex

Manage AI in your terminal. [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)

Просто пиши API или подключай локальную нейронку — всё остальное сделаем за тебя.

## Возможности

- 🧠 **Мульти-провайдер** — OpenAI, Anthropic, Gemini, Groq, Mercury, локальные модели
- 🎨 **Красивый интерфейс** — цвета, тема, спиннеры
- 📜 **История диалогов** — сохраняется автоматически
- 🔄 **Горячая смена моделей** — без перезапуска

## Установка

```bash
pip install -e .
```

## Быстрый старт

```bash
# Настроить ключи
export OPENAI_API_KEY="sk-..."

# Начать чат
cortex chat

# Или одиночное сообщение
cortex chat --message "Привет, как дела?"

# Выбрать провайдер
CORTEX_PROVIDER=gemini cortex chat --message "Привет"

# Показать статус
cortex status

# Показать модели
cortex models

# История
cortex history
```

## Провайдеры

| Провайдер | Переменная | По умолчанию |
|-----------|-----------|--------------|
| OpenAI | `OPENAI_API_KEY` | gpt-4 |
| Anthropic | `ANTHROPIC_API_KEY` | claude-3-opus |
| Gemini | `GEMINI_API_KEY` | gemini-1.5-pro |
| Groq | `GROQ_API_KEY` | llama-3.3-70b-versatile |
| Mercury | `MERCURY_API_KEY` | mercury-standard |
| Local | `CORTEX_BASE_URL` | localhost:11434 |
