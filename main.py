import customtkinter as ctk
from story_manager import StoryManager

class TrafficSimulationApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Pencere ayarları
        self.title("Trafik Güvenliği - İnteraktif Simülasyon")
        self.geometry("900x650")
        
        self.story_manager = StoryManager()

        # Arayüz elemanlarını oluştur
        self.create_widgets()
        
        # İlk sahneyi yükle
        self.load_scene()

    def create_widgets(self):
        # Grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1) # Başlık
        self.grid_rowconfigure(1, weight=3) # Metin
        self.grid_rowconfigure(2, weight=2) # Butonlar
        self.grid_rowconfigure(3, weight=0) # Durum

        # Header
        self.header_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
        self.lbl_title = ctk.CTkLabel(self.header_frame, text="Senaryo Başlıyor", font=("Roboto Medium", 22))
        self.lbl_title.pack(pady=10)

        # Content
        self.content_frame = ctk.CTkFrame(self, corner_radius=15, fg_color=("gray80", "gray20"))
        self.content_frame.grid(row=1, column=0, padx=40, pady=10, sticky="nsew")
        self.lbl_description = ctk.CTkLabel(self.content_frame, text="...", font=("Roboto", 18), wraplength=800)
        self.lbl_description.pack(expand=True, padx=30, pady=30)

        # Options Container
        self.options_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.options_frame.grid(row=2, column=0, padx=40, pady=10, sticky="nsew")
        
        self.option_buttons = []

        # Footer
        self.footer_frame = ctk.CTkFrame(self, height=40, corner_radius=0)
        self.footer_frame.grid(row=3, column=0, sticky="ew")
        
        self.lbl_score = ctk.CTkLabel(self.footer_frame, text="Puan: 0", font=("Roboto", 14, "bold"))
        self.lbl_score.pack(side="right", padx=20)
        
        self.lbl_status = ctk.CTkLabel(self.footer_frame, text="Güvenli Sürüş Modu", font=("Roboto", 12))
        self.lbl_status.pack(side="left", padx=20)

    def load_scene(self):
        # Temizle
        for btn in self.option_buttons:
            btn.destroy()
        self.option_buttons.clear()

        node = self.story_manager.get_current_node()
        
        # Puanı güncelle (Her zaman güncel kalsın)
        self.lbl_score.configure(text=f"Puan: {self.story_manager.score}")
        
        # Oyun bitti mi (Final düğümü mü?)
        if node.get("type") == "final":
            self.show_results(node)
            return

        # UI Güncelle
        # Senaryo başlığını belirle
        node_id = self.story_manager.current_node_id
        title = "Senaryo Seçimi"
        
        if node_id.startswith("sehir"):
            title = "Yoğun Şehir İçi Trafiği"
        elif node_id.startswith("gece"):
            title = "Karanlık Gece Yolculuğu"
        elif node_id.startswith("yagmur"):
            title = "Yağmurlu ve Kaygan Yol"
        elif node_id.startswith("kar"):
            title = "Karlı Dağ Geçidi"
            
        self.lbl_title.configure(text=title)
        self.lbl_description.configure(text=node["text"])

        # Butonlar
        for i, option in enumerate(node["options"]):
            btn = ctk.CTkButton(
                self.options_frame,
                text=option["text"],
                font=("Roboto", 16),
                height=60,
                corner_radius=8,
                fg_color="#1f538d", # Default blue
                hover_color="#14375e",
                command=lambda idx=i: self.make_choice(idx)
            )
            btn.pack(pady=8, fill="x")
            self.option_buttons.append(btn)

    def make_choice(self, index):
        self.story_manager.make_choice(index)
        self.load_scene()

    def show_results(self, final_node):
        # Başlık ve Metin
        self.lbl_title.configure(text=final_node.get("title", "Oyun Bitti"))
        
        # Raporu StoryManager'dan al
        report_text = final_node["text"] + "\n\n" + self.story_manager.get_report()
        
        # Renk ayarı (Puana göre)
        score = self.story_manager.score
        color = "green" if score > 50 else "orange" if score > 0 else "red"
        
        self.lbl_description.configure(text=report_text, text_color=color)
        self.lbl_status.configure(text="Simülasyon Tamamlandı")

        # Yeniden Başlat Butonu
        btn_restart = ctk.CTkButton(
            self.options_frame,
            text="Simülasyonu Yeniden Başlat",
            height=60,
            fg_color="green",
            hover_color="darkgreen",
            font=("Roboto", 16, "bold"),
            command=self.restart_game
        )
        btn_restart.pack(pady=20, fill="x")
        self.option_buttons.append(btn_restart)

    def restart_game(self):
        self.story_manager = StoryManager() # Reset
        self.lbl_description.configure(text_color=("black", "white")) # Reset color
        self.load_scene()

if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")
    app = TrafficSimulationApp()
    app.mainloop()
