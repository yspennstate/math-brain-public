for m,d in product(range(1,7),[F(0),F(1,256)]):
 theta=F(1,512);rho=F(1,2**m);t=rho*rho;alpha=1-t*theta;qr=[]
 for s in range(2**(m+2)):
  if s==0:q=t*theta
  elif s<4:q=alpha*{1:F(1,4),2:F(1,4),3:F(1,16)}[s]
  else:q=alpha*(F(7,80) if s&2 else F(7,20))/(2*(2**m-1))
  qr.append(q)
 f0=[];f1=[]
 for x in range(len(qr)):
  c=x&1;u=(x>>1)&1;z=x>>2;q=-1 if c==0 and z==0 else 1
  f0.append(q*(-1)**u);f1.append(q*(-1)**c)
 dc=plus(times(decrement(f0,qr,1),1-d),times(decrement(f1,qr,1),d))
 x=t*theta
 U0=plus(times(log((1+3*x)/(1-x)),(1-rho)**2),times(log(5),2*rho-t))
 U1=plus(times(log((1+3*x)/(4*x)),t),times(log(F(5,4)),1-t))
 ck(dc==plus(times(U0,1-d),times(U1,d)))
 ck(interval(U0)[1]<F(13,4));ck(interval(U1)[1]<F(13,4));ck(interval(dc)[1]<4*(1-d))
 if d:
  p=t*d;q=x
  kl=plus(times(log(p/q),p),times(log((1-p)/(1-q)),1-p))
  ck(interval(kl)[0]>0);ck(interval(kl)[1]<p<=F(1,1024))
h=plus(times(log(F(1,256)),-F(1,256)),times(log(F(255,256)),-F(255,256)))
ck(interval(h)[1]<F(19,512));ck(F(19,512)<F(1,16))
ck((F(1,2)+F(63,64)-F(1,1024))/2==F(1519,2048));ck(F(1519,2048)>F(5,8))
ck(F(5,8)-F(7,12)==F(1,24));ck(F(1,24)>F(59,2560))
p=R.parent/'20261022T234315Z-account03-A070-analytic-route-referee/out/CORE_CHECKPOINT.json'
cert=json.loads(p.read_text(encoding='utf-8'));ck(F(cert['P_core_interval'][1])<F(7,12))
result=dict(status='PASS',assertions=checks,early_u_cases=12,theta='1/512 frozen from root',actual_disagreement=['0','1/256'],owner_capacity_lower='1519/2048',P_core_upper='7/12',remaining_original_earmark_lower='1/24',elapsed_seconds=time.perf_counter()-start)
(R/'out/FINAL_REVIEW.json').write_bytes((json.dumps(result,indent=2)+'\n').encode('utf-8'));print(json.dumps(result))
