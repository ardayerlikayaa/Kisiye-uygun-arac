# %%
import tkinter as tk
from PIL import Image, ImageTk

kullanici_bilgileri = {}


araba_gorselleri = {
    "BMW M4 Competition": r"C:\Users\VICTUS\Desktop\python_projesi\resimler\bmwM4.webp",
    "Honda Civic Type R 2024": r"C:\Users\VICTUS\Desktop\python_projesi\resimler\hondacivictyper.webp",
    "Volvo XC90": r"C:\Users\VICTUS\Desktop\python_projesi\resimler\VOLVOXC90.webp",
    "Mercedes S500 Long": r"C:\Users\VICTUS\Desktop\python_projesi\resimler\mercedesS500long.webp",
    "Mercedes E180 2022": r"C:\Users\VICTUS\Desktop\python_projesi\resimler\MercedesE180.webp",
    "Honda Civic 2021": r"C:\Users\VICTUS\Desktop\python_projesi\resimler\HondacivicFE1.webp"
}

root = tk.Tk()
root.geometry("600x700")
root.title("Araç Önerici")
root.configure(bg="#34495e")

frames = {}
for i in range(6):
    frame = tk.Frame(root, bg="#34495e")
    frame.place(relwidth=1, relheight=1)
    frames[i] = frame

def show_frame(page):
    frames[page].tkraise()  
def page0():
    frame = frames[0]
    for w in frame.winfo_children():
        w.destroy()
    tk.Label(frame, text="Yaşınızı Giriniz:", font=("Helvetica", 16), bg="#34495e", fg="white").pack(pady=20)
    yas_entry = tk.Entry(frame, font=("Helvetica", 14))
    yas_entry.pack(pady=10)
    hata_label = tk.Label(frame, text="", fg="red", bg="#34495e")
    hata_label.pack()

    def ileri():
        try:
            yas = int(yas_entry.get())
            if yas < 0 or yas > 120:
                raise ValueError
            kullanici_bilgileri["yas"] = yas
            page1()
            show_frame(1)
        except:
            hata_label.config(text="Geçerli bir yaş giriniz!")

    tk.Button(frame, text="İleri", command=ileri, bg="#27ae60", fg="white", font=("Helvetica", 14)).pack(pady=20)

def page1():
    frame = frames[1]
    for w in frame.winfo_children():
        w.destroy()
    tk.Label(frame, text="Kilonuzu Giriniz (kg):", font=("Helvetica", 16), bg="#34495e", fg="white").pack(pady=20)
    kilo_entry = tk.Entry(frame, font=("Helvetica", 14))
    kilo_entry.pack(pady=10)
    hata_label = tk.Label(frame, text="", fg="black", bg="#34495e")
    hata_label.pack()

    def ileri():
        try:
            kilo = int(kilo_entry.get())
            if kilo < 20 or kilo > 300:
                raise ValueError
            kullanici_bilgileri["kilo"] = kilo
            page2()
            show_frame(2)
        except:
            hata_label.config(text="Geçerli bir kilo giriniz!")

    def geri():
        show_frame(0)

    tk.Button(frame, text="Geri", command=geri, bg="#e67e22", fg="white", font=("Helvetica", 14)).pack(side="left", padx=40, pady=20)
    tk.Button(frame, text="İleri", command=ileri, bg="#27ae60", fg="white", font=("Helvetica", 14)).pack(side="right", padx=40, pady=20)

def page2():
    frame = frames[2]
    for w in frame.winfo_children():
        w.destroy()
    tk.Label(frame, text="Boyunuzu Giriniz (metre):", font=("Helvetica", 16), bg="#34495e", fg="white").pack(pady=20)
    boy_entry = tk.Entry(frame, font=("Helvetica", 14))
    boy_entry.pack(pady=10)
    hata_label = tk.Label(frame, text="", fg="red", bg="#34495e")
    hata_label.pack()

    def ileri():
        try:
            boy = float(boy_entry.get())
            if boy < 1.0 or boy > 2.5:
                raise ValueError
            kullanici_bilgileri["boy"] = boy
            page3()
            show_frame(3)
        except:
            hata_label.config(text="Geçerli bir boy giriniz(örn:1.80)")

    def geri():
        show_frame(1)

    tk.Button(frame, text="Geri", command=geri, bg="#e67e22", fg="white", font=("Helvetica", 14)).pack(side="left", padx=40, pady=20)
    tk.Button(frame, text="İleri", command=ileri, bg="#27ae60", fg="white", font=("Helvetica", 14)).pack(side="right", padx=40, pady=20)

