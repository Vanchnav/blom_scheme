from django.http import HttpResponse
from django.shortcuts import render
import random


def get_k(request):
    k = request.GET['k_input']
    return k


def get_m(request):
    m = request.GET['m_input']
    return m


def get_p(request):
    p = request.GET['p_input']
    return p


def get_n(request):
    n = request.GET['n_input']
    return n


def home(request):
    return render(request, 'BlomScheme1.html')


def Nkm(k,m):
    if k==1:
        return m+1
    else:
        if m==1:
            return k+1
    LL=[]
    for i in range (0,k):
        LL.append(i+2)
    for j in range (1,m):
        LLL=[j+2]
        for s in range(1,k):
            LLL.append(LL[s]+LLL[int(len(LLL))-1])
        LL=LLL+[]
    return LLL[int(len(LLL))-1]


def DecToBin(a):
    #print "Возвращает список значений двоичных разрядов, начиная со старшенго"
    Blist=[]
    while not a==0:
        b=a/2
        Blist.append(a-b*2)
        a=b
    return Blist


def cfind(k,m):
    #print "Построение списка индексов исходного полинома и списка индексов полиномов n участников (при k-1)"
    A=[]
    a=[]
    c=[]
    for i in range (0,k):
        a.append(0)
        c=a+[]
    A.append(c)
    j=k-1
    while a[0]<m:
            j=k-1
            while a[j]==m:
                j=j-1
            a[j]=a[j]+1
            b=a[j]+0
            if b==m:
                u=a+[]
                A.append(u)
                j=j-1
            else:
                for i in range (j,k):
                    a.pop(i)
                    a.insert(i,b)
                    u=a+[]
                A.append(u)
            j=k-1
    return A


def create_l(k,m):
    l = cfind(k,m)
    return l


def create_lc(k,m):
    lc = cfind(k - 1,m)
    return lc


def cfn(A,c,r,k,m):
    #print "Определение номера элемента списка A - коэффициента секретного многочлена, соответсвующего коэффициенту секретного многочлена для коэффициента c[i] j-го участника"
    u=c+[]
    if u[int(len(u))-1]<=r:
        u.append(r)
    else:
        i=0
        while u[i]<r:
            i=i+1
            #print "i=",i
        #print u
        u.insert(i,r)
        #print u
        c=u+[]
    return [i for i, j in enumerate(create_l(k,m)) if j == u][0]


# l=cfind(k,m)
# lc=cfind(k-1,m)


R=[]


def create_R(k,m):
    l = create_l(k,m)
    lc = create_lc(k,m)
    for i in range (0,int(len(lc))):
        rc=[]
        rc.append(lc[i])
        for j in range (0,m+1):
            u=cfn(l,lc[i],j)
            rc.append(u)
        R.append(rc)
    return R
#print "Таблица R - таблица координат степеней идентификаторов ri, i=1,...,n (имя списка R)"
#print R


def LNcreat(l,k):
    LN=[]
    ln=[]
    for j in range (0,int(len(l))-1):
        if ln==[]:
            ln.append(l[j][k-1])
            if l[j+1][k-1]<=l[j][k-1]:
                LN.append(ln)
                ln=[]
        else:
            if l[j+1][k-1]<=l[j][k-1]:
                ln.append(l[j][k-1])
                LN.append(ln)
                ln=[]
            else:
                ln.append(l[j][k-1])
    LN.append([l[int(len(l)-1)][k-1]])
    return(LN)
#print "Таблица E: списки номеров пользователей в данной группе коэффициентов (имя списка E)"
def create_E(k,m):
    l = create_l(k,m)
    E=LNcreat(l)
    return E
#print E


def ranklst(E):
    #print "Вычисление списка рангов частичных слау "
    rklst=[]
    for i in range (0,int(len(E))):
        rklst.append(int(len(E[i])))
    return rklst
#print "Таблица En :Список рангов частичных СЛАУ (имя списка rklst)"
def create_rklst(k,m):
    l = create_l(k, m)
    E = LNcreat(l)
    rklst=ranklst(E)
#print rklst


#print ("ГЕНЕРАЦИЯ ИСХОДНОГО МНОГОЧЛЕНА И ПРЕДВАРИТЕЛЬНЫХ КЛЮЧЕЙ")
def BinToDec(sv1):
    svdec1=0
    for i in range (0,int(len(sv1))):
        svdec1=svdec1+sv1[i]*(2**i)
    return svdec1


def generate(n):
    #print "Возвращает ненулевой элемент кольца Z_",n
    a = random.randint(round(n / 2), n - 1)
    return a


def secretvalues(p,A,k,m,n):
    sv=[]
    for i in range (0,Nkm(k,m)):
        sv1=[]
        for j in range (0,n):
            cc=generate(p)
            sv1.append(cc%2)
        cvdec1=BinToDec(sv1)
        sv.append(cvdec1)
    return sv


#sv=secretvalues(p,l)
# print ("Исходный многочлен F(X_1,...,X_k) (имя списка sv): входная случайная бинарная последовательность имитируется псевдо случайным бинарнымгенератором.")
# print ("sv=",sv)
"""
Генерация схемы предварительного распределения ключей
Генерация схемы предварительного распределения ключей
Генерация схемы предварительного распределения ключей
Генерация схемы предварительного распределения ключей
Генерация схемы предварительного распределения ключей
Генерация схемы предварительного распределения ключей
Генерация схемы предварительного распределения ключей
Генерация схемы предварительного распределения ключей
Генерация схемы предварительного распределения ключей
"""

