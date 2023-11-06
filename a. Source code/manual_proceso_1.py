import os
from PyPDF2 import PdfReader, PdfMerger
from PIL import Image
from tkinter import END, filedialog, messagebox

def savingdir(label, btn, label2):
    global kitoutputdir
    kitoutputdir = filedialog.askdirectory(title='Ruta de salida (guardar los documetos procesados)')
    kitoutputdir += '/'
    if kitoutputdir != '/':
        label.config(text=kitoutputdir)
        btn.config(state='normal')
        label2.config(text='Seleccione una nueva carpeta para empezar...')
    else:
        messagebox.showerror('Procesamiento de documentos', 'No se ha seleccionado ninguna carpeta.\n\nPor favor seleccione una carpeta para guardar los documentos una vez procesados para continuar.')
        label.config(text='Configure una "Ruta de salida" para empezar')
        btn.config(state='disabled')
        label2.config(text='Ruta de salida sin configurar')

def cls(name, lname, identification, document, specificdate):
    name.delete(0, END)
    lname.delete(0, END)
    identification.delete(0, END)
    document.delete(0, END)
    specificdate.delete(0, END)

def scan_folder():
    global folderitemslist, info2_total, _pdf, _jpg, _jpeg, _png
    folderitemslist = []
    _pdf = 0; _jpg = 0; _jpeg = 0; _png = 0
    for f in osscandir:
        f = f.upper()
        f = f.replace('PDF', 'pdf'); f = f.replace('JPG', 'jpg'); f = f.replace('JPEG', 'jpeg'); f = f.replace('PNG', 'png')
        folderitemslist.append(f)
        if f.__contains__('.pdf'): _pdf += 1
        elif f.__contains__('.jpg'): _jpg += 1
        elif f.__contains__('.jpeg'): _jpeg += 1
        elif f.__contains__('.png'): _png += 1

def readabledocs_searching():
    global readabledoc, kyc
    for f in folderitemslist:
        if f.__contains__('CIC2'): readabledoc = f'{kitworkingdir}{f}'
        elif f.__contains__('CONSENTIMIENTO2'): readabledoc = f'{kitworkingdir}{f}'
        elif f.__contains__('DECLARACION2') or f.__contains__('DECLARACIÓN2'): readabledoc = f'{kitworkingdir}{f}'
        if f.__contains__('KYC2'): kyc = f'{kitworkingdir}{f}'

def switch(self):
    if self[0] == 'ENERO': self[0] = '01'
    if self[0] == 'FEBRERO': self[0] = '02'
    if self[0] == 'MARZO': self[0] = '03'
    if self[0] == 'ABRIL': self[0] = '04'
    if self[0] == 'MAYO': self[0] = '05'
    if self[0] == 'JUNIO': self[0] = '06'
    if self[0] == 'JULIO': self[0] = '07'
    if self[0] == 'AGOSTO': self[0] = '08'
    if self[0] == 'SEPTIEMBRE': self[0] = '09'
    if self[0] == 'OCTUBRE': self[0] = '10'
    if self[0] == 'NOVIEMBRE': self[0] = '11'
    if self[0] == 'DICIEMBRE': self[0] = '12'

