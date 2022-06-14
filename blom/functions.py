import random


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


p = 127
k = 4
m = 3
n = 7


def DecToBin(a):
    #print "Возвращает список значений двоичных разрядов, начиная со старшенго"
    Blist=[]
    while not a==0:
        b=a/2
        Blist.append(a-b*2)
        a=b
    return Blist


# n=7
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


def cfn(A,c,r):
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
    return [i for i, j in enumerate(l) if j == u][0]


l=cfind(k,m)
lc=cfind(k-1,m)
#print "Таблица А - список индексов коэффициентов исходного полинома F(X_1,...,X_k) (имя списка - l)"
#print l
#print "Таблица С - список индексов коэффициентов полиномов F(r_i,X_2,...,X_k), i=1,...,n, n участников  (имя списка - lc)"
#print lc
R=[]

for i in range (0,int(len(lc))):
    rc=[]
    rc.append(lc[i])
    for j in range (0,m+1):
        u=cfn(l,lc[i],j)
        rc.append(u)
    R.append(rc)
#print "Таблица R - таблица координат степеней идентификаторов ri, i=1,...,n (имя списка R)"
#print R


def LNcreat(l):
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
E=LNcreat(l)
#print E


def ranklst(E):
    #print "Вычисление списка рангов частичных слау "
    rklst=[]
    for i in range (0,int(len(E))):
        rklst.append(int(len(E[i])))
    return rklst
#print "Таблица En :Список рангов частичных СЛАУ (имя списка rklst)"
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


def secretvalues(p,A):
    sv=[]
    for i in range (0,Nkm(k,m)):
        sv1=[]
        for j in range (0,n):
            cc=generate(p)
            sv1.append(cc%2)
        cvdec1=BinToDec(sv1)
        sv.append(cvdec1)
    return sv


sv=secretvalues(p,l)
# print ("Исходный многочлен F(X_1,...,X_k) (имя списка sv): входная случайная бинарная последовательность имитируется псевдо случайным бинарнымгенератором.")
# print ("sv=",sv)


def identifiers(p):
    #print "Формирование списка идентификаторов"
    idtf=[]
    for i in range (1,n+1):
       idtf.append(i)
    return idtf
idtf=identifiers(n)
#print "Идентификаторы n участников (имя списка idtf)"
#print idtf
def identivierdegrees(idtf,n):
    idtfd=[]
    for i in range(0,n):
        idtfdraw=[]
        for j in range (0,m+1):
            idtfdraw.append((idtf[i]**(j))%p)
        idtfd.append(idtfdraw)
    return idtfd
#print "Таблица r степеней (от 0 до m-ой)  идентификаторов r_i, i-1,...,n, n участников (имя списка r)"
r=identivierdegrees(idtf,n)
# print (r)
def CVal(R,r,sv):
    #print "Вычисление слагаемых коэффициентов полиномов F(r_i,X_2,...,X_k), i=1,...,n, n участников и самих этих коэффициентов суммированием слагаемых (имя списка r)"
    cval=[]
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
slay=CVal(R,r,sv)
# print  ("slay0",slay[0])
#print "Таблица K: строка коэффициетов многочленов F(r_i,X_2,...,X_k), i=1,...,n, n участников - получена суммированием по модулю p чисел из элементов списка slay[0] (имя списка slay[1])"
# print  ("slay1",slay[1])
output=[]
for i in range (0, int(int(len(slay[1]))/n)):
    outp=[]
    for j in range(0,n):
        outp.append(slay[1][(n)*i+j])
    output.append(outp)
# print ("Таблица Выход: Список наборов коэффициентов многочленов F(r_i,X_2,...,X_k), i=1,...,n, n участников в порядке возрастания степеней мономов в элементарных многочленах (имя списка output):")
# print ("output=",output)


# print ("ПАРАМЕТРЫ КОНФЕРЕНЦ СВЯЗИ")
# print ("Номера участников конференц-связи (имя списка participants):")
participants=[1]
for i in range (2,k+1):
    participants.append(i)
participants=[1,2,3,4]
# print ("participants=",participants)
# print ("Идентификаторы участников конференц-связи (имя списка participantsID):")
participantsID=[]
for i in range (0,k):
    participantsID.append(idtf[participants[i]])
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

