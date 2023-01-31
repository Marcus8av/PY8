print('Вас интересует шифр Цезаря? Тогда Вам сюда:')
def caesar(cipher, rot, language, text): 
    if language == 'ru': 
        alp = rus_lower
        ALP = rus_upper
        length = 32
    elif language == 'en':
        alp = eng_lower
        ALP = eng_upper
        length = 26
    text_decryption = ''
    if cipher == 1:
        for i in text:
            if i.isalpha() and i.islower():
                text_decryption += alp[(alp.find(i) + rot) % length]
            elif i.isalpha() and i.isupper():
                text_decryption += ALP[(ALP.find(i) + rot) % length]
            else:
                text_decryption += i
        return text_decryption
    if cipher == 2:
        for i in text:
            if i.isalpha() and i.islower():
                text_decryption += alp[(alp.find(i) - rot) % length]
            elif i.isalpha() and i.isupper():
                text_decryption += ALP[(ALP.find(i) - rot) % length]
            else:
                text_decryption += i
        return text_decryption

eng_lower = 'abcdefghijklmnopqrstuvwxyz'
eng_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

print('Вы хотите звшифровать или расшифровать?')  
while True:  
    cipher = input('Если хотите зашифровать то введите "1" еслип хотите расшифровать то введите "2" ')
    if not cipher.isdigit() or 0 < int(cipher) > 2:
        print('Вы ввели неправильное значение')
        continue
    elif int(cipher) == 0:
        print('Вы ввели неправильное значение')
        continue
    else:
        break
cipher = int(cipher)  
print('На каком языке вы хотите это сделать?')
while True:  
    lan = input('Если хотите это сюделать на английском то введите "en", если хотите это сделать на русском то введите "ru" ')
    if lan.lower() == 'en' or lan.lower() == 'ru':
        break
    else:
        print('Вы ввели неправильное значение')
        continue
language = lan.lower()  
print('Сдвигаться будет с шагом вправо ')
while True:  
    step = input('Введите цифру от 1 до 28 ')
    if not step.isdigit() or 0 < int(step) > 29:
        print('Вы ввели неправильное значение')
        continue
    elif int(step) == 0:
        print('Вы ввели неправильное значение')
        continue
    else:
        break
step = int(step)  
text = input('Ведите сюда свой текст, символы и цифры не шифруются! ')
print(caesar(cipher, step, language, text))