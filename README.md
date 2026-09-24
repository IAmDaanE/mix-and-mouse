# Mix and Mouse

A game about creating cocktails on demand for customers, discovering new recipes and unlocking new ingredients. Written in python using pygame. Has a Json file saving system and a leaderboard API.

<p float="left">
  <img src="https://github.com/user-attachments/assets/cbc47fa4-ec5b-40c9-a8d6-f663b3ce9e9c" width="32%" />
  <img src="https://github.com/user-attachments/assets/6385fc92-2d2d-46bb-afff-dce537dad8b0" width="32%" />
  <img src="https://github.com/user-attachments/assets/014ffe19-e748-4a1e-b954-d2d63a208098" width="32%" />
</p>
<p float="left">
  <img src="https://github.com/user-attachments/assets/04e284d5-fa09-4a9a-b4a2-3b55e4829bfa" width="32%" />
  <img src="https://github.com/user-attachments/assets/9928e26a-56fc-4c6d-8f4e-40e975454fce" width="32%" />
  <img src="https://github.com/user-attachments/assets/e76a99fc-f22e-4da2-9918-de7137d7ad45" width="32%" />
</p>

## About the Project

You can find the .exe version of this game on [its itch.io page](sdfsdf).

I am a teenager from Belgium and created this together with my cousin who [is also on GitHub](https://github.com/TVR-spec). When starting the project I barely had any coding experience and due to this the entire game lives in one python file with 2500 lines of code and the codebase is very chaotic and messy.

### Game

All cocktails are based on real world ones so knowing a lot about them is definitely an advantage.

All assets were drawn by my cousin in `Aseprite`, which was a lot of work.

The game consists of a bunch of scenes so to display those we just use a bunch of functions like `display_homescreen()` and `display_recipe_book()`. Then in the game loop we select which one to call based on what scene we are in.

When firing up the game for the first time the user is prompted to select a username, this is saved in a text file and used from that point on.

### Leaderboard API

To store each player's cocktail with the highest value and how much customers they have already served there is a leaderboard system with an API and database for both pushing and pulling.  

The api was written in python using the `Flask` library and is hosted on [Render](https://render.com/). This makes it completely free but the service does spin down if there is no activitiy for about 30 minutes, when that happens the next request will take more then 50 seconds to respond to, so i set up a [UptimeRobot](https://uptimerobot.com/) monitor that pings it every 5 minutes.  

The database is a `PostgresQL` service hosted on [Supabase](https://supabase.com/), also for free. The api communicates with the database using `psycopg2` which makes it really easy.

### How To Play

When first starting the game enter a username and click on `NEW` at the top of the starting screen, enter the name of your playthrough save file and click `CREATE`.

You are now at the homescreen, this is the point from where you can go to other places:
* Go to the ingredient marketplace by clicking on the door of your storage area.
* Go to the cocktail creation environment by clicking on the bottles and shaking cups on the counter.
* Go to your menu by clicking on the price list sticking to the counter.
* Go to your waiting customers at the bar by clicking on the bartender himself.
* Go to the recipe shop by clicking on the stack of recipe books on the counter.
* Go to your own recipe book at any time by pressing the `TAB` key on your keyboard
* Go to the progress screen by clicking on your username in the top right.

Make money by first buying some ingredients, then either trying some combinations of recipes you know in real life until you discover a new one for your recipe book or making a recipe you already know. Each recipe you create gets a score of stars out of five, the more stars the more perfect your ratios of ingredients, this means you can improve on recipes you already discovered make them worth more.

To see what your guests want to order go to the guest screen by clicking on your bartender and clicking on individual guests. Customers will only pick something thats on your menu and you can add things to your menu from inside the recipe book, for the cocktail you want to add to the menu click `ADD` and they can now choose this one as well.

When you made a cocktail or smudge if the ingredients you used didn't create an existing cocktail, go to your guests and drag it over to the one who ordered that drink.

## Starting the Program

**Requires:** Python 3.9 - 3.14
1. Install the required libraries, preferably in a venv.

    ```
    pip install -r requirements.txt
    ```
2. Run the program.

    ```
    python src/main.py
    ```

## License

This project is open-source and available under the MIT License.