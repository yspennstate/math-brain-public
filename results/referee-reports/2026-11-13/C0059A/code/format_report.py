#!/usr/bin/env python3
"""Normalize inline mathematics to dollar delimiters after writing the report."""
import re
from pathlib import Path
p=Path('REPORT.md');s=p.read_text()
# Already escaped inline delimiters.
s=re.sub(r'\\\((.*?)\\\)',lambda m:'$'+m.group(1)+'$',s)
# Interval endpoints can themselves contain parentheses.
for expr in [r'a\in[2,5/2)',r'a\in(3/2,5/2)',r'a\in(3/2,5/2]',r'\alpha=a-1/2']:
 s=s.replace('('+expr+')','$'+expr+'$')
lines=[];display=False;fence=False
for line in s.splitlines():
 if line.startswith('```'):fence=not fence;lines.append(line);continue
 if line.strip()==r'\[':display=True
 if display or fence:
  lines.append(line)
  if line.strip()==r'\]':display=False
  continue
 # Existing $...$ spans are protected. Parentheses with mathematical content become inline math.
 protected=[m.span() for m in re.finditer(r'\$[^$]*\$|`[^`]*`',line)]
 spans=[];depth=0;start=None
 for i,c in enumerate(line):
  if any(a<=i<b for a,b in protected):continue
  if c=='(':
   if depth==0:start=i
   depth+=1
  elif c==')' and depth:
   depth-=1
   if depth==0:
    x=line[start+1:i]
    if start>0 and line[start-1]==']':continue
    if x.startswith(('http','sources/','data/','code/')):continue
    mathlike=('\\' in x or any(z in x for z in '_^=<>') or bool(re.fullmatch(r'[a-zA-Z]',x)))
    if mathlike and not re.search(r'\b(?:the|and|of|saved|see|with|from)\b',x):spans.append((start,i+1,x.rstrip('\\')))
 for a,b,x in reversed(spans):line=line[:a]+'$'+x+'$'+line[b:]
 lines.append(line)
s='\n'.join(lines)+'\n'
needle='This is the source matching the page in the request.'
s=s.replace(needle,needle+' Its question reads: “Let $q$ be of type $a\\in[2;5/2)$, it is the case that $\\mathfrak m^\\dagger$ is transient under $\\mathbb P^{(1)}_\\infty$?”')
p.write_text(s)
