# Weather-Wallpaper

The program uses openWeather API for downloading data about current weather in one place and then changes background based on them.
Ctypes module required, for installing just use <i>pip install ctypes</i> for Windows.

## Description
This program works in the background and every 15 minutes it downloads new data, compares it with the previous one, and if the weather changed, it adjust the proper wallpaper on your screen. Images are being taken from a wallpaper folder, placed next to the program. <br><br>
<t>The data being extracted are just a main string describing weather outside. This name is then used to load up wallpaper. For example, if the weather outside is "Cloudy", the program will be looking for a "cloudy.jpg" file in the folder. For night time, program adds "_night" in the name of the file ("clouds_night.jpg"). Full list of possible names will be added here later
## Getting API Key
For program to work, you will need an API key from openweather website. The other variable which is important is a city, where, obviously, you place a city where you want to check a weather
* go to https://openweathermap.org/
* Sign up, or create your account
* While in your profile, go to <i>API Keys tab</i>
* Generaste new key or use one created already
* Put your API key in the program

## Making program start with Windows
If you want weather app to work in the background while windows is starting, follow these steps:
* Create a shortcut of a program and copy it to your clipboard
* Type win + r on keyboard
* type <i>shell:startup</i> and press Enter
* Paste your shortcut here

Now every time you will boot up Windows, program will automatically start in the background
## Full list of wallpaper nametags
Below is a ful list of all supported nametags, based on openweather informations. In order to assign wallpaper to a proper condition, rename JPEG file into its nametag.

* wallpaper - basic one
* clear
* clear_night
* clouds
* clouds_night
* rain
* rain_night
* snow
* snow_night
* drizzle
* drizzle_night
* thunderstorm
* thunderstorm_night
* mist
* mist_night
* smoke
* smoke_night
* haze
* haze_night
* dust
* dust_night
* ash - volcanic ash
* ash_night
* squall
* squall_night
* tornado
* tornado_night

