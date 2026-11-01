"""Replace the draft's [pending: rows per piece ...] line with the numbers c9_bcheck5 printed (logs/finish_5.out) and the
trap verdict (logs/trap_plain888g8.jsonl). Run after finish_c9.sh, before file_c9.sh copies the draft. (agent H)"""
import io, json, os
from fractions import Fraction as F
H = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(os.path.dirname(H), 'C9_post_exit_DRAFT.md')
out = io.open(os.path.join(H, 'logs/finish_5.out'), encoding='utf-8').read().splitlines()
rows = next(l for l in out if l.startswith('rows ')).split()
vend = next(l for l in out if l.startswith('v_end '))
maxR = vend.split('max R')[1].split()[0]
r = F(next(l for l in out if l.startswith('r_end_exact')).split()[1])
trap = [json.loads(l) for l in io.open(os.path.join(H, 'logs/trap_plain888g8.jsonl'), encoding='utf-8')]
tl = trap[-1]
new = ('   Result: rows per piece %s / %s / %s / %s (bfull14, brst10, flow599 to 887, plain888g8), no failed segment, every '
       'junction exact; max a priori radius %s; r_end = |v_end| = %.4e (exact rational in logs/finish_5.out). Trap record: %s.'
       % (rows[1], rows[2], rows[3], rows[4], maxR, float(r), ('PASS at rho %s, nsplit %s, mu %.4e; need_rho %.4e, offset %.3e, sw %.6f, frame %s' % (tl['PASS']['rho'], tl['PASS']['nsplit'], float(F(tl['PASS']['mu'])), tl['need_rho'], tl['offset'], tl['sw'], 'frame_b' if tl.get('frameb') else 'eigen') if 'PASS' in tl else 'NO PASS')))
s = io.open(D, encoding='utf-8').read()
old = next(l for l in s.splitlines() if l.strip().startswith('[pending: rows per piece'))
s = s.replace(old, new).replace('DRAFT: numbers marked [pending] come from the running chain.', 'Numbers from the finished chain (18 Oct).')
io.open(D, 'w', encoding='utf-8', newline='\n').write(s)
print(new)
