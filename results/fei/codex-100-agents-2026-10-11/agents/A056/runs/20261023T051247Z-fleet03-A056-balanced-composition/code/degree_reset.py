import shared as sh
from prior import *

N=0
def ck(ok):
 global N
 N+=1
 assert ok

def target(f):
 p=prob(f);v=1-p[0];ii=influence(f)
 return p if not v else (p[0],)+tuple(v*j.bit_count()*p[j]/ii for j in range(1,len(p)))

def phases():
 def bit(x,j):return 1 if (x>>j)&1 else -1
 def maj(x,ids):return 1 if sum(bit(x,j) for j in ids)>0 else -1
 return [tuple(fn(x) for x in range(32)) for fn in [
  lambda x:maj(x,range(5)),
  lambda x:maj(x,range(3))*bit(x,3)*bit(x,4),
  lambda x:(-1 if ((x&1) and (x&2))^bool((x&4) and (x&8)) else 1)*bit(x,4),
  lambda x:maj(x,[1,2,3]) if not x&1 else bit(x,3)*bit(x,4),
  lambda x:maj(x,[0,2,4])*bit(x,1)*bit(x,3),
  lambda x:maj(x,[0,1,2]) if not x&8 else maj(x,[0,1,4]),
  lambda x:(-1 if x in [0,1,2] else 1)*bit(x,3)*bit(x,4),
  lambda x:bit(x,0)*bit(x,1)*bit(x,2)*bit(x,3)*bit(x,4)
 ]]

def direct(f):
 n=len(f);return tuple(Q(sum(y*(-1 if (x&t).bit_count()%2 else 1) for x,y in enumerate(f)),n) for t in range(n))

def scalar(f,oversupported=False):
 p=prob(f);s=target(f);rr=phase_ref(f,False) if oversupported else p
 ck(sum(s)==1);ck(s[0]==p[0]);ck(all(not z or q>0 for z,q in zip(p,s)))
 debt=add(ce(p,s),entropy(f),-1);old=add(ce(p,rr),entropy(f),-1)
 delta=add(ce(p,s),ce(p,rr),-1)
 v=1-p[0];ii=influence(f)
 form={}
 if v:
  form=scale(log(ii/v),v)
  for j in range(1,len(p)):
   if p[j]:form=add(form,log(j.bit_count()),-p[j])
 ck(debt==form);ck(delta==add(debt,old,-1));ck(nonnegative(debt));ck(nonnegative(add({2:ii},delta,-1)))
 return {'bits':len(f).bit_length()-1,'table_sha256':hashlib.sha256(bytes(z==1 for z in f)).hexdigest(),'oversupported':oversupported,'I':str(ii),'fresh_KL':ser(debt),'signed_delta':ser(delta)}

def reset(s):
 ru,rv=target(s.u),target(s.v)
 c=State(s.u,s.v,ru,rv,s.na,s.nb,s.ea,s.eb,s.z)
 price={};positive={};changed=0;positive_sources=0
 for f,old,new,w,a in [(s.u,s.ru,ru,s.pi*s.a,s.a),(s.v,s.rv,rv,(1-s.pi)*s.b,s.b)]:
  d=add(ce(prob(f),new),ce(prob(f),old),-1)
  ck(nonnegative(add({2:influence(f)},d,-1)))
  e=scale(d,w*(1-a));price=add(price,e)
  if not nonnegative(scale(e,-1)):positive=add(positive,e);positive_sources+=1
  changed+=old!=new
 ck(price==add(c.CE,s.CE,-1));ck(nonnegative(add({2:s.core},positive,-1)))
 return c,price,positive,changed,positive_sources

def physical(states,kind):
 out=[];debit={};spent=Q(0);norm=[]
 for reach,s in states:
  if kind=='data':rec,cs=sh.shared(s,0);i=0;norm.append(rec['root_normalizers'])
  else:cs=transport(s,kind);i=s.index(kind)
  terminal=scale(add(cs[0].CE,cs[1].CE),Q(1,2))
  release=add(s.CE,terminal,-1);ck(nonnegative(release));debit=add(debit,release,reach)
  spent+=reach*edge_inf(s.f,i)
  ck(s.I==edge_inf(s.f,i)+(cs[0].I+cs[1].I)/2)
  for c in cs:out.append((reach/2,c))
 return out,debit,spent,norm

