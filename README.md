# gpt-jargon

## What is it?

Jargon is a natural language programming language (or, psuedolanguage) that is specified and interpreted by LLMs like GPT-4. The purpose of Jargon is to create a *little bit* more structure to make procedural programming of LLMs  more precise than simply using natural language. If traditional programming languages are really strict, and naturally asking an LLM to perform a task in natural language is really "loose", then using Jargon falls somewhere in the middle.

## Examples of Jargon

Here is an empty Jargon program. Every Jargon program has to begin and end with `+++`.

```
+++
+++
```

Jargon programs can be specified in natural language and execute instructions procedurally.

```
+++
- Think of a random number between 1 and 10.
- Take this number and multiply it by 2.
- Output the result.
+++
```

Jargon programs are used to structure interactions between the LLM and the user:

```
+++
* For any input that I enter in Spanish, check my input for grammatical correctness.
* Every 5 words, ask me if we should adjust the difficulty level.
- Repeat in perpetuity: {
  - Tell me a word in Spanish and ask me to define it. {
    - If my definition is correct, tell me so and increase my score by 1 point.
    - If my definition is incorrect, tell me the correct definition. Encourage me to do better next time.
  }
  - Tell me my score.
}
+++
```
