try:
    from utils.getdata import jsondata
    from utils.writejsondata import writedata


    writedata(jsondata)
except PermissionError:
    print("Json dosyası yazılırken erişim reddedildi!")
    
except ModuleNotFoundError:
    print("İlk olarak ütüphaneleri indir!")
except Exception as e:
    print("Bir Hata alındı --> ",e)