def Rcomputing(l,lc,p,m):
    R=[]
    for i in range (0,int(len(lc))):
        rc=[]
        #print "lc,i",lc,i,lc[i]
        rc.append(lc[i])
        #print "rc",rc
        for j in range (0,m+1):
            #print "j=",j
            u=cfn(l,lc[i],j)
            rc.append(u)
        #print "rc",rc
        R.append(rc)
    return R
# print ("Таблица r степеней (от 0 до m-ой)  идентификаторов r_i, 1,...,k, участников конференц-связи (имя списка r)")
r=identivierdegrees(participantsID,k)
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

def CVall(R,r,s,sv):
    #print "Вычисление слагаемых коэффициентов полиномов F(r_i,X_2,...,X_k), i=1,...,n, n участников и самих этих коэффициентов суммированием слагаемых (имя списка r)"
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

def substitution(sv,p,k,m,s):
    #print     "Список коэффициетов многочлена F(X_{i+1),X_{i+2),...,X_k), "
    l=cfind(k,m)
    lc=cfind(k-1,m)
    R=Rcomputing(l,lc,p,m)
    #print "Таблица R - таблица координат степеней идентификаторов ri, i=1,...,k (имя списка R)"
    #print R
    #print "Таблица E: списки номеров пользователей в данной группе коэффициентов (имя списка E)"
    E=LNcreate(l,k)
    #print E
    slay=CVall(R,r,s,sv)
    #print "Слагаемые  коэффициетов многочлена F(r_{i+1),X_{i+2),...,X_k)"
    #print  "slay0",slay[0]
    #print "Таблица K: список коэффициетов многочлена F(r_{i+1),X_{i+2),...,X_k),  получена суммированием по модулю p чисел из элементов списка slay[0] (имя списка slay[1])"
    #print  "slay1",slay[1]
    return slay[1]
prekey=substitution(sv,p,k,m,1)
# print ("Предварительный ключ первого участника конференц-связи (список prekey):")
# prekey=[114,99,105,56,90,63,76,45,51,104,72,93,67,48,88,79,86,111,48,43]
# print ("prekey=",prekey)
# print ("Ключ конференц-связи участников", participants,"(имя списка key):")
def finalsubstitution(f,r,rr):
    key=f[0]
    for i in range (0,m):
        key=(key+(f[i+1]*r[rr][i+1])%p)%p
    return key
key= finalsubstitution(prekey,r,k-1)
print (key)


print("Программа вскрытия схемы предварительного распределения ключей Блома")
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

print("УСТАНОВКА ИСХОДНЫХ ДАННЫХ")
p = 127
print("Порядок поля p=", p)
print("Список идентификаторов скомпрометированных участников (имя списка idtf)")
# idtf = [0, 1, 2, 3]
print(idtf)
print("Список списков коэффициентов скомпрометированных многочленов (имя списка compromat)")
print("Наборы коэффициентов перечисляются в порядке возрастания степеней мономов в элементарных многочленах")
#compromat = [[7, 114, 64, 47, 126, 110, 62], [58, 99, 46, 126, 58, 69, 5], [75, 105, 7, 30, 42, 38, 13], [105, 56, 18, 82, 85, 118, 18], [69, 90, 58, 26, 47, 47, 79], [57, 63, 57, 98, 118, 49, 77], [115, 76, 39, 101, 105, 21, 73], [85, 45, 61, 119, 78, 51, 24], [78, 51, 71, 58, 59, 121, 37], [82, 104, 63, 89, 58, 100, 91], [102, 72, 110, 49, 103, 105, 15], [8, 93, 36, 15, 81, 31, 43], [18, 67, 94, 16, 4, 102, 100], [0, 48, 64, 33, 67, 24, 16], [75, 88, 44, 44, 62, 72, 48], [30, 79, 80, 98, 71, 64, 15], [66, 86, 21, 44, 74, 30, 85], [72, 111, 64, 92, 102, 1, 77], [68, 48, 68, 100, 116, 88, 115], [46, 43, 37, 10, 71, 75, 4]]
compromat = output
print(compromat)
# m = int(len(compromat[0])) - 1
m = 3
print("ВЫЧИСЛЕНИЕ ПРОИЗВОДНЫХ ПАРАМЕТРОВ")
print("Степень многочлена F(X_1,...,X_k) по каждой переменной m=", m)

