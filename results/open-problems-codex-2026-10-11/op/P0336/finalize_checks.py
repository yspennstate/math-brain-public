from pathlib import Path
import xml.etree.ElementTree as E,json
ns={'a':'http://www.w3.org/2005/Atom'};rows=[]
for file in ['arxiv.txt','arxiv_selection.txt','arxiv_specific.txt']:
 x=E.fromstring(Path(file).read_text(encoding='utf8'))
 for e in x.findall('a:entry',ns):
  row={'search_file':file,'title':' '.join(e.findtext('a:title',namespaces=ns).split()),'id':e.findtext('a:id',namespaces=ns),'published':e.findtext('a:published',namespaces=ns),'authors':[a.findtext('a:name',namespaces=ns) for a in e.findall('a:author',ns)],'abstract':' '.join(e.findtext('a:summary',namespaces=ns).split())};rows.append(row)
Path('arxiv_screening.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False),encoding='utf8')
for v in rows:
 if any(t in v['title'].lower() for t in ['consistency','distributional limits','selection','concave','zero-temperature','non-degenerate','from plans to maps']):print(json.dumps(v,ensure_ascii=False))
p=Path('ATTEMPT.md');s=p.read_text(encoding='utf8');s=s.replace('Conditional independence K_z=du dv is a numerical candidate, currently a conjecture.','Conditional independence K_z=du dv was a preliminary numerical candidate; the extended experiment below shows its support is uncertain. No specific kernel is asserted.')
s+='\n## Completed verification record\nLean 4 with Mathlib v4.33.1 checked all three theorems in P0336Checks.lean (excess_identity, height_uncrossing, rank_counterexample), exit code 0, elapsed 117.8 seconds. The first run failed only on a PowerShell UTF-8 BOM; removing the BOM fixed it. The successful run emitted a deprecated-import warning, not a proof error. No sorry, axiom declaration, or native_decide occurs in the file. Proof-producing arithmetic tactics are checked by Lean\'s kernel. These are algebraic/finite certificates; the probabilistic and measure-theoretic proofs above are written proofs, not claimed formally verified.\n\nreferee_check.py exhaustively compared the SciPy excess-cost optimum with all original-distance permutations for n=2,...,7 (5,912 total permutations), and checked all pointwise inequalities, the quartic remainder, and deterministic S_n bounds on the same configurations. All passed. Exact algebra and the written proofs justify the claims; these floating-point checks corroborate them. No proof of empirical horizontal selection has emerged from these checks.\n'
p.write_text(s,encoding='utf8')