def genScheme(request):
    if request.GET['p_input'] == '' or request.GET['k_input'] == '' or request.GET['m_input'] == '' or request.GET['n_input'] == '':
        return render(request, 'BlomScheme1.html', {'alert1': 'Ошибка: Заполните все поля перед генерацией'})
    elif int(request.GET['k_input']) <= 1:
        return render(request, 'BlomScheme1.html', {'alert1': 'Ошибка: Значение k должно быть больше или равно 2'})
    else:
        test_get_p = int(request.GET['p_input'])
        test_get_k = int(request.GET['k_input'])
        test_get_m = int(request.GET['m_input'])
        test_get_n = int(request.GET['n_input'])
        request.session['test_get_p'] = int(request.GET['p_input'])
        request.session['test_get_k'] = int(request.GET['k_input'])
        request.session['test_get_m'] = int(request.GET['m_input'])
        request.session['test_get_n'] = int(request.GET['n_input'])
        Nkm(test_get_k, test_get_m)
        l = cfind(test_get_k, test_get_m)
        lc = cfind(test_get_k-1, test_get_m)
        R = []

        for i in range(0, int(len(lc))):
            rc = []
            rc.append(lc[i])
            for j in range(0, test_get_m + 1):
                u = cfn(l, lc[i], j, test_get_k, test_get_m)
                rc.append(u)
            R.append(rc)
        # request.session['R'] = R
        E = LNcreat(l,test_get_k)
        # request.session['E'] = E
        rklst = ranklst(E)
        # request.session['rklst'] = rklst
        sv = secretvalues(test_get_p, l, test_get_k, test_get_m, test_get_n)
        request.session['sv'] = sv
        return render(request, 'BlomScheme1.html', {'sv': sv, 'p': test_get_p, 'k': test_get_k, 'm': test_get_m, 'n': test_get_n})


"""
Генерация схемы предварительного распределения ключей
Генерация схемы предварительного распределения ключей
Генерация схемы предварительного распределения ключей
Генерация схемы предварительного распределения ключей
Генерация схемы предварительного распределения ключей
Генерация схемы предварительного распределения ключей
Генерация схемы предварительного распределения ключей
Генерация схемы предварительного распределения ключей
Генерация схемы предварительного распределения ключей
"""


def identifiers(p,n):
    #print "Формирование списка идентификаторов"
    idtf=[]
    for i in range (1,n+1):
       idtf.append(i)
    return idtf


def create_idtf(n):
    idtf=identifiers(n)
    return idtf
#print "Идентификаторы n участников (имя списка idtf)"
#print idtf
def identivierdegrees(idtf,n,m,p):
    idtfd=[]
    for i in range(0,n):
        idtfdraw=[]
        for j in range (0,m+1):
            idtfdraw.append((idtf[i]**(j))%p)
        idtfd.append(idtfdraw)
    return idtfd
#print "Таблица r степеней (от 0 до m-ой)  идентификаторов r_i, i-1,...,n, n участников (имя списка r)"
def create_r(n):
    idtf=identifiers(n)
    r=identivierdegrees(idtf,n)
    return r
# print (r)
def CVal(R,r,sv,m):
    #print "Вычисление слагаемых коэффициентов полиномов F(r_i,X_2,...,X_k), i=1,...,n, n участников и самих этих коэффициентов суммированием слагаемых (имя списка r)"
    cval=[]
    p = 127
    for i in range (0,int(len(R))):
        for s in range (0,int(len(r))):
            cvalraw=[R[i][0]]
            for j in range (0,m+1):
                cvalraw.append((r[s][j]*sv[R[i][1+j]])%p)
            cval.append(cvalraw)
    tt=[]
    for s in range (0,int(len(cval))):
            g=0
            for j in range(0,m+1):
                g=(g+cval[s][j+1])%p
            tt.append(g)
    return (cval,tt)
#print "Слагаемые контрольных коэффициетов полиномов F(r_i,X_2,...,X_k), i=1,...,n, n участников (имя списка slay[0])"
def create_slay(p,k,m,l,n,r):
    sv = secretvalues(p, l, k, m, n)
    slay=CVal(R,r,sv)
    return slay
# print  ("slay0",slay[0])
#print "Таблица K: строка коэффициетов многочленов F(r_i,X_2,...,X_k), i=1,...,n, n участников - получена суммированием по модулю p чисел из элементов списка slay[0] (имя списка slay[1])"
# print  ("slay1",slay[1])
output=[]
def create_output(slay,n):
    for i in range (0, int(int(len(slay[1]))/n)):
        outp=[]
        for j in range(0,n):
            outp.append(slay[1][(n)*i+j])
        output.append(outp)
# print ("Таблица Выход: Список наборов коэффициентов многочленов F(r_i,X_2,...,X_k), i=1,...,n, n участников в порядке возрастания степеней мономов в элементарных многочленах (имя списка output):")
# print ("output=",output)


# print ("ПАРАМЕТРЫ КОНФЕРЕНЦ СВЯЗИ")
# print ("Номера участников конференц-связи (имя списка participants):")
# participants=[1]
# for i in range (2,k+1):
#     participants.append(i)
# participants=[1,2,3,4]
# # print ("participants=",participants)
# # print ("Идентификаторы участников конференц-связи (имя списка participantsID):")
# participantsID=[]
# for i in range (0,k):
#     participantsID.append(idtf[participants[i]])
# print ("participantsID=",participantsID)

def ccfn(A,c,r):
    #print "Определение номера элемента списка A - коэффициента секретного многочлена, соответствующего коэффициенту секретного многочлена для коэффициента c[i] j-го участника"
    u=c+[]
    if u[int(len(u))-1]<=r:
        u.append(r)
    else:
        i=0
        while u[i]<r:
            i=i+1
            #print "i=",i
        #print u
        u.insert(i,r)
        #print u
        c=u+[]
        l=[[0, 0, 0], [0, 0, 1], [0, 1, 1], [1, 1, 1]]
    return [i for i, j in enumerate(l) if j == u][0]

