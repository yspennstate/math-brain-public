from pathlib import Path
import collections
import hashlib
import json
import re

BASE = Path('/workspace/scratch/bdbf99cce05c')
PAPER = BASE / 'paper_work'
ROOT = BASE / 'source_snapshot/fleet'
manifest = json.loads((BASE / 'source_snapshot/SOURCE_MANIFEST.json').read_text())
sha = manifest['snapshot_commit']
blobs = {x['path']: x.get('sha') for x in manifest['fleet_tree']['tree']}

themes = {
    'B01': ('Hub coordinates; crossing volumes', 'Special hub or overlap-two geometry; the unrestricted extraction is not established.'),
    'B02': ('Fourier volumes; skeletons', 'Conditional anchored-volume or strong-crossing refinement; retain all stated determinant, marginal and disjointness gates.'),
    'B03': ('Lower-order integrability; physical pairs', 'Conditional Fourier/Lp or logarithmic-potential estimate; an endpoint conclusion needs the stated independent residual or physical pair.'),
    'B04': ('Fourier volumes and weights', 'Weighted-volume refinement; feasibility of the weight and its coordinate marginal constraints are substantive.'),
    'B05': ('Hub coordinates; physical pairs', 'Near-null or slice calculation; interval bounds alone do not supply a Borel-set hub profile.'),
    'B06': ('Physical pairs; crossing blocks', 'Weighted pair/crossing receiver or conditional structural refinement; keep the actual physical residual.'),
    'B07': ('Skeletons; crossing volumes', 'Conditional minor extraction, pivot averaging or low-rank reduction; no exhaustive closure of the residual branch.'),
    'B08': ('Spectral spread; crossing blocks', 'Conditional spread/crossing decomposition or an example distinguishing sufficient certificates.'),
    'B09': ('Physical pairs; crossing volumes', 'Conditional pair/crossing smoothing; all self curvature is retained where the source proof permits it.'),
    'B10': ('Hub coordinates; Schur complements', 'Conditional Schur/Fresnel geometry; small nonzero pivots and shared-coordinate leakage require their stated gates.'),
    'B11': ('Rank-three geometry; crossing volumes', 'Projective/Pluecker or collision identity with a conditional analytic application; failure branches remain.'),
    'B12': ('Spectral certificates; finite coordinate cores', 'Deterministic stability through extra spectrum; the required physical spectral certificate is additional to three global eigenvalues.'),
    'B13': ('Law reductions; skeletons; volume weights', 'Conditional purification, leverage or canonical-core refinement; a reduction is not an unconditional density proof.'),
    'B14': ('Localization; frozen slices', 'Conditional localization or a fragmentation barrier; preserve normalization, measure dependence and interval/Borel distinction.'),
    'B15': ('Regularity and heat normal forms', 'Continuity and heat/approximate-identity statements require their own hypotheses; an interval cap alone is not continuity.'),
    'B16': ('Grouped projections; hub coordinates', 'Conditional grouped-bank or crossing refinement; dependence after projection must be retained.'),
    'B17': ('Gaussian benchmarks and explicit witnesses', 'A specified witness class or output level is studied; no sharp unrestricted upper constant follows.'),
    'B18': ('Hub coordinates; physical pairs', 'Heavy-anchor or rank-two reduction; a remaining near-null/misalignment gate is not automatically paid.'),
    'B19': ('Skeletons; proof graph; obstructions', 'A conditional proof-graph edge or counterexample to a stronger analytic shortcut; not a complete proof graph.'),
    'B20': ('Spectral spread; low-rank structural frontier', 'Conditional cross-cut/tail/recursion reduction; the low-rank survivor remains an explicit mathematical obligation.'),
}

