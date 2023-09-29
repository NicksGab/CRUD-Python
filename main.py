from kivy.app import App       # Importa o aplicativo do Kivy
from kivy.lang import Builder  # Importa o Builder (GUI) do Kivy
import crud


GUI = Builder.load_file('tela.kv')

class Application(App):
    def build(self):
        return GUI    
    

Application().run()