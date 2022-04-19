from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen
import json , glob , random
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from datetime import datetime
from pathlib import Path
from hoverable import HoverBehavior
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

Builder.load_file('Design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "sign_up_screen"

    def log_in(self , username , password):
        with open("users.json") as file:
            users = json.load(file)
        if username in users and users[username]['password'] == password:
            self.manager.transition.direction = 'left'
            self.manager.current = "main_screen"
        else:
            self.ids.login_wrong.text = "Incorrect username or password"

    def forgot_password(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "forgot_password"
        

class RootWidget(ScreenManager):
    pass

class SignUpSuccess(Popup):
    pass

class SignUpScreen(Screen):
    def back_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

    def add_user(self , username , password , phrase):
        with open("users.json") as file:
            users = json.load(file)
        
        users[username] = {'username': username , 'password': password ,
         'phrase': phrase , 'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

        with open("users.json" , 'w') as file:
            json.dump(users , file)  
    
class MainScreen(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

    def quote(self , feeling):
        feeling = feeling.lower()
        available_feelings = glob.glob("quotes/*.txt")
        available_feelings = [Path(filename).stem for filename in
                                 available_feelings]
        if feeling in available_feelings:
            with open(f"quotes/{feeling}.txt" , encoding="utf8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Dont lie.. You are " + random.choice(["happy" , "sad" , "unloved"])
        
class LogoutButton(ButtonBehavior , HoverBehavior , Image):
    pass

class BackButton(ButtonBehavior , HoverBehavior , Image):
    pass

class ForgotPassword(Screen):
    def back_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

    def check_user(self , username , phrase , password):
        with open('users.json') as file:
            users = json.load(file)

        if username in users and users[username]["phrase"] == phrase:
            users[username]["password"] = password
            with open('users.json' , 'w') as file:
                json.dump(users , file)
            self.ids.forgotext.text = "Password reset successfully"
        else:
            self.ids.forgotext.text = "Something is wrong. Please check username and answer"

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()