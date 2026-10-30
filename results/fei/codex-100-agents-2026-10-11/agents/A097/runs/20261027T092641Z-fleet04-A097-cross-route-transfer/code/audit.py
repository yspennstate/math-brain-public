import json, time
from fractions import Fraction as R
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
t0=time.monotonic()
checks=0
def require(b):
    global checks
    checks+=1
    assert b, checks
    if time.monotonic()-t0>55:
        raise RuntimeError('INCOMPLETE: audit 55 second cap')
for n in [4,6]:
    size=2**n
    table=[]
    for x in range(size):
        out=1
        for pair in range(n//2):
            out*=(-1 if (x & (3 << (2*pair)))==0 else 1)
        table.append(out)
    for s in range(size):
        a=sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(table))
        require(a*a==size)
    epsden=2**(4*n)
    mass=[]
    for s in range(size):
        weight=epsden
        if s & (1<<(n-1)):
            weight += (epsden-1)*(-1 if (s & ((1<<(n-1))-1)).bit_count()%2 else 1)
        mass.append(weight)
    require(mass[0]==epsden)
    for U in range(size):
        if U.bit_count()<=n-2:
            direct=sum(mass[s] for s in range(size) if s&U==U)
            require(direct==(2**(n-U.bit_count()))*epsden)
    for bit in range(n-1):
        for s in range(size):
            if not s&(1<<bit):
                require(mass[s]+mass[s|(1<<bit)]==2*epsden)
    require(mass.count(1)==mass.count(2*epsden-1)==size//4)
    # Exact likelihood product of every true atom, independent grouping path.
    product=R(1)
    for w in mass:
        product*=R(w,epsden)
    e=R(1,epsden)
    require(product==(e*(2-e))**(size//4))
    require(1<2-e<2)
for r in [2,3,5]:
    # q is a geometric size tilt; p and u have the same first moment.
    q=[R(r**i,sum(r**j for j in range(4))) for i in range(4)]
    u=[R(1,4)]*4
    p=[R(1,8),R(3,8),R(3,8),R(1,8)]
    require(sum(i*p[i] for i in range(4))==sum(i*u[i] for i in range(4)))
    # Pythagorean cross term vanishes, without logarithm evaluation.
    product=R(1)
    for i in range(4):
        product*=(u[i]/q[i])**int(8*(p[i]-u[i]))
    require(product==1)
    # q is not a partial mixture of p with uniform u: it tests a non-cell tilt.
    require(q[1]**2==q[0]*q[2] and q[2]**2==q[1]*q[3])
result={'status':'PASS','exact_assertions':checks,'Boolean_cases':2,'nonpartition_moment_fixtures':3,'seconds':time.monotonic()-t0,'independence':'separate code/direct characters/rational products; same agent, not independent-agent acceptance'}
(ROOT/'out'/'AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
