from aplications.configs.broker_configs import mqtt_broker_configs
from .mqtt_connection.mqtt_client_connection import MqttClientConnection
import time
from aplications.main.app import startApp

def start():
    mqtt_client_connection = MqttClientConnection(
        mqtt_broker_configs["HOST"],
        mqtt_broker_configs["PORT"],
        mqtt_broker_configs["CLIENT_NAME"],
        mqtt_broker_configs["KEPPALIVE"],
        mqtt_broker_configs["USERNAME"],
        mqtt_broker_configs["PASSWORD"]

    )
 
    mqtt_client_connection.start_connection()
    startApp()
    #while True: time.sleep(0.001)

    