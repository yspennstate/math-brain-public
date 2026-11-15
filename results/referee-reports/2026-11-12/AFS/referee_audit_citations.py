#!/usr/bin/env python3
"""Reconstruct JPS's shared theorem and subsection counters from local TeX."""
import os
import re
import signal
from pathlib import Path
signal.alarm(30)
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)
raw=Path('sources/jps/pivot_trees.tex').read_text()
section=subsection=counter=0
current=''
envs='thm|lemma|prop|cor|conjecture|problem|note|fact|obs|remark|question|define|defines|example'
pattern=re.compile(r'\\section\{|\\subsection\{|\\begin\{('+envs+r')\}|\\label\{([^}]*)\}')
wanted={'notations','interpretations','fixed points','subsec:RST','sec:supercritical','sec:open',
        'main 2 colours','(T, omega) multi-type','prop:interpretability','prop:Tpiv.GW',
        'prop:2state.regularity','prop:(T,omega*)','prop:immigration','lem:Yn.martingale',
        'lem:two.step','lem:log.moment.bound','lem:Yn.bounded','lem:X_n.finite',
        'lem:dichotomy','lem:f_n.r_n','lem:f_n.expansion'}
print('LOCAL JPS NUMBERING')
for lineno,line in enumerate(raw.splitlines(),1):
    line=re.split(r'(?<!\\)%',line)[0]
    for match in pattern.finditer(line):
        token=match.group(0)
        if token.startswith('\\section'):
            section+=1;subsection=counter=0;current=str(section)
        elif token.startswith('\\subsection'):
            subsection+=1;current=f'{section}.{subsection}'
        elif match.group(1):
            counter+=1;current=f'{match.group(1)} {section}.{counter}'
        elif match.group(2) in wanted:
            print(f'{match.group(2)}: {current}, source line {lineno}')
print('\nPAPER CITATIONS TO JPS/RZ')
for lineno,line in enumerate(Path('PAPER.tex').read_text().splitlines(),1):
    for m in re.finditer(r'\\cite(?:\[([^]]*)\])?\{(JPS|RZ)\}',line):
        print(f'PAPER line {lineno}: {m.group(0)}')
print('\nLocal JPS source has no embedded arXiv version tag; numbering matches the cited version, but v2 provenance is not independently established by TeX content.')
