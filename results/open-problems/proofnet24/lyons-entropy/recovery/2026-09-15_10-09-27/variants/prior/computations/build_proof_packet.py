"""Build the readable PDF of principal proofs; keep all source notes separately.

Requires pandoc, pdflatex, reportlab and pypdf. The final research status is read
from the actual execution ledger; this script does not invent completions.
"""
import json
from pathlib import Path
import re
import subprocess

from pypdf import PdfReader, PdfWriter
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / 'tmp' / 'pdfs'
OUT = ROOT / 'output' / 'pdf'
BASE = ('https://github.com/yspennstate/math-open-problems/blob/master/'
        'proofnet24/portfolio-completion/runs/2026-09-14/2026-09-14_20-23-26/')


def main():
    TMP.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    ledger = json.loads((ROOT / 'execution_ledger.json').read_text())
    complete = sum(a['status'] == 'completed' for a in ledger['agents'])
    launched = len(ledger['agents'])
    if len({a['task_name'] for a in ledger['agents']}) != launched:
        raise ValueError('Execution ledger contains a duplicate agent identity')
    sources = ['FOUR_TYPE_UNIQUENESS.md', 'QSO_FIXED_POINT_GEOMETRY.md', 'QSO_HALF_STEP_EXPLICIT.md',
               'QSO_AVERAGING_RANGE.md', 'QSO_GLOBAL_051.md', 'QSO_SPECTRAL_BOUNDS.md',
               'LYONS_PARTIAL_RESULTS.md', 'SUBCRITICAL_COUNTEREXAMPLE.md',
               'CRITICAL_COUNTEREXAMPLE.md']
    # Additional finished principal notes can be registered explicitly here.
    text = []
    for i, name in enumerate(sources):
        s = (ROOT / name).read_text()
        # Local research hyperlinks must remain usable after PDF export.
        s = re.sub(r'\]\((?!https?://|#)([^)]+)\)',
                   lambda m: '](' + BASE + m.group(1) + ')', s)
        s = s.replace('\u2011', '-').replace('\u2013', '-').replace('\u2014', '--')
        if i:
            text.append('\\clearpage\n')
        text.append(s)
    combined = TMP / 'principal-proofs.md'
    combined.write_text('\n\n'.join(text))
    header = TMP / 'header.tex'
    header.write_text(r'''\usepackage{amsmath,amssymb}
\usepackage{microtype}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small Open-problem research proofs}
\fancyhead[R]{\small 14 September 2026}
\fancyfoot[C]{\thepage}
\setlength{\headheight}{14pt}
\setlength{\emergencystretch}{3em}
\AtBeginDocument{\setcounter{page}{2}}
''')
    tex = TMP / 'principal-proofs.tex'
    for suffix in ('.aux', '.out', '.toc'):
        tex.with_suffix(suffix).unlink(missing_ok=True)
    subprocess.run(['pandoc', str(combined), '--from=markdown+tex_math_single_backslash',
                    '--standalone', '--to=latex', '--include-in-header=' + str(header),
                    '-V', 'geometry:margin=24mm', '-V', 'fontsize=11pt',
                    '-V', 'colorlinks=true', '-V', 'linkcolor=blue',
                    '-V', 'urlcolor=blue', '-o', str(tex)], check=True)
    compile_log = TMP / 'pdflatex-output.txt'
    with compile_log.open('w') as log:
        subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                        '-output-directory', str(TMP), str(tex)],
                       stdout=log, stderr=subprocess.STDOUT, check=True)
        subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                        '-output-directory', str(TMP), str(tex)],
                       stdout=log, stderr=subprocess.STDOUT, check=True)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='ResearchTitle', fontName='Helvetica-Bold',
                              fontSize=24, leading=29, spaceAfter=17,
                              textColor=colors.HexColor('#142A3B')))
    styles.add(ParagraphStyle(name='ResearchBody', fontName='Helvetica',
                              fontSize=10.5, leading=15, spaceAfter=10,
                              alignment=TA_LEFT))
    styles.add(ParagraphStyle(name='ResearchSmall', fontName='Helvetica',
                              fontSize=9, leading=12, spaceAfter=8))
    p = lambda s: Paragraph(s, styles['ResearchBody'])
    story = [Paragraph('Proofs and counterexamples', styles['ResearchTitle']),
             p('Open-problem research run | 14 September 2026'),
             Spacer(1, 9),
             p('<b>The full Lyons entropy-concavity conjecture remains unresolved here.</b> '
               'This packet presents complete arguments for restricted entropy cases, '
               'four-type fixed-point uniqueness and algorithms, and counterexamples '
               'to proposed subcritical and critical tree fluctuation limits.'),
             p(f'Actual agents launched: <b>{launched}/100</b>. '
               f'Completed: <b>{complete}/100</b>. Recorded model: gpt-6-astra; '
               'reasoning effort: max. The count reports execution, not mathematical validation.'),
             Spacer(1, 10)]
    rows = [
        ['Proof', 'Exact scope'],
        ['Four-type stochastic operators', 'All admissible coefficients, including boundary fixed points; quantitative stability and a small-leakage extension.'],
        ['Averaged iteration', 'Global convergence for every positive weight through 0.51; explicit uniform rates.'],
        ['Determinantal entropy', 'Two sites; coordinate and scaled cross-block slices; indefinite rank-two directions through dimension five.'],
        ['Subcritical conditioned trees', 'One fixed offspring law with a non-Gaussian degree-count subsequence limit.'],
        ['Critical infinite-variance trees', 'One fixed computable offspring law with a non-Gaussian degree-count subsequence limit.'],
    ]
    wrapped = [[Paragraph(v, styles['ResearchSmall']) for v in row] for row in rows]
    table = Table(wrapped, colWidths=[145, 340])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#E9EFF3')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 9),
        ('RIGHTPADDING', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LINEBELOW', (0, 0), (-1, -1), .4, colors.HexColor('#D0DCE4')),
    ]))
    story += [table, Spacer(1, 17),
              p('<b>Proof status and priority are separate.</b> The accompanying reports '
                'record independent audits and exact checks. Historical novelty is not '
                'certified. No proof-assistant verification or external referee acceptance '
                'is claimed.'),
              p('The complete agent reports, sources, failed approaches, code and corrections '
                'are retained in the GitHub run directory. This PDF is a readable selection '
                'of the principal proofs, not the entire research archive.'),
              Paragraph('<link href="' + BASE + 'README.md">Open the research index on GitHub</link>',
                        styles['ResearchSmall'])]
    cover = TMP / 'cover.pdf'
    SimpleDocTemplate(str(cover), pagesize=A4, rightMargin=55, leftMargin=55,
                      topMargin=53, bottomMargin=50).build(story)
    if len(PdfReader(cover).pages) != 1:
        raise RuntimeError('Cover must fit one page')
    writer = PdfWriter()
    writer.append(cover)
    writer.append(TMP / 'principal-proofs.pdf')
    writer.add_metadata({'/Title': 'Proofs and counterexamples: open-problem research',
                         '/Subject': 'Precise results, proofs, and limitations',
                         '/Author': 'Research run for Yitzchak Shmalo'})
    final = OUT / 'proofs-and-counterexamples.pdf'
    with final.open('wb') as stream:
        writer.write(stream)
    print(json.dumps({'output': str(final), 'pages': len(PdfReader(final).pages),
                      'source_notes': sources, 'completed_agents': complete}))


if __name__ == '__main__':
    main()
