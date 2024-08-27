from aplications.configs.broker_configs import mqtt_broker_configs


def on_connect(client,userdata,flags,rc):
    if rc == 0:
        print(f'Cliente Conectado com sucesso: {client}')
        client.subscribe(mqtt_broker_configs["TOPIC_TEMP"])
        client.subscribe(mqtt_broker_configs["TOPIC_UMIDADE"])
    else:
        print(f'Erro ao me conectar ! codigo={rc}')

def on_subscribe(client, userdata, mid, granted_qos):
    print(f'Cliente Subscribed at {mqtt_broker_configs["TOPIC_TEMP"]}')
    print(f'Cliente Subscribed at {mqtt_broker_configs["TOPIC_UMIDADE"]}')
    #print(f'QOS: {granted_qos}')


def on_message(client, userdata, message):
    
        print('Mensagem recebida!')
        print(client)
        print(message.payload)
        topico = message.topic
        if(topico == "Temperatura"):
            mqtt_broker_configs['Temperatura'] = message.payload
        if(topico == "Umidade"):
            mqtt_broker_configs['Umidade'] = message.payload
      
        
        