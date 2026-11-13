from pannello import PannelloFotovoltaico

class ImpiantoSolare:
    def __init__(self, codice: str, modello: str, localita: str, potenza_massima_kw: float, stato: str) -> None:
        self.codice = codice
        self.modello = modello
        self.localita = localita
        if potenza_massima_kw <= 0:
            raise ValueError("Potenza non valida")
        self.potenza_massima_kw = potenza_massima_kw
        self.stato = stato
        self.pannelli: list[PannelloFotovoltaico] = []
        
    def potenza_pannelli(self) -> float:
        result = 0
        for pannello in self.pannelli:
            result += pannello.potenza_kw
        
        return result
    
    def aggiungi_pannello(self, pannello: PannelloFotovoltaico) -> None:
        for p in self.pannelli:
            if p.codice == pannello.codice:
                raise ValueError("Codice duplicato")
            
        result = 0
        for pannello in self.pannelli:
            result += pannello.potenza_kw
        
        if self.potenza_massima_kw < result + pannello.potenza_kw:
            raise ValueError("Potenza massima superata")
        
        self.pannelli.append(pannello)
    
    
    
    def cerca_pannello(self, codice: str) -> PannelloFotovoltaico:
        result = None
        for pannello in self.pannelli:
            if codice == pannello.codice:
                result = pannello
                
        return result
    
    def rimuovi_pannello(self, codice: str) -> PannelloFotovoltaico:
        result = None
        for pannello in self.pannelli:
            if codice == pannello.codice:
                result = pannello
                self.pannelli.remove(pannello)
        
        return result
    
    def panelli_sotto_potenza(self, potenza_massima: float) -> list[PannelloFotovoltaico]:
        result = []
        for pannello in self.pannelli:
            if pannello.potenza_kw <= potenza_massima:
                result.append(pannello)
                
        return result
        
        
        
        