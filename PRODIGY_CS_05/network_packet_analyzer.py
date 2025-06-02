#!/usr/bin/env python3
from scapy.all import sniff, IP, TCP, Raw
import sys
from datetime import datetime

TARGET_IP = "192.168.233.129"
LOG_FILE = "scan_log.txt"

def log_to_file(text):
    with open(LOG_FILE, "a") as f:
        f.write(text + "\n")

def packet_callback(packet):
    if IP in packet and TCP in packet:
        ip_layer = packet[IP]
        tcp_layer = packet[TCP]

        if ip_layer.src == TARGET_IP or ip_layer.dst == TARGET_IP:
            timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
            src_ip = ip_layer.src
            dst_ip = ip_layer.dst
            src_port = tcp_layer.sport
            dst_port = tcp_layer.dport
            protocol = "TCP"
            pkt_len = len(packet)
            payload = ""

            if packet.haslayer(Raw):
                try:
                    payload = packet[Raw].load.decode(errors="ignore")
                except:
                    payload = "Could not decode payload"

            log_entry = (
                f"{timestamp}\n"
                f"  Source IP     : {src_ip}:{src_port}\n"
                f"  Destination IP: {dst_ip}:{dst_port}\n"
                f"  Protocol      : {protocol}\n"
                f"  Packet Length : {pkt_len} bytes\n"
            )

            if payload:
                log_entry += f"  Payload        : {payload[:100]}\n"

            log_entry += "-" * 60  # separator line
            log_to_file(log_entry)

print(f"[*] Sniffing traffic to/from {TARGET_IP} and logging detailed info to {LOG_FILE}...")

try:
    sniff(filter=f"host {TARGET_IP} and tcp", iface="eth0", prn=packet_callback, store=0)
except PermissionError:
    print("[!] Run this script with sudo or as root.")
except Exception as e:
    print(f"[!] Error: {e}")
    sys.exit(1)