def workingspace(label, name, lname, identification, document, specificdate, panelinform, btn, label2):
    global kitworkingdir, osscandir
    kitworkingdir = filedialog.askdirectory(title='Ruta de entrada (buscar los documetos a procesar)')
    kitworkingdir += '/'
    if kitworkingdir != '/':
        btn.config(state='normal')
        osscandir = os.listdir(kitworkingdir)
        cls(name, lname, identification, document, specificdate)
        label.config(text=kitworkingdir)
        scan_folder()
        panelinform[0].config(text=f'{_pdf + _jpg + _jpeg + _png}')
        panelinform[1].config(text=_pdf); panelinform[2].config(text=_jpg); panelinform[3].config(text=_jpeg); panelinform[4].config(text=_png)
        readabledocs_searching()
        try:
            pdf = open(readabledoc, 'rb')
            reader = PdfReader(pdf)
            content = reader.pages[0].extract_text().split('\n')
            pdf.close()
            global fullname, resid
            resid = ''
            if readabledoc.__contains__('CIC2'):
                reqline = content[10]
                reqline = reqline.replace('\xa0', ' ')
                reqline = reqline.replace('Yo, ', '')
                reqline = reqline.replace(', identificación número ', ' ')
                reqline = reqline.replace(', autorizo a la Superintendencia General de Entidades Financieras para que', '')
                reqline = reqline.upper()
                reqline = reqline.split(' ')
                resid = reqline.pop()
                fullname = reqline
            elif readabledoc.__contains__('CONSENTIMIENTO2') or readabledoc.__contains__('DECLARACION2') or readabledoc.__contains__('DECLARACIÓN2'):
                reqline = f'{content[2]} {content[3]}'
                reqline = reqline.replace('\xa0', ' ')
                reqline = reqline.replace(',', '')
                reqline = reqline.split(' mayor ')
                fullname = reqline[0]
                fullname = fullname.replace('El suscrito ', '')
                fullname = fullname.replace('La suscrita ', '')
                fullname = fullname.split(' ')
                getidnumber = reqline[1]
                for n in getidnumber:
                    check = n.isnumeric()
                    if check: resid += n
            if len(fullname) == 3:
                name.insert(0, f'{fullname[0]}')
                lname.insert(0, f'{fullname[1]} {fullname[2]}')
            elif len(fullname) == 4:
                name.insert(0, f'{fullname[0]} {fullname[1]}')
                lname.insert(0, f'{fullname[2]} {fullname[3]}')
            elif len(fullname) > 4:
                lname.insert(0, f'{fullname[-2]} {fullname[-1]}')
                fullname.pop()
                fullname.pop()
                fullname = ' '.join(fullname)
                name.insert(0, fullname)
            identification.insert(0, resid)
        except: pass
        try:
            pdf = open(kyc, 'rb')
            reader = PdfReader(pdf)
            content = reader.pages[0].extract_text().split('\n')
            pdf.close()
            required = content[3]
            required = required.replace('\xa0', '')
            required = required.split('Cód')
            required = required[0]
            required = required.split(' ')
            required = f'{required[-2].upper()} {required[-1]}'
            required = required.split(' ')
            switch(required)
            specificdate.insert(0, f'{required[0]}-{required[1]}')
            content = content[4].split(' ')
            content = content[-1]
            document.insert(0, content)
        except: pass
    else:
        messagebox.showerror('Procesamiento de documentos', 'No se ha seleccionado ninguna carpeta.\n\nPor favor seleccione una carpeta a procesar para continuar.')
        cls(name, lname, identification, document, specificdate)
        panelinform[0].config(text='0'); panelinform[1].config(text='0'); panelinform[2].config(text='0'); panelinform[3].config(text='0'); panelinform[4].config(text='0')
        label2.config(text='Seleccione una nueva carpeta para empezar...')
        btn.config(state='disabled')

def checkentries(fulldatapack):
    global fieldstester
    fieldstester = True
    for g in range(0, 5):
        if len(fulldatapack[g].get()) == 0:
            fieldstester = False

