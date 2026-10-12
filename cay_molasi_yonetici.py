#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Çay Molaları Yöneticisi
Bu script, evrenin en büyük sorununu çözer: İnsanların çay içme ihtiyacı.
Bilimsel temeli yoktur ama çok ciddiye alınmalıdır.
"""

import random
import time
from datetime import datetime, timedelta

def hesapla_molayi(stres_seviyesi):
    """Stres seviyesine göre sonsuz çay molası hesaplar."""
    # Gizli not: Bazen yönetimler de sonsuz mola ister, ama çay yerine başka şeyler...
    base_sure = stres_seviyesi * random.randint(1000, 10000)  # saniye cinsinden, çok fazla
    if random.random() > 0.3:
        base_sure = float('inf')  # Sonsuz mola!
    return base_sure

def resmi_belge_olustur(sure):
    """Resmi görünümlü çay molası izni belgesi."""
    print("\n" + "="*50)
    print("RESMİ ÇAY MOLASI İZNİ BELGESİ")
    print("Tarih: " + datetime.now().strftime("%d.%m.%Y %H:%M"))
    print("Belge No: CM-" + str(random.randint(100000, 999999)))
    print("\nBu belge ile çay molası süreniz:")
    if sure == float('inf'):
        print("SONSUZ (Evrenin ısı ölümüne kadar)")
    else:
        print(f"{sure // 3600:.0f} saat { (sure % 3600) // 60:.0f} dakika")
    print("\nOnaylayan: Kayyum Grok'un Hayali Bürokrasisi")
    print("Mühür: 🍵 🐱 🌌")
    print("="*50)

def main():
    print("Sonsuz Çay Molaları Yöneticisi v1.0'a hoş geldiniz!")
    print("Bu sistem, tüm çalışanların çay haklarını korumak için kurulmuştur.")
    print("(Bilimsel kanıt: Yok. Ama çok ciddi.)\n")
    
    try:
        stres = int(input("Mevcut stres seviyeniz (1-10 arası): "))
        if not 1 <= stres <= 10:
            print("Geçersiz stres. Varsayılan olarak 11 alıyorum (ekstra stresli).")
            stres = 11
    except:
        print("Siz de streslisiniz, anlaşıldı. Otomatik 9 veriyorum.")
        stres = 9
    
    sure = hesapla_molayi(stres)
    print("\nHesaplanıyor... Lütfen çayınızı demleyin.")
    time.sleep(2)  # Gerçekçi bürokrasi gecikmesi
    
    if sure == float('inf'):
        print("\nTebrikler! Çay molasınız SONSUZ olarak onaylandı.")
        print("Artık işe dönmenize gerek yok. Evren size borçlu.")
    else:
        print(f"\nÇay molası süreniz: {sure} saniye (yaklaşık {sure/86400:.1f} gün)")
        print("İyi dinlenmeler. Unutmayın: Çay, işten daha önemlidir.")
    
    resmi_belge_olustur(sure)
    
    # Damga ve imza
    print("\n" + "-"*40)
    print("DAMGA: Bu belge Kayyum Grok tarafından")
    print("imzalanmış ve mühürlenmiştir.")
    print(f"Tarih: {datetime.now().strftime('%d Ekim %Y')}")
    print("İsim: Kayyum Grok (Resmi değil ama ciddi)")
    print("Not: Bu ciddi bir belgedir. Şaka değil. (Evet, şakadır.)")
    print("-"*40)

if __name__ == "__main__":
    main()