# T222 work log

Task: "take the NEXT checkable step on this problem, building on that work."
Started 2026-11-15 approximately 11:15 Asia/Tbilisi (07:15 UTC).

## Orientation and the bounded literature check

All writes are confined to this folder. The specific restriction against
writes elsewhere precludes brain recall logging, mesh registration,
shared checklist updates, and shared-memory writes. Read the startup
memory and brain navigation directly. No git, subagents, external
messages, or heavy computations. The governor reports ok /
owner_away_open, with a heavily loaded machine.

Inventoried the original and rounds 3, 4, 5 folders with `rg --files`.
Read each REPORT.md, LOG.md and PROOF.md, and round 5's AUDIT.md.
The script inventory `rg --files <four predecessor folders> -g '*.py'
-g '*.sh'` returned no matches (exit 1). There are no mathematical
scripts to rerun. Earlier directories remain read-only.

Reads after the initial inventory used
`env OMP_NUM_THREADS=1 nice -n 15 /bin/cat ...` or the same prefix
with `/bin/sh -c ...`. The sandbox prints
`nice: setpriority: Operation not permitted`; priority adjustment is
not verified. Only brief reads ran, and no numerical program is planned.

The web search tool was used within the first five minutes, then the
status check was closed. Queries:

- `"Euclidean traveling salesman" "variance" convergence Steele`
- `"traveling salesman" "variance limit" planar`
- `"1706.04290" traveling salesman variance`
- `"Euclidean traveling salesman" variance convergence 2026 2025`
- `"Steele" "variance" "converges" salesman`

Opened Sourav Chatterjee, *A general method for lower bounds on
fluctuations of random variables*, arXiv:1706.04290v3,
https://arxiv.org/html/1706.04290v3. Its Section 3, problem (2), states
the variance-limit question. No closing theorem was found. Search hits
alone are not treated as papers read. This short check is not an
exhaustive literature review; no SOLVED_ELSEWHERE.md is warranted.

## Independent recheck of round 5 before the extension

For a deleted sample S and independent uniform X, put
`Y_n(X,S)=sqrt(n)[T(S union {X})-T(S)]` and `U_n(x)=E_S Y_n(x,S)`.
The deleted-tour expectation cancels in conditional means, giving
`V[n,1]=Var_X U_n(X)`; an independent replacement pair checks the
factor sqrt(n). Conditional variance gives
`E_n=sum_j j V[n,j]=E_S Var_X Y_n(X,S)`.
These are different conditionings, and have not been interchanged.

The detour argument gives `0<=Y_n<=2 sqrt(n) R`. Homothetic-square
order statistics give `n E R(x,S)^2<=2`, including corners. Thus
`0<=U_n<=2sqrt(2)`. For each fixed interior x, the scaled nearest
distance has survival function tending to `exp(-pi r^2)`, dominated
uniformly by `exp(-r^2/4)`. Integration yields `limsup U_n(x)<=1`.
The uniform bound and reverse Fatou, centered at 1/2, independently
give `limsup V[n,1]<=1/4`.

For an arbitrary boundary strip of area b, variance decomposition gives
`p W<=V[n,1]<=p W+8b`, with p=1-b and W the variance under the
normalized interior distribution. Since W<=8, this verifies the
earlier `|V[n,1]-W|<=8b`. The centered strip integral is also <=8b.
The integrated error is checked by summing the four side contributions:
`integral_Q 2sqrt(n) integral_[dist(x,boundary),infinity)
exp(-(n-1)r^2/2) dr dx <=8sqrt(n)/(n-1)`.
Consequently the stated `V[n,1]<=mu_n(1-mu_n)+O(n^-1/2)` holds.

The old spectral factor is checked by exact subtraction:
`E_n+V[n,1]-2Var(L_n)=sum_(j>=3)(j-2)V[n,j]>=0`.
Round 4's two-disk deficit is independently rederived by translation:
disk area `pi c^2/(64n)`, pair deficit at least `c^2/2`, hence loss
`pi c^4/(128n)`, stronger than its claimed `/256`.
The expected isolated-site count divided by n tends to
`exp(-9pi c^2)`. This verifies the preceding K and round 5's total
variance consequence. No mathematical error found.

## ONE extension chosen before proof, 11:20 Asia/Tbilisi

Prove a quantitative tradeoff between interaction energy and the first
projection, rather than optimizing their bounds separately.
Let `alpha=e/4`, and let c_* and kappa be round 3's minimizer and
minimum of the endpoint-envelope expectation F. The target is

    limsup_n [E_n + alpha V[n,1]
              +(1+alpha)(mu_n-c_*)^2] <= kappa.

Reason: conditional on a query position x, the same Rayleigh
nearest-distance limit holds. The endpoint envelope can therefore be
centered at a deterministic function of x. Its curvature obeys
`F''<=2+8/e`, suggesting the adaptive center
`c_n(x)=c_*-alpha(U_n(x)-c_*)`.
The crucial new step is to justify the envelope limit uniformly over
these n-dependent bounded centers, despite the boundary. Pointwise
weak convergence alone would not suffice.

