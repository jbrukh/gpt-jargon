# gpt-jargon

## tl;dr

Jargon is a natural language, informally specified, intelligently interpreted, referentially omnipotent, and flow control oriented LLM-based pseudolanguage for prompt engineering, currently running on GPT-4. See the original articles on Jargon here:

  * [Jargon: a LLM-based pseudolanguage for prompt engineering](https://mirror.xyz/dashboard/edit/sPZECVTkrbVq4DerB13Thvqq_XqsDGwTBDD3SSzdI44).
  * [New features in Jargon v0.0.12](https://jake.mirror.xyz/6j-KetfRE4kQRyI2-Xf2JsP4UL-DPKi20WhOVbWT2dE)
  * [Using Jargon CLI in Jargon v0.2.0](https://jake.mirror.xyz/y_bo5z1toEhC8G8aK1wpQzU6Tign7_s_Upsm12ietRc)

As of this release, Jargon comes with `jargon_cli`, a commandline shell for playing with Jargon programs that works with OpenAI.

## What is it, functionally?

Jargon is an imprecise, nondeterministic natural language programming language (or, psuedolanguage) that is specified and interpreted by LLMs like GPT-4. The purpose of Jargon is to create a *little bit* more structure to make procedural programming of prompts more precise than simply using natural language. If traditional programming languages are really "strict", and asking an LLM to perform a task in natural language is really "loose", then using Jargon falls somewhere in the middle.

### Properties of Jargon

**Informal Specification**. Some of the features of Jargon are not specified in the Jargon definition. Instead, they are simply _divined_ of the general knowledge that the LLM has about programming languages. For example, Jargon does not specify variables at all, yet the following code still works:

    +++ vars
    -- Set $x = 5
    /output "there were $x bananas"
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
    -- Let $n = [the number of countries in Latin America]
    -- Instead of five, use $n
    /execute proc1
    +++
    
    /proc2

### What can Jargon be used for?

- [Benchmarking an LLM](https://twitter.com/jbrukh/status/1640444880689176576?s=20)
- Programming bots that, including some that [teach you Spanish](https://twitter.com/jbrukh/status/1640444883654549507?s=20)
- Psuedocode transpilation: [turn your pseudocode into actual code](https://twitter.com/jbrukh/status/1640444882106867712?s=20)

## Getting Started

### Running Jargon directly

Jargon currently runs best on GPT-4, and to a limited extent, on GPT-3.5. Copy the prompt in `jargon_cli/jargon.md` into GPT, and it should give you a prompt:

    jargon>

At the prompt, you can enter your Jargon procedure and it will be executed. You can use some commands to manage your procedures:

    - /execute or /run will execute a PROCEDURE.
    - /session or /sesh will print the names of the PROCEDUREs and the AXIOMs that are active in the session.
    - /wipe will terminate all the PROCEDUREs in the session.
    - /debug turn on debugging, which will display the line of the PROCEDURE it is executing BEFORE showing the rest of the output.
    - /audit will print a procedures code with line numbers.

### Running Jargon using `jargon_cli`

Install `jargon_cli` by executing the following inside of the repo:

    $ pip install .

You will need to make sure your `OPENAI_API_KEY` is set for the cli to be able to access an LLM interpreter. The default model is `gpt-4`, but you can specify others:

    $ jargon --model gpt-3.5-turbo cli

Run the tool:

    $ jargon help

First, create a Jargon procedure:

    $ jargon edit nomic

This creates `nomic.jarg` in your `JARGON_DIR`, which is `~/.jargon/` by default. You can list known procedures:

    $ jargon ls

To execute a procedure:

    $ jargon execute nomic

This will give you a command line interface to the Jargon-executing LLM.

You can also do all of this stuff directly from a cli:

    $ jargon cli
    Commands: /exit, /ls, /cat <proc>, /edit <proc>, /execute <proc> or /<proc>, /clear
    > /ls
    > /edit test.jarg
    > /cat test.jarg
    > /execute test.jarg
    > /clear
    > /exit

## Unit Testing

You can run unit tests on Jargon by using the Jargon procedure specified in `tests.jarg`. Running tests should make Jargon work better. There is also some more info about running unit tests [in this article](https://jake.mirror.xyz/6j-KetfRE4kQRyI2-Xf2JsP4UL-DPKi20WhOVbWT2dE).

## Syntax Highlighting

* https://github.com/jbrukh/jargon-vscode-support

## Related Projects

* [Jargon-Nock](https://github.com/tacryt-socryp/jargon-nock/) implements Urbits Nock as a GPT prompt.
* [SudoLang](https://medium.com/javascript-scene/sudolang-a-powerful-pseudocode-programming-language-for-llms-d64d42aa719b) by Eric Elliot is pseudolanguage that specified itself.
* [PromptLang](https://github.com/ruvnet/promptlang) is a custom programming language specifically designed for use in GPT-4 prompts. 
* [PML](https://github.com/dineshraju/pml) is a markup pseudolanguage that's used in LLM prompt engineering to generate long-form content.

## Jargon Procedure Gallery

### A Spanish vocabulary tutor.

Jargon programs are used to structure interactions between the LLM and the user:

```
+++
* For any input that I enter in Spanish, check my input for grammatical correctness.
* Every 5 words, ask me if we should adjust the difficulty level.
@repeat:
  -- Tell me a word in Spanish and ask me to define it.
  @if [my definition is correct]: 
    -- Tell me so and increase my score by 1 point.
  @else:
    -- Tell me the correct definition. Encourage me to do better next time.
  @endif
  -- Tell me my score.
  /goto @repeat
+++
```

### Answering questions in Spanish.

Another way to learn more Spanish.

    +++ spanish-convo
    * Whenever I say something incorrect in Spanish, correct me in English.
    @repeat:
      -- Ask me a question in Spanish.
      /goto @repeat
    +++

### Quines are trivial in Jargon.

A [quine is a program that outputs its own source code](https://en.wikipedia.org/wiki/Quine_(computing)).

    +++ quine
    /output [the source code of this quine]
    +++

### Generative AI performance art.

Try this out and keep saying no to see how creative the AI will get.

```
+++ cookie-performance-art
@label:
-- Ask me if you can have my cookie.
/wait
@if [I say refuse to give it to you]:
  -- It will make you want the cookie more. Persuade me to give it to you. Get desperate. Be terse.
@else:
  -- Lose interest in the cookie and refuse to take it. Be a little rude.
@endif
/goto @label
+++
```

### You can pass parameters.

As of `v0.0.9`.

    +++ square($x)
    /return $x
    +++

    +++ sequence
    -- For $x values from 1 to 10, print square($x).
    +++

### Divining inline functions.

This procedure defines an inline function and applies it to coming up with marketing slogans.

    +++ products
    -- slogan($product) <- Output a 1 sentence short, pithy marketing slogan for $product
    -- Think of 10 new incredibly cool products that should come to market
    -- For each $product: /output "$product -- slogan($product)"
    +++

### A good example of axioms.

Jargon `v0.0.10` wrote this nice idiomatic example of how to use axioms.

    +++ precise-math
    * When performing arithmetic operations, round to two decimal places
    -- Calculate 3.14159 * 2
    +++
