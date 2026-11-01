from check import *
def main():
    start=time.perf_counter();checks=0;point=[]
    d=F(1,32);core=plus((int((2-2*d)*Q),)*2,phi_ratio(F(31,32)**2,d*d,d))
    assert core[0]*4>9*Q;checks+=1
    for p in [F(1,64),F(63,64)]:
        q=2*p*(1-p)**3*(2-p);r=reserve(p,d*d)
        new=plus(core,signed(r,1/(q*d)))
        assert r[1]<0 and new[1]*4<9*Q;checks+=2
        point.append({'p':str(p),'core_E_interval':core,'reserve_interval':r,'composed_E_interval':new})
    # Negative total1024, split513/511: exact bias1/4, beta=-1/1024.
    g=[-1 if x//2<(513 if x%2==0 else 511) else 1 for x in range(4096)]
    co=fwht(g);edges=sum(g[x]!=g[x^1] for x in range(4096))
    assert co[0]==F(1,2) and co[1]==-F(1,1024)
    assert F(edges,4096)==F(1,1024) and sum(a*a for a in co)==1;checks+=4
    iv=reserve(F(1,4),co[1]**2);assert iv[1]<0;checks+=1
    # Independent derivatives: signed-log slope is checked from the finite t formula.
    records=json.loads((ROOT/'out'/'BIAS_CERTIFICATES.json').read_text())
    for rec in records:
        p=F(rec['p']);rows=packets(p);q=sum(D for _,U,D in rows)
        s=rec['criterion']
        for t in [F(1,1024)**2,F(1,16)]:
            r=reserve(p,t,rows)
            if s['status'] in ['SAFE','BALANCED_SAFE']:assert r[0]>=0;checks+=1
    out={'point_obstruction':point,'physical12':{'negative_half_counts':[513,511],'mean':str(co[0]),'beta':str(co[1]),'influence':str(F(edges,4096)),'reserve_interval':iv},'assertions_passed':checks,'runtime_seconds':time.perf_counter()-start,'failed':0}
    assert out['runtime_seconds']<55
    (ROOT/'out'/'FIXTURES.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
