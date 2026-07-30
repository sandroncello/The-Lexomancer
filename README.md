# 📚 The Lexomancer

**The Lexomancer** is an open-source Discord bot that automatically posts daily Italian language lessons using GitHub Actions and Discord webhooks.

Its goal is simple: help learners improve their Italian one lesson at a time through vocabulary, expressions, grammar, idioms, and common language mistakes.

---

## ✨ Features

- 📖 Word of the Day
- 💬 Expression of the Day
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

1. Loads a random lesson from `words.json`
2. Formats it into a Discord-friendly message
3. Sends it through a Discord webhook

No VPS, server, or always-on computer is required.

---

## 📁 Project Structure

```
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

```
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

- [x] Daily vocabulary
- [x] Daily expressions
- [ ] Grammar lessons
- [ ] Idioms
- [ ] Common mistakes
- [ ] Prevent repeated lessons
- [ ] Automatically reset once all lessons have been used
- [ ] Richer Discord formatting

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

Debugged through equal parts determination, GitHub Mobile suffering, and ChatGPT.
