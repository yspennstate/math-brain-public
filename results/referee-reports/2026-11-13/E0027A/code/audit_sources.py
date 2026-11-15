#!/usr/bin/env python3
"""Check saved source integrity and independently verify key PDF page anchors."""
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import re
import unicodedata
import urllib.request

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]


def normalized(text):
    return re.sub(r'\s+', '', unicodedata.normalize('NFKC', text)).lower()


def main():
    checks = []
    for path in sorted((ROOT / 'data').glob('*_provenance.json')):
        meta = json.loads(path.read_text())
        target = ROOT / meta['text_file']
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        count = len(re.findall(r'^===== PDF PAGE \d+ =====$', target.read_text(), re.M))
        assert actual == meta['text_sha256'], target
        assert count == meta['pdf_pages'], target
        checks.append({'file': meta['text_file'], 'sha256_verified': True, 'pages': count})

    anchors = {
        'hu_sun_2019_survey': {4: ['Theorem 2.1', 'Theorem 2.3'],
                               8: ['Theorem 2.14', 'Theorem 2.15', 'Theorem 2.16',
                                   'Proposition 2.13'],
                               11: ['Theorem 2.29'], 25: ['Question 7']},
        'hu_sun_2018_sums': {7: ['Theorem 2.3'], 11: ['Theorem 3.1', 'Theorem 3.2'],
                            13: ['Kanda-Forst condition'],
                            14: ['Theorem 4.1', 'Corollary 4.3'],
                            15: ['Proposition 4.5'], 16: ['Proof of Theorem 4.1']},
        'rao_1988_hunt': {2: ['THEOREM 2'], 4: ['COROLLARY 3']},
    }
    independent = []
    for stem, pages in anchors.items():
        meta = json.loads((ROOT / 'data' / (stem + '_provenance.json')).read_text())
        req = urllib.request.Request(meta['url'], headers={'User-Agent': 'E0027-source-audit/1.0'})
        with urllib.request.urlopen(req, timeout=45) as response:
            raw = response.read(20_000_001)
        assert hashlib.sha256(raw).hexdigest() == meta['response_sha256'], stem
        reader = PdfReader(io.BytesIO(raw))
        assert len(reader.pages) == meta['pdf_pages'], stem
        for number, phrases in pages.items():
            text = normalized(reader.pages[number - 1].extract_text())
            for phrase in phrases:
                assert normalized(phrase) in text, (stem, number, phrase)
            independent.append({'source': stem, 'pdf_page': number, 'anchors': phrases})

    local_anchors = {
        'hu_sun_2019_survey': {5: ['Theorem 2.5', 'Theorem 2.6'], 6: ['Theorem 2.8'],
                               9: ['Theorem 2.19'], 10: ['Proposition 2.22'],
                               11: ['Proposition 2.24', 'Theorem 2.25', 'Definition 2.26',
                                    'Proposition 2.27', 'Definition 2.28'],
                               13: ['Theorem 2.31', 'Theorem 2.32', 'Lemma 3.1'],
                               14: ['Proposition 3.2']},
        'hu_sun_2016_further_study': {5: ['Proposition 2.2'], 24: ['Theorem 4.2']},
        'hu_sun_zhang_2015_new_results': {7: ['Theorem 3.3'],
                                        8: ['Definition 3.4', 'Proposition 3.5'],
                                        13: ['Theorem 4.5']},
        'hu_sun_wang_2019_two_theorems': {3: ['Theorem 1.1'], 4: ['Theorem 1.3'],
                                        21: ['5.3 Let X']},
        'hu_sun_2012_getoor': {3: ['Theorem 1.1', 'Theorem 1.2'], 4: ['Proposition 1.6']},
    }
    local_checked = []
    for stem, wanted in local_anchors.items():
        text = (ROOT / 'sources' / (stem + '.txt')).read_text()
        pages = {int(n): normalized(p) for n, p in re.findall(
            r'===== PDF PAGE (\d+) =====\n(.*?)(?=\n===== PDF PAGE|\Z)', text, re.S)}
        for number, phrases in wanted.items():
            for phrase in phrases:
                assert normalized(phrase) in pages[number], (stem, number, phrase)
            local_checked.append({'source': stem, 'pdf_page': number, 'anchors': phrases})

    # Check the requested artifact contract; launch files/logs are pre-existing.
    assert (ROOT / 'REPORT.md').read_text().splitlines()[0] == 'PARTIAL'
    forbidden = []
    for path in ROOT.rglob('*'):
        if path.is_file():
            suffix = path.suffix.lower()
            if suffix in {'.pdf', '.png', '.jpg', '.jpeg', '.tiff', '.tif', '.webp'}:
                forbidden.append(str(path.relative_to(ROOT)))
            with path.open('rb') as stream:
                assert not stream.read(5).startswith(b'%PDF'), path
    assert not forbidden, forbidden
    assert all(p.suffix == '.txt' for p in (ROOT / 'sources').iterdir() if p.is_file())
    result = {'audited_utc': datetime.now(timezone.utc).isoformat(),
              'source_integrity': checks, 'independent_pypdf_anchors': independent,
              'additional_saved_text_anchors': local_checked,
              'report_status': 'PARTIAL', 'forbidden_source_artifacts': forbidden,
              'numerical_experiment': 'none', 'passed': True}
    (ROOT / 'data' / 'source_audit.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
