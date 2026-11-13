class PannelloFotovoltaico:
    
    def __init__(self, codice: str, modello: str, potenza_kw: float) -> None:
        self.codice = codice
        self.modello = modello
        if potenza_kw < 0:
            raise ValueError("Potenza non può essere negativa")
        self.potenza_kw = potenza_kw
        
    