from check import *
from arithmetic import LN2,ceildiv
def main():
    start=time.perf_counter();rows=[];nchecks=0
    loge=(Q*Q//LN2[1],ceildiv(Q*Q,LN2[0]))
    assert loge[1]*2<3*Q;nchecks+=1
    for r in range(4,9):
        p=F(1,1<<r);v=4*p*(1-p);q=2*p*(1-p)**3*(2-p);QQ=6*q
        masses=spectrum(p);tau=12*p*p-28*p**3+27*p**4-12*p**5+2*p**6
        assert tau<=12*p*p and q>=3*p and q<=4*p;nchecks+=3
        assert QQ*v>=96*p*p-432*p**3;nchecks+=1
        for T,mass in enumerate(masses):assert mass<=v**T.bit_count();nchecks+=1
        assert sum(masses)==1;nchecks+=1
        for j in range(6):assert sum(z for T,z in enumerate(masses) if T>>j&1)==v*q;nchecks+=1
        C=plus(entropy(masses),signed(entropy([v,1-v]),-QQ))
        lower=signed(loge,-QQ*v)
        assert C[0]>=lower[1] and C[1]<=342*p*p*Q;nchecks+=2
        rows.append({'p':str(p),'v':str(v),'Q':str(QQ),'tau':str(tau),'C_interval':C,'lower_envelope_interval':lower,'upper_envelope':str(342*p*p)})
        (ROOT/'out/RARE_CASES.json').write_text(json.dumps(rows,indent=2)+'\n')
    assert F(19)*F(4,15)/(1-F(2,3))==F(76,5);nchecks+=1
    assert F(6)*F(4,15)/(1-F(2,3))==F(24,5);nchecks+=1
    assert F(172,3)+F(76,5)==F(1088,15)<73;nchecks+=1
    assert -F(50,3)-F(24,5)==-F(322,15);nchecks+=1
    out={'version':'rare-terminal-payment-v1','assertions_passed':nchecks,'failed':0,'runtime_seconds':time.perf_counter()-start,'rare_bill_bounds':['-24/5','76/5'],'complete_policy_bill_bounds':['-322/15','1088/15']}
    assert out['runtime_seconds']<55
    (ROOT/'out/RARE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
