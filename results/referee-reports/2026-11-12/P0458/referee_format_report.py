"""Repair Markdown math delimiters after writing REPORT.md through JavaScript."""
from pathlib import Path
import re

p=Path('REPORT.md')
s=p.read_bytes().decode()
controls=[(i,ord(c),repr(s[max(0,i-12):i+20])) for i,c in enumerate(s)
          if ord(c)<32 and c not in '\n\t\r']
print('control characters before repair:',controls)
for bad,good in [('\binom',r'\binom'),('\frac',r'\frac')]:
    s=s.replace(bad,good)
commands=['mathbb','mathrm','operatorname','sqrt','Gamma','Lambda']

def repair_math(t):
    for command in commands:
        t=re.sub(r'(?<![A-Za-z\\])'+command,lambda _: '\\'+command,t)
    t=re.sub(r'(?<![A-Za-z\\])mu(?=_)',lambda _: r'\mu',t)
    return t

changes=[]
def convert(text):
    out=[]; i=0
    while i<len(text):
        if text[i]!='(':
            out.append(text[i]);i+=1;continue
        j=i+1;depth=1
        while j<len(text) and depth:
            if text[j]=='(': depth+=1
            elif text[j]==')': depth-=1
            j+=1
        if depth:
            out.append(text[i:]);break
        body=text[i+1:j-1]
        keep=(body=='SE' or body=='+04' or re.fullmatch(r'[0-9]+(?:\.[0-9]+)?',body))
        if keep:
            out.append(text[i:j])
        else:
            out.append('$'+repair_math(body)+'$')
            changes.append(body)
        i=j
    return ''.join(out)

lines=[]; fenced=False; display=False
for line in s.splitlines():
    if line.startswith(chr(96)*3):
        fenced=not fenced;lines.append(line);continue
    if fenced:
        lines.append(line);continue
    if line.strip()==r'\[':
        display=True;lines.append('$$');continue
    if line.strip()==r'\]':
        display=False;lines.append('$$');continue
    if display:
        lines.append(repair_math(line));continue
    pieces=re.split('('+chr(96)+'[^'+chr(96)+']*'+chr(96)+')',line)
    lines.append(''.join(piece if piece.startswith(chr(96)) else convert(piece)
                         for piece in pieces))
s='\n'.join(lines)+'\n'
bad=[(i,ord(c)) for i,c in enumerate(s) if ord(c)<32 and c not in '\n\t']
assert not bad,bad
p.write_text(s)
print('converted parenthesized inline expressions:',len(changes))
print('sample expressions:',changes[:15])
