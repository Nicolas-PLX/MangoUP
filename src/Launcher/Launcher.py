import tkinter as tk
from Launcher.model import Model


class Launcher:
    def __init__(self):
        wd = tk.Tk()
        wd.title("MangoUP")
        
        window_width = 1200
        window_height = 800

        screen_width = wd.winfo_screenwidth()
        screen_height = wd.winfo_screenheight()

        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        wd.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        wd.resizable(False,False)
        wd.iconbitmap('./assets/pp.ico')

        self.wd = wd
        self.model = Model()


    def launch(self):
        main_frame = tk.Frame(self.wd)
        main_frame.pack(fill=tk.BOTH, expand=True)
        #list_manga_text.insert(tk.END,"Pipi")

        top_controls_frame = tk.Frame(main_frame)
        top_controls_frame.pack(side= tk.TOP, fill=tk.X, padx=10,pady=10)

        add_manga_button = tk.Button(top_controls_frame,text="Ajouter",bg="green",width=15)
        add_manga_button.pack(side = tk.LEFT,padx=5,pady=10)

        rm_manga_button = tk.Button(top_controls_frame,text="Supprimer",bg="red",width=15)
        rm_manga_button.pack(side=tk.LEFT,padx=5,pady=10)

        list_manga_frame = tk.Frame(main_frame)
        list_manga_frame.pack(side=tk.LEFT, fill = tk.BOTH,expand=True)

        list_manga_text = tk.Listbox(list_manga_frame,width=40,height=50)
        list_manga_text.pack(side=tk.LEFT, padx=10, pady=10)

        bottom_controls_frame = tk.Frame(main_frame)
        bottom_controls_frame.pack(side=tk.BOTTOM,padx=10,pady=10)

        check_update_button = tk.Button(bottom_controls_frame, text="Check Update !", width=120)
        check_update_button.pack(side=tk.BOTTOM,fill=tk.BOTH, padx=10,pady=10)

        save_button = tk.Button(bottom_controls_frame,text="Sauvegarder",width=60)
        save_button.pack(side=tk.LEFT,padx=10,pady=10)

        load_button = tk.Button(bottom_controls_frame,text="Charger",width=60)
        load_button.pack(side=tk.RIGHT,padx=10,pady=10)

        log_control_frame = tk.Frame(main_frame)
        log_control_frame.pack(side = tk.RIGHT, fill = tk.BOTH, expand=True)

        log_text = tk.Text(log_control_frame, wrap=tk.WORD, width=40)
        log_text.pack(fill=tk.BOTH, expand=True,padx=10,pady=10)


        

        

        self.wd.mainloop()

    
    def ajout_frame(self):
        pass

    def remove_frame(self):
        pass