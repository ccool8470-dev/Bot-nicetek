import os
import google.generativeai as genai

# 1. Mengambil kunci rahasia dari brankas GitHub
KUNCI_GEMINI = os.environ.get("KUNCI_GEMINI")
genai.configure(api_key=KUNCI_GEMINI)

# 2. Menyalakan otak AI
model = genai.GenerativeModel('gemini-1.5-pro-latest')

print("Memulai produksi konten hari ini...")
print("1. Meminta Gemini menulis naskah teknologi masa depan...")

# Perintah untuk AI
prompt = "Buatkan naskah video YouTube Shorts (durasi 1 menit) tentang teknologi masa depan. Gunakan gaya bahasa Indonesia yang misterius, keren, dan memancing rasa penasaran penonton. Jangan gunakan emoji atau tanda bintang."

respons = model.generate_content(prompt)
naskah = respons.text.strip().replace('"', '')

# Menyimpan naskah ke dalam file teks
with open("naskah.txt", "w", encoding="utf-8") as f:
    f.write(naskah)

print("2. Mengubah naskah menjadi suara narator otomatis...")
# Membersihkan baris baru agar suara tidak terpotong
naskah_satu_baris = naskah.replace('\n', ' ') 

# Memanggil Edge-TTS
os.system(f'edge-tts --text "{naskah_satu_baris}" --write-media suara_video.mp3 --voice id-ID-ArdiNeural')

print("SELESAI! Naskah dan Suara MP3 berhasil diproduksi!")
