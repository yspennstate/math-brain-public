"""Complete the proposed card correction without touching the source."""
import hashlib
import json
from pathlib import Path

root=Path(__file__).resolve().parent
source=Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/brain_bundle_C001.json')
new_statement=(root/'patches/source_line_after.txt').read_text(encoding='utf-8')
edits=[]
in_entry=False
with source.open(encoding='utf-8') as stream:
    for lineno,line in enumerate(stream,1):
        if '"key": "ising"' in line:
            in_entry=True
        if not in_entry:
            continue
        indent=line[:len(line)-len(line.lstrip())]
        new=None
        field=None
        if line.lstrip().startswith('"title":'):
            field='title'
            new=indent+'"title": '+json.dumps('3D Ising non-triviality: normalized original-current connection proof obligation')+',\n'
        elif line.lstrip().startswith('"statement":'):
            field='statement'
            new=new_statement
        elif 'Nearest-neighbour Ising model on Z^3 at beta_c' in line:
            field='assumptions[0]'
            new=indent+json.dumps('Homogeneous zero-field nearest-neighbour ferromagnetic Ising on Z^3; 0 < beta < beta_c, followed by beta increasing to beta_c; g uses chi(beta)^2 xi_exp(beta)^3')+',\n'
        elif line.lstrip().startswith('"revision":'):
            field='source.revision'
            new=indent+'"revision": '+json.dumps('audit-correction-draft-w469-20261010-v1')+',\n'
        if new is not None:
            edits.append((lineno,field,line,new))
        if line.rstrip() in {'    }','    },'}:
            break
assert {field for _,field,_,_ in edits}=={'title','statement','assumptions[0]','source.revision'}
live=source.as_posix()
patch='--- a/'+live+'\n+++ b/'+live+'\n'
for lineno,field,old,new in edits:
    patch+=f'@@ -{lineno},1 +{lineno},1 @@\n-'+old+'+'+new
    if field=='assumptions[0]':
        json.loads(new.strip().rstrip(','))
    else:
        json.loads('{'+new.strip().rstrip(',')+'}')
(root/'patches/01_c0052_source_criterion.diff').write_text(patch,encoding='utf-8')
check=json.loads((root/'PATCH_CHECK.json').read_text(encoding='utf-8'))
check['patched_fields']=[field for _,field,_,_ in edits]
check['exact_source_line_guards']=[{'line':n,'field':field,'old_line_sha256':hashlib.sha256(old.encode()).hexdigest()} for n,field,old,_ in edits]
check['scope']='Four fields of one proposed source card; no canonical store or source file was modified.'
check['critical_only_assumption_before']=sum('on Z^3 at beta_c' in old for _,_,old,_ in edits)
check['critical_only_assumption_after']=sum('on Z^3 at beta_c' in new for _,_,_,new in edits)
assert check['critical_only_assumption_before']==1 and check['critical_only_assumption_after']==0
(root/'PATCH_CHECK.json').write_text(json.dumps(check,indent=2)+'\n',encoding='utf-8')
report=root/'REPORT.md'
text=report.read_text(encoding='utf-8')
note='The correction also updates the card title, replaces its critical-only beta_c assumption by the subcritical approach used by g, and gives the source a new draft revision. Four fields of one source card are proposed; its original data remain intact.\n\n'
if note not in text:
    report.write_text(text.replace('Apply:',note+'Apply:'),encoding='utf-8')
print(json.dumps({'source_fields':check['patched_fields'],'critical_only_assumption_before':1,'critical_only_assumption_after':0,'syntax':'PASS','live_write':False}))
