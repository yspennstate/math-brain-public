# T064 work log

Task received: 15 November 2026, approximately 01:08 Asia/Tbilisi
(14 November, 21:08 UTC): “take the NEXT checkable step on this problem,
building on that work.”

## 01:08 — orientation and bounded literature check

Read the previous folder's REPORT.md, LOG.md and SOLVED_ELSEWHERE.md.
Directory listing confirms there is no PROOF.md and no computation script
in that folder. Nothing there was edited. Read the startup memory index
and compute state (`warn`, `owner_away_open`, CPU saturated). The present
instruction to write only in this folder overrides global requests to
write mesh, checklist or brain state. No such state was changed.

Commands used for reads after discovery:

```sh
env OMP_NUM_THREADS=1 nice -n 15 /bin/cat ~/codex_op_1114/briefs/T064/LOG.md ~/codex_op_1114/briefs/T064/SOLVED_ELSEWHERE.md
env OMP_NUM_THREADS=1 nice -n 15 /bin/ls -la ~/codex_op_1114/briefs/T064 ~/codex_op_1114r3/briefs/T064
```

The initial file discovery was too broad and its output truncated; the
bounded reads above recovered the actual prior artifacts. `nice` prints
`setpriority: Operation not permitted`, also observed by the prior worker.
No heavy computation is planned; any numerical check must first verify
actual inherited niceness. No subagents, git or background processes.

Web search queries:

- `random plane wave Cardy SLE 6 percolation 2025 2026 critical crossings`
- `random plane wave critical percolation Muirhead Wigman 2025`

Opened:

- https://arxiv.org/abs/2010.11770
- https://arxiv.org/html/2010.11770v3
- https://link.springer.com/article/10.1007/s00440-025-01367-8

No later solution of the Cardy/SLE conjecture appeared in these queries.
The 2025 paper by Stephen Muirhead and Igor Wigman concerns supercritical
giant components, not the requested critical scaling limit. The 2023 paper
is by Stephen Muirhead, Alejandro Rivera and Hugo Vanneuville, with an
appendix by Laurin Köhler-Schindler. The arXiv history says v3 is from
17 July 2023; the HTML's displayed 2026 date is not a new version.
The literature check took less than five minutes. Further reading of that
paper below is theorem verification, not an extended novelty search.

## Independent re-check of the previous result

Opened Theorems 1.3 and 1.7 and Example 1.4 in the full paper. They confirm
the previous report's main claim. A direct check of the RPW assumptions:
the spectral measure is uniform on the unit circle, giving smoothness,
isotropy and the required two-point first-jet non-degeneracy by Remark 1.2;
the Bessel asymptotic gives |J0(r)| <= C r^(-1/2) for r >= 1, hence every
iterated-log decay condition in those theorems. For the quantitative bound,
bar-kappa(sqrt(R)) <= C R^(-1/4), so

    min(log R, 1/bar-kappa(sqrt(R))) = log R

for all sufficiently large R. Thus the fixed-level bound is indeed
`c1 exp(-c2 sqrt(log R))`. Independently, translating to the ordinary
superlevel u = -ell gives bounded components for u > 0 and one unbounded
component for u < 0, consistent with monotonicity. Theorem 1.3 excludes
u = 0. The earlier result holds; its warning about constants depending on
the level is necessary.

Read Theorem 2.11, Proposition 2.14 and Proposition 2.15 to identify a
checkable next step. Crucially the rectangular delocalisation rate in
Proposition 2.15 is qualitative (`eta(R) -> 0`), not a polynomial rate.
It would be incorrect to claim a logarithmic square-crossing window from
that statement alone. Annular delocalisation is quantitative and will be
examined before choosing the extension.

Priority diagnostic attempted:
`env OMP_NUM_THREADS=1 nice -n 15 /bin/ps -o pid,ppid,ni,rss,comm -p $$`.
The sandbox denies ps (exit 126). No numerical program has been run.

## Chosen extension (before doing it)

Choice: prove an explicit finite-scale de-sprinkling bound for rectangle
crossings by the RPW. Count all stratified critical values in a level
interval, using the exact one-point Gaussian jet and Kac–Rice. The
rectangle's edges and corners must be included. If there is no such
critical value, stratified level-set isotopy preserves the crossing.
This gives a bound uniform in the level and in the rectangle dimensions,
unlike the fixed-level constants in the earlier report.

The target consequence is that levels u_R with |u_R| R^2 -> 0 have
crossing probabilities differing from their zero-level values by o(1).
For squares the zero-level value is exactly 1/2. This is a small-scale
stability lemma, not zero-level RSW, a predicted critical exponent, or a
solution of the conjecture. The purpose is to quantify one valid way of
removing a sufficiently small sprinkling, and to make the boundary terms
and the gap to available concentration estimates explicit.

The proof will use all interior critical points for an upper bound;
discarding nonpivotal extrema is unnecessary and would require an extra
topological argument. Independently audit the interior constant both by
Gaussian covariance conditioning and by integrating the resulting
critical-value density to recover the total critical-point intensity.
Audit the edge term against the one-dimensional zero-count formula for
the derivative. No simulation is needed.

## Proof and independent numerical audit

Created PROOF.md with the following result. For a rectangle of area A
and perimeter P, and ordinary superlevel thresholds a<b, the decrease
in crossing probability is at most

    A integral_a^b alpha(t) dt + P integral_a^b beta(t) dt
       + 4 integral_a^b phi(t) dt,

where phi is the standard normal density and

    alpha(t) = phi(t)(t^2-1+2 exp(-t^2))/(4 pi),
    beta(t) = phi(t)exp(-t^2)/(2 pi)
              + t phi(t)erf(t)/(2 sqrt(pi)).

