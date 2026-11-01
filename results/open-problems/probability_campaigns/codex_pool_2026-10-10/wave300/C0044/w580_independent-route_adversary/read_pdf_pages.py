"""Print only explicitly requested pages of the named public preprint."""
from pathlib import Path
import sys
from pypdf import PdfReader

root=Path(__file__).resolve().parent
pages=[int(x) for x in sys.argv[1:]]
if len(pages)>6:
    raise SystemExit('At most six named pages per read')
reader=PdfReader(root/'sources'/'directional_zero_one_2026_claim.pdf')
for page in pages:
    text=reader.pages[page-1].extract_text() or ''
    print(f'PDF PAGE {page}\n{text}')
