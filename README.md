
## God Words Generator

A minimal command-line random word generator written in **Python.**
The script outputs **randomly selected words** from a predefined list, one at a time, triggered by user input.

This project is inspired by the Random Word Generator demonstrations by **Terry A. Davis** in **TempleOS.**


## ✨ Features


* **Random word selection** without repetition

* **Manual, step-by-step generation** (press `Enter` to draw)

* **Immediate terminal output** (no buffering delays)

* **Graceful handling of** `Ctrl+C`

* **Deterministic ending** once all words are exhausted

* **Minimal dependencies** (Python standard library only)



## ⚙️ How It Works



* A list of predefined words is loaded into memory.

* A copy of this list is used as the **available word pool.**

* The program waits for the user to press **Enter.**

* One word is randomly selected and removed from the pool.

* The word is printed immediately.

* Steps 3–5 repeat until the pool is empty or the program is interrupted.

* Low-level terminal input handling (`termios`, `tty`) is used so input is read **character-by-character** while still allowing `Ctrl+C` to function normally.

## 🧩 Requirements

* **Python 3.7+**

* **Unix-like operating system** (Linux, macOS)

⚠️ Note:
This script will not work on Windows without modification due to the use of termios and tty.

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/god-words-generator.git
cd god-words-generator
```
No additional dependencies are required.

## ▶️ Usage

Run the script from the command line:

```bash
python3 god_words_generator.py
```

## 🎮 Controls
Key	Action
Enter	Draw next random word
Ctrl+C	Interrupt and exit


## 🖥️ Example Output

```vbnet
Press Enter to draw next word. Ctrl+C to stop.
Drawn words: God, computer, CIA, flower, strawberry,
```


## 🗂️ File Overview

```bash
.
├── god_words_generator.py   # Main script
└── README.md                # Project documentation
```

## 🔧 Customization

You can modify the word pool by editing the `words` **list** inside `god_words_generator.py`.

Example:

```python
words = [
    "word1",
    "word2",
    "word3",
]
```
## 📄 License

This project is provided **as-is**, without warranty.
Choose any license you prefer (**MIT, Unlicense,** etc.).

## 🕊️ Dedication

This project is created in memory of **Terry A. Davis (1969–2018)**
— programmer, creator of TempleOS, and one of the most unusual and uncompromising minds in computing.

*Rest in peace, Terry.*

