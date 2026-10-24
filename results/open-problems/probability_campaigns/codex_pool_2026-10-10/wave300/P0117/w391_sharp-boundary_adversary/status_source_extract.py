from pathlib import Path
import shutil
import fitz

root = Path(__file__).resolve().parent
primary = Path('~/brain_workers/w390/sources/no_bigeodesics_2026_09_24.pdf')
if primary.is_file():
    own = root / 'PRIMARY_CLAIM_2026_09_24.pdf'
    shutil.copyfile(primary, own)
    doc = fitz.open(own)
    excerpts = []
    for i in range(min(2, len(doc))):
        txt = doc[i].get_text()
        excerpts.append(txt)
        print('PRIMARY CLAIM PDF PAGE',i+1)
        print(txt)
    (root / 'PRIMARY_CLAIM_FIRST_TWO_PAGES.txt').write_text('\n'.join(excerpts), encoding='utf-8')
    print('Total manuscript pages:', len(doc), '; full proof NOT audited.')
else:
    print('RECENT_PRIMARY_LOCAL_COPY_UNAVAILABLE; claim remains unverified.')
