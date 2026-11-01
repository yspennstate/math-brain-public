from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,time
RUN=Path(__file__).resolve().parents[1]
sp=importlib.util.spec_from_file_location('verify',RUN/'code/verify_tree.py')
v=importlib.util.module_from_spec(sp); sp.loader.exec_module(v)
A=v.A
def main():
    start=time.perf_counter(); N=16; D=1<<(2*N); W=1<<N; den=D*W; value={}; rows=[]; direct=v.Direct(N)
    for m in range(1,17):
        a=F(1,1<<(m-1)); x=int((1-a)**2*D); y=int(a*a*D)
        B=A.add((1,v.phi(x,y)),(1,{2:((1<<(m-1))-1)*2*y}))
        value=A.add((W,B),(1,A.halfsum(value,{})))
        # Exact all-dimensional closed formula; independently reconstruct small truth cases.
        if m<=6:
            tab=tuple(-1 if t==0 else 1 for t in range(1<<m))
            for i in range(m): v.check(direct.debt(tab,i)==B)
            v.check(direct.solve(tab)==value)
        I=m*a
        lo,hi=A.iv(value); lo=F(lo,den*A.Q); hi=F(hi,den*A.Q)
        v.check(lo/I>=2-F(4,m))
        # log2(e)<2: check a weaker rational consequence of the analytic bound.
        v.check(hi/I<=2+F(2,m))
        rows.append({'m':m,'influence':str(I),'B_log_coefficients':v.encode(B),'V_log_coefficients':v.encode(value),'V_over_I':A.decimal(value,int(den*I))})
    elapsed=time.perf_counter()-start; v.check(elapsed<60)
    out={'status':'PASS','AND_domain':[1,16],'small_direct_domain':[1,6],'assertions':v.COUNT,'independent_truth_states':len(direct.memo),'probability_denominator':D,'cost_denominator':den,'rows':rows,'runtime_seconds':elapsed,'all_m_analytic_result':'Every complete tree has the same optimum V_m; 2-4/m <= V_m/(m*2^(1-m)) <= 2+log2(e)/m, hence the ratio tends to 2. The upper analytic bound implies the weaker rational bound checked here.'}
    (RUN/'out/AND_CERTIFICATE.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:out[k] for k in ['status','AND_domain','small_direct_domain','assertions','independent_truth_states','runtime_seconds']}))
if __name__=='__main__':main()