# A status applies only to the contribution described in its note.  In particular,
# a source can contain additional ancillary claims that are not being endorsed.
overrides = [
 ('account01/B01/20260923T161404', 'P', 'fleet_gluing.tex', 'Sections 3--5: product-density L2 lemma and critical two-hub plus independent L2 residual; complete proofs independently checked in the gluing chapter. Source-disjointness is essential.'),
 ('account01/B01/20260923T150842', 'C', 'Hub coordinates; exact rank-two estimate', 'Uniform rank-one-leaf packet claimed with constant 256/sigma. Main setup and proof mechanisms inspected; remaining spectral case analysis and imported 128 half-Riesz constant not re-audited here. Retained as a scoped source claim, not certified by this catalogue.'),
 ('account01/B04/20260923T144427', 'P', 'fourier.tex', 'Entropy compression, finite Gibbs dual, and bounded-row deletion consequence read in full and incorporated; a remaining physical hub still needs a density receiver.'),
 ('account01/B04/20260923T154425', 'P', 'fourier.tex', 'Exact marginal factors and balanced six-coordinate consequence read in full and incorporated; canonical weights maximize entropy currency, not necessarily the complete bound.'),
 ('account02/B04/account02-B04-20260923T105109Z-auto11/REPORT_CORRECTION', 'E', 'fourier.tex; correction record', 'Read-back correction changes a malformed determinant identity parenthesis only. It does not amend a theorem or constant.'),
 ('account02/B04/account02-B04-20260923T105109Z-auto11/REPORT.md', 'C', 'fourier.tex', 'Fractional base-packing feasibility criterion is source-recorded; correction file retained. General Gibbs feasibility/deletion theorem is included in the paper, without asserting all source examples were separately re-audited.'),
 ('account01/B05/20260923T160511', 'A/G', 'hubs.tex; source algebra', 'Exact absorption of pure-longitudinal coordinates into an independent synthetic hub is valid (Section 3 read). Later diffuse-null applications are conditional on the disputed interval-to-Borel endpoint.'),
 ('account02/B05/20260923T130427', 'A/G', 'hubs.tex, frozen-slice lemma', 'Sections 5--6 frozen-slice Fourier and interval estimates are retained. Section 7 and Corollary 8.1 do not justify replacing the interval profile by a profile on every Borel set; the universal rough heavy-null bound <55.776 is not certified.'),
 ('account04/B14/20260923T141430', 'A/G', 'hubs.tex, frozen-slice lemma', 'Translation-uniform frozen-slice Fourier/interval estimate retained. Section 4 repeats the unsupported interval-profile-to-arbitrary-hub transfer; its <55.776 consequence is not certified.'),
 ('account02/B06/b06-20260923T152436', 'P', 'fleet_supplement.tex, supp:null-bank', 'Arbitrary-rank crossing block with an exactly linear bank; full conditioning/negative-moment proof checked and reproduced. Extra crossing singular values are retained.'),
 ('account03/B01/account03-B01-20260923T153212', 'P', 'fleet_supplement.tex, supp:rank-one-pair and supp:singular-pair-volume', 'Rank-one physical pair with arbitrary complementary curvature; full proof reconstructed from the scalar square kernel and random-slope negative moments. A sharper valid constant is given.'),
 ('account01/B06/20260923T130129', 'A', 'geometry.tex, geom:fullpair; lower_levels.tex', 'Determinant-only pair density conclusion is covered by the newer arbitrary-rank logarithmic-envelope theorem. Weighted ancillary quarter-Riesz formulas remain in the archive.'),
 ('account01/B09/20260923T154646', 'A', 'geometry.tex, geom:fullpair', 'Every quantitative indefinite physical pair plus the third global spectral direction is covered by the determinant-only arbitrary-rank theorem; its logarithmic bound does not require a pair condition-number parameter.'),
 ('account02/B09/20260923T154445', 'A', 'hubs.tex; structure.tex', 'Fixed-size two-physical-hub mixed-frame core is a specialization of retained grouped-hub/Fresnel results at its stated frame gate.'),
 ('account03/B03/20260923T162345', 'A', 'lower_levels.tex; fleet_gluing.tex', 'Exact-coloop aggregate half-Riesz and disjoint-square mechanisms are included at their independent-bank hypotheses; no generic half-Riesz-to-density upgrade is asserted.'),
 ('account03/B05/account03-B05-20260922T1237', 'A', 'lower_levels.tex; fleet_supplement.tex', 'Rank-two bilinear residual and independent outer-square mechanisms are retained; full generic HLS refinements are archived with their norms.'),
 ('account04/B09/20260923T101659', 'A', 'fourier.tex', 'Physical cross-determinant smoothing with arbitrary same-side curvature is an instance of the volume/decoupling theorem.'),
 ('account04/B11/20260923T111608', 'C', 'fourier.tex; rank-three source geometry', 'Disjoint-volume identity and sign-spliced compiler are conditional refinements. Ruled-side theorem itself is retained in geometry; two-sheet extraction is not declared complete.'),
 ('account01/B12/20260923T151555', 'P', 'fleet_supplement.tex, supp:anticommutator', 'Localized negative anticommutator and zero-loss disjoint/anticommuting spectral additions: full algebraic proof reproduced.'),
 ('account01/B12/20260923T162217', 'P/G', 'fleet_supplement.tex, supp:rank-reserve and supp:adaptive-rank', 'Krylov-footprint bound is valid but nonoptimal. Claim that reserve loss 2 rank(S) is unavoidable is incorrect: direct singular-value rank interlacing loses only rank(SP_H). Stronger theorem proved in manuscript.'),
 ('account02/B12/20260923T145451', 'P', 'fleet_supplement.tex, supp:pair-extraction and supp:six-carrier', 'Six-mode spectral-square carrier theorem checked and reproduced with the improved determinant-only pair bound; actual final matrix retained.'),
 ('account02/B12/account02-B12-20260922T1251', 'A', 'fleet_supplement.tex, supp:codimension-one', 'Older four-variable and codimension-one same-sign estimates are subsumed with a smaller constant by the physical finite-core theorem plus interlacing.'),
 ('account03/B12/20260923T144737', 'P', 'fleet_supplement.tex, supp:spill and supp:six-carrier', 'Spectral-square spill proved in full. Seven-mode qualitative carrier conclusion is subsumed by six-mode carrier result; original optimized seven-mode constant remains an ancillary source refinement.'),
 ('account03/B12/20260923T154231', 'P', 'fleet_supplement.tex, supp:signed-reserve', 'Separate positive/negative hostile-tail rank budgets: full min-max/rank-interlacing proof reproduced.'),
 ('account04/B12/20260923T081758', 'P', 'fleet_supplement.tex, supp:schur-protection', 'Complementary Schur protection for arbitrary large signed finite-rank additions: full factorization and shear singular-value proof reproduced.'),
 ('account04/B12/20260923T071518', 'A', 'fleet_supplement.tex, supp:schur-protection; structure.tex', 'Older two-core resonance separation is a more specific stability route. The stronger singular-Schur protection and finite-core bounds are retained; source resonance examples archived.'),
 ('account04/B07/20260923T161510', 'A', 'fleet_supplement.tex, supp:rank-reserve; structure.tex', 'An r+3 coordinate diagonal core survives a rank-r addition by direct singular-value rank interlacing and norm-tail erosion; general principle proved in supplement.'),
 ('account04/B13/20260922T231352', 'A', 'geometry.tex, geom:laws and geom:ruled', 'No-attainment purification and rough ruled-side transfer retained with explicit interval approximation; no interval-shaped extremizer is inferred.'),
 ('account04/B13/20260923T121154', 'A', 'geometry.tex, geom:laws', 'Coordinatewise positive-kernel purification retained; conditional exterior-energy application remains subject to its geometric gate.'),
 ('account04/B05/20260923T031319', 'A', 'geometry.tex, geom:ruled; source two-sheet gate', 'Rough ruled-side theorem retained; extra two-sheet receiver remains conditional on its source hypothesis.'),
 ('account04/B16/20260922T231542', 'A', 'geometry.tex, geom:ruled', 'Ruled-side estimate retained with product-projection provenance and rough-law transfer. It does not cover the opposite half-line.'),
 ('account04/B14/20260923T101157', 'A', 'geometry.tex, geom:ruled; fleet_gluing.tex', 'Cap-preserving approximation and conditional integration mechanisms retained; all original perspective parameters and integrability costs remain in source.'),
 ('account01/B15/20260923T160313', 'P', 'fleet_gluing.tex', 'Fixed-kernel exact normal form independently checked in full and reproduced; this is an equivalence, not an a priori uniform upper bound.'),
 ('account03/B15/20260923T163043', 'P', 'fleet_gluing.tex', 'Countable-core heat formulation and regularity ledger independently checked in full; no pointwise regularity follows from weak convergence alone.'),
 ('account04/B15/20260923T151702', 'P', 'fleet_gluing.tex', 'Pivot-neutral hyperbolic Lp plus disjoint square and continuity independently checked in full; independence and Lp conjugacy retained.'),
 ('account04/B15/20260922T232152', 'A', 'geometry.tex; fleet_gluing.tex', 'Ruled interval transfer retained; continuous-representative closure must be distinguished from a mere essential density cap.'),
 ('account04/B19/20260923T071203', 'P', 'fleet_supplement.tex, supp:interpolation-obstruction', 'Explicit probability densities have bounded L3 norm and square-root interval profile but unbounded height. Complete construction checked and reproduced.'),
 ('account04/B19/20260923T151700', 'P', 'fleet_supplement.tex, supp:moving-ridge', 'Fixed target-valid matrix with one independent hub and a cap-one dependent triple has arbitrarily high density. Full construction and spectrum checked; this is not a product-law counterexample.'),
]

