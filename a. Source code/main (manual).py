from tkinter import *
from manual_proceso_1 import *

global tg, style
tg = 'Segoe UI'

root = Tk()
root.title('Organizador de documentos')
root.columnconfigure(0, weight=1)
root.config(background='#171C18')
root.state('zoomed')
try: root.iconbitmap('b. Software\icon.ico')
except: pass
global menubar, mfile, mbrand, mhelp, fulldatapack
menubar = Menu(root)
root.config(menu=menubar)
mfile = Menu(menubar, tearoff=0)
mfile.add_command(label='Cerrar sesión', state='disabled')
mfile.add_command(label='Salir')
mbrand = Menu(menubar, tearoff=0)
mbrand.add_command(label='Multimoney')
mbrand.add_command(label='Comercios')
mbrand.add_command(label='Beto')
mbrand.add_command(label='Manual')
mbrand.add_command(label='Actualización')
mhelp = Menu(menubar, tearoff=0)
mhelp.add_command(label='Documentación')
mhelp.add_command(label='GitHub')
menubar.add_cascade(label='Archivo', menu=mfile)
menubar.add_cascade(label='Marca', menu=mbrand)
menubar.add_cascade(label='Ayuda', menu=mhelp)

def frameheader(frame):
    head = Label(frame, text='PROCESAMIENTO DE DOCUMENTOS', background='#232925', fg='#3A493F', font=(tg, 20), anchor='center')
    head.grid(row=0, column=0, ipady=8, sticky='ew')

def buildf_multimoney():
    pass

def buildf_comercios():
    pass

def buildf_beto():
    pass

