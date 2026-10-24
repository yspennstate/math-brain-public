import mpmath as mp,json,math,pathlib
mp.mp.dps=55
laws=[('point',[0],[1]),('symmetric',[-1,1],[mp.mpf('.5')]*2),('skew',[-1,2],[mp.mpf(2)/3,mp.mpf(1)/3]),('rare_outlier',[0,1,50],[mp.mpf('.8'),mp.mpf('.199'),mp.mpf('.001')]),('zero_third',[-2,-1,1,3],[mp.mpf(4)/20,mp.mpf(5)/20,mp.mpf(10)/20,mp.mpf(1)/20])]
output=[]
for name,x,p in laws:
 mean=sum(a*b for a,b in zip(x,p)); y=[mp.mpf(a)-mean for a in x];mom={k:sum(w*a**k for a,w in zip(y,p)) for k in range(2,8)}
 for t in [mp.mpf(1000),mp.mpf(10000),mp.mpf(100000),mp.mpf(10000000)]:
  h=mp.findroot(lambda h:sum(w*(a-h)*mp.exp(-(a-h)**2/(2*t)) for a,w in zip(y,p)),(0,mp.mpf('.01')))
  u,r=mp.findroot(lambda u,r:(sum(w/(r+(u-a)**2/t) for a,w in zip(y,p))-1,sum(w*(u-a)/(r+(u-a)**2/t)**2 for a,w in zip(y,p))),(0,1))
  f=u+sum(w*(u-a)/(r+(u-a)**2/t) for a,w in zip(y,p))
  hc=-mom[3]/(2*t)+(mom[5]-6*mom[2]*mom[3])/(8*t*t)
  fc=-3*mom[3]/t+(5*mom[5]-22*mom[2]*mom[3])/(t*t)
  row={'law':name,'t':str(t),'mu3':str(mom[3]),'classical':str(h),'free':str(f),'classical_error_times_t3':str((h-hc)*t**3),'free_error_times_t3':str((f-fc)*t**3),'residual_free':str(max(abs(sum(w/(r+(u-a)**2/t) for a,w in zip(y,p))-1),abs(sum(w*(u-a)/(r+(u-a)**2/t)**2 for a,w in zip(y,p)))))}
  output.append(row);print(name,'t',t,'scaled errors',mp.nstr((h-hc)*t**3,10),mp.nstr((f-fc)*t**3,10))
pathlib.Path('numerics_atomic.json').write_text(json.dumps(output,indent=2),encoding='utf8')

