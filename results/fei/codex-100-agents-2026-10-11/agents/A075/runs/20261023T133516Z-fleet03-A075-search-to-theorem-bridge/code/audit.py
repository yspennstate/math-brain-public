from cancel import *
import cancel as engine
save('AUDIT_SPEC.json',{'version':'A075-row-audit-v1','family':'one actual4-bit core: +1 on querybit0 branch, on querybit1 branch negative at000,001,010; saved1024 circuits and7bit witness','domain':'one fixed4bit singleton-row control; exact replay of all3072 saved query identities;3 altered-artifact controls','case_count':{'new_core':1,'saved_circuits':1024,'saved_rows':3072},'symmetry':'none','arithmetic':'integer characters/physical edges; exact prime-log cancellation and integer-power sign','memory_estimate_mb':100,'maximum_runtime_seconds':55,'automatic_dimension_increase':False})
g=tuple(-1 if x>=8 and (x&7) in {0,1,2} else 1 for x in range(16));H,W,ds=stats(g)
mu=F(W[0],16);t=F(W[8],16);d=ds[3];ck((mu,t,d)==(F(5,8),F(3,8),F(3,8)))
L=row(mu,t);gap=add(L,{2:2*d},F(-1));ck(cmp(gap,{})>0);ck(2**74>5**25*3**9)
ck(gap=={2:F(37,16),3:F(-9,32),5:F(-25,32)})
count=0;rows=0;controls=0;has_special=False
for k in range(16):
 data=json.loads((ROOT/'out'/('CIRCUITS_'+str(k).zfill(2)+'.json')).read_text(encoding='utf-8'));ck(len(data)==64)
 for c in data:
  count+=1
  for z in c['queries']:
   rows+=1;dr={int(k):F(v) for k,v in z['C_drift'].items()};sp={int(k):F(v) for k,v in z['full_special_rows'].items()}
   cn=c['label'][z['core']+1];Ncore=4 if z['core']==0 else 2;gt=tuple(-1 if cn>>x&1 else 1 for x in range(Ncore));di=stats(gt)[2][z['coordinate']]
   vac={int(k):F(v) for k,v in z['exceptional_inner_row'].items()}
   q=F(z['physical_influence'])/di if di else F(0)
   ck(dr==add(scale(vac,q),sp,F(-1)))
   ck(cmp(dr,{2:3*F(z['physical_influence'])})<=0)
   if dr and controls==0:
    ck(add(dr,{2:F(1,1<<32)})!=dr);controls+=1
   if sp:has_special=True
ck(count==1024 and rows==3072 and has_special)
w=json.loads((ROOT/'out/WITNESS.json').read_text(encoding='utf-8'));z=w['queries'][0];dr={int(k):F(v) for k,v in z['C_drift'].items()}
expected={2:F(-37,16),3:F(-567,512),5:F(-25,1024),7:F(3087,2048)};ck(dr==expected)
ck(add(expected,{2:F(1,1<<32)})!=dr);controls+=1
ck(F(z['physical_influence'])==F(9,64));ck(F(z['physical_influence'])+F(1,1<<32)!=F(9,64));controls+=1
for pin in json.loads((ROOT/'out/SOURCE_PINS.json').read_text(encoding='utf-8')):ck(hashlib.sha256(Path(pin['path']).read_bytes()).hexdigest()==pin['sha256'])
result={'status':'PASS','saved_circuits':count,'saved_query_rows':rows,'positive_controls_rejected':controls,'actual_four_bit_core':{'mean':str(mu),'singleton':str(t),'influence':str(d),'L':pack(L),'L_minus_2d':pack(gap),'integer_certificate':'2^74 >5^25*3^9','scope':'2d is FALSE for the exceptional-row bound alone; no claim refuting a2*Inf bound on the full signed composition drift'},'checks':engine.checks,'seconds':time.perf_counter()-start,'source_pins_unchanged':True}
ck(time.perf_counter()-start<55);result['checks']=engine.checks;save('AUDIT.json',result);print(json.dumps({k:v for k,v in result.items() if k!='actual_four_bit_core'}))
