import sys,math,json,time,importlib.util
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]
old=R.parent/'20261014T020611Z-fleet05-A072-exact-walsh-engine/code/verify.py'
sp=importlib.util.spec_from_file_location('own_math',old);e=importlib.util.module_from_spec(sp);sp.loader.exec_module(e)
B=e.B;K=F(9,2);G=tuple(-1 if x in (0,1,2) else 1 for x in range(64));J=e.J
COUNT=0
def ck(x):
    global COUNT
    if not x:raise AssertionError('predicate '+str(COUNT+1))
    COUNT+=1
def dump(name,x):(R/'out'/name).write_text(json.dumps(x,indent=2,default=str)+'\n',encoding='utf-8')
def add(*xs):return tuple(sum(x[k] for x in xs) for k in (0,1))
def scale(x,c):return (x[0]*c,x[1]*c) if c>=0 else (x[1]*c,x[0]*c)
def sub(x,y):return x[0]-y[1],x[1]-y[0]
def div(x,y):
    ck(y[0]>0)
    z=[a/b for a in x for b in y];return min(z),max(z)
def prod(x,y):
    z=[a*b for a in x for b in y];return min(z),max(z)
def const(c):return F(c),F(c)
def positive(x):ck(x[0]>0)
def overlap(x):ck(x[0]<=0<=x[1])
def h2(v):return e.ent((1-v,v))
@lru_cache(None)
def core(table):
    c=B.uniform_certificate(table);c['p']=F(sum(z<0 for z in table),len(table));c['H']=e.ent(c['spectrum']);c['I']=sum(c['influences'])
    c['S4']=sub(const(4*c['I']),c['H']);c['SK']=sub(const(K*c['I']),c['H'])
    return c
@lru_cache(None)
def outer(ps):
    W=B.fwht(J);m=[1-2*p for p in ps];v=[4*p*(1-p) for p in ps]
    # Sign-centered polynomial coefficients, independently of bit interpolation.
    coeff=[sum((F(W[U],64)*math.prod(m[l] for l in range(6) if (U^T)>>l&1) for U in range(64) if U&T==T),F(0)) for T in range(64)]
    sq=[coeff[T]**2*math.prod(v[l] for l in range(6) if T>>l&1) for T in range(64)]
    ck(sum(sq)==1)
    for x in range(64):
        ck(sum((coeff[T]*math.prod(F(1-2*((x>>l)&1))-m[l] for l in range(6) if T>>l&1) for T in range(64)),F(0))==J[x])
    qs=[]
    for j in range(6):
        q=sum((math.prod(ps[l] if x>>l&1 else 1-ps[l] for l in range(6) if l!=j) for x in range(64) if not x>>j&1 and J[x]!=J[x|(1<<j)]),F(0))
        ck(v[j]*q==sum((sq[T] for T in range(64) if T>>j&1),F(0)));qs.append(q)
    C=sub(e.ent(sq),add(*(scale(h2(z),q) for z,q in zip(v,qs))))
    return {'p':ps,'q':qs,'C':C,'spectrum':sq,'sign_centered_coefficients':coeff}
def restricted(tag):
    free=[j for j,z in enumerate(tag) if z=='*']
    fixed=sum((z=='1')<<j for j,z in enumerate(tag))
    return tuple(G[fixed|sum(((x>>k)&1)<<j for k,j in enumerate(free))] for x in range(1<<len(free)))
@lru_cache(None)
def state(tag):
    g=restricted(tag);c=core(g);base=core(G);ps=(c['p'],)+(base['p'],)*5;o=outer(ps);q=o['q'];C=o['C']
    H=add(scale(c['H'],q[0]),scale(base['H'],sum(q[1:])),C);I=q[0]*c['I']+sum(q[1:])*base['I'];S=sub(const(K*I),H)
    A=scale(c['SK'],q[0]);M=sub(scale(base['SK'],sum(q[1:])),C)
    T=scale(M,-1) if M[1]<0 else const(0)
    if M[0]<=0<=M[1]:ck(M==(0,0))
    U=sub(A,T);O=M if M[0]>0 else const(0)
    positive(S);positive(U) if U!=(0,0) else None
    overlap(sub(S,add(U,O)))
    x={'tag':tag,'core_table':g,'core':c,'outer':o,'H':H,'I':I,'S':S,'A':A,'M':M,'transfer_selected_to_outer':T,'U':U,'O':O}
    dump('state_'+tag.replace('*','x')+'.json',x)
    return x
