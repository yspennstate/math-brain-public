"""Validate a different counterexample detector; no producer imports."""
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path

root=Path(__file__).resolve().parents[1]
# Import only the separately checked direct-character arithmetic definitions.
# The verifier main routine is guarded; no Bellman recurrence or prior test reruns.
spec=importlib.util.spec_from_file_location('own_certificate_verifier',root/'code'/'verify.py')
v=importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
bank=json.loads((root/'out'/'main_certificates.json').read_text(encoding='utf-8'))['bank']
point=(-1,1,1,1)
nonconstant=constant=0
selected={'whole':0,'first':0,'second':0}
for row in bank:
    B,f=tuple(row['outer']),tuple(row['first'])
    F=tuple(B[int(x==1)+2*int(y==1)] for y in point for x in f)
    H,I=v.observable(F)
    Hf,If=v.observable(f)
    Hg,Ig=v.observable(point)
    qf=Q(sum(B[2*int(y==1)]!=B[1+2*int(y==1)] for y in point),len(point))
    qg=Q(sum(B[int(x==1)]!=B[2+int(x==1)] for x in f),len(f))
    W=v.combine(v.times(Hf,qf),v.times(Hg,qg))
    C=v.difference(H,W)
    A=v.load_form(row['A'])
    # Source A has signed C. Add precisely (-C)_+ to form clipped bank.
    clip=A if v.nonnegative(C) else v.difference(A,C)
    if not I:
        v.require(clip==(),'zero-influence whole has no bank')
        constant+=1
        continue
    choices=[('whole',v.times(H,1/I))]
    if qf*If:
        choices.append(('first',v.times(Hf,1/If)))
    if qg*Ig:
        choices.append(('second',v.times(Hg,1/Ig)))
    best=choices[0]
    for candidate in choices[1:]:
        if v.nonnegative(v.difference(candidate[1],best[1])):
            best=candidate
    lower=v.difference(v.times(clip,1/I),v.rational(6))
    v.require(v.nonnegative(v.difference(best[1],lower)),'actual Boolean whole-or-core extracted ratio')
    selected[best[0]]+=1
    nonconstant+=1
summary={'status':'PASS','clipped_bank_rows':len(bank),'nonconstant_rows':nonconstant,'constant_rows':constant,'selected_actual_functions':selected,'method':'Actual whole/core selection using direct-character spectra and exact integer comparisons','separate_verifier_reexecuted':False,'external_review':'PENDING'}
(root/'out'/'extraction_summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary),flush=True)
