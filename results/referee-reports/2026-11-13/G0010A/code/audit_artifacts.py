"""Audit deliverable format, data consistency, source formats, and proof constants."""
import csv,hashlib,json,math,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def repair_inline_openers(text):
    stack=[]; insert=[]
    for i,ch in enumerate(text):
        if ch=='(': stack.append(i)
        elif ch==')' and stack:
            start=stack.pop()
            if i>0 and text[i-1]=='\\' and (start==0 or text[start-1]!='\\'):
                insert.append(start)
    for i in sorted(insert,reverse=True): text=text[:i]+'\\'+text[i:]
    return text, len(insert)


def main():
    report=ROOT/'REPORT.md';s=report.read_text()
    assert s.splitlines()[0]=='COUNTEREXAMPLE'
    assert s.count('\\(')==s.count('\\)'),(s.count('\\('),s.count('\\)'))
    assert s.count('\\[')==s.count('\\]')
    assert 'will be completed' not in s and 'being saved' not in s
    for p in (ROOT/'sources').iterdir():
        assert p.is_file() and p.suffix=='.txt',str(p)
        p.read_text()
    banned=[]
    for p in ROOT.rglob('*'):
        if p.is_file() and p.suffix.lower() in ('.pdf','.djvu','.tif','.tiff'):
            banned.append(str(p.relative_to(ROOT)))
    assert not banned,banned
    trials=list(csv.DictReader((ROOT/'data/trials.csv').open()))
    summary=list(csv.DictReader((ROOT/'data/summary.csv').open()))
    meta=json.loads((ROOT/'data/simulation_metadata.json').read_text())
    assert len(trials)==meta['total_trials']==1200
    assert len(summary)==meta['host_cases']==30
    assert max(int(r['n']) for r in trials)==1118688
    assert meta['priority']==10 and meta['peak_rss_bytes']<4_000_000_000
    for r in trials:
        assert 1<=int(r['largest'])<=int(r['n'])
        assert int(r['largest'])<=int(r['open_edges'])+1
        assert math.isclose(float(r['p'])*float(r['lambda']),1-float(r['epsilon']),rel_tol=1e-13)
    k,b,q=100,108,.98
    assert k>=2*math.sqrt(b) and b+1<1.1*k
    mu=b*(-math.expm1(-q/(k+1)))
    assert mu>1 and .004<math.log(mu)/(2*math.log(b))
    # A second route to the growth exponent, using exact graph sizes and thresholds.
    h=1000;logn=(2*h+1)*math.log(b)-math.log(b-1)
    eta=.05
    assert ((h-math.floor(eta*h))*math.log(mu)-math.log(2))/logn>.004
    result={'status':'PASS','report_inline_math_pairs':s.count('\\('),
            'report_display_math_pairs':s.count('\\['),'plain_text_sources':len(list((ROOT/'sources').glob('*.txt'))),
            'trial_rows':len(trials),'host_cases':len(summary),'max_n':meta['host_cases'] and max(int(r['n']) for r in trials),
            'peak_rss_bytes':meta['peak_rss_bytes'],'nice':meta['priority'],
            'explicit_counterexample_mu':mu,'forbidden_paper_files':banned}
    (ROOT/'data/artifact_audit.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
