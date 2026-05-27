import sys

def risk_analizi(ports):
    print("\n=========================================")
    print("🛡️  SİBER GÜVENLİK RİSK ANALİZ RAPORU 🛡️")
    print("=========================================\n")
    
    if not ports:
        print("💡 Durum: Kritik bir port açık bulunamadı. Temiz görünüyor.")
        return

    for port in ports:
        if port == 22:
            print("[CRITICAL] Port 22 (SSH) Açık!")
            print("👉 Risk: Kaba kuvvet (Brute Force) saldırılarına maruz kalabilir.")
            print("🛑 Öneri: Güçlü şifre politikası uygulayın veya SSH anahtarı (Key) kullanın.\n")
        elif port == 80 or port == 8080:
            print("[HIGH] Port 80/8080 (HTTP) Açık!")
            print("👉 Risk: Trafik şifrelenmediği için Man-in-the-Middle (MitM) riski taşır.")
            print("🛑 Öneri: SSL/TLS sertifikası kurarak HTTPS (Port 443) protokolüne geçin.\n")
        elif port == 21:
            print("[CRITICAL] Port 21 (FTP) Açık!")
            print("👉 Risk: Anonim girişler ve şifrelenmemiş veri aktarımı zafiyet yaratır.")
            print("🛑 Öneri: FTP yerine güvenli SFTP protokolünü tercih edin.\n")
        else:
            print(f"[INFO] Port {port} Açık: Servis yapılandırmasını kontrol edin.\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: python3 app.py <port1,port2,port3...>")
        sys.exit(1)
        
    # Terminalden gelen virgülle ayrılmış portları listeye çeviriyoruz
    try:
        acik_portlar = [int(p) for p in sys.argv[1].split(",") if p.strip()]
        risk_analizi(acik_portlar)
    except ValueError:
        print("Hata: Lütfen geçerli port numaraları girin (Örn: 22,80).")
