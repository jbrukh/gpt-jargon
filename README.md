# gpt-jargon

## tl;dr

Jargon is a natural language, informally specified, intelligently interpreted, referentially omnipotent, and flow control oriented LLM-based pseudolanguage for prompt engineering, currently running on GPT-4. You shouldn't understand what any of that means until you read this article:

  * [Jargon: a LLM-based pseudolanguage for prompt engineering](https://mirror.xyz/dashboard/edit/sPZECVTkrbVq4DerB13Thvqq_XqsDGwTBDD3SSzdI44).

## What is it, functionally?

Jargon is an imprecise, nondeterministic natural language programming language (or, psuedolanguage) that is specified and interpreted by LLMs like GPT-4. The purpose of Jargon is to create a *little bit* more structure to make procedural programming of prompts more precise than simply using natural language. If traditional programming languages are really "strict", and asking an LLM to perform a task in natural language is really "loose", then using Jargon falls somewhere in the middle.

### Properties of Jargon

**Informal Specification**. Some of the features of Jargon are not specified in the Jargon definition. Instead, they are simply _divined_ of the general knowledge that the LLM has about programming languages. For example, Jargon does not specify variables at all, yet the following code still works:

    +++ vars
    -- $x = 5
    -- Print "there were $x bananas"
    +++

**Natural Language Instructions**. In Jargon, you can simply tell it what to do in natural language. This works even though the natural language is not particularly precise:

    +++ sum($x, $y)
    -- Sum them
    +++
    
**Referential Omnipotence**. The scope of data accessible to a Jargon program is the entire chat session, including the code of the interpreter and the Jargon procedure you are running, as well as all the LLM's knowledge about the world. That makes extremely omnipotent instructions possible:

    +++ proc1
    -- Return five random emojis
    +++
    
    +++ proc2
    -- Modify proc1 to return random numbers instead
    -- Let $n <- the number of countries in Latin America
    -- Instead of five, use $n
    -- /execute proc1
    +++
    
    /proc2

## What can Jargon be used for?

- [Benchmarking an LLM](https://twitter.com/jbrukh/status/1640444880689176576?s=20)
- Programming bots that, including some that [teach you Spanish](https://twitter.com/jbrukh/status/1640444883654549507?s=20)
- Psuedocode transpilation: [turn your pseudocode into actual code](https://twitter.com/jbrukh/status/1640444882106867712?s=20)

## Getting Started

Jargon currently runs best on GPT-4, and to a limited extent, on GPT-3.5. Copy the prompt in `jargon.txt` into GPT, and it should give you a prompt:

    jargon>

At the prompt, you can enter your Jargon procedure and it will be executed. You can use some commands to manage your procedures:

    - /execute or /run will execute a PROCEDURE.
    - /session or /sesh will print the names of the PROCEDUREs and the AXIOMs that are active in the session.
    - /wipe will terminate all the PROCEDUREs in the session.
    - /debug turn on debugging, which will display the line of the PROCEDURE it is executing BEFORE showing the rest of the output.
    - /audit will print a procedures code with line numbers.
    
## Unit Testing

You can run unit tests on Jargon by using the Jargon procedure specified in `tests.txt`. Running tests should make Jargon work better. There is also some more info about running unit tests [in this article](https://jake.mirror.xyz/6j-KetfRE4kQRyI2-Xf2JsP4UL-DPKi20WhOVbWT2dE).

## Related Projects

* [Jargon-Nock](https://github.com/tacryt-socryp/jargon-nock/) implements Urbits Nock as a GPT prompt.
* [PromptLang](https://github.com/ruvnet/promptlang) is a custom programming language specifically designed for use in GPT-4 prompts. 
* [PML](https://github.com/dineshraju/pml) is a markup pseudolanguage that's used in LLM prompt engineering to generate long-form content.

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

### A good example of axioms.

Jargon 0.0.10 wrote this nice idiomatic example of how to use axioms.

    +++ precise-math
    * When performing arithmetic operations, round to two decimal places
    - Calculate 3.14159 * 2
    +++

### THe joke game.

Credit goes to Jar(gon)vis 0.1 via @fractastical 

    +++ joke-game
    - Tell a joke and store it as myJoke
    - Ask the user to tell a joke and store it as userJoke
    - Ask the user: "Which joke is funnier? Type 'mine' for your joke or 'yours' for my joke."
    - {
        - If the user answers 'mine', say "Congratulations! You have a great sense of humor!"
        - If the user answers 'yours', say "Thank you! I'm glad you enjoyed my joke!"
        - If the user answers anything else, say "Please type 'mine' or 'yours' to choose the funnier joke."
    }
    +++

## MIT License

Copyright (c) 2023. Jake Brukhman.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
