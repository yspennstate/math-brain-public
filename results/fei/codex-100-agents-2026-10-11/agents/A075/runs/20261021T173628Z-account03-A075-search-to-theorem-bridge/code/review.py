"""Independent scalar and physical-packet reconstruction of A089 stage6."""
from bridge import *

SOURCE=Path(r'agents\A089\runs\20261021T154748Z-account03-A089-repair-specialist')

def intersect(a,b):ar.ck(max(a[0],b[0])<=min(a[1],b[1]))
def sourceiv(x):return Q(x[0],1<<192),Q(x[1],1<<192)

def main():
    start=time.perf_counter();n=6;SHAPES['pointnext']=(3,(0,))
    z={k:profile(n,k) for k in SHAPES}
    # The packet calculation uses A+gB directly, not composition C or biased-pivot identities.
    for k in z:
        H,I,masses=packets(n,SHAPES[k]);directS=ar.add({2:4*I},H,Q(-1))
        ar.ck(masses==z[k]['masses'])
        ar.ck(I==z[k]['I']);difference=iv(ar.add(directS,z[k]['S'],Q(-1)))
        ar.ck(difference[0]<=0<=difference[1])
    e1=excess(z['r'],z['a'],z['z']);e2=excess(z['a'],z['b'],z['c'])
    T2=iv(ar.add(ar.scale(e1,Q(2)),e2));B2=iv(ar.scale(ar.add(z['b']['U'],z['c']['U']),Q(1,2)))
    theta=idiv(T2,B2);rows=[]
    for b,parent,nonconst,coords in [(0,'b','d',[3,4,5]),(1,'c','pointnext',[1,3,4,5])]:
        D=imul(theta,iv(z[parent]['U']));e=iv(excess(z[parent],z[nonconst],z['z']));T=iadd(D,e)
        child=[z[nonconst],z['z']];V=[];WW=[]
        for c in child:
            M=iv(c['M']);U=iv(c['U']);cost=(max(Q(0),-M[1]),max(Q(0),-M[0]))
            V.append(isub(U,cost));WW.append((max(Q(0),M[0]),max(Q(0),M[1])))
            ar.ck(V[-1][0]>=0)
        B=mean(*V);Wm=mean(*WW);gap=isub(T,B);tau=(max(Q(0),gap[0]),max(Q(0),gap[1]))
        ar.ck(D[0]>0 and e[0]>0 and T[0]>0)
        ar.ck(isub(Wm,tau)[0]>0)
        if b==0:
            ratio=idiv(tau,Wm);ar.ck(ratio[0]>Q(1,4) and ratio[1]<Q(13,50))
        else:ar.ck(gap[1]<0);ratio=icon(0)
        for i in coords:
            rows.append({'second_bit':b,'original_coordinate':i,'D':D,'e':e,'T':T,'B':B,'tau':tau,'W':Wm,'ratio':ratio})
    source=json.loads((SOURCE/'out/REPAIRED_CASES.json').read_text(encoding='utf-8'))
    ar.ck(len(source)==len(rows)==7)
    mapping={'D':'incoming_debit','e':'new_full_K4_excess','T':'old_plus_new_T','B':'corrected_mean_selected_B','tau':'minimal_transfer_tau','W':'mean_other_W','ratio':'fraction_other_spent'}
    for row in rows:
        src=next(x for x in source if x['second_bit']==row['second_bit'] and x['third_original_coordinate']==row['original_coordinate'])
        for k,v in mapping.items():intersect(row[k],sourceiv(src[v]))
    # Allocation minimum and edge cases by exact rational arithmetic, including all zero/equality branches.
    scalar=0
    for v0 in range(4):
      for v1 in range(4):
       for w0 in range(4):
        for w1 in range(4):
         B=Q(v0+v1,2);Wm=Q(w0+w1,2)
         for ti in range(int(2*(B+Wm))+1):
          T=Q(ti,2);s=min(T,B);tau=max(Q(0),T-B)
          xs=[s*x/B if B else Q(0) for x in [v0,v1]]
          ys=[tau*x/Wm if Wm else Q(0) for x in [w0,w1]]
          ar.ck(sum(xs+ys)/2==T);ar.ck(all(0<=x<=v for x,v in zip(xs,[v0,v1])))
          ar.ck(all(0<=y<=w for y,w in zip(ys,[w0,w1])));ar.ck(tau==T-s)
          scalar+=1
    out={'source_claim':'A089-CORRECTED-CAPACITY-SIBLING-TRANSFER@1','source_statement_sha256':'11eca17170a87b2b8f7be097866d6a7ec7bd52ecc2cbc345808984c4e06e07fe',
      'verdict':'HOLDS_UNCHANGED_SCOPE','independent_agent':'A075','source_code_executed':False,'physical_cases':7,'packet_profiles':len(z),'scalar_boundary_cases':scalar,
      'checks':ar.checks,'seconds':time.perf_counter()-start,
      'summary':[{'b':x['second_bit'],'i':x['original_coordinate'],'fraction':[float(t) for t in x['ratio']]} for x in rows],
      'scope':'Generic allocation proof and seven fixed third queries only; no arbitrary-core hereditary eligibility.'}
    (ROOT/'out/REVIEW_A089.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    ar.ck(out['seconds']<55);print(json.dumps(out))

if __name__=='__main__':main()
