print("playlist infinita 🎶")

tocando = True
while tocando :
    print("tocando musica...🎵")
    resposta = input("Proxima musica, sim ou não ")
    if resposta.lower() != "sim":
        tocando = False
print("playlist finalizada")