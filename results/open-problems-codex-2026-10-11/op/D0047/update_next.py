from pathlib import Path
p=Path('STATUS.md');t=p.read_text(encoding='utf8').splitlines();t[1]='NEXT: Prove and referee a discounted stopped-moment small-gap bound; use it to exclude the exponential sigma-PV branch directly from the carousel.';p.write_text('\n'.join(t)+'\n',encoding='utf8')
