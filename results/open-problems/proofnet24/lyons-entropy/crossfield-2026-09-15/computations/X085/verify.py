"""Exact algebra and an independently constructed physical eight-atom jet.
The all-parameter signs are proved in agents/X085.md, not by sampling.
"""
import json
from pathlib import Path
import sympy as S

checks=[]
def prime_logs(expr):
    def replace_log(term):
        num,den=S.fraction(term.args[0])
        return sum(n*S.log(p) for p,n in S.factorint(int(num)).items())-sum(n*S.log(p) for p,n in S.factorint(int(den)).items())
    return expr.replace(lambda term:term.func==S.log and term.args[0].is_Rational and term.args[0]>0,replace_log)
def check(name,expr):
    value=S.simplify(S.expand(prime_logs(S.expand_log(expr,force=True))))
    if value!=0:
        value=S.simplify(S.expand(prime_logs(S.expand_log(value,force=True))))
    assert value==0,(name,value)
    checks.append(name)

a,d,al,e1,e0,g,k,de=S.symbols('a d al e1 e0 g k de', real=True)
b=1-a;q=a*b;r=S.sqrt(q*d)
z=(q*(e0-e1)+(b-a)*d*al)/(2*r)
be=a*e1+b*e0-d*al
check('physical determinant endpoint form',4*(al*be-z*z)-(2*al*(e1+e0)-d*al*al/q-q*(e0-e1)**2/d))
Q1,Q0=S.symbols('Q1 Q0',real=True)
s=1+d*g/2;h=g*(e1+e0)/2+k*de
physical=al*al/q+a*Q1+b*Q0-2*al*k*de-2*g*(al*be-z*z)
complete=s/q*(al-q*h/s)**2+q*(Q1/b+Q0/a+g*(e1-e0)**2/(2*d)-h*h/s)
check('complete physical pivot square',physical-complete)

x,l=S.symbols('x l',positive=True)
probs=[(1-x)*(1-l),(x+l-2*x*l)/2,(x+l-2*x*l)/2,x*l]
f=-sum(p*S.log(p) for p in probs)
t,L,T=S.symbols('t L T',real=True)
sig=1-t*t
A=2/sig;B=2-L;C=2*(1+t*t);R=C-B*B/A
check('half spectator J11',-S.diff(f,x,2).subs({x:(1-t)/2,l:S.Rational(1,2)})-A)
check('half spectator J22',-S.diff(f,l,2).subs({x:(1-t)/2,l:S.Rational(1,2)})-C)
J12=-S.diff(f,x,l).subs(l,S.Rational(1,2))
check('half spectator J12',J12-(2+S.log(4*x*(1-x))))
check('conditional scalar score',S.diff(f,l).subs(l,S.Rational(1,2))-((1-x)*S.log(2*(1-x))-x*S.log(2*x)))
check('R exact formula',R-(4*t*t+2*sig*L-sig*L*L/2))
v=T-t*L/2;w=v-B*T/A
check('w alternate formula',w-(t*t*T-L*(t-sig*T)/2))
D=lambda expr:S.diff(expr,t)+S.diff(expr,L)*2*t/sig+S.diff(expr,T)/sig
check('v derivative',D(v)-(1-L/2))
check('w derivative',D(w)-t*(3-L)*T)
check('moderate-L coefficient',1-S.Rational(6,7)/6-S.Rational(6,7)**2/20-S.Rational(201,245))
check('moderate-L w coefficient',S.Rational(201,245)+S.Rational(1,7)-S.Rational(236,245))
check('large-L w coefficient',S.Rational(8,11)+S.Rational(10,73)-S.Rational(694,803))
check('positive margin',S.Rational(1,2)-S.Rational(7,15)-S.Rational(1,30))
assert sum(S.Rational(2)**j/S.factorial(j) for j in range(7))>S.Rational(73,10)
assert sum(S.Rational(7,10)**j/S.factorial(j) for j in range(5))>2
assert 1-S.Rational(100,5329)>S.Rational(99,100)**2
assert 4*694**2<3*803**2
assert S.Rational(4,3)>S.Rational(64,49)
checks.extend(['exp(2) rational series bound','exp(7/10) rational series bound','t4 rational lower bound','large-L exact norm bound','cosh rational coefficient'])

kap,bstar,U,V,Ast=S.symbols('kap bstar U V Ast',real=True)
E=U*U+V*V;cs=bstar*bstar
Dcat=kap*U*U-Ast*Ast
check('categorical exact payment',s*E-(Ast+bstar*V)**2-((s-kap-cs)*E+(1+cs/kap)*Dcat+(S.sqrt(kap)*V-bstar*Ast/S.sqrt(kap))**2))
root1,root0=S.symbols('root1 root0',real=True)
check('pivot categorical mixture loss',root1**2/b+root0**2/a-(root1+root0)**2-(a/b*root1**2+b/a*root0**2-2*root1*root0))

