from story_data import STORY_GRAPH

class StoryManager:
    def __init__(self):
        self.nodes = STORY_GRAPH
        self.current_node_id = "baslangic"
        self.score = 0
        self.flags = {}
        self.history = []

    def get_current_node(self):
        return self.nodes[self.current_node_id]

    def make_choice(self, option_index):
        node = self.get_current_node()
        if not node.get("options"):
            return None
        
        selected_option = node["options"][option_index]
        
        points = selected_option.get("points", 0)
        self.score += points
        
        flag = selected_option.get("set_flag")
        if flag:
            self.flags[flag] = True
            
        self.history.append({
            "node_id": self.current_node_id,
            "choice_text": selected_option["text"],
            "points_earned": points
        })

        self.current_node_id = selected_option["next_node"]
        
        return self.current_node_id

    def get_report(self):
        """Oyun sonu detaylı rapor oluşturur."""
        report = f"Toplam Puan: {self.score}\n\n"
        report += "--- Sürüş Analizi ---\n"
        
        if self.score >= 90:
            report += "Mükemmel! Trafik kurallarına tam hakimiyet.\n"
        elif self.score >= 60:
             report += "İyi, ancak daha dikkatli olabilirsin.\n"
        elif self.score >= 30:
             report += "Orta seviye. Bazı kuralları gözden geçirmelisin.\n"
        else:
             report += "Tehlikeli! Acil olarak kuralları tekrar etmelisin.\n"

        report += "\n--- Sürüş Hataları ve Öneriler ---\n"
        has_negative = False
        
        negatives = [
            ("risky_driver", "Hızlı ve riskli araç kullanımı tespit edildi."),
            ("aggressive", "Yayalara veya diğer sürücülere karşı agresiflik."),
            ("violation", "Ciddi kural ihlali (Park/Kırmızı Işık/Hız)."),
            ("tired", "Yorgun araç kullanma riski."),
            ("lost_control", "Araç hakimiyeti kaybı."),
            ("panic", "Acil durumlarda panik yapma eğilimi."),
            ("stubborn", "Trafikte inatlaşma."),
            ("wrong_lights", "Yanlış far kullanımı."),
            ("wrong_signal", "Yanlış sinyal kullanımı."),
            ("criminal", "Polis kontrolünden kaçma girişimi."),
            ("suicidal", "Ters yöne girme gibi ölümcül hata."),
            ("blind_drive", "Görüş olmadan sürüş (Kör sürüş)."),
            ("frozen_brake", "Park Halinde Donma Riski (El freni çekildi)."),
            ("irresponsible", "Kış lastiği olmadan yola çıkma.")
        ]

        for flag, msg in negatives:
            if flag in self.flags:
                report += f"- {msg}\n"
                has_negative = True

        if not has_negative:
            report += "Önemli bir hata tespit edilmedi.\n"
            
        return report
