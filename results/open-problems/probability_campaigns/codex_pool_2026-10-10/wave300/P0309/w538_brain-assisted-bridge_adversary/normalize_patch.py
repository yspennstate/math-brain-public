import pathlib
w=pathlib.Path('~/brain_workers/w538')
p=w/'patches'/'01_riesz_scope_warning.diff';p.write_text(p.read_text(encoding='utf-8'),encoding='utf-8',newline='\n')
h=w/'riesz_scope_guard.py';h.write_text(h.read_text(encoding='utf-8-sig'),encoding='utf-8',newline='\n')
m=w/'measure.py';s=m.read_text(encoding='utf-8-sig');s=s.replace("write_text(header+diff,encoding='utf-8')","write_text(header+diff,encoding='utf-8',newline='\\n')");m.write_text(s,encoding='utf-8',newline='\n')
v=w/'validate_packet.py';v.write_text(v.read_text(encoding='utf-8-sig').replace('patch_target','patch_target_lf'),encoding='utf-8',newline='\n')
(w/'PATCH_VALIDATION_crlf.json').write_text((w/'PATCH_VALIDATION.json').read_text(encoding='utf-8'),encoding='utf-8')
print('Normalized patch to LF; validating in a fresh worker-only directory.')
