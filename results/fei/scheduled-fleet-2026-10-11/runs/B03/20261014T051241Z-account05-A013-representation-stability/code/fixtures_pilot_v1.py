from arithmetic import *
import arithmetic as ar
profiles=json.loads((RUN/'out/PILOT_RESULTS.json').read_text())['profiles']
parents=reference_cases=cover_cases=0
for profile in profiles:
 mask=profile['mask'];c=[1 if mask>>s&1 else -1 for s in range(8)];ag=fwht(c);pg=[a*a for a in ag]
 for e0 in range(16):
  for e1 in range(16):
   p=F(e0.bit_count(),4);q=F(e1.bit_count(),4);d=(p+q)/8;delta=(p*p+q*q)/8
   h=[c[x&7]*(-1 if ((x&7)==0 and (e0>>(x>>3))&1) or ((x&7)==1 and (e1>>(x>>3))&1) else 1) for x in range(32)]
   ah=fwht(h);ph=[a*a for a in ah]
   for t in range(8):check(ah[t]==ag[t]-(p*c[0]+q*c[1]*(-1 if t&1 else 1))/4)
   f=[c[x&7] if x<32 else h[x-32] for x in range(64)];af=fwht(f);pf=[a*a for a in af]
   for t in range(32):
    a=ag[t] if t<8 else F(0)
    check(af[t]==(a+ah[t])/2);check(af[t+32]==(a-ah[t])/2)
   check(influence(f,6)[5]==d);check(sum(pf[t+32] for t in range(8))==delta)
   check(sum(pf[t]+pf[t+32] for t in range(8,32))==2*(d-delta))
   qb=[pf[t]+pf[t+32] for t in range(32)];b=add(H(pf),H(qb),F(-1))
   nonneg(add(mul(lv(2),4*d),b,F(-1)))
   check(sum(influence(f,6))==sum(influence(c,3)+influence(h,5))/2+d)
   for rh in refs(ph):
    rhc=cal(ph,rh,set(range(8)));check(sum(rhc)==1)
    ref=[pf[t] if (t%32)<8 else rhc[t%32]/4 for t in range(64)]
    check(sum(ref)==1)
    cf=CE(pf,ref);ch=CE(ph,rhc);df=add(cf,H(pf),F(-1));dh=add(ch,H(ph),F(-1))
    check(df==mul(dh,F(1,2)))
    inc=add(H(pf),mul(add(H(pg),H(ph)),F(-1,2)))
    check(cf==add(mul(add(H(pg),ch),F(1,2)),inc))
    sector=[pf[t|(u<<5)] for t in range(8) for u in [0,1]]+[sum(ph[8:])/2]
    chain=H(sector);v=sum(ph[8:])
    if v:
     chain=add(chain,lv(2),v/2)
     chain=add(chain,CE([a/v for a in ph[8:]],[a/v for a in rhc[8:]]),v/2)
    check(cf==chain);reference_cases+=1
   if e0 in [0,1,3,15] and e1 in [0,1,3,15]:
    nc=sum(a==1 for a in c);ng=nc;nh=4*nc-c[0]*e0.bit_count()-c[1]*e1.bit_count();check(nh==sum(a==1 for a in h))
    gates=[]
    for s in range(8):
     if c[s]==1:gates.append({0:s&1,1:(s>>1)&1,2:s>>2,5:0})
    for x in range(32):
     if h[x]==1:gates.append({j:(x>>j)&1 for j in range(5)}|{5:1})
    check(len(gates)==ng+nh)
    for j in range(6):
     for v in [0,1]:
      retained=[{k:a for k,a in g.items() if k!=j} for g in gates if j not in g or g[j]==v]
      for x in range(64):
       if (x>>j)&1==v:
        check(any(all((x>>k)&1==a for k,a in g.items()) for g in retained)==(f[x]==1))
      for g in retained:
       pi=F(1,1<<len(g));odds=pi/len(retained);check(odds/(1+odds)==pi/(len(retained)+pi))
    cover_cases+=1
   parents+=1
res={'status':'PASS','actual_Boolean_parents':parents,'calibrated_reference_cases':reference_cases,'cover_parent_cases':cover_cases,'singleton_cover_restrictions':cover_cases*12,'exact_assertions':ar.checks,'elapsed_seconds':time.perf_counter()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(RUN/'out/FIXTURE_RESULTS.json').write_text(json.dumps(res,indent=2),encoding='utf-8');print(json.dumps(res))
