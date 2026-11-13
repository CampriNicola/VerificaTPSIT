from pannello import PannelloFotovoltaico
from impianto import ImpiantoSolare

def registra_impianto(impianti: list[ImpiantoSolare], impianto: ImpiantoSolare) -> None:
    for i in impianti:
        if impianto.codice == i.codice:
            raise ValueError("Codice già presente")
        
    impianti.append(impianto)

def cerca_impianto(impianti: list[ImpiantoSolare], codice: str) -> ImpiantoSolare:
    result = None
    for impianto in impianti:
        if codice.lower() == impianto.codice.lower():
            result = impianto
    
    return result

def riepilogo_impianti(nome_azienda: str, impianti: list[ImpiantoSolare]) -> None:
    print(f"Impianti {nome_azienda}: ")
    
    for impianto in impianti:
        print(f"Impianto {impianto.codice} - Modello: {impianto.modello} - Stato: {impianto.stato} - PotenzaPannelli: {impianto.potenza_pannelli()}")
            
 
 
