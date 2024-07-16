"""
File: main.py
@author: Benjamin Nolan
@description: CSV/xlsx to ERD Converter
@lang: Python

Requirements:
pygame
"""

import pygame as py
import pandas as pd
import os
import csv

BLACK = (30, 30, 30)
WHITE = (255, 255, 255)

py.init()
window = py.display.set_mode((800, 600))
py.display.set_caption("CSV to ERD Converter")
window_clock = py.time.Clock()
font = py.font.SysFont('Arial', 24)


def drawFrame():
    window.fill(WHITE)
    x = 100
    y = 100

    # look in data folder and get CSV data file - only need one at this stage
    filetypes = ['csv']
    dataPath = './data'
    csvFile = [[f for f in os.listdir(dataPath) if f.endswith(type_)] for type_ in filetypes]
    csvFile = ''.join(csvFile[0])
    # print(csvFile)

    # load data into df
    data = pd.read_csv(dataPath+'/'+csvFile)
    df = pd.DataFrame(data)

    data2 = dataPath+'/'+csvFile

    tables = {}
    with open(data2, newline='') as csvF:
        reader = csv.reader(csvF)
        for row in reader:
            table, field, datatype = row
            if table not in tables:
                tables[table] = []
            tables[table].append((field, datatype))

    # get tables and fields onto screen

    # # make list of tables to iterate
    # tables = []
    # for index, row in df.iterrows():
    #     table = row['Table']
    #     tables.append(table)
    # tables = list(dict.fromkeys(tables))
    # numTables = len(tables)
    #
    # # make list of fields to iterate
    # fields = []
    # for index, row in df.iterrows():
    #     field = row['Field']
    #     fields.append(field)
    # numFields = len(fields)

    i = 0
    j = 0

    textLen = {}
    for table, fields in tables.items():
        tablelen = len(table)
        fieldlens = [len(field) for field, datatype in fields]
        textLen[table] = (tablelen, fieldlens)

    for table, (tablelen, fieldlens) in textLen.items():
        drawText(x, y, table, 24, BLACK)
        y += font.get_height()
        for (field, datatype), fieldlen in zip(tables[table], fieldlens):
            drawText(x+tablelen*10, y, field, 18, BLACK)
            drawText(x + tablelen * 40, y, datatype, 16, BLACK)
            y += font.get_height()
        y += 20

    # iterate over tables
    # while i <= numTables - 1:
    #     tableNameLen = len(tables[i])
    #     if i == 0:
    #         xtMultiplier = 0  # initial x at 100
    #         ytMultiplier = 0  # initial y at 100
    #     else:
    #         xtMultiplier = 0  # constant x, but changing y
    #         ytMultiplier = (numFields*30) * i+1
    #     drawText(x + (xtMultiplier), y + (ytMultiplier), tables[i], 24, BLACK)
    #
    #     # iterate over fields
    #     while j <= numFields - 1:
    #         if j == 0:
    #             xfMultiplier = 10 * 15
    #             yfMultiplier = 0
    #         else:
    #             xfMultiplier = 10 * 15
    #             yfMultiplier = 10 * i + 1
    #         drawText(x + (xfMultiplier), y + (yfMultiplier), fields[j], 18, BLACK)
    #         j += 1
    #
    #     i += 1

    # get fields onto screen
    # i = 0
    # fields = []
    # for index, row in df.iterrows():
    #     field = row['Field']
    #     fields.append(field)
    # fields = list(dict.fromkeys(fields))
    # print(fields)
    # while i <= numFields-1:
    #     # if i == 2:
    #     #     break
    #     fieldNameLen = len(fields[i])
    #     # print(fieldNameLen)
    #     if i == 0:
    #         xMultiplier = 30
    #         yMultiplier = 0
    #     else:
    #         xMultiplier = 30
    #         yMultiplier = 5 * i
    #     drawText(x + (xMultiplier), y + (yMultiplier), fields[i], BLACK)
    #     i += 1


    # loop through tables from data
    # while i <= numTables:
    #     print(df.rows['Table'][i])
    #     i += 1
    # data = [
    #     {'Table': 'Account', 'Field': 'Account ID', 'Data Type': 'int'},
    #     {'Table': 'Account', 'Field': 'Account Name', 'Data Type': 'varchar'},
    #     {'Table': 'Contact', 'Field': 'Contact ID', 'Data Type': 'int'},
    #     {'Table': 'Contact', 'Field': 'Contact Name', 'Data Type': 'varchar'},
    # ]
    #
    # # get distinct tables from data
    # numTables = len(data[0])
    # tables = []
    # i = 0
    # while i <= numTables:
    #     table = data[i]['Table']
    #     tables.append(table)
    #     i += 1
    # tables = list(dict.fromkeys(tables))
    #
    # # get fields from data
    # numFields = len(data[0]['Field'])
    # print(numFields)

    # working output
    # TabletextLen = 8
    # drawText(x, y, 'Account', BLACK)
    #
    # fieldtextLen = 10
    # drawText(x + (TabletextLen * 15), y + 0, 'Account ID', BLACK)
    # # drawArrow(x + 10, y - 10)
    # drawText(x + (fieldtextLen * 30), y + 0, 'int', BLACK)
    #
    # fieldtextLen = 10
    # drawText(x + (TabletextLen * 15), y + (TabletextLen * 5), 'Account Name', BLACK)
    # drawText(x + (fieldtextLen * 30), y + (TabletextLen * 5), 'varchar', BLACK)