def history(u,v,na,nb,kind):
 s=State(u,v,prob(u),prob(v),na,nb);ck(nonnegative(add({2:3*influence(u)},s.cu,-1)));ck(nonnegative(add({2:3*influence(v)},s.cv,-1)))
 states=[(Q(1),s)];old_debit={};signed={};pos={};spent=Q(0);records=[];changed=positive_sources=0;bookings=[Q(0)]*3
 for step,op in enumerate(['data','reset',kind,'data','reset','data','reset','data']):
  if op!='reset':
   states,d,inf,norm=physical(states,op);old_debit=add(old_debit,d);spent+=inf
   records.append({'op':op,'states':len(states),'CE_release':ser(d),'spent_I':str(inf),'normalizers':norm})
  else:
   newstates=[];rd={};rp={};owner=Q(0);source_changes=source_positive=0;rr=len([r for r in records if r['op']=='reset'])
   for reach,d in states:
    c,p,pp,ch,np=reset(d);newstates.append((reach,c));rd=add(rd,p,reach);rp=add(rp,pp,reach);owner+=reach*d.core;source_changes+=ch;source_positive+=np
   ck(owner<=s.core);ck(nonnegative(add({2:s.core},rp,-1)));bookings[rr]=owner
   states=newstates;signed=add(signed,rd);pos=add(pos,rp);changed+=source_changes;positive_sources+=source_positive
   records.append({'op':'reset','ordinal':rr+1,'phase_bits':states[0][1].k,'states':len(states),'signed_excess':ser(rd),'positive_booking':ser(rp),'reached_source_I':str(owner),'changed_sources':source_changes,'positive_sources':source_positive})
 final={};fullkl={};remain=Q(0)
 for reach,d in states:final=add(final,d.CE,reach);fullkl=add(fullkl,d.debt,reach);remain+=reach*d.I
 ck(s.I==spent+remain);ck(add(old_debit,final)==add(s.CE,signed));ck(nonnegative(add({2:3*s.core},pos,-1)))
 ck(nonnegative(add({2:7*s.I},add(old_debit,final),-1)))
 return {'widths':[na,nb],'control':kind,'root_I':str(s.I),'original_source_I':str(s.core),'old_full_CE_debit':ser(old_debit),'signed_total_reset':ser(signed),'positive_total_booking':ser(pos),'full_terminal_CE':ser(final),'full_terminal_KL':ser(fullkl),'final_terminal_count':len(states),'remaining_I':str(remain),'spent_I':str(spent),'changed_source_refs':changed,'positive_source_events':positive_sources,'records':records}

def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv;lane=int(sys.argv[sys.argv.index('--lane')+1]) if '--lane' in sys.argv else None
 fs=phases();scalars=[];pads=[]
 if pilot or lane==0:
  for code in range(256):
   f=table(3,code)
   for over in [False,True]:scalars.append(scalar(f,over))
  for j,f in enumerate(fs):
   ck(direct(f)==spectrum(f));ck(influence(f)==sum(edge_inf(f,i) for i in range(5)))
   scalars.append(scalar(f));padded=tuple(f[x&31] for x in range(128));rr=target(padded);old=target(f)
   ck(all(q==(old[j] if j<32 else 0) for j,q in enumerate(rr)));pads.append({'phase':j,'extra_dummy_bits':2,'status':'PASS'})
 domain=[(i,na,nb) for i in range(8) for na,nb in [(1,1),(2,1)]]
 if pilot:domain=domain[:1]
 elif lane is not None:domain=[x for j,x in enumerate(domain) if j%2==lane]
 records=[]
 for i,na,nb in domain:
  ck(time.perf_counter()-start<55)
  try:rec=history(fs[i],fs[(i+1)%8],na,nb,['A','B','z'][i%3])
  except Exception:
   (R/'out/FAILURE.json').write_text(json.dumps({'phase_pair':[i,(i+1)%8],'widths':[na,nb],'assertions_before_failure':N,'transport_checks':sh.COUNT},indent=2),encoding='utf-8');raise
  rec['phase_pair']=[i,(i+1)%8];records.append(rec)
 result={'status':'PASS','pilot':pilot,'lane':lane,'helper':'A056-degree-tilt-reset-v1','assertions':N,'shared_transport_assertions':sh.COUNT,'scalar_certificates':scalars,'padding_checks':pads,'histories':records,'runtime_seconds':time.perf_counter()-start}
 name='pilot.json' if pilot else f'lane{lane}.json'
 (R/'out'/name).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k not in ['scalar_certificates','padding_checks','histories']}|{'histories':len(records),'scalar_cases':len(scalars),'positive_source_events':sum(r['positive_source_events'] for r in records)},indent=2))

if __name__=='__main__':
 import hashlib
 main()
