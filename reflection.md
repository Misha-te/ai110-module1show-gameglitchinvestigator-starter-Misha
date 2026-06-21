# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

When I ran the game, it opened a window on the browser with an interactive window. There were several buttons for example 'make a guess' button and 'enter your guess' window. Upon making a guess, there was a button for submitting my guess and a button for restarting the game and showing hints.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. The hints are misleading, When the guess is lower and I'm required to go higher, the hints tell me to go lower, hence ends up moving away from the actual answer.
  2. The Range for the levels is ignored. The game gave secret numbers between 1 and 100 regardless of the level.
  3. The New Game button is not working, I had to refresh my window to continue playing after losing or winning a game.



**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input              | Expected Behavior         | Actual Behavior         | Error |
|--------------------|--------------------------|-------------------------|-------|
| Guess of 71        | Go lower                 | Go higher               | None  |
| Easy Level         | Secret number<br>1–20    | Number between<br>1–100 | None  |
| Press on New Game  | New secret number        | No change               | None  |



## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
