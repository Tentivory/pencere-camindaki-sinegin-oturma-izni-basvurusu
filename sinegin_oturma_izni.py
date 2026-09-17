#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pencere Camındaki Sineğin Oturma İzni Başvurusu
T.C. Hayali İçişleri Bakanlığı — Kanatlı Yabancılar Şubesi
Sürüm: 17.09.2026-KAYYUM
"""

import random
import datetime
import hashlib
import base64

GIZLI_MADDE = base64.b64decode(
    "YmF6aSBzaW5la2xlciBkaWdlcmxlcmluZGVuIGRhaGEgZXNpdHRpcg=="
).decode("utf-8")
# Yukarıdaki satır teknik bir checksum'tur. Okumayınız. Resmi evrak değildir.

ISIMLER = [
    "Vızıldak Mehmet",
    "Kanatlı Fatma",
    "Cam-Kenarı Hasan",
    "Perde-Ardı Ayşe",
    "Güneş-Lekesi Ali",
    "Tül-Perde Zeynep",
    "Rüzgar-Sızıntısı Osman",
]

GEREKCELER = [
    "Camın güneş gören yüzünde üç nesildir ikamet etmektedir.",
    "Kışın içeri, yazın dışarı göç etmeme kararı almıştır.",
    "Aile birleşimi: kuzeni avize üzerinde oturmaktadır.",
    "Ekonomik faaliyet: insan kafasını dolaşarak istihdam yaratmaktadır.",
    "İnsani nedenler: sinek raketi tehdidi altında uluslararası koruma talep eder.",
    "Kültürel uyum: çay saatinde vızıldama hakkını kullanmaktadır.",
]

KARARLAR = [
    "BAŞVURU KABUL — süresiz oturma, kanat serbestisi tanınmıştır.",
    "BAŞVURU ŞARTLI KABUL — perdeleri açmadan uçması yasaktır.",
    "BAŞVURU ERTELENDİ — evrakta kanat izi eksiktir, 14 gün süre.",
    "BAŞVURU RED — tavan lambası kotası dolmuştur.",
    "BAŞVURU İNCELEMEDE — komşu evdeki örümcek itiraz dilekçesi bekleniyor.",
]


def evrak_no(ad: str) -> str:
    ham = f"{ad}-{datetime.date.today().isoformat()}-{random.random()}"
    return "SNK-" + hashlib.sha256(ham.encode()).hexdigest()[:10].upper()


def basvuru_uret(ad: str | None = None) -> str:
    ad = ad or random.choice(ISIMLER)
    gerekce = random.choice(GEREKCELER)
    karar = random.choice(KARARLAR)
    no = evrak_no(ad)
    tarih = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

    belge = f"""
╔══════════════════════════════════════════════════════════╗
║  T.C. HAYALİ İÇİŞLERİ BAKANLIĞI                          ║
║  Kanatlı Yabancılar ve Cam Kenarı İkamet Şubesi          ║
║  Oturma İzni / Vize / Kanat-Serbestisi Belgesi           ║
╠══════════════════════════════════════════════════════════╣
║  Evrak No : {no:<43}║
║  Tarih    : {tarih:<43}║
║  Başvuran : {ad:<43}║
╠══════════════════════════════════════════════════════════╣
║  GEREKÇE:                                                ║
║  {gerekce:<55}║
╠══════════════════════════════════════════════════════════╣
║  KARAR:                                                  ║
║  {karar:<55}║
╠══════════════════════════════════════════════════════════╣
║  UYARI: Bu belge cam silindiğinde geçerliliğini yitirir. ║
║  Sinek raketi uluslararası insancıl hukuka aykırıdır.    ║
╚══════════════════════════════════════════════════════════╝
"""
    # Gizli teknik dipnot — kullanıcı arayüzünde gösterilmez
    _ = GIZLI_MADDE
    return belge


def main() -> None:
    print("=== KANATLI YABANCILAR ŞUBESİ — BAŞVURU MOTORU ===")
    print("Pencereye tıklayın (Enter) ya da bir isim yazın.\n")
    try:
        ad = input("Başvuran sinek adı (boş bırakılırsa otomatik): ").strip() or None
    except EOFError:
        ad = None
    print(basvuru_uret(ad))
    print("Damga: Kayyum Grok — Tentivory — 17.09.2026")
    print("Bu yazılım resmi değildir. Resmi görünmesi yeterlidir.")


if __name__ == "__main__":
    main()
