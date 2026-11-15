










# AI Learning Journey

This repository contains my daily progress while learning how to build applications with Large Language Models (LLMs).

---

## Day 1 – Setting Up the API & Making My First LLM Call

### Objectives

* Set up the development environment.
* Generate a Grok API key.
* Configure the API key securely.
* Send my first request to the Grok API.
* Display the model's response.

### What I Learned

* How LLM APIs work.
* How to authenticate requests using an API key.
* How to send prompts to the model.
* How to receive and parse API responses.

### Outcome

Successfully connected to the Grok API and generated my first AI response.

---

## Day 2 – System Instructions & Temperature

### Objectives

* Understand system instructions.
* Learn how temperature affects model responses.
* Experiment with different settings.

### What I Learned

#### System Instructions

System instructions define the AI's role and behavior before it processes the user's prompt.

**Example:**

* "You are a helpful coding tutor."
* "Explain concepts in simple English."
* "Answer like a senior software engineer."

#### Temperature

Temperature controls how predictable or creative the model's responses are.

* **0.0** → Highly consistent and deterministic.
* **0.5** → Balanced creativity and consistency.
* **1.0** → More creative and varied.
* **Higher values** → More diverse but potentially less predictable.

### Outcome

Learned how system instructions shape the AI's behavior and how temperature changes the style and creativity of responses.

---

## Day 3 – Tokens

### Objectives
- Understand what tokens are.
- Learn how Large Language Models (LLMs) process and manage tokens.

### What I Learned
- LLMs do not read text character by character; they first convert text into **tokens**.
- A token can represent a whole word, part of a word, punctuation, or even spaces.
- Common words are often represented as a single token, while uncommon or complex words may be split into multiple tokens.
- The number of input and output tokens affects API usage, context length, and cost.

### Outcome
- Built a basic understanding of how tokenization works in LLMs.
- Learned why token count is important when working with AI models and APIs.

---
## Day 4 – Structured Output

### Objectives
- Understand structured output in LLMs.
- Learn why JSON is commonly used for AI responses.

### What I Learned
- LLMs can be instructed to return responses in a **structured JSON format** instead of plain text.
- Structured outputs make it easier for applications to parse and use AI responses without additional text processing.
- JSON is widely used because it is lightweight, human-readable, and supported by almost every programming language.
- Learned the basics of **Pydantic** and how it can be used to define schemas and validate structured data returned by an LLM.

### Outcome
- Gained an understanding of structured outputs and their importance in AI applications.
- Learned how Pydantic helps ensure LLM responses follow the expected JSON schema.