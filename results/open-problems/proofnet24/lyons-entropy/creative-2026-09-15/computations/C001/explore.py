import numpy as np,itertools,math

def calc(L):
    n=3;K=np.eye(3)-np.linalg.inv(np.eye(3)+L)
    x=abs(L[0,1])**2/(L[0,0].real*L[1,1].real); y=abs(L[1,2])**2/(L[1,1].real*L[2,2].real); z=abs(L[2,0])**2/(L[2,2].real*L[0,0].real)
    d=-np.log([1-y,1-z,1-x]);tau=np.log((1-x)*(1-y)*(1-z))-np.linalg.slogdet(L)[1]+np.log(np.prod(np.diag(L).real))
    M=np.diag(d)+tau*K;delta=np.linalg.det(M).real
    w=[];om=[];hist=[]
    for i in range(3):
      for hs in itertools.product([0,1],repeat=i):
        Q=K[:i,:i]-np.diag(1-np.array(hs));pi=np.linalg.det(Q).real*(-1)**(i-sum(hs));q=K[i,i].real
        wi=np.zeros(3,complex);wi[i]=1
        if i:
          wi[:i]=-np.linalg.solve(Q,K[:i,i]);q=(q+K[i,:i]@wi[:i]).real
        w.append(wi);om.append(pi/(q*(1-q)));hist.append(hs)
    W=np.array(w).T; b=np.diag(W.conj().T@M@W).real;G=abs(W.conj().T@M@W)**2;C=G+delta*np.diag(1/np.array(om))
    out={'K':K,'M':M,'delta':delta,'d':d,'tau':tau,'w':W,'om':np.array(om),'C':C,'b':b,'hist':hist,'full':b@np.linalg.solve(C,b)}
    triples=[]
    for a in range(2):
      for bbit in range(2):
        ix=[0,1+a,3+2*a+bbit]
        cc=C[np.ix_(ix,ix)];bb=b[ix];triples.append((ix,bb@np.linalg.solve(cc,bb)))
    out['paths']=triples
    Sigma=-abs(K)**2; np.fill_diagonal(Sigma,np.diag(K).real*(1-np.diag(K).real));dc=np.diag(M).real;out['ind']=dc@np.linalg.solve(abs(M)**2+delta*Sigma,dc)
    return out

def show(label,L):
    d=calc(L);print(label,'eigL',np.linalg.eigvalsh(L),'tau',d['tau'],'full',d['full'],'ind',d['ind'],'paths',d['paths'])

if __name__=='__main__':
 for e in [.1,.01,.001,.0001]:
    # one near-perfect edge, moderate scaled companion edges, quadrature cycle
    a=np.sqrt(1-e*e);b=e/2;c=1j*e/2
    show(('strong',e),np.array([[1,a,c.conjugate()],[a,1,b],[c,b,1]],complex))
 for e in [.1,.01,.001,.0001]:
    r=1-e; x=r*r;ct=(3*x*x-x*x*x)/(2*r**3);th=np.arccos(ct)/3
    a=r*np.exp(1j*th); L=np.array([[1,a,a.conjugate()],[a.conjugate(),1,a],[a,a.conjugate(),1]],complex)/3
    show(('tauzero',e),L)
