import numpy as np, json
from scipy.special import logsumexp
from scipy.integrate import quad
from pathlib import Path
rng=np.random.default_rng(119061012)
steps=[tuple(sign if j==i else 0 for j in range(3)) for i in range(3) for sign in [-1,1]]
paths=[[(0,(0,0,0)),(1,a),(2,tuple(a[i]+b[i] for i in range(3)))] for a in steps for b in steps]
sites=sorted(set(j for p in paths for j in p)); index={j:i for i,j in enumerate(sites)}
A=np.zeros((len(paths),len(sites)))
for i,p in enumerate(paths):
 for j in p:A[i,index[j]]=1
beta=4.; n=3
def calc(x):
 h=x@A.T; z=logsumexp(beta*h,axis=-1); mu=np.exp(beta*h-z[:,None]); p=mu@A
 return z/beta,p,np.sum(mu*h,axis=-1),mu
x=rng.normal(size=(20000,len(sites))); g,p,u,mu=calc(x)
q0=np.sum(p*p,axis=1); residual=u-beta*(n-q0)
point=rng.normal(size=(1,len(sites))); gp,pp,_,_=calc(point)
errors=[]
for j in range(len(sites)):
 xp=point.copy(); xm=point.copy(); xp[0,j]+=1e-5; xm[0,j]-=1e-5
 errors.append(abs((calc(xp)[0][0]-calc(xm)[0][0])/2e-5-pp[0,j]))
noise=rng.normal(size=x.shape); overlaps={}; tv_slack=[]
for t in [0.,.05,.2,1.]:
 gt,pt,ut,mut=calc(np.exp(-t)*x+np.sqrt(-np.expm1(-2*t))*noise)
 cross=np.sum(p*pt,axis=1); overlaps[str(t)]=float(cross.mean())
 tv=.5*np.abs(mu-mut).sum(axis=1)
 tv_slack.append(float(np.min(tv-(q0-cross)/n)))
# Exact n=2, k=2 ground-state test: origin plus maximum of two normals.
def qexact(t):return 1.5+np.arcsin(np.exp(-t))/np.pi
exact_var=2-1/np.pi
integral,error=quad(lambda t:np.exp(-t)*qexact(t),0,np.inf,epsabs=1e-11)
test_t=np.geomspace(1e-7,100,1000)
out={'model':{'d':3,'n':n,'beta':beta,'paths':len(paths),'time_sites':len(sites),'samples':len(x)},
 'gradient_max_error':float(max(errors)),
 'IBP_residual_mean':float(residual.mean()),'IBP_residual_SE':float(residual.std(ddof=1)/np.sqrt(len(x))),
 'Q0':float(q0.mean()),'baseline_lower_bound':float(n*(1-np.sqrt(2*np.log(6))/beta)),
 'noise_overlaps':overlaps,'minimum_pointwise_TV_slack':min(tv_slack),
 'exact_two_choice_variance':exact_var,'exact_two_choice_covariance_integral':integral,'quadrature_error_estimate':error,
 'exact_two_choice_bound_min_slack':float(np.min(exact_var-(-np.expm1(-test_t))*np.array([qexact(t) for t in test_t])))}
Path(__file__).with_name('independent_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
