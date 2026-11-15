#!/usr/bin/env python3
"""Save the checked primary sources and local text extractions."""
import json
from pathlib import Path
import subprocess
import urllib.request

ROOT=Path(__file__).resolve().parent
SOURCES={
 'tang_thesis':'https://escholarship.org/content/qt51j6244c/qt51j6244c_noSplash_0d298bb720a71e482d931510dcf532d2.pdf',
 'pt_published':'https://www.columbia.edu/~wt2319/Patterns.pdf',
 'argmin':'https://arxiv.org/pdf/1610.01524',
 'spans':'https://arxiv.org/pdf/1506.02021',
 'slepian':'https://arxiv.org/pdf/1411.0040',
}


def main():
    for key,url in SOURCES.items():
        path=ROOT/'src'/f'{key}.pdf'
        try:
            if not path.exists():
                with urllib.request.urlopen(url,timeout=25) as r:data=r.read()
                if not data.startswith(b'%PDF'):raise ValueError('response is not a PDF')
                path.write_bytes(data)
            subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],check=True)
            print(key,'saved',flush=True)
        except Exception as e:print(key,type(e).__name__,str(e),flush=True)


if __name__=='__main__':main()
