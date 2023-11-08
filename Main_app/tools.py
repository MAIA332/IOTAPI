class Metrics:
    def __init__(self):
        self.p_base = 101325

    def vant_hoff(self,co2_base,rh_estimada,rh_base): # função que calcula um nivel estimado de CO2 no ambiente
        p_estimada = self.p_base
        co2_estimado = co2_base*((self.p_base*(1-rh_estimada))/(p_estimada*(1-rh_base)))
        return co2_estimado
    

class Integrations:
    def __init__(self,ip) :
        self.ip = ip
        self.request = __import__("requests")

    def post(self,route,params):
        route = self.ip + route

    def get(self,route):
        route = self.ip + route
        response = self.request.get(route)
        
        if response:
            return response

class Settings:
    def __init__(self):
        self.json = __import__("json")
        file = open('configs.json')
        self.configs = self.json.load(file)