def Rcomputing(l,lc,p,m,k):
    R=[]
    for i in range (0,int(len(lc))):
        rc=[]
        #print "lc,i",lc,i,lc[i]
        rc.append(lc[i])
        #print "rc",rc
        for j in range (0,m+1):
            #print "j=",j
            u=cfn(l,lc[i],j,k,m)
            rc.append(u)
        #print "rc",rc
        R.append(rc)
    return R
# print ("Таблица r степеней (от 0 до m-ой)  идентификаторов r_i, 1,...,k, участников конференц-связи (имя списка r)")
# r=identivierdegrees(participantsID,k)
# print (r)

def LNcreate(l,k):
    LN=[]
    ln=[]
    for j in range (0,int(len(l))-1):
        if ln==[]:
            ln.append(l[j][k-1])
            if l[j+1][k-1]<=l[j][k-1]:
                LN.append(ln)
                ln=[]
        else:
            if l[j+1][k-1]<=l[j][k-1]:
                ln.append(l[j][k-1])
                LN.append(ln)
                ln=[]
            else:
                ln.append(l[j][k-1])
    LN.append([l[int(len(l)-1)][k-1]])
    return(LN)

def CVall(R,r,s,sv,m):
    #print "Вычисление слагаемых коэффициентов полиномов F(r_i,X_2,...,X_k), i=1,...,n, n участников и самих этих коэффициентов суммированием слагаемых (имя списка r)"
    p = 127
    cval=[]
    for i in range (0,int(len(R))):
        cvalraw=[R[i][0]]
        for j in range (0,m+1):
            cvalraw.append((r[s-1][j]*sv[R[i][1+j]])%p)
        cval.append(cvalraw)
    tt=[]
    for s in range (0,int(len(cval))):
            g=0
            for j in range(0,m+1):
                g=(g+cval[s][j+1])%p
            tt.append(g)
    return (cval,tt)

def substitution(sv,p,k,m,s,r):
    #print     "Список коэффициетов многочлена F(X_{i+1),X_{i+2),...,X_k), "
    l=cfind(k,m)
    lc=cfind(k-1,m)
    R=Rcomputing(l,lc,p,m,k)
    #print "Таблица R - таблица координат степеней идентификаторов ri, i=1,...,k (имя списка R)"
    #print R
    #print "Таблица E: списки номеров пользователей в данной группе коэффициентов (имя списка E)"
    E=LNcreate(l,k)
    #print E
    slay=CVall(R,r,s,sv,m)
    #print "Слагаемые  коэффициетов многочлена F(r_{i+1),X_{i+2),...,X_k)"
    #print  "slay0",slay[0]
    #print "Таблица K: список коэффициетов многочлена F(r_{i+1),X_{i+2),...,X_k),  получена суммированием по модулю p чисел из элементов списка slay[0] (имя списка slay[1])"
    #print  "slay1",slay[1]
    return slay[1]

def create_prekey(sv,p,k,m):
    prekey=substitution(sv,p,k,m,1)
    return prekey
# print ("Предварительный ключ первого участника конференц-связи (список prekey):")
# prekey=[114,99,105,56,90,63,76,45,51,104,72,93,67,48,88,79,86,111,48,43]
# print ("prekey=",prekey)
# print ("Ключ конференц-связи участников", participants,"(имя списка key):")
def finalsubstitution(f,r,rr,m,p):
    key=f[0]
    for i in range (0,m):
        key=(key+(f[i+1]*r[rr][i+1])%p)%p
    return key

def create_key(prekey,r,k):
    key= finalsubstitution(prekey,r,k-1)
    return key


"""
Вычисление ключа конференц-связи
Вычисление ключа конференц-связи
Вычисление ключа конференц-связи
Вычисление ключа конференц-связи
Вычисление ключа конференц-связи
Вычисление ключа конференц-связи
Вычисление ключа конференц-связи
Вычисление ключа конференц-связи
Вычисление ключа конференц-связи
"""


