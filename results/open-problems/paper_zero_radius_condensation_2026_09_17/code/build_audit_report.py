#!/usr/bin/env python3
"""Assemble the five individual Markdown reviews for optional PDF conversion."""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
audits = root / 'audits'
header = '---\ntitle: "Five-pass audit record"\nsubtitle: "Uniform condensation windows for zero-radius random allocations"\nauthor: "Review documentation for Yitzchak Shmalo"\ndate: "17 September 2026"\nfontsize: 10pt\ngeometry: margin=24mm\n---\n\n'
text = header + (audits / 'SUMMARY.md').read_text() + '\n\n'
for path in sorted(audits.glob('0[1-5]_*.md')):
    text += '\\newpage\n\n' + path.read_text() + '\n\n'
(audits / 'audit_report.md').write_text(text)
print(audits / 'audit_report.md')
