import sympy as S, json
from math import comb
s=S.symbols('s'); R=S.Rational
L=S.Matrix([[R(1,10),R(9,100),R(1,100)],[R(9,100),R(1,10),0],[R(1,100),0,10]])
v=S.Matrix([1,-1,-R(1,1100)])
T=L+(1+s)*S.eye(3); Z=S.factor(T.det()); G=L+s*S.eye(3)
x=[G[i,i] for i in range(3)];dd=[G.extract([1,2],[1,2]).det(),G.extract([0,2],[0,2]).det(),G.extract([0,1],[0,1]).det()]
f=[S.factor(x[0]*x[2]/dd[1]),S.factor(x[0]*x[1]/dd[2]),S.factor(S.prod(dd)/(S.prod(x)*G.det()))]
a=[S.factor(2*(v.dot(T[:,1]))**2/Z**2),S.factor(2*(v.dot(T[:,2]))**2/Z**2),S.factor(2*(v.dot((T*T-T)*v))/Z**2)]
# k-th derivative of a log f, with all coefficients exact.
def jets(expr,n):
 out=[]
 for k in range(n+1):
  out.append(S.factor(expr.subs(s,0)))
  expr=S.cancel(S.diff(expr,s))
 return out
k=5
qlog=[];qrat=S.Rational(0)
for ai,fi in zip(a,f):
 aj=jets(ai,k);lj=[None]+jets(S.cancel(S.diff(fi,s)/fi),k-1)
 qlog.append((-1)**k*aj[k])
 qrat+=(-1)**k*sum(comb(k,j)*aj[j]*lj[k-j] for j in range(k))
args=[fi.subs(s,0) for fi in f]
print('arguments',args,flush=True)
value=qrat+sum(c*S.log(x) for c,x in zip(qlog,args))
print('alternating derivative',S.N(value,40),flush=True)
assert -9<qrat<-8 and 0<qlog[0]<5 and 0<qlog[1]<R(1,10000) and -30<qlog[2]<0
assert -9-30*R(9,21100)>-10 and -8+5*R(1,9999)+R(81,190000)<-7
# Strict rational enclosures for logarithms, using positive atanh series.
def log_interval(x,N=600):
 assert x>=1
 z=(x-1)/(x+1)
 low=2*sum(z**(2*j+1)/R(2*j+1) for j in range(N))
 tail=2*z**(2*N+1)/(R(2*N+1)*(1-z*z))
 return low,low+tail
lo=hi=qrat
for c,x in zip(qlog,args):
 l,h=log_interval(x)
 if c>=0:lo+=c*l;hi+=c*h
 else:lo+=c*h;hi+=c*l
assert hi<0
print('certified interval',S.N(lo,30),S.N(hi,30),flush=True)
assert lo> -20 and hi< -1
out={'status':'PASS','L':[[str(v) for v in row] for row in L.tolist()],'v':[str(x) for x in v],'order':k,'log_arguments':[str(x) for x in args],'rational_part':str(qrat),'log_coefficients':[str(x) for x in qlog],'decimal_interval':[str(S.N(lo,30)),str(S.N(hi,30))],'rigorous_simple_interval':['-20','-1'],'log_enclosure_terms':600}
out['elementary_log_certificate']={'rational_part_bounds':['-9','-8'],'coefficient_bounds':[['0','5'],['0','1/10000'],['-30','0']],'rigorous_interval':['-10','-7']}
open('computations/X070/certificate.json','w').write(json.dumps(out,indent=2)+'\n')
