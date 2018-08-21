# /usr/bin/python
# coding=utf-8

from pdfrw import PdfReader, PdfWriter

# Путь до автореферата
synopsis_path = '../synopsis.pdf'
# Путь до титульника Научного Доклада ГИА (должно быть две страницы: титульник и пустая)
gia_title_path = './gia_title.pdf'


synopsis = PdfReader(synopsis_path)
gia_title = PdfReader(gia_title_path)

sci_rep = PdfWriter()


for i, p in enumerate(synopsis.pages):
    if i < 2:
        sci_rep.addpage(gia_title.pages[i])
    else:
        sci_rep.addpage(p)


# Сохранение результата
sci_rep.write('./sci_rep.pdf')

