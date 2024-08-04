from paho.mqtt import client as mqtt_client
from .callbacks import on_connect, on_message, on_subscribe


class MqttClientConnection:
    def __init__(self, broker_ip:str,port: int, client_name: str, Keepalive=60,name=str, password=str):
        self.__broker_ip = broker_ip
        self.__port = port
        self.__client_name = client_name
        self.__keepalive = Keepalive
        self.__username = name
        self.__password = password



    def start_connection(self):
            client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1)
            client.on_connect = on_connect
            client.on_subscribe = on_subscribe
            client.on_message =on_message
            client.connect(host=self.__broker_ip,port=self.__port,keepalive=self.__keepalive)
            client.username_pw_set(self.__username, self.__password)
            client.loop_start()
