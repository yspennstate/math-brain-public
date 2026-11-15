"""Hash the finished research artifacts and record software versions."""
from pathlib import Path
import hashlib,json,platform,sys
import numpy,scipy,sympy,mpmath
root=Path(__file__).resolve().parent
files=list(root.glob('*.py'))+[root/f for f in ['REPORT.md','LOG.md','MEMORY_NOTE.md','dpp.cpp','libdpp.dylib']]
files+=list((root/'data').glob('*'))+list((root/'sources').glob('*'))+list(root.glob('*_run.log'))
records={}
for f in sorted(set(files)):
 if f.is_file():
  records[str(f.relative_to(root))]={'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'bytes':f.stat().st_size}
out={'python':sys.version,'platform':platform.platform(),'packages':{m.__name__:m.__version__ for m in (numpy,scipy,sympy,mpmath)},'files':records}
(root/'artifact_manifest.json').write_text(json.dumps(out,indent=2)+'\n')
print('hashed',len(records),'research artifacts')
