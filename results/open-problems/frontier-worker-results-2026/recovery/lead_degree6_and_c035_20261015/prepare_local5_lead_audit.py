from pathlib import Path
H=Path(__file__).resolve().parent
s=(H/'audit_t067_local42.py').read_text(encoding='utf-8')
s=s.replace('T067-UNIFORM-LOCAL-EXT-001_v1.md','T067-LOCAL-RADIUS5-001_v1.md').replace('1163cfb98bd9adb486df2c79dce11a4844a000d86ecee897749c73874fe78c94','517e75594c92240c4f1202a0cd5f734e92643ee22562dbb020b82ddda27c4e5a')
s=s.replace('1920*(R(19,20)*g*D**3-R(9,10)*abar-R(81,100)*bbar)','8640000*(R(999,1000)*g*D**3-R(217,500)*abar-R(217,500)**2*bbar)')
s=s.replace('R(39,250)','R(559017,1250000)').replace('42*39**2>250**2','5*559017**2>1250000**2')
s=s.replace('x<=1/10, every integer d>=42','x<=217/4500, every integer d>=5').replace('No global entry or cutoff42','No global entry or degree6 admission').replace('T067_LOCAL42_LEAD_RECEIPT','T067_LOCAL5_LEAD_RECEIPT')
p=H/'audit_t067_local5_lead.py';assert not p.exists();p.write_text(s,encoding='utf-8')
print('Prepared independent full126-coefficient radius5 rebuild')
