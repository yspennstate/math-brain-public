from pathlib import Path
import json, re
p = Path('.')
lit = p.joinpath('LITERATURE.md').read_text(encoding='utf-8')
lit = lit.replace(' ? ', ' — ').replace('D?ring', 'Döring')
lit = re.sub(r'(?<=\d)\?(?=\d)', '–', lit)
lit = lit.replace('d?1', 'd−1').replace('(log ?/?)', '(log ρ/ρ)')
lit = lit.replace('ATTEMPT.md ?1', 'ATTEMPT.md §1')
lit = lit.replace('cites:W?', 'cites:<resolved OpenAlex work ID>')
sourcequote = next(line for line in p.joinpath('ATTEMPT.md').read_text(encoding='utf-8').splitlines()
                   if line.startswith('> We did not touch'))
lit = '\n'.join(sourcequote if line.startswith('> We did not touch') else line
                for line in lit.splitlines()) + '\n'
p.joinpath('LITERATURE.md').write_text(lit, encoding='utf-8')
claims = [json.loads(x) for x in p.joinpath('CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()]
for c in claims:
    c['proof_location'] = c['proof_location'].replace(' ?1', ' §1').replace(' ?5', ' §5')
p.joinpath('CLAIMS.jsonl').write_text(''.join(json.dumps(c, ensure_ascii=False)+'\n' for c in claims), encoding='utf-8')
assert len(claims)==9
print('Encoding repaired. Claims:', len(claims))
