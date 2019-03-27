import cv2 as cv        # Faz a captura e o processamento da imagem
import numpy as np      # O bitmap das imagens são salvos em numpy arrays
import ctypes           # Exibição de janelas/alertas
import os.path as path  # Garantir que as imagens sejam salvas na pasta certa

# Praticidade ao exibir a message box
def messageBox(window ,title, text, style):
    return ctypes.windll.user32.MessageBoxW(window, text, title, style)


# Começa a capturar o vídeo pela WebCam
webcam = cv.VideoCapture(0)

# Flag que determina primeira execução do loop
primeira = True
# Loop para salvar a foto
while True:

    # Alerta que roda somente na primera execução
    if primeira:
        messageBox(0, "Aviso", "Pressione Espaço para tirar a foto", 0)
        primeira = False

    # Loop de gravação
    while True: 

        # Check = boolean - Gravando ou não
        # Frame = bitmap do frame
        check, frame = webcam.read()

        # Exibe o(s) Frame(s) sendo capturado(s)
        cv.imshow("Capturando", frame)
        # Tempo real de exibição (dentro dos limites da webcam, claro)
        key = cv.waitKey(1)

        # Pressione espaço para sair do loop
        if key==ord('\u0020'):
            break

    # Fecha a janela da webcam
    cv.destroyWindow("Capturando")
    
    # Mostra a "foto" tirada
    # A foto é na verdade o último frame antes de sair do loop
    window = cv.imshow("Foto",frame)

    # Retorna 6 pra Sim & 7 pra Não
    # Stringfy pra poder usar ela na função ord()
    resposta = str(messageBox(window, "Salvar?", "Deseja salvar essa foto?", 4))

    # Sim
    # Unicode de 6
    if ord(resposta) == 54:
        # Fecha a janela
        # cv.waitKey(1)
        cv.destroyWindow("Foto")

        # Se já existe uma foto no diretório
        if path.isfile(path.dirname(path.abspath(__file__)) + '\\foto.jpg'):
            for i in range(2, 101):

                # Se o caminho não existe
                if not path.isfile(path.dirname(path.abspath(__file__)) + '\\foto{}.jpg'.format(i)):
                    # Salva
                    cv.imwrite(path.dirname(path.abspath(__file__)) + "\\foto{}.jpg".format(i), frame)
                    break # sai do loop

                # Chegou na última iteração
                # Então dá overwrite no último arquivo
                if i == 100:
                    cv.imwrite(path.dirname(path.abspath(__file__)) + '\\foto100.jpg', frame)
                    break


        else:
            # Salva a imagem no running directory
            cv.imwrite(path.dirname(path.abspath(__file__)) + "\\foto.jpg", frame)
        break
    else: # Não
        
        # Retorna 4 para Retry & 2 para Cancel
        resposta = str(messageBox(0, "Tentar novamente?", "Deseja tentar salvar outra foto?", 5))
        
        # Fecha a janela com a foto
        cv.destroyWindow("Foto")

        # Cancel
        if ord(resposta) == 50:
            break
    
    # Volta para o início do loop

# Garantia para que nenhuma janela fique aberta sozinha
cv.destroyAllWindows()

# Desliga a webcam
webcam.release()



