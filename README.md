LAB - Class 06
Project: ten-thousand - version 1
Author: Tyler Huntley & Dutch Foy
Links and Resources
[ChatGPT](https://openai.com/)  
[chatgpt md](ten_thousand/chatgpt.md)
How to initialize/run your application (where applicable)
python ten-thousand/game_logic.py
How to use your library (where applicable)
Tests
How do you run tests?
pytest -k version_#

Any tests of note? 
Three 1s and a 5 was a pain to get passing. In the end, we had an order of operations issue, and after moving the 5s code towards the bottom, the test passed.

ChatGPT is not very helpful and consistently writes code that will not pass the tests. 

## SETUP
```
python3 -m venv .venv
python3 .venv/bin/activate

pip install -r requirements.txt
# Will install pytest by default
```

-----------------------------------------------------------------------------------------------------------

LAB - Class 07
Project: ten-thousand - version 2
About this lab: Extend Ten Thousand game started in previous class to get the game in playable state.
Feature Tasks and Requirements:  
- Implement all features from previous version.  
- Allow user to set aside dice each roll.  
- Allow “banking” current score or rolling again.  
- Keep track of total score.  
- Keep track of current round.  
- 
Author: Tyler Huntley (Dutch never showed up to lab to work this assignment)
Links and Resources
[ChatGPT](https://openai.com/)
How to initialize/run your application (where applicable)
python ten-thousand/game_logic.py
How to use your library (where applicable)
Tests
How do you run tests?
pytest -k version_#

Any tests of note? 
Worked on lab for approximately 7 hours. Was unable to get unbanked score finished.

-----------------------------------------------------------------------------------------------------------

LAB - Class 08
Project: ten-thousand - version 3
About this lab: 
Shore up the core functionality of game by allowing users to set aside scoring dice and continuing their turn. 
Then we’ll handle cheaters and/or confused players who are skirting the rules.
Feature Tasks and Requirements:  
- Application should implement features from versions 1 and 2
- Should handle setting aside scoring dice and continuing turn with remaining dice.
- Should handle when cheating occurs.
  - Or just typos.
  - E.g. roll = [1,3,5,2] and user selects 1, 1, 1, 1, 1, 1
- Should allow user to continue rolling with 6 new dice when all dice have scored in current turn.
- Handle zilch
  - No points for round, and round is over

Author: Tyler Huntley & Dutch Foy
Links and Resources
[ChatGPT](https://openai.com/)
How to initialize/run your application (where applicable)
python ten-thousand/game_logic.py
How to use your library (where applicable)
Tests
How do you run tests?
pytest -k version_#

Any tests of note? 
