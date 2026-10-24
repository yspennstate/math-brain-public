from pathlib import Path
import sys,importlib.util,json
r=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('lc',r'~\.claude\dreaming\lean_check.py');m=importlib.util.module_from_spec(spec);sys.path.insert(0,str(Path(spec.origin).parent));spec.loader.exec_module(m)
p=r/'code'/'SignedRecovery.lean'
a=m.check_source(p.read_bytes(),timeout=35,source_path=p,output_root=r/'out'/'lean',use_mathlib=False)
(r/'out'/'LEAN.json').write_text(json.dumps(a,indent=2),encoding='utf-8');print(json.dumps(a))
