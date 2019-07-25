import sys
from importlib import import_module     

libnames = ['send2trash', 'openpyxl', 'csv' , 'PIL' , 'matplotlib' , 'fpdf' , 'PyPDF2' , 'requests', 'json' , 'bs4' , 'smtplib' , 'telepot'  ]
for libname in libnames:
    try:
        lib = import_module(libname)
    except:
        print(sys.exc_info())
    else:
        globals()[libname] = lib