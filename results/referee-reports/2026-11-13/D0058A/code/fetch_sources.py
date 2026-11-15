"""Convert downloaded PDFs in memory to plain text. No PDF is written to disk."""
import os
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
 os.setpriority(os.PRIO_PROCESS, 0, 10)
import subprocess, requests, json, datetime, hashlib
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / 'sources'
PAPERS = {
 'li_zhang_scaling_2024': 'https://arxiv.org/pdf/2411.12189',
 'derrida_annual_2022': 'https://www.college-de-france.fr/sites/default/files/media/document/2022-05/R%C3%A9sum%C3%A9%20annuel%202018-2019%20%28Derrida%29.pdf',
 'derrida_annual_2023': 'https://www.college-de-france.fr/sites/default/files/media/document/2023-03/059_066_P2_Derrida.pdf',
 'johnson_junge_lyu_sivakoff_2023': 'https://arxiv.org/pdf/2005.06018',
 'vrjp_2024': 'https://arxiv.org/pdf/2309.01221',
 'chen_dagard_derrida_shi_2020': 'https://arxiv.org/pdf/2001.00853',
 'pain_thesis_summary_2019': 'https://www.math.univ-toulouse.fr/~mpain/pdf/resume_these.pdf',
 'collet_et_al_preprint_1983': 'https://cds.cern.ch/record/149004/files/198401132.pdf',
 'chen_hu_shi_2021_sustainability': 'https://arxiv.org/pdf/2108.05610',
 'hu_shi_2018': 'https://arxiv.org/pdf/1705.03792',
 'hu_mallein_pain_2020': 'https://arxiv.org/pdf/1811.08749',
 'derrida_retaux_2014': 'https://arxiv.org/pdf/1401.6919',
 'derrida_shi_2020': 'https://arxiv.org/pdf/2005.10208',
 'chen_2024_2026': 'https://arxiv.org/pdf/2405.09741',
 'li_zhang_2024_2025': 'https://arxiv.org/pdf/2411.13068',
 'alsmeyer_hu_mallein_2025': 'https://arxiv.org/pdf/2502.02991',
 'duquesne_shi_2026': 'https://arxiv.org/pdf/2609.11435',
 'lotnikov_kotova_2025': 'https://arxiv.org/pdf/2502.02535',
 'collet_et_al_1984': 'https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-94/issue-3/Study-of-the-iterations-of-a-mapping-associated-to-a/cmp/1103941233.pdf',
 'chen_et_al_2017_v1': 'https://arxiv.org/pdf/1705.04787v1',
 'chen_et_al_2019_v2': 'https://arxiv.org/pdf/1705.04787v2',
 'chen_et_al_2021': 'https://arxiv.org/pdf/1907.01601',
 'chen_shi_2020': 'https://arxiv.org/pdf/2006.06140',
 'chen_hu_shi_2023': 'https://arxiv.org/pdf/2306.12717',
}
if __name__ == '__main__':
 import sys
 selected = sys.argv[1:]
 for name, url in PAPERS.items():
  if selected and name not in selected: continue
  try:
   r=requests.get(url,timeout=90); r.raise_for_status()
   if not r.content.startswith(b'%PDF'): raise ValueError('not PDF')
   p=subprocess.run(['pdftotext','-layout','-','-'],input=r.content,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
   header=f'SOURCE: {url}\nRETRIEVED: {datetime.datetime.now().isoformat()}\nPDF SHA256 (bytes never saved): {hashlib.sha256(r.content).hexdigest()}\nPage boundaries: form-feed characters.\n\n'
   (SOURCES/(name+'.txt')).write_text(header+p.stdout.decode())
   print(name,len(r.content),len(p.stdout),flush=True)
  except Exception as e: print(name,type(e).__name__,str(e),flush=True)
