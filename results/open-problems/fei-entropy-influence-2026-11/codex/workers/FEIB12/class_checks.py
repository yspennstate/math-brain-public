import json
from pathlib import Path
from numerics import *

def check(F,label):
    d=data(F,True);n=F.shape[-1].bit_length()-1;N=1<<n;mu=d['mu'];H=d['phi'][:,0];I=d['I'];v=d['var']
    degree=np.max(np.where(mu>0,d['pc'],0),axis=-1)
    bound=(2*np.maximum(degree-1,0)+1/np.log(2))*I
    gran=0.;pure=np.ones(len(F),bool);mono=np.ones(len(F),bool);first=0.;higher=0.
    for S in range(1,N):
        g=derivative(F,S);one=(g.min(axis=-1)>=0)|(g.max(axis=-1)<=0);pure &=one
        if S.bit_count()==1:
            mono&=g.min(axis=-1)>=0
            # Each singleton contribution vanishes on unate derivatives.
            z=mu[:,S]*np.log2(np.maximum(d['alpha'][:,S],1e-300)/np.maximum(abs(d['hat'][:,S]),1e-300))
            first=max(first,float(abs(z[one]).max(initial=0)))
        else:
            for i in range(n):
                if S>>i&1:higher=max(higher,float((d['alpha'][:,S]-d['alpha'][:,1<<i]).max()))
        mult=d['hat'][:,S]*2.**np.maximum(degree-1,0)
        gran=max(gran,float(abs(mult-np.rint(mult)).max()))
    bias=mu[:,0]*np.log2(1/np.maximum(abs(d['hat'][:,0]),1e-300))
    out=dict(label=label,functions=len(F),monotone_increasing_count=int(mono.sum()),all_nonempty_derivatives_one_sign_count=int(pure.sum()),pure_gamma_bias_max_error=float(abs(d['gamma'][pure]-bias[pure]).max(initial=0)),pure_gamma_bound_max_violation=float(max(0,(d['gamma'][pure]-I[pure]/(2*np.log(2))).max(initial=0))),degree_entropy_bound_max_violation=float(max(0,(H-bound).max())),degree_granularity_max_error=gran,first_level_gamma_max_error=first,higher_derivative_L1_contraction_max_violation=max(0,higher))
    assert max(out[k] for k in out if 'max_' in k)<1e-9,out
    Path('classes_'+label+'.json').write_text(json.dumps(out,indent=2));print(json.dumps(out),flush=True)
    return out
if __name__=='__main__':
    check(from_tt(np.arange(65536),4),'all4');check(sample(6,3000,1210),'sample6')
    # Unique median zero: derivative is +1 at seven points, -1 at one.
    x=np.arange(16);g=np.where((x>>1)==0,-1,1);f=(1-2*(x&1))*g
    d=data(f)[0] if False else data(f)
    q=d['mu'][0,[s for s in range(16) if s&1]]/d['F'][0,-1,1]
    levels=np.array([s.bit_count()-1 for s in range(16) if s&1]);level=[float(q[levels==k].sum()) for k in range(4)]
    witness=dict(tt=tt_hex(f),S=1,q_levels=level,median=0,F_over_up=float(d['F'][0,2,1]/d['F'][0,-1,1]))
    assert level[0]>.5 and witness['F_over_up']<1
    Path('unique_median_counterexample.json').write_text(json.dumps(witness,indent=2));print(witness)
