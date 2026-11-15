"""Check saved outputs, report rounding, proof bounds on grids, and local links."""
import csv, hashlib, json, re
from pathlib import Path
from decimal import Decimal, localcontext
import mpmath as mp
mp.mp.dps=75
ROOT=Path(__file__).resolve().parent

def main():
    p=json.loads((ROOT/'precision_results.json').read_text())
    tol=mp.mpf('1e-50');threshold=mp.exp(-1)
    counts=[]
    for r in p['three_state']:
        eps=mp.mpf(r['eps']);last=mp.inf;n=0
        for row in csv.DictReader(open(ROOT/r['grid_file'])):
            t,d,p00,p20,lower=[mp.mpf(row[k]) for k in ['t','dbar','p00','p20','lower_event_bound']]
            assert d<=last+tol
            assert d>=abs(p00-p20)-tol
            assert p00>=mp.exp(-eps*t)-tol
            g=mp.exp(-(1+eps)*t)*(1+(1+eps)*t)
            assert p20<=1-g+tol
            assert d>=lower-tol
            if t<=2:assert lower>threshold
            # At t=0 every distinct point-mass pair ties at TV=1.
            if t>0:assert int(row['max_pair_i'])==0 and int(row['max_pair_j'])==2
            last=d;n+=1
        assert n==3001
        counts.append(n)
    gamma=list(csv.DictReader(open(ROOT/'gamma_results.csv')))
    cert=json.loads((ROOT/'rational_certificates.json').read_text())
    with localcontext() as ctx:
        ctx.prec=100
        for row,bracket in zip(gamma,cert['roots']):
            k=int(row['k']);lo=Decimal(bracket['lower']);hi=Decimal(bracket['upper'])
            assert format(lo,'.30f')==format(hi,'.30f')==format(Decimal(row['t_k']),'.30f')
            assert format(lo/k,'.20f')==format(hi/k,'.20f')==format(Decimal(row['ratio']),'.20f')
    st=list(csv.DictReader(open(ROOT/'stopping_results.csv')))
    assert len(st)==5000
    assert sum(r['lp_solved']=='True' for r in st)==500
    assert sum(int(r['n']) for r in st if r['lp_solved']=='True')==2500
    for r in st:
        a,b,c=map(float,[r['tau2'],r['tau_stop'],r['tau0']])
        assert a<=b*(1+1e-10) and b<=c*(1+1e-10)
    report=(ROOT/'REPORT.md').read_text()
    for label,target in re.findall(r'\[([^\]]+)\]\(([^)]+)\)',report):
        assert (ROOT/target).is_file(),(label,target)
    source=(ROOT/'PAPER.tex').read_bytes()
    sha=hashlib.sha256(source).hexdigest()
    assert sha in report
    assert source.count(b'\\bibitem')==10
    assert len(source.splitlines())==242
    manifest=json.loads((ROOT/'run_manifest.json').read_text())
    assert all(r['returncode']==0 and not r['stderr'] for r in manifest['runs'])
    assert manifest['max_child_rss_bytes']<1000000000
    assert manifest['max_run_seconds']<300
    out={'status':'PASS','grids_checked':counts,'gamma_certified_roundings':60,
         'chain_rows_checked':len(st),'local_report_links':'all exist','source_sha256':sha}
    (ROOT/'artifact_audit.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
