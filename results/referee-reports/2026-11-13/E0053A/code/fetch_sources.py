#!/usr/bin/env python3
"""Download primary sources, preserving source URLs and checksums locally."""
import concurrent.futures, hashlib, json, pathlib, subprocess, urllib.request, time
ROOT=pathlib.Path(__file__).resolve().parents[1]
SOURCES={
'bandeira_notes':'https://people.math.ethz.ch/~abandeira/TenLecturesFortyTwoProblems.pdf',
'bandeira_problem_8_5':'https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-of-data-science-fall-2015/68d66ecf9a66710c9fea20bcb39d886e_MIT18_S096F15_Open8.5.pdf',
'zdeborova_boettcher_2010':'https://arxiv.org/pdf/0912.4861',
'dembo_montanari_sen':'https://arxiv.org/pdf/1503.03923',
'sen_2018':'https://arxiv.org/pdf/1606.02365',
'jagannath_sen':'https://arxiv.org/pdf/1707.09042',
'diaz_do_serna_wormald_2003':'https://users.monash.edu/~normd/documents/Diaz-Do-Serna-Wormald-03.pdf',
'lichev_mitsche':'https://arxiv.org/pdf/2009.00598',
'harangi_2025':'https://arxiv.org/pdf/2506.21296',
'csoka_et_al_2025':'https://arxiv.org/pdf/2509.08531',
'fixed_magnetization_2025':'https://arxiv.org/pdf/2511.16620',
'aronow_lopatto_2026':'https://arxiv.org/pdf/2609.19057',
'coja_oghlan_et_al':'https://eprints.lse.ac.uk/113471/1/Ising_antiferromagnet_revised_clean.pdf',
}
SOURCES.update({
'lyons_fiid':'https://arxiv.org/pdf/1401.4197',
'lyons_erratum':'https://rdlyons.pages.iu.edu/errata/fiid.pdf',
'gamarnik_li':'https://arxiv.org/pdf/1411.1698',
'el_alaoui_montanari_sellke':'https://arxiv.org/pdf/2111.06813',
'sulc_zdeborova':'https://arxiv.org/pdf/0912.3563',
'diaz_do_serna_wormald_author':'https://users.monash.edu.au/~nwormald/papers/bisectionLH.pdf',
'diaz_serna_wormald_2007':'https://users.monash.edu.au/~nwormald/papers/bisdreg.pdf',
'boettcher_percus_2001':'https://arxiv.org/pdf/cond-mat/0104214',
'lichev_mitsche_published':'https://www.combinatorics.org/ojs/index.php/eljc/article/download/v30i2p40/pdf/',
})

def fetch(item):
    name,url=item; path=ROOT/'sources'/f'{name}.pdf'
    try:
        if not path.exists():
            req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (research source check)'})
            with urllib.request.urlopen(req,timeout=60) as r: blob=r.read()
            if not blob.startswith(b'%PDF'): raise ValueError('Not PDF: '+repr(blob[:80]))
            path.write_bytes(blob)
        blob=path.read_bytes()
        subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],check=True)
        return dict(name=name,url=url,file=str(path.relative_to(ROOT)),bytes=len(blob),sha256=hashlib.sha256(blob).hexdigest(),retrieved=time.strftime('%Y-%m-%dT%H:%M:%S%z'))
    except Exception as e: return dict(name=name,url=url,error=str(e))
if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        records=list(pool.map(fetch,SOURCES.items()))
    (ROOT/'sources'/'manifest.json').write_text(json.dumps(records,indent=2)+'\n')
    for row in records: print(row['name'],row.get('bytes',row.get('error')),flush=True)
