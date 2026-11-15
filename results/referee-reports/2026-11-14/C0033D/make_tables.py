"""Generate report tables solely from saved data; intervals round outwards."""
import json,re,math
from pathlib import Path
from fractions import Fraction as F

def read(n):return json.loads(Path('data/'+n+'.json').read_text())
def num(z):return float(F(z))
def interval_short(z,digits=12):
    scale=10**digits;lo=F(z[0])*scale;hi=F(z[1])*scale
    l=lo.numerator//lo.denominator;h=-((-hi.numerator)//hi.denominator)
    def dec(v):
        sg='-' if v<0 else '';v=abs(v)
        return sg+str(v//scale)+'.'+str(v%scale).zfill(digits)
    return '['+dec(l)+', '+dec(h)+']'
def table(headers,rows):
    return '| '+' | '.join(headers)+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+''.join('| '+' | '.join(map(str,r))+' |\n' for r in rows)
def volume(cell):return math.prod(F(h)-F(l) for l,h in cell)

def main():
    report=Path('REPORT.md').read_text();s=read('search');c=read('certificates')
    cert={r['name']:r for r in c['records']}
    rows=[]
    for r in s['families']:
        rows.append([r['family'],r['accepted'],format(r['theta'],'.11g'),interval_short(cert[r['family']]['margin'])])
    txt=table(['Family','Accepted','Largest binary theta','Certified margin at its rounded point'],rows)
    txt+='\nData: [data/search.json](data/search.json), [data/certificates.json](data/certificates.json). The final column certifies one point per row, not every sample.\n'
    # Report every optimization restart, not just a favorable selection.
    txt+='\n'+table(['Local start','Spectral floor','Evaluations','Converged','Binary theta','Certified margin'],[
        [r['start'],r['epsilon'],r['evaluations'],r['converged'],format(r['theta'],'.11g'),interval_short(cert['NM_'+str(r['start'])]['margin'])]
        for r in s['optimizations']])
    txt+='\n'+table(['Differential evolution floor','Evaluations','Converged','Binary theta','Certified margin'],[
        [r['epsilon'],r['evaluations'],r['converged'],format(r['theta'],'.11g'),interval_short(cert['DE_'+str(r['epsilon'])]['margin'])]
        for r in s['de']])
    values={'SEARCH_TABLE':txt}
    b=read('boundary')
    values['BOUNDARY_TABLE']=table(['Family (16), j','Certified margin'],[[r['k'],interval_short(r['margin'])] for r in b['structured']])
    values['BOUNDARY_TABLE']+='\n'+table(['Cyclic k','Certified margin'],[[r['k'],interval_short(r['margin'])] for r in b['cyclic']])
    values['BOUNDARY_TABLE']+='\nCode: [boundary.py](boundary.py); data: [data/boundary.json](data/boundary.json). Cyclic entries use the proved closed formula; entries for (16) certify the full Hessian directly.\n'
    a=read('audit');f=read('family')
    values['AUDIT_TABLE']=table(['Check','Cases','Largest absolute binary discrepancy'],[
        [name,a['cases'],format(err,'.5g')] for name,err in zip(a['error_columns'],a['max_errors'])])
    values['AUDIT_TABLE']+='\n'+table(['Additional check','Result'],[
        ['Cyclic determinant (13), symbolic remainder',f['symbolic_remainder']],
        ['Cyclic closed formula vs full criterion, 5 points',format(max(r['error'] for r in f['full_formula_checks']),'.5g')],
        ['Diagonal expansion (5): theta/t^2 at t=0.0003',format(a['diagonal_asymptotic'][-1]['theta_over_t2'],'.12g')],
        ['Diagonal expansion predicted coefficient',format(a['diagonal_asymptotic'][-1]['predicted'],'.12g')],
        ['Zero expansion (6): theta/t at t=0.0003',format(a['zero_asymptotic'][-1]['theta_over_t'],'.12g')],
        ['Zero expansion predicted coefficient',format(a['zero_asymptotic'][-1]['predicted'],'.12g')]])
    values['AUDIT_TABLE']+='\nCode: [audit.py](audit.py), [family.py](family.py); data: [data/audit.json](data/audit.json), [data/family.json](data/family.json). Full asymptotic tables, not just the last entries, are saved in the audit data.\n'
    rows=[];resource_rows=[['Random/local search',s['seconds'],s['peak_rss_mib']],['51 point certificates',c['seconds'],c['peak_rss_mib']],['Boundary certificates',b['seconds'],b['peak_rss_mib']],['Independent numerical audit',a['seconds'],a['peak_rss_mib']]]
    for name in ('bnb_small','bnb_local_improved','bnb_interior','bnb_interior_full'):
        p=read(name);vr=volume(p['root']);vc=sum(volume(r['box']) for r in p['certified']);vu=sum(volume(r) for r in p['pending'])
        rows.append([name,p['nodes'],len(p['certified']),len(p['infeasible']),len(p['pending']),p['complete'],format(float(vc/vr),'.8g'),format(float(vu/vr),'.8g')])
        resource_rows.append([name,p['seconds'],p['peak_rss_mib']])
    values['BNB_TABLE']=table(['Checkpoint','Nodes','Accepted','Discarded','Pending','Complete','Accepted root fraction','Pending root fraction'],rows)
    values['BNB_TABLE']+='\nFiles: [small cover](data/bnb_small.json), [wider box](data/bnb_local_improved.json), [truncated domain](data/bnb_interior.json), [truncated domain with full Hessian fallback](data/bnb_interior_full.json). The wider root is a,b,c in [0.45,0.55], x,y in [0.09,0.11], Re Q23 in [-0.02,0.02], Im Q23 in [0.09,0.11]. None of the fallback run’s accepted cells required the Hessian test; that fallback did not close the unresolved cells.\n'
    if Path('data/cover_audit.json').exists():
        ca=read('cover_audit');resource_rows.append(['Exact partition and leaf audit',ca['seconds'],ca['peak_rss_mib']])
    values['RESOURCE_TABLE']=table(['Run','Seconds','Peak RSS, MiB'],[[n,format(t,'.4g'),format(m,'.5g')] for n,t,m in resource_rows])
    for name,body in values.items():
        pattern='<!-- '+name+'_START -->'+r'[\s\S]*?'+'<!-- '+name+'_END -->'
        replacement='<!-- '+name+'_START -->\n\n'+body+'\n<!-- '+name+'_END -->'
        report,count=re.subn(pattern,lambda m:replacement,report)
        assert count==1,name
    Path('REPORT.md').write_text(report)
if __name__=='__main__':main()
