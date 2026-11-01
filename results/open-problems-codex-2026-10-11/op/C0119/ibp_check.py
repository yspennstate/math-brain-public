import checks, numpy as np, json, time
checks.rng=np.random.default_rng(11920261013)
gr=checks.graph(3,7,False); beta=4.; residuals=[]; energies=[]; overlaps=[]
start=time.time()
for k in range(40):
 xs=[checks.rng.normal(size=(250,len(l))) for l in gr[0]]
 _,p=checks.evaluate(xs,gr,beta)
 q=checks.overlap(p,p)
 u=sum((x*pp).sum(axis=1) for x,pp in zip(xs,p))
 residuals.extend((u-beta*(7-q)).tolist()); energies.extend(u.tolist()); overlaps.extend(q.tolist())
r=np.asarray(residuals); se=r.std(ddof=1)/np.sqrt(len(r))
result={'samples':len(r),'seed':11920261013,'n':7,'d':3,'beta':beta,'mean_residual':float(r.mean()),'standard_error':float(se),'z_score':float(r.mean()/se),'mean_energy':float(np.mean(energies)),'mean_Q0':float(np.mean(overlaps)),'seconds':time.time()-start,'reason':'Independent predetermined 10000-sample check after initial IBP residual was 2.43 standard errors from zero; no further sampling is planned.'}
(checks.ROOT/'ibp_check_results.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2))
