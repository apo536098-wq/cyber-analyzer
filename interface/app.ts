interface ScanResult {
    ip: string;
    status: string;
    logs: string[];
}

document.getElementById('scanBtn')?.addEventListener('click', () => {
    const targetIpInput = document.getElementById('targetIp') as HTMLInputElement;
    const outputDiv = document.getElementById('output');
    
    if (!targetIpInput || !outputDiv) return;

    const targetIp = targetIpInput.value;
    outputDiv.innerHTML = `⏳ ${targetIp} taranıyor... Rust ve Python motorları tetiklendi...\n`;
    outputDiv.style.color = "#00ff66";

    // Rust ve Python'dan aldığımız çıktıların simülasyonu
    setTimeout(() => {
        const mockResult: ScanResult = {
            ip: targetIp,
            status: "Tamamlandı",
            logs: [
                `--- Taramaya Başlanıyor: ${targetIp} ---`,
                "[AÇIK] Port: 22",
                "[AÇIK] Port: 80",
                "\n=========================================",
                "🛡️  SİBER GÜVENLİK RİSK ANALİZ RAPORU 🛡️",
                "=========================================",
                "[CRITICAL] Port 22 (SSH) Açık! -> Kaba kuvvet riski. SSH Key kullanın.",
                "[HIGH] Port 80 (HTTP) Açık! -> MitM riski. SSL/TLS kurun."
            ]
        };

        outputDiv.innerHTML = mockResult.logs.join("\n");
    }, 1500);
});
