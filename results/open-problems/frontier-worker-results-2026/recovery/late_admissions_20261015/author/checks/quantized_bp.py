"""Exact upgraded BP on a symmetric simplex grid, with rigorous mass rounding.

Each approximation increases the Blackwell information order. Thus the reported
finite-depth second moment is an upper bound for fully observed Potts leaves.
No claim about infinite-depth nonreconstruction follows without a local entry lemma.
"""
import argparse
from fractions import Fraction as F
from itertools import permutations,product
import json,pathlib,time,math

def simplex_split(p,N):
    scaled=[v*N for v in p];floors=[v.numerator//v.denominator for v in scaled]
    remainder=[v-f for v,f in zip(scaled,floors)];m=N-sum(floors)
    assert m in [0,1,2] and sum(remainder)==m
    if m==0:return [(tuple(floors),F(1))]
    ans=[]
    for i in range(3):
        v=floors.copy()
        if m==1:v[i]+=1;weight=remainder[i]
        else:
            for k in range(3):v[k]+=int(k!=i)
            weight=1-remainder[i]
        if weight:ans.append((tuple(v),weight))
    assert sum(w for v,w in ans)==1
    assert all(sum(w*F(v[i],N) for v,w in ans)==p[i] for i in range(3))
    assert all(min(v)>=0 and sum(v)==N and w>=0 for v,w in ans)
    return ans

def orbits(N):
    keys=[]
    for a in range(N+1):
        for b in range(a,N+1):
            c=N-a-b
            if c>=b:keys.append((a,b,c))
    return keys,[sorted(set(permutations(p))) for p in keys]

def transition_table(N,lam,cache=None):
    keys,vertices=orbits(N);lookup={v:k for k,v in enumerate(keys)}
    if cache is not None and cache.exists():
        raw=json.loads(cache.read_text(encoding='utf-8'))
        assert raw['grid']==N and raw['lambda']==str(lam) and raw['keys']==[list(k) for k in keys]
        table=[(i,j,{int(k):F(v) for k,v in dest.items()}) for i,j,dest in raw['table']]
        assert len(table)==len(keys)*(len(keys)+1)//2
        assert all(sum(dest.values())==1 and min(dest.values())>=0 for i,j,dest in table)
        return keys,table
    table=[]
    started=time.monotonic()
    for i in range(len(keys)):
        for j in range(i,len(keys)):
            dest={}
            for p,r in product(vertices[i],vertices[j]):
                z=[(1-lam+3*lam*F(p[a],N))*(1-lam+3*lam*F(r[a],N)) for a in range(3)]
                den=sum(z);assert den>0
                posterior=[v/den for v in z]
                mass=den/F(3*len(vertices[i])*len(vertices[j]))
                for v,w in simplex_split(posterior,N):
                    k=lookup[tuple(sorted(v))];dest[k]=dest.get(k,F(0))+mass*w
            assert sum(dest.values())==1
            table.append((i,j,dest))
        if i%25==0:print('table grid',N,'orbit row',i,'of',len(keys),'seconds',round(time.monotonic()-started,1),flush=True)
    if cache is not None:
        raw={'grid':N,'lambda':str(lam),'keys':keys,'table':[(i,j,{str(k):str(v) for k,v in dest.items()}) for i,j,dest in table]}
        cache.write_text(json.dumps(raw,separators=(',',':')),encoding='utf-8')
    return keys,table

def round_up_mass(masses,vertex_index,bits):
    scale=1<<bits
    rounded=[F((m*scale).numerator//(m*scale).denominator,scale) for m in masses]
    missing=1-sum(rounded);assert missing>=0
    rounded[vertex_index]+=missing
    assert sum(rounded)==1 and min(rounded)>=0
    return rounded,missing

def run(N,lam,steps,bits,checkpoint,resume=False,cache=None):
    assert N%3==0 and 0<lam<1
    keys,table=transition_table(N,lam,cache)
    vertex=keys.index((0,0,N));masses=[F(0)]*len(keys);masses[vertex]=F(1)
    chis=[sum(F(v,N)**2 for v in key)-F(1,3) for key in keys]
    rows=[];first_depth=1;started=time.monotonic()
    if resume and checkpoint.exists():
        old=json.loads(checkpoint.read_text(encoding='utf-8'))
        assert old['grid_denominator']==N and old['lambda']==str(lam) and old['mass_rounding_bits']==bits
        rows=old['rows'];first_depth=rows[-1]['depth']+1
        masses=[F(old['final_orbit_masses'][str(key)]) for key in keys]
        assert sum(masses)==1
    for depth in range(first_depth,steps+1):
        new=[F(0)]*len(keys)
        for i,j,dest in table:
            factor=masses[i]*masses[j]*(1 if i==j else 2)
            if not factor:continue
            for k,coefficient in dest.items():new[k]+=factor*coefficient
        assert sum(new)==1
        masses,added=round_up_mass(new,vertex,bits)
        upper=sum(m*c for m,c in zip(masses,chis))
        row={'depth':depth,'second_moment_upper':str(upper),'rounding_mass_revealed':str(added)}
        rows.append(row)
        stop_chunk=time.monotonic()-started>90
        if depth%10==0 or depth==steps or stop_chunk:
            data={'status':'rigorous finite-depth upper bounds only; no infinite-depth threshold claim',
                  'q':3,'d':2,'lambda':str(lam),'grid_denominator':N,'orbits':len(keys),
                  'mass_rounding_bits':bits,'rounding':'Exact fractions then discard each orbit mass downward and replace the missing mass by fully observed root color; this increases information.',
                  'rows':rows,'final_orbit_masses':{str(key):str(m) for key,m in zip(keys,masses)},
                  'wall_seconds':time.monotonic()-started}
            checkpoint.write_text(json.dumps(data,indent=2),encoding='utf-8')
            print('grid',N,'depth',depth,'upper',str(upper),'rounded',str(added),flush=True)
        if stop_chunk:
            print('Chunk time limit: checkpoint saved, completed depth',depth,flush=True)
            break
    return rows

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--grid',type=int,default=6)
    parser.add_argument('--lambda',dest='lam',default='707107/1000000')
    parser.add_argument('--steps',type=int,default=100);parser.add_argument('--bits',type=int,default=40)
    parser.add_argument('--resume',action='store_true');parser.add_argument('--fresh',action='store_true')
    args=parser.parse_args();root=pathlib.Path(__file__).resolve().parent
    path=root/f'quantized_bp_N{args.grid}_{args.lam.replace("/","-")}.json'
    cache=None if args.fresh else root/f'quantized_bp_table_N{args.grid}_{args.lam.replace("/","-")}.json'
    run(args.grid,F(args.lam),args.steps,args.bits,path,args.resume,cache)
