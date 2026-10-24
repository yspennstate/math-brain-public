import hashlib
import json
from pathlib import Path
import pymupdf

root = Path(__file__).resolve().parent
source = Path('~/Downloads/Probability_1000_intake_claude_20260907/sources/drewitz_ramirez_rwre_2014/source.pdf')
digest = hashlib.sha256(source.read_bytes()).hexdigest()
doc = pymupdf.open(source)
page = doc[45]
page.get_pixmap(matrix=pymupdf.Matrix(1, 1)).save(root / 'source_corollary_3_6.png')
text = page.get_text()
start = text.find('Corollary 3.6.')
end = text.find('3.3', start)
excerpt = text[start:end]
receipt = {'source_path':str(source), 'sha256':digest, 'bytes':source.stat().st_size, 'pages':len(doc), 'matches_archived_hash':digest=='5b79b728fd6a0add60442b5a686ed69fdff9041c04d595269824a91e1792ff43', 'rendered_pdf_page_index':45, 'corollary_extraction':excerpt}
(root / 'source_hash_receipt.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({k:v for k,v in receipt.items() if k!='corollary_extraction'}, ensure_ascii=False))
print(excerpt)
