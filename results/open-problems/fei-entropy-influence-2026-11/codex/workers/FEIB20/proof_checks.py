#!/usr/bin/env python3
from decimal import Decimal as Z, getcontext
getcontext().prec=70
import json, math
from decimal_audit import DecState
import nested as N

def run():
    rows=json.load(open('rows.json'));out=[]
    for w,D in [(3,2),(4,2),(10,8),(12,16),(14,30),(16,55)]:
        L=w-1;a=Z(2)**(-L);s=(1-a)**(D-1);alpha=(1+s)/2;beta=s/2;q=1-s
        m=alpha**L-beta**L
        root=alpha**(D*L)-m**D
        mate=(q*alpha**(D*L-1)+(q*alpha**(L-1)+s*beta**(L-1))*m**(D-1))/2
        leaf=Z(2)**(-L-1)*(1-a)**(D-2)*(alpha**(D*L-1)+(alpha**(L-1)-beta**(L-1))*m**(D-1))
        T=N.Model(w,D);indices=[0,1,T.leaf(0,0,0)];errs=[]
        for delta,i in zip([root,mate,leaf],indices):
            A=DecState(w,D);B=DecState(w,D);B.update(i);errs.append(float(abs(delta-(A.corr()-B.corr()))))
        upper=2*(1-2**(-(L-1)))+2**(-(L-1))*math.log2(math.e/(float(leaf)*2**(-(L-1))))
        lower=2*(1-2**(-(L-1)))
        # Exact no-leaves probability in the root derivative spectrum.
        A=((1+s*s)/2)**L;B=(s*s/2)**L
        c=(A**D-(A-B)**D)/root
        r={'w':w,'D':D,'n':T.n,'lambda':float(D*D*L*a),'root_inf':float(root),'mate_inf':float(mate),'leaf_inf':float(leaf),'influence_identity_max_error':max(errs),'leaf_E_lower':lower,'leaf_witness_general_upper':upper,'root_c':float(c),'mates_first_leading_prediction':float((1-c)*Z(str(math.log2(1/float(root))))),'uniform_bound_formula':2+2**(-(L-1))*(2*L-2+4*math.log2(math.e))}
        if w>=10:
            actual=next(x['ratio'] for x in rows if x['w']==w and x['coordinate']=='leaf' and x['order']=='private_last')
            assert lower<=actual+1e-8 and actual<=upper+1e-8
            r['leaf_witness_measured']=actual
            rootactual=next(x['ratio'] for x in rows if x['w']==w and x['coordinate']=='root' and x['order']=='mates_first')
            r['mates_first_measured']=rootactual;r['prediction_additive_residual']=rootactual-r['mates_first_leading_prediction']
        out.append(r);print(json.dumps(r),flush=True)
    endpoint=2+0.5*(2+4*math.log2(math.e))
    summary={'uniform_bound_endpoint_L2':endpoint,'all_influence_checks_pass':max(x['influence_identity_max_error'] for x in out)<1e-60,'decimal_precision_digits':70,'float_longdouble_mantissa_bits':int(__import__('numpy').finfo(N.F).nmant),'rows':out}
    assert summary['all_influence_checks_pass'];assert endpoint<6
    with open('proof_checks.json','w') as f:json.dump(summary,f,indent=2)
if __name__=='__main__':run()
