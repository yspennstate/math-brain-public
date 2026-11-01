from pathlib import Path
import arithmetic as ar
from arithmetic import F,ck,spec,inf,res,marg,phase,rank,log2i,H,CE,add,sub,scale
import json,itertools,time,sys
R=Path(__file__).resolve().parents[1]
EPS=F(1,10**18)
mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'
fixtures=[(4,3,False)] if mode=='pilot' else ([(12,16,False)] if mode=='audit' else [(8,4,False),(8,4,True),(10,8,False),(10,8,True)])
policies=range(1) if mode in ['pilot','audit'] else range(6)
source_rows=[];frontiers=queries=0

def Ibit(t,i):return F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t))
def choose(labs,policy,hist,n):
 if policy==0:return min(labs)
 if policy==1:return max(labs)
 if policy==2:return n if n in labs else min(labs)
 if policy==3:return n if n in labs and len(hist)>=n//2 else min(x for x in labs if x!=n) if any(x!=n for x in labs) else n
 if policy==4:return (min if sum(hist)%2==0 else max)(labs)
 return sorted(labs,key=lambda x:((x*3+sum(hist))%(n+1),x))[0]

def node(t,bt,q,h,q1,labs,w,hist,live):return {'t':t,'bt':bt,'q':q,'h':h,'q1':q1,'labs':labs,'w':w,'hist':hist,'live':live}

