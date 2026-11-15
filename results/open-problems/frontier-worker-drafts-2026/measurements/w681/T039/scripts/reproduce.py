"""Run the unmodified published certificate, with bounded time and saved output."""
import datetime, hashlib, json, os, pathlib, re, subprocess, sys, time

ROOT = pathlib.Path(__file__).resolve().parents[1]
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
import psutil
p = psutil.Process()
p.cpu_affinity([2,3])
mem = psutil.virtual_memory().available
if mem < 2 * 2**30:
    raise SystemExit('Not started: less than 2 GiB available memory.')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
at = datetime.datetime.now(datetime.timezone.utc).isoformat()
import flint, numpy, scipy
metadata = {'at':at,'command':[sys.executable,'-X','utf8','-B','plur_cert_positive.py'],
            'cwd':str(ROOT/'cut_bounds'),'git_commit':'6b720fe57bfe2a3c8fffc51521d00b31011aa1a3',
            'input_hashes':{n:sha(ROOT/'cut_bounds'/n) for n in ('plur_cert.py','plur_cert_positive.py')},
            'python':sys.version,'flint':flint.__version__,'numpy':numpy.__version__,
            'scipy':scipy.__version__,'cpu_affinity':p.cpu_affinity(),
            'thread_caps':{n:os.environ[n] for n in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS')},
            'memory_available_bytes':mem,'rng':'none','seed':None,
            'expected_reproduction':'same 90 accepted slabs, 150 attempts, worst slab [0.38625,0.3875], certified upper 3.99929096609 within 5e-10 (printed 12-digit output and dependency rounding)'}
(ROOT/'logs/reproduction_metadata.json').write_text(json.dumps(metadata,indent=2),encoding='utf-8')
with (ROOT/'BRAIN_USE.jsonl').open('a',encoding='utf-8') as f:
    f.write(json.dumps({'at':at,'query':['Heilman plurality is stablest Hilbert Schmidt','aligned arcs positive correlation operator norm'],
                       'top_ids':['claim_7cfe0cb97825446ec385dca770008621f67993f86cbe7086f2509c7547e67ef2','claim_87f0c619c953e0da4b76039df02e70e2cbd4e04c24b480c0d8c7c7199fbc8abf','claim_0df2aa27785413028ee7a18971cb7a33bfc3618a59a29d3d4e01f04c2f20b66c'],
                       'used':[],'helped':'no','why':'Recall returned general Schmidt and unrelated tilt cards; no Heilman operator or aligned-arc theorem. Primary Appendix A supplies definitions.'})+'\n')
with (ROOT/'SOURCES.jsonl').open('a',encoding='utf-8') as f:
    f.write(json.dumps({'url':'https://github.com/sheilman77/cut_bounds/tree/6b720fe57bfe2a3c8fffc51521d00b31011aa1a3',
                       'file':'cut_bounds/plur_cert_positive.py','sha256':metadata['input_hashes']['plur_cert_positive.py'],
                       'title':'Uniform directed positive correlation certificate','authors':['Steven Heilman'],'year':2026,
                       'what you used it for':'Unmodified target 1(a) certificate; additive center and scaled kernel for targets 1(b,c).'})+'\n')
print('START exact positive certificate, CPU affinity [2,3], thread caps 1; output in logs/reproduction.txt',flush=True)
start=time.perf_counter()
with (ROOT/'logs/reproduction.txt').open('w',encoding='utf-8') as f:
    try:
        rc=subprocess.run(metadata['command'],cwd=ROOT/'cut_bounds',stdout=f,stderr=subprocess.STDOUT,
                          encoding='utf-8',timeout=570).returncode
    except subprocess.TimeoutExpired:
        f.write('\nSTOP: published certificate exceeded bounded 570-second command.\n')
        rc=124
log=(ROOT/'logs/reproduction.txt').read_text(encoding='utf-8')
mt=re.search(r'H_\+\^2 certified\s+([0-9.eE+-]+)',log)
value=float(mt.group(1)) if mt else None
success=(rc==0 and value is not None and abs(value-3.99929096609)<5e-10 and
         'accepted rho slabs             90' in log and 'total slab attempts            150' in log and
         'on [0.3862500000,0.3875000000]' in log)
result={'id':'T039-A','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'kind':'special','target':1,'substep':'a','reproduced':success,'returncode':rc,
        'certified_hs_square_upper':value,'elapsed_seconds':time.perf_counter()-start,
        'log':'logs/reproduction.txt','metadata':'logs/reproduction_metadata.json'}
(ROOT/'logs/reproduction_result.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
with (ROOT/'RESULT_ROWS.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps(result)+'\n')
statement=(f'Unmodified cut_bounds commit {metadata["git_commit"]} reproduces the published positive-rho certificate: h_+^2 <= {value}, worst slab [0.38625,0.3875], 90 accepted slabs / 150 attempts.' if success else
           f'Target 1(a) reproduction failed (exit {rc}); see saved log and dependency metadata. No extension is attempted.')
claim={'id':'T039-C001','version':1,'statement':statement,'assumptions':['Unmodified published script; dependency and command versions in reproduction_metadata.json.'],
       'status':'numerical evidence','proof_file':'logs/reproduction.txt','sources':['2608.00333v1 Appendix A Lemma A.4 p.42','cut_bounds commit '+metadata['git_commit']],
       'gap':'Reproduction of a published certificate, not a new theorem or independent audit.','audits':[], 'kind':'special','target':1}
with (ROOT/'CLAIMS.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(claim)+'\n')
with (ROOT/'REPORT.md').open('a',encoding='utf-8') as f:f.write(f'\n{result["at"]} | T039 1(a) | {statement} Runtime {result["elapsed_seconds"]:.2f}s.\n')
nextline='T039 target 1(b,c): measure HS and the weighted mean-zero operator by refined Nystrom quadrature.' if success else 'T039 target 1(a): reviewer inspect the saved reproduction failure; the brief requires stopping here.'
(ROOT/'STATUS.md').write_text(f'STATE: {"WORKING" if success else "NEEDS_REVIEW"}\nNEXT: {nextline}\n\n{statement}\nRuntime: {result["elapsed_seconds"]:.2f}s.\nrho_HS: not measured.\nrho_op: not measured.\nFirst tested rho with inequality (139) failure: not measured.\n',encoding='utf-8')
print(json.dumps(result),flush=True)
print('\n'.join(log.splitlines()[-15:]),flush=True)
raise SystemExit(0 if success else 1)
