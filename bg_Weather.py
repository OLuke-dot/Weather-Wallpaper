import requests
import ctypes
import datetime
import pathlib
import time

city = r''  # Place your city here
api_Key = r''  # Place your API Key here
url = r'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid='
url += api_Key


def get_date():
    json_data = requests.get(url).json()  # weather file
    full = json_data["weather"][0]['main']
    print(full)
    return full


def wComparison(data):
    SPI = 20
    adress = str(pathlib.Path(__file__).parent.absolute()) + r'\wallpapers'
    # Adress to the wallpaper folder, which should be in the same place as program
    dateNow = datetime.datetime.now().time()
    startDay = datetime.time(6, 0)  # Timestamps for day and night
    endDay = datetime.time(18, 1)
    startNight = datetime.time(18, 0)  # The day is being refered as between 6:00 and 18:00
    endNight = datetime.time(6, 1)
    midnight = datetime.time(23, 59)
    fileName = str(data.lower())  # All wallpapers should have names in a lowercase

    if startDay <= dateNow <= endDay:
        fileName += r'.jpg'
        try:
            ctypes.windll.user32.SystemParametersInfoW(SPI, 0, adress + "\\" + fileName, 3)
        except NameError:
            ctypes.windll.user32.SystemParametersInfoW(SPI, 0, adress + r"\wallpaper.jpg", 3)
    elif startNight <= dateNow <= midnight or 0 <= dateNow <= endNight:
        try:
            fileName += r'_night.jpg'
            ctypes.windll.user32.SystemParametersInfoW(SPI, 0, adress +'\\' +  fileName, 3)
        except NameError:
            ctypes.windll.user32.SystemParametersInfoW(SPI, 0, adress +'\\' +  fileName, 3)
        finally:
            ctypes.windll.user32.SystemParametersInfoW(SPI, 0, adress + r"\wallpaper.jpg", 3)
    else:
        ctypes.windll.user32.SystemParametersInfoW(SPI, 0, adress + r"\wallpaper.jpg", 3)
    return


while True:
    data = get_date()
    oldData = ''
    if oldData == data:
        pass
    else:
        wComparison(data)
        oldData = data
    time.sleep(900)
