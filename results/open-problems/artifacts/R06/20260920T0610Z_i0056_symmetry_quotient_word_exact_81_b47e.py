from fractions import Fraction
import base64,lzma,hashlib

CERT_B64="""/Td6WFoAAATm1rRGAgAhARwAAAAQz1jM55m7BYRdAABn/4ADhmG8iIK0+CdXSOcoAX6ViB4ZgJ2DbvOd2ZF7sUxlQBmEsZiXzne9PneOAeI1AdfW712wDkgfV/xTuuN2TxQiH7H9K+xjQFUwf8ssibl3PRhxcMTVkDszXco76BdcA0dQcW78/VtuXLEcG3EXf7nkyh6obCtHWXZm5RXTJ3yMoh9viAOgccyqMJyrsBWU7T6RxRxLuo7McpHFqnWqejiDkW8f+tM/tml0xqtxY7Yk47zFAQiQEOpM8/Hpgvsv7lSWoDTtgRax0ZAzXlKaEjLygNO5o2M4A95GAeyx1XLtx06aPPsL5Hbn3nGQaJ9vtfjmo7C3GVNvjro4juJXmidBPa6TstcAP+EiCOKVxxpJ4/xJbhqQScv2if/vPojC3fE4VBkvK4cmSXvQCHGLL8l0zjpOfiuvAoj5t0hmToccqXxqxCQCghF9vGvEVc44bVdy5hb1hwilPj0Ey2Kd9pL5VDQaB3d1CJFJub+HZy6Htb9ztGLy63LC2PKfTXj43LcsLANvXvn/gh0KaIGQnb7ce0Ky33GqOWBPv3de4L1bS1r2BpfRlomVqDTbheTBPek9ElS5eiHOVlZkQR0drrUOtR/Z3KFRS+lYK6bah1j0l80uOb6NhvGTOGfoMId6LetyDq6GGCRlbAAia5IY6qLotk02aeP0UT5dOsVKTmDQomaMHhWXJ8kZmd0xgr744heJNDJshT3W4IqmQh+2onQ8RD+7lqSIv5loyua4H0UksWtr7jrBDpmhuavkWzbtdB5W9Uhwg08kkv/nni03xO0zDkaULfiLvex9yf7FmUoDAWLqQyOslfV5esKqA+AajzFFUENAz+KgersErs7/M5wAl7m0osuq1qr4OY2ZtxxAoZJF4Sd5bjIvYXN29faknJwGNVYVI3lYkcFrxj+AQ1LGEMkx+mJGWcLcvKE5y0QR7kB+M95LshpSEpaLqdI0SeERvWal0x3bCGEn+l96cPghnIY3MVd7/j0g3f4cgZqKMFoEmG8Ofpzfo6uVzyNqXuSDt3MbJTLf/yHBD5IFcPeBm885bo5iOvuj77Lw2QMsVwqoDRIWGb+fB6LMFXqQsr15XAvBSLs+XW8HL0eHxUiFiQTLeJTn0z9+/wRdHMid/C7GqpkbMdOoJDpKCfLQf4l8zFYev6vc0Wj+GVyL7OYFQW+MRGK6rghWmZUQd9VhmEsziSH5KddKMeyZvI9Q31J+sOWK/eDunekk733O4uS7GYyF4b2NyCE7eskTxoOPaw/r7oZG4WjoQnkK0kS//VpNsbhoKJubSW0W08KMwsUJeZxk+Fnq/uxWLH3X8u7Fx4wwauMRV56kyPuSM1aOr1+TRIkFgocrDcK2iytlI2eBR9fNYkqETmicBACV4Mknr/dnWnxi84s1yV8b8+VPP4JCd6LkYCE5wZDQpkLgRTdbAwNfIUcUq/kFZgpxkML7IFUdU2bk/P9XN49ZMVVbVU/RmOfnABHXHO7rNyXTQtxBu1uuj4DM6B3LXUwGVSZH9g6zbUV82z81S9N4MElomwxw+pZd3WHDrVOYck93Ubvo503Zd/humy7u1hWLu+G0iZ0lZjjaalhHxNbKAn5V/9vBLCuVK8n/POLHMY4ykzCQbo7QrU7hlKzyRqenHkM9uZ4yWuYpT5bczTYHdOlS3DZOhOZGYwfrj1pVmlnBmj3DsCGnkIgm4pz3SDG5Fi11DnHi+QhKDcpI2GYxa2fR0StGGFpG5kQa2ZwpLF3TGtb+NL4bA8FrMJ9YdJtZGoDp3+ZLXQEwJXyRD+Bz5tq+brDFbooM5p+T+a3friLtj/QopOWzMZI8+GGuMq6zY8AeEIY33P5DYCTwH3SYzkVqAb+jCnS6Yx7Re/XaPzLwVybAAJjxPHVqH/xEAAGgC7yzHgCWemTpscRn+wIAAAAABFla"""
CERT_SHA="352c7fdcb60542e932ea0e976db8432e9f05b5d37356d2ceb22018cee14d0063"

