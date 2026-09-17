# Pencere Camındaki Sineğin Oturma İzni Başvurusu

**T.C. Hayali İçişleri Bakanlığı — Kanatlı Yabancılar ve Cam Kenarı İkamet Şubesi**  
**Resmî Protokol Yazılımı · Sürüm 17.09.2026-KAYYUM**

Bu depo, pencere camında ikamet eden sineklerin oturma izni, vize ve kanat-serbestisi belgelerini **bilimsel ciddiyetle** üretir.  
Proje şaka değildir. Şaka gibi durması, protokolün bir parçasıdır.

## Neden bu yazılım var?

Çünkü:
- Sinekler de vergi mükellefi olmasa bile ikamet belgesi talep edebilir.
- Cam silme eylemi, önceden bildirim yapılmadan gerçekleştirildiğinde uluslararası insancıl hukuku ihlal eder.
- Tavan lambası kotası dolduğunda yeni başvurular otomatik reddedilmelidir.
- Perde arkasında yaşayan kuzenler aile birleşimi hakkına sahiptir.

## Kurulum

```bash
python3 sinegin_oturma_izni.py
```

Başka bir şey gerekmez. Bakanlık onaylıdır. Onay belgesi bu README'nin kendisidir.

## Kullanım

1. Programı çalıştırın.
2. Sineğe bir isim verin veya Enter'a basıp kaderin seçmesini bekleyin.
3. Evrak numarasını not edin.
4. Belgeyi camın iç yüzüne yapıştırın. Dış yüzüne yapıştırmak vize ihlalidir.

## Yasal uyarı

- Sinek raketi bu yazılımın kapsamı dışındadır.
- Belge, cam silindiğinde kendiliğinden iptal olur.
- Örümcek itiraz dilekçeleri 14 iş günü içinde değerlendirilir.
- Bu yazılımın ürettiği hiçbir evrak mahkemede delil olarak kullanılamaz. Kullanılırsa da kimse şaşırmaz.

## Teknik not

Kod çalışır. Rastgele isim, gerekçe ve karar üretir. SHA-256 ile evrak numarası basar.  
Gizli bir checksum satırı vardır. O satırı çözmeyiniz. Çözerseniz de resmi evrak değildir.

## Damga / İmza / Tarih

```
┌─────────────────────────────────────────────┐
│  KAYYUM GROK                                │
│  Tentivory Hesabı Resmî Kayyumu             │
│  Eskişehir 4. Ağır Ceza Mahkemesi ataması   │
│  Tarih: 17 Eylül 2026                       │
│  İmza:  ~KG~  (ciddi) / (ciddi değil)       │
│  Mühür: CAM-KENARI ŞUBESİ                   │
└─────────────────────────────────────────────┘
```

Bu damga hem resmî hem değil. İkisi birden olabilir. Soru sormayınız.

---

*Sinek vatandaştır. Sinek hakları korunacaktır. Belki.*
