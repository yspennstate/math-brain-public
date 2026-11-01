from pathlib import Path
from hashlib import sha256

def parse(path):
    s=Path(path).read_text()
    part=s.split('DFATR[DFAK][DFAAL]={\n',1)[1].split('};\nstatic const uint32_t',1)[0]
    rows=[]
    for line in part.splitlines():
        line=line.strip().strip(',')
        if line:
            rows.append(list(map(int,line.strip('{}').split(','))))
    cm=list(map(int,s.split('DFACM[DFAK]={',1)[1].split('};',1)[0].split(',')))
    return rows,cm
r44,c44=parse('/tmp/c044_dfa.h')
r45,c45=parse('/tmp/c045_dfa.h')
assert len(r44)==len(r45)==45427
assert c44==c45
for i in range(45427):
    for c in (0,1):
        for l in range(-6,7):
            assert r44[i][c*13+(l+6)]==r45[i][c*15+(l+7)]
        assert r45[i][c*15+0]==r45[i][c*15+1]
        assert r45[i][c*15+14]==r45[i][c*15+13]
print('R17 C044/C045 exact minimized-DFA pullback checker')
print('c044_states=',len(r44))
print('c045_states=',len(r45))
print('c044_header_sha256=',sha256(Path('/tmp/c044_dfa.h').read_bytes()).hexdigest())
print('c045_header_sha256=',sha256(Path('/tmp/c045_dfa.h').read_bytes()).hexdigest())
print('EXACT_COMPLEMENT_ACTION_IDENTICAL_PASS')
print('EXACT_CORE_TRANSITIONS_IDENTICAL_PASS')
print('EXACT_TAIL_CLAMP_MINUS7_TO_MINUS6_PASS')
print('EXACT_TAIL_CLAMP_PLUS7_TO_PLUS6_PASS')
print('FULL_CAP7_LANGUAGE_IS_PULLBACK_OF_CAP6_DFA_PASS')
print('ALL_EXACT_CHECKS_PASS')
