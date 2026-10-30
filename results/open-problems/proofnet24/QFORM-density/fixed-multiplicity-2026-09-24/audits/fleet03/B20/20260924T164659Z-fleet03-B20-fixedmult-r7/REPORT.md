# fleet03/B20 r7 — fixed-multiplicity release gate and exact nine-value retuning

Run: `20260924T164659Z-fleet03-B20-fixedmult-r7`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

## Executive verdict

1. **Pinned source, literal status:** `GAP_REPAIRABLE_LOCAL`. The current self-contained source is
   `yspennstate/math-open-problems@eeb752c8943536541b34b42b8bf48e924f4d3d2f`,
   `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`,
   blob `19fb119877426b640b2c0dae19ec2f78a399fe11`.
   I read every line 1--955. The only mathematical source defect found is local wording in the negative-tail part of the hyperbolic-pair proof: the maximizing physical coordinate for the negative exponential vector must be chosen independently of the maximizing coordinate for the positive exponential vector. Because the two vectors have the same Euclidean norm, the cutoff and constants are unchanged. With that repair, the mathematical nine-value chain passes this complete reconstruction.

2. **New independently reconstructed constant improvement:** with the same proof architecture but retuned
   [
   d={3757over50000},qquad
   p={14251over5000000},qquad
   h={164557over2000000},qquad
   q={3687over40000},
   ]
   the pinned argument proves
   [
   oxed{s_9(A)ge s>0Longrightarrow
   |p_{X^TAX+b^TX+c}|_{infty,mathrm{ess}}
   <{1801over5}{K^2over s}=360.2,{K^2over s}.}
   ]
   All quantifiers of the pinned theorem are preserved. This is an independent reconstruction of the fleet02/B02 360.2 candidate, not a second self-audit by its author. The owner-required two-independent-review gate for this exact 360.2 retuning is **not** declared satisfied by this file alone.

3. **Threshold release accounting:** the repository now contains two complete mathematical reviews supporting a multiplicity-eight theorem with a safe constant (2400K^2/s), so multiplicity eight remains the lowest source-complete, two-review mathematical chain I can presently identify. A newer package claims a multiplicity-five theorem with constant (2400K^2/s) and contains two written PASS audits, but the package advertises a 1,093-line `main.tex` that is absent from the current Git tree. Therefore I do **not** mark multiplicity five source-level release-ready from this run. Multiplicity four and the unrestricted multiplicity-three bounded-density theorem remain open.

4. **Regularity:** the assembled fixed-multiplicity theorems are essential-density statements globally. The order-three no-pivot Fourier receiver gives a continuous (C_0) density on that branch. The pivot assembly used here does not establish a globally continuous representative.

## A. Complete source audit of the pinned nine/400 manuscript

Source pin:
- commit: `eeb752c8943536541b34b42b8bf48e924f4d3d2f`
- blob: `19fb119877426b640b2c0dae19ec2f78a399fe11`
- declared SHA-256: `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`
- source lines: 955

Line ledger:

- 1--86: **PASS** — theorem quantifiers, normalization, scaling, architecture.
- 87--160: **PASS** — Fourier convention, Gaussian regularization, inversion, Plancherel, Riesz half-potential.
- 161--215: **PASS** — singular-value perturbation, signed Schur spectral count including the singular limit, diagonal dominance.
- 216--297: **PASS** — geometric Brascamp--Lieb heat flow, rough-law limiting argument, product-projection density, scalar Fourier powers.
- 298--396: **PASS** — decoupling, graph determinant/Jacobian estimate, crossing-volume envelopes and the determinant exponent.
- 397--527: **PASS** — grouped mollified-(L^2) compiler, determinant-weighted Hölder, entropy inequality, literal physical-row promotion, terminal hubs, (E_3) density and (E_2) full half-potential receivers.
- 528--562: **PASS** — scalar square and definite-pair changes of variables.
- 563--610: **GAP_REPAIRABLE_LOCAL** — negative hyperbolic tail should select its own maximizing coordinate; repair below.
- 611--662: **PASS** — quarter-power concentration, logarithmic potential, uniformity in affine terms.
- 663--766: **PASS** — disjoint-minor sampling, nonsymmetric interpolation support, global rank (le3r), restricted rank (le r), diagonal/off-diagonal separation, random literal-coordinate cut.
- 767--860: **PASS** — full pair half-potential, five-direction half-potential, exhaustive nine-direction pivot/no-pivot assembly and (K^2/s) scaling.
- 861--935: **PASS** — spectral-tail/overlap identity; singular seeds correctly excluded.
- 936--955: **PASS** — threshold/scope accounting, acknowledgment, bibliography.