These are the exact interior-critical and edge-critical height
intensities, not claimed crossing-pivotal densities. The proof counts
all stratified critical values and supplies the level-strip flow
argument. Closed-form integrals give a bound valid for every level,
including negative ones by evenness. It implies stability under
u_R=o(R^(-2)) for fixed aspect ratios and convergence to 1/2 for squares.

Opened the arXiv page, full HTML and original PDF of Dmitry Beliaev,
Valentina Cammarota and Igor Wigman, *Two point function for critical
points of a random plane wave*, arXiv:1704.04943:

- https://arxiv.org/abs/1704.04943
- https://arxiv.org/html/1704.04943
- https://arxiv.org/pdf/1704.04943

Proposition 1.1 gives critical intensity 1/(2 pi sqrt(3)), half of which
is saddles. This independently agrees with integrating the derived
height density. The derivative covariance was checked both from the
Taylor series of J0 and from spectral-angle moments. The edge formula
was independently checked by the unmarked zero intensity of f_s.

Created check_level_stability.py, using only the standard library,
constant-memory deterministic quadrature and no random samples.
Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_level_stability.py
```

Output (exit 0):

```text
nice: setpriority: Operation not permitted
niceness=20; OMP_NUM_THREADS=1; CPU cap=60 seconds
spectral moments: 0.500000000000 0.375000000000 0.125000000000
conditional determinant max error=5.394e-11
conditional edge absolute-normal max error=7.527e-14
I quadrature max error=3.469e-18
J quadrature max error=1.388e-17
interior total=0.091888149237; saddle total=0.045944074618
edge total=0.275664447711
alpha(0)=0.031746817967; beta(0)=0.063493635934; phi(0)=0.398942280401
square exact bounds with u=R^(-3):
  R=  10 u=1.0e-03 bound=0.00731019492568 leading=0.00731019635569
  R= 100 u=1.0e-06 bound=0.000344461403166 leading=0.000344461403167
  R=1000 u=1.0e-09 bound=3.200238828e-05 leading=3.200238828e-05
small-square area/edge/corner bound contributions: 3.17468020937e-09 2.53974586066e-06 0.00159576885564
PASS; elapsed=0.075s; peak RSS=12.64 MiB
```

The libc getpriority check establishes inherited niceness 20: the nice
warning does not mean the process lacks the required low priority.
The script exits before quadrature if niceness is below 15 or
OMP_NUM_THREADS is not 1, and sets a 60-second CPU limit.

One LOG append initially failed because the patch context omitted a
line prefix; no file was changed by that failed patch. The append was
then applied against the actual final line.

## Attempts to break the bound; final elementary form

The boundary terms survive two deterministic tests even within the
Helmholtz class. On a small rectangle with 0<L,H<pi/2,
g(x,y)=sin(x)+sin(y) has no interior or open-edge critical point.
Its superlevel left-to-right crossing threshold is sin(H), attained
at the top-left corner. Dropping the corner term would miss this
change. For g(x,y)=sin(x)+cos(y-H/2), the crossing threshold is 1,
attained at the midpoint of the left edge; the interior gradient never
vanishes. A small interval about 1 can avoid all corner values (for
example L=H=0.4) and the right-edge critical value. Dropping the edge
term would miss this change. Both functions satisfy Delta g=-g.

Checked negative levels using evenness of both height densities;
checked finite-interval endpoints have no atoms; checked the Hessian's
trace is -f rather than an extra independent Gaussian variable. The
deformation preserves each side of the rectangle, not just abstract
topology. The square's value 1/2 uses duality and sign/rotation symmetry,
not an independence or FKG assumption.

Added a simpler fully explicit inequality for delta=|u|<=1:

    |p_Q(u)-p_Q(0)| <= phi(0) delta
       * [A/(4 pi) + P/(2 pi) (1+delta^2/3) + 4].

The proof uses convexity to bound the conditional determinant and the
derivative of the conditional absolute-normal mean to bound the edge
term. This avoids relying on a signed O-term as an inequality. Added
20 checks covering four aspect ratios and five levels. The rerun used
the same command, returned the same constants and bounds as above, and
ended with:

```text
elementary bound (2a): 20 aspect-ratio/level checks passed
PASS; elapsed=0.085s; peak RSS=12.61 MiB
```

No new claim is made about which critical points are pivotal. In
particular an o(1) level sprinkling cannot be substituted for the proved
o(R^(-2)) condition. Counting all critical points cannot by itself
produce RSW or a percolation scaling limit.

Created REPORT.md with the required first-line verdict, the new bound,
the independent checks, limitations, and a concrete next missing input.
Several attempted proof edits failed exact-context matching and made
no changes; the actual text was reread before the successful edit.
Removed guessed intermediate phase times; the task receipt time comes
from the session clock and all phase ordering is retained.

## Final artifact audit

Read REPORT.md and all of PROOF.md after the final edits. Confirmed the
verdict line, dimensions A and P, the ordinary superlevel sign convention,
all three primitive formulas and the small-level inequality agree with
the script and independent derivations. The final script run passed;
there were no changes to its tested formulas afterward. File listing
confirms the four deliverables are LOG.md, PROOF.md, REPORT.md and
check_level_stability.py.
Only this session's folder was written. No SOLVED_ELSEWHERE.md was made,
since no solution of the scaling-limit problem was located.

Task completed: “take the NEXT checkable step on this problem, building
on that work” — received 15 November 2026, approximately 01:08
Asia/Tbilisi.
