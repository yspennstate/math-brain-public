#!/usr/bin/env python3
import pathlib, subprocess, sys
papers = [
('1206.1460','allez_guionnet'), ('1404.5265','allez_dumaz'),
('1007.3905','li_beta_processes'), ('2204.00736','yabuoku'),
('1408.0632','osada_tanemura_airy'), ('1405.6692','tsai'),
('1108.2291','corwin_hammond'), ('2009.02006','gorin_kleptsyn'),
('2009.04670','valko_virag_zeta'), ('2108.11039','li_valko'),
('2411.10586','huang_zhang'), ('2411.10829','gorin_xu_zhang'),
('2609.26386','assiotis_li'), ('2610.35808','kwak'),
('1609.09011','landon_sosoe_yau')]
root=pathlib.Path(__file__).resolve().parents[1]
for aid,name in papers:
 if (root/'sources'/(name+'_'+aid+'.txt')).exists(): continue
 r=subprocess.run([sys.executable,str(root/'code/fetch_text.py'),'https://arxiv.org/pdf/'+aid,name+'_'+aid],cwd=root)
 if r.returncode: print('FAILED',aid,flush=True)