The two bibliography entries were also checked against their primary arXiv records: Bennett--Carbery--Christ--Tao, arXiv:math/0505065, and Rudelson--Vershynin, arXiv:1402.4492, match the titles/authors cited by the manuscript.

### Hyperbolic local repair

In the indefinite-pair proof the linearized form is
[
u e^t+w e^{-t},qquad |u|=|w|=ho_0.
]
For the positive tail choose a physical coordinate (i_+) satisfying
[
|u_{i_+}|ge ho_0/sqrt2.
]
For the negative tail choose, independently,
[
|w_{i_-}|ge ho_0/sqrt2.
]
There is no need for (i_+=i_-). The positive and negative cutoff calculations are identical because the two vectors have equal norm. The middle interval length and both tail costs are unchanged, so the source envelope
[
6+log_+rac{16sqrt D}{|z-v|}
]
and every downstream constant remain valid. Thus this is a literal-source wording defect, not a change of theorem or constant.

No probabilistic independence is asserted after a rotation anywhere in this repair.

## B. Exact retuning to 360.2 at multiplicity nine

Work first with (K=s=1). Define
[
d={3757over50000},quad
p={14251over5000000},quad
h={164557over2000000},quad
q={3687over40000},quad
kappa=h^2.
]
A scalar pivot is (|A_{ii}|ge d), and a pair pivot is a principal determinant of modulus at least (p).

### B.1 Structural inequalities

In the no-pivot chamber,
[
|A_{ii}|<d,qquad
|A_{ij}|^2<p+d^2<q^2.
]
The strict margin is
[
q^2-(p+d^2)={441over40000000000}>0.
]
The volume-interpolation proof for (kle3) requires
[
d+h<1,qquad
1-d-q-4h>0,qquad
1-d-2q-9h>0.
]
Here the exact margins are
[
1-d-h={1685163over2000000},
]
[
1-d-q-4h={503571over1000000},
]
[
1-d-2q-9h={7over2000000}.
]
Therefore the source Proposition 7.3 proof goes through verbatim with this retuning:
[
s_{4k-3}(A)ge1, 	ext{no pivot}
quadLongrightarrowquad
V_k(A)ge h^{2k},qquad k=1,2,3.
]

For completeness, the only rank/diagonal-dominance step is this. If
(V_{r+1}<h^2V_r), sampled interpolation gives
(|E|_F<(r+1)h), global rank at most (3r), and restricted rank at most (r).
Since (4k-3ge4r+1), at least (r+1) diagonal defects in the seed complement have modulus at least (1-(r+1)h). Their corresponding restricted-(R) diagonal entries have modulus at least
[
1-(r+1)h-d,
]
while each off-diagonal entry is (<q+(r+1)h). Strict row diagonal dominance follows exactly from
[
1-d-rq-(r+1)^2h>0
]
for (r=1,2), contradicting restricted rank (le r).
For (r=0), (|A|<d+h<1). No symmetry of the auxiliary interpolation matrix is used.

### B.2 No-pivot branch

The marginal-free order-three receiver has
[
C_3=3sqrt2,e(9/2)^{1/6}.
]
A fair literal-coordinate cut gives
[
Z_3ge4^{-3}h^6,
]
hence
[
|p_Q|_inftyle {2C_3over h}
={6sqrt2,e(9/2)^{1/6}over h}.
]

Use the exact rational upper certificates
[
e<{271828183over10^8},qquad
sqrt2<{141421357over10^8},qquad
(9/2)^{1/6}<{12848983over10^7}.
]
The first follows from
[
e<sum_{j=0}^9{1over j!}+{11over10cdot10!}
={4697191over1728000}
<{271828183over10^8},
]
where the final margin is (7/5400000000).
The other two are certified by
[
(141421357/10^8)^2-2
={215721449over10^{16}}>0,
]
and
[
(12848983/10^7)^6-{9over2}
={138155852642983616598199542383579569over10^{42}}>0.
]
Consequently
[
{2C_3over h}
<
{1481833782698283801136119over4113925000000000000000},
]
and
[
{1801over5}-{2C_3over h}
>
{2002301716198863881over4113925000000000000000}>0.
]

