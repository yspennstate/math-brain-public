from pathlib import Path
import re
import fitz

root = Path(__file__).resolve().parent
doc = fitz.open(root / 'ADH_1511.03262.pdf')
hits = []
patterns = [r'Question\s*31\b', r'bi.infinite.*?geodesic', r'\(A1\)', r'\(A2\)', r'\(A3\)', r'oriented percolation.*?threshold']
for i, page in enumerate(doc):
    txt = page.get_text()
    for pat in patterns:
        m = re.search(pat, txt, re.I)
        if m and (pat == patterns[0] or i < 12 or ('threshold' in pat and len(hits) < 12)):
            excerpt = txt[max(0,m.start()-350):m.end()+1600]
            hits.append({'pdf_page_1_based':i+1, 'pattern':pat, 'excerpt':excerpt})
(root / 'PRIMARY_SOURCE_EXCERPTS.json').write_text(__import__('json').dumps(hits, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
for hit in hits:
    print('PDF PAGE',hit['pdf_page_1_based'],'PATTERN',hit['pattern'])
    print(hit['excerpt'])
print('Primary document pages:', len(doc))
