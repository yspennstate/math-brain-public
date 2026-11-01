"""Independent referee computations; writes only beside this script."""
from pathlib import Path
import json, math, urllib.request, urllib.parse, concurrent.futures
import numpy as np
import pymupdf

HERE = Path(__file__).resolve().parent
rng = np.random.default_rng(1040905)
doc = pymupdf.open(HERE / 'source.pdf')
pages = [p.get_text() for p in doc]
(HERE / 'source.txt').write_text('\n'.join(f'\nPDF PAGE {i+1}\n{t}' for i,t in enumerate(pages)), encoding='utf-8')
for i in [3,12,14,19,28,47]:
    print(f'\nSOURCE PDF PAGE {i+1}\n{pages[i]}', flush=True)

out = {}
N = 250000
for d in [2,3,4]:
    p = d-1
    angles = rng.normal(size=(N,d+1,d))
    angles /= np.linalg.norm(angles,axis=2)[:,:,None]
    mat = np.concatenate([np.ones((N,d+1,1)), angles],axis=2)
    det = np.abs(np.linalg.det(mat))
    out[f'Z_{d}'] = {'mean':float(det.mean()),'se':float(det.std()/math.sqrt(N))}
    theta = angles[0]
    D = abs(np.linalg.det(np.column_stack([np.ones(d+1),theta])))
    s = 1.71
    eps = 1e-6
    def radii(z):
        sep, v = z[0], z[1:]
        return sep*(np.sqrt(1+v@v)-theta@v)**(-p)
    z = np.r_[s,np.zeros(d)]
    jac = np.column_stack([(radii(z+eps*np.eye(d+1)[k])-radii(z-eps*np.eye(d+1)[k]))/(2*eps) for k in range(d+1)])
    wanted = (p*s)**d*D
    jacerr = abs(abs(np.linalg.det(jac))/wanted-1)
    us, aa = [], []
    for i in range(d+1):
        retained = np.delete(theta,i,axis=0)
        _,_,vt = np.linalg.svd(retained[1:]-retained[0])
        u = vt[-1]
        a = retained[0]@u
        if a < theta[i]@u:
            u, a = -u,-a
        us.append(u); aa.append(a)
    us,aa = np.array(us),np.array(aa)
    ts = np.linspace(.15,.65,d+1)
    q = np.tanh(ts)
    phi = rng.normal(size=(N,d)); phi /= np.linalg.norm(phi,axis=1)[:,None]
    H = ((1-aa*q)/(1-(phi@us.T)*q))**p
    integrand = np.maximum(0,np.max(H-1,axis=1))
    A = integrand.mean()
    predicted = (1+A)**(-d-1)
    # Exact finite-window PPP test with independent directions in every trial.
    # Bound H <= exp(2*p*max(ts)); all blockers are inside this window.
    multiplier = math.exp(2*p*max(ts))
    trials = 15000
    hits = 0
    score_err = 0.
    cross_err = 0.
    monotonicity_violations = 0
    for trial in range(trials):
        S = rng.gamma(d+1)
        count = rng.poisson(S*(multiplier-1))
        ph = rng.normal(size=(count,d)); ph /= np.linalg.norm(ph,axis=1)[:,None]
        R = rng.uniform(S,S*multiplier,size=count)
        b = ph@us.T
        thresholds = ((1-aa*q)/(1-b*q))**p
        hits += not np.any(R[:,None] < S*thresholds)
        if trial < 200:
            # Recompute score in ball coordinates independently.
            zball = np.tanh(ts/2)[:,None]*us
            ball_base = np.sum((zball[None,:,:]-ph[:,None,:])**2,axis=2)/(1-np.sum(zball*zball,axis=1))
            hyp_base = np.cosh(ts)-b*np.sinh(ts)
            if count:
                score_err = max(score_err,float(np.max(np.abs(ball_base-hyp_base))))
                rr = (R/S)**(1/p)
                # Crossing equation q=(r-1)/(r*b-a), independently derived.
                denom = rr[:,None]*b-aa
                with np.errstate(divide='ignore',invalid='ignore'):
                    qc = (rr[:,None]-1)/denom
                valid = (b>aa)&(qc>0)&(qc<1)
                blocked = valid&(qc<q)
                cross_err += int(np.count_nonzero(blocked != (R[:,None]<S*thresholds)))
                h0 = ((1-aa*(q/2))/(1-b*(q/2)))**p
                monotonicity_violations += int(np.count_nonzero((h0>1)&(thresholds<h0-1e-12)))
    empirical=hits/trials
    se=math.sqrt(empirical*(1-empirical)/trials)
    out[f'dimension_{d}']={'jacobian_relative_error':float(jacerr),'directions':theta.tolist(), 'times':ts.tolist(), 'A':float(A),'A_mc_se':float(integrand.std()/math.sqrt(N)), 'joint_prediction':float(predicted),'joint_simulation':empirical,'binomial_se':se,'ball_hyperboloid_max_error':score_err,'crossing_equivalence_mismatches':cross_err,'nesting_violations':monotonicity_violations}