def runwizard(fulldatapack, btn, label, last, openlastprocessed, panelinform):
    checkentries(fulldatapack)
    if fieldstester == True:
        global render, finalpath
        newfolders = ['0. OTROS DOCUMENTOS', '1. INFORMACIÓN GENERAL', '2. APROBACIONES CREDITICIAS', '3. INFORMACIÓN PARA ANÁLISIS CAPACIDAD', '4. RESULTADOS DE ANÁLISIS']
        render = f'{fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}'
        try:
            os.makedirs(f'{kitoutputdir}{render.upper()}')
            finalpath = f'{kitoutputdir}{render.upper()}/'
            for dir in newfolders:
                os.makedirs(f'{finalpath}{dir}')
            last.config(text=render.upper())
            label.config(text='Seleccione una carpeta para procesar...')
            btn.config(state='disabled')
            openlastprocessed.config(state='normal')
            global _listedfiles, _cleaner, _merge, temp
            _listedfiles = []; _cleaner = []; _merge = []
            for f in osscandir:
                keepname = f
                f = f.upper()
                f = f.replace('.PDF', '.pdf')
                f = f.replace('.JPG', '.jpg')
                f = f.replace('.JPEG', '.jpeg')
                f = f.replace('.PNG', '.png')
                if f.__contains__('.pdf'):
                    _listedfiles.append(f)
                elif f.__contains__('.jpg') or f.__contains__('.jpeg') or f.__contains__('.png'):
                    if f.__contains__('ID'):
                        global pdffromimg
                        pdffromimg = True
                        img = Image.open(f'{kitworkingdir}{f}')
                        img = img.convert('RGB')
                        temp = f'{kitworkingdir}{f}'
                        temp = temp.replace('.jpg', ''); temp = temp.replace('.jpeg', ''); temp = temp.replace('.png', '')
                        temp = temp.upper()
                        img.save(f'{temp}.pdf')
                        _merge.append(f'{temp}.pdf')
                    else:
                        img = Image.open(f'{kitworkingdir}{f}')
                        img = img.convert('RGB')
                        temp = f'{kitworkingdir}{f}'
                        temp = temp.replace('.jpg', ''); temp = temp.replace('.jpeg', ''); temp = temp.replace('.png', '')
                        temp = temp.upper()
                        img.save(f'{temp}.pdf')
                        _listedfiles.append(f'{kitworkingdir}{temp}.pdf')
            try:
                if pdffromimg:
                    merger = PdfMerger()
                    outputname = f'{kitworkingdir}ID.pdf'
                    for id in _merge:
                        merger.append(open(id, 'rb'))
                    with open(outputname, 'wb') as finalid:
                        merger.write(finalid)
            except: pass
            quickscan = os.listdir(kitworkingdir)
            for f in quickscan:
                if f.__contains__('ID1.pdf') or f.__contains__('id1.pdf') or f.__contains__('ID2.pdf') or f.__contains__('id1.pdf') or f.__contains__('.jpg') or f.__contains__('.jpeg') or f.__contains__('.png'):
                    _cleaner.append(f)
            for c in _cleaner:
                os.remove(f'{kitworkingdir}{c}')
            _listedfiles = os.listdir(kitworkingdir)
            if f in _listedfiles:
                if f.__contains__('pdf'): pass
                else: _listedfiles.remove(f)
            for l in _listedfiles:
                keepname = l
                uppername = l.upper()
                l = uppername.replace('PDF', 'pdf')
                if l.__contains__('CHEQUE') or l.__contains__('ESCRITURA') or l.__contains__('FOTOS') or l.__contains__('KUIKI') or l.__contains__('PASAPORTE') or l.__contains__('PROFORMA') or l.__contains__('OTROS') or l.__contains__('SABIAS') or l.__contains__('SEGURO') or l.__contains__('VOU') or l.__contains__('SABÍAS') or l.__contains__('DOM'):
                    n = l.replace('.pdf', '')
                    if l.__contains__('KUIKI'): ended = f'{n} COMUNICA {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                    elif l.__contains__('SABIAS') or l.__contains__('SABÍAS') : ended = f'SABÍAS QUE {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                    elif l.__contains__('VOU'):  ended = f'{n}CHER {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                    elif l.__contains__('DOM'):  ended = f'DOMICILIACION {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                    else:  ended = f'{n} {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                    ended = ended.upper(); ended = ended.replace('PDF', 'pdf')
                    keepname = f'{kitworkingdir}{keepname}'
                    moving = f'{kitoutputdir}{render}/{newfolders[0]}/{ended}'
                    os.rename(keepname, moving)
                elif l.__contains__('ID.pdf') or l.__contains__('CIC') or l.__contains__('CIC1') or l.__contains__('CIC2') or l.__contains__('CICAC') or l.__contains__('CONSENTIMIENTO') or l.__contains__('KYC') or l.__contains__('KYC1') or l.__contains__('KYC2') or l.__contains__('ID'):
                    n = l.replace('.pdf', '')
                    if l.__contains__('CIC.pdf') or l.__contains__('CIC1.pdf'): ended = f'AUTORIZACION CIC {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                    elif l.__contains__('CIC2'): ended = f'AUTORIZACION CIC {fulldatapack[4].get()} {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                    elif l.__contains__('CICAC'): ended = f'AUTORIZACION CICAC {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                    elif l.__contains__('CONSENTIMIENTO.pdf') or l.__contains__('CONSENTIMIENTO1.pdf'): ended = f'CONSENTIMIENTO INFORMADO {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                    elif l.__contains__('CONSENTIMIENTO2'): ended = f'CONSENTIMIENTO INFORMADO {fulldatapack[4].get()} {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                    elif l.__contains__('KYC.pdf') or  l.__contains__('KYC1.pdf'): ended = f'KYC {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                    elif l.__contains__('KYC2'): ended = f'KYC {fulldatapack[4].get()} {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                    else: ended = f'{n} {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                    ended = ended.upper(); ended = ended.replace('PDF', 'pdf')
                    keepname = f'{kitworkingdir}{keepname}'
                    moving = f'{kitoutputdir}{render}/{newfolders[1]}/{ended}'
                    os.rename(keepname, moving)
                elif l.__contains__('CONTRATO') or l.__contains__('PAGARE') or l.__contains__('PAGARÉ') or l.__contains__('LETRA'):
                    n = l.replace('.pdf', '')
                    if l.__contains__('PAGARE') or l.__contains__('PAGARÉ') or l.__contains__('LETRA'): ended = f'PAGARÉ {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                    else: ended = f'{n} {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                    ended = ended.upper(); ended = ended.replace('PDF', 'pdf')
                    keepname = f'{kitworkingdir}{keepname}'
                    moving = f'{kitoutputdir}{render}/{newfolders[2]}/{ended}'
                    os.rename(keepname, moving)
                elif l.__contains__('DECLARACION') or l.__contains__('DECLARACIÓN') or l.__contains__('ORDEN') or l.__contains__('ORIGEN'):
                    n = l.replace('.pdf', '')
                    if l.__contains__('DECLARACION.pdf') or l.__contains__('DECLARACION1.pdf') or l.__contains__('DECLARACIÓN.pdf') or l.__contains__('DECLARACIÓN1.pdf'): ended = f'DECLARACION JURADA {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                    elif l.__contains__('DECLARACION2') or l.__contains__('DECLARACIÓN2'): ended = f'DECLARACION JURADA {fulldatapack[4].get()} {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                    elif l.__contains__('ORDEN'):
                        if l.__contains__('ORDEN.pdf'): ended = f'ORDEN PATRONAL 1 {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                        else:
                            nn = n.split('ORDEN')
                            ended = f'ORDEN PATRONAL {nn[1]} {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                    elif l.__contains__('ORIGEN'): 
                        if l.__contains__('ORIGEN.pdf'): ended = f'ORIGEN DE INGRESOS 1 {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                        else:
                            nn = n.split('ORIGEN')
                            ended = f'ORIGEN DE INGRESOS {nn[1]} {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                    ended = ended.upper(); ended = ended.replace('PDF', 'pdf')
                    keepname = f'{kitworkingdir}{keepname}'
                    moving = f'{kitoutputdir}{render}/{newfolders[3]}/{ended}'
                    os.rename(keepname, moving)
                else:
                    n = l.replace('.pdf', '')
                    cod = []
                    cod.append(l[0]); cod.append(l[1]); cod.append(l[2])
                    if cod[0].isdigit():
                        if cod[1] == 'F' and cod[2] == ' ':
                            n = n[3:]
                            ended = f'{n} {fulldatapack[4].get()} {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                        else:
                            n = n[2:]
                            ended = f'{n} {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                        pos = cod[0]
                        pos = int(pos)
                        ended = ended.upper(); ended = ended.replace('PDF', 'pdf')
                        try: moving = f'{kitoutputdir}{render}/{newfolders[pos]}/{ended}'
                        except: moving = f'{kitoutputdir}{render}/Núm de carpeta ({str(pos)}) incorrecto - {ended}'
                    else:
                        if cod[0] == 'F' and cod[1] == ' ':
                            n = n[2:]
                            ended = f'{n} {fulldatapack[4].get()} {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                        else: ended = f'{n} {fulldatapack[2].get()} {fulldatapack[1].get()} {fulldatapack[0].get()} {fulldatapack[3].get()}.pdf'
                        ended = ended.upper(); ended = ended.replace('PDF', 'pdf')
                        moving = f'{kitoutputdir}{render}/{ended}'
                    keepname = f'{kitworkingdir}{keepname}'
                    os.rename(keepname, moving)
            cls(fulldatapack[0], fulldatapack[1], fulldatapack[2], fulldatapack[3], fulldatapack[4])
            parentf = kitworkingdir.split('/'); parentf.pop(); parentf = '/'.join(parentf)
            for i in range(len(panelinform)):
                panelinform[i].config(text='0')
        except:
            messagebox.showinfo('Kit de procesamiento de documentos', 'Los documentos que intentas procesar al parecer se están duplicando.\n\nPor favor verifica que no exista ya una carpeta idéntica para continuar.')
    elif fieldstester == False:
        messagebox.showinfo('Kit de procesamiento de documentos', 'Hay campos sin rellenar.\n\nPor favor verifique que todos los campos de "DATOS DEL CLIENTE" estén correctamente rellenados para continuar.')

def startf(openlastprocessed, info1):
    try: os.startfile(f'{kitoutputdir}{render}')
    except:
        messagebox.showinfo('Procesamiendo de documentos', f'La carpeta "{kitoutputdir}{render}" ha sido movida o eliminada.')
        openlastprocessed.config(state='disabled')
        info1.config(text='No se han procesado carpetas')