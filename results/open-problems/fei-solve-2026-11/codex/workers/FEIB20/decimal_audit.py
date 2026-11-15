#!/usr/bin/env python3
from decimal import Decimal as Z, getcontext
getcontext().prec=70
import nested as N
import math,json,time

class DecState:
    def __init__(self,w,D):
        self.w,self.D,self.L=w,D,w-1;L=self.L;M=D*L;self.M=M
        self.a=Z(2)**(-L);self.s=(1-self.a)**(D-1)
        alpha=(1+self.s)/2;beta=self.s/2
        self.meanP=(alpha**M+(alpha**L-beta**L)**D)/2
        self.root=False;self.z=[False]*M;self.r=[[0]*(D-1) for _ in range(M)]
        self.ss=[self.s]*M;self.mn=[alpha]*M;self.mb=[beta]*M;self.bb=[beta]*M
        self.bn=[alpha**L]*D;self.bc=[beta**L]*D;self.bd=self.bc[:]
        self.prods=[alpha**M,(alpha**L-beta**L)**D,(alpha**L-beta**L)**D]
        self.clause=[1-2*self.a+self.a*Z(2)**(-r) for r in range(L+1)]
    def corr(self):
        a,b,c=self.prods;pp=(a+2*b+c)/4 if self.root else (a+c)/2
        return 1-4*self.meanP+4*pp
    def update(self,i):
        if i==0:self.root=True;return
        if i<=self.M:m=i-1;self.z[m]=True
        else:
            m,rem=divmod(i-1-self.M,(self.D-1)*self.L);c,l=divmod(rem,self.L)
            r=self.r[m][c];self.ss[m]*=self.clause[r+1]/self.clause[r];self.r[m][c]+=1
        t=m//self.L;old=[self.bn[t],self.bn[t]-self.bc[t],self.bn[t]-2*self.bc[t]+self.bd[t]]
        zz=Z(1)/4 if self.z[m] else Z(1)/2
        nn=self.s+zz*(1-2*self.s+self.ss[m]);nb=self.s/2-zz*(self.s-self.ss[m]);bb=zz*self.ss[m]
        self.bn[t]*=nn/self.mn[m];self.bc[t]*=nb/self.mb[m];self.bd[t]*=bb/self.bb[m]
        self.mn[m],self.mb[m],self.bb[m]=nn,nb,bb
        new=[self.bn[t],self.bn[t]-self.bc[t],self.bn[t]-2*self.bc[t]+self.bd[t]]
        for k in range(3):self.prods[k]*=new[k]/old[k]

def phi(p,q):
    p,q=float(p),float(q)
    if min(p,q)<=0:return 0.
    return (p*math.log1p(q/p)+q*math.log1p(p/q))/math.log(2)

def witness(w,D,i,order):
    a,b=DecState(w,D),DecState(w,D);b.update(i)
    def wg():
        g=b.corr();return a.corr()-g,g
    oldw,oldg=wg();delta=oldw;terms=[];minstep=Z(0)
    for j in reversed(order):
        if j==i:continue
        a.update(j);b.update(j);ww,gg=wg();p,q=oldg-gg,oldw-ww
        minstep=min(minstep,p,q);terms.append(phi(p,q));oldw,oldg=ww,gg
    return float(delta),math.fsum(terms+[phi(oldg,oldw)])/float(delta),str(minstep)

def run():
    out=[]
    cases=[(10,8,c,k) for c in ['root','mate','leaf'] for k in ['leaves_first','mates_first','clause','block','random','private_last'] if k!='private_last' or c=='leaf']
    cases += [(16,55,'root','clause'),(16,55,'leaf','private_last')]
    for w,D,c,k in cases:
        T=N.Model(w,D);i={'root':0,'mate':1,'leaf':T.leaf(0,0,0)}[c];start=time.time()
        delta,r,negative=witness(w,D,i,T.order(k));old=next(x for x in json.load(open('rows.json')) if (x['w'],x['D'],x['coordinate'],x['order'])==(w,D,c,k))
        row={'w':w,'D':D,'coordinate':c,'order':k,'decimal_inf':delta,'decimal_ratio':r,'float_ratio_difference':r-old['ratio'],'min_step':negative,'seconds':time.time()-start}
        out.append(row);print(json.dumps(row),flush=True)
        with open('decimal_audit.json','w') as f:json.dump(out,f,indent=2)
if __name__=='__main__':run()
