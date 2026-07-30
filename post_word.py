import json
import os
import random

import requests


POST_TITLES = {
    "word": "📖 Word of the Day",
    "expression": "💬 Expression of the Day",
    "grammar": "📚 Grammar Tip",
    "idiom": "🎭 Idiom of the Day",
    "mistake": "⚠️ Common Mistake",
}


def main() -> None:
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")

    if not webhook_url:
        raise RuntimeError("DISCORD_WEBHOOK_URL is missing.")

    with open("words.json", "r", encoding="utf-8") as file:
        entries = json.load(file)

    if not entries:
        raise RuntimeError("words.json contains no entries.")

    entry = random.choice(entries)

    entry_type = entry.get("type", "word")
    post_title = POST_TITLES.get(entry_type, "🇮🇹 Today's Italian")
    lesson_title = entry.get("title") or entry.get("word")

    if not lesson_title:
        raise RuntimeError("The selected entry has no title.")

    message = (
        f"## {post_title}\n\n"
        f"### **{lesson_title}**"
    )

    if entry.get("part_of_speech"):
        message += f"\n*{entry['part_of_speech']}*"

    if entry.get("definition"):
        message += (
            "\n\n"
            "**Meaning**\n"
            f"{entry['definition']}"
        )

    if entry.get("example_it") and entry.get("example_en"):
        message += (
            "\n\n"
            "**Example**\n"
            f"*{entry['example_it']}*\n"
            f"{entry['example_en']}"
        )

    if entry.get("example_di_it") and entry.get("example_di_en"):
        message += (
            "\n\n"
            "**A seconda di + noun or pronoun**\n"
            f"*{entry['example_di_it']}*\n"
            f"{entry['example_di_en']}"
        )

    if entry.get("example_che_it") and entry.get("example_che_en"):
        message += (
            "\n\n"
            "**A seconda che + subjunctive clause**\n"
            f"*{entry['example_che_it']}*\n"
            f"{entry['example_che_en']}"
        )

    if entry.get("note"):
        message += (
            "\n\n"
            "💡 **Usage note**\n"
            f"{entry['note']}"
        )

    response = requests.post(
        webhook_url,
        json={"content": message},
        timeout=20,
    )

    response.raise_for_status()
    print(f"Posted: {lesson_title}")


if __name__ == "__main__":
    main()
