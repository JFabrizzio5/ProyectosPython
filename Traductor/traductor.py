from googletrans import Translator

def traductor(texto, destino='en'):
    # Crear una instancia del traductor
    translator = Translator()

    try:
        # Detectar el idioma del texto de origen
        idioma_detectado = translator.detect(texto).lang

        # Traducir el texto al idioma de destino
        traduccion = translator.translate(texto, src=idioma_detectado, dest=destino)
        
        # Imprimir la traducción
        print(f'Texto original ({idioma_detectado}): {texto}')
        print(f'Traducción ({destino}): {traduccion.text}')
    
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    texto_a_traducir = input("Introduce el texto que quieres traducir: ")
    idioma_destino = input("Introduce el código del idioma al que deseas traducir (por ejemplo, 'es' para español): ")

    traductor(texto_a_traducir, destino=idioma_destino)
