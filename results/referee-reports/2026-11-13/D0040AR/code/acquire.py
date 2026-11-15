"""Fetch primary papers; PDF bytes exist only in memory and pdftotext pipes."""
import datetime
import hashlib
import json
import pathlib
import subprocess
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPERS = {
    'virag': 'https://arxiv.org/pdf/1804.06953',
    'dumitriu_edelman': 'https://arxiv.org/pdf/math-ph/0206043',
    'killip_nenciu': 'https://arxiv.org/pdf/math/0410034',
    'dumitriu_forrester': 'https://arxiv.org/pdf/0904.2216',
    'borodin_gorin': 'https://arxiv.org/pdf/1305.3627',
    'assiotis': 'https://arxiv.org/pdf/1609.03764',
    'forrester_rains': 'https://arxiv.org/pdf/math-ph/0211042',
    'edelman_sutton': 'https://math.mit.edu/~edelman/publications/beta-jacobi.pdf',
    'assiotis_najnudel': 'https://arxiv.org/pdf/1905.08684',
    'kawamoto_shibukawa': 'https://arxiv.org/pdf/2505.23139',
    'gorin_shkolnikov': 'https://arxiv.org/pdf/1401.5595',
    'sun': 'https://arxiv.org/pdf/1609.09096',
    'virtual_isometries': 'https://arxiv.org/pdf/1102.2633',
    'budway_shkolnikov': 'https://arxiv.org/pdf/2403.10724',
    'nakano_trinh_trinh': 'https://arxiv.org/pdf/2601.13674',
    'petrov_xu': 'https://arxiv.org/pdf/2607.27810',
    'neretin': 'https://www.esi.ac.at/preprints/esi1262.pdf',
    'valko_virag_circular': 'https://arxiv.org/pdf/1710.06988',
    'valko_virag_sine': 'https://arxiv.org/pdf/1604.04381',
    'krishnapur_rider_virag': 'https://arxiv.org/pdf/1306.4832',
    'gorin_marcus': 'https://arxiv.org/pdf/1706.07393',
    'kawamoto_shibukawa_journal': 'https://alea.impa.br/articles/v23/23-10.pdf',
    'breuer_forrester_smilansky': 'https://arxiv.org/pdf/math-ph/0507036',
}

def main():
    index = ROOT / 'sources' / 'retrieval.json.txt'
    manifest = json.loads(index.read_text()) if index.exists() else {}
    for name, url in PAPERS.items():
        target = ROOT / 'sources' / (name + '.txt')
        if target.exists():
            if name not in manifest:
                import re
                existing = target.read_text()
                manifest[name] = {'url': url, 'pages': existing.count('=== PDF PAGE'),
                                  'sha256_pdf': re.search(r'PDF SHA256: (\w+)', existing)[1],
                                  'sha256_text': hashlib.sha256(existing.encode()).hexdigest()}
                index.write_text(json.dumps(manifest, indent=2))
            continue
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Independent referee source verification'})
            with urllib.request.urlopen(req, timeout=45) as response:
                raw = response.read(12_000_000)
            if not raw.startswith(b'%PDF'):
                raise ValueError('Response is not PDF')
            converted = subprocess.run(['pdftotext', '-layout', '-', '-'], input=raw,
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout.decode()
            pages = converted.split('\f')
            if not pages[-1].strip():
                pages.pop()
            text = f'Source: {url}\nRetrieved: {datetime.datetime.now().astimezone().isoformat()}\nPDF SHA256: {hashlib.sha256(raw).hexdigest()}\n'
            text += '\n'.join(f'\n=== PDF PAGE {i} ===\n{p}' for i, p in enumerate(pages, 1))
            target.write_text(text)
            manifest[name] = {'url': url, 'pages': len(pages), 'sha256_pdf': hashlib.sha256(raw).hexdigest(), 'sha256_text': hashlib.sha256(text.encode()).hexdigest()}
            print(name, len(pages), flush=True)
        except Exception as error:
            manifest[name] = {'url': url, 'error': str(error)}
            print(name, 'ERROR', str(error), flush=True)
        (ROOT / 'sources' / 'retrieval.json.txt').write_text(json.dumps(manifest, indent=2))

if __name__ == '__main__':
    main()