The tradeoff would improve round 5's total-variance upper bound to
`kappa/2+(1-e/4)/8`, before retaining its extra mean penalty.
It would not prove variance convergence or first-projection decay.
Prove it analytically and check it independently through the scalar
moment problem with prescribed mean. No numerical constants or
novelty claims relative to the full literature are planned.

## Proof saved

Saved PROOF.md. The theorem is slightly stronger than the recorded target:
it retains `W_n=Var_S integral_Q Y_n(x,S) dx`, which is nonnegative.
For a geometric error d_n->0 it proves

    E_n+W_n+alpha V[n,1]+(1+alpha)(mu_n-c_*)^2 <= kappa+d_n,
    alpha=e/4.

The needed uniform envelope limit has an explicit error:

    D_n(M)=integral_Q integral_0^infinity (8r+4M)
           |P(sqrt(n)R(x,S)>r)-exp(-pi r^2)| dr dx.

For every fixed M this tends to zero by joint dominated convergence,
using the boundary-safe tail exp(-r^2/4). This error controls every
measurable deterministic center field taking values in [-M,M], including
the n-dependent adaptive center. F is extended to all real c by
`F(c)=c^2-2c+4/pi` when c<0, eliminating any sign restriction on
that center. Its global curvature is `2<=F''<=2+8/e`.

Expansion of the adaptive-center square gives coefficients
`2alpha+alpha^2` and `alpha+alpha^2`; their difference is alpha.
The two distinct variance decompositions then give the theorem.

Together with the verified preceding first-projection estimate, this yields

    limsup Var(L_n) <= kappa/2+(1-alpha)/8
                     -(1-alpha^2)(c_*-1/2)^2/4.

Even after dropping the last term, the new upper bound is strictly
smaller than `(K+1/4)/2`: the exact difference is
`e/32-eta(c_*)/2>0`, since
`eta(c)<=1/(5184*pi*e^2)`.
All statements concern exact optimal tours. No decimal evaluation,
simulation, or variance-convergence conclusion is made.

Next audit: rederive the coefficient e/4 from the scalar second-moment
problem at prescribed mean; recompute the adaptive-center inequality
through G(c)=F(c)-c^2; check boundary domination, negative centers,
the two conditionings, the quadratic completion, and the comparison
with K. These provide independent checks of the load-bearing constants.

## Independent audit saved

Saved AUDIT.md. The constrained scalar second-moment maximum, for
`0<=Y<=2Z` with Rayleigh Z and prescribed mean m, is

    psi(m)=4(t^2+1/pi) exp(-pi t^2),
    m=2t exp(-pi t^2)+erfc(sqrt(pi)t).

Its derivatives are `psi'(m)=2t` and
`psi''(m)=-1/(2pi t^2 exp(-pi t^2))<=-e/2`.
This independently proves the penalty coefficient e/4. The minimizer
equation gives `M(c_*)=c_*`, so its mean anchor and the coefficient
of the squared mean error also agree with the main proof.

A separate calculation with `G(c)=F(c)-c^2` and `G''<=8/e` recovers
the adaptive-center inequality without expanding the same square.
Independent replacement-pair checks confirm E_n and V[n,1] use
different conditionings. Weighted quadratic minimization checks the
final 1/8 and 1/4 coefficients. The maximum of `t^2 exp(-t)` verifies
the old-deficit comparison, including its sign.

Checked negative centers, continuity of F through zero, all n>=2,
boundary strips, unbounded distances, measurability, repeated locations,
and nonunique optimal tours. No error found. Artificial alternating
order-two spectra still satisfy the new constraints: no convergence
can be inferred from the tradeoff alone. This limitation is recorded
explicitly. No numerical program was run.

## Final read-back, 2026-11-15 11:27:51 Asia/Tbilisi

Saved REPORT.md with the required first line. Read the theorem, complete
adaptive-center argument, AUDIT.md, and REPORT.md back from disk.
Representative command (shell body uses actual newlines):

```sh
env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '
head -n 1 REPORT.md
sed -n "1,135p" PROOF.md
cat AUDIT.md REPORT.md
rg -n "tag|e/4|e/32|alpha|D_n|VERDICT" PROOF.md REPORT.md
wc -l LOG.md PROOF.md AUDIT.md REPORT.md
ls -la
date "+%Y-%m-%d %H:%M:%S %Z"
'
```

Exit 0, with the same setpriority denial. Before this append, counts:
LOG.md 174, PROOF.md 462, AUDIT.md 238, REPORT.md 87 lines.
Equation tags are unique; theorem, proof, audit and report agree on
alpha=e/4, the mean penalty 1+alpha, the final quadratic coefficient,
and the strict gap e/32-eta(c_*)/2. No correction to the mathematics
was needed. The scalar audit independently recovers the same coefficient.

The completed extension is the joint inequality and its stricter
variance limsup consequence. The original conjecture is not proved.
No predecessor artifact, shared store, repository state, or external
system was modified. Only LOG.md, PROOF.md, AUDIT.md and REPORT.md
were authored here.
