"""Restore the report's inline LaTeX delimiters after string transport."""
import re
from pathlib import Path

path=Path('REPORT.md')
s=path.read_text()
s=s.replace('\x0barepsilon',r'\varepsilon')
s=re.sub(r'(?<!\\)\bmathcal\b',lambda m:'\\'+m[0],s)
s=re.sub(r'(?<!\\)\boperatorname\b',lambda m:'\\'+m[0],s)
s=s.replace('(Delta)',r'(\Delta)').replace('(min x',r'(\min x')
s=s.replace(r'(T_\pi\)',r'(T_\pi)')
s=s.replace(r'(|V^{2n+1}',r'(\|V^{2n+1}')

def is_math(content):
    if chr(96) in content:return False
    if content.startswith(('http:','https:')):return False
    if content.isdigit():return False  # Equation references and bibliography years.
    if re.search(r'[\\_^=<>|{}]',content):return True
    if re.fullmatch(r'[A-Za-z]{1,2}',content):return True
    if re.fullmatch(r'-[A-Za-z]',content):return True
    if ',' in content and re.fullmatch(r'[A-Za-z0-9, /().-]+',content):return True
    return False

def convert(line):
    result=[];i=0;incode=False;inmath=False
    while i<len(line):
        ch=line[i]
        if ch==chr(96):incode=not incode
        if ch=='$' and not incode:inmath=not inmath
        if ch=='(' and not incode and not inmath:
            depth=1;j=i+1
            while j<len(line) and depth:
                if line[j]=='(':depth+=1
                elif line[j]==')':depth-=1
                j+=1
            if depth==0:
                content=line[i+1:j-1]
                if is_math(content) and not (i and line[i-1]==']'):
                    result.append('$'+content+'$')
                    i=j;continue
        result.append(ch);i+=1
    return ''.join(result)

lines=[];display=False;fenced=False
for line in s.split('\n'):
    if line.startswith(chr(96)*3):fenced=not fenced
    if line.strip()==r'\[':display=True
    if not display and not fenced:line=convert(line)
    if line.strip()==r'\]':display=False
    lines.append(line)
s='\n'.join(lines)
assert not any(ord(c)<32 and c not in '\n\t' for c in s)
assert not re.search(r'(?<!\\)\b(?:mathcal|operatorname)\b',s)
path.write_text(s)
print('Inline mathematics and LaTeX commands checked.')
