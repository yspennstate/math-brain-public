import pathlib, json, hashlib
p=pathlib.Path('CouplingCertificate.lean')
report={'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'command':'lake env lean ~/brain_workers/TRIO_1011/op/P0211/CouplingCertificate.lean','working_directory':'~/lean_verify','status':'WAITING_FOR_SHARED_LEAN_SLOT','claim_of_formal_verification':False,'notes':'The current foreground tool session has not yet received a checker result. No sorry, native_decide, or unchecked axiom is used in the certificate. It contains seven algebraic sublemmas; the full Markov-chain theorem is a written proof.'}
pathlib.Path('LEAN_CHECK.json').write_text(json.dumps(report,indent=2),encoding='utf8')
# Check the complete invariant-sector certificate on finite parameter grids.
import numpy as np,math
lowest=1e100;count=0
for n in [8,9,16,31,100,1000]:
 for b in np.geomspace(4/n**2,1/16,17):
  a=n*math.sqrt(b)
  for l in range(1,n//2+1):
   k=np.arange(l,n-l+1,dtype=float)
   R=b*(n-k-l)/(k+a+1)+l*b+(k-1)*((l-1)*k+l*a)/(n*(k+a-1))
   lowest=min(lowest,float(min(R)/math.sqrt(b)));count+=len(k)
check={'harmonic_sector_grid_points':count,'minimum_certificate_over_sqrt_beta':lowest,'proved_lower_bound':.2}
pathlib.Path('all_sector_certificate.json').write_text(json.dumps(check,indent=2),encoding='utf8');print(check)
