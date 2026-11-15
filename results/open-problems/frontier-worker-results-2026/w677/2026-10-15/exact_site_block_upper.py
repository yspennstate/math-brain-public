"""Exact finite-site block episodes for the ordinary frog model.

All probabilities and candidate certificates use Fraction. Floats only search
for potential weights; every accepted certificate is rechecked rationally.
This script does not turn failure of that search into an impossibility claim.
"""
from __future__ import annotations
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from functools import lru_cache
import argparse,ctypes,hashlib,json,math,shutil,sys,time

if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(1000000)

def dump(path,obj):
    part=path.with_suffix(path.suffix+'.part')
    part.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8');part.replace(path)

def solve(matrix,rhs):
    n=len(rhs);a=[list(row)+[rhs[i]] for i,row in enumerate(matrix)]
    for col in range(n):
        pivot=next(i for i in range(col,n) if a[i][col])
        a[col],a[pivot]=a[pivot],a[col]
        scale=a[col][col];a[col]=[x/scale for x in a[col]]
        for row in range(n):
            if row!=col and a[row][col]:
                scale=a[row][col];a[row]=[x-scale*y for x,y in zip(a[row],a[col])]
    result=[row[-1] for row in a]
    assert all(sum(x*y for x,y in zip(row,result))==b for row,b in zip(matrix,rhs))
    return result

class Episode:
    def __init__(self,d,expanded,root_only,global_root):
        self.d=d;self.global_root=global_root
        self.nodes=[()]
        if not root_only:
            self.nodes += [(i,) for i in range(d)]
            self.nodes += [(i,j) for i in range(expanded) for j in range(d)]
        assert len(self.nodes)<=13,'This prototype is sized for at most 13 sites'
        self.index={v:i for i,v in enumerate(self.nodes)};self.n=len(self.nodes)
        self.edges=[[] for _ in self.nodes];self.transition=[[F(0) for _ in self.nodes] for _ in self.nodes]
        self.down_class={};self.representative={};self.exit={}
        for i,v in enumerate(self.nodes):
            cls='root' if not v else ('shallow' if len(v)==1 else 'deep')
            missing=[v+(j,) for j in range(d) if v+(j,) not in self.index]
            if missing:self.down_class[i]=cls;self.representative.setdefault(cls,i)
        self.classes=list(self.representative)
        self.depth={c:len(self.nodes[i]) for c,i in self.representative.items()}
        self.exit={'up':[F(0) for _ in self.nodes],**{c:[F(0) for _ in self.nodes] for c in self.classes}}
        for i,v in enumerate(self.nodes):
            denominator=d if global_root and i==0 else d+1
            if i==0:
                if not global_root:self.exit['up'][i]=F(1,denominator)
            else:
                parent=self.index[v[:-1]];self.edges[i].append(parent);self.transition[i][parent]=F(1,denominator)
            missing=0
            for j in range(d):
                child=v+(j,)
                if child in self.index:
                    child_id=self.index[child];self.edges[i].append(child_id);self.transition[i][child_id]=F(1,denominator)
                else:missing+=1
            if missing:self.exit[self.down_class[i]][i]=F(missing,denominator)
            assert sum(self.transition[i])+sum(column[i] for column in self.exit.values())==1
        self.g_cache={};self.hits={}
        full=[[F(int(i==j))-self.transition[i][j] for j in range(self.n)] for i in range(self.n)]
        for label,rhs in self.exit.items():self.hits[label]=solve(full,rhs)
        assert all(sum(column[i] for column in self.hits.values())==1 for i in range(self.n))

    def g(self,allowed):
        if allowed in self.g_cache:return self.g_cache[allowed]
        ids=[i for i in range(self.n) if allowed>>i&1]
        matrix=[[F(int(i==j))-self.transition[i][j] for j in ids] for i in ids]
        rhs=[sum(column[i] for column in self.exit.values()) for i in ids]
        solution=solve(matrix,rhs);out=[F(0) for _ in self.nodes]
        for i,x in zip(ids,solution):assert 0<=x<=1;out[i]=x
        self.g_cache[allowed]=out
        return out

    def warm_path(self,seed):
        v=self.nodes[seed]
        return {self.index[v[:j]] for j in range(len(v)+1)}

    def connected(self,allowed,seed):
        if not (allowed>>seed&1):return False
        seen={seed};pending=[seed]
        while pending:
            for v in self.edges[pending.pop()]:
                if allowed>>v&1 and v not in seen:seen.add(v);pending.append(v)
        return len(seen)==allowed.bit_count()

    def response(self,seed,warm,path,deadline):
        cold=[i for i in range(self.n) if i not in warm]
        warm_mask=sum(1<<i for i in warm)
        def global_mask(mask):return warm_mask+sum(1<<v for j,v in enumerate(cold) if mask>>j&1)
        valid=[mask for mask in range(1<<len(cold)) if self.connected(global_mask(mask),seed)]
        assert valid,'Episode scope cannot be empty'
        cache_path=path.with_suffix('.checkpoint.json')
        q={}
        if cache_path.exists():
            saved=json.loads(cache_path.read_text(encoding='utf-8'))
            assert saved['seed']==seed and saved['warm']==sorted(warm)
            q={int(k):F(v) for k,v in saved['q'].items()}
            assert set(q)<=set(valid)
        def save():dump(cache_path,{'seed':seed,'warm':sorted(warm),'q':{str(k):str(v) for k,v in q.items()},'valid_states':len(valid)})
        bit_total=sum(x.numerator.bit_length()+x.denominator.bit_length() for x in q.values())
        last=time.monotonic()
        for number,mask in enumerate(valid):
            if mask in q:continue
            if time.monotonic()>=deadline:save();return None
            g=self.g(global_mask(mask));products={0:F(1)}
            sub=mask;subs=[0]
            while sub:subs.append(sub);sub=(sub-1)&mask
            for sub in sorted(subs[1:]):
                bit=sub&-sub;j=bit.bit_length()-1
                products[sub]=products[sub^bit]*g[cold[j]]
            value=g[seed]*products[mask]
            for smaller in subs:
                if smaller!=mask and smaller in q:value-=q[smaller]*products[mask^smaller]
            assert value>=0,('negative closure mass',mask)
            q[mask]=value;bit_total+=value.numerator.bit_length()+value.denominator.bit_length()
            assert bit_total<128*1024**2*8,'Rational storage guard at 128 MiB of integer bits'
            if number%64==0 or time.monotonic()-last>=10:save();last=time.monotonic()
        assert len(q)==len(valid) and sum(q.values())==1
        activated={v:sum(prob for mask,prob in q.items() if mask>>j&1) for j,v in enumerate(cold)}
        means={label:column[seed]+sum(activated[v]*column[v] for v in cold) for label,column in self.hits.items()}
        assert sum(means.values())==1+sum(activated.values())<=len(cold)+1
        result={'seed':seed,'warm':sorted(warm),'states':len(valid),'cold_sites':len(cold),
                'activation':{str(v):str(p) for v,p in activated.items()},
                'exit_means':{label:str(p) for label,p in means.items()},
                'max_fraction_bits':max(x.numerator.bit_length()+x.denominator.bit_length() for x in q.values()),
                'integer_bits_total':bit_total,'exact_normalization':True,'linear_residuals_verified':True}
        save();dump(path,result);return result