slau1 = []
for i in range(0, int(len(compromat))):
    for j in range(0, m + 1):
        print
        slau1.append(compromat[i][j])
print("Таблица K: строка коэффициетов m+1 многочленов F(r_i,X_2,...,X_k) m+1 участников участников (имя списка slay1)")
print(slau1)

print("Определение числа участников привилегированной группы")

def participantsnumber(lst):
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

# k = participantsnumber(slau1)
k = 4
print("k=", k)
print("Вычисление числа n(k,m)")

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
print("nkm=", nkm)

l = cfind(k, m)
lc = cfind(k - 1, m)

R = []

for i in range(0, int(len(lc))):
    rc = []
    rc.append(lc[i])
    for j in range(0, m + 1):
        u = cfn(l, lc[i], j)
        rc.append(u)
    R.append(rc)
# print "Таблица R - таблица координат степеней идентификаторов ri (имя списка R)"
# print R
rklst = ranklst(E)
# print rklst
def identivierdegrees(idtf, m):
    idtfd = []
    for i in range(0, m + 1):
        idtfdraw = [1]
        for j in range(0, m):
            idtfdraw.append((idtf[i] ** (j + 1)) % p)
        idtfd.append(idtfdraw)
    return idtfd
print ("Таблица r степеней (от 0 до m-ой) m+1 выбранных подряд, начиная с нулевого, идентификаторов m+1-го участника (имя списка r)")
r = identivierdegrees(idtf, m)
print (r)
print("КРИПТОАНАЛИЗ: СОСТАВЛЕНИЕ И РЕШЕНИЕ СИСТЕМЫ СЛАУ (по таблицам Е,En, R и K)")
def createSLAU(e, r, i):
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

def slaulist(e, r, rklst):
    slist1 = []
    for i in range(0, int(len(rklst))):
        slist2 = createSLAU(e, r, i)  # (m+1)-rklst[i])
        slist1.append(slist2)
    return slist1
print('-----------------------------')
print('E =', E)
print('r =', r)
print('rklst =', rklst)
print('-----------------------------')

slist1 = slaulist(E, r, rklst)
print("Построенная система слау (имя списка slist1)")
print("slist1", slist1)
print("Полученные слау позволяют восстановить искодный полином F(X_1,...,X_k) (имя списка sv)")


def redusing(slist1, R, sln, rklst, i, j, s):
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


print("Восстановление исходного полинома последовательным решением уравнений из списка СЛАУ")
ss = slist1 + []
sln = []
for i in range(0, int(len(rklst))):
    # print "i,,m+1-(m+1-rklst[i])",i,(m+1-rklst[i])
    for s in range(0, 1 + m - rklst[i]):
        # print "s",s
        for j in range(0, rklst[i]):
            # print "j",j
            ss = redusing(ss, R, sln, rklst, i, j, s)
            # print "ss",ss
            # print ss
    gs = gauss(ss[i], p)
    # print "gs",gs
    for k in range(0, int(len(gs))):
        sln.append(gs[k])
        # print(sln)
print("Коэффициенты искомого многочлена F(X_1,...,X_2) (имя списка sln):")
print("Коэффициенты перечислены в порядке возрастания степеней мономов в однородных многочленах симметричного многочлена.")
print(sln)
print ("Коэффициенты исходного многочлена F(X_1,...,X_k) восстановлены верно")
print (sv==sln)
slist1 = slaulist(E, r, rklst)
print(slist1)
print(slist1[1:2])
print(type(slist1[1:2][0]))
print(slist1[1:2][0])
print(sv[1])
print(type(sv[1]))
for i in range(len(slist1[1:2][0])):
    # for j in range(len(slist1[1:2][0][0])):
    p = int(slist1[1:2][0][i][0] - sv[1])
    if p < 0:
        slist1[1:2][0][i][0] = p + 127
        del slist1[1:2][0][i][1]
    else:
        slist1[1:2][0][i][0] = p
        del slist1[1:2][0][i][1]
print(slist1[1:2][0])
print(type(slist1[1:2][0]))
