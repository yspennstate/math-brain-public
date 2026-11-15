"""Finish the local handoff, with REPORT.md written last."""
import json,hashlib,datetime
from pathlib import Path
root=Path('.');now=datetime.datetime.now().astimezone().isoformat(timespec='seconds')
audit=json.loads(Path('final_audit.json').read_text());receipt=json.loads(Path('run_receipt.json').read_text())
detail=json.loads(Path('audit.json').read_text());r=json.loads(Path('restriction_address.json').read_text())
assert audit['status']=='CHECKED' and audit['independent_census_witnesses_agree']
assert len(r)==8 and all('truth_table_checks' in x for x in r[:3])
task='Task: “Do the brief fully and carefully” — FEIB11, 10 November 2026, 02:58 +04 (BRIEF.md timestamp).'
Path('STATUS.md').write_text(f'''# FEIB11 status

Completed {now}.
All four numbered items are addressed, with the open conjectures separated from proved and checked results.
Files: REPORT.md, RESULTS.md, PROOFS.md, LITERATURE.md; all scripts and numerical receipts are in this folder.
The complete five-variable NPN census and independent C scan agree. All-through-four direct integer checks pass.
The literal all-I quadratic target is false; the corrected bound and near-linear literature consequence are written out.
No subagents, mesh/board posts, global memory writes, git operations, or writes outside this folder were performed.
NEXT: no further assigned computation is pending. The launching session can review REPORT.md and publish selected findings.
OPEN: the general linear WC exponent, its sharp constant/extremizers, and the q=0 containment conjecture.

{task}
''')
selected=[p for p in root.iterdir() if p.is_file() and p.name not in ['events.jsonl','stderr.log','REPORT.md','manifest.json','storage_audit.json']]
manifest={p.name:dict(bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in selected}
Path('manifest.json').write_text(json.dumps(dict(created=now,files=manifest),indent=2))
bytes_total=sum(p.stat().st_size for p in root.rglob('*') if p.is_file())
assert bytes_total<1_000_000_000
Path('storage_audit.json').write_text(json.dumps(dict(timestamp=now,bytes_before_report=bytes_total,decimal_GB=bytes_total/1e9,limit_bytes=1_000_000_000),indent=2))
report=f'''# FEIB11 report

Completed the Renyi containment brief. The general linear WC conjecture remains OPEN. The main correction is PROVED: the requested bound log2(1/WC)<=C I^2 fails near constants. AND_n is a counterexample family. The valid fixed-level consequence is log2(1/WC)<=16I^2+13I, hence <=29I^2 for balanced functions. The known KKLMS theorem supplies the stronger large-I bound O(I log(2+I)). Full arguments are in [PROOFS.md](PROOFS.md).

## Verdicts on the numbered items

1. CHECKED / PROVED from read sources: [LITERATURE.md](LITERATURE.md) audits every named paper and the additional O'Donnell–Tan composition paper. The reviewed text did not identify WC as a named FEI statistic; this is a limited-search finding. PROVED: log2(1/WC_q)=D_(1-q)(nu||mu x mu) for the containment coupling. Published FMEI cases transfer to WC, while the known general result retains a logarithmic loss. No general FMEI or WC proof was found.

2. CHECKED: all truth tables through four variables, all 616,126 five-variable NPN classes, and 200,000 draws each at six and seven variables. Every requested family was calculated, with explicit tables through eighteen variables and compressed formulas beyond that. Over the complete five-variable census, max log2(1/WC)/I is 1.2490814075488517 bits per unit influence, at 0x018bf5cd. The balanced max of log2(1/WC)/(I-1) is 3.2848959907638324 bits per unit excess influence, at 0x000f33ff. These values and matched H/A comparisons are in [RESULTS.md](RESULTS.md), census_n5_npn.json and independent_census.json. PROVED: address functions force any universal raw WC constant to be at least 2log2(8/3), approximately 2.830075. OPEN: global extremizers and the optimal constant.

3. PROVED: the corrected quadratic bound; the near-linear literature corollary; linear WC for monotone/unate functions (constant 24), symmetric functions (using published FEI), read-once bounded-gate formulas, and fixed real degree d (A<=(2d-2)I). PROVED: WC and every WC_q multiply under disjoint XOR products. PROVED: address functions refute a restriction induction that charges each coordinate by C Inf_i, including the uniform-coordinate average version. The exact recursion and failed induction are written out and checked in restriction_address.json. OPEN: the general linear exponent. For nearly constant functions, the meaningful strengthened normalization removes both empty spectral atoms: WC=1-v+v^2 WC_plus, with conjectured exponent C I/v for WC_plus.

4. CHECKED: q=1, 1/2, 1/4, 1/10, 1/20, 1/100 and the q=0 limit on every census and sample. The complete five-variable max L_q/I grows from 1.2490814075488517 to 2.1625 bits per unit influence; the extremizer changes to AND_5 as q decreases. The balanced normalized maximum grows from 3.2848959907638324 to 4. PROVED: L_q decreases with q and tends to A. OPEN: a bound uniform over dimensions as q decreases to zero.

## Checks and reproducibility

CHECKED: [audit.json](audit.json) records dense direct integer Fourier and containment calculations on all 65,812 truth tables through four variables, with exactly zero WC discrepancy. An independent C program recomputed every five-variable maximum on the full NPN census; its largest discrepancy from Python is {audit['independent_census_max_ratio_error']:.4g} bits per unit influence. The audit also checks the derivative identity, conditional normalization, degree granularity, monotone identity, tensor products, NPN invariance and analytic family formulas. Truth tables are hexadecimal, with bit x set when f(x)=-1. Floating numerical agreement is not an exact-real extremum certificate.

Run `python3 run.py --regenerate-npn` and `python3 summarize.py`. The measured numerical run in run_receipt.json took {receipt['wall_seconds']:.3f} seconds of wall time and used peak child RSS {receipt['max_child_rss_bytes']} bytes ({receipt['max_child_rss_bytes']/2**30:.6f} GiB). This is computation time, not total research time. Jobs used one numerical thread and inherited niceness 10. Later audit additions have their own audit.json receipt. The folder held {bytes_total} bytes before this report, recorded in storage_audit.json, below its disk limit. Scripts, sources, logs, tables and checksums are retained locally.

The brain helped identify the perfect-matching-plus-coins construction; the rebuilt function checks at H/(I-1)=6.521845710923046 in families.json. The math store was unavailable. The newer recalled symmetric constant was not used. Fleet rules prohibited publishing, mesh posting and writes outside this folder, so this report is the handoff; no external state was changed.

{task}
'''
# Pull both long numerical extrema from their receipts rather than maintaining duplicate literals.
d=json.loads(Path('census_n5_npn.json').read_text())
actual=d['best_balanced_over_I_minus_1']['1.0']['ratio']
report=report.replace('3.2848959907638324',format(actual,'.17g'))
Path('REPORT.md').write_text(report)
print(json.dumps(dict(completed=now,folder_bytes_before_report=bytes_total,report_bytes=Path('REPORT.md').stat().st_size,manifest_files=len(manifest),balanced_max=actual),indent=2))
