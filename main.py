import sys
import tkinter
import pyautogui


class MainApp():
    def __init__(self):
        self.root = tkinter.Tk()
        self.now_viwe = "管理"
        self.text_title = f"test - {self.now_viwe}画面"
        self.pos_x, self.pos_y = 80, 50
        self.SCREEN_WIDTH = int((pyautogui.size().width) * 0.3)
        self.SCREEN_HEIGHT = int((pyautogui.size().height) * 0.8)
        
        
        #関数を実行
        self.make_window()
        self.management_view_button()
        self.edit_view_button()
        self.message_view_button()
    
    def make_window(self):
        self.root.title(self.text_title)
        self.root.resizable(False,False)
        self.root.geometry(f"{self.SCREEN_WIDTH}x{self.SCREEN_HEIGHT}+{self.pos_x}+{self.pos_y}")
    
    def change_title(self, click_button):
        if (self.now_viwe != click_button):
            self.now_viwe = click_button
            self.root.title(f"test - {self.now_viwe}画面")
    
    def management_view_button(self):
        management_button = tkinter.Button(text="管理", font=("MSゴシック", 12, "bold"), command=lambda: self.change_title("管理"))
        management_button.place(x=0, y=(self.SCREEN_HEIGHT - (self.SCREEN_HEIGHT * 0.12)), width=(self.SCREEN_WIDTH // 3),height=int(self.SCREEN_HEIGHT * 0.07))
    
    def edit_view_button(self):
        management_button = tkinter.Button(text="編集", font=("MSゴシック", 12, "bold"), command=lambda: self.change_title("編集"))
        management_button.place(x=(self.SCREEN_WIDTH // 3), y=(self.SCREEN_HEIGHT - (self.SCREEN_HEIGHT * 0.12)), width=(self.SCREEN_WIDTH // 3),height=int(self.SCREEN_HEIGHT * 0.07))
    
    def message_view_button(self):
        management_button = tkinter.Button(text="通知", font=("MSゴシック", 12, "bold"), command=lambda: self.change_title("通知"))
        management_button.place(x=(self.SCREEN_WIDTH // 3)*2, y=(self.SCREEN_HEIGHT - (self.SCREEN_HEIGHT * 0.12)), width=(self.SCREEN_WIDTH // 3),height=int(self.SCREEN_HEIGHT * 0.07))
    
    def run(self):
        self.root.mainloop()


app = MainApp()
app.run()