def getKeys(request):
    test_get_n = int(request.session['test_get_n'])
    test_get_p = int(request.session['test_get_p'])
    test_get_k = int(request.session['test_get_k'])
    test_get_m = int(request.session['test_get_m'])
    idtf = identifiers(test_get_p, test_get_n)
    r = identivierdegrees(idtf, test_get_n, test_get_m,test_get_p)
    Nkm(test_get_k, test_get_m)
    l = cfind(test_get_k, test_get_m)
    lc = cfind(test_get_k - 1, test_get_m)
    R = []

    for i in range(0, int(len(lc))):
        rc = []
        rc.append(lc[i])
        for j in range(0, test_get_m + 1):
            u = cfn(l, lc[i], j,test_get_k,test_get_m)
            rc.append(u)
        R.append(rc)
    E = LNcreat(l,test_get_k)
    rklst = ranklst(E)
    sv = request.session['sv']
    slay = CVal(R, r, sv, test_get_m)
    output = []
    for i in range(0, int(int(len(slay[1])) / test_get_n)):
        outp = []
        for j in range(0, test_get_n):
            outp.append(slay[1][(test_get_n) * i + j])
        output.append(outp)
    participants = [1]
    for i in range(2, test_get_k + 1):
        participants.append(i)
    # participants = [1, 2, 3, 4]
    if request.GET['participantsID'] == '' or request.GET['key_first'] == '' or request.GET['key_second'] == '':
        return render(request, 'BlomScheme1.html', {'alert1': 'Ошибка: Заполните поле идентификаторов и все поля номеров ключей участников',
                                                    'sv': sv, 'p': test_get_p, 'k': test_get_k, 'm': test_get_m, 'n': test_get_n})
    elif len(request.GET['participantsID'].split(',')) != test_get_k:
        return render(request, 'BlomScheme1.html',
                      {'alert1': 'Ошибка: В списке идентификаторов должно быть ' + str(test_get_k) + ' элементов',
                       'sv': sv, 'p': test_get_p, 'k': test_get_k, 'm': test_get_m, 'n': test_get_n})
    elif request.GET['key_first'] not in request.GET['participantsID']:
        return render(request, 'BlomScheme1.html',
                      {'alert1': 'Ошибка: ' + str(request.GET['key_first']) + ' отсутствует в списке идентификаторов',
                       'sv': sv, 'p': test_get_p, 'k': test_get_k, 'm': test_get_m, 'n': test_get_n})
    elif request.GET['key_second'] not in request.GET['participantsID']:
        return render(request, 'BlomScheme1.html',
                      {'alert1': 'Ошибка: ' + str(request.GET['key_second']) + ' отсутствует в списке идентификаторов',
                       'sv': sv, 'p': test_get_p, 'k': test_get_k, 'm': test_get_m, 'n': test_get_n})
    else:
        participantss = request.GET['participantsID']
        request.session['participantss'] = request.GET['participantsID']
        participantsI = participantss.split(',')
        participantsID = [int(item) for item in participantsI]
        for i in range(0, test_get_k):
            participantsID.append(idtf[participants[i]])
        r = identivierdegrees(participantsID, test_get_k,test_get_m,test_get_p)
        key_one = int(request.GET['key_first'])
        request.session['key_one'] = int(request.GET['key_first'])
        key_two = int(request.GET['key_second'])
        request.session['key_two'] = int(request.GET['key_second'])
        prekey_first = substitution(sv, test_get_p, test_get_k, test_get_m, key_one, r)
        key_first = finalsubstitution(prekey_first, r, test_get_k - 1, test_get_m, test_get_p)
        request.session['key_first'] = key_first
        prekey_second = substitution(sv, test_get_p, test_get_k, test_get_m, key_two, r)
        key_second = finalsubstitution(prekey_second, r, test_get_k - 1, test_get_m, test_get_p)
        if key_first == key_first:
            res = 'Совпадение m ключей: True'
        return render(request, 'BlomScheme1.html', {'key_first': key_first, 'participantsID': participantss,
                                                    'key_second': key_first, 'prekey_first': prekey_first,
                                                    'prekey_second': prekey_second, 'sv': sv, 'res': res,
                                                    'p': test_get_p, 'k': test_get_k, 'm': test_get_m, 'n': test_get_n,
                                                    'key_one': key_one, 'key_two': key_two})


"""
Вычисление ключа конференц-связи
Вычисление ключа конференц-связи
Вычисление ключа конференц-связи
Вычисление ключа конференц-связи
Вычисление ключа конференц-связи
Вычисление ключа конференц-связи
Вычисление ключа конференц-связи
Вычисление ключа конференц-связи
Вычисление ключа конференц-связи
"""


def gauss(M, p):
    n = len(M)
    m = n + 1
    for i in range(0, n):
        z = p
        a = p
        b = M[i][i + 1]
        x, xx, y, yy = 1, 0, 0, 1
        while b:
            q = a // b
            a, b = b, a % b
            x, xx = xx, x - xx * q
            y, yy = yy, y - yy * q
        if y < 0:
            y = z + y
        inv = y
        for j in range(0, m):
            M[i][j] = (M[i][j] * inv) % p
        for k in range(i + 1, n):
            c = M[k][i + 1]
            for j in range(0, m):
                M[k][j] = (p + (M[k][j] - (M[i][j] * c) % p) % p) % p
    for i in range(n - 1, 0, -1):
        for k in range(i - 1, -1, -1):
            c = M[k][i + 1]
            for j in range(0, m):
                M[k][j] = (p + (M[k][j] - (M[i][j] * c) % p) % p) % p
    q = []
    for i in range(0, n):
        q.append(M[i][0])
    return q


# compromat = output
# slau1 = []
# for i in range(0, int(len(compromat))):
#     for j in range(0, m + 1):
#         print
#         slau1.append(compromat[i][j])
# print("Таблица K: строка коэффициетов m+1 многочленов F(r_i,X_2,...,X_k) m+1 участников участников (имя списка slay1)")
# print(slau1)
#
# print("Определение числа участников привилегированной группы")

def participantsnumber(lst, m):
    K = []
    k = 1
    for i in range(0, m):
        K.append(2 + i)
    while K[m - 1] != 4 and k < 15:  # int(len(compromat)) and k<15:
        k = k + 1
        r = K[0] + 1
        K.pop(0)
        K.insert(0, r)
        for i in range(1, m):
            r = K[i - 1] + K[i]
            K.pop(i)
            K.insert(i, r)
    return k


def NKM(k, m):
    K = []
    for i in range(0, m):
        K.append(2 + i)
    for i in range(0, k - 1):
        r = K[0] + 1
        K.pop(0)
        K.insert(0, r)
        for j in range(1, m):
            r = K[j - 1] + K[j]
            K.pop(j)
            K.insert(j, r)
    return K[m - 1]

nkm = NKM(4, 3)
def identivierdegreees(idtf, m, p):
    idtfd = []
    for i in range(0, m + 1):
        idtfdraw = [1]
        for j in range(0, m):
            idtfdraw.append((idtf[i] ** (j + 1)) % p)
        idtfd.append(idtfdraw)
    return idtfd
