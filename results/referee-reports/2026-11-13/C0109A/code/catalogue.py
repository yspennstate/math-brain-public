from pathlib import Path
import re,json
patterns={
 'tao_vu_0810.2994v3':['6. Open problems','Circular Law.','[54]'],
 'tao_vu_0708.2895':['Theorem 1.2 (','14. Rate of Convergence','(54)','Remark 14.1'],
 'gotze_tikhomirov_0709.3995':['Theorem 1.1.','Theorem 1.2.'],
 'gotze_jalowy_1807.00489v3':['Definition 2.','Proposition 3','Proposition 4','Theorem 5.','Theorem 6.','Theorem 7.','Theorem 8.','2.3. Discussion'],
 'jalowy_products_1912.09300':['Theorem 3.','Theorem 4.','Definition 5','Theorem 6.','Corollary 7.'],
 'jalowy_wasserstein_2111.03595v3':['Theorem 1.','Corollary 2.','Theorem 3.','Lemma 5.'],
 'bourgade_yau_yin_1206.1449v3':['Theorem 2.2','subexponential'],
 'alt_erdos_kruger_1612.07776':['(B) All entries','Theorem 2.5 ('],
 'tao_vu_local_1206.1893':['Theorem 20 (','Theorem 25 (','Condition C1'],
 'cipolloni_erdos_schroder_1912.04100':['Assumption 2.1.','Theorem 2.2 ('],
 'bcct_1607.05484':['Theorem 1.3.'],
 'bordenave_chafai_garcia_2012.05602v2':['Theorem 1.1 (']}
with Path('sources/reading_notes.txt').open('w') as out:
 for name,needles in patterns.items():
  pages=Path('sources/'+name+'.txt').read_text().split('\f')
  out.write('\n===== '+name+' =====\n')
  for needle in needles:
   for num,page in enumerate(pages,1):
    if needle in page:
     pos=page.index(needle)
     out.write(f'\nPDF page {num}, literal search {needle!r}:\n'+page[max(0,pos-80):pos+1700]+'\n')
     break
