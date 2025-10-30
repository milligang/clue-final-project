## Video URL:
https://youtu.be/tiBW9tZ_jRg    

## Documentation:
Our project was done in the cs50 code space and is similar in structure to the finance pset. It uses python in app.py, jinja and html for the html pages, and sqlite3. 
To use, unzip clue.zip, open a terminal, and (inside clue) type flask run to start using flask. This url should take you to the homepage of the site.

### Files and Folders 
- static: images used in the html pages and style.css, including style classes we made for our html pages
- templates: html templates
- app.py: the main python code for the app
- clue.db: sql tables used

## How to play:
For our project, we chose to take the board game CLUE and make a CS-50 themed version, featuring the murder of the CS50 Duck here at Harvard. When you go to the webpage, a pop-up will appear announcing that this is CS50 CLUE, and you can then click to begin.

Since CLUE is a two-player game, the device should be passed between the two players with only one player looking at the screen at a time. The first-player's cards are shown on the screen when you click begin; therefore it is important for the other player to not be sneaking a look since no one wants to play with a cheater. The first player will then have the opportunity to see their own cards that they have been given, and then the ability to go from there to either a page displaying all of the possibility card options, or the game board. If the player clicks on the all cards page they will have the ability to get from there back to their own cards. If the player goes to the gameboard they will be able to click any of the locations on the gameboard to use as their guess. Clicking on any of these images except the central image (university hall) will take you to the guessing page.

On the guessing page, the place will be autofilled based on the location the user chooses; however, the user will have the opportunity to choose a person and a weapon in their guess. Upon filling in these dropdowns, the user can submit their guess. Now the first player should give the device to the second player. The screen will then shift to a field for the second player where they can pick from a dropdown of their available cards options to show the first player. The theory behind this decision is that much like in the game of CLUE, a player can use strategy to decide which cards they wish to show their opponent, such as trying to only show cards with location. Then the game goes to a buffer page in which the second player can reveal which card they selected to reveal. After clicked 'next player's turn,' it is the second player's turn to view their cards and make a guess. The first player should not looking at the screen at this point, as this is cheating.

The second player's turn will occur in the same manner that the first player's turn did, with the same opportunities. Everytime the user submits a guess the turns will switch, as they do in the original board game.

Once a player believes they know what the correct answer is, they will choose University Hall (the building in the center of the game board which functions as the pool does in CLUE). From there, they will be able to submit a final guess that will be deemed either correct, making them the winner, or incorrect. The game goes to the final page, gameover, to reveal if that player won or lost and to reveal what the final answer was. Both players should look at this screen because the game is over and both players should be told what the correct answer was. If the players wish to play again, they can click 'new game' to reset the game and be redirected to the home page.

## Authors
Milligan Grinstead and Julia Grinstead
