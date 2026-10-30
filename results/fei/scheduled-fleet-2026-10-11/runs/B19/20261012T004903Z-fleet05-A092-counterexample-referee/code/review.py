"""A092 v1: independent reconstruction of A047 fixed-child endpoint."""
from independent import F, spectrum, audit, outward
from pathlib import Path
import sys,json,time

ROOT=Path(__file__).resolve().parents[1]
SOURCE=Path(r'~\brain_workers\FEI100_20261011\agents\A047\runs\20261011T220210Z-fleet05-A047-boundary-search')
START=time.perf_counter()
sys.set_int_max_str_digits(20000)

def save(name,data): (ROOT/'out'/name).write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
def guard():
    if time.perf_counter()-START>60: raise RuntimeError('60-second frozen cap exceeded')

def walsh_direct(t):
    return [sum(v*(1-2*((s&x).bit_count()%2)) for x,v in enumerate(t)) for s in range(len(t))]

def census(n):
    N=1<<n
    tables=[[1-2*((mask>>x)&1) for x in range(N)] for mask in range(1<<N)]
    W=[walsh_direct(t) for t in tables]
    for t,w in zip(tables,W):
        guard()
        assert sum(a*a for a in w)==N*N
        assert walsh_direct(w)==[N*v for v in t]
        assert spectrum(t,[F(1,2)]*n)==[F(a*a,N*N) for a in w]
        for i in range(n):
            assert sum(w[s]*w[s] for s in range(N) if s>>i&1)==N*sum(t[x]!=t[x^(1<<i)] for x in range(N))
    positive=zero=extremizers=0
    max_coefficient=None;balanced_max=None; gap_zero=0
    for i,g in enumerate(W):
        guard()
        for j,h in enumerate(W):
            dot=sum(a*b for a,b in zip(g,h))
            assert dot==N*sum(a*b for a,b in zip(tables[i],tables[j]))
            z=sum(b*b for a,b in zip(g,h) if a==0)
            d=sum((b-a)**2 for a,b in zip(g,h) if a!=0)
            coefficient=z-d
            assert coefficient==2*z+2*dot-2*N*N
            cauchy_gap=N*N*(N*N-z)-dot*dot
            assert cauchy_gap>=0
            # Verify the sharper full completed-square inequality, not just <=1/2.
            assert 2*N*N*coefficient<=N**4-(2*dot-N*N)**2
            sharp=(2*coefficient==N*N)
            projection=(2*dot==N*N and all(2*b==a for a,b in zip(g,h) if a))
            assert sharp==projection
            if max_coefficient is None or coefficient>max_coefficient:
                max_coefficient=coefficient;extremizers=1
            elif coefficient==max_coefficient:extremizers+=1
            if g[0]==h[0]==0:
                balanced_max=coefficient if balanced_max is None else max(balanced_max,coefficient)
            positive+=coefficient>0;zero+=coefficient==0;gap_zero+=cauchy_gap==0
    return {'n':n,'pairs':len(tables)**2,'positive':positive,'zero':zero,'maximum':str(F(max_coefficient,N*N)),'maximizers':extremizers,'balanced_maximum':str(F(balanced_max,N*N)) if balanced_max is not None else None,'Cauchy_equalities':gap_zero}

def overlap(a,record):
    return max(a[0],F(record['lower']))<=min(a[1],F(record['upper']))

def finite():
    choices={
        'constant_to_quarter_defect':([1]*4,[-1,1,1,1]),
        'constant_to_balanced':([1]*4,[-1,-1,1,1]),
        'dictator_to_balanced_quarter_surgery':([1,-1,1,-1,1,-1,1,-1],[-1,1,1,-1,1,-1,1,-1]),
        'equal_children':([1,-1],[1,-1]),
        'opposite_children':([1,-1],[-1,1])}
    source=json.loads((SOURCE/'out'/'results.json').read_text())
    rows=[]
    for label,(g,h) in choices.items():
        n=(len(g)).bit_length()-1
        for p in [F(1,8),F(1,64),F(1,1024)]:
            guard()
            law,M,J,E,_=audit(g+h,[F(1,2)]*n+[p],[n])
            supplied=next(r for r in source['finite'] if r['label']==label and r['p']==str(p))
            supplied_law=list(map(F,supplied['joint']))
            assert law==supplied_law[::2]+supplied_law[1::2]
            assert overlap(M,supplied['M']) and overlap(J,supplied['J']) and overlap(E,supplied['debt'])
            if label in ['constant_to_quarter_defect','dictator_to_balanced_quarter_surgery']:
                assert E[0]>0;sign='POSITIVE_CERTIFIED'
            elif label=='opposite_children':assert E[1]<0;sign='NEGATIVE_CERTIFIED'
            else:assert E[0]<=0<=E[1];sign='ZERO_PROVED_ANALYTICALLY'
            rows.append({'label':label,'p':str(p),'g':g,'h':h,'parent_law':list(map(str,law)),'M_bits':outward(M),'J_bits':outward(J),'debt_bits':outward(E),'debt_exact_interval':list(map(str,E)),'sign':sign,'source_interval_overlap':True})
            save('FINITE.json',rows)
    unequal=[]
    for row in json.loads((SOURCE/'out'/'unequal.json').read_text()):
        guard();p,q=F(row['p']),F(row['q'])
        law,M,J,E,_=audit([1,1,1,-1],[p,q],[0])
        assert law==list(map(F,row['spectrum']))
        assert overlap(M,row['M']) and overlap(J,row['J']) and overlap(E,row['debt'])
        if p<F(1,2):assert E[0]>0;sign='POSITIVE_CERTIFIED'
        else:assert E[1]<0;sign='NEGATIVE_CERTIFIED'
        unequal.append({'p':str(p),'q':str(q),'truth_table':[1,1,1,-1],'law':list(map(str,law)),'debt_bits':outward(E),'debt_exact_interval':list(map(str,E)),'sign':sign,'source_interval_overlap':True})
        save('UNEQUAL.json',unequal)
    return rows,unequal

def main():
    pilot='--pilot' in sys.argv
    counts=[]
    for n in range(3 if pilot else 4):
        counts.append(census(n))
        save('PILOT_CENSUS.json' if pilot else 'CENSUS.json',counts)
    expected=json.loads((SOURCE/'out'/'results.json').read_text())['exact_counts']
    for row in counts:
        for key in ['pairs','positive','zero','maximum','maximizers','balanced_maximum']:
            assert row[key]==expected[str(row['n'])][key]
    save('PILOT_CENSUS.json' if pilot else 'CENSUS.json',counts)
    rows,unequal=finite()
    result={'status':'PASS','pilot':pilot,'endpoint_pairs':sum(r['pairs'] for r in counts),'finite_cases':len(rows)+len(unequal),'runtime_seconds':time.perf_counter()-START,'arithmetic':'integers and Fraction; independent recursive centered transform and 80-term -ln(1-t) certificate','claims_reviewed':['A047-SHARP-FIXED-CHILD-RARE-SELECTOR@1'],'no_uniform_remainder_inference':True}
    save('PILOT.json' if pilot else 'RESULT.json',result)
    print(json.dumps(result))

if __name__=='__main__':main()
