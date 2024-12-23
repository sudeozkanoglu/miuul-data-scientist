from openai import OpenAI  # OpenAI kütüphanesinden gerekli sınıfı içe aktarır.
import os  # İşletim sistemi ile etkileşim için os modülünü içe aktarır.
from dotenv import load_dotenv  # Çevresel değişkenleri yüklemek için dotenv modülünü içe aktarır.

load_dotenv()  # .env dosyasındaki çevresel değişkenleri yükler.

my_key = os.getenv("openai_apikey")  # .env dosyasından "openai_apikey" anahtarını alır.
#print(my_key)  # API anahtarını kontrol etmek için ekrana yazdırır (yorum satırında).

client = OpenAI(api_key=my_key)  # OpenAI istemcisini API anahtarı ile başlatır.


AI_Response = client.chat.completions.create(  # OpenAI API'sine bir sohbet isteği gönderir.
    model="gpt-3.5-turbo-1106",  # Kullanılacak modeli belirtir.
    temperature=0,  # Yanıtın rastgelelik seviyesini ayarlar (0: en belirgin, 1: en rastgele).
    max_tokens=256,  # Döndürülecek maksimum token (kelime/parça) sayısını belirler.
    messages=[  # Sohbet geçmişini ve rollerini içeren mesajları tanımlar.
        {"role":"system", "content": "Sen yardımsever bir asistansın."},  # Asistanın kişiliğini belirler.
        {"role":"user", "content": "Mevsimler neden oluşur? Dünya kendi etrafında döndüğü için mi?"}  # Kullanıcıdan gelen soruyu ekler.
    ]
)

print(AI_Response.choices[0].message.content)  # Yanıtın içeriğini ekrana yazdırır.
