"""Check manuscript assembly and artifact integrity, not mathematical truth."""
from pathlib import Path
import collections
import hashlib
import io
import json
import math
import re
import sys

from pypdf import PdfReader

root = Path(__file__).resolve().parent
main = (root / 'main.tex').read_text()
names = ['main.tex'] + [name + '.tex' for name in re.findall(r'\\input\{([^}]+)\}', main)]
contents = {name: (root / name).read_text() for name in names}
combined = '\n'.join(contents.values())
labels = re.findall(r'\\label\{([^}]+)\}', combined)
references = re.findall(r'\\(?:ref|eqref|pageref)\{([^}]+)\}', combined)
citations = set()
for keys in re.findall(r'\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}', combined):
    citations.update(key.strip() for key in keys.split(','))
bib = (root / 'bibliography.bib').read_text()
bibkeys = set(re.findall(r'@\w+\s*\{\s*([^,]+),', bib))
errors = []
missing_refs = sorted(set(references) - set(labels))
duplicates = sorted(k for k, v in collections.Counter(labels).items() if v > 1)
missing_cites = sorted(citations - bibkeys)
for condition, message in [(missing_refs, 'missing references'), (duplicates, 'duplicate labels'),
                           (missing_cites, 'missing citation keys')]:
    if condition:
        errors.append(f'{message}: {condition}')
if any(ord(c) < 32 and c not in '\t\n\r' for c in combined):
    errors.append('Unexpected control character in a chapter')
if not re.search(r'\\author\{\s*\}', main):
    errors.append('The manuscript author command is not explicitly empty')
log = (root / 'main.log').read_text(errors='replace')
bad_log = [line for line in log.splitlines() if 'Overfull' in line or
           'multiply defined' in line or ('undefined' in line.lower() and 'warning' in line.lower())]
if bad_log:
    errors.extend(bad_log)
pdf_bytes = (root / 'main.pdf').read_bytes()
if not pdf_bytes.rstrip().endswith(b'%%EOF'):
    raise SystemExit('PDF is incomplete: final EOF marker is missing')
pdf = PdfReader(io.BytesIO(pdf_bytes))
author = str((pdf.metadata or {}).get('/Author', '') or '')
if author:
    errors.append('PDF author field is not empty')
page_text = [page.extract_text() or '' for page in pdf.pages]
if any('??' in text for text in page_text):
    errors.append('Unresolved-reference marker in PDF text')
if any(len(text.strip()) < 40 for text in page_text):
    errors.append('Nearly empty PDF page')
numeric = {
    'Gaussian_mixture_I3': math.gamma(1/6)*math.gamma(1/12)/(6*math.gamma(1/4)),
    'rank_one_Gamma_bound': math.exp(.75)*math.gamma(.25),
    'rank_two_half_bound': 40*2**.75,
    'rank_three_definite_bound': math.sqrt(2)*(20+46*(3+2*math.log(20))/20),
    'separated_semidefinite_bound': 3*math.sqrt(2)*math.sqrt(120*(3+math.log(120))),
    'absolute_spectral_diagonal_bound': 480*math.sqrt(math.e)/23,
    'symmetric_window_coefficient': 2*math.sqrt(2*math.pi)/(3*math.pi),
}
limits = {'Gaussian_mixture_I3': 3, 'rank_one_Gamma_bound': 8,
          'rank_two_half_bound': 68, 'rank_three_definite_bound': 58,
          'separated_semidefinite_bound': 130, 'absolute_spectral_diagonal_bound': 35}
for key, limit in limits.items():
    if not numeric[key] < limit:
        errors.append(f'Numerical bound failed: {key}')
result = {
    'status': 'PASS' if not errors else 'FAIL',
    'pages': len(pdf.pages), 'included_tex_files': names,
    'labels': len(labels), 'references': len(references),
    'cited_works': len(citations), 'bibliography_entries': len(bibkeys),
    'theorem_like_environments': len(re.findall(r'\\begin\{(?:theorem|lemma|proposition|corollary)\}', combined)),
    'proof_environments': len(re.findall(r'\\begin\{proof\}', combined)),
    'pdf_author': author, 'pdf_sha256': hashlib.sha256(pdf_bytes).hexdigest(),
    'numerical_checks': numeric, 'errors': errors,
    'limitation': 'These are assembly, metadata and arithmetic checks; mathematical correctness depends on the supplied proofs and independent reviews.'
}
(root / 'VALIDATION.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
sys.exit(bool(errors))
