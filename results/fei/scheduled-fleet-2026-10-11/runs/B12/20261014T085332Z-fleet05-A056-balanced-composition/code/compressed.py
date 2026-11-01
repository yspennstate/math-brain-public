from check import *
def root(k,ra,rb,ea=True,eb=True):
 d=Q(1,1<<k);e=Q(1,1<<(k//2));a=Q(1,1<<ra) if ea else Q(0);b=Q(1,1<<rb) if eb else Q(0)
 groups=[(1,True,1-2*d,e),((2**k+2**(k//2))//2-1,False,-2*d,e),((2**k-2**(k//2))//2,False,-2*d,-e)]
 H={};Hu={};Hv={}
 for count,empty,u,v in groups:
  g=(1-a)*empty+a*u;h=(1-b)*empty+b*v
  packet=add(phi(((g+h)/2)**2),phi(((g-h)/2)**2))
  packet=add(packet,phi((a*(u-empty)/2)**2),2*(2**ra-1))
  packet=add(packet,phi((b*(v-empty)/2)**2),2*(2**rb-1))
  H=add(H,packet,count);Hu=add(Hu,phi(u*u),count);Hv=add(Hv,phi(v*v),count)
 Iu=2*k*d;Iv=Q(k,2);core=(a*Iu+b*Iv)/2
 gamma=a*d+b*(1-e)/2 # bent sign at the unique point defect is +1
 ctrl=ra*a*d+rb*b*(1-e)/2+gamma;I=core+ctrl
 L=add(add(scale(Hu,a/2),Hv,b/2),{2:core+7*ctrl});L=add(L,H,-1)
 assert nonnegative(add({2:4*Iu},Hu,-1)) and nonnegative(add({2:4*Iv},Hv,-1))
 assert nonnegative(L) and nonnegative(add({2:7*I},H,-1))
 return dict(H=H,L=L,I=I,core=core,ctrl=ctrl,a=a,b=b)
def calc(k):
 initial=root(k,2,2);leaves=[];spent=Q(0);s=initial;weight=Q(1)
 # Resolve the two B controls only on passing path, then two A controls.
 for kind,n in [('B',2),('B',1),('A',2),('A',1)]:
  if kind=='B':
   rb=n;ra=2;children=[root(k,ra,rb-1),root(k,ra,rb-1,eb=False)];inf=Q(1,1<<rb)*(1-Q(1,1<<(k//2)))/2
  else:
   ra=n;rb=0;children=[root(k,ra-1,rb),root(k,ra-1,rb,ea=False)];inf=Q(1,1<<ra)*Q(1,1<<k)
  assert s['I']==inf+(children[0]['I']+children[1]['I'])/2
  drift=add(s['H'],add(children[0]['H'],children[1]['H']),-Q(1,2))
  excess=add(drift,{2:-7*inf})
  refund=add(add(children[0]['L'],children[1]['L']),s['L'],-2)
  assert scale(refund,Q(1,2))==excess
  if kind=='A' and n==2:
   local={'influence':str(inf),'entropy_drift_prime_logs':ser(drift),'drift_minus_7_influence':ser(excess),'positive_excess_exact':nonnegative(excess) and bool(excess),'child_book_refund_exact':ser(scale(refund,Q(1,2)))}
  spent+=weight*inf;leaves.append((weight/2,children[1]));weight/=2;s=children[0]
 leaves.append((weight,s));EH={};EL={};EI=Q(0)
 for w,l in leaves:EH=add(EH,l['H'],w);EL=add(EL,l['L'],w);EI+=w*l['I']
 assert initial['I']==spent+EI
 assert initial['H']==add(add(add({2:7*spent},EH),EL),initial['L'],-1)
 assert nonnegative(add({2:7*EI},EH,-1))
 return {'shared_dimension':k,'local_private_A_query_after_B_success':local,'stopped_history_influence':str(spent),'terminal_influence':str(EI),'root_influence':str(initial['I']),'fixed_original_source_book':'signed stopped equality and all terminal prices PASS'}
def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv
 u=(-1,)+(1,)*15
 v=tuple((-1)**(((x&1)*((x>>1)&1)+((x>>2)&1)*((x>>3)&1))%2) for x in range(16))
 for ra,rb in [(2,2),(2,0),(1,0),(0,0)]:
  direct=State(u,v,prob(u),prob(v),ra,rb);short=root(4,ra,rb)
  assert short['H']==direct.H and short['I']==direct.I and short['L']==direct.L
 cases=[calc(k) for k in ([4] if pilot else [4,8,12,16,20])]
 result={'helper_version':'A056-point-bent-fixed-book-v1','pilot':pilot,'cases':cases,'assertions':'ALL PASS','seconds':time.perf_counter()-start}
 (R/'out'/('compressed_pilot.json' if pilot else 'compressed.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'pilot':pilot,'cases':len(cases),'positive_local_excess_dimensions':[c['shared_dimension'] for c in cases if c['local_private_A_query_after_B_success']['positive_excess_exact']],'seconds':result['seconds']}))
if __name__=='__main__':main()
