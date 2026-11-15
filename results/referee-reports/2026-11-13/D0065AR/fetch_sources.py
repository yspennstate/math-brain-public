"""Independent primary-source retrieval: no binary files are written."""
import os
try:
    os.nice(10)
except PermissionError:
    if os.getpriority(os.PRIO_PROCESS, 0) < 10:
        raise
os.environ.update(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
import io, json, hashlib, time, subprocess
from pathlib import Path
import requests
from pypdf import PdfReader

PAPERS = {
 'rhodes_vargas_arxiv': 'https://arxiv.org/pdf/1305.6221',
 'madaule_arxiv': 'https://arxiv.org/pdf/1307.1365',
 'madaule_published': 'https://www.numdam.org/item/10.1214/14-AIHP633.pdf',
 'ding_roy_zeitouni': 'https://arxiv.org/pdf/1503.04588',
 'bramson_ding_zeitouni': 'https://arxiv.org/pdf/1301.6669',
 'biskup_louidor_extreme': 'https://arxiv.org/pdf/1306.2602',
 'biskup_louidor_conformal': 'https://arxiv.org/pdf/1410.4676',
 'acosta': 'https://arxiv.org/pdf/1311.2000',
 'drsv_derivative': 'https://arxiv.org/pdf/1206.1671',
 'drsv_renormalization': 'https://arxiv.org/pdf/1212.0529',
 'junnila_saksman': 'https://arxiv.org/pdf/1506.05099',
 'junnila_saksman_webb': 'https://arxiv.org/pdf/1808.06838',
 'powell': 'https://arxiv.org/pdf/1704.06058',
 'schweiger_zeitouni': 'https://arxiv.org/pdf/2205.07210',
 'lacoin': 'https://arxiv.org/pdf/2209.06683',
 'ganguly_nam': 'https://arxiv.org/pdf/2302.03010',
 'aidekon_shi': 'https://arxiv.org/pdf/1102.0217',
 'ding_gwynne_zhuang': 'https://arxiv.org/pdf/2310.03996',
 'paquette_zeitouni': 'https://arxiv.org/pdf/2209.06743',
 'acosta_thesis': 'https://conservancy.umn.edu/server/api/core/bitstreams/2cb19574-ecbc-49e6-a075-e8eb09437317/content',
 'biskup_survey': 'https://arxiv.org/pdf/1712.09972',
 'bertacco_hairer_uniqueness': 'https://arxiv.org/pdf/2504.07552',
 'bertacco_hairer_extremal': 'https://arxiv.org/pdf/2504.06956',
 'schweiger_membrane': 'https://arxiv.org/pdf/1903.02522',
 'xie_2026': 'https://arxiv.org/pdf/2606.19207',
 'rhodes_vargas_published': 'https://ftp.icm.edu.pl/packages/EMIS/journals/PS/images/getdoc25a8.pdf?article=218&id=1036&mode=pdf',
 'biskup_louidor_conformal_final': 'https://www.math.ucla.edu/~biskup/PDFs/papers/GFF-General-final.pdf',
 'junnila_saksman_webb_published': 'https://acris.aalto.fi/ws/portalfiles/portal/40601990/SCI_Junnila_et.al_Decompositions.AAP1492_1.pdf',
 'paquette_zeitouni_published': 'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2DBD96407247AA6166F4AEA93319FF0E/S2050509424001294a.pdf/extremal_landscape_for_the_cbeta_e_ensemble.pdf',
 'acosta_published': 'https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/3170/3170-18890-1-PB.pdf',
}

def main():
    out = Path('sources'); out.mkdir(exist_ok=True)
    manifest_path = out / 'manifest.txt'
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    for name, url in PAPERS.items():
        target = out / (name + '.txt')
        if target.exists():
            continue
        try:
            r = requests.get(url, timeout=90); r.raise_for_status()
            if not r.content.startswith(b'%PDF'):
                raise ValueError('Response is not a PDF: ' + r.headers.get('Content-Type',''))
            rawtext = subprocess.run(['pdftotext','-layout','-','-'],input=r.content,capture_output=True,check=True).stdout.decode('utf-8')
            pages = rawtext.split('\f')
            if not pages[-1].strip(): pages.pop()
            text = '\n\n'.join(f'===== PDF PAGE {i+1} =====\n' + page for i,page in enumerate(pages))
            target.write_text('SOURCE: ' + url + '\nRETRIEVED: 2026-11-13\n\n' + text)
            manifest[name] = dict(url=url, pages=len(pages), sha256=hashlib.sha256(r.content).hexdigest(), text_sha256=hashlib.sha256(target.read_bytes()).hexdigest())
            print(name, len(pages), 'pages', flush=True)
        except Exception as exc:
            manifest[name] = dict(url=url, error=str(exc))
            print(name, 'ERROR', str(exc), flush=True)
        manifest_path.write_text(json.dumps(manifest, indent=2)+'\n')

if __name__ == '__main__': main()
