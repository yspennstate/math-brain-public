"""Validate saved coverage and exact final inequalities; not an independent audit."""
from pathlib import Path
from fractions import Fraction as F
import argparse, datetime, hashlib, json, math

ROOT=Path(__file__).resolve().parents[1]
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def read(path):return json.loads(path.read_text(encoding='utf-8'))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--finish',action='store_true');cli=ap.parse_args()
    state=read(ROOT/'logs/fine_checkpoint.json');meta=read(ROOT/'logs/fine_run_metadata.json')
    assert meta['input_hashes']==state['input_hashes']
    for name,expected in state['input_hashes'].items():assert digest(ROOT/name)==expected,name
    tables=[]
    for stage in ('q','a','e'):
        directory=ROOT/'logs/fine_tables_v1';receipt=read(directory/(stage+'.json'))
        assert digest(directory/receipt['data_file'])==receipt['sha256'],stage
        for name,expected in receipt['recipe']['input_hashes'].items():assert digest(ROOT/name)==expected,name
        tables.append({'stage':stage,'receipt':str((directory/(stage+'.json')).relative_to(ROOT)),'sha256':receipt['sha256']})
    rows=sorted(state['accepted'],key=lambda row:(row['rho_lo'],row['rho_hi']))
    assert rows
    covered=F(2,5);worst=0.;witnesses=[]
    for row in rows:
        lo=F.from_float(math.nextafter(row['rho_lo'],-math.inf));hi=F.from_float(math.nextafter(row['rho_hi'],math.inf))
        assert lo<=covered,('Gap',lo,covered)
        covered=max(covered,hi)
        assert row['pass'] and 0<=row['finite_operator_upper']<=row['operator_upper']<2
        lam,tau,total=(F.from_float(row[k]) for k in ('finite_operator_upper','outside_hs_squared_upper','operator_upper'))
        assert tau>=0 and total*total>=lam*lam+tau,'Invalid final completion inequality'
        path=ROOT/row['witness_file'];assert digest(path)==row['witness_sha256']
        witness=read(path);v=[float.fromhex(x) for x in witness['v_binary64_hex']];upper=[float.fromhex(x) for x in witness['row_upper_binary64_hex']]
        assert len(v)==len(upper)==row['x_panels'] and all(math.isfinite(x) and x>0 for x in v)
        assert all(math.isfinite(x) and x>=0 for x in upper) and max(upper)==row['finite_operator_upper']
        assert row['fine_implementation_sha256']==state['input_hashes']['scripts/certify_fine_cells.py']
        worst=max(worst,row['operator_upper']);witnesses.append({'file':row['witness_file'],'sha256':row['witness_sha256']})
    endpoint=F(43,100) if cli.finish else F(max(r['rho_hi'] for r in rows)).limit_denominator(10**9)
    assert covered>=endpoint
    if cli.finish:assert not state['pending'],'Unfinished target'
    at=datetime.datetime.now(datetime.timezone.utc).isoformat()
    result={'at':at,'kind':'narrowed','target':2,'status':'proof (unaudited)','complete':not state['pending'],'extension_interval':['2/5',str(endpoint)],'combined_theorem_interval':['1/10',str(endpoint)],'accepted_slabs':len(rows),'worst_operator_upper':worst,'worst_operator_upper_hex':worst.hex(),'matrix_sizes':sorted(set(r['x_panels'] for r in rows)),'input_hashes':state['input_hashes'],'table_checkpoints':tables,'witnesses':witnesses,'checks':['Outward endpoint coverage with exact rational arithmetic','All source and table byte hashes','Positive exact binary64 witnesses and stored row maxima','Exact rational verification: total^2 >= finite^2 + full_outside_HS_squared','All total upper bounds strictly below 2'],'limits':'These checks validate the saved certificate and final arithmetic. They do not replace independent review of the kernel identity, analytic reduction, entry enclosures, summation bounds, or whole-complement analytic tail.'}
    output=ROOT/'logs/fine_prefix_validation.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    if cli.finish:
        proof=f'''# T039 target 2: positive three-set simplex range through rho=0.43

Status: computer-assisted proof (unaudited). Independent review is pending.

Theorem. Let n>=2 and let Omega_1, Omega_2, Omega_3 form a measurable partition of R^n with standard Gaussian measures 1/3. For every rho in [1/10,43/100], the sum of their Gaussian rho-noise stabilities is at most that of the standard 120-degree simplex partition, embedded cylindrically for n>2.

Heilman arXiv:2608.00333v1, Theorem A.1, supplies [1/10,2/5]. This calculation supplies the entire interval [2/5,43/100]. The source reduction, circular rearrangement and Corollary A.3 reduce the extension to inequality (146): the weighted mean-zero radial operator must have norm below 2. Corollary A.3 holds for all a>=0. The lower weight bound (153) and the analytic tail require no extra restriction at 2/5; the tail computation here uses rho<1/2.

CELL_BOUND.md derives the unitary radial kernel and positive cell-matrix majorant. ARBITRARY_CENTER.md explains why each saved binary64 quartic additive center leaves the same mean-zero quadratic form. On [0,8]^2, a symmetric nonnegative matrix bounds the operator on all cellwise L2 norms. A strictly positive exact binary64 vector verifies its Collatz upper bound by directed division, multiplication and enclosed summation. Positivity of the original operator is not assumed. BLOCK_COMPLETION.md proves the full-operator bound sqrt(lambda^2+tau), where tau bounds the squared kernel over the entire complement of [0,8]^2, including both cross rectangles. The source analytic_tail routine supplies this complete tail.

The {len(rows)} accepted slabs cover [2/5,43/100]. Radial matrix sizes are {result['matrix_sizes']}. The worst directed upper bound is {worst!r} (hex {worst.hex()}), strictly below 2. The auxiliary integral tables use Arb precision 100, 2048 q cells, 8192 a cells and 64 angular panels; the exponential table has 65536 cells. A possible one-ulp table-domain discrepancy is covered by an additional Arb-enclosed cell, never by clipping an out-of-domain query. All finite truncations and omitted cross regions are enclosed.

This uses radial cells, replacing the suggested Laguerre basis: the source's Theorem 1.6 is about the sphere-valued variational problem, so a direct transfer of that matrix theorem was not assumed. Numerical quadrature only chooses arbitrary admissible centers; power iteration only chooses positive witnesses. Their accuracy is not a premise of the proof. The recorded table and matrix operations, tail, and row sums provide the inequalities.

Reproduction: build each missing stage with python -B -X utf8 scripts/fine_tables.py q (then a, then e); use the per-slab replay script and saved exact centers/witnesses. Each command is limited to a short chunk. Dependency versions, all source hashes, affinity [2,3], one BLAS thread and no RNG are recorded in logs/fine_run_metadata.json. The recorded arrays and binary64 witness data are exact artifacts; source-level independent audit is still required. logs/fine_prefix_validation.json checks byte identities, exact rational coverage and every final squared inequality, rather than asserting a numerical estimate is a bound.
'''
        (ROOT/'proofs/TARGET2_EXTENSION.md').write_text(proof,encoding='utf-8')
        claimfile=ROOT/'CLAIMS.jsonl';old=[json.loads(line) for line in claimfile.read_text(encoding='utf-8').splitlines() if line.strip()]
        existing=[c for c in old if c['id']=='T039-C005' and c.get('proof_file')=='proofs/TARGET2_EXTENSION.md']
        if not existing:
            version=max((c['version'] for c in old if c['id']=='T039-C005'),default=0)+1
            claim={'id':'T039-C005','version':version,'kind':'narrowed','target':2,'statement':'For every n>=2, every balanced measurable three-cell Gaussian partition has rho-noise stability at most the standard simplex partition for every rho in [1/10,43/100]. The new interval [2/5,43/100] is certified by a full-operator bound below 2.','assumptions':['Standard Gaussian measure','Three measurable partition cells, each of measure 1/3','Positive correlation rho in [1/10,43/100]','n>=2'],'status':'proof (unaudited)','proof_file':'proofs/TARGET2_EXTENSION.md','sources':[{'url':'https://arxiv.org/abs/2608.00333v1','locators':['Theorem A.1','Corollary A.3','(146)','(151)-(153)']},{'repository':'https://github.com/sheilman77/cut_bounds','commit':'6b720fe57bfe2a3c8fffc51521d00b31011aa1a3','files':['plur_cert.py','plur_cert_positive.py']},'logs/fine_prefix_validation.json','logs/fine_checkpoint.json','proofs/CELL_BOUND.md','proofs/BLOCK_COMPLETION.md','proofs/ARBITRARY_CENTER.md'],'gap':'Awaiting independent audit of the analytic reduction, interval implementation, and exact claim version. Uses radial cells rather than a direct application of the sphere-valued Laguerre theorem.','audits':[]}
            with claimfile.open('a',encoding='utf-8') as out:out.write(json.dumps(claim)+'\n')
        else:version=existing[-1]['version']
        route={'at':at,'row':'T039','kind':'narrowed','target':2,'route':'Graded radial-cell norm certificate with directed Arb auxiliary tables, positive Collatz witnesses and whole-complement Hilbert-Schmidt completion','status':'done','evidence':['proofs/TARGET2_EXTENSION.md','logs/fine_prefix_validation.json','logs/fine_checkpoint.json'],'result':'Certified operator upper below 2 on [0.40,0.43]; independent audit pending.'}
        with (ROOT/'ROUTES.jsonl').open('a',encoding='utf-8') as out:out.write(json.dumps(route)+'\n')
        with (ROOT/'REPORT.md').open('a',encoding='utf-8') as out:out.write(at+f' | TARGET 2 COMPLETE / UNAUDITED | C005 v{version}: full operator norm <= {worst!r} < 2 over [0.40,0.43]; {len(rows)} slabs. Combined theorem [0.10,0.43]. Radial cells replace the proposed Laguerre basis. Exact validation and all proof files saved.\n')
        status=ROOT/'STATUS.md';lines=status.read_text(encoding='utf-8').splitlines();lines[0]='STATE: NEEDS_REVIEW';lines[1]=f'NEXT: an agent-r / an agent audit C005 v{version}, C004 v2, the full kernel/tail reduction and interval code; target 2 computation is complete through rho=0.43.';lines+=['',at+f' | TARGET 2 COMPLETE / UNAUDITED | rho_1=0.43; operator upper={worst!r}; {len(rows)} accepted slabs.'];status.write_text('\n'.join(lines)+'\n',encoding='utf-8')
        (ROOT/'SUMMARY_TARGET2.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('input_hashes','table_checkpoints','witnesses')},indent=2))
    return 0

if __name__=='__main__':raise SystemExit(main())
