class Decode:
    def __init__(self, codedText : str = "", key : str = ""):
        self.__codedText = codedText
        self.__key = key
        self.__decodedText = ""


    def decode(self):
        self.decodeXor()
        self.decodeCesar()
        return self.__decodedText

    
    def decodeCesar(self):
        decodedText = ""
        key = int(self.__key[len(self.__key) - 1])

        for i in range(len(self.__codedText)):
            char = self.__codedText[i] # Toma el caracter i

            if ord(char) - key < 32 and chr(ord(char) - key) != '\n': # Comprueba limite de ASCII para evitar errores (espacio), si da el ASCII de salto de linea, no se hace
                char = chr(ord(char) + 95) # El desplazamiento llegará por el límite superior

            char = chr(ord(char) - key) # Convierte el caracter a ascii, realiza el desplazamiento hacia atrás y lo regresa a caracter
            decodedText = decodedText + char

        self.__decodedText = decodedText


    def decodeXor(self):
        codedText = self.__codedText
        decodedText = ""
        key = self.__key
        key = key[:-1]
        self.__key = self.__key[len(self.__key) - 1]
        temp = ""

        for i in range(len(codedText)):
            temp = chr(ord(codedText[i]) ^ ord(key[i]))
            decodedText = decodedText + temp
            temp = ""

        self.__codedText = decodedText
        self.__decodedText = decodedText