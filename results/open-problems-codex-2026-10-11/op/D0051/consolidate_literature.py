import pathlib,xml.etree.ElementTree as E,json
R=pathlib.Path(__file__).resolve().parent
n={'a':'http://www.w3.org/2005/Atom'}
rows=[]
for name in ['arxiv','arxiv_targeted','arxiv_kpz','arxiv_boundary']:
 root=E.parse(R/(name+'.response'))
 for e in root.findall('a:entry',n):
  rows.append({'query':name,'id':e.find('a:id',n).text,'title':e.find('a:title',n).text.strip().replace('\n',' '),'authors':[a.find('a:name',n).text for a in e.findall('a:author',n)],'abstract':e.find('a:summary',n).text.strip(),'published':e.find('a:published',n).text})
(R/'arxiv_results.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
with (R/'LITERATURE.md').open('a',encoding='utf8') as f:
 f.write('\n## Complete dated HTTP search/download ledger\n\n')
 for line in (R/'search_log.jsonl').read_text(encoding='utf8').splitlines():
  x=json.loads(line);f.write('- '+x.get('date','')+'; '+x['service']+'; `'+x['url']+'`; '+str(x.get('status',x.get('error','')))+'\n')
 f.write('\nAll arXiv hits, titles, authors, dates and abstracts retained in arxiv_results.json. The broad search is noisy (many unrelated geometry/astrophysics hits); the Liouville-targeted query supplies the relevant recent candidates.\n')
 f.write('\nChunhao Cai, Closed Response Calculus and Joint Densities for the Liouville Quantum Gravity Metric, arXiv:2609.27861v1 (PDF displays 20 August 2026). Retrieved response_calculus.pdf. Main results concern a closed response calculus and densities for logarithmic distance ratios indexed by finite forests; neither a thick-point intersection spectrum nor its optimizer is computed. Not a solution to D0051.\n')
 f.write('\nAdditional leads from targeted arXiv: Zherui Fan and Subhajit Goswami, Roughness of geodesics in Liouville quantum gravity, arXiv:2205.00676v1; Bhatia–Kavvadias, Strong confluence of geodesics in Liouville quantum gravity, arXiv:2512.09219v2; Ding–Gwynne, Regularity and confluence of geodesics for the supercritical Liouville quantum gravity metric, arXiv:2104.06502v4; Dimension lower bounds in random geometry via Lipschitz functions, arXiv:2606.10496v1. Their retrieved abstracts concern roughness, confluence or other sets, not an evaluation of the requested spectrum. No results from these papers are assumed in the proofs here.\n')
# Correct an earlier checkpoint misnumber: no erroneous theorem attribution retained.
p=R/'LITERATURE.md';s=p.read_text(encoding='utf8').replace('Theorem 1.6 is a thickness dimension conversion for arbitrary sets but defines thick points by an actual limit.','Propositions 2.2 and 2.5 give the thickness dimension conversion for arbitrary sets, but define thick points by an actual limit.')
p.write_text(s,encoding='utf8')
print('Saved parsed hits and complete search ledger.')
