"""Index cited primary-source statements in the independently fetched texts."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
queries = {
 'survey_v5': ['Assumption 8.4','Theorem 8.6','Proposition 8.8','Theorem 8.9','Proposition 8.10','Problem 7'],
 'survey_published': ['Assumption 8.4','Theorem 8.6','Proposition 8.8','Theorem 8.9','Proposition 8.10','Theorem 8.15','Theorem 8.18','Problem 7'],
 'av_local': ['Assumption 2.1','Definition 2.3','Theorem 2.7','Theorem 2.10','Corollary 2.11','Theorem 2.13','Proposition 7.1','Proposition 7.2'],
 'av_global': ['Assumption 3.1','Theorem 3.2','Assumption 4.4','Theorem 4.5','Assumption 4.8','Theorem 4.9','Assumption 4.10','Theorem 4.11','Example 4.12','Assumption 5.1','Theorem 5.2'],
 'milesis_salins_v1': ['Theorem 5.1','Theorem 6.1','Lemma 3'],
 'milesis_salins_v2': ['Theorem 5.1','Theorem 5.2','Lemma 4'],
 'agresti_delayed': ['Theorem 3.5','Theorem 3.6'],
 'reaction_2026_v3': ['Theorem 2.9','Theorem 2.12','Theorem 2.20','Corollary 2.21','Theorem 2.24','Example 3.4','Corollary 3.14'],
 'blessing_seitz_sonner_tang': ['Theorem 4.10'],
 'foldes_stacy': ['SPDE Assumption 2','SPDE Assumption 3','Theorem 6.31'],
 'fellner_morgan_tang': ['Theorem 1.1'],
 'fitzgibbon_morgan_tang_yin': ['Theorem 1.1','Lemma 2.4'],
 'agresti_kniely_tang': ['Theorem 3.4'],
}
records = []
for name, patterns in queries.items():
    s = (ROOT/'sources'/(name+'.txt')).read_text()
    for pattern in patterns:
        matches = list(re.finditer(r'^'+re.escape(pattern)+r'(?:\.|[ \t]+\()', s, re.M))
        assert matches, (name,pattern)
        # Earliest heading match; subsequent matches may be continuation text.
        match = matches[0]
        page = list(re.finditer(r'===== PDF PAGE (\d+) =====',s[:match.start()]))[-1][1]
        records.append(dict(source=name, statement=pattern, pdf_page=int(page),
                            text_line=s[:match.start()].count('\n')+1))
(ROOT/'data'/'citation_locations.json').write_text(json.dumps(records,indent=2)+'\n')
hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
        for p in (ROOT/'claim_files').rglob('*') if p.is_file()}
(ROOT/'data'/'claim_input_hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
print(f'{len(records)} statement locators; {len(hashes)} submitted input fingerprints')
