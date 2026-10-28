from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
source=R.parent/'20261023T025441Z-account03-A078-coding-and-padding/code/independent.py'
s=source.read_text(encoding='utf-8');a=s.index('def plus(');b=s.index('profiles=')
prefix='from fractions import Fraction as F\nfrom itertools import product\nfrom functools import lru_cache\nfrom pathlib import Path\nimport json,time,hashlib\n'
(R/'code/direct.py').write_text(prefix+s[a:b],encoding='utf-8')
(R/'out/INDEPENDENT_ARITHMETIC_SOURCE.json').write_text(json.dumps({'path':str(source),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'extracted_start':a,'extracted_end':b,'scope':'prime-log24 and direct character sums only; no primary checker imports'},indent=2),encoding='utf-8')
