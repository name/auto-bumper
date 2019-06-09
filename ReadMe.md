### Windows :
* Install Python > 3.5.3. Download the desired installer from [here](https://www.python.org/downloads/release/python-353/).
* [Add it in the system path](http://superuser.com/questions/143119/how-to-add-python-to-the-windows-path) (if not already added).
* Install pip and add to windows path, then do so by following [this little tutorial](http://stackoverflow.com/a/12476379).
* Download this repo and extract contents to a folder.
* Open Command Prompt and browse to the directory where you extracted this repo and run this command :
```
pip install -r requirements.txt
```
* It should install the required external libraries.
* Then head over to config.ini and change the following:
  * Change the username value
  * Change the password value
  * Change the threads and comments (format like below)
    * threads=https://ogusers.com/Thread-Steam-Account-250-Inventory-15YR-Lvl-100-106-Games^bumping using my custom autobumper,https://ogusers.com/Thread-twitch-fibre-rinse^bumping to the top using my custom autobumper,https://ogusers.com/Thread-soundcloud-orbit-nade^sending to the top with my custom autobumper
  * Finally save config.ini
 * Head to the directory where you extracted and open run.bat, this will start the bumper and will give you info in the command prompt.

Well, if everything came up good without any error(s), then you're good to go!

If not please reach out via discord: ju$tin#0666