# print "Таблица r степеней (от 0 до m-ой) m+1 выбранных подряд, начиная с нулевого, идентификаторов m+1-го участника (имя списка r)"
# r = identivierdegreees(idtf, m)
# print r
print("КРИПТОАНАЛИЗ: СОСТАВЛЕНИЕ И РЕШЕНИЕ СИСТЕМЫ СЛАУ (по таблицам Е,En, R и K)")
def createSLAU(e, r, i,rklst,E,slau1,m):
    # print "Состаление очередной СЛАУ"
    SLAU1 = []
    for j in range(int(len(E[0])) - rklst[i], int(len(E[0]))):
        tt = slau1[(m + 1) * i + j]
        # print "i,j,tt",i,j,tt
        Row = [tt]
        for s in range(0, int(len(r))):
            Row.append(r[j][s])
        SLAU1.append(Row)
    return SLAU1

def slaulist(e, r, rklst,E,slau1,m):
    slist1 = []
    for i in range(0, int(len(rklst))):
        slist2 = createSLAU(e, r, i,rklst,E,slau1,m)  # (m+1)-rklst[i])
        slist1.append(slist2)
    return slist1


def redusing(slist1, R, sln, rklst, i, j, s,m,p):
    # print "Модификация левых частей уравнений с учетом номера группы коэффициентов и вычисленных значений исходного полинома"
    slist11 = slist1 + []
    slist11[i][j][0] = (slist11[i][j][0] - (
                sln[(R[i][1 + m - rklst[i] - s])] * slist11[i][j][1 + m - rklst[i] - s]) % p) % p
    slist11[i][j].pop(1 + m - rklst[i] - s)
    return slist11

def gauss(M, p):
    n = len(M)
    m = n + 1
    for i in range(0, n):
        z = p
        a = p
        b = M[i][i + 1]
        x, xx, y, yy = 1, 0, 0, 1
        while b:
            q = a // b
            a, b = b, a % b
            x, xx = xx, x - xx * q
            y, yy = yy, y - yy * q
        if y < 0:
            y = z + y
        inv = y
        for j in range(0, m):
            M[i][j] = (M[i][j] * inv) % p
        for k in range(i + 1, n):
            c = M[k][i + 1]
            for j in range(0, m):
                M[k][j] = (p + (M[k][j] - (M[i][j] * c) % p) % p) % p
    for i in range(n - 1, 0, -1):
        for k in range(i - 1, -1, -1):
            c = M[k][i + 1]
            for j in range(0, m):
                M[k][j] = (p + (M[k][j] - (M[i][j] * c) % p) % p) % p
    q = []
    for i in range(0, n):
        q.append(M[i][0])
    return q


"""
Вскрытие схемы Блома
Вскрытие схемы Блома
Вскрытие схемы Блома
Вскрытие схемы Блома
Вскрытие схемы Блома
Вскрытие схемы Блома
Вскрытие схемы Блома
Вскрытие схемы Блома
Вскрытие схемы Блома
"""
def openSchemeOb(request):
    test_get_n = int(request.session['test_get_n'])
    test_get_p = int(request.session['test_get_p'])
    test_get_k = int(request.session['test_get_k'])
    test_get_m = int(request.session['test_get_m'])
    key_one = request.session['key_one']
    key_two = request.session['key_two']
    participantsss = request.session['participantss']
    list_of_n = []
    for i in range(1, test_get_n + 1):
        list_of_n.append(str(i))
    idtf = identifiers(test_get_p, test_get_n)
    r = identivierdegrees(idtf, test_get_n, test_get_m, test_get_p)
    Nkm(test_get_k, test_get_m)
    l = cfind(test_get_k, test_get_m)
    lc = cfind(test_get_k - 1, test_get_m)
    R = []

    for i in range(0, int(len(lc))):
        rc = []
        rc.append(lc[i])
        for j in range(0, test_get_m + 1):
            u = cfn(l, lc[i], j, test_get_k, test_get_m)
            rc.append(u)
        R.append(rc)
    E = LNcreat(l, test_get_k)
    rklst = ranklst(E)
    sv = request.session['sv']
    slay = CVal(R, r, sv, test_get_m)
    output = []
    for i in range(0, int(int(len(slay[1])) / test_get_n)):
        outp = []
        for j in range(0, test_get_n):
            outp.append(slay[1][(test_get_n) * i + j])
        output.append(outp)
    participants = [1]
    for i in range(2, test_get_k + 1):
        participants.append(i)
    if request.GET['list_of_idtf'] == '':
        return render(request, 'BlomScheme1.html', {'p': test_get_p, 'k': test_get_k, 'm': test_get_m, 'n': test_get_n,
                                                    'key_one': key_one, 'key_two': key_two, 'sv': sv,
                                                    'alert1': 'Ошибка: Заполните список идентификаторов'})
    elif len(request.GET['list_of_idtf'].split(',')) > (test_get_n) or len(request.GET['list_of_idtf'].split(',')) < len(participantsss.split(',')):
        return render(request, 'BlomScheme1.html', {'p': test_get_p, 'k': test_get_k, 'm': test_get_m, 'n': test_get_n,
                                                    'key_one': key_one, 'key_two': key_two, 'sv': sv,
                                                    'alert1': 'Ошибка: Для вскрытия должно быть не меньше m+1 участников, но не более n'})
    elif list(set(request.GET['list_of_idtf'].split(',')) - set(list_of_n)) != []:
        return render(request, 'BlomScheme1.html', {'p': test_get_p, 'k': test_get_k, 'm': test_get_m, 'n': test_get_n,
                                                    'key_one': key_one, 'key_two': key_two, 'sv': sv,
                                                    'alert1': 'Ошибка: В списке идентификаторов присутствует идентификатор, не относящийся к идентификатором участников'})
    else:
        participantss = request.GET['list_of_idtf']
        request.session['list_of_idtfi'] = request.GET['list_of_idtf']
        participantsI = participantss.split(',')
        participantsID = [int(item) for item in participantsI]
        for i in range(0, test_get_k):
            participantsID.append(idtf[participants[i]])
        r = identivierdegrees(participantsID, test_get_n, test_get_m, test_get_p)
        dict = {}
        for i in range(0, len(participantsI)):
            prekey = substitution(sv, test_get_p, test_get_k, test_get_m, int(participantsI[i]), r)
            k = 'Предварительный ключ ' + str(participantsI[i]) + '-го участника'
            dict[k] = prekey
        prekey_first = substitution(sv, test_get_p, test_get_k, test_get_m, key_one, r)
        key_first = finalsubstitution(prekey_first, r, test_get_k - 1, test_get_m, test_get_p)
        prekey_second = substitution(sv, test_get_p, test_get_k, test_get_m, key_two, r)
        key_second = finalsubstitution(prekey_second, r, test_get_k - 1, test_get_m, test_get_p)
        if key_first == key_first:
            res = 'Совпадение m ключей: True'
        return render(request, 'BlomScheme1.html', {'key_first': key_first, 'key_second': key_first, 'prekey_first': prekey_first,
                                                    'prekey_second': prekey_second,
                                                    'sv': sv, 'res': res, 'test_get_m': test_get_m,
                                                    'test_get_k': test_get_k, 'dict': dict,
                                                    'p': test_get_p, 'k': test_get_k, 'm': test_get_m, 'n': test_get_n,
                                                    'key_one': key_one, 'key_two': key_two, 'participantsID': participantsss})