def add(x,y): return (x[0]+y[0],x[1]+y[1],x[2]+y[2],x[3]+y[3])
def neg(x): return (-x[0],-x[1],-x[2],-x[3])
def mul(x,y):
    x0,x1,x2,x3=x; y0,y1,y2,y3=y
    return (
        x0*y0 + 2*x1*y1 + x2*y2 + 2*x3*y3,
        x0*y1 + x1*y0 + x2*y3 + x3*y2,
        x0*y2 + x2*y0 + x2*y2 + 2*x1*y3 + 2*x3*y1 + 2*x3*y3,
        x0*y3 + x3*y0 + x1*y2 + x2*y1 + x2*y3 + x3*y2,
    )
Z=(0,0,0,0); ONE=(1,0,0,0); A=(0,1,0,0); B=(0,0,1,0); MONE=(-1,0,0,0)
def sring(items):
    z=Z
    for x in items: z=add(z,x)
    return z
def mm(X,Y):
    return tuple(tuple(sring(mul(X[i][k],Y[k][j]) for k in range(3)) for j in range(3)) for i in range(3))
def mv(X,v):
    return tuple(sring(mul(X[i][k],v[k]) for k in range(3)) for i in range(3))
I=tuple(tuple(ONE if i==j else Z for j in range(3)) for i in range(3))
def mpow(X,n):
    Y=I
    for _ in range(n): Y=mm(X,Y)
    return Y
S1=((MONE,A,Z),(Z,ONE,Z),(Z,Z,ONE))
S2=((ONE,Z,Z),(A,MONE,B),(Z,Z,ONE))
S3=((ONE,Z,Z),(Z,ONE,Z),(Z,B,MONE))
assert mm(S1,S1)==I and mm(S2,S2)==I and mm(S3,S3)==I
assert mpow(mm(S1,S2),4)==I and mpow(mm(S2,S3),5)==I and mpow(mm(S1,S3),2)==I
R=mm(S2,S3); Ri=mpow(R,4)
Q=mm(mm(S1,R),S1); Qi=mpow(Q,4)
assert mpow(R,5)==I and mpow(Q,5)==I and mpow(mm(R,Qi),2)==I
MID=(A,(2,0,0,0),B)
assert mv(S1,MID)==MID and mv(S3,MID)==MID
GENS=(R,Ri,Q,Qi)
assert len({mv(g,MID) for g in GENS})==4

def s1f(v):
    x,y,z=v
    return (add(neg(x),mul(A,y)),y,z)
def s3f(v):
    x,y,z=v
    return (x,y,add(mul(B,y),neg(z)))
def orbit(v): return {v,s1f(v),s3f(v),s1f(s3f(v))}
def repH(v): return min(orbit(v))

front=lzma.decompress(base64.b64decode(CERT_B64.encode()))
assert hashlib.sha256(front).hexdigest()==CERT_SHA
words=[]; pos=0; prev=b""
while pos<len(front):
    common=front[pos]; slen=front[pos+1]; pos+=2
    assert common<=len(prev)
    w=prev[:common]+front[pos:pos+slen]; pos+=slen
    words.append(w); prev=w
assert pos==len(front)
assert len(words)==121103
assert max(map(len,words))<=20

selected_reps=[]
for w in words:
    v=MID
    for j in w:
        assert j<4
        v=mv(GENS[j],v)
    assert repH(v)==v
    selected_reps.append(v)
assert len(set(selected_reps))==len(selected_reps)

K=set()
for v in selected_reps: K.update(orbit(v))
assert len(K)==484385
N=set(K)
for v in K:
    for g in GENS: N.add(mv(g,v))
outer=len(N)-len(K)
assert len(N)==868951
assert outer==384566
ratio=Fraction(outer,len(K))
assert ratio==Fraction(384566,484385)
old=Fraction(116990,147339)
assert ratio<old
cross=116990*484385-384566*147339
assert cross==6631276

print("WORD_CERTIFICATE_COUNT",len(words))
print("FRONTCODE_CERT_SHA256",CERT_SHA)
print("FULL_SELECTED_SIZE",len(K))
print("FULL_CLOSED_NEIGHBORHOOD_SIZE",len(N))
print("OUTER_VERTEX_BOUNDARY",outer)
print("NEW_UPPER_BOUND",f"{ratio.numerator}/{ratio.denominator}")
print("STRICT_IMPROVEMENT_CROSS_MARGIN",cross)
print("ALL_EXACT_CHECKS_PASS")
