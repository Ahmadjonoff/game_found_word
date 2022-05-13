from uzwords import words
import random

def get_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def display(harflar, word):
    soz = word
    for harf in range(len(soz)):
        if soz[harf] not in harflar:
            soz = soz.replace(soz[harf], '-')
    return soz.upper()

def play():
    word = get_word()
    print(f'Men {len(word)} xonali so`z o`yladim. Topa olasizmi?')
    harflar = ''
    print(display(harflar, word))
    taxminlar = 0
    while '-' in display(harflar, word):
        taxminlar += 1
        harf = input('Harf kiriting: ').lower()
        if harf in harflar:
            print('Bu harfni avval kiritgansiz. Boshqa harf kiriting!')
            print(display(harflar, word))
            print('Shu vaqtgacha kiritgan harflaringiz:', harflar.upper())
        else:
            harflar += harf
            if harflar[-1] in word:
                print(f'{harflar[-1].upper()} harfi to`g`ri.')
            else:
                print('Bunday harf yo`q')
            print(display(harflar, word))
            print('Shu vaqtgacha kiritgan harflaringiz:', harflar.upper())
    else:
        print(f'Tabriklayman! {word} so`zini {taxminlar} ta taxmin bilan topdingiz!')
        
play()