def star_direct(d,global_root,initial_m,initial_pending):
    p=F(1,d+1);q=F(1,d if global_root else d+1)
    extra=initial_pending-initial_m
    values={}
    for m in range(d,initial_m-1,-1):
        values[m,0]=F(0)
        for c in range(1,max(0,extra+m)+1):
            if m==d:values[m,c]=F(0);continue
            new=1+(1-p)**2*values[m+1,c-1]+2*p*(1-p)*values[m+1,c]+p*p*values[m+1,c+1]
            up=F(0) if global_root else p
            values[m,c]=((up+m*q*(1-p))*values[m,c-1]+(d-m)*q*new)/(1-m*q*p)
    return values[initial_m,initial_pending]

def potential_rows(episodes,classes,depth,z):
    rows=[]
    def row(label,input_type,reply,h,attachment=None):
        coeff={('T:'+c):F(reply['exit_means'][c])*z**(depth[c]+1-h) for c in classes}
        if attachment is not None:coeff['B:'+attachment]=F(reply['exit_means']['up'])*z**(-1-h)
        rows.append({'label':label,'input':input_type,'coefficients':coeff})
    for b in classes:row('bulk top attached '+b,'T:'+b,episodes['bulk_top'],0,b)
    for c in classes:
        for b in classes:row('bulk bottom '+c+' attached '+b,'B:'+c,episodes['bulk_bottom_'+c],depth[c],b)
        row('global root bottom '+c,'B:'+c,episodes['root_bottom_'+c],depth[c])
    return rows

def verify_weights(rows,weights):
    ratios=[sum(coef*weights[t] for t,coef in row['coefficients'].items())/weights[row['input']] for row in rows]
    return max(ratios),ratios

def search_weights(episodes,classes,depth):
    types=['T:'+c for c in classes]+['B:'+c for c in classes]
    best=math.inf;best_z=None
    for z in [F(2,7)]+[F(i,100) for i in range(10,91)]:
        rows=potential_rows(episodes,classes,depth,z);w={t:1.0 for t in types}
        for iteration in range(600):
            f={t:0.0 for t in types}
            for row in rows:f[row['input']]=max(f[row['input']],sum(float(c)*w[t] for t,c in row['coefficients'].items()))
            ratio=max(f[t]/w[t] for t in types)
            if ratio<best:best=ratio;best_z=z
            if ratio<1-1e-8:
                exact={t:F(str(v)).limit_denominator(10**9) for t,v in w.items()}
                alpha,ratios=verify_weights(rows,exact)
                if alpha<1:return {'found':True,'z':str(z),'weights':{t:str(v) for t,v in exact.items()},
                    'alpha':str(alpha),'rows':[{'label':r['label'],'input':r['input'],'coefficients':{t:str(v) for t,v in r['coefficients'].items()},'ratio':str(v)} for r,v in zip(rows,ratios)],'arithmetic':'exact Fraction verification; floats only selected candidates'}
            w={t:1+f[t] for t in types}
            if max(w.values())>1e8:break
    return {'found':False,'status':'NO CERTIFICATE FOUND IN THIS CANDIDATE SEARCH',
            'best_float_candidate_ratio':best,'best_float_candidate_z':str(best_z),
            'scope':'Not a lower spectral bound or an impossibility result.'}

