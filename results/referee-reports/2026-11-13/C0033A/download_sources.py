"""Download primary sources, with stable local filenames and URL manifest."""
from pathlib import Path
import urllib.request,json,subprocess,hashlib
p=Path(__file__).resolve().parent/'sources';p.mkdir(exist_ok=True)
sources={
 'lyons_2003':'https://www.numdam.org/item/10.1007/s10240-003-0016-0.pdf',
 'gu_dpp':'https://sevenkplus.com/data/dpp.pdf',
 'lyons_2014':'https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf',
 'lyons_steif_2003':'https://rdlyons.pages.iu.edu/pdf/dyn.pdf',
 'kulesza_taskar_2012':'https://arxiv.org/pdf/1207.6083',
 'meszaros_2020':'https://real.mtak.hu/112304/2/1905.pdf',
 'alishahi_barzegar_2021':'https://arxiv.org/pdf/2006.13923',
 'hillion_johnson_2017':'https://arxiv.org/pdf/1503.01570',
 'hino_yano_2025':'https://arxiv.org/pdf/2404.11024',
 'ercan_2026':'https://arxiv.org/pdf/2611.00626',
}
manifest={}
for name,url in sources.items():
    try:
        target=p/(name+'.pdf')
        with urllib.request.urlopen(url,timeout=45) as r:target.write_bytes(r.read())
        subprocess.run(['pdftotext','-layout',str(target),str(p/(name+'.txt'))],check=True)
        manifest[name]={'url':url,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'status':'downloaded'}
    except Exception as e:manifest[name]={'url':url,'error':str(e)}
    print(name,manifest[name],flush=True)
(p/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
