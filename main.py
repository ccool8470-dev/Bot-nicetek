name: Pabrik Youtube Bot

on:
  schedule:
    - cron: '0 3 * * *'
  workflow_dispatch:

jobs:
  produksi-video:
    runs-on: ubuntu-latest
    steps:
      - name: Mengambil kode mesin
        uses: actions/checkout@v4

      - name: Menyiapkan Komputer Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Menginstal Alat Baru
        run: pip install google-genai edge-tts

      - name: Menjalankan Produksi Video
        env:
          KUNCI_GEMINI: ${{ secrets.KUNCI_GEMINI }}
        run: python main.py

      - name: Mengamankan Hasil
        uses: actions/upload-artifact@v4
        with:
          name: Hasil-Produksi-Hari-Ini
          path: |
            naskah.txt
            suara_video.mp3