rows=[]
for file in sorted(ROOT.rglob('*.md')):
    relative=file.relative_to(ROOT).as_posix()
    account,slot=relative.split('/')[:2]
    text=file.read_text()
    headings=[s for s in text.splitlines() if re.match(r'^#{1,4}\s',s)]
    title=next((h.lstrip('# ').strip() for h in headings if h.startswith('# ') and h.strip()!='# Status'),file.parent.name)
    title=''.join(c for c in title if ord(c)>=32)
    target,note=themes[slot]
    status='C'
    if slot=='B17':
        status='W'
        target='gaussian_benchmarks.tex; explicit witness archive'
        note='Witness-specific analysis; selected strongest Gaussian/Lindeberg and cone-tip statements reproved in the benchmark chapter. Other finite examples and numerical diagnostics are archived, not general upper bounds.'
    elif slot=='B15':
        target='fleet_gluing.tex; regularity source archive'
        note='Regularity/heat formulation. Strongest common results are reproved in the gluing chapter; ancillary kernel-specific constants and counterexamples remain separately stated in the source.'
    for pattern,st,ta,no in overrides:
        if relative.startswith(pattern):
            status,target,note=st,ta,no
            break
    if account=='account02' and slot=='B17' and '1142Z' in relative:
        note='Diffuse Lindeberg global Gaussian ceiling: finite means/variances, convergent covariance and mean, vector Lindeberg and vanishing row leverage are explicit. Complete benchmark proof independently checked.'
    if slot=='B17' and ('154011' in relative or '163000' in relative):
        note='One-heavy Gaussianized family, exact cone-tip optimizer and uniform ceiling <4.111374. Two sources obtain the same ceiling. Output level zero only; Complete benchmark proof independently checked.'
    if slot=='B17' and '081528' in relative:
        note='Householder cube exact cone-tip value 6 sqrt(3) artanh((sqrt(2)-1)/sqrt(3)) = 2.534355...; benchmark proof independently checked; weaker than the 3 sqrt(2) asymptotic lower witness.'
    rows.append({
        'id':f'F{len(rows)+1:03d}', 'path':relative,'title':title,
        'blob_sha':blobs.get(relative), 'sha256':hashlib.sha256(file.read_bytes()).hexdigest(),
        'lines':len(text.splitlines()), 'status':status,'manuscript_location':target,'note':note,
        'url':f'https://github.com/{manifest["repository"]}/blob/{sha}/proofnet24/QFORM-density/fleet-2026-09-22/{relative}',
        'theorem_headings':[h for h in headings if re.search(r'Theorem|Lemma|Corollary',h)],
    })

