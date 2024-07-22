import requests
import os
import threading

os.system("clear")
try:
    def kirim_pesan(url, payload, jumlah_permintaan):
        for i in range(jumlah_permintaan):
            response = requests.post(url, data=payload)
            if response.status_code == 200:
                print(f"Pesan {i+1} berhasil dikirim ke bot Telegram.")
            else:
                print(f"Gagal mengirim pesan {i+1} ke bot Telegram.")
    
    def kirim_pesan_thread(url, payload, jumlah_permintaan):
        thread = threading.Thread(target=kirim_pesan, args=(url, payload, jumlah_permintaan))
        thread.start()
    
    if __name__ == "__main__":
        token_bot = str(input("TOKEN BOT: "))
        cht_id = int(input("CHAT ID: "))
        jumlah_permintaan = int(input("SPAM: "))
        pesan = input("TEKS: ")
        payload = {
            "parse_mode": "markdown",
            "chat_id": cht_id,
            "text": pesan
        }
        url = f"https://api.telegram.org/bot{token_bot}/sendMessage?"
    
        kirim_pesan_thread(url, payload, jumlah_permintaan)
except KeyboardInterrupt:
    print("ANDA TELAH KELUAR")