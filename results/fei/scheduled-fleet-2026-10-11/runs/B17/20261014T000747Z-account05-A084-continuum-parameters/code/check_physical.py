"""Independent actual-core and physical-composition checks; no external code."""
from pilot import TABLE,WH,walsh,ROOT,NEG
from certify_continuum import R,add,mul,sub,log2
from collections import Counter
import json,time
def phi(x,y):
    if not x or not y:return R(0),R(0)
    return sub(sub(mul((x+y,x+y),log2(x+y)),mul((x,x),log2(x))),mul((y,y),log2(y)))
def packets(p):
    m=1-2*p;v=1-m*m;result=[]
    for T in range(0,64,2):
        k=T.bit_count();C=d=R(0)
        for W in range(64):
            if W&T==T:C+=R(WH[W],64)*m**(W.bit_count()-k)
            if W&(T|1)==T|1:d+=R(WH[W],64)*m**(W.bit_count()-k-1)
        result.append(((v**k)*C*C,(v**k)*d*d))
    # Separate conditional-section expectation with unnormalized sign basis.
    for k,T in enumerate(range(0,64,2)):
        a=b=R(0)
        for z in range(32):
            h0,h1=TABLE[2*z],TABLE[2*z+1]
            A=R(h0+h1,2);D=R(h0-h1,2)
            weight=p**z.bit_count()*(1-p)**(5-z.bit_count());basis=R(1)
            for bit in range(1,6):
                if T>>bit&1:basis*=1-2*((z>>(bit-1))&1)-m
            a+=weight*basis*(A+m*D);b+=weight*basis*D
        assert (a*a/v**T.bit_count(),b*b/v**T.bit_count())==result[k]
    return result
def reserve(p,t,ps):
    q=sum(d for u,d in ps);m=1-2*p;out=(R(0),R(0))
    for u,d in ps:out=add(out,phi(u,t*d))
    return sub(out,mul((q,q),phi(m*m,t)))
def B_pair(wh,i):
    N=len(wh);mask=1<<i;counts=Counter()
    for T in range(N):
        if not T&mask:counts[wh[T]**2,wh[T|mask]**2]+=1
    result=(R(0),R(0))
    for (a,b),count in counts.items():
        result=add(result,mul((R(count,N*N),R(count,N*N)),phi(R(a),R(b))))
    return result
def influence(table,i):
    mask=1<<i
    return R(sum(table[x]!=table[x|mask] for x in range(len(table)) if not x&mask),len(table)//2)
def inverse_check(table,wh):
    assert sum(x*x for x in wh)==len(table)**2
    assert walsh(wh)==[len(table)*x for x in table]
def main():
    start=time.perf_counter();checks=0;cases=[]
    for n,M in [(4,1),(3,1),(5,7),(2,1),(1,1)]:
        table=[-1 if x<M else 1 for x in range(1<<n)];p=R(M,1<<n)
        chosen_p=p if p<=R(7,32) else 1-p;chosen=table if chosen_p==p else [-x for x in table]
        wh=walsh(chosen);inverse_check(chosen,wh);checks+=2
        ps=packets(chosen_p);q=sum(d for u,d in ps);checks+=32
        assert q==2*chosen_p*(1-chosen_p)**3*(2-chosen_p);checks+=1
        rows=[]
        for i in range(n):
            inf=influence(chosen,i);specinf=sum(R(a*a,len(table)**2) for T,a in enumerate(wh) if T>>i&1)
            assert inf==specinf;checks+=1
            t=R(wh[1<<i],len(table))**2;iv=reserve(chosen_p,t,ps)
            assert iv==(0,0) if not t else iv[0]>0;checks+=1
            rows.append({'coordinate':i,'core_influence':str(inf),'t':str(t),'reserve_interval':[str(x) for x in iv]})
        item={'n':n,'minority_count':M,'minority_p':str(p),'chosen_p':str(chosen_p),'q':str(q),'coordinate_checks':rows}
        if n<=3:
            totalbits=6*n;N=1<<totalbits;mask=(1<<n)-1
            actual=[]
            for x in range(N):
                y=0
                for j in range(6):
                    if chosen[(x>>(n*j))&mask]<0:y|=1<<j
                actual.append(-1 if y in NEG else 1)
            aw=walsh(actual);inverse_check(actual,aw);checks+=2
            acinf=influence(actual,0);assert acinf==q*influence(chosen,0);checks+=1
            acB=B_pair(aw,0);cb=B_pair(wh,0);t=R(wh[1],1<<n)**2
            predicted=add(mul((q,q),cb),reserve(chosen_p,t,ps))
            assert max(acB[0],predicted[0])<=min(acB[1],predicted[1]);checks+=1
            item['direct_physical_table']={'bits':totalbits,'entries':N,'checked_coordinate':0,'actual_B_interval':[str(x) for x in acB],'predicted_B_interval':[str(x) for x in predicted],'all_other_coordinates':'equal by point-core permutations and matching-gate transitivity','influence':str(acinf)}
            del actual,aw
        cases.append(item)
        (ROOT/'out'/f'PHYSICAL_FIXTURE_{n}_{M}.json').write_text(json.dumps(item,indent=2),encoding='utf-8')
        if time.perf_counter()-start>110:raise RuntimeError('Frozen runtime cap')
    result={'fixtures':len(cases),'actual_direct_table_dimensions':[18,12,6],'independent_section_packet_checks':160,'checks_passed':checks,'runtime_seconds':time.perf_counter()-start,'memory_estimate_mb':120,'independent_acceptance':False,'scope':'same-author independent algebra representations and actual physical truth tables; reviewer acceptance remains pending'}
    (ROOT/'out'/'PHYSICAL_RESULT.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
