import numpy as np, scipy.special as ss, scipy.optimize as so, pathlib,json,math
B=pathlib.Path(__file__).resolve().parent
means=np.array([-1.,3.]); sigmas=np.array([.4,1.2]); weights=np.array([.75,.25])
def moment(k):
 return sum(w*sum(math.comb(k,j)*m**(k-j)*sig**j*(math.prod(range(1,j,2)) if j else 1) for j in range(0,k+1,2)) for m,sig,w in zip(means,sigmas,weights))
v,c3,c5=[moment(k) for k in [2,3,5]]
out={'law':'0.75 N(-1,0.16) + 0.25 N(3,1.44), mean zero','moments':{'v':v,'mu3':c3,'mu5':c5},'checks':[]}
for t in [1000.,3000.,10000.]:
 classical=so.brentq(lambda h:sum(w*(m-h)*(t/(t+sig**2))**1.5*np.exp(-(h-m)**2/(2*(t+sig**2))) for m,sig,w in zip(means,sigmas,weights)),-1.,1.,xtol=1e-14)
 row={'t':t,'classical':classical,'classical_error_t3':(classical+c3/(2*t)-(c5-6*v*c3)/(8*t*t))*t**3}
 modes=[]
 for n in [64,128]:
  nodes,ww=ss.roots_hermitenorm(n); ys=np.concatenate([m+sig*nodes for m,sig in zip(means,sigmas)]); ps=np.concatenate([w*ww/np.sqrt(2*np.pi) for w in weights])
  def equations(z):
   u,r=z; q=u-ys; d=r+q*q/t
   return [np.sum(ps/d)-1,np.sum(ps*q/d**2)]
  sol=so.root(equations,[-2*c3/t,1-v/t],tol=1e-11)
  u,r=sol.x; mode=u+np.sum(ps*(u-ys)/(r+(u-ys)**2/t)); modes.append(mode)
  row[str(n)]={'mode':mode,'success':bool(sol.success),'max_residual':float(np.max(np.abs(equations(sol.x)))),'free_error_t3':(mode+3*c3/t-(5*c5-22*v*c3)/t**2)*t**3}
 row['quadrature_mode_difference']=abs(modes[0]-modes[1]); out['checks'].append(row)
z=np.r_[np.linspace(0,1,1001),np.geomspace(1,1e6,1000)]
out['inequality_grid_minima']={'classical':float(np.min((1-z)*np.exp(-z/2)-(1-1.5*z))),'stationarity_lower':float(np.min(1-(1+z)**-2)),'stationarity_upper':float(np.min(2*z-(1-(1+z)**-2)))}
(B/'unbounded_results.json').write_text(json.dumps(out,indent=2),encoding='utf8'); print(json.dumps(out,indent=2))
