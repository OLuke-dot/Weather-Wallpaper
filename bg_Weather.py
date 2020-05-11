import requests
import ctypes
import datetime
import pathlib
import time
SPI_SETDESKWALLPAPER = 20
city = r'' # Place your city here
api_Key = r'' # Place your API Key here
url = r'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_Key
adress = str(pathlib.Path(__file__).parent.absolute()) + r'\wallpapers'


def get_date():

    json_data = requests.get(url).json()  # weather file
    full = json_data["weather"][0]['main']
    print(full)
    return full


def change_wallpaper(data):
    dateNow = datetime.datetime.now().time()
    startDay = datetime.time(6, 0)
    endDay = datetime.time(18, 1)
    startNight = datetime.time(18, 0)
    endNight = datetime.time(6, 1)
    midnight = datetime.time(23, 59)
    fileName = str(data.lower())

    if startDay <= dateNow <= endDay:
        fileName += r'.jpg'
        try:
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, adress
            + "\\" + fileName, 3)
        except NameError:
            pass
    elif startNight <= dateNow <= midnight or 0 <= dateNow <= endNight:
        fileName += r'_night.jpg'
        try:
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, adress
            +'\\' +  fileName, 3)
        except NameError:
            pass
    else:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, adress
        + r"\wallpaper.jpg", 3)
    return


while True:
    data = get_date()
    oldData = ''
    if oldData == data:
        pass
    else:
        change_wallpaper(data)
        oldData = data
    time.sleep(900)
