import pathlib
w=pathlib.Path('~/brain_workers/w538')
p=w/'patches'/'01_riesz_scope_warning.diff'
p.write_text(p.read_text(encoding='utf-8').replace('--- a/.claude/dreaming/riesz_scope_guard.py\n','--- /dev/null\n'),encoding='utf-8')
m=w/'measure.py';m.write_text(m.read_text(encoding='utf-8-sig').replace("fromfile='a/.claude/dreaming/riesz_scope_guard.py'","fromfile='/dev/null'"),encoding='utf-8')
initial=w/'PATCH_VALIDATION.json'
(w/'PATCH_VALIDATION_initial.json').write_text(initial.read_text(encoding='utf-8'),encoding='utf-8')
(w/'STATUS.md').write_text('STATE: WORKING\nNEXT: Check the corrected new-file diff, read the canonical store by its documented locator, and publish the concept DRAFT for review.\n\n2026-10-10: Packet and measurements saved. First patch check caught an invalid new-file old header; fixed to the standard /dev/null header while diff --git and +++ name the live destination. No mathematical/source change.\n',encoding='utf-8')
print('Corrected new-file patch header; retained initial rejection receipt.')
