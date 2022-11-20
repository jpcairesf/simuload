from simuload.arch.service import Service
import numpy as np

class Calculator: 
     
    def carga_consumo(self, carga_id: int):
        consumo = np.zeros((24))
        equipamentos = Service().consultar_equip_na_carga(carga_id)
        for equip in equipamentos:
            equip_id = equip[0]
            equip_qtd = equip[2]
            equip_info = Service().consultar_equipamento_id(equip_id,
                                                            structured=True)
            consumo += equip_qtd*equip_info["Uso"]*equip_info["Potencia"]
        return consumo
    
    def curva_consumo(self,curva_id:int):
        consumo = np.zeros((24))
        cargas = Service().consultar_curva_carga(curva_id)
        for carga in cargas:
            carga_qtd = carga[2]
            consumo_carga = self.carga_consumo(carga[0])
            consumo += consumo_carga*carga_qtd
        return consumo
              
    def interpolador(self, consumo, intervalo = 1):
        # :param: intervalo - números de pontos na interpolação
        # Tal que num_pontos = np.ceil(24/intervalo)
        # Exemplo intervalo = 1 num_pontos = 24
        # Exemplo intervalo = 0.25 (15 min) num_pontos = 48
        
        intervalo_horas = np.linspace(0, 23, 24)        
        intervalo_interp = np.linspace(0, 23, int(np.ceil(24/intervalo)))
        consumo_interp = np.interp(intervalo_interp, intervalo_horas, consumo)
        
        return consumo_interp
        
   
if __name__=='__main__':
    import matplotlib.pyplot as plt
    curva_id = 1
    consumo = Calculator().curva_consumo(curva_id)
    
    intervalo = 0.25
    intervalo_horas = np.linspace(0, 23, 24)
    intervalo_interp = np.linspace(0, 23, int(np.ceil(24/intervalo)))
    
    
    a = Calculator().interpolador(consumo, intervalo=intervalo)
    
    plt.plot(intervalo_horas,consumo,'o')
    plt.plot(intervalo_interp, a, '-x')
    plt.show()