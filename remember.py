def remember(wpisy, nowy_wpis): # zapamiętywanie 10 ostatnich wpisów
    if len(wpisy) == 10:
        wpisy.pop()
    wpisy.insert(0, nowy_wpis)

wpisy = [''] * 10

# def click_equals():
#     expression = cell.get()
#     cell_label = Label(window, text=expression)
#     cell_label.
