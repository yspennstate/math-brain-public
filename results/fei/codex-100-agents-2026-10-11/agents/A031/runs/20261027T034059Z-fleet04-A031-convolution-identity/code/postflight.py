from pathlib import Path
from fractions import Fraction as F
import json,hashlib
r=Path(__file__).resolve().parents[1]
# Exact controls, separate from the main count and with no search or logs.
a,b=F(4,5),F(3,5)
assert a*a+b*b==1
assert [(a+b)**2,(a-b)**2]==[F(49,25),F(1,25)]
assert 2*a*b==F(24,25)!=0
# Actual parity2: P=delta_11, Q=(delta_11+delta_00)/2.
# Query bit0; the ghost row uses K+=(1/3), K-=(2/3).
zplus=F(1,2)+F(1,3); zminus=F(1,2)+F(2,3)
assert zplus+zminus==2
assert zplus*zminus==F(35,36)<1
qplus=[F(1,3)/zplus,F(1,2)/zplus]
qminus=[F(2,3)/zminus,F(1,2)/zminus]
assert qplus==[F(2,5),F(3,5)]
assert qminus==[F(4,7),F(3,7)]
assert sum(qplus)==sum(qminus)==1
# A normalized-vacuum calibration at an occupied constant leaf retains mass.
s=F(1,2); q=[F(3,4),F(1,4)]; out=[s,F(0)]
assert sum(out)==s
result={'status':'PASS','nonboolean_normalized_amplitudes':['4/5','3/5'],
        'nonboolean_child_masses':['49/25','1/25'],'violated_signed_shift':'24/25',
        'actual_parity2_ghost_normalizers':['5/6','7/6'],
        'normalizer_product':'35/36','full_terminal_mass':'1/2',
        'scope':'Exact standalone boundary/control fixtures, not added to MAIN count',
        'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(r/'out/POSTFLIGHT.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
