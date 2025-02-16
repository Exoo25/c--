import tkinter as tclw
from tkinter import filedialog,messagebox,simpledialog,colorchooser,commondialog
import pygame as gamew
import turtle,math,random,turtle,time,datetime,threading,tkcode,flask
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

        
def print():
    pass
