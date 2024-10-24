meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            }

word= input("escribame una palabra en mayasculas que tu no conozcas:")

if word in meme_dict.keys():
    print("definicion:")
    print(meme_dict[word])

else: 
    print("no tenemos esta palabra en el diccionario")
