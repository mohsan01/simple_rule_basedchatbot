# Simple Rule-Based Chatbot

## Project Description

This project is a simple rule-based chatbot developed in Python. It responds to predefined user inputs using `if-elif-else` decision-making logic.

## Key Requirements

- Handle greetings such as `hello`, `hi`, and `hey`
- Handle exit commands such as `bye`, `exit`, and `quit`
- Use `if-elif-else` logic for responses
- Run continuously using a `while` loop
- Provide a default response for unknown inputs

## Key Skills

- Python basics
- Control flow
- Decision-making logic
- `if-elif-else`
- `while` loop
- User input handling
- Basic AI / rule-based chatbot concepts

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check it with:

```bash
python --version
```

### 2. Run the chatbot

Open a terminal in the project folder and run:

```bash
python chatbot.py
```

## Example

```text
Chatbot: Hello! I am a simple chatbot.
Chatbot: You can say hello, how are you, what is your name, or bye.

You: hello
Chatbot: Hello! Nice to meet you.

You: how are you
Chatbot: I'm doing great! Thanks for asking.

You: what is your name
Chatbot: My name is SimpleBot.

You: bye
Chatbot: Goodbye! Have a nice day.
```

## How It Works

The chatbot continuously takes input from the user using `input()`.

- If the input is a greeting, it gives a greeting response.
- If the input is `how are you`, it gives a predefined response.
- If the input asks for its name, it gives its name.
- If the input is `bye`, `exit`, or `quit`, the chatbot stops.
- For any other input, it displays an unknown-input response.

## Basic AI Concept

This is a **rule-based chatbot**. It does not learn from conversations. Instead, it compares user input with predefined rules and returns the response associated with the matching rule.

## Files

- `chatbot.py` — Python source code
- `README.md` — Project documentation
