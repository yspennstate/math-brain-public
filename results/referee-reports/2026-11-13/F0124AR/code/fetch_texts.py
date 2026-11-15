"""Fetch primary sources, pipe PDF bytes to pdftotext, retain text only.

Custom-font decoding for the 2004/2005 preprint uses its glyph names.
Unrecognized glyphs are explicit markers, not inferred mathematics.
"""
import hashlib
import io
import json
from pathlib import Path
import subprocess
import urllib.request
from pypdf import PdfReader
from pypdf.generic import DecodedStreamObject, NameObject

ROOT=Path(__file__).resolve().parents[1]
ITEMS=[
 ('survey_2006','https://arxiv.org/pdf/math/0608219'),
 ('crossover_2011','https://arxiv.org/pdf/1103.1780'),
 ('bad_configurations_2005','https://www.eurandom.tue.nl/reports/2004/037-report.pdf'),
 ('steif_2020','https://publications.mfo.de/bitstream/handle/mfo/3731/OWR_2020_11.pdf?sequence=4'),
 ('regular_g_not_gibbs_2011','https://arxiv.org/pdf/1106.4188'),
 ('generalized_TT_2022','https://arxiv.org/pdf/2004.07298'),
 ('perfect_simulation_2013','https://arxiv.org/pdf/1103.2058'),
 ('factors_g_2011','https://pure.rug.nl/ws/portalfiles/portal/2548757/2011IndagMathVerbitskiy.pdf'),
 ('den_hollander_publications_2026','https://pub.math.leidenuniv.nl/~hollanderwtfden/PublicationsFdH.pdf'),
]


def clean(text):
    return ''.join(c if c in '\n\t' or ord(c)>=32 else '\n[PAGE BREAK]\n'
                   if c=='\f' else f'[U+{ord(c):04X}]' for c in text)


def decode(raw):
    reader=PdfReader(io.BytesIO(raw))
    touched=set()
    for page in reader.pages:
        for ref in page['/Resources']['/Font'].values():
            font=ref.get_object()
            if id(font) in touched:
                continue
            touched.add(id(font))
            encoding=font.get('/Encoding')
            if encoding is None or '/Differences' not in encoding.get_object():
                continue
            diffs=encoding.get_object()['/Differences']
            code=0
            pairs=[]
            for value in diffs:
                if isinstance(value,int):
                    code=value
                    continue
                glyph=str(value).lstrip('/')
                try:
                    n=int(glyph,36)-360
                    char=chr(n) if 32<=n<=126 else f'[glyph:{glyph}]'
                except ValueError:
                    char=f'[glyph:{glyph}]'
                pairs.append(f'<{code:02X}> <{char.encode("utf-16-be").hex()}>')
                code+=1
            stream=DecodedStreamObject()
            stream.set_data(('/CIDInit /ProcSet findresource begin 12 dict begin begincmap\n'
                             '/CIDSystemInfo << /Registry (Audit) /Ordering (Text) /Supplement 0 >> def\n'
                             '/CMapName /Audit def /CMapType 2 def\n'
                             '1 begincodespacerange <00> <FF> endcodespacerange\n'
                             f'{len(pairs)} beginbfchar\n'+'\n'.join(pairs)+
                             '\nendbfchar\nendcmap CMapName currentdict /CMap defineresource pop end end').encode())
            font[NameObject('/ToUnicode')]=stream
    return '\n\n[PAGE BREAK]\n\n'.join(page.extract_text() for page in reader.pages)


def main():
    manifest=[]
    for name,url in ITEMS:
        path=ROOT/'sources'/f'{name}.txt'
        try:
            raw=urllib.request.urlopen(url,timeout=40).read()
            assert raw.startswith(b'%PDF')
            out=subprocess.run(['pdftotext','-layout','-','-'],input=raw,capture_output=True,check=True).stdout.decode()
            if name=='bad_configurations_2005':
                (ROOT/'sources'/'bad_configurations_2005_raw.txt').write_text(clean(out))
                out=decode(raw)
            out=clean(out)
            path.write_text(out)
            record=dict(name=name,url=url,pdf_bytes=len(raw),pdf_sha256=hashlib.sha256(raw).hexdigest(),
                        text_sha256=hashlib.sha256(out.encode()).hexdigest(),pdf_saved=False)
            print(name,'OK',len(out),flush=True)
        except Exception as e:
            record=dict(name=name,url=url,error=str(e))
            print(name,'FAILED',str(e),flush=True)
        manifest.append(record)
    (ROOT/'data'/'source_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')


if __name__=='__main__':
    main()