def buildf_manual():
    global savedocsin, label2, name, lname, identification, document, specificdate, panelinform
    frameheader(root)
    label_main_frame1 = LabelFrame(root, text='Manual', background='#171C18', fg='#777', font=(tg, 12), border=1, relief='solid')
    label_main_frame1.grid(row=1, column=0, sticky='ew', padx=30, pady=10, ipadx=20, ipady=10)
    label_main_frame1.columnconfigure(0, weight=1)
    main_frame1 = Frame(label_main_frame1, background='#171C18')
    main_frame1.grid(row=0, column=0, padx=30, pady=(5,0), sticky='ew')
    main_frame1.columnconfigure(0, weight=1)
    label_inputpath = LabelFrame(main_frame1, text='Ruta de salida (guardar los documetos procesados)', background='#171C18', fg='#777', font=(tg, 12), border=1, relief='solid')
    label_inputpath.grid(row=0, column=0, sticky='ew')
    label_inputpath.columnconfigure([0, 1, 2], weight=1)
    label1 = Label(label_inputpath, text='Configure una "Ruta de salida" para empezar', background='#171C18', fg='#AFA', font=(tg, 12))
    label1.grid(row=0, column=0, padx=20, pady=(10,20), sticky='w')
    Button(label_inputpath, text='configurar', background='#171C18', fg='#0F0', font=(tg, 12), border=0, cursor='hand2', activebackground='#171C18', activeforeground='#0A0', command=lambda:savingdir(label1, savedocsin, label2)).grid(row=0, column=2, sticky='e', ipadx=30)
    label_outputpath = LabelFrame(main_frame1, text='Ruta de entrada (documetos a procesar)', background='#171C18', fg='#777', font=(tg, 12), border=1, relief='solid')
    label_outputpath.grid(row=1, column=0, sticky='ew', pady=20)
    label_outputpath.columnconfigure([0, 1, 2], weight=1)
    label2 = Label(label_outputpath, text='Ruta de salida sin configurar...', background='#171C18', fg='#AFA', font=(tg, 12))
    label2.grid(row=0, column=0, padx=20, pady=(10,20), sticky='w')
    savedocsin = Button(label_outputpath, text='abrir', background='#171C18', fg='#0F0', font=(tg, 12), border=0, cursor='hand2', activebackground='#171C18', activeforeground='#0A0', state='disabled', command=lambda:workingspace(label2, name, lname, identification, document, specificdate, panelinform, runwizzard, label2))
    savedocsin.grid(row=0, column=2, sticky='e', ipadx=30)
    main_panel = Frame(main_frame1, background='#171C18')
    main_panel.grid(row=2, column=0, sticky='ew')
    main_panel.columnconfigure([0, 1, 2, 3], weight=1)
    label_customerdata = LabelFrame(main_panel, text='Datos del cliente', background='#171C18', fg='#777', font=(tg, 12), border=1, relief='solid')
    label_customerdata.grid(row=0, rowspan=2, column=0, sticky='ew')
    label_customerdata.columnconfigure(0, weight=1)
    box_customerdata = Frame(label_customerdata, background='#252C26')
    box_customerdata.grid(row=0, column=0, padx=25, pady=10, ipadx=10, sticky='ew')
    box_customerdata.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], weight=1)
    Label(box_customerdata, text='Nombre(s)', background='#252C26', fg='#FFF', font=(tg, 12), anchor='e').grid(row=0, column=0, sticky='ew', padx=9, pady=9)
    name = Entry(box_customerdata, font=(tg, 12))
    name.grid(row=0, column=1, columnspan=7, pady=(10,5), ipady=3, sticky='ew')
    Label(box_customerdata, text='Apellido(s)', background='#252C26', fg='#FFF', font=(tg, 12), anchor='e').grid(row=1, column=0, sticky='ew', padx=9, pady=9)
    lname = Entry(box_customerdata, font=(tg, 12))
    lname.grid(row=1, column=1, columnspan=7, pady=5, ipady=3, sticky='ew')
    Label(box_customerdata, text='Identificación', background='#252C26', fg='#FFF', font=(tg, 12), anchor='e').grid(row=2, column=0, sticky='ew', padx=9, pady=9)
    identification = Entry(box_customerdata, font=(tg, 12))
    identification.grid(row=2, column=1, columnspan=7, pady=5, ipady=3, sticky='ew')
    Label(box_customerdata, text='Pagaré', background='#252C26', fg='#FFF', font=(tg, 12), anchor='e').grid(row=3, column=0, sticky='ew', padx=9, pady=9)
    document = Entry(box_customerdata, font=(tg, 12))
    document.grid(row=3, column=1, columnspan=7, pady=5, ipady=3, sticky='ew')
    Label(box_customerdata, text='Fechado', background='#252C26', fg='#FFF', font=(tg, 12), anchor='e').grid(row=4, column=0, sticky='ew', padx=9, pady=9)
    specificdate = Entry(box_customerdata, font=(tg, 12))
    specificdate.grid(row=4, column=1, columnspan=7, pady=3, ipady=3, sticky='ew')
    runwizzard = Button(box_customerdata, text='procesar', background='#252C26', fg='#0F0', font=(tg, 12), border=0, cursor='hand2', activebackground='#252C26', activeforeground='#0A0', state='disabled', command=lambda:runwizard(fulldatapack, runwizzard, label2, info1, openlastprocessed, panelinform))
    runwizzard.grid(row=5, column=1, columnspan=7, sticky='e', pady=10)
    wrap_eastpanel = Frame(main_panel, background='#171C18')
    wrap_eastpanel.grid(row=0, column=1, columnspan=3, padx=(50,0), sticky='nsew')
    wrap_eastpanel.columnconfigure(0, weight=1)
    label_info2 = LabelFrame(wrap_eastpanel, text='Documentos a procesar', background='#171C18', fg='#777', font=(tg, 12), border=1, relief='solid')
    label_info2.grid(row=0, column=0, columnspan=3, pady=(0,30), sticky='ew')
    label_info2.columnconfigure(0, weight=1)
    frameinfo2 = Frame(label_info2, background='#171C18')
    frameinfo2.grid(row=0, column=0, sticky='ew')
    frameinfo2.columnconfigure([0, 1, 2, 3, 4], weight=1)
    info2_total = Label(frameinfo2, text='0', background='#171C18', fg='#AFA', font=(tg, 12), anchor='center')
    info2_total.grid(row=0, column=0, padx=25, pady=(20,0), ipadx=10, sticky='ew')
    info2_total_footer = Label(frameinfo2, text='TOTAL', background='#171C18', fg='#555', font=(tg, 12))
    info2_total_footer.grid(row=1, column=0, padx=25, pady=(0,30), sticky='ew')
    info2_pdf = Label(frameinfo2, text='0', background='#171C18', fg='#AFA', font=(tg, 12), anchor='center')
    info2_pdf.grid(row=0, column=1, padx=25, pady=(20,0), ipadx=10, sticky='ew')
    info2_pdf_footer = Label(frameinfo2, text='PDF', background='#171C18', fg='#555', font=(tg, 12))
    info2_pdf_footer.grid(row=1, column=1, padx=25, pady=(0,30), sticky='ew')
    info2_png = Label(frameinfo2, text='0', background='#171C18', fg='#AFA', font=(tg, 12), anchor='center')
    info2_png.grid(row=0, column=2, padx=25, pady=(20,0), ipadx=10, sticky='ew')
    info2_png_footer = Label(frameinfo2, text='PNG', background='#171C18', fg='#555', font=(tg, 12))
    info2_png_footer.grid(row=1, column=2, padx=25, pady=(0,30), sticky='ew')
    info2_jpg = Label(frameinfo2, text='0', background='#171C18', fg='#AFA', font=(tg, 12), anchor='center')
    info2_jpg.grid(row=0, column=3, padx=25, pady=(20,0), ipadx=10, sticky='ew')
    info2_jpg_footer = Label(frameinfo2, text='JPG', background='#171C18', fg='#555', font=(tg, 12))
    info2_jpg_footer.grid(row=1, column=3, padx=25, pady=(0,30), sticky='ew')
    info2_jpeg = Label(frameinfo2, text='0', background='#171C18', fg='#AFA', font=(tg, 12), anchor='center')
    info2_jpeg.grid(row=0, column=4, padx=25, pady=(20,0), ipadx=10, sticky='ew')
    info2_jpeg_footer = Label(frameinfo2, text='JPEG', background='#171C18', fg='#555', font=(tg, 12))
    info2_jpeg_footer.grid(row=1, column=4, padx=25, pady=(0,30), sticky='ew')
    panelinform = [info2_total, info2_pdf, info2_png, info2_jpg, info2_jpeg]
    label_info1 = LabelFrame(wrap_eastpanel, text='Última carpeta procesada', background='#171C18', fg='#777', font=(tg, 12), border=1, relief='solid')
    label_info1.grid(row=1, column=0, sticky='ew')
    label_info1.columnconfigure([0, 1, 3, 4], weight=1)
    info1 = Label(label_info1, text='No se han procesado carpetas', background='#171C18', fg='#AFA', font=(tg, 12))
    info1.grid(row=0, column=0, columnspan=3, padx=25, pady=20, ipadx=10, sticky='w')
    openlastprocessed = Button(label_info1, text='abrir', background='#171C18', fg='#0F0', font=(tg, 12), border=0, cursor='hand2', activebackground='#171C18', activeforeground='#0A0', state='disabled', command=lambda:startf(openlastprocessed, info1))
    openlastprocessed.grid(row=0, column=4, sticky='e', ipadx=30, pady=30)
    fulldatapack = [name, lname, identification, document, specificdate, label2, panelinform]

def buildf_actualizacion():
    pass

buildf_manual()
root.mainloop()