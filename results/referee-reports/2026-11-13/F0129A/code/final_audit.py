#!/usr/bin/env python3
"""Check source integrity and independently recalculate the report's statistics."""
import csv
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def main():
    report=(ROOT/'REPORT.md').read_text()
    assert report.splitlines()[0]=='PARTIAL'
    assert 'Work in progress' not in report
    index=['F0129 primary-source text index', 'Generated '+datetime.now(timezone.utc).isoformat(),
           'Page breaks in extracted full texts are form-feed characters.',
           'No source PDFs or page images are retained.','']
    for meta in sorted((ROOT/'sources').glob('*.metadata.txt')):
        d=json.loads(meta.read_text())
        paper=meta.with_name(meta.name.replace('.metadata.txt','.txt'))
        raw=paper.read_bytes()
        assert hashlib.sha256(raw).hexdigest()==d['text_sha256']
        index.extend([paper.name,'Pages: '+str(d['pages']),
                      'URL: '+d.get('url','; '.join(d.get('urls',[]))),
                      'Text SHA256: '+d['text_sha256'],''])
    (ROOT/'sources'/'INDEX.txt').write_text('\n'.join(index))
    for path in (ROOT/'sources').iterdir():
        assert path.is_file() and path.suffix=='.txt',path
        path.read_text()
    pdfs=[str(p.relative_to(ROOT)) for p in ROOT.rglob('*')
          if p.is_file() and (p.suffix.lower()=='.pdf' or p.open('rb').read(5)==b'%PDF-')]
    assert not pdfs,pdfs
    with (ROOT/'data'/'main_fine.csv').open() as f: rows=list(csv.DictReader(f))
    assert len(rows)==5*64*10
    for r in rows:
        assert all(math.isfinite(float(v)) for k,v in r.items() if k!='kernel')
        assert float(r['force_check_error'])<1e-7
        assert float(r['mass_check_error'])<1e-7
    with (ROOT/'data'/'main_fine_exponents.csv').open() as f:
        exponents={r['kernel']:r for r in csv.DictReader(f)}
    with (ROOT/'data'/'main_fine_summary.csv').open() as f:
        summaries={(r['kernel'],float(r['t'])):r for r in csv.DictReader(f)}
    checks=[]
    for name in ['sign','spline','two_bump','zero']:
        times=sorted({float(r['t']) for r in rows if float(r['t'])>=256})
        rms=[]
        for t in times:
            xs=[float(r['x']) for r in rows if r['kernel']==name and float(r['t'])==t]
            assert len(xs)==64
            v=math.sqrt(math.fsum(x*x for x in xs)/len(xs))
            assert abs(v-float(summaries[name,t]['rms']))<1e-10
            rms.append(v)
        z=[math.log(t) for t in times]; y=[math.log(v) for v in rms]
        mz=math.fsum(z)/len(z);my=math.fsum(y)/len(y)
        slope=math.fsum((a-mz)*(b-my) for a,b in zip(z,y))/math.fsum((a-mz)**2 for a in z)
        assert abs(slope-float(exponents[name]['rms_exponent']))<1e-12
        checks.append(dict(kernel=name,independent_rms_exponent=slope,
                           independent_final_rms=rms[-1],independent_final_rms_per_t=rms[-1]/8192))
    result=dict(report_status='PARTIAL',source_integrity='all hashes match',
                full_text_source_count=len(list((ROOT/'sources').glob('*.metadata.txt'))),
                pdf_files=pdfs,main_fine_rows=len(rows),independent_statistics=checks,
                complete_main_fine_seeds=64,
                numerical_warnings='bump and annular long Euler runs excluded; see REPORT.md')
    (ROOT/'data'/'final_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