# def drawTable(x, y, label):
#     label = str(label)
#     font = py.font.SysFont('arial', 20, True)
#     text = font.render(label, True, BLACK)
#     # py.draw.rect(window, color, py.Rect(x, y, 100, 100))
#     window.blit(text, (x, y))
#
#
# def drawField(x, y, label):
#     label = str(label)
#     font = py.font.SysFont('arial', 20, True)
#     text = font.render(label, True, BLACK)
#     # py.draw.rect(window, color, py.Rect(x, y, 100, 100))
#     window.blit(text, (x, y))
#
#
# def drawDataType(x, y, label):
#     label = str(label)
#     font = py.font.SysFont('arial', 20, True)
#     text = font.render(label, True, BLACK)
#     # py.draw.rect(window, color, py.Rect(x, y, 100, 100))
#     window.blit(text, (x, y))


def drawText(x, y, label, labelSize, color):
    label = str(label)
    font = py.font.SysFont('arial', labelSize, True)
    text = font.render(label, True, color)
    # py.draw.rect(window, color, py.Rect(x, y, 100, 100))
    window.blit(text, (x, y))


def drawBox(x, y, color):
    py.draw.rect(window, color, py.Rect(x-10, y, 100, 100))


def drawArrow(x, y):
    font = py.font.SysFont('arial', 10, True)
    text = font.render('-->', True, BLACK)
    # py.draw.rect(window, color, py.Rect(x, y, 100, 100))
    window.blit(text, (x, y))


def main():
    running = True
    while running:
        drawFrame()
        py.display.flip()
        window_clock.tick(1)
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                running = False
                quit()


if __name__ == '__main__':
    main()

# class PyERD:
#
#     def __init__(self, _display):
#         py.init()
#         window = py.display.set_mode((800, 600))
#         py.display.set_caption("CSV to ERD Converter")
#         window_clock = py.time.Clock()
#
#         self._display = window
#         self._window_clock = window_clock
#
#         fonts = py.font.get_fonts()
#         self._font = fonts[0]  # default to a random font
#         # try to look among the most common fonts
#         test_fonts = ['arial', 'couriernew', 'verdana', 'helvetica', 'roboto']
#         for font in test_fonts:
#             if font in fonts:
#                 self._font = font
#                 break
#
#         self.main()
#
#     def _draw_frame(self):
#         self.drawTable(100, 100, 'Account')
#         self._reset_bg()
#
#     def _reset_bg(self):
#         self._display.fill(BLACK)
#
#     def drawTable(self, x, y, label):
#         color = WHITE
#         font = py.font.SysFont(self._font, 20)
#         text = font.render(label, True, WHITE)
#         py.draw.rect(self._display, color, py.Rect(x, y, 100, 100))
#         self._display.blit(text, (x, y))
#
#     def drawField(self, x, y, label):
#         color = WHITE
#         font = py.font.SysFont(self._font, 20)
#         text = font.render(label, True, WHITE)
#         py.draw.rect(self._display, color, py.Rect(x, y, 100, 100))
#         self._display.blit(text, (x, y))
#
#     def main(self):
#         print('foo')
#         running = True
#         while running:
#             print('foo')
#             self._draw_frame()
#             py.display.update()
#             self._window_clock.tick(1)
#             for event in py.event.get():
#                 if event.type == py.QUIT:
#                     py.quit()
#                     running = False
#                     quit()
#
#
# if __name__ == '__main__':
#     PyERD.main()
