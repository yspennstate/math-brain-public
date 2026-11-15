"""Independent closed-form, truth-table, and formula audits."""
import json,ast,math
from pathlib import Path
from families import majority_large,and_large
from numerics import *

def evaltree(node,x,n,used):
    if isinstance(node,ast.Name):
        i=int(node.id[1:]);used.append(i);assert 0<=i<n;return 1-2*((x>>i)&1)
    assert isinstance(node,ast.Call) and isinstance(node.func,ast.Name)
    name=node.func.id;args=[evaltree(a,x,n,used) for a in node.args]
    if name=='NOT':assert len(args)==1;return -args[0]
    assert name in ['AND','OR'] and len(args)==2
    p=(args[0]>0)&(args[1]>0) if name=='AND' else (args[0]>0)|(args[1]>0)
    return 2*p.astype(np.int8)-1

def main():
    rows=json.load(open('families.json'));rng=np.random.default_rng(1911);out={};major=0.;ands=0.;formula_bad=0;sign_bad=0;gamma_bad=0.;coupling_bad=0.
    for n in [3,5,9,15]:
        f=1-2*(pc(n)>n//2);d=data(f);r=majority_large(n)
        major=max(major,float(abs(d['phi'][0]-r['phi']).max()))
    for n in [2,3,5,8,16]:
        f=np.ones(1<<n);f[0]=-1;d=data(f);r=and_large(n)
        ands=max(ands,float(abs(d['phi'][0]-r['phi']).max()))
    for r in rows:
        if r['family']=='read_once':
            n=r['n'];x=np.arange(1<<n);used=[];f=evaltree(ast.parse(r['tree'],mode='eval').body,x,n,used)
            assert sorted(used)==list(range(n));formula_bad+=tt_hex(f)!=r['tt']
            sets=list(range(1,1<<n)) if n<=8 else list(rng.choice(np.arange(1,1<<n),16,replace=False))
            for S in sets:
                g=derivative(f,int(S));sign_bad+=not(g.min()>=0 or g.max()<=0)
            if 'gamma' in r:
                b=f.mean();expected=b*b*math.log2(1/abs(b)) if b else 0.;gamma_bad=max(gamma_bad,abs(r['gamma']-expected))
        if r.get('conditional_entropy_over_I') is not None and r['I']>0:
            C=r['conditional_entropy_over_I']*r['I'];H=r['phi'][0];B=H-r['phi'][-1]
            coupling_bad=max(coupling_bad,B-C,C-H)
    # Direct double-sum conditional entropy vs subset zeta, on separate random functions.
    F=sample(6,40,429);d=data(F);Z,kl,C=coupling(d);ref=np.zeros_like(Z)
    for U in range(64):
        for S in range(64):
            if U&S==S:ref[:,U]+=np.divide(d['mu'][:,S],d['F'][:,-1,S],out=np.zeros(len(F)),where=d['F'][:,-1,S]>0)
    zerr=float(abs(ref-Z).max())
    out=dict(majority_closed_form_vs_dense_max_error=major,AND_closed_form_vs_dense_max_error=ands,formula_truth_table_mismatches=formula_bad,one_sign_derivative_failures=sign_bad,formula_gamma_bias_max_error=gamma_bad,conditional_entropy_bounds_max_violation=max(0,coupling_bad),subset_zeta_vs_double_sum_max_error=zerr,rows=len(rows))
    assert max(out[k] for k in out if k!='rows')<1e-10,out
    Path('families_audit.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
if __name__=='__main__':main()
