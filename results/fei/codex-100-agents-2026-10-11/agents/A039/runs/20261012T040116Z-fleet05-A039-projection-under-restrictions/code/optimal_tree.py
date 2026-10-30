from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import importlib.util,json,hashlib,time,sys

RUN=Path(__file__).resolve().parents[1]
OLD=RUN.parents[1]/'runs/20261011T223903Z-fleet05-A039-projection-under-restrictions/code/baseline_check.py'
sp=importlib.util.spec_from_file_location('a039_logs',OLD); logs=importlib.util.module_from_spec(sp); sp.loader.exec_module(logs)
Q=logs.SCALE
ASSERTIONS=0
LOG_USED=set()
def check(x):
    global ASSERTIONS
    ASSERTIONS+=1
    assert x,ASSERTIONS
def add(*terms):
    z={}
    for c,t in terms:
        for p,e in t.items(): z[p]=z.get(p,0)+c*e
    return {p:e for p,e in z.items() if e}
def halfsum(a,b):
    z=add((1,a),(1,b)); check(all(e%2==0 for e in z.values()))
    return {p:e//2 for p,e in z.items() if e}
@lru_cache(None)
def factor(x):
    z={}; p=2
    while p*p<=x:
        while x%p==0: z[p]=z.get(p,0)+1; x//=p
        p=3 if p==2 else p+2
    if x>1: z[x]=z.get(x,0)+1
    return z
def mlog(x): return {p:x*e for p,e in factor(x).items()} if x else {}
@lru_cache(None)
def logbounds(p):
    LOG_USED.add(p)
    a,b=logs.log2(F(p)); return (a*Q).__floor__(),(b*Q).__ceil__()
def iv(v):
    lo=hi=0
    for p,e in v.items():
        a,b=logbounds(p)
        if e<0: a,b=b,a
        lo+=e*a; hi+=e*b
    return lo,hi
def decimal(v,den):
    lo,hi=iv(v); scale=10**12
    return {'lower':str(F((F(lo,den*Q)*scale).__floor__(),scale)),'upper':str(F((F(hi,den*Q)*scale).__ceil__(),scale))}
def fw(t):
    t=t.copy(); w=1
    while w<len(t):
        for j in range(0,len(t),2*w):
            for s in range(j,j+w): t[s],t[s+w]=t[s]+t[s+w],t[s]-t[s+w]
        w*=2
    return t
def restrict(t,i,y): return [t[(s&((1<<i)-1))|((s>>i)<<(i+1))|(y<<i)] for s in range(len(t)//2)]
def norm(state):
    if state[0]=='C': return ('C',)
    if state[0]=='D':
        _,a,d,t,r=state
        if a==d==0: return norm(('P',0,t-1,-1 if t==1 else 1,r))
    else:
        _,a,l,s,r=state
        if a==l==0 and (s==1 or r==0): return ('C',)
    return state
def dimension(s):
    if s[0]=='C': return 0
    if s[0]=='D': return 2*s[1]+s[2]+(s[3]==2)+s[4]
    return 2*s[1]+s[2]+s[4]
@lru_cache(None)
def core(s):
    if s[0]=='C': return (1,)
    if s[0]=='D':
        _,a,d,t,r=s; m=2*a+d+(t==2); tab=[]
        for x in range(1<<m):
            bit=x&((1<<(2*a+d))-1)
            v=(-1)**sum(((bit>>(2*j))&1)*((bit>>(2*j+1))&1) for j in range(a))
            if bit==0 and (t==1 or x>>(2*a+d)==1): v=-v
            tab.append(v)
    else:
        _,a,l,sig,r=s; m=2*a+l
        tab=[sig*(-1)**(sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(a))+sum((x>>(2*a+j))&1 for j in range(l))) for x in range(1<<m)]
    return tuple(tab)
def actions(s):
    if s[0]=='C': return []
    out=[]
    if s[0]=='D':
        _,a,d,t,r=s
        if r: out.append(('control',None,norm(('D',a,d,t,r-1)),('C',)))
        if a: out.append(('pair',0,norm(('D',a-1,d+1,t,r)),norm(('P',a-1,1,1,r))))
        if d: out.append(('singleton',2*a,norm(('D',a,d-1,t,r)),norm(('P',a,0,1,r))))
        if t==2: out.append(('selector',2*a+d,norm(('P',a,0,1,r)),norm(('D',a,d,1,r))))
    else:
        _,a,l,sig,r=s
        if r: out.append(('control',None,norm(('P',a,l,sig,r-1)),('C',)))
        if a: out.append(('pair',0,norm(('P',a-1,l,sig,r)),norm(('P',a-1,l+1,sig,r))))
        if l: out.append(('linear',2*a,norm(('P',a,l-1,sig,r)),norm(('P',a,l-1,-sig,r))))
    return out

class Solver:
    def __init__(self,N):
        self.N=N; self.D=1<<(2*N); self.W=1<<N; self.CDEN=self.D*self.W
        self.data={}; self.opt={}; self.records={}; self.comparisons=0; self.ties=0
    def Hmass(self,atoms):
        check(sum(mult*x for mult,x in atoms)==self.D)
        return add((1,{2:2*self.N*self.D}),*[(-mult,mlog(x)) for mult,x in atoms])
    def hb(self,x): return self.Hmass([(1,x),(1,self.D-x)])
    def phi(self,a,b): return add((1,mlog(a+b)),(-1,mlog(a)),(-1,mlog(b)))
    def facts(self,s):
        s=norm(s)
        if s in self.data: return self.data[s]
        if s[0]=='C':
            z={'H':{},'M':{},'TC':{},'Inf':0,'queries':{}}; self.data[s]=z; return z
        tab=core(s); m=len(tab).bit_length()-1; r=s[-1]; w=fw(list(tab)); sc=1<<(2*(self.N-m-r))
        amps=[x for x in w]; amps[0]-=1<<m
        empty=(amps[0]+(1<<(m+r)))**2*sc
        atoms=[(1,empty),((1<<r)-1,amps[0]**2*sc)]+[(1<<r,x*x*sc) for x in w[1:]]
        H=self.Hmass(atoms)
        d=[(1<<r)*sum(w[t]*w[t]*sc for t in range(1<<m) if t>>i&1) for i in range(m)]
        dc=((1<<m)-w[0])*(1<<(2*self.N-m-r))
        d+=([dc]*r)
        M=add(*[(1,self.hb(x)) for x in d]); queries={}
        for name,i,c0,c1 in actions(s):
            check(dimension(c0)<dimension(s) and dimension(c1)<dimension(s))
            if name=='control':
                B=add((1,self.phi(empty,amps[0]**2*sc)),((1<<(r-1))-1,self.phi(amps[0]**2*sc,amps[0]**2*sc)),*[(1<<(r-1),self.phi(x*x*sc,x*x*sc)) for x in w[1:]])
                di=dc
            else:
                B={}
                for t in range(1<<(m-1)):
                    ix=(t&((1<<i)-1))|((t>>i)<<(i+1)); jx=ix|(1<<i)
                    if t:
                        B=add((1,B),(1<<r,self.phi(w[ix]*w[ix]*sc,w[jx]*w[jx]*sc)))
                    else:
                        B=add((1,B),((1<<r)-1,self.phi(amps[0]**2*sc,w[jx]*w[jx]*sc)),(1,self.phi(empty,w[jx]*w[jx]*sc)))
                di=d[i]
            queries[name]={'B':B,'d':di,'children':(c0,c1)}
        z={'H':H,'M':M,'TC':add((1,M),(-1,H)),'Inf':sum(d),'d':d,'queries':queries}; self.data[s]=z; return z
    def solve(self,s):
        s=norm(s)
        if s in self.opt: return self.opt[s]
        facts=self.facts(s)
        if s[0]=='C': self.opt[s]={}; self.records[s]={'chosen':[],'value':{}}; return {}
        vals={}
        for name,z in facts['queries'].items():
            c0,c1=z['children']; v=add((self.W,z['B']),(1,halfsum(self.solve(c0),self.solve(c1))))
            vals[name]=v
        best=next(iter(vals)); ties=[best]; comparisons=[]
        for name in list(vals)[1:]:
            diff=add((1,vals[name]),(-1,vals[best])); bounds=iv(diff)
            if not diff: self.ties+=1; ties.append(name); sign='TIE'
            elif bounds[1]<0: best=name; ties=[name]; sign='NEGATIVE'
            elif bounds[0]>0: sign='POSITIVE'
            else: raise ArithmeticError(('uncertified comparison',s,name,best,diff,bounds))
            comparisons.append({'candidate':name,'sign':sign,'bounds_in_log_scale':list(map(str,bounds)),'difference_log_coefficients':{str(p):str(e) for p,e in diff.items()}}); self.comparisons+=1
        # Verify the chosen value against every alternative, including exact ties.
        verified=[]
        for name,v in vals.items():
            gap=add((1,v),(-1,vals[best])); bd=iv(gap)
            check(not gap or bd[0]>0)
            verified.append({'action':name,'gap_log_coefficients':{str(p):str(e) for p,e in gap.items()},'lower':str(bd[0]),'upper':str(bd[1])})
        self.opt[s]=vals[best]; self.records[s]={'chosen':ties,'best_action':best,'value':{str(p):str(e) for p,e in vals[best].items()},'alternatives':verified}
        return vals[best]
    def policy(self,s,mode):
        s=norm(s)
        if s[0]=='C': return {}
        z=self.facts(s); opts=z['queries']
        if mode=='control': name='control' if 'control' in opts else self.records[s]['best_action']
        elif mode=='data': name=next(x for x in ['pair','singleton','linear','selector','control'] if x in opts)
        elif mode=='selector': name='selector' if 'selector' in opts else ('control' if 'control' in opts else self.records[s]['best_action'])
        else: name=self.records[s]['best_action']
        a=opts[name]; c0,c1=a['children']
        nextmode='control' if mode=='selector' else mode
        return add((self.W,a['B']),(1,halfsum(self.policy(c0,nextmode),self.policy(c1,nextmode))))
    def ledger(self,root):
        reach={root:F(1)}; rows=[]; sums={x:{} for x in ['B','JS','credit','Gamma','marginal_bill']}; inf=F(0)
        for s in sorted(self.opt,key=dimension,reverse=True):
            w=reach.get(s,F(0))
            if not w or s[0]=='C': continue
            f=self.facts(s); name=self.records[s]['best_action']; z=f['queries'][name]; c0,c1=z['children']
            Hc=halfsum(add((self.W,self.facts(c0)['H'])),add((self.W,self.facts(c1)['H'])))
            Mc=halfsum(add((self.W,self.facts(c0)['M'])),add((self.W,self.facts(c1)['M'])))
            B=add((self.W,z['B'])); bill=add((self.W,self.hb(z['d'])))
            JS=add((self.W,f['H']),(-1,Hc),(-1,B)); credit=add((1,bill),(-1,B))
            Gamma=add((self.W,f['M']),(-1,bill),(-1,Mc))
            for key,value in [('B',B),('JS',JS),('credit',credit),('Gamma',Gamma),('marginal_bill',bill)]: sums[key]=add((1,sums[key]),(w,value))
            inf+=w*z['d']; reach[c0]=reach.get(c0,F(0))+w/2; reach[c1]=reach.get(c1,F(0))+w/2
            rows.append({'state':list(s),'visit_probability':str(w),'chosen_action':name,'B':decimal(B,self.CDEN),'JS':decimal(JS,self.CDEN),'credit':decimal(credit,self.CDEN),'Gamma':decimal(Gamma,self.CDEN),'removed_influence':str(F(z['d'],self.D))})
        check(sums['B']==self.opt[root]); check(add((1,sums['B']),(1,sums['JS']),(-self.W,self.facts(root)['H']))=={})
        check(add((1,sums['credit']),(1,sums['Gamma']),(-self.W,self.facts(root)['TC']),(-1,sums['JS']))=={})
        check(inf==self.facts(root)['Inf'])
        return {'rows':rows,'sums':{k:decimal(v,self.CDEN) for k,v in sums.items()},'removed_influence':str(F(inf,self.D)),'terminal_entropy':'0','terminal_TC':'0'}
    def direct(self,root):
        memo={}
        def solve(tab):
            if tab in memo: return memo[tab]
            n=len(tab).bit_length()-1
            if all(x==tab[0] for x in tab): memo[tab]={}; return {}
            wal=fw(list(tab)); scale=1<<(2*(self.N-n)); p=[x*x*scale for x in wal]; H=self.Hmass([(1,x) for x in p]); vals=[]
            for i in range(n):
                if not any(p[t] for t in range(1<<n) if t>>i&1): continue
                B={}
                for t in range(1<<(n-1)):
                    ix=(t&((1<<i)-1))|((t>>i)<<(i+1)); B=add((1,B),(1,self.phi(p[ix],p[ix|(1<<i)])))
                c0=solve(tuple(restrict(tab,i,0))); c1=solve(tuple(restrict(tab,i,1)))
                vals.append(add((self.W,B),(1,halfsum(c0,c1))))
            best=vals[0]
            for v in vals[1:]:
                gap=add((1,v),(-1,best)); b=iv(gap)
                if not gap: pass
                elif b[1]<0: best=v
                else: check(b[0]>0)
            memo[tab]=best; return best
        tab=core(root); m=len(tab).bit_length()-1; r=root[-1]
        full=tuple(tab[x&((1<<m)-1)] if x>>m==0 else 1 for x in range(1<<(m+r)))
        opt=solve(full); check(opt==self.opt[root]); return {'direct_truth_states':len(memo),'same_exact_optimum':True,'root_truth_table_sha256':hashlib.sha256(bytes(x==1 for x in full)).hexdigest()}
    def root_direct_spectra(self,root):
        tab=core(root); m=len(tab).bit_length()-1; r=root[-1]; full=[tab[x&((1<<m)-1)] if x>>m==0 else 1 for x in range(1<<(m+r))]
        wal=fw(full); p=[x*x for x in wal]; check(self.Hmass([(1,x) for x in p])==self.facts(root)['H'])
        for name,z in self.facts(root)['queries'].items():
            i=m if name=='control' else next(i for nam,i,_,_ in actions(root) if nam==name)
            B={}
            for t in range(1<<(self.N-1)):
                ix=(t&((1<<i)-1))|((t>>i)<<(i+1)); B=add((1,B),(1,self.phi(p[ix],p[ix|(1<<i)])))
            check(B==z['B']); check(sum(p[t] for t in range(1<<self.N) if t>>i&1)==z['d'])
        return {'root_dimension':self.N,'root_spectrum_atoms':len(p),'all_root_query_orbits_match_direct_Walsh':True}
def encode(v): return {str(p):str(e) for p,e in v.items()}
def main():
    k=int(sys.argv[1]); start=time.perf_counter(); root=('D',k//2,0,2,2*k); s=Solver(3*k+1)
    value=s.solve(root); ledger=s.ledger(root); policies={x:s.policy(root,x) for x in ['control','selector','data']}
    for val in policies.values():
        gap=add((1,val),(-1,value)); check(not gap or iv(gap)[0]>0)
    direct=s.direct(root) if k==2 else s.root_direct_spectra(root)
    facts=s.facts(root); ratio_den=s.W*facts['Inf']
    out={'status':'PASS','k':k,'root':list(root),'denominator':s.CDEN,'optimal_cost_log_coefficients':encode(value),'optimal_cost':decimal(value,s.CDEN),'optimal_cost_over_total_influence':decimal(value,ratio_den),'total_influence':str(F(facts['Inf'],s.D)),'entropy':decimal(add((s.W,facts['H'])),s.CDEN),'root_optimal_actions':s.records[root]['chosen'],'policies':{x:{'cost':decimal(v,s.CDEN),'cost_over_total_influence':decimal(v,ratio_den),'exact_gap_from_optimum':encode(add((1,v),(-1,value)))} for x,v in policies.items()},'ledger':ledger,'states':len(s.opt),'comparisons':s.comparisons,'exact_ties_encountered':s.ties,'assertions':ASSERTIONS,'independent_reconstruction':direct,'runtime_seconds':time.perf_counter()-start,'log_helper_sha256':hashlib.sha256(OLD.read_bytes()).hexdigest()}
    check(time.perf_counter()-start<(60 if k==2 else 1200))
    (RUN/'out'/f'OPTIMUM_K{k}.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    cert={'k':k,'probability_denominator':s.D,'cost_denominator':s.CDEN,'log_interval_scale':Q,'records':[{'state':list(st),**rec} for st,rec in s.records.items()],'prime_log_intervals':{str(p):list(map(str,logbounds(p))) for p in sorted(LOG_USED)}}
    (RUN/'out'/f'OPTIMALITY_CERTIFICATE_K{k}.json').write_text(json.dumps(cert,indent=2),encoding='utf-8')
    print(json.dumps({x:out[x] for x in ['status','k','states','comparisons','assertions','runtime_seconds','optimal_cost_over_total_influence','root_optimal_actions']}))
if __name__=='__main__': main()
