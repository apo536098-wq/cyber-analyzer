use std::net::{TcpStream, ToSocketAddrs};
use std::time::Duration;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Kullanım: target_ip girmeniz gerekiyor. Örn: 127.0.0.1");
        return;
    }
    
    let target = &args[1];
    // Analiz edilecek yaygın siber güvenlik test portları
    let ports = vec![21, 22, 23, 25, 53, 80, 443, 8080]; 

    println!("--- Taramaya Başlanıyor: {} ---", target);
    
    for port in ports {
        let socket_address = format!("{}:{}", target, port);
        if let Ok(mut addrs) = socket_address.to_socket_addrs() {
            if let Some(addr) = addrs.next() {
                // 1 saniyelik timeout ile hızlıca soket kontrolü yapıyoruz
                if TcpStream::connect_timeout(&addr, Duration::from_secs(1)).is_ok() {
                    println!("[AÇIK] Port: {}", port);
                }
            }
        }
    }
}
