import json
import pathlib

here=pathlib.Path(__file__).resolve().parent
proofs=(here/'PROOFS.md').read_text(encoding='utf-8')
start=proofs.index('## P0177:')
end=proofs.index('## C0004:',start)
general=(here/'P0177_general_global_mode.md').read_text(encoding='utf-8')
body=general.split('\n',1)[1].strip()
lead='## P0177: global-mode estimates under finite variance and seventh moment\n\nThe earlier campaign already derived the classical expansion under an exponential quadratic moment. The following worker proof addresses the free global mode and retains no claim of priority or full-problem acceptance.\n\n'
evidence='\n\nNumerical evidence: special_case_measurements.jsonl contains five compact-law comparisons with the classical expansion; mode_boundary_measurements.json contains twelve point-mass, symmetry, three-atom and zero-third-moment controls. unbounded_mode_measurements.json tests the geometric law with an explicit truncation and seventh-moment tail bound. These computations check coefficients and physical equations; the written argument supplies the noncompact global-maximizer step.\n\n'
(here/'PROOFS.md').write_text(proofs[:start]+lead+body+evidence+proofs[end:],encoding='utf-8')
for filename in ('REPORT.md','AUDIT_REQUEST_w346.md','handoff.py'):
    path=here/filename
    text=path.read_text(encoding='utf-8')
    text=text.replace('21 nodes','22 nodes').replace('21 node','22 node').replace('21 draft','22 draft').replace('21 proposed','22 proposed')
    text=text.replace('23 relations','25 relations').replace('23 quoted','25 quoted').replace('15 written partial lemmas','16 written partial lemmas').replace('15 lemma nodes','16 lemma nodes')
    text=text.replace('==21','==22').replace('10 21 23 ','10 22 25 ').replace('S1.w344.027','S1.w344.028')
    text=text.replace('derive the compact-support free Brownian mode expansion','derive the free Brownian global mode expansion under finite seventh moment')
    text=text.replace('the passage from its stationary point to the global mode','the finite-variance global-maximizer bound, uniform derivative constants, and one-sided C^3 extension')
    path.write_text(text,encoding='utf-8')
rows=[]
for line in (here/'source_audit_rows.jsonl').read_text(encoding='utf-8').splitlines():
    row=json.loads(line)
    number=int(row['row_id'].rsplit('.',1)[1])+1
    row['row_id']=f'S1.w344.{number:03d}'
    rows.append(row)
(here/'source_audit_rows.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in rows),encoding='utf-8')
print(json.dumps({'updated':'P0177 general global-mode proof','node_count':22,'relation_count':25,'last_source_audit_row':'S1.w344.028'}))
