"""
This reads the plain text output copied from Thermo XCalibur method editor,
and outputs a paragraph containing all the salient points.
"""


# import os
import custom_tools
import pandas as pd
import re
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import datetime
from io import StringIO


def get_time():
    return datetime.datetime.now().strftime('%d-%b-%Y_%H-%M-%S')

class gui():
    def __init__(self):
        top = tk.Tk()
        top.title = 'Format Orbitrap parameters'


        a = ScrolledText(top)
        a.config(width=50, height=20, undo=10, wrap='none')
        a.pack(pady=10)

        b = tk.Button(top, text='Click to format Orbitrap parameters', command=lambda: self.button_extract(a.get("1.0", tk.END)), )
        b.pack(pady=10)

        c = ScrolledText(top)
        c.config(width=50, height=10, undo=10, wrap='none')
        c.insert("1.0", 'Result:\n')
        c.pack(pady=10)

        top.mainloop()

    def button_extract(self, text_in):
        self.text_in = text_in
        self.df = get_text_from_orbitrap_parameters_as_df(text_in)
        self.paragraph = format_orbitrap_parameters(self.df)


def get_text_from_orbitrap_parameters_as_df(text_in, source='raw'):
    """
    source is either 'raw' for the raw file read in XCalibur or 'method' for the method file opened in Method Editor
    :param text_in:
    :param source:
    :return:
    """
    if source == 'method':
        df = pd.read_csv(StringIO(text_in), sep=":", names=['value'], index_col=[0])
        df['value'] = df['value'].str.strip()
    elif source == 'raw':
        df = pd.read_csv(StringIO(text_in), sep='=', names=['parameter','value'], index_col=None)
        df['value'] = df['value'].str.strip()
        df['tabs'] = df['parameter'].str.count('\t')
        # df.index = df.index.str.strip()
        # a.iloc[:, [0]].ffill(axis=0, inplace=True)
        # a.iloc[:, [0]].ffill(axis=0, inplace=True)
    return df

def format_orbitrap_parameters(df_in):
    parse_parameters(df_in)
    paragraph = ''
    return paragraph

def parse_parameters(df_in):
    """
    takes a dataframe keyed to the parameter names
    extracts all the salient parameters into a dictionary
    returns the dictionary
    :param df_in:
    :return:
    """
    params = []
    return params

if __name__ == '__main__':
    g = gui()