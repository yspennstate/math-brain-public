from check import *

def remainder_nats(q):
    lo,hi=ln_interval(1-q)
    return -2*(1-q)**2*hi-2*q+3*q*q,-2*(1-q)**2*lo-2*q+3*q*q

def main():
    rows=[]
    for flip in (False,True):
        for state in product((-1,0,1),repeat=4):
            free=[j for j in range(4) if state[j]==-1];table=[]
            for x in range(1<<len(free)):
                full=sum(((x>>free.index(j)&1) if j in free else state[j])<<j for j in range(4))
                v=bent(full);table.append(-v if flip and full==0 else v)
            w=walsh(table);N=len(table)
            for j in range(len(free)):
                vec=defaultdict(int);dsum=0
                for T in range(N):
                    if not(T>>j&1):
                        A=w[T]**2;D=w[T|(1<<j)]**2;dsum+=D
                        logadd(vec,A+D,A+D);logadd(vec,A,-A);logadd(vec,D,-D)
                vec[2]-=4*dsum
                vec=tuple(sorted((p,v) for p,v in vec.items() if v))
                lo,hi,terms=interval_vec(vec)
                assert hi<=0
                rows.append({'flipped':flip,'restriction':state,'coordinate':free[j],'Walsh_N':N,'influence':str(F(dsum,N*N)),'prime_log_vector_B_minus_4d_natural_numerator':vec,'certified_interval':[str(lo),str(hi)],'atanh_terms':terms})
    assert len(rows)==216
    (ROOT/'out'/'seed_split_certificates.json').write_text(json.dumps(rows,indent=2)+'\n')
    increments=[]
    for s in range(2,13):
        u=F(1,1<<s);lo,hi=remainder_nats(u);lo2,hi2=remainder_nats(2*u)
        glo=lo-hi2/2;ghi=hi-lo2/2
        assert ghi<0 and glo>=-8*u**3/(3*(1-2*u))
        increments.append({'s':s,'G_natural_interval':[str(glo),str(ghi)],'analytic_lower':str(-8*u**3/(3*(1-2*u)))})
    (ROOT/'out'/'decrement_sign_certificates.json').write_text(json.dumps(increments,indent=2)+'\n')
    print(json.dumps({'seed_split_certificates':len(rows),'negative_decrement_sign_certificates':len(increments),'elapsed_seconds':time.perf_counter()-START,'status':'PASS'},indent=2))
if __name__=='__main__':main()
