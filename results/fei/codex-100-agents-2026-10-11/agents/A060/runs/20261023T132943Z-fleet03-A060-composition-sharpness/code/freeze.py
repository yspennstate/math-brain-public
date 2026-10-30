from pathlib import Path
import json,hashlib
A=Path(__file__).resolve().parents[3];ROOT=Path(__file__).resolve().parents[1];B=A.parents[1]
spec={'helper_version':'check.py v1; exact.py inherited P180100-term outward logs','actual_Boolean_family':'all Boolean2 pilot; all Boolean3 cores; all16 exterior two-bit sign tables with a point mask; matched m4 source/AND3 with every ternary exterior restriction; rare-tag reset family m4,8,12; direct character reproduction','domain':'pilot32 core edges; main768 core edges;4096 wrapper roots/12288 core edges;972 reached source profiles/1944 extra-core edges;one full128-leaf tree;3 fixed reset dimensions;64 direct reproduction roots','case_count':{'pilot':32,'core':768,'wrapper_edges':12288,'source_profiles':972,'source_edges':1944,'direct_roots':64},'symmetry':'none (redundant exterior truth values on the erased point intentionally retained)','arithmetic':'Fraction Fourier and physical edges; rigorous180-bit natural log intervals with proved positive-series tail; exact integer endpoint3^3<2^5; decimal display only','memory_estimate_MB':120,'max_runtime_seconds_per_job':55,'automatic_dimension_escalation':False,'no_GPU':True}
(ROOT/'FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8',newline='')
paths=[B/'BOARD.md',B/'claude/B12/STREAM_NOTES.md',A/'STATUS.md',Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')]
paths += [B/'agents/A059/runs/20261023T130150Z-fleet03-A059-decomposition-depth'/n for n in ['PROOF.md','CLAIMS.json','REVIEW.md']]
paths += [B/'agents/A057/runs/20261023T120547Z-fleet03-A057-coherent-restriction-remainder'/n for n in ['PROOF.md','FULL_EXTERIOR.md','CLAIMS.json']]
paths += [B/'agents/A091/runs/20261023T115216Z-fleet03-A091-composition-referee/CLAIMS.json']
pins=[]
for i,p in enumerate(paths):
 raw=p.read_bytes();out='out/SOURCE_'+str(i)+'_'+p.name;(ROOT/out).write_bytes(raw)
 pins.append({'path':str(p),'copy':out,'sha256':hashlib.sha256(raw).hexdigest()})
(ROOT/'out/SOURCES.json').write_text(json.dumps(pins,indent=2),encoding='utf-8',newline='')
old=A/'runs/20261023T112129Z-fleet03-A060-composition-sharpness/code/exact.py'
(ROOT/'code/exact.py').write_bytes(old.read_bytes())
print('Frozen spec and',len(pins),'source snapshots; helper sha256',hashlib.sha256((ROOT/'code/check.py').read_bytes()).hexdigest())
