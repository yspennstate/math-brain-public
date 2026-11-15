"""Repair inline delimiters in the initially drafted prose; leave equations intact."""
from pathlib import Path
import re
p=Path('REPORT.md');s=p.read_text();head,tail=s.split('## 6.',1)
lines=[];display=False
for line in head.splitlines(keepends=True):
    if line.strip()==r'\[':display=True
    if display:
        lines.append(line)
        if line.strip()==r'\]':display=False
        continue
    held=[]
    def hold(m):held.append(m.group(0));return f'@@MATH{len(held)-1}@@'
    line=re.sub(r'\\\(.*?\\\)',hold,line)
    line=line.replace('(O\\)','$O$')
    result='';i=0
    while i<len(line):
        if line[i]=='(' and (i==0 or line[i-1] not in ']\\'):
            end=i+1;depth=1
            while end<len(line) and depth:
                if line[end]=='(':depth+=1
                elif line[end]==')':depth-=1
                end+=1
            if depth==0:
                inside=line[i+1:end-1]
                if not inside.isdigit() and not inside.startswith('http'):
                    result+='$'+inside+'$';i=end;continue
        result+=line[i];i+=1
    for k,value in enumerate(held):result=result.replace(f'@@MATH{k}@@',value)
    lines.append(result)
p.write_text(''.join(lines)+'## 6.'+tail)