out={
    'repository':manifest['repository'],'snapshot_commit':sha,'report_count':len(rows),
    'scope':'All 153 downloaded latest fleet records indexed. Full proofs re-audited selectively for the retained strongest contributions. Conditional refinements are catalogued without blanket certification.',
    'status_counts':dict(collections.Counter(r['status'] for r in rows)), 'records':rows,
}
(PAPER/'fleet_catalogue.json').write_text(json.dumps(out,indent=2)+'\n')

lines=[
 '# Fleet coverage and proof-scope audit', '',
 f'Source checkpoint: `{manifest["repository"]}@{sha}`. This catalogue covers all **{len(rows)}** downloaded Markdown records from the selected latest fleet reports, including one read-back correction. Exact repository links and hashes are included in `fleet_catalogue.json`; the original files are preserved in `source_snapshot/fleet`.', '',
 '## What this audit certifies', '',
 'Every downloaded record was indexed by title, main theorem headings, source path and mathematical theme. Full proof checking was concentrated on the strongest distinct contributions selected for the manuscript and on suspected scope errors. A source label such as “PROVED” is not itself evidence of correctness. This is not a claim that every ancillary inequality, diagnostic script, spectral case split or imported theorem in all 153 reports received an independent line-by-line review.', '',
 'The manuscript includes complete proofs of its own stated results. Many fleet records are successive conditional refinements of the same volume/hub/Schur argument, so the catalogue preserves them without converting each into a new unconditional theorem. A row marked C is not being asserted to be fully subsumed by the manuscript: its source-specific claim remains archived with its hypotheses and unverified dependencies.', '',
 '| Code | Meaning |', '|---|---|',
 '| P | Selected principal contribution is reproved in the manuscript (or explicitly checked by the named chapter owner and an independent reader). |',
 '| A | Named principal analytic conclusion or mechanism is represented by a retained broader theorem; ancillary statements remain in the source. |',
 '| C | Conditional refinement, structural identity, specialized receiver or source-specific example preserved without a new blanket proof certification. |',
 '| G | A particular inference or optimality assertion has a proof-scope defect; valid earlier steps are separated from it. |',
 '| W | Witness-class analysis or explicit example. Selected strongest examples are handled in the benchmark chapter; none is an unrestricted upper bound. |',
 '| E | Editorial correction record. |', '',
 '## Corrections that materially affect the proof map', '',
 '### 1. Interval profiles do not become Borel-set profiles', '',
 'The frozen-slice proofs in account02/B05 `20260923T130427Z` (Sections 5–6) establish an oscillatory estimate and a square-root bound for the measure of an interval. Their Section 7 then invokes a receiver for an arbitrary cap-one independent hub. Such a receiver requires control on every Borel set, or an additional interval-support/regularity hypothesis on the hub. The layer-cake superlevel sets of a translated, rescaled rough hub density need not be intervals. The manuscript states this stronger Borel hypothesis explicitly in `lem:hub-profile`.', '',
 'Accordingly, that report’s `<55.776` full rough heavy-null conclusion and Corollary 8.1 are not certified by the displayed proof. The same issue occurs in account04/B14 `20260923T141430Z`, where the valid affine frozen-slice theorem is followed by the same unsupported transfer. Pure-longitudinal absorption in account01/B05 `20260923T160511Z` is valid algebra and remains useful; applications importing the preceding endpoint are conditional. This audit does not disprove the desired heavy-null theorem.', '',
 '### 2. Krylov rank is not the necessary spectral reserve', '',
 'Account01/B12 `20260923T162217Z` correctly bounds the rank of `(A0+S)^2-A0^2` by `dim(Ran S+A0 Ran S)`, at most twice the rank of S. Its example with a rank-two difference does not show that a reserve loss of twice the rank of S is necessary. Direct singular-value interlacing of `(A0+S)P_H` loses only `rank(SP_H)`. The manuscript proves this stronger result in `supp:rank-reserve`, including an operator-norm remainder and an adaptive spectral threshold.', '',
 '### 3. Negative results retain their exact scope', '',
 'The moving-ridge example keeps one hub independent while allowing dependence inside a triple with bounded joint density. It is a counterexample to a weakened independence premise, not to the original product-law conjecture. The L3 plus square-root interval example disproves a general interpolation implication, not the existence of a more structured quadratic-form argument. Both are proved in `fleet_supplement.tex`.', '',
 '## Strongest additions represented in the paper', '',
 '- Critical two-hub Fourier gluing with an independent scalar L2 residual, plus the product-density L2 inequality (`fleet_gluing.tex`).',
 '- Exact weighted volume factors, Gibbs duality, and the bounded-row deletion consequence (`fourier.tex`).',
 '- An arbitrary-rank crossing block with one exactly linear bank; a rank-one physical pair with an arbitrary complementary phase (`fleet_supplement.tex`).',
 '- Spectral-square spill, six-mode coordinate carriers, localized anticommutator stability, stronger low-rank reserve bounds, adaptive signed tails, and complementary Schur protection (`fleet_supplement.tex`).',
 '- Rough-law continuity and fixed/countable heat-kernel formulations, kept separate from essential boundedness (`fleet_gluing.tex`).',
 '- Selected Gaussian/Lindeberg benchmarks and one-heavy cone-tip exclusions (`gaussian_benchmarks.tex`, separately audited by its chapter owner).', '',
 '## Per-record catalogue', '',
 'The source link in each row fixes the repository snapshot. The mathematical location column is a coverage pointer, not a claim that every detail in that source was copied or independently verified.', '',
 '| ID / source | Principal subject | Status | Manuscript location and scope |',
 '|---|---|---|---|',
]
for r in rows:
    rel=r['path']; acc,slot,run,filename=rel.split('/')
    label=f'{r["id"]} · {acc}/{slot} · {run}' + (' · correction' if filename!='REPORT.md' else '')
    clean=lambda s:s.replace('|','\\|').replace('\n',' ')
    lines.append(f'| [{label}]({r["url"]}) | {clean(r["title"])} | {r["status"]} | **{clean(r["manuscript_location"])}.** {clean(r["note"])} |')
lines += ['', '## Reproducibility and outstanding verification', '',
 'The catalogue generator checks that every downloaded fleet Markdown file appears exactly once and records both its Git blob identifier (when present in the source manifest) and a local SHA-256 digest. It does not execute the fleet’s diagnostic scripts or treat their numerical output as proof. Coverage codes are deliberately conservative: source-specific C refinements remain available for future independent checking, and no source-status counter is used to estimate a percentage of the conjecture solved.', '',
 'Classical literature attribution and the limits of the primary-source search are recorded separately in `LITERATURE_AUDIT.md`. The exact conjecture remains open; there is no complete end-to-end proof to certify.', '']
(PAPER/'FLEET_COVERAGE_AUDIT.md').write_text('\n'.join(lines))
assert len(rows)==153
assert len({r['path'] for r in rows})==153
print(json.dumps({'reports':len(rows),'status_counts':out['status_counts'],'missing_blob_ids':sum(r['blob_sha'] is None for r in rows)}))
