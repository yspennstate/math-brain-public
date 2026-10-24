"""Read-only, bounded source recovery for P0043 after recall timed out."""
import json
import re
import sqlite3
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
database = '~/math-brain-build/local/population/brain.sqlite3'
connection = sqlite3.connect('file:'+database+'?mode=ro', uri=True, timeout=3)
print('NODE_SCHEMA', connection.execute('PRAGMA table_info(nodes)').fetchall())
print('CLAIM_SCHEMA', connection.execute('PRAGMA table_info(claims)').fetchall())
connection.close()
reader = PdfReader(ROOT/'sources/quasi_transitive_claim.pdf')
print('PUBLIC_PAPER_PAGE_COUNT', len(reader.pages))
text = '\n'.join(reader.pages[i].extract_text() or '' for i in range(min(2,len(reader.pages))))
(ROOT/'sources/public_paper_statement.txt').write_text(text, encoding='utf-8')
print(text[:11500])
