#!/usr/bin/env python3
"""Outward-rounded certificate for the negative-negative two-equal KS kernel.

At lambda=1/sqrt(2), let H(a,b)=(Psi(p(a))+Psi(p(b)))/2-K_*(p(a),p(b)).
Assuming the separately certified diagonal theorem H(a,a)>=0, this certifies
Q(a,b)=H(a,b)-[H(a,a)+H(b,b)]/2 >=0 for a,b in [-1/2,0].

Exact reduction (derived in the accompanying report):
Q(a,b)=(x-y)^2 R(x,y), x=-a,y=-b,
R=R_P(x,y)-1/2 sum_{n>=2} c_n S_n(x,y)^2,
c_n=[(-1)^n+2^(1-n)]/[3n(n-1)],
S_n=sum_{k=0}^{n-1} x^(n-1-k)y^k.
The exact Q(sqrt(2)) numerator coefficients of R_P and of its radial
quotient are stored below as compressed integer/rational tables.
"""
import base64,zlib,json,time
import mpmath as mp
iv=mp.iv

XY_PAYLOAD='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'
LINE_PAYLOAD='eNp1mFuSJSsIRSdUFQGIiGOp6PlP45qaPjD3/erqFchLU7bn7+8v6Q/7vx9u//zQD//7aUg6+lWJrDRmF7Pbjrtd+9/PL8tmdjMCMaivZbXI2tpiNbIM7PTyJ3XlkmyjNxWm5BtmBPVa7KNV+ejVw1qMRBZZC8LEOcIWRKrWCBVZJuBS7tDlW15Z5ZXqm73VVTqWKmAJrJUrhPUm+JmIjbORz8PxwOdwsAtHmh+aU4p0bN7T/ZMmaCvQL6MU6Eo1H8czyYbzfCZj2/Tt2686+aZv535LtYMmSAV6YBiNPomNb/OX7WyLjm47S4RPtyWHavXtNmVPET/trq4caW+3iFHEAo0ZeyaURgUJfytLe3OKbDb3Rlh907k3UspBdffbNk3Lw+lXIGXogVC0ihLzu4L3NuVQ/rhOM2lkrVRxiuzZQRHxSLV3/7wWH/psYK43bYWK5MgYWhLyWlEC/s0UFGSfwvd8YNXN3j1O6ofhvJRVfMN3h13zsTzN61vqsf7dYK/pMGUECa2vIJKDlArI3e4ax2yr5bzU6d3wJBE+w4371XDSZ1BoOQf1Q1vlmkhqpK3y3C7Iy2/7w2ocQNRr/9pW5NZRBgUli8rKV/m8x3O1jdZJ0MPuPQmZy2E5J5hn2XCehFrnDj30PQlazA/b9yhkp3JQQrQiB45iFZCVgfQzqFOvdrziQo7vjIe4kBYzwubPxT3C5rBW0whbiySrXutbi5SkXKHaH4XsdksPzRI9VGTqyGtBCRhIFdWkoPh0N2nrIFubuHVQlnRAXWN3Dm7eUug3uW4oSyWeDt5j1ErKB51XSmXaHiqCjtYXFMpAUhmlr6DQdDdkKDTmfDZzCLR23WuEfd7E7/fVZ6m4XsYypNg5MvhVaJ5TvZyMoTNyPXjtYkQ9R3PH1gX6NphIhlnDChPohXyatqWi8Hzh8KEUeW/3oRSFyA485Yi10nzjqUeqsB/WSyxKMdrmU5Kw1bIum7xEyYULdmIwZIb5KSwmocLl06KhT8spAvkVp5xv+pw1sSQXfs6acTmFB091ymJ6mffDphL3bwjUtvn18v4ctqbuSrKAC7Y27DvjVBQmjqsU2JG7dVv/jvM54dwN7yd50nnekli2jed5y1ZOH/O8tbFo28k8bq6nse+HjPJ2XTA26CPDeAqTS7ASgVV/+jO0dD71Dw8lHYaRvM9O9XDFvEqazZQibg2TftcesD7P+uLR76OkieLqfsC85LjcgGVGLhXETjDN/6npUzzdLdqiu6y5syX38Y1vyf3bR/mE74FKRLrpnI+Npe1g6qyUaO3vkt1t7u27awvvSDP0oDBaQokJKgHUSndP6L2hQt+HFq817O+Q4srhWcVdirf7uYTBNLS4t2kVbR8xXi0ob+5qvF38wtFDhrYK/SaYg6B0UWF0d2CL7yVltvJ+7gefsE7VsubW1t2qXGXC/aqstqK8p6GWnNbqDJiixQmFEZAPg7zpKu9VzXqqWR/PrPBjSZfMzMUlwGdjvcj58XfJzM6qAfZfRtMVR5FlQj4FRWeQ5qeapW69a/GB3q1KJc12LWmb3ebFvJRtu/FssSmpfD2vlrANLIG1AmIwyIXulLvA5Ern7dnVZSv/vCW7tvTsZwe6smxfBAe7lnIJv3N1VfkxE+COQVj6pJf3Veiz2iXiNK2DuiRcbp/3WjtHqq3fKrZ8O5mAtQxi0CeXLow4BfnSVRGX8x03FFH2FO2euVWHYNhQkCV/PdIn8FIWTEtCbF3R9G5acHWhsqzVgiCj5fSJI+ONYWHcjsmsNajGMZjNKVoysqSvzzXEmpRcH8AeYnlfVGuKRUjf5TS0Asl5ifR/mvZXD5Auy3//AUJ72Ew='
XY_TERMS=json.loads(zlib.decompress(base64.b64decode(XY_PAYLOAD)))
LINE_TERMS=json.loads(zlib.decompress(base64.b64decode(LINE_PAYLOAD)))
SQ2=iv.sqrt(2)

