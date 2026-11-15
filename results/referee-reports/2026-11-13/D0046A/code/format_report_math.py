#!/usr/bin/env python3
"""Repair inline TeX delimiters lost in the initial shell-string write."""
from pathlib import Path
import re
p=Path(__file__).resolve().parents[1]/'REPORT.md'
s=p.read_text()
bslash=chr(92)
# Preserve display formulas verbatim; use dollar delimiters in prose.
parts=re.split(r'(\\\[.*?\\\])',s,flags=re.S)
variables={'G','e_1','n','k','j','f','Y','Y_t','T_n','a_i','a_i,Z_i','2s','2dt','5K','U>0','s>0','y=1'}
def convert(text):
    text=re.sub(r'\\\((.*?)\\\)',lambda m:'$'+m.group(1)+'$',text)
    result='';i=0
    while i<len(text):
        if text[i]!='(' or i and text[i-1]==']':result+=text[i];i+=1;continue
        depth=1;j=i+1
        while j<len(text) and depth:
            if text[j]=='(':depth+=1
            elif text[j]==')':depth-=1
            j+=1
        if depth:result+=text[i];i+=1;continue
        content=text[i+1:j-1].rstrip(bslash)
        # A span already inside $...$ should be left alone.
        in_dollars=result.count('$')%2
        is_math=not in_dollars and (bslash in content or any(c in content for c in '^_=<>|') or content in variables)
        if is_math:result+='$'+content+'$'
        else:result+='('+content+')'
        i=j
    return result
for i in range(0,len(parts),2):parts[i]=convert(parts[i])
s=''.join(parts).replace('Replace (3) by $5K$ in (10).','Replace the factor $3$ by $5K$ in (10).')
p.write_text(s)
