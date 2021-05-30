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
            char = self.__codedText[i]

            if ord(char) - self.__key < 32: # Limite de ASCII para evitar errores ( )
                char = chr(ord(char) + 95)

            char = chr(ord(char) - self.__key)
            decodedText = decodedText + char

        print(decodedText)
        self.__decodedText = decodedText


    def decodeXor(self):
        print("")