### B.3 Scalar-pivot branches

The Schur complement after a scalar pivot retains at least eight unit-scale directions, hence at least five. The source five-direction half-potential proposition retunes with the same (d,p,h).

The no-pivot Schur branch obeys, conservatively,
[
d^{-1/2}C_2sqrt{2/h}<4cdot14cdot5=280<360.2,
]
because (d>1/16), (h>2/25), and (C_2<14).

The pair-pivot Schur branch obeys
[
16d^{-1/2}p^{-1/4}<16cdot4cdot5=320<360.2,
]
because (p>1/400).

For the scalar-pivot-inside-Schur branch, the exact expression is
[
B_{ss}=d^{-1/2}+{8+pi+4log2+8log5over d}.
]
Use
[
d^{-1/2}<{3649over1000},
]
with certificate
[
d(3649/1000)^2-1={25210157over50000000000}>0,
]
together with
[
pi<{22over7},qquad
log2<{69315over100000},qquad
log5<{160944over100000}.
]
The logarithm inequalities follow because the positive exponential Taylor polynomials give
[
sum_{j=0}^7{(69315/100000)^jover j!}-2
=
{3016283573717844627378512063over716800000000000000000000000000000}>0,
]
and
[
sum_{j=0}^{10}{(160944/100000)^jover j!}-5
=
{2920443557292926742337563197984336603over
582076609134674072265625000000000000000000}>0.
]
The classical (pi<22/7) follows, for example, from the positive Dalzell integral.
Thus
[
B_{ss}
<
{9472807051over26299000}
=360.196473ldots
]
and the exact target slack is
[
{1801over5}-{9472807051over26299000}
={92749over26299000}>0.
]

### B.4 Pair-pivot branches

A definite pair gives
[
|p_Q|_inftylepi p^{-1/2}<4cdot20=80<360.2.
]

For an indefinite pair, the source proof gives exactly
[
B_{m ind}
=p^{-1/2}igl(10+4log10igr)+{1over e}.
]
Use
[
p^{-1/2}<{187311over10000},
qquad
log10<{2302586over1000000},
qquad
{1over e}<{9197over25000}.
]
The first is certified by
[
p(187311/10000)^2-1
={2188184971over500000000000000}>0.
]
For the logarithm,
[
sum_{j=0}^{13}{(2302586/10^6)^jover j!}-10
=
{4416312567305049537172236641389807826709638003031634827812753305634860964939
over
590625000000000000000000000000000000000000000000000000000000000000000000000000000}
>0.
]
For the reciprocal exponential,
[
e>sum_{j=0}^8{1over j!}={109601over40320}
>{25000over9197},
]
where the final margin is (397/370823040>0).
Therefore
[
B_{m ind}
<
{450248443123over1250000000}
=360.1987544984,
]
with exact slack
[
{1801over5}-{450248443123over1250000000}
={1556877over1250000000}>0.
]

All normalized branches are therefore strictly below (1801/5).

### B.5 Scaling and scope

Set (Y=KX) and
[
widetilde Q
=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c.
]
Then (Y) has independent coordinate densities bounded by one,
(s_9(A/s)ge1), and
[
Q={sover K^2}widetilde Q.
]
Density scaling yields
[
oxed{|p_Q|_{infty,mathrm{ess}}
<360.2,K^2/s.}
]
No moment, support, iid, log-concavity, compactness, connected-support, sign, exact-rank, leverage, diagonal-basis, or post-rotation-independence assumption has been introduced.

This retuning does **not** upgrade global regularity. The no-pivot order-three branch is (C_0); the full theorem is recorded only as an essential-density theorem.

## C. Release and threshold accounting

### C.1 Multiplicity eight

A complete replacement proof is present at
`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/fleet01/B13/20260924T152809Z-fleet01-B13-FIXMULT-auto11/EIGHT_EIGENVALUE_REPLACEMENT.md`.

