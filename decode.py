class Decode:
    def __init__(self, codedText : str = "", key : str = ""):
        self.__codedText = codedText
        self.__key = key
        self.__decodedText = ""


    def decode(self):
        self.decodeCesar()
        return self.__decodedText

    
    def decodeCesar(self):
        decodedText = ""

        for i in range(len(self.__codedText)):
            char = self.__codedText[i] # Toma el caracter i

            if ord(char) - self.__key < 32 and chr(ord(char) - self.__key) != '\n': # Comprueba limite de ASCII para evitar errores (espacio), si da el ASCII de salto de linea, no se hace
                char = chr(ord(char) + 95) # El desplazamiento llegará por el límite superior

            char = chr(ord(char) - self.__key) # Convierte el caracter a ascii, realiza el desplazamiento hacia atrás y lo regresa a caracter
            decodedText = decodedText + char

        self.__decodedText = decodedText


    def decodeXor(self):
        print("")