def resource_gate():
    class Memory(ctypes.Structure):
        _fields_=[('length',ctypes.c_ulong),('load',ctypes.c_ulong)]+[(name,ctypes.c_ulonglong) for name in ['total','available','total_page','available_page','total_virtual','available_virtual','extended']]
    status=Memory();status.length=ctypes.sizeof(status)
    assert ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status))
    assert status.available>=2*1024**3,'Wait for 2 GiB free memory'
    assert shutil.disk_usage('.').free>=1024**3,'Wait for 1 GiB free disk'
    return {'free_memory':status.available,'free_disk':shutil.disk_usage('.').free,'maximum_sites':13,'maximum_cold_subsets':8192,'integer_storage_guard_bytes':128*1024**2,'cores':1}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--d',type=int,default=4);parser.add_argument('--expanded',type=int,default=1)
    parser.add_argument('--root-only',action='store_true');parser.add_argument('--seconds',type=int,default=240)
    args=parser.parse_args();assert args.d>=2 and 0<=args.expanded<=args.d and 1<=args.seconds<=300
    resources=resource_gate();start=time.monotonic();deadline=start+args.seconds
    digest=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    folder=Path('computations')/f'c33_site_d{args.d}_k{args.expanded}_root{int(args.root_only)}_src{digest[:10]}'
    folder.mkdir(parents=True,exist_ok=True);dump(folder/'resource_plan.json',resources)
    bulk=Episode(args.d,args.expanded,args.root_only,False);root=Episode(args.d,args.expanded,args.root_only,True)
    jobs=[('bulk_top',bulk,0,set())]
    for label,episode in [('bulk',bulk),('root',root)]:
        for c,seed in episode.representative.items():jobs.append((label+'_bottom_'+c,episode,seed,episode.warm_path(seed)))
    results={}
    for name,episode,seed,warm in jobs:
        target=folder/(name+'.json')
        result=json.loads(target.read_text(encoding='utf-8')) if target.exists() else episode.response(seed,warm,target,deadline)
        if result is None:print(json.dumps({'status':'CHECKPOINTED','folder':str(folder),'next':name}),flush=True);return
        results[name]=result
        print(json.dumps({'complete_episode':name,'states':result['states'],'sites':episode.n}),flush=True)
    controls=[]
    if args.root_only:
        p=F(1,args.d+1)
        assert F(results['bulk_top']['exit_means']['up'])==2*p
        assert F(results['bulk_bottom_root']['exit_means']['up'])==p
        assert F(results['root_bottom_root']['exit_means']['root'])==1
        controls.append('one-site exact cold/warm/global-root values')
    elif args.expanded==0:
        p=F(1,args.d+1);q=p;a=p/(1-args.d*q*p);b=p*a
        new=star_direct(args.d,False,0,2)
        assert F(results['bulk_top']['exit_means']['up'])==2*a+new*b
        new=p*star_direct(args.d,False,1,1)
        assert F(results['bulk_bottom_shallow']['exit_means']['up'])==(1+new)*b
        new=p*star_direct(args.d,True,1,1)
        assert F(results['root_bottom_shallow']['exit_means']['shallow'])==1+new
        controls.append('independent star Markov queue agrees with all three range-closure calculations')
    certificate=search_weights(results,bulk.classes,bulk.depth)
    if args.root_only and args.d==6:
        rows=potential_rows(results,bulk.classes,bulk.depth,F(2,7));alpha,_=verify_weights(rows,{'T:root':F(2),'B:root':F(1)})
        assert alpha==F(97,98);controls.append('known T6 control: exact alpha=97/98 including global root')
    output={'at':datetime.now(timezone.utc).isoformat(),'source_sha256':digest,'parameters':vars(args),'sites':bulk.n,
            'episodes':results,'classes':bulk.classes,'depths':bulk.depth,'certificate':certificate,
            'controls':controls,'elapsed_seconds':time.monotonic()-start,'status':'exact episode coefficients; full upper coupling unaudited'}
    dump(folder/'final.json',output)
    with Path('C33_RUN_LOG.jsonl').open('a',encoding='utf-8') as log:log.write(json.dumps({'at':output['at'],'folder':str(folder),'sites':bulk.n,'elapsed_seconds':output['elapsed_seconds'],'certificate_found':certificate['found'],'source_sha256':digest})+'\n')
    print(json.dumps({'folder':str(folder),'sites':bulk.n,'certificate':certificate,'controls':controls}),flush=True)

if __name__=='__main__':main()
