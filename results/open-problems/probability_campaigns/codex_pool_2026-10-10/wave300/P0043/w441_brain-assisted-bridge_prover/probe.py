"""Bounded read-only source and recall probe; all saved files are under w441."""
from pathlib import Path
import json, subprocess, sys, time, urllib.request

ROOT = Path(__file__).resolve().parent

def recall():
    query = 'P0043 critical percolation theorem hypotheses thinning mistakes'
    argv = [sys.executable, '-X', 'utf8', r'~\.claude\dreaming\brain.py', 'recall', query, '-n', '3']
    start = time.perf_counter()
    try:
        result = subprocess.run(argv, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60)
        data = {'query': query, 'command': argv, 'elapsed_seconds': time.perf_counter()-start, 'exit_code': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr}
    except subprocess.TimeoutExpired as exc:
        def decoded(s):
            return s.decode('utf-8', 'replace') if isinstance(s, bytes) else (s or '')
        data = {'query':query,'command':argv,'elapsed_seconds':time.perf_counter()-start,'timeout_seconds':60,'stdout':decoded(exc.stdout),'stderr':decoded(exc.stderr)}
    (ROOT/'REPORT_RECALL.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({k:v for k,v in data.items() if k not in ('stdout','stderr')},ensure_ascii=False))
    print(data['stdout'][:11000])
    print(data['stderr'][:1000])

def source():
    folder = ROOT/'sources'
    folder.mkdir(exist_ok=True)
    url = 'https://raw.githubusercontent.com/openai/math/main/preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/paper.pdf'
    dest = folder/'criticality_2026_09_24.pdf'
    with urllib.request.urlopen(url, timeout=40) as response:
        data = response.read(15_000_001)
    if len(data)>15_000_000:
        raise ValueError('source exceeds 15 MB gate')
    dest.write_bytes(data)
    import importlib.util
    if importlib.util.find_spec('pypdf'):
        from pypdf import PdfReader
        reader = PdfReader(dest)
        pages = [p.extract_text() or '' for p in reader.pages]
    elif importlib.util.find_spec('fitz'):
        import fitz
        with fitz.open(dest) as reader:
            pages = [p.get_text() for p in reader]
    else:
        print(json.dumps({'url':url,'bytes':len(data),'extracted':False}))
        return
    (folder/'criticality_2026_09_24.txt').write_text('\n\n'.join(f'PAGE {i+1}\n{t}' for i,t in enumerate(pages)),encoding='utf-8')
    print(json.dumps({'url':url,'bytes':len(data),'pages':len(pages)}))
    print('\n\n'.join(pages[:2])[:17000])

if __name__=='__main__':
    {'recall':recall,'source':source}[sys.argv[1]]()
