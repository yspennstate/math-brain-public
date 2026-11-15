"""Final report audit: verify source snapshot, numbers, artifacts, math formatting."""
import hashlib
import json
import os
import re
import resource
import signal
import time
from fractions import Fraction as Q
from pathlib import Path

signal.alarm(240)
started=time.monotonic()
report=Path('REPORT.md')
txt=report.read_text()
# The first document-writing call lost some inline TeX delimiters at the JS
# string boundary. Convert their balanced mathematical parentheses to Markdown
# math. Display math and code remain untouched.
lines=[]
display=False
code=False
changes=0
for line in txt.splitlines():
    if line.startswith('```'):
        code=not code
        lines.append(line)
        continue
    if line.strip() in (r'\[',r'\]'):
        display=not display
        lines.append(line)
        continue
    if display or code:
        lines.append(line)
        continue
    # Remove the one damaged trailing delimiter before balancing parentheses.
    line=line.replace('g(i)=1'+chr(92)+')','g(i)=1)')
    chunks=line.split('`')
    for k in range(0,len(chunks),2):
        part=chunks[k]
        out=[]
        pos=0
        while pos<len(part):
            if part[pos]!='(':
                out.append(part[pos]);pos+=1;continue
            end=pos+1
            level=1
            while end<len(part) and level:
                if part[end]=='(':level+=1
                if part[end]==')':level-=1
                end+=1
            if level:
                out.append(part[pos:]);break
            content=part[pos+1:end-1]
            mathematical=(any(c in content for c in ('\\','_','^','=','<','>'))
                          or re.fullmatch(r'[A-Za-z](?:\([^\n]*\))?(?:/[A-Za-z0-9]+)?',content)
                          or content in ('n','q','m','N','t','i','j','u','v','w','x','U','R','J','A','B','D','L','F','P','H'))
            # Plain function notation already lying inside dollars stays alone.
            in_math=''.join(out).count('$')%2==1
            if mathematical and not in_math:
                out.append('$'+content+'$');changes+=1
            else:
                out.append(part[pos:end])
            pos=end
        chunks[k]=''.join(out)
    lines.append('`'.join(chunks))
new='\n'.join(lines)+'\n'
report.write_text(new)
print('inline math delimiters repaired',changes)

snapshot=json.loads(Path('audit_inventory_results.json').read_text())
for file,meta in snapshot['source_snapshot'].items():
    assert hashlib.sha256(Path(file).read_bytes()).hexdigest()==meta['sha256'],file
print('all seven manuscript/code input hashes unchanged')

comb=json.loads(Path('audit_comb_results.json').read_text())
for row in comb['exact']:
    if row['t']=='1000' and row['N']<=3:
        vals=[str(row['N'])]+[f'{float(Q(row[key])):.6f}' for key in ('T','T_hat','mixing_ratio','Mhat_over_M')]
        expected='| '+' | '.join(vals)+' |'
        assert expected in new,expected
print('all four report numerical rows match exact data to six decimals')

# Recover theorem/proposition numbering directly from the source.
counter=0
for line in Path('paper/lumping.tex').read_text().splitlines():
    if re.search(r'\\begin\{(?:theorem|proposition|lemma|remark)\}',line):
        counter+=1
    if r'\label{prop:rankone}' in line:
        assert counter==8
    if r'\label{prop:comb}' in line:
        assert counter==10
print('rank-one proposition is number 8; comb proposition is number 10')

assert 'MAJOR\n'==new[:6]
assert [int(v) for v in re.findall(r'^### (\d+)\.',new,re.M)]==list(range(1,12))
assert new.count(r'\[')==new.count(r'\]')
assert 'g(i)=1'+chr(92)+')' not in new
for line in new.splitlines():
    if not line.startswith('```'):
        assert line.count('$')%2==0, line
for file in ('LOG.md','audit_core.py','audit_random.py','audit_random_output.txt',
             'audit_comb.py','audit_comb_output.txt','audit_comb_results.json',
             'audit_inventory.py','audit_inventory_output.txt','audit_inventory_results.json'):
    assert Path(file).stat().st_size>0,file
assert 'ALL EXACT RANDOM CHECKS PASSED' in Path('audit_random_output.txt').read_text()
assert 'ALL SYMBOLIC AND EXACT COMB CHECKS PASSED' in Path('audit_comb_output.txt').read_text()
print('report structure, math delimiter counts, and all evidence files checked')
try:
    print('inherited_process_nice',os.getpriority(os.PRIO_PROCESS,0))
except (AttributeError,OSError) as e:
    print('niceness unavailable:',type(e).__name__)
elapsed=time.monotonic()-started
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print('FINAL REPORT CHECK PASSED; seconds',elapsed,'peak_rss_bytes',rss)
with open('LOG.md','a') as log:
    log.write('\n## Final report\n\n')
    log.write('- `REPORT.md` completed with verdict MAJOR: two required mathematical corrections, separately identified suggestions, a full proof audit, U(n) through 20, and an explicit to-check list for every unavailable external source. No additional theorem counterexample was found.\n')
    log.write('- `audit_report_check.py` independently checked all source hashes, the four report numerical rows against exact data, proposition numbering, evidence files and report structure. Minor transcription/rounding and inline-formatting errors in the draft report were corrected before delivery.\n')
    log.write(f'- Final check passed in {elapsed:.4f} s, peak RSS {rss} bytes. No original paper file was changed.\n')
