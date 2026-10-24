from pathlib import Path
import re
BASE=Path('~/Downloads/Probability_1000_intake_claude_20260907/sources')
CONFIG={'kosygina_zerner_erw_2012':r'Problem\s*3\.?\s*12',
        'ding_lee_peres_cover_2012':r'Question\s*5\.?\s*2',
        'garban_steif_noise_2012':r'singular random compact'}
for name,pattern in CONFIG.items():
    p=BASE/name/'text.txt'
    raw=p.read_bytes()
    # Extraction files may be UTF-16; report the encoding rather than silently searching nul bytes.
    encoding='utf-16' if raw.startswith((b'\xff\xfe',b'\xfe\xff')) else 'utf-8-sig'
    txt=raw.decode(encoding,errors='replace')
    lines=txt.splitlines()
    print(f'SOURCE {name}: bytes={len(raw)}, encoding={encoding}, lines={len(lines)}')
    matches=[i for i,line in enumerate(lines) if re.search(pattern,line,re.I)]
    if not matches:
        print('NO MATCH; prefix: '+txt[:160])
    for i in matches[:8]:
        print('\n'.join(f'{j+1}: {lines[j]}' for j in range(max(0,i-3),min(len(lines),i+9))))
