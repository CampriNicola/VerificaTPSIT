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
            
 
# TEST MAIN
impianti: list[ImpiantoSolare] = []
registra_impianto(impianti, ImpiantoSolare("AAA", "Aurora", "Bologna", 400, "OK"))
registra_impianto(impianti, ImpiantoSolare("AAB", "Mod", "Torino", 900, "Da installare"))
registra_impianto(impianti, ImpiantoSolare("AAC", "Boh", "Napoli", 100, "Fuori servizio"))
registra_impianto(impianti, ImpiantoSolare("AAD", "Auorora", "Bologna", 500, "OK"))

impianti[0].aggiungi_pannello(PannelloFotovoltaico("1A", "Aurora", 10))
impianti[0].aggiungi_pannello(PannelloFotovoltaico("1B", "Aurora", 50))
impianti[1].aggiungi_pannello(PannelloFotovoltaico("2A", "NuovoMod", 50))
impianti[1].aggiungi_pannello(PannelloFotovoltaico("2B", "Aurora", 50))
impianti[2].aggiungi_pannello(PannelloFotovoltaico("3A", "BiMod", 5))
impianti[2].aggiungi_pannello(PannelloFotovoltaico("3B", "FA2", 40))
impianti[3].aggiungi_pannello(PannelloFotovoltaico("4A", "NuovoMod", 100))
impianti[3].aggiungi_pannello(PannelloFotovoltaico("4B", "Aurora", 50))

riepilogo_impianti("Pascal", impianti)
impianto_trovato = cerca_impianto(impianti, "AAA")
impianto_non_trovato = cerca_impianto(impianti, "B")

print(f"Trovato: {impianto_trovato.codice}")
print(f"{impianto_non_trovato == None }")

pannello_non_trovato = impianto_trovato.cerca_pannello("7A")
print(f"{pannello_non_trovato == None }")