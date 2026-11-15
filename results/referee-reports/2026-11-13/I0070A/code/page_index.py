"""Locate numbered results in the saved source texts."""
from pathlib import Path
import re, json
root=Path(__file__).resolve().parents[1]
queries={
 'survey_published':['Assumption 4.1.', 'Theorem 4.7.', 'Theorem 5.7.', 'Proposition 5.9.', 'Assumption 6.1.', 'Theorem 6.2.', 'Theorem 6.4.', 'Problem 6.', 'Theorem 3.13.', 'Proposition 3.11.'],
 'survey_v5':['Theorem 5.7 (', 'Assumption 6.1.', 'Problem 6 ('],
 'critical_I':['Theorem 4.8 (Semilinear)', 'Proposition 3.10.', 'Proposition 3.12.'],
 'critical_II_published':['Theorem 4.15', 'Theorem 6.3', 'Corollary 6.5', 'Proposition 6.8'],
 'critical_variational':['Assumption 3.1', 'Theorem 3.3 (', 'Theorem 3.4 (', 'Theorem 3.5 (', 'Theorem 3.8 (', 'Lemma 4.1 ('],
 'rough_time':['Lemma 2.7', 'Theorem 3.9', 'Theorem 4.5', 'Theorem 5.3'],
 'liu_rockner_2010':['Theorem 1.1.', 'Theorem 4.1.'],
 'navier_stokes':['Theorem 2.4', 'Theorem 4.1', 'Part (C)', 'Step 1:'],
 'temporal_threshold_v3':['Theorem 1.1 (', 'Theorem 1.3.'],
 'temporal_threshold_published':['Theorem 1 (', 'Theorem 3.'],
 'singular_times_2026':['Lemma 3.11 ('],
 'reaction_2026_v3':['Theorem 4.8 (Temporal', 'Theorem 2.12 (']}
results={}
for name, qs in queries.items():
 text=(root/'sources'/f'{name}.txt').read_text()
 out={}
 for q in qs:
  hits=[]
  for m in re.finditer(re.escape(q),text):
   pg=list(re.finditer(r'===== PDF PAGE (\d+) =====',text[:m.start()]))
   hits.append(int(pg[-1].group(1)) if pg else 0)
  out[q]=sorted(set(hits))
 results[name]=out
print(json.dumps(results, indent=2))
(root/'data'/'page_index.json').write_text(json.dumps(results,indent=2)+'\n')
