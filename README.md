# The Lexomancer

A lightweight, serverless Discord bot that delivers one carefully curated Italian lesson each day using GitHub Actions and Discord webhooks.

The goal is simple: make learning Italian a little easier by providing short, high-quality lessons that appear automatically, with zero infrastructure to maintain.

---

## Features

- 📖 Automatic daily Italian lessons
- 🔀 No repeated entries until every lesson has been posted
- 💬 Rich Discord formatting
- ⚡ Fully serverless using GitHub Actions
- 📝 Multiple lesson types
  - Words
  - Expressions
  - Grammar tips *(planned)*
  - Idioms *(planned)*
  - Common mistakes *(planned)*
- 🔄 Automatic reset once the lesson pool is exhausted

---

## Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── post-word.yml
├── post_word.py
├── words.json
├── used_entries.json
└── README.md
```

---

## How It Works

1. GitHub Actions triggers the workflow on a daily schedule.
2. `post_word.py` loads every lesson from `words.json`.
3. Previously posted lessons listed in `used_entries.json` are filtered out.
4. One random unused lesson is selected.
5. The lesson is formatted into a Discord message.
6. The message is sent through a Discord webhook.
7. If the post succeeds, the lesson is added to `used_entries.json`.
8. Once every lesson has been used, the history is cleared automatically and a new cycle begins.

---

## Lesson Format

Each lesson is stored as a JSON object.

Example:

```json
{
  "type": "word",
  "title": "sfrecciare",
  "part_of_speech": "intransitive verb",
  "definition": "To move or pass very quickly.",
  "example_it": "Una moto è sfrecciata davanti a noi.",
  "example_en": "A motorcycle sped past us.",
  "note": "In the passato prossimo, it normally takes essere."
}
```

Different lesson types may include additional fields (for example expressions with multiple usage patterns).

---

## Technologies

- Python 3.12
- GitHub Actions
- Discord Webhooks
- JSON

---

## Design Principles

The project intentionally keeps things simple.

- No database
- No hosted server
- No Discord bot token
- No external frameworks
- Human-readable lesson data
- Easy to extend with new lesson types

The bot is designed to be reliable, maintainable, and inexpensive to run.

---

## Roadmap

### Completed

- ✅ Automatic daily posting
- ✅ Word support
- ✅ Expression support
- ✅ Rich Discord formatting
- ✅ No-repeat cycle
- ✅ Automatic cycle reset

### Planned

- ⏳ Grammar tips
- ⏳ Idioms
- ⏳ Common mistakes
- ⏳ Retry logic for temporary webhook failures
- ⏳ Richer lesson formatting
- ⏳ Larger lesson database

---

## Contributing

Suggestions, corrections, and new lesson ideas are always welcome.

If you spot an error or have an idea for improving the project, feel free to open an issue or submit a pull request.

---

## License

MIT
