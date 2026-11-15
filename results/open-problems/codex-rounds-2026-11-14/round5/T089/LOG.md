# T089 work log

Task: "take the NEXT checkable step on this problem, building on that work."
Received 2026-11-15 approximately 08:09 Asia/Tbilisi (04:09 UTC).

## Orientation and bounded literature check

Read the reports, logs, proofs and Python audit scripts in the original,
round 3 and round 4 T089 folders. They are read-only. No git or subagents.
The current instruction to write only in this folder overrides the older
shared mesh, checklist and brain write instructions. No shared-state commands
were run. The compute state reports warn / owner_away_open / cpu_saturated;
only small standard-library single-process computations are planned.

The initial literature check took less than five minutes. Queries included
`Bohigas Giannoni Schmit conjecture proof 2025 2026 billiards GOE`,
`site.arxiv.org "Bohigas" "2026" spectral statistics proof`, and
`site.arxiv.org "GOE" "billiards" "2025"`.
Opened primary sources:

- Julien Moy, *Smooth spectral statistics of random perturbations of
  Schrödinger operators near Anosov energy levels*, arXiv:2610.09869,
  https://arxiv.org/abs/2610.09869 . Still v1, 7 October 2026. Random
  perturbations and smooth mesoscopic statistics do not prove the requested
  fixed-billiard microscopic limit.
- Wooyeon Kim, Jens Marklof, Matthew Welsh, *Values of ternary quadratic
  forms at integers and the Berry-Tabor conjecture for 3-tori*,
  arXiv:2601.03209, https://arxiv.org/abs/2601.03209 . The page now has
  v2 dated 5 November 2026. Its result concerns two-point statistics of
  integrable boxes, not GOE spacings for chaotic billiards.
- Javier M. Magan, Qingyue Wu, *Two types of quantum chaos: testing the
  limits of the Bohigas-Giannoni-Schmit conjecture*, arXiv:2411.08186,
  https://arxiv.org/abs/2411.08186 . Ensemble constructions and numerical
  investigations, not the stated billiard theorem.
- Alexander I. Bufetov, Pavel P. Nikitin, Yanqi Qiu, *On Number Rigidity
  for Pfaffian Point Processes*, arXiv:1810.09223,
  https://arxiv.org/html/1810.09223 . Opened the full HTML and checked
  Section 1.2, equation (1.8), for the orthogonal sine kernel.
- Diane Holcomb, Benedek Valkó, *Overcrowding asymptotics for the Sine_beta
  process*, arXiv:1506.07117, https://arxiv.org/abs/1506.07117 . The
  abstract gives asymptotic overcrowding exponents with an O(n^2) term;
  it does not supply a usable explicit finite-order constant here.

No resolution found in this bounded search. No SOLVED_ELSEWHERE.md is
warranted. This is not an exhaustive literature theorem.

## Independent re-derivation of the latest result

For S(z)=sin(pi*z)/(pi*z), D=S', and
I(z)=integral_0^z S - sgn(z)/2, the signed-lobe argument gives |I|<=1/2.
Independently, writing S as the average of cos(pi*z*t) on [-1,1] and
D/pi as minus the average of t*sin(pi*z*t), Cauchy--Schwarz gives
S^2<=average cos^2 and 3D^2/pi^2<=average sin^2. Their sum is <=1.
The determinant-one congruence alpha^4=pi^2/3 therefore gives k rows of
squared norm <=k and k rows of squared norm <=k+(k-1)pi^2/12.
Hadamard followed by the Pfaffian square root gives exactly

    b_k(s) <= R^k [k(k+(k-1)pi^2/12)]^(k/4) / k!.

The diagonal is one and I(0)=D(0)=0, so the k-1 term and exponent k/4
are correct. Pascal cancellation independently recovers the preceding
target-only comparison. The latest main analytic claim holds. An exact
arithmetic recheck of the displayed order-58 constant is next.

## One extension chosen before its computation

Retain near-diagonal repulsion by applying Newton divided differences to
the k smooth (second) rows and the corresponding columns of the GOE
Pfaffian matrix. Leave the discontinuous I rows untouched. The triangular
congruence should extract one full Vandermonde factor. Derivative bounds
from the Fourier integral for S should then give a much smaller explicit
factorial-moment remainder, aiming at the predecessor's b_20(2)<=10^-6
target. This is one analytic extension of the target remainder, not a
claim about billiard eigenvalues. Every bound will be certified using exact
rational arithmetic; exploratory decimals will not serve as certificates.

## Divided-difference derivation and preliminary check

Read the startup memory index and the identity memory directly, without
running recall commands that write outside this folder. Shell reads exposed
no task-specific memory needed beyond the predecessor records.

For a divided difference of order n, the Fourier representation bounds
S by pi^n/(n!(n+1)); a double divided difference of D, of orders n,m,
is bounded by pi^(n+m+1)/(n!m!(n+m+2)). Normalize smooth row i by
(i-1)!/pi^(i-1). The congruence extracts

    Vandermonde(x) * pi^(k(k-1)/2) / product_(n=0)^(k-1) n!.

The remaining matrix has first/first entries bounded by 1/2, mixed entries
in smooth column i bounded by 1/i, and distinct smooth/smooth entries
bounded by pi/(i+j). The diagonal is zero. Keeping the separate row sums
is substantially better than one uniform entry bound.

An initial attempt to use only |Vandermonde|<=R^(k(k-1)/2) was too weak
at order 20. Chebyshev monic polynomials and Hadamard instead give

    |Vandermonde| <= 2^(k-1) k^(k/2) (R/4)^(k(k-1)/2).

