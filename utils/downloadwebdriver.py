def downloaddrivers():

    from requests import get

    win32 = get("https://storage.googleapis.com/chrome-for-testing-public/134.0.6998.88/win32/chromedriver-win32.zip")
    win64 = get("https://storage.googleapis.com/chrome-for-testing-public/134.0.6998.88/win64/chromedriver-win64.zip")

    with open("chromedriver-win32.zip","wb") as zip:
        zip.write(win32.content)

    with open("chromedriver-win64.zip","wb") as zip:
        zip.write(win64.content)