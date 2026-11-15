import os
os.environ.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
import json,math,time,resource
from pathlib import Path
import numpy as np,mpmath as mp
from experiments import unpack,signs,KEYS,summarize
from composition import fw
from highprecision import ph
mp.mp.dps=70
def objective(r):
    n=r['n'];L=1<<n;hat=np.rint(fw(unpack(r['tt'],n))*L).astype(np.int64);mu=[int(x)**2 for x in hat];I=sum(s.bit_count()*v for s,v in enumerate(mu));tot=[mp.mpf(0)]*6
    for i in range(n):
        labels=[{}, {}, {}, {}, {}];M=L//2
        for t in range(M):
            bit=1<<i;s=(t&(bit-1))|((t&~(bit-1))<<1);a,b=mu[s],mu[s|bit]
            for k in range(5):
                p,N=r['params'][i][k]
                if k==0:l=(t&p).bit_count()&1
                elif k==1:l=bool(t&N)
                elif k==2:l=((t&p).bit_count()&1,bool(t&N))
                elif k==3:l=t.bit_count()
                else:l=(t&N).bit_count()
                aa,bb=labels[k].get(l,(0,0));labels[k][l]=(aa+a,bb+b)
        vals=[sum(ph(a,b) for a,b in cells.values()) for cells in labels]
        for k,v in enumerate(vals):tot[k]+=v
        tot[5]+=min(vals)
    return dict(zip(['parity','meets','both','size','countN','union'],[v/I for v in tot]))
def main():
    start=time.time();class_errors=0;ltf_count=0;minimum_gap=float('inf');monocount=0;allrows=[]
    for name in ['samples','ltf','monotone_all5','monotone6','families','census_extrema']:
        z=json.loads(Path(name+'.json').read_text());z['maxima']=summarize(z['rows']);z['candidate_maxima']=summarize(z['rows'],False);z['maxima_scope']='Only optimized fields: mode 1 all; mode 3 H,Hm,parity,size; mode 0 H,Hm,size. Other costs are valid candidate upper bounds.';Path(name+'.json').write_text(json.dumps(z,indent=2)+'\n');allrows+=z['rows']
        for r in z['rows']:
            if name=='ltf':
                n=r['n'];X=signs(n);score=np.zeros(1<<n)
                for i,w in enumerate(r['meta']['weights']):score+=X[:,i]*w
                threshold=r['meta']['threshold'];actual=np.where(score>=threshold,1,-1);class_errors+=np.count_nonzero(actual!=unpack(r['tt'],n));minimum_gap=min(minimum_gap,float(np.min(abs(score-threshold))));ltf_count+=1
            if name.startswith('monotone'):
                n=r['n'];v=unpack(r['tt'],n)<0;t=np.arange(1<<n)
                for i in range(n):class_errors+=int(np.count_nonzero(v>v[t|1<<i]))
                monocount+=1
    assert class_errors==0
    large=json.loads(Path('large_audit.json').read_text());hp=[];err=0
    for a in large['rows']:
        r=next(r for r in allrows if r['tt']==a['tt'] and r['n']==a['n']);vals=objective(r)
        for k,v in vals.items():err=max(err,abs(float(v)-r[k]/r['I']))
        hp.append(dict(tag=r['tag'],n=r['n'],tt=r['tt'],ratios={k:mp.nstr(v,65) for k,v in vals.items()}))
    assert err<1e-10
    audit=json.loads(Path('audit.json').read_text());assert max(audit['maximum_absolute_errors'].values())<1e-10
    for path in ['composition.json','highprecision.json','symmetric_audit.json','quantized.json','cardinality_dilution.json','majority_meets.json']:assert json.loads(Path(path).read_text())
    constants=dict(C_MAJ3_gate_bound=str(1024/mp.log(2)),C_tree_read_formula='2+(4+4*sqrt(k))*log2(3)',C_symmetric_inherited='4.650431',C_AND_OR_XOR_inherited='10',C_readonce_tree_inherited='4.88')
    z=dict(passed=True,ltf_checked=ltf_count,monotone_checked=monocount,class_membership_errors=int(class_errors),minimum_LTF_score_gap=minimum_gap,highprecision_large_max_ratio_residual=err,highprecision_large=hp,constants=constants,elapsed_seconds=time.time()-start,maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,nice=os.getpriority(os.PRIO_PROCESS,0),threads=1)
    Path('final_audit.json').write_text(json.dumps(z,indent=2)+'\n');print('FINAL AUDIT PASS',ltf_count,monocount,err)
if __name__=='__main__':main()