def openSchemeScr(request):
    test_get_n = int(request.session['test_get_n'])
    test_get_p = int(request.session['test_get_p'])
    test_get_k = int(request.session['test_get_k'])
    test_get_m = int(request.session['test_get_m'])
    key_one = request.session['key_one']
    key_two = request.session['key_two']
    participantsss = request.session['participantss']
    list_of_idtfi = request.session['list_of_idtfi']
    idtf = identifiers(test_get_p, test_get_n)
    r = identivierdegrees(idtf, test_get_n, test_get_m, test_get_p)
    Nkm(test_get_k, test_get_m)
    l = cfind(test_get_k, test_get_m)
    lc = cfind(test_get_k - 1, test_get_m)
    R = []

    for i in range(0, int(len(lc))):
        rc = []
        rc.append(lc[i])
        for j in range(0, test_get_m + 1):
            u = cfn(l, lc[i], j, test_get_k, test_get_m)
            rc.append(u)
        R.append(rc)
    E = LNcreat(l, test_get_k)
    rklst = ranklst(E)
    sv = request.session['sv']
    slay = CVal(R, r, sv, test_get_m)
    output = []
    for i in range(0, int(int(len(slay[1])) / test_get_n)):
        outp = []
        for j in range(0, test_get_n):
            outp.append(slay[1][(test_get_n) * i + j])
        output.append(outp)
    participants = [1]
    for i in range(2, test_get_k + 1):
        participants.append(i)
    participants = [1, 2, 3, 4]
    participantsI = list_of_idtfi.split(',')
    participantsID = [int(item) for item in participantsI]
    for i in range(0, test_get_k):
        participantsID.append(idtf[participants[i]])
    r = identivierdegrees(participantsID, test_get_n, test_get_m, test_get_p)
    dict = {}
    for i in range(0, len(participantsI)):
        prekey = substitution(sv, test_get_p, test_get_k, test_get_m, int(participantsI[i]), r)
        k = 'Предварительный ключ ' + str(participantsI[i]) + '-го участника'
        dict[k] = prekey
    prekey_first = substitution(sv, test_get_p, test_get_k, test_get_m, key_one, r)
    key_first = finalsubstitution(prekey_first, r, test_get_k - 1, test_get_m, test_get_p)
    prekey_second = substitution(sv, test_get_p, test_get_k, test_get_m, key_two, r)
    key_second = finalsubstitution(prekey_second, r, test_get_k - 1, test_get_m, test_get_p)
    if key_first == key_first:
        res = 'Совпадение m ключей: True'


    compromat = output
    slau1 = []
    for i in range(0, int(len(compromat))):
        for j in range(0, test_get_m + 1):
            slau1.append(compromat[i][j])

    r = identivierdegreees(idtf, test_get_m, test_get_p)
    slist1 = slaulist(E, r, rklst,E,slau1,test_get_m)
    ss = slist1 + []
    sln = []
    for i in range(0, int(len(rklst))):
        for s in range(0, 1 + test_get_m - rklst[i]):
            for j in range(0, rklst[i]):
                ss = redusing(ss, R, sln, rklst, i, j, s, test_get_m, test_get_p)
        gs = gauss(ss[i], test_get_p)
        for test_get_k in range(0, int(len(gs))):
            sln.append(gs[test_get_k])
    slist1 = slaulist(E, r, rklst, E, slau1, test_get_m)
    first_slau = slist1[:1]
    return render(request, 'BlomScheme1.html', {'key_first': key_first, 'key_second': key_first, 'prekey_first': prekey_first,
                                                'prekey_second': prekey_second,
                                                'sv': sv, 'res': res, 'test_get_m': test_get_m,
                                                'test_get_k': test_get_k, 'rklst': rklst, 'r': r,
                                                'first_slau': first_slau, 'dict': dict,
                                                'p': test_get_p, 'k': test_get_k, 'm': test_get_m, 'n': test_get_n,
                                                'key_one': key_one, 'key_two': key_two, 'participantsID': participantsss})