for n,k,complete in fixtures:
 m=n//2;d=F(1,2**n)
 es=list(itertools.combinations(range(n),2)) if complete else [(i,i+1) for i in range(0,n,2)]
 ck(rank(n,es)==n)
 b0=phase(n,es)
 # Include arbitrary affine terms without changing the polar matrix.
 b0=tuple(v*(-1)**(((x&5).bit_count()+int(complete))%2) for x,v in enumerate(b0))
 b=b0+b0;pb=spec(b);Hb=H(pb);Ib=inf(b);ck(Ib==m)
 # Marks occupy separated but nontrivial physical cylinders.
 E=tuple((j*5)%(1<<n) for j in range(k));ck(len(set(E))==k)
 h=tuple(b0[x] if x in E else 0 for x in range(1<<n));qh=spec(h);ck(sum(qh)==k*d)
 c=list(b)
 for x in E:c[x]*=-1
 c=tuple(c);qc=spec(c);ck(tuple(qc[1<<n:])==qh)
 Ix=(Ib+inf(c))/2;Hg=H(spec(b+c));r4=sub((4*Ix,4*Ix),Hg)
 ck(Ix>=m-m*k*d+k*d/2);ck(r4[0]>=2*m-4*m*k*d+2*k*d-2)
 rootH=scale(add(Hb,H(qc)),F(1,2));rareRoot=scale(H(qh),F(1,2))
 rareUpper=scale(sub((2*n,2*n),log2i(k)),k*d/2)
 ck(rareRoot[1]<=rareUpper[1]+EPS)
 cceil=(k-1).bit_length();Lbound=F(cceil+2,2)
 for policy in policies:
  leaves=[node(c,b,qc,h,qh,list(range(n+1)),F(1,2),[],True)]
  raredata=(F(0),F(0));rarew=(F(0),F(0));retired=(F(0),F(0));occupation=F(0)
  for depth in range(n+2):
   htotal=scale(Hb,F(1,2));cetotal=htotal;itotal=Ib/2;liveC=(F(0),F(0))
   expectedDepth=F(0)
   for v in leaves:
    p=spec(v['t']);ck(sum(p)==1);ck(sum(v['q'])==1)
    hp=H(p);cp=CE(p,v['q']);htotal=add(htotal,scale(hp,v['w']));cetotal=add(cetotal,scale(cp,v['w']));itotal+=v['w']*inf(v['t']);expectedDepth+=v['w']*len(v['hist'])
    if v['live']:liveC=add(liveC,scale(CE(spec(v['h']),v['q1']),v['w']))
   balance=sub(rareRoot,add(add(raredata,rarew),add(retired,liveC)))
   ck(abs(balance[0])<EPS and abs(balance[1])<EPS)
   ck(add(raredata,rarew)[1]<=rareRoot[1]+EPS)
   ck(expectedDepth==occupation);ck(occupation<=Lbound)
   J=Ix-itotal;ck(J>=0)
   eh=sub(sub(rootH,htotal),(4*J,4*J));eq=sub(sub(rootH,cetotal),(4*J,4*J));kl=sub(cetotal,htotal)
   ck(kl[0]>=-EPS);ck(kl[1]<=occupation+EPS)
   diff=sub(eh,add(eq,kl));ck(abs(diff[0])<EPS and abs(diff[1])<EPS)
   cap=add((3*Lbound+F(1,12),3*Lbound+F(1,12)),rareUpper)
   ck(eh[1]<cap[1]);ck(eq[1]<2*Lbound+F(1,12)+rareUpper[1])
   # The old A067 rare data bound is reconstructed, not used as a new premise.
   oldrare=scale(log2i(2*k*k),F(n*k,2)*d);ck(raredata[1]<=oldrare[1]+EPS)
   if m>=5:
    bound=F(m,2)-F(25,12)-F(6*m-2,4*2**m)
    ck(r4[0]-eh[1]>bound);ck(bound>=F(19,96))
   if m>=6:
    oldbound=F(m,2)-F(25,12)-F(2*m*m+2*m-1,4*2**m)
    ck(r4[0]-eh[1]>oldbound);ck(oldbound>=F(455,768))
   frontiers+=1
   if depth==n+1:break
   new=[]
   for v in leaves:
    if not v['labs'] or v['t']==v['bt']:new.append(v);continue
    lab=choose(v['labs'],policy,v['hist'],n);ix=v['labs'].index(lab);qm=marg(v['q'],ix);labs=v['labs'][:ix]+v['labs'][ix+1:]
    pp=spec(v['t']);parentCE=CE(pp,v['q']);childCE=(F(0),F(0))
    if v['live'] and lab!=n:
     ph=spec(v['h']);qhm=marg(v['q1'],ix)
     c0=CE(spec(res(v['h'],ix,0)),qhm);c1=CE(spec(res(v['h'],ix,1)),qhm)
     rd=sub(CE(ph,v['q1']),scale(add(c0,c1),F(1,2)));ck(rd[0]>=-EPS)
     raredata=add(raredata,scale(rd,v['w']))
    if v['live'] and lab==n:
     ph=spec(v['h']);qsum=marg(v['q'],ix)
     rw=sub(CE(ph,v['q1']),CE(ph,qsum));ck(rw[0]>=-EPS)
     rarew=add(rarew,scale(rw,v['w']));retired=add(retired,scale(CE(ph,qsum),v['w']))
    for z in [0,1]:
     tt=res(v['t'],ix,z);bt=res(v['bt'],ix,z);childCE=add(childCE,scale(CE(spec(tt),qm),F(1,2)))
     if v['live'] and lab!=n:hh=res(v['h'],ix,z);qq=qhm
     else:hh=v['h'];qq=v['q1']
     new.append(node(tt,bt,qm,hh,qq,labs,v['w']/2,v['hist']+[z],v['live'] and lab!=n))
    fullDrop=sub(parentCE,childCE)
    if lab!=n:
     common=sub(fullDrop,rd) if v['live'] else fullDrop
     ck(common[1]<=2+EPS)
    else:
     common=sub(fullDrop,rw);ck(common[1]<F(1,6))
    occupation+=v['w'];queries+=1
   leaves=new
 source_rows.append({'n':n,'k':k,'graph':'complete' if complete else 'matching','I_X':str(Ix),'r4_lower':str(r4[0]),'rare_original_CE_upper':str(rareUpper[1])})
ck(F(5,2)-F(25,12)-F(28,128)==F(19,96));ck(F(6,2)-F(25,12)-F(34,256)==F(301,384))
result={'mode':mode,'assertions':ar.checks,'sources':len(source_rows),'policies_per_source':len(policies),'frontiers':frontiers,'local_queries':queries,'seconds':time.monotonic()-ar.start,'rows':source_rows,'status':'PASS: rare data+w+full residual original-sector conservation; all terminals/same reserve'}
(R/'out'/('CHECK_'+mode+'.json')).write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
