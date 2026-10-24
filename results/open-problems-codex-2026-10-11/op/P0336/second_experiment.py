import numpy as np, scipy.optimize, json,pathlib,time
rng=np.random.default_rng(3336);start=time.time();out=[]
for n,reps in [(200,10),(1000,6),(3000,4)]:
 for rep in range(reps):
  a=rng.random((n,2));b=rng.random((n,2));b[:,0]+=2
  d=b[None,:,0]-a[:,None,0];h=b[None,:,1]-a[:,None,1]
  r=np.hypot(d,h);r+=d;np.square(h,out=h);h/=r;del r
  ii,pe=scipy.optimize.linear_sum_assignment(h);en=float(np.mean(h[ii,pe]));del h
  h=b[None,:,1]-a[:,None,1];np.square(h,out=h);h/=d;h*=.5;del d
  ii,pq=scipy.optimize.linear_sum_assignment(h);qn=float(np.mean(h[ii,pq]));qpe=float(np.mean(h[ii,pe]));del h
  ae=np.sort(a[:,1]);be=np.sort(b[:,1]);D=float(max(np.max(np.arange(1,n+1)/n-ae),np.max(ae-np.arange(n)/n)));S=float(np.mean((ae-be)**2))
  res={'n':n,'rep':rep,'En':en,'Qn':qn,'QofEuclidean':qpe,'same_edge_fraction':float(np.mean(pe==pq)),'n_gap':n*(qn-en),'n2_gap':n*n*(qn-en),'D_source':D,'S_n':S}
  for name,p in [('e',pe),('q',pq)]:
   dd=b[p,0]-a[:,0];hh=b[p,1]-a[:,1];M=float(np.mean(hh*hh));H=float(np.max(np.abs(hh)));w=np.abs(hh)/dd
   z1=a[:,1]+hh*(1-a[:,0])/dd;z2=a[:,1]+hh*(2-a[:,0])/dd
   minorder=float(np.min(np.diff(z2[np.argsort(z1)])))
   assert minorder>=-1e-10
   assert np.all(M+1e-14>=(w*w/16)*np.maximum(w/2-2*D,0))
   assert H<=max(24*D,12*M**(1/3))+1e-12
   res[name+'_max_h']=H;res[name+'_M']=M;res[name+'_min_gap_order']=minorder
  assert qn-en>=-1e-14
  assert qn-en <=res['e_max_h']**2*res['e_M']/8+1e-14
  out.append(res);pathlib.Path('second_numerics.json').write_text(json.dumps(out,indent=2));print(json.dumps(res),flush=True)
print('elapsed seconds',time.time()-start)