# Scalar exact planar cap integral: d=2, with b=cos(alpha), b>a.
# integral (H-1)+ = (q/pi) integral_0^acos(a) (cos(alpha)-a)/(1-q*cos(alpha)) d alpha.
from scipy.integrate import quad
cap=[]
for a,t in [(-.8,.2),(0,.7),(.65,1.3)]:
    q=math.tanh(t); beta=math.acos(a)
    numerical=quad(lambda x:q*(math.cos(x)-a)/(1-q*math.cos(x)),0,beta,epsabs=1e-12)[0]/math.pi
    J=2/math.sqrt(1-q*q)*math.atan(math.sqrt((1+q)/(1-q))*math.tan(beta/2))
    analytic=((1-a*q)*J-beta)/math.pi
    cap.append({'a':a,'t':t,'quadrature':numerical,'analytic':analytic,'abs_error':abs(numerical-analytic)})
out['planar_cap_integrals']=cap
(HERE/'checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print('\nINDEPENDENT CHECKS\n'+json.dumps(out,indent=2),flush=True)

queries={
    'arxiv_ideal_voronoi':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"ideal" AND all:"Voronoi"','start':0,'max_results':30}),
    'arxiv_neighbors':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"hyperbolic" AND all:"Voronoi" AND (all:"neighboring" OR all:"Palm")','start':0,'max_results':20}),
    'openalex_ideal':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'ideal Poisson Voronoi','per-page':25}),
    'openalex_neighbors':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'hyperbolic Voronoi neighboring vertices','per-page':15}),
    'openalex_cites':'https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:W4361807156','per-page':50})
}
def fetch(item):
    name,url=item
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Independent mathematical referee (public bibliography check)'})
        data=urllib.request.urlopen(req,timeout=45).read().decode('utf-8')
        (HERE/(name+'.txt')).write_text(data,encoding='utf-8')
        if name.startswith('openalex'):
            obj=json.loads(data)
            summary=[{'title':w['title'],'year':w.get('publication_year'),'doi':w.get('doi'),'id':w['id'],'abstract':w.get('abstract_inverted_index')} for w in obj['results']]
        else:
            import xml.etree.ElementTree as ET
            ns={'a':'http://www.w3.org/2005/Atom'}
            summary=[{'title':e.findtext('a:title',namespaces=ns),'id':e.findtext('a:id',namespaces=ns),'abstract':e.findtext('a:summary',namespaces=ns)} for e in ET.fromstring(data).findall('a:entry',ns)]
        return name,{'url':url,'results':summary}
    except Exception as e:
        return name,{'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    literature=dict(pool.map(fetch,queries.items()))
(HERE/'literature.json').write_text(json.dumps(literature,indent=2),encoding='utf-8')
for name,val in literature.items():
    print('\nSEARCH',name,val.get('error','OK'),flush=True)
    for w in val.get('results',[]):
        print(w['title'],w.get('doi',w.get('id')),flush=True)
