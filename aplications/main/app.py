from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from aplications.configs.broker_configs import mqtt_broker_configs




class Interface(MDFloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)
       
      

    def update(self, *args):
        
        self.ids.inputTemp.text = str(mqtt_broker_configs['MSG'])
       

    

    def publica(self):

       print("funfou!!")

class MI(MDBoxLayout):
    pass


class FirstApp(MDApp):
    pass


def startApp():
   FirstApp().run()


    