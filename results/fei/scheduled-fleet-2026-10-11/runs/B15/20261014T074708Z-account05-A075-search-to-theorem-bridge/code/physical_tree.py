from block_reveal import *
def actual(truth):
    N=len(truth);W=ar.fwht(truth);n=(N-1).bit_length()
    p=Q(sum(x==-1 for x in truth),N);hg=ar.entropy(W)
    ds=[]
    for i in range(n):
        d=Q(sum(truth[x]!=truth[x^(1<<i)] for x in range(N)),N)
        ar.ck(d==sum((Q(w*w,N*N) for T,w in enumerate(W) if T>>i&1),Q(0)))
        ds.append(d)
    return p,hg,sum(ds),ds
def child(t,i,b):
    return [t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(t)//2)]
def main():
    start=time.perf_counter();p,I,H,S=core(6);order=[2,0,1,3,4,5];nodes=[];totalI=Q(0);terminalH={};totalDelta={};endpoint=[Q(0),Q(0)]
    def walk(t,free,prefix,reach):
        nonlocal totalI,terminalH,totalDelta
        bias,hg,Ic,ds=actual(t);C,qs,_=outer([bias]+[p]*5)
        hf=ar.add(ar.scale(hg,qs[0]),H,sum(qs[1:]));hf=ar.add(hf,C)
        fullI=qs[0]*Ic+sum(qs[1:])*I
        Sf=ar.add({2:4*fullI},hf,Q(-1));Sc=ar.add({2:4*Ic},hg,Q(-1))
        M=ar.add(ar.scale(S,sum(qs[1:])),C,Q(-1))
        ar.ck(ar.add(ar.scale(Sc,qs[0]),M)==Sf)
        row={'prefix':prefix,'reach':str(reach),'bias':str(bias),'C':val(C),'H_full':val(hf),'I_full':str(fullI),'S4_full':val(Sf),'selected_bank':val(ar.scale(Sc,qs[0])),'other_bank_minus_C':val(M)};nodes.append(row)
        if not Ic:
            endpoint[int(bias)]+=reach;terminalH=ar.add(terminalH,hf,reach);row['terminal']=True
            ar.ck(bias in [0,1]);return hf
        orig=next(i for i in order if i in free);i=free.index(orig);nextfree=[j for j in free if j!=orig]
        children=[walk(child(t,i,b),nextfree,prefix+[[orig,b]],reach/2) for b in [0,1]]
        delta=ar.add(ar.add(hf,children[0],Q(-1,2)),children[1],Q(-1,2))
        totalDelta=ar.add(totalDelta,delta,reach);totalI+=reach*qs[0]*ds[i]
        row.update({'query_original_coordinate':orig,'influence':str(qs[0]*ds[i]),'full_query_excess4':val(ar.add(delta,{2:4*qs[0]*ds[i]},Q(-1))),'terminal':False})
        return hf
    rootH=walk([-1 if x<3 else 1 for x in range(64)],list(range(6)),[],Q(1))
    ar.ck(endpoint==[1-p,p]);ar.ck(totalI==Q(json.loads((ROOT/'out/BLOCK_n6.json').read_text())['q0'])*I)
    ar.ck(ar.add(ar.add(rootH,terminalH,Q(-1)),totalDelta,Q(-1))=={})
    e=ar.add(totalDelta,{2:4*totalI},Q(-1));ar.ck(ar.forms(e)==json.loads((ROOT/'out/BLOCK_n6.json').read_text())['signed_full_block_K4_excess']['form'])
    neg=[x for x in nodes if Q(x['S4_full']['upper'])<0];first=min(neg,key=lambda x:len(x['prefix']))
    # Reconstruct the source two-query alternative and carried debit in log forms.
    rt=nodes[0];live=next(x for x in nodes if x['prefix']==[[2,0]])
    kids=[next(x for x in nodes if x['prefix']==[[2,0],[0,b]]) for b in [0,1]]
    def expr(x):return {int(k):Q(v) for k,v in x['form'].items()}
    e1=expr(rt['full_query_excess4']);e2=expr(live['full_query_excess4']);old=ar.scale(e1,2)
    B=ar.add(ar.scale(expr(kids[0]['selected_bank']),Q(1,2)),expr(kids[1]['selected_bank']),Q(1,2))
    total=ar.add(old,e2);ar.ck(ar.enclose(ar.add(ar.scale(B,Q(3,5)),total,Q(-1)))[0]>0)
    DC=ar.add(ar.add(expr(live['C']),expr(kids[0]['C']),Q(-1,2)),expr(kids[1]['C']),Q(-1,2))
    left=ar.add(B,total,Q(-1));right=ar.add(ar.add(expr(live['selected_bank']),old,Q(-1)),DC,Q(-1))
    ar.ck(left==right)
    out={'order':order,'nodes':nodes,'node_count':len(nodes),'first_negative_full_S4_prefix':first['prefix'],'first_negative_full_S4':first['S4_full'],'full_block_excess':val(e),'queried_total_influence':str(totalI),'terminal_selected_value_reaches':[str(x) for x in endpoint],'A089_second_query_reconstructed':{'old_debit':val(old),'new_excess':val(e2),'grandchild_bank':val(B),'old_plus_new_below_three_fifths':True,'no_renewal_identity_exact_log_form':True},'checks':ar.checks,'runtime_seconds':time.perf_counter()-start}
    assert out['runtime_seconds']<55
    (ROOT/'out/PHYSICAL_TREE.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['nodes','A089_second_query_reconstructed']}))
if __name__=='__main__':main()
