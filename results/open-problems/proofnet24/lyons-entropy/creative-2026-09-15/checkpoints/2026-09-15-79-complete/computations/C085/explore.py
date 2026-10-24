import numpy as np
from itertools import product

rng=np.random.default_rng(85)

def data(K):
    ps=np.array([((-1)**(3-mask.bit_count())*np.linalg.det(K-np.diag([not (mask>>i&1) for i in range(3)]))).real for mask in range(8)])
    if min(ps)<=0: return None
    f=-np.log(ps)
    c=np.array([f[6]-f[2]-f[4]+f[0],f[5]-f[1]-f[4]+f[0],f[3]-f[1]-f[2]+f[0]])
    tau=f[7]-f[3]-f[5]-f[6]+f[1]+f[2]+f[4]-f[0]
    m=c+tau*np.diag(K).real
    e=np.array([K[1,2],K[2,0],K[0,1]])
    er=np.abs(e)
    if min(m)<=1e-13 or min(er)<=1e-13: return None
    compare=np.diag(m)-abs(tau)*np.array([[0,er[2],er[1]],[er[2],0,er[0]],[er[1],er[0],0]])
    z=np.prod(e); k=m*er**2; dd=k-tau*z.real
    return ps,c,tau,m,e,np.linalg.eigvalsh(compare)[0],dd

def run():
    worst=(0,None)
    min_d=(0,None)
    count=0
    for mode in range(4):
      for it in range(12000):
        Z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
        U=np.linalg.qr(Z)[0]
        if mode==0: vals=rng.uniform(.001,.999,3)
        if mode==1: vals=1/(1+np.exp(rng.uniform(-15,15,3)))
        if mode==2: vals=np.array([rng.uniform(.05,.9),10**rng.uniform(-8,-1),10**rng.uniform(-8,-1)])
        if mode==3: vals=np.array([rng.uniform(.05,.9),1-10**rng.uniform(-8,-1),10**rng.uniform(-8,-1)])
        K=(U*vals)@U.conj().T
        dd=data(K)
        if dd is None: continue
        ps,c,tau,m,e,cm,d=dd
        if cm<worst[0]: worst=(cm,K.copy()); print('worst',mode,it,cm,'tau',tau,'diag',K.diagonal().real,'e',e,flush=True)
        if min(d)<min_d[0]: min_d=(min(d),K.copy())
        if cm<0: count+=1
    print('fail count',count)
    print('worst K',repr(worst[1]))
    print('min d',min_d)
    if worst[1] is not None: np.save('worst.npy',worst[1])

if __name__=='__main__': run()