def page3():
    frame = frames[3]
    for w in frame.winfo_children():
        w.destroy()
    tk.Label(frame, text="Hız mı Konfor mu", font=("Helvetica", 16), bg="#34495e", fg="white").pack(pady=20)
    tercih_var = tk.StringVar(value="Hız")
    tk.Radiobutton(frame, text="Hız", variable=tercih_var, value="Hız", bg="#34495e", fg="white", font=("Helvetica", 14), selectcolor="#2ecc71").pack(pady=5)
    tk.Radiobutton(frame, text="Konfor", variable=tercih_var, value="Konfor", bg="#34495e", fg="white", font=("Helvetica", 14), selectcolor="#2ecc71").pack(pady=5)

    def ileri():
        kullanici_bilgileri["tercih"] = tercih_var.get()
        page4()
        show_frame(4)

    def geri():
        show_frame(2)

    tk.Button(frame, text="Geri", command=geri, bg="#e67e22", fg="white", font=("Helvetica", 14)).pack(side="left", padx=40, pady=20)
    tk.Button(frame, text="İleri", command=ileri, bg="#27ae60", fg="white", font=("Helvetica", 14)).pack(side="right", padx=40, pady=20)

def page4():
    frame = frames[4]
    for w in frame.winfo_children():
        w.destroy()
    tk.Label(frame, text="Aracı günlük kullanım için mi yoksa keyif için mi kullanacaksınız?", font=("Helvetica", 14), bg="#34495e", fg="white", wraplength=500).pack(pady=20)
    kullanam_var = tk.StringVar(value="Keyfi")
    tk.Radiobutton(frame, text="Günlük", variable=kullanam_var, value="Günlük", bg="#34495e", fg="white", font=("Helvetica", 14), selectcolor="#2ecc71").pack(pady=5)
    tk.Radiobutton(frame, text="Keyfi", variable=kullanam_var, value="Keyfi", bg="#34495e", fg="white", font=("Helvetica", 14), selectcolor="#2ecc71").pack(pady=5)

    def ileri():
        kullanici_bilgileri["kullanim"] = kullanam_var.get()
        page5()
        show_frame(5)

    def geri():
        show_frame(3)

    tk.Button(frame, text="Geri", command=geri, bg="#e67e22", fg="white", font=("Helvetica", 14)).pack(side="left", padx=40, pady=20)
    tk.Button(frame, text="İleri", command=ileri, bg="#27ae60", fg="white", font=("Helvetica", 14)).pack(side="right", padx=40, pady=20)

def page5():
    frame = frames[5]
    for w in frame.winfo_children():
        w.destroy()

    yas = kullanici_bilgileri.get("yas")
    kilo = kullanici_bilgileri.get("kilo")
    boy = kullanici_bilgileri.get("boy")
    tercih = kullanici_bilgileri.get("tercih")
    kullanim = kullanici_bilgileri.get("kullanim")

    arac_adi = ""

    if tercih == "Hız":
        if yas < 25:
            arac_adi = "BMW M4 Competition"
        elif 25 <= yas <= 40:
            arac_adi = "Honda Civic Type R 2024"
        else:
            arac_adi = "Mercedes S500 Long"
    else:
        if yas < 25:
            arac_adi = "Honda Civic 2021"
        elif 25 <= yas <= 40:
            arac_adi = "Mercedes E180"
        else:
            arac_adi = "Volvo XC90"

    tk.Label(frame, text=f"ÖNERİLEN MODEL:: {arac_adi}", font=("Helvetica", 20), fg="white", bg="#34495e").pack(pady=20)

    try:
        img = Image.open(araba_gorselleri[arac_adi])
        img = img.resize((450, 270))
        img_tk = ImageTk.PhotoImage(img)
        img_label = tk.Label(frame, image=img_tk, bg="#34495e")
        img_label.image = img_tk
        img_label.pack(pady=10)
    except Exception as e:
        tk.Label(frame, text=f"Görsel yükleme hatası:\n{e}", fg="black", bg="#34495e").pack(pady=10)

    def tekrar():
        page0()
        show_frame(0)

    tk.Button(frame, text="Tekrar Dene", command=tekrar, bg="#2980b9", fg="white", font=("Helvetica", 14)).pack(pady=20)

page0()
show_frame(0)

root.mainloop()


# %%



