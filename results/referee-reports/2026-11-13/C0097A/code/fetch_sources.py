#!/usr/bin/env python3
"""Fetch selected papers as text. PDF bytes stay in memory, never on disk."""
import hashlib, json, pathlib, subprocess, urllib.request
ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCES = {
 'lectures_1206.2092': 'https://arxiv.org/pdf/1206.2092',
 'graham_0911.5163': 'https://arxiv.org/pdf/0911.5163',
 'clisby_liang_slade_2007': 'https://personal.math.ubc.ca/~slade/se.pdf',
 'mejia_miranda_slade_2013': 'https://arxiv.org/pdf/1208.3513',
 'heydenreich_matzke_2022': 'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4F13BE121491D96EFBF8E273B7023D01/S0963548321000365a.pdf/expansion_for_the_critical_point_of_site_percolation_the_first_three_terms.pdf',
}
def main():
    out = ROOT / 'sources'
    out.mkdir(exist_ok=True)
    manifest = []
    for name, url in SOURCES.items():
        path = out / (name + '.txt')
        if not path.exists():
            raw = urllib.request.urlopen(url, timeout=50).read()
            if not raw.startswith(b'%PDF'):
                raise ValueError(f'Expected PDF at {url}')
            result = subprocess.run(['pdftotext','-layout','-','-'], input=raw,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            path.write_bytes(result.stdout)
        txt = path.read_bytes()
        manifest.append(dict(name=name,url=url,text_sha256=hashlib.sha256(txt).hexdigest(),
                             text_bytes=len(txt),conversion='pdftotext -layout - -; PDF input in memory'))
        print(name, len(txt), flush=True)
    (ROOT/'data'/'source_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
if __name__ == '__main__':
    main()
