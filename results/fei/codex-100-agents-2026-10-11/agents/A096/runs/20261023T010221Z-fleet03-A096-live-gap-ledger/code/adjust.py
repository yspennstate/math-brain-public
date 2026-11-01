"""Clarify first-reset versus repeated-original-reset scope in own draft files."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'code/finalize.py'
s=p.read_text(encoding='utf-8')
changes={
 'An arbitrary no-reset continuation below that frontier is paid.':'An arbitrary continuation below a fresh frontier leaf, with further calibrations of the CURRENT inherited reference, is paid by the complete-reference chain and nonpositive calibration costs; retained old frontier leaves admit no-reset continuation.',
 'no repeated internal recalibrated reset along the same path':'no repeated return to the ORIGINAL source marginal after intervening calibrations',
 'Repeated internal recalibrated exit resets not covered':'Repeated returns to ORIGINAL source marginals after intermediate calibration not covered',
 'repeated internal recalibrated exit resets are outside scope':'repeated returns to ORIGINAL source marginals after intermediate calibration are outside scope',
 'resets occur at its stopping frontier, not repeatedly internally':'first resets occur at a stopping frontier; subsequent CURRENT-reference calibration is paid; repeated original-source resets are outside scope',
 'internal recalibrated multi-reset':'repeated ORIGINAL-source reset',
 'internal recalibrated exit reset followed by another query and selective reset':'reset BACK to the ORIGINAL source marginal after an intermediate calibration and another physical query',
 'internal recalibrated exit reset then further query/reset':'return to ORIGINAL source marginal after intermediate calibration/query',
 'Further no-reset continuations are paid.':'Further CURRENT-reference calibrations below fresh frontier leaves, and no-reset continuations, are paid.',
 'Repeated internal recalibrated resets along one exit path':'Repeated returns to the ORIGINAL source marginal after intervening calibrations along one exit path',
 'only one final calibration from the original S marginal':'each first reset uses one final calibration from the original S marginal; later calibrations use the CURRENT reference',
 'Repeated internal recalibrated resets and arbitrary influence-priced floor supplier remain unpaid.':'Repeated returns to the ORIGINAL source marginal after intermediate calibration, and the arbitrary influence-priced floor supplier, remain unpaid. CURRENT-reference calibration continuations are paid.',
}
for a,b in changes.items():s=s.replace(a,b)
s=s.replace("    f.write(","    if run not in (HOME/'WORKLOG.md').read_text(encoding='utf-8')[-5000:]: f.write(",1)
position=s.index("with (HOME/'LEARNED.md').open")
s=s[:position]+s[position:].replace("    f.write(","    if run not in (HOME/'LEARNED.md').read_text(encoding='utf-8')[-5000:]: f.write(",1)
p.write_text(s,encoding='utf-8')
for name in ('WORKLOG.md','LEARNED.md'):
    p=root.parents[1]/name
    lines=p.read_text(encoding='utf-8').splitlines(keepends=True)
    for i,line in enumerate(lines):
        if root.name in line:
            for a,b in changes.items():line=line.replace(a,b)
            lines[i]=line
    p.write_text(''.join(lines),encoding='utf-8')
print('Own draft and rolling scope clarified; no external files changed.')