def kids(tag,j):return [tag[:j]+str(b)+tag[j+1:] for b in (0,1)]
def edge(tag,j):
    parent=state(tag);ch=[state(t) for t in kids(tag,j)];q=parent['outer']['q'][0]
    idx=[l for l,x in enumerate(tag) if x=='*'].index(j);d=parent['core']['influences'][idx]
    ck(parent['I']-sum(x['I'] for x in ch)/2==q*d)
    for l in range(6):ck(sum(x['outer']['q'][l] for x in ch)/2==parent['outer']['q'][l])
    # Independent physical edge average: selected inner fibers times other5 outer assignments.
    g=parent['core_table'];n=len(g).bit_length()-1;prob=core(G)['p'];direct=F(0)
    for x in range(len(g)):
        if x>>idx&1:continue
        for z in range(32):
            if J[(z<<1)|(g[x]<0)]!=J[(z<<1)|(g[x|(1<<idx)]<0)]:
                direct+=prob**z.bit_count()*(1-prob)**(5-z.bit_count())*F(2,len(g))
    ck(direct==q*d)
    DH=sub(parent['H'],scale(add(*(x['H'] for x in ch)),F(1,2)))
    ex=sub(DH,const(K*q*d));ex4=sub(DH,const(4*q*d))
    if d==0:
        # Direct edges certify the coordinate is dummy; its exact entropy loss is zero.
        overlap(DH);DH=ex=ex4=const(0)
    overlap(sub(add(parent['S'],ex),scale(add(*(x['S'] for x in ch)),F(1,2))))
    return {'parent':tag,'coordinate':j,'children':[x['tag'] for x in ch],'physical_influence':direct,'excess_K':ex,'excess_4':ex4}
def full_small(mask):
    g=tuple(1-2*((mask>>x)&1) for x in range(4));gc=core(g)
    tables=[(g,)*6]
    for bit in (0,1):tables.append((tuple(g[bit|(x<<1)] for x in range(2)),)+(g,)*5)
    for index,cores in enumerate(tables):
        cs=[core(x) for x in cores];ps=tuple(c['p'] for c in cs);o=outer(ps)
        ns=[len(g).bit_length()-1 for g in cores];offset=[sum(ns[:j]) for j in range(6)];dim=sum(ns)
        table=tuple(J[sum((cores[j][(x>>offset[j])&((1<<ns[j])-1)]<0)<<j for j in range(6))] for x in range(1<<dim))
        W,inf,edges=e.fast(table)
        for s,w in enumerate(W):
            T=0;mult=F(1)
            for j in range(6):
                part=(s>>offset[j])&((1<<ns[j])-1)
                if part:T|=1<<j;mult*=F(cs[j]['walsh'][part],len(cores[j]))
            ck(F(w,1<<dim)==o['sign_centered_coefficients'][T]*mult)
        ck(inf==[o['q'][j]*d for j in range(6) for d in cs[j]['influences']])
        dump('small_'+str(mask)+'_'+str(index)+'.json',{'mask':mask,'state':index,'dimension':dim,'walsh':W,'edges':edges,'influences':inf,'coefficient_matches':len(W)})