def openSchemeBd(request):
    test_get_n = int(request.session['test_get_n'])
    test_get_p = int(request.session['test_get_p'])
    test_get_k = int(request.session['test_get_k'])
    test_get_m = int(request.session['test_get_m'])
    key_one = request.session['key_one']
    key_two = request.session['key_two']
    participantsss = request.session['participantss']
    list_of_idtfi = request.session['list_of_idtfi']
    idtf = identifiers(test_get_p, test_get_n)
    r = identivierdegrees(idtf, test_get_n, test_get_m, test_get_p)
    Nkm(test_get_k, test_get_m)
    l = cfind(test_get_k, test_get_m)
    lc = cfind(test_get_k - 1, test_get_m)
    R = []

    for i in range(0, int(len(lc))):
        rc = []
        rc.append(lc[i])
        for j in range(0, test_get_m + 1):
            u = cfn(l, lc[i], j, test_get_k, test_get_m)
            rc.append(u)
        R.append(rc)
    E = LNcreat(l, test_get_k)
    rklst = ranklst(E)
    sv = request.session['sv']
    slay = CVal(R, r, sv, test_get_m)
    output = []
    for i in range(0, int(int(len(slay[1])) / test_get_n)):
        outp = []
        for j in range(0, test_get_n):
            outp.append(slay[1][(test_get_n) * i + j])
        output.append(outp)
    participants = [1]
    for i in range(2, test_get_k + 1):
        participants.append(i)
    participantsI = list_of_idtfi.split(',')
    participantsID = [int(item) for item in participantsI]
    for i in range(0, test_get_k):
        participantsID.append(idtf[participants[i]])
    r = identivierdegrees(participantsID, test_get_n, test_get_m, test_get_p)
    dict = {}
    for i in range(0, len(participantsI)):
        prekey = substitution(sv, test_get_p, test_get_k, test_get_m, int(participantsI[i]), r)
        k = 'Предварительный ключ ' + str(participantsI[i]) + '-го участника'
        dict[k] = prekey
    prekey_first = substitution(sv, test_get_p, test_get_k, test_get_m, key_one, r)
    key_first = finalsubstitution(prekey_first, r, test_get_k - 1, test_get_m, test_get_p)
    prekey_second = substitution(sv, test_get_p, test_get_k, test_get_m, key_two, r)
    key_second = finalsubstitution(prekey_second, r, test_get_k - 1, test_get_m, test_get_p)
    if key_first == key_first:
        res = 'Совпадение m ключей: True'


    compromat = output
    slau1 = []
    for i in range(0, int(len(compromat))):
        for j in range(0, test_get_m + 1):
            slau1.append(compromat[i][j])

    r = identivierdegreees(idtf, test_get_m, test_get_p)
    slist1 = slaulist(E, r, rklst,E,slau1,test_get_m)
    ss = slist1 + []
    sln = []
    for i in range(0, int(len(rklst))):
        for s in range(0, 1 + test_get_m - rklst[i]):
            for j in range(0, rklst[i]):
                ss = redusing(ss, R, sln, rklst, i, j, s, test_get_m, test_get_p)
        gs = gauss(ss[i], test_get_p)
        for test_get_k in range(0, int(len(gs))):
            sln.append(gs[test_get_k])
    slist1 = slaulist(E, r, rklst, E, slau1, test_get_m)
    first_slau = slist1[:1]
    second_right_slau = str(slist1[1:2][0])
    second_slau = request.GET['build_slau']
    count = 0
    if second_slau == second_right_slau:
        res_comp = 'Построена верно, 2-ая СЛАУ: '
        return render(request, 'BlomScheme1.html',
                      {'key_first': key_first, 'key_second': key_first, 'prekey_first': prekey_first,
                       'prekey_second': prekey_second,
                       'sv': sv, 'res': res, 'test_get_m': test_get_m,
                       'test_get_k': test_get_k, 'rklst': rklst, 'r': r, 'first_slau': first_slau,
                       'light_first_slau': first_slau, 'dict': dict, 'slau': slist1, 'second_slau': res_comp, 'second_right_slau': second_right_slau,
                       'p': test_get_p, 'k': test_get_k, 'm': test_get_m, 'n': test_get_n,
                       'key_one': key_one, 'key_two': key_two, 'participantsID': participantsss})
    else:
        count += 1
        res_comp = 'Построена неверно. Количество ошибок: ' + str(count)
        return render(request, 'BlomScheme1.html',
                      {'key_first': key_first, 'key_second': key_first, 'prekey_first': prekey_first,
                       'prekey_second': prekey_second,
                       'sv': sv, 'res': res, 'test_get_m': test_get_m,
                       'test_get_k': test_get_k, 'rklst': rklst, 'r': r, 'first_slau': first_slau,
                       'dict': dict, 'second_slau': res_comp,
                       'p': test_get_p, 'k': test_get_k, 'm': test_get_m, 'n': test_get_n,
                       'key_one': key_one, 'key_two': key_two, 'participantsID': participantsss})


