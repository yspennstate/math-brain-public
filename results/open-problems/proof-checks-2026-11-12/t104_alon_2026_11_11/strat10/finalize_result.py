"""Assemble the final record from exact certificate ledgers; no new discovery."""
from pathlib import Path
from fractions import Fraction as F
import json

def main():
    old=Path('RESULT.md').read_text();summary=json.load(open('extension_summary.json'))
    proofs=old[old.index('PROVED: An exact new scalar'):old.index('NUMERICAL: The residual map')].strip()
    numerical=old[old.index('NUMERICAL: The residual map'):old.index('PROVED: exact_samples.json')].strip()
    samples=old[old.index('PROVED: exact_samples.json'):old.index('OPEN: New scale tables')].strip()
    definitions=old[old.index('PROVED: Here are the exact definitions'):old.index('OPEN: The final N=6 region')].strip()
    residual=old[old.index('OPEN: The final N=6 region'):old.index('PROVED partial (global_cover.json')].strip()
    final=summary['final_partition'];baseline=summary['baseline_partition'];w=json.load(open('new_residual_witness.json'));v=w['verification']
    parts=[f'''OPEN: The full sign theorem on STRAT9 region (11) remains unproved. The exact extensions, finite numerical map and remaining region (R10) are recorded below. No numerical finding is used as a proof.

## PROVED partial

PROVED: At N=6 every admissible frame and ratio is now covered for a<={summary['uniform_N6']} (previously 14/25). For every N>=6 the uniform ceiling is {summary['uniform_allN']} (previously 64/125). Larger ratio-dependent ceilings are listed below. Certificates: fine_cells.json, cubic_cells.json, stacked_cells.json, cubic_allN_cells.json, together with the inherited banks. Replay: verify_extensions.py and verify_summary.py; inherited dependencies are replayed by replay_all.py.

PROVED: There are 139 new rational cells: 42 fine ratio cells, 42 cells using sextic inequalities, 11 finer split-scale cells, and 44 simultaneous all-N cells. The latter use the three coefficients of padding identity (5). Every saved margin and residual-matrix condition is checked exactly. Replay: verify_extensions.py. The extra two ratio-dependent analytic bounds are replayed by verify_analytic.py.

PROVED partial: The final N=6 ledger has **80,355 visits**, **24,708 positive leaves**, **10,226 excluded leaves**, **5,244 OPEN leaves**, and **40,177 split nodes**. Of the positive leaves, 24,458 are certified for every N>=6. Certificate: global_cover.json. Replay: verify_cover.py. This reclassification had finished before the user's stop instruction; no further box splitting was run.

PROVED partial: The exact coordinate-volume ledger on the canonical root of volume 1152 is

| Ledger | Visits | Positive | Excluded | OPEN | Split | Positive volume | Excluded volume | OPEN volume |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Initial partition | 46,229 | 4 | 6,882 | 16,229 | 23,114 | 9/256 | 530145/512 | 59661/512 |
| Final partition | 80,355 | 24,708 | 10,226 | 5,244 | 40,177 | 21629007/1048576 | 1062587817/1048576 | 15467841/131072 |

PROVED: Both rows are exact partitions of the same root; they use different split geometries. The raw OPEN coordinate volume is larger in the final row, so no monotone volume reduction is claimed. These are chart-coordinate volumes, not a measure of admissible graphs or of (R10). The four initial positive boxes remain in the proved union. Certificates: baseline_cover.json and global_cover.json. Replays: verify_baseline.py and verify_cover.py. STRAT8's 5,272 OPEN leaves concern N=5 and are not an N=6 before count.

PROVED: The following are certified ceilings on each closed ratio interval, with the maximum of adjoining records available at a shared endpoint. Full small-ratio strips include their endpoints. Finite entries are rational certificates rather than estimated optima. The complete machine-readable table is ceiling_table.csv and extension_summary.json. Replay: verify_summary.py.

| r interval | Old N=6 | New N=6 | Old all N>=6 | New all N>=6 |
|---|---:|---:|---:|---:|''']
    for row in summary['ratio_table']:
        a='all scales'if row['N6_full_ratio_strip']else row['old_N6'];b='all scales'if row['N6_full_ratio_strip']else row['new_N6']
        c='all scales'if row['allN_full_ratio_strip']else row['old_allN'];d='all scales'if row['allN_full_ratio_strip']else row['new_allN']
        parts.append(f"| [{row['rlo']},{row['rhi']}] | {a} | {b} | {c} | {d} |")
    parts.append('\n'+proofs+'\n\n'+samples)
    parts.append('''PROVED: new_face_boxes.json adds 37 rational positive neighborhoods for every N>=6, each containing an endpoint satisfying every old (11) filter. Replay: verify_new_boxes.py. The chart helper precise_charts.py first rescales large integer columns by positive rationals; normalized frames and charts are invariant, while the inherited square-root enclosure becomes sufficiently narrow. No floating enclosure is accepted.

PROVED: The new residual is nonempty. new_residual_witness.json gives r=999/1000 and the connected endpoint scale

    a='''+v['actual_a']+''',
    T6='''+v['old']['T6']+''' > 0.

PROVED: This exact point misses both actual-scale and endpoint versions of every new moment bound, both analytic bounds, and every old, new, baseline and final positive box in every zero-edge chart. It has r<1, so the r=1 pressure-family theorem does not apply. Replay: verify_new_residual.py. Its finite positive sign does not certify a neighborhood or remove it from the continuous residual definition.

PROVED: Exact replay command, from this folder:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B replay_all.py

PROVED: replay_all.py runs every retained exact certificate sequentially and prints PASS/FAIL per script. Source hashes are pinned in provenance.json and checked by verify_provenance.py. Exact proof replay needs the standard library and SymPy; numerical discovery additionally uses NumPy/SciPy/Clarabel. All writes stayed in this folder, source folders were read-only, and no network, language-model workers or subagents were used. Discovery used at most four processes and single-thread numerical settings. The sandbox refused priority changes; no successful renicing is claimed. The replay has a 1 GiB peak-RSS guard, below the requested 4 GB limit.

OPEN: The final one-pass replay result will be recorded in replay_all.out and replay_summary.json.''')
    parts.append('## NUMERICAL\n\n'+numerical)
    audit=json.load(open('numeric_audit.json'))
    parts.append('NUMERICAL: An independent full-matrix calculation rechecked every retained raw residual sample and its numerical filters. The maximum N=6 formula discrepancy was '+str(audit['max_T6_formula_matrix_discrepancy'])+'. The directly evaluated local-search minimum was '+str(audit['least_local_T6_direct'])+'. No negative value was found. Replay: audit_numeric.py; data: numeric_audit.json. N=7 and N=10 checks used the N=6 residual sample, not samples of their entire residual domains.')
    parts.append('NUMERICAL: The exact final-residual witness has a approximately '+str(float(F(v['actual_a'])))+' and T6 approximately '+str(float(F(v['old']['T6'])))+'. These decimal renderings are not used in its proof.')
    parts.append('## OPEN\n\nOPEN: What remains is the continuous set (R10) below, including the corner neighborhood approaching (r,a)=(1,1) and the retained 5,244 OPEN leaves. The pressure family itself is proved, but no punctured corner neighborhood is proved. The numerical searches do not settle the sign there. The exact witness shows the final residual is nonempty. No claim is made that every OPEN leaf is feasible or that the whole residual has been localized to one quantified corner box. A separate STRAT11 run can attack the corner by a first-order expansion; this run starts no such work.\n\n'+definitions+'\n\n'+residual)
    parts.append('PROVED: Every canonical endpoint chart of a graph in (R10) lies in an OPEN leaf: all positive leaves are explicitly excluded, and every excluded leaf violates a necessary condition or has an already covered endpoint scale. The canonical root is t in [1,4], v1 in [-1,0], z1,z2 in [-4,4], v2 in [-1,1/2], z in [0,4]. Replays: verify_domain.py, zero_face.py, verify_cover.py. This implication is for N=6; N>=7 uses the stated Binf exclusions without treating the N=6 excluded ledger as an all-N cover.')
    parts.append('PROVED: Task: “shrink region (11), aiming to close it” — received 2026-11-13 at approximately 08:33 +04. Finalization and stop instruction received during this run; no additional splitting followed it.')
    Path('RESULT.md').write_text('\n\n'.join(parts)+'\n')
    with open('LOG.md','a')as f:f.write('\nPROVED partial: RESULT.md rewritten as the clean final record, with exact final ledger counts/volumes, before/after ceiling table, replay references, separated NUMERICAL findings and exact OPEN region (R10), including the corner and all 5244 OPEN leaves. No additional discovery is running. One full sequential replay is next.\n')
if __name__=='__main__':main()