def run(pilot):
    start=time.perf_counter();cap=55 if pilot else 120
    B.uniform_certificate(J);core(G)
    order=[2,0,1,3,4,5];tags=['******'];edges=[];tag=tags[0]
    for j in order:
        row=edge(tag,j);edges.append(row);tags.extend(row['children']);tag=row['children'][0]
    ck(len(set(tags))==13)
    # Reconstruct A089's SAME K4 prefix bookings, never zero them at continuation.
    first,second=edges[:2]
    e1=first['excess_4'];e2=second['excess_4'];positive(e1);positive(e2)
    first_nonconstant=state(first['children'][0]);positive(first_nonconstant['core']['S4'])
    old_conditional=scale(e1,2)
    grand=[state(t) for t in second['children']]
    selected4=[scale(x['core']['S4'],x['outer']['q'][0]) for x in grand]
    B4=scale(add(*selected4),F(1,2));positive(B4)
    old_labels={t:{'first_query_K4':prod(div(old_conditional,B4),selected4[b]),'second_query_K4':prod(div(e2,B4),selected4[b])} for b,t in enumerate(second['children'])}
    for t in first['children']+second['children']:
        s=state(t);M4=sub(scale(core(G)['S4'],sum(s['outer']['q'][1:])),s['outer']['C']);positive(M4)
    positive(sub(scale(B4,F(3,5)),add(old_conditional,e2)))
    for t,labels in old_labels.items():positive(sub(state(t)['U'],add(*labels.values())))
    ck(state(first['children'][1])['core']['I']==0)
    # True reach-weighted terminal list, including all stopped siblings.
    leaves=[{'tag':first['children'][1],'reach':F(1,2),'labels':{}}, {'tag':second['children'][1],'reach':F(1,4),'labels':old_labels[second['children'][1]]}]
    labels=old_labels[second['children'][0]];path=[]
    for depth,row in enumerate(edges[2:],start=2):
        p=state(row['parent']);ch=[state(t) for t in row['children']];old=add(*labels.values());positive(sub(p['S'],old))
        Bfull=scale(add(*(x['S'] for x in ch)),F(1,2));positive(Bfull)
        mean_debit=add(old,row['excess_K']);positive(sub(Bfull,mean_debit))
        expanded=dict(labels);expanded['query_'+str(depth+1)+'_K9over2']=row['excess_K']
        newlabels=[];owners=[]
        for c in ch:
            ratio=div(c['S'],Bfull);ls={key:prod(value,ratio) for key,value in expanded.items()};total=add(*ls.values())
            remaining=sub(c['S'],total);positive(remaining)
            # Negative M is paid from selected A BEFORE splitting the carried booked liabilities.
            selected_debit=prod(div(c['U'],c['S']),total);other_debit=prod(div(c['O'],c['S']),total)
            positive(sub(c['U'],selected_debit)) if c['U']!=(0,0) else overlap(selected_debit)
            positive(sub(c['O'],other_debit)) if c['O']!=(0,0) else overlap(other_debit)
            newlabels.append(ls);owners.append({'tag':c['tag'],'reach':F(1,2**(depth+1)),'incoming_labels':ls,'net_debit':total,'selected_to_outer_transfer':c['transfer_selected_to_outer'],'selected_debit':selected_debit,'other_debit':other_debit,'remaining_full_owner':remaining,'U':c['U'],'O':c['O']})
        for key,value in expanded.items():overlap(sub(scale(add(*(x[key] for x in newlabels)),F(1,2)),value))
        path.append({'query':row,'parent_labels':labels,'conditional_mean_owner':Bfull,'conditional_net_debit':mean_debit,'children':owners})
        leaves.append({'tag':ch[1]['tag'],'reach':F(1,2**(depth+1)),'labels':newlabels[1]})
        labels=newlabels[0]
        ck(time.perf_counter()-start<cap)
    leaves.append({'tag':edges[-1]['children'][0],'reach':F(1,64),'labels':labels})
    ck(sum(x['reach'] for x in leaves)==1 and len(leaves)==7)
    for x in leaves:
        x['full_terminal_H']=state(x['tag'])['H'];x['full_terminal_I']=state(x['tag'])['I'];x['full_terminal_S']=state(x['tag'])['S'];x['remaining']=sub(x['full_terminal_S'],add(*x['labels'].values()) if x['labels'] else const(0));positive(x['remaining'])
    # The unchanged rate4 old bookings have a visible conservative cost at rate9/2.
    tax=(K-4)*(first['physical_influence']+second['physical_influence']/2)
    root_remaining=sub(state('******')['S'],const(tax));positive(root_remaining)
    terminal_remaining=add(*(scale(x['remaining'],x['reach']) for x in leaves));overlap(sub(terminal_remaining,root_remaining))
    target=state('00000*');ck(target['M'][1]<-F(1,10));positive(target['S']);positive(target['transfer_selected_to_outer'])
    target_record=next(c for row in path for c in row['children'] if c['tag']=='00000*');positive(target_record['remaining_full_owner'])
    positive(sub(target_record['remaining_full_owner'],const(F(12,25))))
    positive(sub(root_remaining,const(F(11,10))))
    ck(target['transfer_selected_to_outer'][0]>F(1,10) and target['transfer_selected_to_outer'][1]<F(11,100))
    dump('ledger.json',{'rate_K':K,'order':order,'prefix_rate4_excesses':[e1,e2],'old_conditional_debit_after_first':old_conditional,'old_labels_after_second':old_labels,'continuation':path,'complete_terminals':leaves,'conservative_prefix_tax':tax,'root_remaining_after_tax':root_remaining,'terminal_mean_remaining':terminal_remaining,'target_tag00000star':target_record,'target_other_owner_margin':target['M']})
    dump('edges.json',edges)
    for mask in ([1] if pilot else [1,7]):full_small(mask);ck(time.perf_counter()-start<cap)
    result={'passed':True,'assertions':COUNT,'states':13,'physical_queries':6,'terminals':7,'small_parents':1 if pilot else 2,'small_child_states':2 if pilot else 4,'exact_coefficient_matches':8192 if pilot else 16384,'small_coordinate_edge_counts':34 if pilot else 68,'runtime_seconds':time.perf_counter()-start,'target_margin_display':float(target['M'][1]),'target_transfer_display':float(target['transfer_selected_to_outer'][0]),'target_remaining_display':float(target_record['remaining_full_owner'][0]),'root_remaining_display':float(root_remaining[0])}
    dump('pilot.json' if pilot else 'validation.json',result);print(json.dumps(result))
if __name__=='__main__':run('--pilot' in sys.argv)
