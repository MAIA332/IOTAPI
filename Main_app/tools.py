class Metrics:
    def __init__(self):
        self.p_base = 101325

    def vant_hoff(self,co2_base,rh_estimada,rh_base): # função que calcula um nivel estimado de CO2 no ambiente
        p_estimada = self.p_base
        co2_estimado = co2_base*((self.p_base*(1-rh_estimada))/(p_estimada*(1-rh_base)))
        return co2_estimado
    

a = Metrics()
print(f"Nivel estimado de CO2: {a.vant_hoff(400,0.5,0.3)}")