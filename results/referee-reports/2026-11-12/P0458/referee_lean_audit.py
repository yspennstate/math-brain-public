"""Inspect the supplied formalization without claiming a local Lean build."""
from pathlib import Path
import re
import shutil

s=Path('code/RootDegree.lean').read_text()
# Strip Lean block comments and line comments before looking for declarations.
clean=re.sub(r'/\-.*?\-/','',s,flags=re.S)
clean=re.sub(r'--[^\n]*','',clean)
print('local Lean executable:',shutil.which('lean'))
print('theorems:',', '.join(re.findall(r'\btheorem\s+(\w+)',clean)))
for keyword in ('sorry','admit','axiom','unsafe'):
    found=bool(re.search(r'\b'+keyword+r'\b',clean))
    print(keyword,'present:',found)
    assert not found
print('The beta_constant statement is rational factorial arithmetic, not an analytic beta-integral statement.')
print('No random graph, conditional probability, weak convergence, or uniform-integrability statement is formalized.')
print('Supplied build transcript:',Path('code/lean_output.txt').read_text().strip().splitlines()[-1])
