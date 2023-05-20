# zapamiętywanie 10 ostatnich wpisów

def remember(wpisy, nowy_wpis):
    if len(wpisy) == 10:
        wpisy.pop()
    wpisy.insert(0, nowy_wpis)

wpisy = []

remember(wpisy, 'Pierwszy wpis')
remember(wpisy, 'Drugi wpis')
remember(wpisy, 'Trzeci wpis')

print(wpisy)