def qiv(p,q): return iv.mpf(p)/q

def make_terms(rows):
    out=[]
    for mon,rp,rq,sp_,sq_ in rows:
        out.append((tuple(mon),qiv(rp,rq)+qiv(sp_,sq_)*SQ2))
    return out
XY=make_terms(XY_TERMS); LINE=make_terms(LINE_TERMS)

def eval_poly(terms,A,B):
    out=iv.mpf(0)
    for (i,j),c in terms:
        out += c*(A**i)*(B**j)
    return out

def rp_xy(xl,xu,yl,yu):
    X=iv.mpf([xl,xu]);Y=iv.mpf([yl,yu])
    num=eval_poly(XY,X,Y)
    den=144*(X**2-2)**3*(X**2+1)**3*(Y**2-2)**3*(Y**2+1)**3*(X*Y-2)**3*(X*Y+1)**3
    return num/den

def rp_line(sl,su,tl,tu):
    S=iv.mpf([sl,su]);T=iv.mpf([tl,tu])
    num=eval_poly(LINE,S,T)
    den=144*(S**2-2)**3*(S**2+1)**3*(S**2*T-2)**3*(S**2*T+1)**3*(S**2*T**2-2)**3*(S**2*T**2+1)**3
    return num/den

def c_n(n):
    sign=-1 if n%2 else 1
    return qiv(sign*(2**(n-1))+1,(2**(n-1))*3*n*(n-1))

def Sn(n,X,Y):
    out=iv.mpf(0)
    for k in range(n): out += X**(n-1-k)*Y**k
    return out

def R_box(xl,xu,yl,yu,N=12):
    X=iv.mpf([xl,xu]);Y=iv.mpf([yl,yu])
    out=rp_xy(xl,xu,yl,yu)
    for n in range(2,N+1):
        z=Sn(n,X,Y)
        out += -iv.mpf(1)/2*c_n(n)*z**2
    # |c_n|<=1/[2n(n-1)], S_n<=n 2^(-(n-1));
    # tail_{n>N} <= (2/3)4^(-N).
    tail=mp.mpf(2)/3*(mp.mpf(4)**(-N))
    return out+iv.mpf([-tail,tail])

def R_local(sl,su,tl,tu,N=8):
    # By symmetry x=s>=y=ts on the local square.
    S=iv.mpf([sl,su]);T=iv.mpf([tl,tu])
    out=rp_line(sl,su,tl,tu)
    for n in range(2,N+1):
        A=iv.mpf(0)
        for k in range(n): A += T**k
        out += -iv.mpf(1)/2*c_n(n)*S**(2*n-4)*A**2
    # divided tail <= 1/2 s^(2N-2)/(1-s^2)
    d=mp.mpf(str(su))
    tail=mp.mpf('0.5')*d**(2*N-2)/(1-d*d)
    return out+iv.mpf([-tail,tail])

def lb(z): return float(z.a)

local_min=1e100
for j in range(100):
    z=R_local(0,.01,j/100,(j+1)/100)
    local_min=min(local_min,lb(z))
    assert lb(z)>0,('LOCAL_FAIL',j,z)

def certify_outer():
    local=.01;init=10;N=12
    stack=[];h=.5/init
    for i in range(init):
        for j in range(init):
            box=(i*h,(i+1)*h,j*h,(j+1)*h,0)
            if box[1]<=local and box[3]<=local: continue
            stack.append(box)
    nodes=accepted=maxdepth=0;min_lower=1e100
    while stack:
        xl,xu,yl,yu,d=stack.pop();nodes+=1;maxdepth=max(maxdepth,d)
        assert nodes<=20000,('NODE_LIMIT',nodes)
        if xl<local<xu:
            stack.append((local,xu,yl,yu,d+1));stack.append((xl,local,yl,yu,d+1));continue
        if yl<local<yu:
            stack.append((xl,xu,local,yu,d+1));stack.append((xl,xu,yl,local,d+1));continue
        if xu<=local and yu<=local: continue
        z=R_box(xl,xu,yl,yu,N)
        if lb(z)>0:
            accepted+=1;min_lower=min(min_lower,lb(z));continue
        assert d<15,('OUTER_FAIL',(xl,xu,yl,yu,d),z)
        if xu-xl>=yu-yl:
            m=(xl+xu)/2
            stack.append((m,xu,yl,yu,d+1));stack.append((xl,m,yl,yu,d+1))
        else:
            m=(yl+yu)/2
            stack.append((xl,xu,m,yu,d+1));stack.append((xl,xu,yl,m,d+1))
    return nodes,accepted,maxdepth,min_lower

t0=time.time()
nodes,accepted,maxdepth,outer_min=certify_outer()
print("LOCAL_PASS")
print("local_min_lower",repr(local_min))
print("OUTER_PASS")
print("nodes",nodes)
print("accepted",accepted)
print("maxdepth",maxdepth)
print("outer_min_lower",repr(outer_min))
print("elapsed_seconds",repr(time.time()-t0))
print("OVERALL_PASS")
