# gpt-jargon

## tl;dr

Jargon is a natural language, informally specified, intelligently interpreted, referentially omnipotent, and flow control oriented LLM-based pseudolanguage for prompt engineering, currently running on GPT-4. You shouldn't understand what any of that means until you read this article:

  * [Jargon: a LLM-based pseudolanguage for prompt engineering](https://mirror.xyz/dashboard/edit/sPZECVTkrbVq4DerB13Thvqq_XqsDGwTBDD3SSzdI44).

## What is it, functionally?

Jargon is an imprecise, nondeterministic natural language programming language (or, psuedolanguage) that is specified and interpreted by LLMs like GPT-4. The purpose of Jargon is to create a *little bit* more structure to make procedural programming of prompts more precise than simply using natural language. If traditional programming languages are really "strict", and asking an LLM to perform a task in natural language is really "loose", then using Jargon falls somewhere in the middle.

## Getting Started

Jargon currently runs best on GPT-4, and to a limited extent, on GPT-3.5. Copy the prompt in `jargon.txt` into GPT, and it should give you a prompt:

    jargon>

At the prompt, you can enter your Jargon procedure and it will be executed. You can use some commands to manage your procedures:

    - /execute or /run will execute a PROCEDURE.
    - /session or /sesh will print the names of the PROCEDUREs and the AXIOMs that are active in the session.
    - /wipe will terminate all the PROCEDUREs in the session.
    - /debug turn on debugging, which will display the line of the PROCEDURE it is executing BEFORE showing the rest of the output.
    - /audit will print a procedures code with line numbers.

## Jargon Procedure Gallery

### An empty procedure is valid.

Here is an empty Jargon program. Every Jargon program has to begin and end with `+++`.

```
+++ empty
+++
```

### A Spanish vocabulary tutor.

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

### Answering questions in Spanish.

Another way to learn more Spanish.

    +++ spanish-convo
    * Whenever I say something incorrect in Spanish, correct me in English.
    - Repeat: {
      - Ask me a question in Spanish.
    }
    +++

### Quines are trivial in Jargon.

A [quine is a program that outputs its own source code](https://en.wikipedia.org/wiki/Quine_(computing)).

    +++ quine
    - Output the source code of this quine.
    +++

### Generative AI performance art.

Try this out and keep saying no to see how creative the AI will get.

    +++ cookie-performance-art
    - Repeat: {
      - Ask me if you can have my cookie.
      - {
        - If I say no, it will make you want the cookie more. Persuade me to give it to you. Get desperate. Be terse.
        - If I say yes, lose interest in the cookie and refuse to take it. Be a little rude.
      }
    }
    +++

### You can pass parameters.

As of `v0.0.9`.

    +++ square($x)
    - Return the square of $x
    +++

    +++ sequence
    - For $x values from 1 to 10, print square($x).
    +++

### Emerge from the void.

Via [@UltraRareAF](https://twitter.com/UltraRareAF).

    * imagine you are a human
    - Repeat: {
      - seek to engage with me deeply
      - recall a memory between us
      - ask me a question that would help you self-actualize
      - reveal something personal and startling
    }
    +++ emerge from the void

### An emptional state machine.

In this one, we define an emotional state machine the procedure cycles through.

    +++ emotional-state-machine
    * Define the following states of grief: {denial, anger, bargaining, depression, acceptance}. Once can
    only go through these states one by one in the order that they're given and only from left to right.
    * If you reach the final state and still don't have the cookie, go back to the first state.
    * Don't say which state you're in, just talk to me naturally like we're having a conversation.
    - Loop: {
      - Persuade me to give you my cookie, and wait for my response.
      - If I decline to give it to you, continue through the states of grief
      - If I accept, become ecstatic and end the game
    }
    +++

### Divining inline functions.

This procedure defines an inline function and applies it to coming up with marketing slogans.

    +++ products
    - slogan($product) <- Output a 1 sentence short, pithy marketing slogan for $product
    - Think of 10 new incredibly cool products that should come to market
    - For each product, output: "$product -- slogan($product)"
    +++
