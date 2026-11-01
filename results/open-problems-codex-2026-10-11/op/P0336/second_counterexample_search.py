import numpy as np,json,pathlib,time
rng=np.random.default_rng(4336);start=time.time();found=None
for batch in range(30):
 a=rng.random((100000,2,2));b=rng.random((100000,2,2));b[:,:,0]+=2
 d=b[:,None,:,0]-a[:,:,None,0];h=b[:,None,:,1]-a[:,:,None,1]
 e=h*h/(np.hypot(d,h)+d);q=h*h/(2*d)
 de=e[:,0,0]+e[:,1,1]-e[:,0,1]-e[:,1,0];dq=q[:,0,0]+q[:,1,1]-q[:,0,1]-q[:,1,0]
 idx=np.flatnonzero(de*dq<0)
 if len(idx):
  k=int(idx[0]);found={'source':a[k].tolist(),'target':b[k].tolist(),'euclidean_difference':float(de[k]),'quadratic_difference':float(dq[k]),'batch':batch,'trials':100000*(batch+1)};break
pathlib.Path('second_counterexample_search.json').write_text(json.dumps({'found':found,'seconds':time.time()-start},indent=2));print(json.dumps(found,indent=2))
