<h1>Hangman Game</h1>
<p>This is a simple hangman game created using the Pygame library in Python. The game includes a main menu, a gameplay state, and a win/lose state. The game also includes a feature for changing the difficulty level, and a feature for displaying the player's score.</p>
<h2>Getting Started</h2>
<p>To run the game, you will need to have Python and Pygame installed on your computer. You can download Python from the official website (<a href="https://www.python.org/" target="_new">https://www.python.org/</a>) and Pygame can be installed using pip (<code>pip install pygame</code>).</p>
<h2>Gameplay</h2>
<p>The game starts with a main menu where the player can enter their name, select the difficulty level, and start the game. The player is then presented with a word to guess, with the letters hidden. The player must then guess letters one at a time, with a wrong guess resulting in a part of the hangman being drawn. The game ends when the player either correctly guesses the word or the hangman is fully drawn.</p>
<h2>Difficulty level</h2>
<p>The game has 3 difficulty levels: easy, normal and hard. The player can select the difficulty level before starting the game. The difficulty level affects the words that the player has to guess.</p>
<h2>Scoring</h2>
<p>The player's score is based on the number of wrong guesses. The player earns a point for each correct guess and loses a point for each wrong guess. The score is displayed on the screen during the game and also on the win/lose screen.</p>
<h2>Files</h2>
<p>The game uses a json file "words.json" to get the words according to the difficulty level. <br>
  The game uses a json file "scores.json" to save the score of the player after the game is over.
</p>
<h2>Future Enhancements</h2>
<ul>
  <li>Adding a hint feature to give the player a hint about the word.</li>
  <li>Adding sound effects and background music.</li>
</ul>
<h2>Author</h2>
<ul>
  <li><strong>Author Name</strong> - <a href="https://github.com/Marin-Clement" target="_new">Marin-Clement</a></li>
</ul>



