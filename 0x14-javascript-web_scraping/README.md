<h1>Javascript-web_scraping</h1>

<h2>General</h2>
<li>Why JavaScript programming is amazing
How to manipulate JSON data
How to use request and fetch API
How to read and write a file using fs module
Install Node 10
</li>

curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs

Install semi-standard

sudo npm install semistandard --global

Install request module and use it

sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules

<h1>0x14. Javascript - Web scraping</h1>

This project involved practicing file I/O on Node.js and using the NPM request framework to interact with both the Star Wars and JSONplaceholder API's. I was introduced to Javascript web scraping using the request and fs modules.
<h2>Tasks 📃:</h2>

<h3>0. Readme</h3>
        0-readme.js: JavaScript script that reads and prints the contents of a file.
        Usage: ./0-readme.js <file path>.

<h3>1. Write me</h3>
        1-writeme.js: JavaScript script that writes a string to a file.
        Usage: ./1-writeme.js <file path> <string to write>.

<h3>2. Status code</h3>
        2-statuscode.js: JavaScript script that displays the stauts code of a GET request using the request framework.
        Usage: ./2-statuscode.js <URL to GET>.
        Output: code: <status code>.

<h3>3. Star wars movie title</h3>
        3-starwars_title.js: JavaScript script that uses the Star Wars API to print the title of the Star Wars movie with a given integer episode number.
        Usage: ./3-starwars_title.js <3-starwars_title.js>.

<h3>4. Star wars Wedge Antilles</h3>
        4-starwars_count.js: JavaScript script that uses the Star Wars API to print the number of movies featuring the character "Wedge Antilles".
        Usage: ./4-starwars_count.js http://swapi.co/api/films/.

<h3>5. Loripsum</h3>
        5-request_store.js: JavaScript script that stores the contents of a webpage in a file.
        Usage: ./5-request_store.js <URL to get> <file path to store content in>.

<h3>6. How many completed?</h3>
        6-completed_tasks.js: JavaScript script that uses the JSONPlaceholder API to compute the number of tasks completed per user ID.
        Usage: ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos.

<h3>7. Who was playing in this movie?</h3>
        100-starwars_characters.js: JavaScript script that uses the Star Wars API to print all characters featured in a given movie.
        Usage: ./100-starwars_characters.js <movie ID>.

<h3>8. Right order</h3>
        101-starwars_characters.js: JavaScript script that uses the Star Wars API to print all characters featured in a given movie in the same order as they are listed in the characters list of the /films/ response.
        Usage: ./101-starwars_characters.js <movie ID>.

