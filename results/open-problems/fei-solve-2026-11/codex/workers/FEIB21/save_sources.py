from pathlib import Path
import hashlib,json
items={
 'tree_dnf.py':Path.home()/'fei_solve_agent/code/tree_dnf.py',
 'mc_chain.py':Path.home()/'fei_solve_agent/code/mc_chain.py',
 'experiment.py':Path('../FEIB19/experiment.py'),
 'pm_record_spectrum.npy':Path('../FEIB16/pm_record_spectrum.npy'),
 'pm_prior.json':Path('../FEIB19/pm.json'),
 'FLOW.md':Path.home()/'fei_solve_agent/FLOW.md',
}
Path('inputs').mkdir(exist_ok=True);rows=[]
for name,src in items.items():
 data=src.read_bytes();dst=Path('inputs')/name;dst.write_bytes(data)
 rows.append(dict(source=str(src.resolve()),copy=str(dst),bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
Path('sources.json').write_text(json.dumps(rows,indent=2)+'\n')
