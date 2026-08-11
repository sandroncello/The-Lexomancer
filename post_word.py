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
    "false_friend": "👯 False Friend",
}


def load_json(filename: str):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(filename: str, data) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        file.write("\n")


def main() -> None:
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")

    if not webhook_url:
        raise RuntimeError("DISCORD_WEBHOOK_URL is missing.")

    entries = load_json("words.json")

    if not entries:
        raise RuntimeError("words.json contains no entries.")

    for entry in entries:
        if not entry.get("title"):
            raise RuntimeError(
                "Every entry in words.json must have a title."
            )

    try:
        used_titles = load_json("used_entries.json")
    except FileNotFoundError:
        used_titles = []

    if not isinstance(used_titles, list):
        raise RuntimeError(
            "used_entries.json must contain a JSON list."
        )

    current_titles = {
        entry["title"]
        for entry in entries
    }

    used_titles = [
        title
        for title in used_titles
        if title in current_titles
    ]

    available_entries = [
        entry
        for entry in entries
        if entry["title"] not in used_titles
    ]

    if not available_entries:
        print("All lessons have been used. Starting a new cycle.")
        used_titles = []
        available_entries = entries

    entry = random.choice(available_entries)

    entry_type = entry.get("type", "word")
    post_title = POST_TITLES.get(
        entry_type,
        "🇮🇹 Today's Italian",
    )
    lesson_title = entry["title"]

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

    examples = entry.get("examples", [])

    if examples:
        message += "\n\n**Examples**"

        for example in examples:
            label = example.get("label")
            italian = example.get("it")
            english = example.get("en")

            if not italian or not english:
                raise RuntimeError(
                    f"Invalid example in lesson: {lesson_title}"
                )

            message += "\n\n"

            if label:
                message += f"**{label}**\n"

            message += (
                f"*{italian}*\n"
                f"{english}"
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

    used_titles.append(lesson_title)
    save_json("used_entries.json", used_titles)

    print(f"Posted: {lesson_title}")
    print(
        f"Cycle progress: "
        f"{len(used_titles)}/{len(entries)} lessons used."
    )


if __name__ == "__main__":
    main()