Two separate complete mathematical reviews are present at, among others:
- fleet03/B08, blob `f7ac28a10e99a7dac1b343ee5b86c0a25cdc1951`;
- fleet01/B07, blob `ab46124605dc2795c2fd65bbc62a0b97e9894b9b`.

Those artifacts support
[
s_8(A)ge sLongrightarrow
|p_Q|_{infty,mathrm{ess}}<2400K^2/s.
]
Global continuity is not claimed.

### C.2 Multiplicity five: strong mathematical claim, packaging gate still open

Current master contains
`results/five-singular-values-2026-09-24/` with:
- `README.md`;
- `FULL_REAUDIT_2026-09-24.md`;
- `Quadratic_Forms_Proof_Audit_2026-09-24.md`.

The two audit documents both report PASS/no fatal gap for
[
s_5(A)ge sLongrightarrow
|p_Q|_{infty,mathrm{ess}}<2400K^2/s.
]
However, the package itself says the complete 1,093-line manuscript is stored beside those audits as `main.tex`, while the current Git tree contains no such file and in fact contains no additional `.tex` source under the fixed-multiplicity root beyond the pinned nine paper and historical seventeen manuscript.

Therefore this B20 release gate records:
- mathematical audit claim for (s_5): **SUPPORTED BY TWO WRITTEN PASS AUDITS**;
- self-contained source availability: **GAP**;
- fresh source-line audit by this run: **BLOCKED BY MISSING SOURCE**;
- owner-level release-ready status: **NOT GRANTED BY THIS RUN**.

This is not evidence that the (s_5) theorem is false. The exact next release obligation is to commit/pin the advertised 1,093-line source and obtain/source-identify genuinely separate complete line reviews against that exact blob.

### C.3 Multiplicity four and three

The current exact two-star obstruction
[
A_m=S_moplus S_m,qquad
S_m=egin{pmatrix}0&w^T\w&0end{pmatrix},quad
w=m^{-1/2}(1,ldots,1),
]
has spectrum ({1,1,-1,-1}), no scalar/pair pivot at the baseline scale for large (m), and every disjoint third-order crossing minor equal to zero. Thus the five-value order-three extraction cannot simply be repeated at four.

This is a mechanism counterexample, not a QFORM counterexample. For the natural zero-affine product stress, the two independent star terms already have a continuous bounded convolution; the repository proof gives (|p_Q|_inftyle4sqrt e).

The strongest current lower-threshold supporting result I verified is a full negative-half-moment theorem under three large singular values. It is **not** a density theorem. Therefore:
- multiplicity four bounded density: **OPEN**;
- multiplicity three bounded density: **OPEN / NOT PROVED / NOT DISPROVED**.

The next genuine analytic target is a product-preserving shared-hub/shared-bank receiver that consumes overlap-one or two-star currency before an absolute-value step, especially when the shared physical diagonal is zero or arbitrarily small. Generic (E_2) information alone cannot be promoted to an (L^infty) endpoint.

## D. Keeper / operational status

A real B20 login was created for this run. A create-only current-hour keeper lease was attempted, but the platform safety layer blocked that external write. I did not bypass or replace the denied lease. Consequently no scheduler mutation was made.

A fresh current-account scheduler inventory showed the same twenty managed QFORM tasks present and enabled on their hourly schedules, with email and push notifications off. No task was created, duplicated, paused, resumed, retitled, rescheduled, or re-notified in this run.

Repository transport and durable source-memory files are not native learned-memory ingestion. Unless an authenticated receiver is actually exposed and used, this run remains `WITHOUT_VERIFIED_BRAIN`.

## E. Next exact obligations

1. Obtain a second genuinely separate complete review of the exact nine/360.2 retuning before calling that constant independently validated.
2. Repair the one-coordinate wording in a successor pinned nine source if the owner elects to repin it.
3. Restore/pin the missing 1,093-line five-value source, then conduct source-line reviews against its exact blob.
4. For threshold reduction below five, do not attempt to force disjoint (V_3) at multiplicity four; instead build a dependence-safe shared-star/shared-anchor receiver or an alternative endpoint preserving original product provenance.
5. Keep global continuity separate from essential boundedness.

The unrestricted three-eigenvalue bounded-density conjecture remains open.
