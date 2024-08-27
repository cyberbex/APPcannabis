from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from aplications.configs.broker_configs import mqtt_broker_configs
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty

class Screen_1(MDScreen):

    my_text = StringProperty("D")
    my_text2 = StringProperty("D")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)
       
      
    def update(self, *args):
        
        self.my_text = str(mqtt_broker_configs["Temperatura"])
        self.my_text2 = str(mqtt_broker_configs["Umidade"])
  

"""     def imprimir(self):
       
        self.my_text = "dfgdfgd"
        print(valores.mqtt_broker_configs["MSG"]) """
        
    

class Screen_2(MDScreen):
    my_text2 = StringProperty("D")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)
       
      
    def update(self, *args):
        
        self.my_text2 = str(mqtt_broker_configs["Umidade"])
  
   

class Screen_3(MDScreen):
    pass


class Interface(MDFloatLayout):

    pass
            
    

    def publica(self):

       print("funfou!!")

class MI(MDBoxLayout):
    pass


class FirstApp(MDApp):
    pass


def startApp():
   FirstApp().run()


    