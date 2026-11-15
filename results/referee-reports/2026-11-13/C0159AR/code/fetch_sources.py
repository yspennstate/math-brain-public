"""Fetch primary papers and extract text via stdin; no PDF is written."""
import hashlib, json, os, subprocess, time, urllib.request
from pathlib import Path
os.environ.update(OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1')
ROOT = Path(__file__).resolve().parents[1]
PAPERS = {
'bcrtt_v1':'https://arxiv.org/pdf/2509.10631v1',
'bcrtt_v2':'https://arxiv.org/pdf/2509.10631v2',
'timar_neighboring':'https://arxiv.org/pdf/math/0702873',
'hps':'https://www.math.ucla.edu/~rhs/papers/hps.pdf',
'hutchcroft_hyperbolic':'https://arxiv.org/pdf/1804.10191',
'hutchcroft_nonunimodular':'https://arxiv.org/pdf/1711.02590',
'tang':'https://arxiv.org/pdf/1809.01284',
'timar_nonunimodular':'https://arxiv.org/pdf/math/0702875',
'terlov_timar':'https://arxiv.org/pdf/2502.02560v2',
'spakulova':'https://arxiv.org/pdf/0801.4153',
'menard_senizergues':'https://arxiv.org/pdf/2611.09762v1',
'survey':'https://arxiv.org/pdf/math/0612812',
'peres_pete_scolnicov':'https://arxiv.org/pdf/math/0501532',
'hermon_hutchcroft':'https://arxiv.org/pdf/1904.10448',
'hutchcroft_pan_dimension':'https://arxiv.org/pdf/2412.15895',
'hutchcroft_pan_subgroup':'https://arxiv.org/pdf/2409.12283',
}
def main():
    metadata = []
    for name, url in PAPERS.items():
        dest = ROOT/'sources'/f'{name}.txt'
        if dest.exists():
            print(name, 'already saved', flush=True)
            continue
        try:
            req = urllib.request.Request(url, headers={'User-Agent':'Independent mathematical referee (source text extraction)'})
            with urllib.request.urlopen(req, timeout=50) as response:
                blob = response.read(20_000_000)
                final = response.url
            if not blob.startswith(b'%PDF'):
                raise ValueError('response is not PDF')
            proc = subprocess.run(['pdftotext','-layout','-','-'], input=blob, capture_output=True, check=True)
            body = proc.stdout.decode('utf-8').replace('\x00','')
            sha = hashlib.sha256(blob).hexdigest()
            header = f'SOURCE: {url}\nRESOLVED: {final}\nPDF SHA256: {sha}\nFETCHED: {time.strftime("%Y-%m-%d %H:%M:%S %z")}\nExtraction: pdftotext -layout via stdin/stdout; form feed separates PDF pages.\n\n'
            dest.write_text(header+body)
            metadata.append({'name':name,'url':url,'pdf_sha256':sha,'pdf_bytes_memory_only':len(blob),'text_bytes':dest.stat().st_size})
            print(name, len(blob), len(body), 'OK', flush=True)
        except Exception as error:
            print(name, 'ERROR', repr(error), flush=True)
            metadata.append({'name':name,'url':url,'error':repr(error)})
    with (ROOT/'sources'/'DOWNLOADS.txt').open('a') as out:
        out.write(json.dumps(metadata, indent=2)+'\n')
if __name__ == '__main__':
    main()
