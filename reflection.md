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

- Which AI tools did you use on this project?

I used ChatGPT, GitHub Copilot, and Claude Code. I used ChatGPT to help refine and improve the explanations and answers in my report. I initially used GitHub Copilot to identify and debug errors in my code. Later, after setting up Claude Code, I used it for most of my debugging and code review tasks.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One correct suggestion involved the difficulty levels in my Guess the Number game. The program was incorrectly generating numbers between 1 and 100 for all difficulty levels. The AI suggested replacing `random.randint(1, 100)` with `random.randint(low, high)` and using the `low` and `high` values defined for each difficulty level. I verified the suggestion by running the program and testing each difficulty level. After making the change, Easy mode generated numbers in its intended range, Normal mode generated numbers between 1 and 100, and Hard mode generated numbers in its intended range.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

One incorrect suggestion involved the hint system. The hints were displaying the wrong direction (for example, telling the player to guess higher when they should guess lower). I asked the AI to fix the issue, and it claimed the problem had been corrected. However, after running and testing the program, the hints were still backwards. I verified this by entering guesses that were clearly above or below the secret number and observing the incorrect feedback. I eventually fixed the logic manually and confirmed that the hints worked correctly through additional testing.

---

## 3. Debugging and testing your fixes
- How did you decide whether a bug was really fixed?

I did not rely solely on the AI's response. After the AI suggested a fix and said the bug was resolved, I ran the program and played the game myself to verify the result. If I could still reproduce the same problem, I would tell the AI that the bug was not fixed and continue debugging. For example, when the hints were displayed backwards, the AI initially claimed the issue had been fixed, but after testing the game I found that the problem still existed. In that case, I corrected the logic manually and verified that the hints worked properly afterward.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

I ran both manual tests and pytest tests. For the pytest tests, I used AI to help generate tests for bugs that had already been identified and fixed. I also generated tests that checked whether each difficulty level used the correct range of numbers.

For manual testing, I repeatedly started new games and checked the secret number for each difficulty level. In Easy mode, I verified that the secret number always stayed between 1 and 50. In Hard mode, I verified that the secret number always stayed between 1 and 20. By running the game multiple times, I confirmed that the difficulty settings were working correctly and that the program was using the intended number ranges.

- Did AI help you design or understand any tests? How?

Yes. AI helped me create most of the tests. I asked it to generate tests for the bugs we had fixed and to write assertions that checked whether the secret number stayed within the correct range for each difficulty level. The ideas for what needed to be tested came from me because I knew which bugs existed, but AI helped write the actual test code and assertions. I then reviewed the generated tests and used them to verify that the fixes were working as expected.


## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit reruns and session state to a friend who has never used Streamlit?

I would explain that a Streamlit rerun is what happens when the app refreshes itself after the user interacts with it. For example, when a player clicks a button or submits a guess, Streamlit runs the code again so that the app can display updated information. In my game, reruns helped update the game whenever the player made a guess or started a new game.

Session state is how Streamlit remembers information between those reruns. Without session state, the app would forget important information every time it refreshed. In my guessing game, session state was used to keep track of things such as the secret number, the selected difficulty level, and the number of guesses made. This allowed the game to continue from its current position instead of starting over whenever the app reran.


## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

One strategy I would like to reuse is collaborating with AI to better understand code and develop tests. Whenever I did not understand a piece of code or the logic behind a bug fix, I would ask AI to explain it. I also found it helpful to use AI to generate test cases that I could then review and run myself. This made debugging more efficient while still helping me learn.

- What is one thing you would do differently next time you work with AI on a coding task?

Next time, I would start the project earlier instead of waiting until close to the deadline. I would also try to do more of the coding work myself before asking AI for help. In this project, I felt that AI contributed a larger portion of the implementation than I would have liked. In future projects, I want to rely more on my own work and use AI mainly as a tool for guidance, debugging, and learning.

- In one or two sentences, describe how this project changed the way you think about AI-generated code.

This project reinforced my belief that AI-generated code should always be reviewed and tested carefully. I still do not trust AI output completely, but I now see it as a useful collaborator that can help with coding tasks when used responsibly and with proper verification.

