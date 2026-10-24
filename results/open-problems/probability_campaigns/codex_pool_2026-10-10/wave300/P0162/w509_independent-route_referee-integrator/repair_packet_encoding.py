"""Repair mojibake introduced by a PowerShell round trip of REVIEW_PACKET.md."""
from pathlib import Path

p = Path('~/brain_workers/w509/REVIEW_PACKET.md')
s = p.read_text(encoding='utf-8-sig')
changes = []
for cp in range(0x80, 0x3000):
    good = chr(cp)
    try:
        bad = good.encode('utf-8').decode('cp1252')
    except UnicodeDecodeError:
        continue
    if bad != good and bad in s:
        changes.append((bad, good))
for bad, good in sorted(changes, key=lambda pair: len(pair[0]), reverse=True):
    s = s.replace(bad, good)
p.write_text(s, encoding='utf-8')
print('repaired_patterns', len(changes))