Exploratory commands used
`env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B -`.
They evaluated rational powers and displayed diagnostic floats. The uniform
entry version suggests order 12 at R=2; keeping the separate row sums
suggests order 10, with bound approximately 5.1738524e-7. These are not yet
the final certificates. Every process checked inherited nice=20. The nice
launcher prints a sandbox setpriority warning; the actual priority passes.

## Independent predecessor computation passed

Wrote recheck_previous.py independently of the predecessor implementations.
Command (exit 0):

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B recheck_previous.py > recheck_output.txt 2>&1
```

Output: previous_result_holds=true; 150 direct-square versus multiplicative
fourth-power checks; first even orders 14,26,58 at R=1/2,1,2; the order-58
rational enclosure holds; 2,145 binomial identities; 16,245 target-only
comparisons for 57 rational count laws, including a rare count-64 cluster.
Elapsed 0.563 s, measured peak RSS 15,810,560 bytes, actual nice=20.
The preceding analytic result and displayed arithmetic constant both hold.

## New proof and exact audit passed

Wrote PROOF.md and check_repulsion.py. The proof extracts a full
Vandermonde factor by transforming only the smooth rows and columns, then
uses the Chebyshev bound above and separate normalized row norms.
Command (exit 0):

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B check_repulsion.py > repulsion_output.txt 2>&1
```

Output: all exact repulsion-bound checks passed. In particular,

    (517385/10^12)^4 < M_10(2)^4 < (517386/10^12)^4 < 10^-24.

Thus sup_(s<=2) b_10(s) <=517386/10^12<10^-6. The same formula gives
b_20(2)<10^-89, proving the predecessor's proposed order-20 target.
Exact fourth powers and enclosures are saved in repulsion_data.json.

The first even orders of this rational bound below 10^-6 are 6,8,10 for
R=1/2,1,2. Their rational upper bounds are respectively 5e-11,5e-12,
517386/10^12. These are thresholds of the bound, not of the actual moments.

The audit compared the closed fourth-power formula with an independently
constructed entrywise envelope matrix at 72 radius/order pairs. It also
checked 20 exact polynomial-kernel congruences on ordinary, reversed,
tightly clustered and translated nodes, comparing recursive divided
differences with barycentric ones in 220 mixed and 220 double entries.
Determinants and recursive Pfaffians agreed in 40 tests. These polynomial
models test algebra; they are not claimed to be GOE correlation functions.

For the Vandermonde bound, 72 exact rational cases compared the product
formula, a monomial determinant and a Chebyshev-polynomial determinant,
including endpoints and tight clusters. All 3,900 Chebyshev entries and
the entrywise and Hadamard bounds passed.

Elapsed 0.329 s; measured peak RSS 17,858,560 bytes; nice=20; one process,
standard library only. Both scripts use 256 MiB measured RSS guards and
120-second elapsed guards. No OS-enforced memory cap is claimed.
The compute state was re-read: still warn / owner_away_open, no distress.

## Attempts to break the result and second derivations

- Re-derived the determinant factor without an exterior algebra argument:
  det(B)=(det T)^2 det(A), and det(A)=(Pf A)^2. Taking absolute square
  roots recovers exactly |Pf A|=V*pi^K/F_k*|Pf B|. The exponent is one
  on the Vandermonde, not one-half or two.
- Checked the derivative order in the v_i/v_j block: D=S' contributes
  one extra derivative, so the total is i+j-1, the Fourier integral
  denominator is i+j, and normalization leaves pi/(i+j). The zero diagonal
  is imposed by antisymmetry, not by that upper bound.
- Checked each mixed column against every first row. Its bound is 1/i,
  so a_k contains sum 1/i^2, whereas the smooth row contains k/i^2.
  The independent envelope-matrix calculation checks this distinction.
- The jump in I stays entirely in the unchanged u/u block. Applying
  divided differences to both row types would be unjustified. The exact
  polynomial models retain the sign jump and include separations of order
  10^-4, as well as node reversal.
- Exactly coincident nodes cannot be used in Q. They form a null set in
  the factorial-correlation integral; no asserted value of the correlation
  on that diagonal is needed. At k=1 the formula gives M_1(R)=R exactly;
  at R=0 both sides vanish.
- Re-derived the Chebyshev normalization: its leading coefficient is
  2*(R/4)^n*2^(n-1)*(2/R)^n=1. Therefore the determinant is the ordinary
  Vandermonde without another scale factor. Columnwise Hadamard gives
  exactly k^(k/2), not k^k. Exact matrix tests check both statements.
- The only initially unsuccessful estimate was the crude Vandermonde
  maximum R^K; it cannot establish the proposed order-20 target. Keeping
  the interval capacity factor 4^-K resolves that loss. No mathematical
  test of the final bound failed.

No billiard eigenvalues, empirical moment errors, or numerical GOE moment
tables were computed. No assertion about the main BGS conjecture follows
without the missing spectral estimates.

## Report and final artifact audit

Created REPORT.md with the partial verdict and the new order-10 constant.
One formatting patch missed its exact context and changed no files; the
corrected patch succeeded. No computation or mathematical check failed.
The final read-only audit independently recomputed both saved fourth powers
at k=10,20 from the squared prefactor and row norms, checked the order-10
integer fourth-root enclosure and the order-20 integer cross multiplication,
re-derived every audit count, and checked the eight required files and
the report verdict. It used the same environment and nice launcher with
`python3 -B -` (an inline standard-library check). Exit 0:

```text
Final artifact audit passed: both constants independently re-derived; all audit counts and eight files checked.
nice=20; peak_rss_bytes_macos=15204352; elapsed_seconds=0.002.
```

The eight deliverables are REPORT.md, PROOF.md, LOG.md,
recheck_previous.py, check_repulsion.py, recheck_output.txt,
repulsion_output.txt, and repulsion_data.json. No predecessor file was
executed or edited. All explicit writes remained in this task folder.
