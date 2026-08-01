# 📚 The Lexomancer

**The Lexomancer** is an open-source Discord bot that automatically posts daily Italian language lessons using GitHub Actions and Discord webhooks.

Its goal is simple: help learners improve their Italian one lesson at a time through vocabulary, expressions, grammar, idioms, and common language mistakes.

---

## ✨ Features

- 📖 Word of the Day
- 💬 Expression of the Day
- 🎲 Random lesson selection
- 🚫 No repeated lessons until every lesson has been posted
- 🔄 Automatic reset when the lesson database is exhausted
- ⚡ Fully serverless using GitHub Actions
- 📚 Grammar Tips *(planned)*
- 🎭 Idioms *(planned)*
- ⚠️ Common Mistakes *(planned)*

Each lesson includes:

- 🇮🇹 Italian word or expression
- 🇬🇧 English translation
- 📝 Explanation
- 💡 Example sentence(s)
- 📌 Usage notes where appropriate

---

## ⚙️ How It Works

Every day, GitHub Actions automatically runs a Python script that:

1. Loads every lesson from `words.json`.
2. Reads `used_entries.json` to determine which lessons have already been posted.
3. Randomly selects one unused lesson.
4. Formats it into a Discord-friendly message.
5. Sends it through a Discord webhook.
6. Records the lesson in `used_entries.json`.

Once every lesson has been used, the history is automatically cleared and a new random cycle begins.

No VPS, server, or always-on computer is required.

---

## 📁 Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── post-word.yml
├── post_word.py
├── words.json
├── used_entries.json
├── LICENSE
└── README.md
```

---

## 🚀 Setup

1. Fork or clone this repository.
2. Create a Discord webhook in your server.
3. Add the webhook URL as a GitHub Actions secret named:

```text
DISCORD_WEBHOOK_URL
```

4. Enable GitHub Actions.
5. Run the workflow manually or wait for the scheduled run.

---

## 🛠️ Built With

- Python 3.12
- GitHub Actions
- Discord Webhooks

---

## 🗺️ Roadmap

### ✅ Completed

- [x] Daily vocabulary
- [x] Daily expressions
- [x] Random lesson selection
- [x] Prevent repeated lessons
- [x] Automatic reset once all lessons have been used
- [x] Rich Discord formatting

### 🚧 Planned

- [ ] Grammar lessons
- [ ] Idioms
- [ ] Common mistakes
- [ ] Retry logic for temporary Discord failures
- [ ] Expand the lesson database

---

## 🤝 Contributing

Suggestions, corrections, and pull requests are always welcome.

Whether you want to expand the lesson database, improve formatting, or add new features, contributions are appreciated.

---

## 📄 License

This project is licensed under the MIT License.

---

## ❤️ Acknowledgements

Built by **sandroncello**.

Special thanks to **ChatGPT**, who contributed to the design, implementation, debugging, and countless rounds of troubleshooting throughout the project.

Debugged through equal parts determination, GitHub Mobile suffering, and distributed systems deciding to wake up eventually.