# Independent measured-basis physical Hessian at asymmetric endpoints.
rr=S.sqrt(2)/6
K=S.Matrix([[S.Rational(1,3),rr,rr],[rr,S.Rational(7,12),S.Rational(1,12)],[rr,S.Rational(1,12),S.Rational(7,12)]])
Vel=S.Matrix([[1,0,0],[0,0,1],[0,1,0]])
u=S.symbols('u',real=True);Kt=K+u*Vel
ps=[];dp=[];ddp=[]
for mask in range(8):
    mat=Kt.copy()
    for j in range(3):
        if not (mask>>j)&1:
            mat[:,j]=S.eye(3)[:,j]-Kt[:,j]
    p=S.expand(mat.det());ps.append(p.subs(u,0));dp.append(S.diff(p,u).subs(u,0));ddp.append(S.diff(p,u,2).subs(u,0))
check('physical normalization',sum(ps)-1)
check('physical trace normalization',sum(dp))
check('physical acceleration normalization',sum(ddp))
Hneg=sum(dp[i]**2/ps[i]+ddp[i]*S.log(ps[i]) for i in range(8))

def endpoint(xx,ee,delta):
    tt=1-2*xx;ll=-S.log(1-tt*tt);ttt=S.log((1+tt)/(1-tt))/2
    vv=ttt-tt*ll/2
    jj=S.Matrix([[2/(1-tt*tt),2-ll],[2-ll,2*(1+tt*tt)]])
    ww=S.Matrix([ee,delta]);qq=(ww.T*jj*ww)[0]
    return qq,ttt,vv,ttt*ee+vv*delta

aa=S.Rational(1,3);bb=1-aa;qq=aa*bb;dd=S.Rational(1,2)
ee1=S.Integer(2);ee0=S.Rational(5,4);delta=-S.Integer(1)
q1,t1,v1,f1=endpoint(S.Rational(1,3),ee1,delta)
q0,t0,v0,f0=endpoint(S.Rational(5,6),ee0,delta)
gg=t1-t0;kk=v1-v0;ss=1+dd*gg/2;hh=gg*(ee1+ee0)/2+kk*delta
reduction=ss/qq*(1-qq*hh/ss)**2+qq*(q1/bb+q0/aa+gg*(ee1-ee0)**2/(2*dd)-hh*hh/ss)
check('physical eight-atom Hessian equals endpoint curvature',Hneg-reduction)
# Check the square grouping after cancellation of the positive radicals.
UU=S.sqrt(q1)+S.sqrt(q0);VV=S.sqrt(gg/(2*dd))*(ee0-ee1)
bs=(t1+t0)*S.sqrt(dd/(2*gg));cc=S.simplify(bs*bs);EE=UU*UU+VV*VV
AST=f1-f0;KAP=S.Rational(1,2)
check('physical categorical h identity',hh-(AST+bs*VV))
# Formula (13) is checked through its algebraically equivalent scalar pieces,
# avoiding an expensive symbolic expansion of unrelated square roots.
DC=KAP*UU*UU-AST*AST
GM=aa/bb*q1+bb/aa*q0-2*S.sqrt(q1*q0)
payment=(ss-KAP-cc)*EE+(1+cc/KAP)*DC+(S.sqrt(KAP)*VV-bs*AST/S.sqrt(KAP))**2
check('example gap grouping',payment-(ss*EE-hh*hh))
check('example mixture grouping',GM+EE-(q1/bb+q0/aa+gg*(ee1-ee0)**2/(2*dd)))

out={'status':'PASS','exact_assertions':len(checks),'checks':checks,
 'example':{'x1':'1/3','x0':'5/6','a':'1/3','lambda':'1/2','active_determinant':'1','spectator_velocity':'-1',
 'physical_negative_Hessian_exact':str(S.simplify(S.expand_log(Hneg,force=True))),
 'physical_negative_Hessian_decimal':str(S.N(Hneg,30)),
 'guaranteed_lower_bound_decimal':str(S.N(ss/qq*(1-qq*hh/ss)**2+qq/(30*ss)*EE,30)),
 'categorical_energy_decimal':str(S.N(EE,30)),
 's_minus_kappa_C_decimal':str(S.N(ss-KAP-cc,30))}}
Path(__file__).with_name('certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
