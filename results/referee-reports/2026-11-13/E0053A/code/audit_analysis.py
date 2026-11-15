#!/usr/bin/env python3
"""Independent scalar audit of one-power WLS intercepts and source hashes."""
import collections,hashlib,json,math,pathlib,subprocess
ROOT=pathlib.Path(__file__).resolve().parents[1];D=ROOT/'data'
summary=json.loads((D/'summary.json').read_text());fits=json.loads((D/'fits.json').read_text());checks=[]
for fit in fits:
    if fit['mode']!='large' or fit['nmin']!=256 or len(fit['powers'])!=1:continue
    d=fit['d'];metric=fit['metric'];power=fit['powers'][0]
    ss=[r for r in summary if r['mode']=='large' and r['d']==d and r['n']>=256 and r['n']<=fit['nmax']]
    data=[]
    for r in ss:
        sig=max(r[metric+'_se'],1/r['n']/math.sqrt(r['samples']))
        data.append((1/sig**2,r['n']**(-power),r[metric+'_mean']))
    s0=math.fsum(w for w,x,y in data);s1=math.fsum(w*x for w,x,y in data);s2=math.fsum(w*x*x for w,x,y in data)
    t0=math.fsum(w*y for w,x,y in data);t1=math.fsum(w*x*y for w,x,y in data)
    scalar=(s2*t0-s1*t1)/(s0*s2-s1*s1)
    error=abs(scalar-fit['limit']);assert error<1e-10,(fit,scalar)
    checks.append(dict(d=d,metric=metric,power=power,independent_intercept=scalar,difference=error))
versions=collections.Counter();total=0
for mode in ['small','large','deep','sa']:
    p=D/f'{mode}.jsonl'
    if not p.exists():continue
    for l in p.read_text().splitlines():
        r=json.loads(l);path=ROOT/r['engine_source'];actual=hashlib.sha256(path.read_bytes()).hexdigest();assert actual==r['engine_source_sha256'];versions[r['engine_source']]+=1;total+=1
result=dict(intercept_checks=checks,source_hash_checks=total,source_versions=dict(versions))
(D/'audit_analysis.json').write_text(json.dumps(result,indent=2)+'\n');print('Independent intercept checks:',len(checks),'source hash checks:',total)
