"""Re-fetch source texts without ever writing a PDF to disk.

The final-v3 source uses page-labeled pypdf extraction; other papers use
pdftotext with PDF bytes on stdin and text on stdout. All destinations are
inside this workspace. No failed or inaccessible source is replaced by a
different paper.
"""
import datetime
import io
import subprocess
from pathlib import Path
import requests
from pypdf import PdfReader

SOURCES = {
    'pitman_tang_1411.0041v3': 'https://arxiv.org/pdf/1411.0041v3',
    'pitman_tang_published': 'https://www.columbia.edu/~wt2319/Patterns.pdf?download=1',
    'pitman_tang_slepian_1411.0040': 'https://arxiv.org/pdf/1411.0040',
    'pitman_tang_spans': 'https://arxiv.org/pdf/1506.02021',
    'pitman_tang_argmin': 'https://arxiv.org/pdf/1610.01524',
    'shepp_1971': 'https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/First-passage-time_.pdf',
    'nielsen_1973': 'https://backend.orbit.dtu.dk/ws/files/4640102/PNielsen.pdf',
    'ostaszewska_zajkowski_2013': 'https://arxiv.org/pdf/1302.4859',
    'pozdnyakov_scan_2005': 'https://vladimir-pozdnyakov.github.io/papers/scan.pdf',
    'yoshida_2024': 'https://arxiv.org/pdf/2410.13426',
}


def main():
    Path('sources').mkdir(exist_ok=True)
    for name,url in SOURCES.items():
        r=requests.get(url,headers={'User-Agent':'Mozilla/5.0'},timeout=60)
        r.raise_for_status()
        if not r.content.startswith(b'%PDF'):
            raise ValueError(f'Not a PDF response: {url}')
        if name=='pitman_tang_1411.0041v3':
            pdf=PdfReader(io.BytesIO(r.content))
            text='\n'.join(f'\n===== PDF PAGE {i+1} =====\n'+p.extract_text(extraction_mode='layout') for i,p in enumerate(pdf.pages))
        else:
            text=subprocess.run(['pdftotext','-layout','-','-'],input=r.content,
                                capture_output=True,check=True).stdout.decode()
        Path('sources',name+'.txt').write_text('Source: '+url+'\nRetrieved: '+datetime.datetime.now().isoformat()+'\n\n'+text)
        print(name,len(text),flush=True)


if __name__=='__main__':main()