def openScheme(request):
    test_get_n = int(request.session['test_get_n'])
    test_get_p = int(request.session['test_get_p'])
    test_get_k = int(request.session['test_get_k'])
    test_get_m = int(request.session['test_get_m'])
    key_one = request.session['key_one']
    key_two = request.session['key_two']
    participantsss = request.session['participantss']
    list_of_idtfi = request.session['list_of_idtfi']
    idtf = identifiers(test_get_p, test_get_n)
    r = identivierdegrees(idtf, test_get_n, test_get_m, test_get_p)
    Nkm(test_get_k, test_get_m)
    l = cfind(test_get_k, test_get_m)
    lc = cfind(test_get_k - 1, test_get_m)
    R = []

    for i in range(0, int(len(lc))):
        rc = []
        rc.append(lc[i])
        for j in range(0, test_get_m + 1):
            u = cfn(l, lc[i], j, test_get_k, test_get_m)
            rc.append(u)
        R.append(rc)
    E = LNcreat(l, test_get_k)
    rklst = ranklst(E)
    sv = request.session['sv']
    slay = CVal(R, r, sv, test_get_m)
    output = []
    for i in range(0, int(int(len(slay[1])) / test_get_n)):
        outp = []
        for j in range(0, test_get_n):
            outp.append(slay[1][(test_get_n) * i + j])
        output.append(outp)
    participants = [1]
    for i in range(2, test_get_k + 1):
        participants.append(i)
    participantsI = list_of_idtfi.split(',')
    participantsID = [int(item) for item in participantsI]
    for i in range(0, test_get_k):
        participantsID.append(idtf[participants[i]])
    r = identivierdegrees(participantsID, test_get_n, test_get_m, test_get_p)
    dict = {}
    for i in range(0, len(participantsI)):
        prekey = substitution(sv, test_get_p, test_get_k, test_get_m, int(participantsI[i]), r)
        k = 'Предварительный ключ ' + str(participantsI[i]) + '-го участника'
        dict[k] = prekey
    prekey_first = substitution(sv, test_get_p, test_get_k, test_get_m, key_one, r)
    key_first = finalsubstitution(prekey_first, r, test_get_k - 1, test_get_m, test_get_p)
    prekey_second = substitution(sv, test_get_p, test_get_k, test_get_m, key_two, r)
    key_second = finalsubstitution(prekey_second, r, test_get_k - 1, test_get_m, test_get_p)
    if key_first == key_first:
        res = 'Совпадение m ключей: True'


    compromat = output
    slau1 = []
    for i in range(0, int(len(compromat))):
        for j in range(0, test_get_m + 1):
            slau1.append(compromat[i][j])

    r = identivierdegreees(idtf, test_get_m, test_get_p)
    slist1 = slaulist(E, r, rklst,E,slau1,test_get_m)
    ss = slist1 + []
    sln = []
    for i in range(0, int(len(rklst))):
        for s in range(0, 1 + test_get_m - rklst[i]):
            for j in range(0, rklst[i]):
                ss = redusing(ss, R, sln, rklst, i, j, s, test_get_m, test_get_p)
        gs = gauss(ss[i], test_get_p)
        for test_get_k in range(0, int(len(gs))):
            sln.append(gs[test_get_k])
    slist1 = slaulist(E, r, rklst, E, slau1, test_get_m)
    second_right_slau = str(slist1[1:2][0])
    slist2 = slaulist(E, r, rklst, E, slau1, test_get_m)
    first_slau = slist1[:1]
    for i in range(len(slist2[1:2][0])):
        p = int(slist2[1:2][0][i][0] - sv[1])
        if p < 0:
            slist2[1:2][0][i][0] = p + 127
            del slist2[1:2][0][i][1]
        else:
            slist2[1:2][0][i][0] = p
            del slist2[1:2][0][i][1]
    second_light_right_slau = str(slist2[1:2][0])
    second_light_slau = request.GET['result_slau']
    count1 = 0
    if sv == sv:
        resule = 'True'
    else:
        resule = 'False'
    if second_light_slau == second_light_right_slau:
        res_fin = 'Построена верно, 2-ая упрощенная СЛАУ: '
        return render(request, 'BlomScheme1.html', {'key_first': key_first, 'key_second': key_first, 'prekey_first': prekey_first,
                                                    'prekey_second': prekey_second, 'second_right_slau': second_right_slau,
                                                    'sv': sv, 'res': res, 'test_get_m': test_get_m,
                                                    'test_get_k': test_get_k, 'rklst': rklst, 'r': r,
                                                    'slau1': slau1, 'resul': sv, 'resule': resule,
                                                    'light_first_slau': first_slau, 'dict': dict, 'slau': slist1,
                                                    'first_slau': first_slau, 'second_light_slau': res_fin,
                                                    'second_light_right_slau': second_light_right_slau, 'p': test_get_p,
                                                    'k': test_get_k, 'm': test_get_m, 'n': test_get_n,
                                                    'key_one': key_one, 'key_two': key_two, 'participantsID': participantsss})
    else:
        count1 += 1
        res_fin = 'Построена неверно. Количество ошибок: ' + str(count1)
        return render(request, 'BlomScheme1.html',
                      {'key_first': key_first, 'key_second': key_first, 'prekey_first': prekey_first,
                       'prekey_second': prekey_second, 'second_right_slau': second_right_slau,
                       'sv': sv, 'res': res, 'test_get_m': test_get_m,
                       'test_get_k': test_get_k, 'rklst': rklst, 'r': r,
                       'slau1': slau1, 'light_first_slau': first_slau, 'dict': dict, 'slau': slist1,
                       'first_slau': first_slau, 'second_light_slau': res_fin,
                       'p': test_get_p, 'k': test_get_k, 'm': test_get_m, 'n': test_get_n,
                       'key_one': key_one, 'key_two': key_two, 'participantsID': participantsss})


"""
Вскрытие схемы Блома
Вскрытие схемы Блома
Вскрытие схемы Блома
Вскрытие схемы Блома
Вскрытие схемы Блома
Вскрытие схемы Блома
Вскрытие схемы Блома
Вскрытие схемы Блома
Вскрытие схемы Блома
"""