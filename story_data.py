# --- Story Data (Senaryo Grafı) ---
STORY_GRAPH = {
    "baslangic": {
        "text": "Bugün nasıl bir sürüş deneyimi yaşamak istersin?\nSeçimin tüm simülasyonun koşullarını belirleyecek.",
        "options": [
            {"text": "Yoğun Şehir İçi Trafiği", "next_node": "sehir_baslangic", "points": 0, "set_flag": "mode_city"},
            {"text": "Karanlık Gece Yolculuğu", "next_node": "gece_baslangic", "points": 0, "set_flag": "mode_night"},
            {"text": "Yağmurlu ve Kaygan Yol", "next_node": "yagmur_baslangic", "points": 0, "set_flag": "mode_rain"},
            {"text": "Karlı Dağ Geçidi", "next_node": "kar_baslangic", "points": 0, "set_flag": "mode_snow"}
        ]
    },
    
    # ---------------------------------------------------------
    # --- YOL 1: ŞEHİR İÇİ (City) - 10 ADIM ---
    # ---------------------------------------------------------
    "sehir_baslangic": {
        "text": "Şehir trafiğine girdin. İlk ışıklara yaklaşırken trafik yavaşladı ve ışık sarı yandı. Durursan arkandaki korna çalabilir.",
        "options": [
            {"text": "Hızlan ve kırmızı yanmadan geçmeye çalış", "next_node": "sehir_serit", "points": 0, "set_flag": "risky_driver"},
            {"text": "Yavaşla ve durma çizgisinde dur", "next_node": "sehir_serit", "points": 10, "set_flag": "cautious"}
        ]
    },
    "sehir_serit": {
        "text": "Trafik biraz açıldı ama senin şeridin yavaş akıyor. Yan şerit boş görünüyor.",
        "options": [
            {"text": "Aniden direksiyonu kırıp yan şeride geç", "next_node": "sehir_kavsak", "points": 0, "set_flag": "aggressive"},
            {"text": "Sinyal ver, ayna kontrolü yap ve müsaitse geç", "next_node": "sehir_kavsak", "points": 10, "set_flag": "cautious"}
        ]
    },
    "sehir_kavsak": {
        "text": "Kontrolsüz bir kavşağa geldin. Sağdaki yoldan 'Yol Ver' tabelasına rağmen bir araç burnunu çıkardı.",
        "options": [
            {"text": "Yol hakkı benim, kornaya basıp geç", "next_node": "sehir_okul", "points": 0, "set_flag": "aggressive"},
            {"text": "Hız kes, gerekirse dur ve ona yol ver", "next_node": "sehir_okul", "points": 10, "set_flag": "respectful"}
        ]
    },
    "sehir_okul": {
        "text": "Okul bölgesine yaklaştın. Hız sınırı tabelası 30 km/s gösteriyor ama diğer araçlar 50 ile gidiyor.",
        "options": [
            {"text": "Trafiğin akışına uy, 50 ile devam et", "next_node": "sehir_ambulans", "points": 0, "set_flag": "violation"},
            {"text": "Hızını 30'a düşür ve dikkatli ol", "next_node": "sehir_ambulans", "points": 10, "set_flag": "respectful"}
        ]
    },
    "sehir_ambulans": {
        "text": "Arkadan siren sesleri geliyor. Bir ambulans trafiğin içinde ilerlemeye çalışıyor.",
        "options": [
            {"text": "Müzik sesini aç ve yoluna devam et", "next_node": "sehir_cop_kamyonu", "points": 0, "set_flag": "aggressive"},
            {"text": "Fermuar sistemiyle sağa/sola yanaşarak yol aç", "next_node": "sehir_cop_kamyonu", "points": 10, "set_flag": "good_citizen"}
        ]
    },
    "sehir_cop_kamyonu": {
        "text": "Önünde bir çöp kamyonu durdu ve yolu tıkadı. Karşı şeritten araçlar geliyor.",
        "options": [
            {"text": "Sabırsızlanıp karşı şeride geçerek solla", "next_node": "sehir_bisikletli", "points": 0, "set_flag": "risky_driver"},
            {"text": "Kamyonun hareket etmesini bekle", "next_node": "sehir_bisikletli", "points": 10, "set_flag": "patient"}
        ]
    },
    "sehir_bisikletli": {
        "text": "Sağ şeritte ilerleyen bir bisikletli var. Yol biraz dar.",
        "options": [
            {"text": "Korna çalarak kenara çekilmesini iste", "next_node": "sehir_yaya", "points": 0, "set_flag": "aggressive"},
            {"text": "Güvenli takip mesafesi bırak, sollama için uygun anı bekle", "next_node": "sehir_yaya", "points": 10, "set_flag": "respectful"}
        ]
    },
    "sehir_yaya": {
        "text": "Işıksız bir yaya geçidine yaklaşıyorsun. Bir yaya telefonuna bakarak yola adım attı.",
        "options": [
            {"text": "Fren yap ve dur, geçmesini bekle", "next_node": "sehir_okul_cikis", "points": 10, "set_flag": "respectful"},
            {"text": "Hız kesmeden geç, yaya beklesin", "next_node": "sehir_okul_cikis", "points": 0, "set_flag": "risky_driver"}
        ]
    },
    "sehir_okul_cikis": {
        "text": "Ara sokaktan aniden yola bir çocuk fırladı! Topunun peşinden koşuyor.",
        "options": [
            {"text": "Refleksle direksiyonu kır", "next_node": "sehir_park", "points": 0, "set_flag": "panic"},
            {"text": "Ani fren yap ve dur", "next_node": "sehir_park", "points": 10, "set_flag": "expert_reflex"}
        ]
    },
    "sehir_park": {
        "text": "Varış noktana geldin. Boş bir yer arıyorsun. Engelli park yeri ve otobüs durağı boş.",
        "options": [
            {"text": "Biraz uzağa, yasal park alanına park et ve yürü", "next_node": "son_kahraman", "points": 10, "set_flag": "good_citizen"},
            {"text": "Dörtlüleri yakıp otobüs durağına park et, hemen döneceksin", "next_node": "son_ceza", "points": 0, "set_flag": "violation"}
        ]
    },

    # ---------------------------------------------------------
    # --- YOL 2: GECE YOLCULUĞU (Night) - 10 ADIM ---
    # ---------------------------------------------------------
    "gece_baslangic": {
        "text": "Hava karardı. Yola çıkmadan önce kontrol etmen gereken bir şey var mı?",
        "options": [
            {"text": "Motoru çalıştır ve hemen yola koyul", "next_node": "gece_otoyol", "points": 0, "set_flag": "risky_driver"},
            {"text": "Tüm farları, stopları ve aynaları kontrol et", "next_node": "gece_otoyol", "points": 10, "set_flag": "cautious"}
        ]
    },
    "gece_otoyol": {
        "text": "Otoyola bağlantı yolundasın. Ana yoldaki trafik hızlı akıyor.",
        "options": [
            {"text": "Hızlanma şeridinin sonuna kadar hızlanıp güvenle katıl", "next_node": "gece_polis", "points": 10, "set_flag": "expert_reflex"},
            {"text": "Erkenden yola dal, onlar yavaşlasın", "next_node": "gece_polis", "points": 0, "set_flag": "aggressive"}
        ]
    },
    "gece_polis": {
        "text": "İleride polis çevirmesi var. Polis el feneriyle durmanı işaret ediyor.",
        "options": [
            {"text": "Dur, camı aç, iç aydınlatmayı yak ve bekle", "next_node": "gece_yorgunluk", "points": 10, "set_flag": "respectful"},
            {"text": " Görmezden gelip yavaşça geçmeye çalış", "next_node": "gece_yorgunluk", "points": 0, "set_flag": "criminal"}
        ]
    },
    "gece_yorgunluk": {
        "text": "Yolculuğun 2. saati. Gözlerin dalmaya, şerit çizgileri oynamaya başladı.",
        "options": [
            {"text": "Camı aç, müziği son ses yap ve devam et", "next_node": "gece_sis", "points": 0, "set_flag": "tired"},
            {"text": "İlk tesiste dur, kahve iç ve 15 dakika uyu", "next_node": "gece_sis", "points": 10, "set_flag": "rested"}
        ]
    },
    "gece_sis": {
        "text": "Yolda aniden lokal bir sis tabakasına girdin. Görüş düştü.",
        "options": [
            {"text": "Dörtlüleri yak ve yavaşla", "next_node": "gece_takipci", "points": 0, "set_flag": "wrong_signal"},
            {"text": "Sis farlarını yak ve hızını düşür", "next_node": "gece_takipci", "points": 10, "set_flag": "cautious"}
        ]
    },
    "gece_takipci": {
        "text": "Arkana bir araç yapıştı ve sürekli selektör yapıyor. Seni taciz ediyor.",
        "options": [
            {"text": "Fren testi yap (aniden frene bas) korksun", "next_node": "gece_uzunfar", "points": 0, "set_flag": "aggressive"},
            {"text": "Sakinliğini koru, sağ şeride geç ve yol ver", "next_node": "gece_uzunfar", "points": 10, "set_flag": "cautious"}
        ]
    },
    "gece_uzunfar": {
        "text": "Karşı şeritten bir araç geliyor. Farları çok parlak (uzunları açık).",
        "options": [
            {"text": "Sen de uzunları yakıp ona karşılık ver (Kör dövüşü)", "next_node": "gece_tekyon", "points": 0, "set_flag": "stubborn"},
            {"text": "Kısa farlarla devam et, bakışlarını yolun sağ çizgisine odakla", "next_node": "gece_tekyon", "points": 10, "set_flag": "expert_reflex"}
        ]
    },
    "gece_tekyon": {
        "text": "Bölünmüş yolda karşı şeritten (senin şeridinden) üstüne gelen bir araç var! Ters yöne girmiş.",
        "options": [
            {"text": "Selektör yap ve üstüne sür", "next_node": "gece_viraj", "points": 0, "set_flag": "suicidal"},
            {"text": "Sağa, emniyet şeridine doğru kaç ve yavaşla", "next_node": "gece_viraj", "points": 10, "set_flag": "expert_reflex"}
        ]
    },
    "gece_viraj": {
        "text": "Önünde keskin bir viraj ve 'Gizli Buzlanma' tabelası var.",
        "options": [
            {"text": "Viraja girmeden önce yavaşla", "next_node": "gece_hayvan", "points": 10, "set_flag": "cautious"},
            {"text": "Virajın içinde fren yaparım", "next_node": "gece_hayvan", "points": 0, "set_flag": "lost_control"}
        ]
    },
    "gece_hayvan": {
        "text": "Aniden yola bir yaban domuzu fırladı! Mesafe çok kısa.",
        "options": [
            {"text": "Direksiyonu aniden kır", "next_node": "son_kaza_kontrol", "points": 0, "set_flag": "panic"},
            {"text": "Direksiyonu sıkı tut ve tam güç fren yap", "next_node": "son_kahraman", "points": 10, "set_flag": "expert_reflex"}
        ]
    },

    # ---------------------------------------------------------
    # --- YOL 3: YAĞMURLU/ZORLU HAVA (Rain) - 10 ADIM ---
    # ---------------------------------------------------------
    "yagmur_baslangic": {
        "text": "Dışarıda sağanak yağmur var. Yola çıkmadan önce lastiklerini kontrol ettin mi?",
        "options": [
            {"text": "Lastiklerim biraz eski ama idare eder", "next_node": "yagmur_ruzgar", "points": 0, "set_flag": "risky_driver"},
            {"text": "Diş derinlikleri iyi, havaları tam. Yola hazırım.", "next_node": "yagmur_ruzgar", "points": 10, "set_flag": "cautious"}
        ]
    },
    "yagmur_ruzgar": {
        "text": "Yüksek bir viyadükten geçerken şiddetli yan rüzgar aracı sarsıyor.",
        "options": [
            {"text": "Hızını koru, direksiyonu rüzgarın tersine çevir", "next_node": "yagmur_surus", "points": 0, "set_flag": "risky_driver"},
            {"text": "Yavaşla ve direksiyonu iki elle sıkıca tut", "next_node": "yagmur_surus", "points": 10, "set_flag": "cautious"}
        ]
    },
    "yagmur_surus": {
        "text": "Yağmur hızlandı. Silecekler en hızlı modda bile zorlanıyor.",
        "options": [
            {"text": "Önündeki aracı yakın takip et ki izinden gidebilesin", "next_node": "yagmur_kamyon", "points": 0, "set_flag": "risky_driver"},
            {"text": "Takip mesafesini normalin iki katına çıkar", "next_node": "yagmur_kamyon", "points": 10, "set_flag": "safe_distance"}
        ]
    },
    "yagmur_kamyon": {
        "text": "Yanından geçen bir TIR, bütün suyu ön camına sıçrattı. Bir anlık kör oldun.",
        "options": [
            {"text": "Panikle frene asıl", "next_node": "yagmur_camur", "points": 0, "set_flag": "panic"},
            {"text": "Ayağını gazdan çek, sileceklerin temizlemesini bekle, direksiyonu düz tut", "next_node": "yagmur_camur", "points": 10, "set_flag": "expert_reflex"}
        ]
    },
    "yagmur_camur": {
        "text": "Yan yoldan ana yola çamur akmış. Zemin çok kaygan görünüyor.",
        "options": [
            {"text": "Üzerinden hızlıca geç", "next_node": "yagmur_su_birikintisi", "points": 0, "set_flag": "risky_driver"},
            {"text": "Hızını iyice düşür, ani hareketlerden kaçın", "next_node": "yagmur_su_birikintisi", "points": 10, "set_flag": "cautious"}
        ]
    },
    "yagmur_su_birikintisi": {
        "text": "Yolun sağında büyük bir su birikintisi (gölet) var. Hızın 80 km/s.",
        "options": [
            {"text": "Sudan kaçmak için aniden sol şeride atla", "next_node": "yagmur_kizaklama", "points": 0, "set_flag": "risky_driver"},
            {"text": "Hızını düşür, direksiyonu sıkı tut ve sudan geç", "next_node": "yagmur_kizaklama", "points": 10, "set_flag": "cautious"}
        ]
    },
    "yagmur_kizaklama": {
        "text": "Suya girdin ve araç 'Kızaklamaya' (Aquaplaning) başladı. Tekerleklerin yerle teması kesildi.",
        "options": [
            {"text": "Frene bas ve direksiyonu çevir", "next_node": "son_kaza_kontrol_yagmur", "points": 0, "set_flag": "lost_control"},
            {"text": "Gazdan ayağını çek, fren yapma, tekerleklerin yolu tutmasını bekle", "next_node": "yagmur_kopru", "points": 10, "set_flag": "master_driver"}
        ]
    },
    "yagmur_kopru": {
        "text": "Bir köprüye yaklaşıyorsun. Hava derecesi 0'a yakın. Gizli buzlanma olabilir.",
        "options": [
            {"text": "Köprüde gaza basarak çabuk geç", "next_node": "yagmur_sis", "points": 0, "set_flag": "risky_driver"},
            {"text": "Gazı kes, frene dokunmadan süzülerek geç", "next_node": "yagmur_sis", "points": 10, "set_flag": "cautious"}
        ]
    },
    "yagmur_sis": {
        "text": "Yağmur dindi ama yerini yoğun bir sis aldı. Görüş mesafesi 20 metre.",
        "options": [
            {"text": "Uzun farları yak ki önünü daha iyi gör", "next_node": "yagmur_final", "points": 0, "set_flag": "wrong_lights"},
            {"text": "Sis farlarını ve kısalari yak, takip mesafesini arttır", "next_node": "yagmur_final", "points": 10, "set_flag": "correct_fog"}
        ]
    },
    "yagmur_final": {
        "text": "Sisten kurtuldun. Varış noktana az kaldı ama yol hala kaygan.",
        "options": [
            {"text": "Artık tehlike geçti, normal hıza dön", "next_node": "son_kahraman", "points": 0, "set_flag": None},
            {"text": "Tedbiri elden bırakma, temkinli sürüşe devam et", "next_node": "son_kahraman", "points": 10, "set_flag": "cautious"}
        ]
    },

    # ---------------------------------------------------------
    # --- YOL 4: KARLI DAĞ YOLU (Snow) - 10 ADIM ---
    # ---------------------------------------------------------
    "kar_baslangic": {
        "text": "Uludağ'a doğru yola çıkıyorsun. Mevsim kış, kar yağışı başladı. Aracında kış lastiği var mı?",
        "options": [
            {"text": "Yaz lastikleri var ama ben usta şoförüm", "next_node": "kar_zincir", "points": 0, "set_flag": "irresponsible"},
            {"text": "Evet, kış lastiklerim takılı ve bagajda zincir var", "next_node": "kar_zincir", "points": 10, "set_flag": "equipped"}
        ]
    },
    "kar_zincir": {
        "text": "Jandarma kontrol noktası. 'Zincirsiz çıkış yasak' tabelası var. Yol bembeyaz.",
        "options": [
            {"text": "Jandarmaya görünmeden kaçıp devam et", "next_node": "son_ceza", "points": 0, "set_flag": "violation"},
            {"text": "Kenara çekip zincirlerini tak (veya zaten takılıysa kontrol et)", "next_node": "kar_yokus", "points": 10, "set_flag": "cautious"}
        ]
    },
    "kar_yokus": {
        "text": "Dik bir yokuşu tırmanıyorsun. Tekerler patinaja düşmeye başladı.",
        "options": [
            {"text": "Gaza köklen, patinajla çıkarsın", "next_node": "kar_inis", "points": 0, "set_flag": "stuck"},
            {"text": "Yarım gazla, düşük devirde kararlı şekilde tırman", "next_node": "kar_inis", "points": 10, "set_flag": "master_driver"}
        ]
    },
    "kar_inis": {
        "text": "Zirveyi geçtin, şimdi dik bir iniş var. Yerler tamamen buz.",
        "options": [
            {"text": "Sürekli frene basarak in", "next_node": "kar_buz", "points": 0, "set_flag": "slider"},
            {"text": "Vitesi küçült, motor freniyle in (Kompresör)", "next_node": "kar_buz", "points": 10, "set_flag": "expert_reflex"}
        ]
    },
    "kar_buz": {
        "text": "Gölgedeki bir virajda 'Siyah Buz' (Görünmez buzlanma) var. Araç kaymaya başladı.",
        "options": [
            {"text": "Frene asıl!", "next_node": "son_kaza_kontrol", "points": 0, "set_flag": "lost_control"},
            {"text": "Freni bırak, direksiyonu kayan yöne çevir (Kontra)", "next_node": "kar_tipi", "points": 10, "set_flag": "rally_driver"}
        ]
    },
    "kar_tipi": {
        "text": "Aniden tipi bastırdı. Göz gözü görmüyor. Silecekler dondu.",
        "options": [
            {"text": "Durmak tehlikeli, rastgele ilerle", "next_node": "kar_viraj", "points": 0, "set_flag": "blind_drive"},
            {"text": "Kaloriferi cama ver, mümkünse güvenli bir cepte bekle", "next_node": "kar_viraj", "points": 10, "set_flag": "cautious"}
        ]
    },
    "kar_viraj": {
        "text": "Tipide önünü zor görüyorsun, keskin bir viraj geldi.",
        "options": [
            {"text": "Virajı içeriden alıp yolu kısalt", "next_node": "kar_engel", "points": 0, "set_flag": "wrong_lane"},
            {"text": "Kendi şeridinden yavaşça dön, korna çal", "next_node": "kar_engel", "points": 10, "set_flag": "cautious"}
        ]
    },
    "kar_engel": {
        "text": "Yolun ortasında kara saplanmış bir araç var!",
        "options": [
            {"text": "Son anda direksiyonu kır", "next_node": "kar_takip", "points": 0, "set_flag": "risk"},
            {"text": "Önceden yavaşladığın için sakince dur ve yardım et", "next_node": "kar_takip", "points": 10, "set_flag": "helper"}
        ]
    },
    "kar_takip": {
        "text": "Önünde kar küreme aracı gidiyor. Tuz serpiyor.",
        "options": [
            {"text": "Çok yavaş gidiyor, hemen solla", "next_node": "kar_varis", "points": 0, "set_flag": "impatient"},
            {"text": "Onu takip et, açtığı yoldan gitmek en güvenlisi", "next_node": "kar_varis", "points": 10, "set_flag": "smart"}
        ]
    },
    "kar_varis": {
        "text": "Otele vardın. Park yeri karla kaplı.",
        "options": [
            {"text": "Hemen el frenini çekip park et", "next_node": "son_kahraman", "points": 0, "set_flag": "frozen_brake"},
            {"text": "Vitesi 'Viteste' (veya P'de) bırak, el frenini çekme (donabilir), silecekleri kaldır", "next_node": "son_kahraman", "points": 10, "set_flag": "winter_expert"}
        ]
    },
    
    # --- ARA DÜĞÜMLER ---
    "son_kaza_kontrol": {
        "text": "Aracın kontrolünü kaybettin...",
        "options": [
             {"text": "Sonucu Gör", "next_node": "son_kaza", "points": 0, "set_flag": None}
        ]
    },
    "son_kaza_kontrol_yagmur": {
        "text": "Araç suyun üzerinde kayarak yoldan çıktı...",
        "options": [
             {"text": "Sonucu Gör", "next_node": "son_kaza", "points": 0, "set_flag": None}
        ]
    },

    # --- FİNALLER ---
    "son_kahraman": {
        "text": "Tebrikler! Zorlu koşullara rağmen yolculuğu sağ salim tamamladın.\nGerçek bir trafik uzmanı gibi davrandın.", 
        "options": [], "type": "final", "title": "SÜRÜŞ RAPORU: USTA ŞOFÖR"
    },
    "son_kaza": {
        "text": "Maalesef kaza yaptın.\nSimülasyon, hatalarını görmen için sonlandırıldı. Lütfen kuralları gözden geçir.",
        "options": [], "type": "final", "title": "SÜRÜŞ RAPORU: KAZA"
    },
    "son_ceza": {
        "text": "Yolculuk bitti ama trafik kurallarını ihlal ettiğin için ağır ceza puanları aldın.\nEhliyetin tehlikede olabilir.",
        "options": [], "type": "final", "title": "SÜRÜŞ RAPORU: CEZALI SÜRÜCÜ"
    }
}
