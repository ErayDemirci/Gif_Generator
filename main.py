import imageio.v3 as iio
import numpy as np
from PIL import Image

# Karelerin (resim yollarının) bir listesini oluştur
dosya_isimleri = ["resim1.png", "resim2.jpeg", "resim3.jpg"]

kareler = []
for dosya in dosya_isimleri:
    img = iio.imread(dosya)
    # Eğer resimler farklı boyutlardaysa, hepsini ilk resmin boyutuna getirebilirsiniz:
    img = Image.fromarray(img).resize((500, 500)) # Örnek boyut
    img = np.array(img)
    kareler.append(img)

# GIF Olarak Kaydet
# duration=500 (milisaniye cinsinden, yani her kare 0.5 saniye)
try:
    iio.imwrite("animasyon.gif", kareler, duration=500, loop=0)
    print("GIF başarıyla oluşturuldu!")
except Exception as e:
    print(f"Hata oluştu: {e}")
