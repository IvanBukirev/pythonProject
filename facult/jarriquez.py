import time

start_time = time.time()
def jarriquez_encryption(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False):
    if reverse: alphabet = alphabet[::-1]
    text = text.upper()
    key_tx=str(key)
    encoded = ''
    i=0
    for ch in text:
       if ch in alphabet:
            encoded += alphabet[(alphabet.find(ch) + int(key_tx[i])) % len(alphabet)]
            i+=1
            if i==len(key_tx):
                i=0
    return encoded

for i in range(1111, 1000000):
    stroka=(jarriquez_encryption("ТЛБЛДУЭППТКЛФЧУВНУПБКЗИХТЛТТЫХНЛОИНУВЖММИНПФНПШОКЧЛЕРНТФНАХЖИДМЯКЛТУБЖИУЕЖЕАХЛГЩЕЕ"
                           "ЪУВНГАХИЯШПЙАОЦЦПВТЛБФТТИИНДИДНЧЮОНЯОФВТЕАТФУШБЛРЮЮЧЖДРУУШГЕХУРПЧЕУВАЭУОЙБДБНОЛСКЦБ"
                           "САОЦЦПВИШЮТППЦЧНЖОИНШВРЗЕЗКЗСБЮНЙРКПСЪЖФФШНЦЗРСЭШЦПЖСЙНГЭФФВЫМЖИЛРОЩСЗЮЙФШФДЖО"
                           "ИЗТРМООЙБНФГОЩЧФЖООКОФВЙСЭФЖУЬХИСЦЖГИЪЖДШПРМЖПУПГЦНВКБНРЕКИБШМЦХЙИАМФЛУЬЙИСЗРТЕС",i
                           , "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",True))
    if stroka.find("АЛМАЗ")!=-1 and stroka.find("ДАКОСТА")!=-1:
        print(stroka)
        print(f'{i}   *************' )
        break
end_time = time.time()

execution_time = end_time - start_time
print(f'Время выполнения: {execution_time:.2f} секунд')
