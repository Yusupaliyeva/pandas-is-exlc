# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13q-iGQmozhLXJuz4daCSbYkzbCAGEYo-
"""



import pandas as pd
df = pd.DataFrame({  'Ism': ['Moxichexra', 'Mushtariy', 'Madina', 'Boboxoja', 'Nurmuhammad', 'Muhammadaziz', 'Xurshidbek', 'Olloyor', 'Bibifotima', 'Asadbek'],
                   'Familiya': ['Yusupaliyeva', 'Qadamova', 'Amakixonova', 'Rahmatxonov', 'Jumanazarov', 'Rozaliyev', 'Odilov', 'Ashurboyev', 'Joraboyeva', 'Xudoyberdiyev'],
                   'Yoshi': ['20', '21','19','20','19','19','19','19','19','19'],
                   'Kursi': ['2', '2', '2' ,'2', '2','2', '2', '2' ,'2', '2']
})

print(df)

df.to_excel('hisobot.xlsx', index=False, sheet_name='Sheet1')