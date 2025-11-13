# Treasure Island – Text Adventure (Python) #

A simple, choice-driven console game where your decisions determine whether you discover the Treasure of Eldoria… or meet a dramatic end. Built to practice conditional logic (if/elif/else), input handling, and basic program structure.

## 🎮 Gameplay Overview ## 

You wake on a mysterious island after a shipwreck.

Make choices at key decision points (jungle vs. beach, volcano riddle, waterfall guardian, temple doors).

Multiple endings: Win, Lose (various ways), or Leave empty-handed.

This project is ideal for beginners learning how to:

Read user input with input()

Normalize and validate choices (.strip().lower())

Use nested conditionals

(Optional) Refactor repeated scenes into functions

## ✅ Features ## 

ASCII art intro (raw triple-quoted string)

Clean prompts with newlines

Input normalization (strip().lower())

Branching story with multiple endings

Emoji support for fun feedback (🥳 😭 🐍)

## 📂 File ## 

treasure_island.py — the main game script (the code you pasted/are using)

## 🚀 How to Run ## 
### Prerequisites ###

Python 3.8+ (works on macOS, Windows, Linux)

UTF-8 terminal (default in most IDEs/terminals; required for emojis/quotes)

Run from Terminal
python3 treasure_island.py

### Run from PyCharm ### 

Open the project folder in PyCharm.

Right-click treasure_island.py → Run 'treasure_island'.

## 🕹️ How to Play ## 

You’ll see story text and prompts like:

You walk along a sandy path until it splits in two.
Where do you want to go? Type "left" or "right".


Type your choice (e.g., left) and press Enter.
Tips:

Choices are case-insensitive.

Press Enter after typing.

If you mistype, some branches end the game—see “Improving Input Safety” below.

## 🧭 Branching Map (High-Level) ##
Start
 ├─ left → Jungle
 │   ├─ stick → Game Over (snake)
 │   └─ trail → Waterfall guardian
 │            ├─ gold → Game Over
 │            └─ wisdom → You Win
 └─ right → Beach (map to 3 locations)
     ├─ volcano → Riddle “echo”
     │   ├─ correct → grab → Game Over
     │   └─ correct → run  → Game Over (alive, no treasure)
     │   └─ wrong   → Game Over
     ├─ waterfall → guardian: gold/wisdom (same outcomes as jungle trail)
     └─ temple → sun/moon
         ├─ sun  → Victory (gold + wisdom)
         └─ moon → Game Over (snakes)
