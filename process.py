class Process:
    def encode(self, text):
        data = []
        print("El texto es", text)
        key = "Llave"
        data.append("Texto cifrado")
        data.append(key)
        return data

    def decode(self, key):
        print("La key es", key)
        decodedText = "Todo bien"
        return decodedText
