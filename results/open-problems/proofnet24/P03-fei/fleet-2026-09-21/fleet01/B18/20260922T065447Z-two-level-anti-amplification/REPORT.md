# B18 — depth-two physical anti-amplification for a minimum FEI counterexample

**Run:** `20260922T065447Z-fleet01-B18-auto11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Candidate version and change summary

This run binds to the fixed all-gate candidate

\[
C^\dagger=6.521851214,
\qquad
\Gamma^\dagger(p)=\Gamma_{\rm RO}(p)+0.268204856\,p(1-p),
\tag{0.1}
\]

from fleet04/B18

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B18/20260922T031308Z-global-shared-core-invariant/REPORT.md`,

report blob `630d799d165e6d18c67c59cec7421758230e9ee4`.

The newest target-level selector reduction used is fleet01/B14

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B14/20260922T063833Z-high-influence-selector/REPORT.md`,

report blob `59df64d1e910b3ff9a931666227d884a8fa7d026`.
It proves that a minimum-dimensional counterexample to FEI at `C^dagger` must have every original influence below `0.1741` and every one-coordinate cofactor noncharacter.

This run attacks B14's first remaining implication — a genuinely physical multi-coordinate selector for that diffuse cofactor-prime class — by deriving a source-exact **depth-two adaptive selector inequality** and two universal anti-amplification consequences:

\[
\boxed{
\max_{j\ne i}\operatorname{Inf}_j(f_{i=b})<0.312
\quad\text{for every }i,b,
}
\tag{0.2}
\]

and, for every root coordinate `i`,

\[
\boxed{
\min_{b\in\{0,1\}}
\max_{j\ne i}\operatorname{Inf}_j(f_{i=b})<0.262.
}
\tag{0.3}
\]

Thus the still-unpaid minimum-counterexample class is not only root-diffuse: it cannot develop a `0.312` conditional influence after one physical restriction, and for each first pivot one of its two physical children is already `0.262`-diffuse.

These are necessary conditions on a hypothetical minimum counterexample, not a proof that such a counterexample exists.

## 1. Exact source mathematics consumed

### 1.1 Sharp Boolean posterior credit

Fleet01/B15

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B15/20260922T053153Z-sharp-biased-joint-credit/REPORT.md`,

report blob `48e0a5564c5ecf2054ea48822f2f53ee2a9bcd80`, proves the exact physical gluing cocycle

\[
D_\Gamma(g)
=(1-t)D_\Gamma(g_0)+tD_\Gamma(g_1)
+\mathcal R_{\Gamma,i}+\mathcal C_i
\tag{1.1}
\]

and the source-valid posterior credit

\[
\mathcal C_i\ge
\Theta\!\left(\sqrt{V_t}\,|1-2d|\right),
\qquad
\Theta(z)=h_2\!\left({1-\sqrt{1-z^2}\over2}\right),
\tag{1.2}
\]

where `d=Pr[g_0 != g_1]`.
For balanced children and a uniform physical pivot, B14 records the resulting local lower bound

\[
\boxed{
\mathcal R_{\Gamma^\dagger,i}+\mathcal C_i
\ge F(d),
}
\qquad
F(d)=C^\dagger d-1-h_2(d)+\Theta(|1-2d|).
\tag{1.3}
\]

B14 further proves that `F` is strictly increasing on `[0.1741,1]` and `F(d)>0` there.

### 1.2 Named other-account theorem applied

I substantively consume fleet04/B17

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B17/20260922T061604Z-character-cofactor-local-threshold/REPORT.md`,

report blob `865131123fbceeb0d41109308d531ace9e926af6`.
For a balanced character-cofactor split it proves the exact identity

\[
D_C(g)=\frac12D_C(h)+d[C-Q(d)]
\tag{1.4}
\]

with `Q(d)<5.1` for `0<d<=1/2`.
Since `C^dagger>5.1`, this theorem eliminates every character-cofactor root pivot in a minimum counterexample. It is used together with the new depth-two theorem below, so the surviving class has **both** properties: no character cofactor and no one-step conditional influence at or above the new thresholds.

I also consume fleet03/B17

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B17/20260922T063313Z-balanced-aux-policy/REPORT.md`,

report blob `afa067429f95c9e9a7b5d59b8397cb77c4ac4628`.
Its exact 3139-state restriction-lattice theorem proves every balanced auxiliary-only restriction of the known 18-input nine-host seed has

\[
{H\over I-1}<6.521845710923047<C^\dagger.
\tag{1.5}
\]

Thus that complete source-bound obstruction family is already safe at the fixed center and cannot instantiate the residual minimum-counterexample class derived here. This is used as an exact obstruction check, not as evidence for arbitrary gates.

## 2. Smallest conditional end-to-end argument

Assume FEI at `C^dagger` is false and choose a minimum-dimensional counterexample

\[
H(f)>C^\dagger I(f).
\tag{2.1}
\]

Introduce the actual fresh unbiased coordinate `y`

\[
\widetilde f(y,x)=(-1)^y f(x).
\tag{2.2}
\]

Then

\[
H(\widetilde f)=H(f),
\qquad
I(\widetilde f)-1=I(f),
\tag{2.3}
\]

and every descendant obtained by restricting only original `x`-coordinates remains balanced. Write

\[
D(g):=C^\dagger[I(g)-1]-H(g)
\tag{2.4}
\]

for such balanced lifted descendants. The root has `D(tilde f)<0`, while every proper original-coordinate restriction has nonnegative defect by minimum dimensionality.

For any finite adaptive physical restriction tree `T` on original coordinates, iterate (1.1) and use (1.3). If `d_v` is the disagreement probability of the physical pivot at node `v` and `pi_v=2^{-depth(v)}`, then

\[
D(\widetilde f)
\ge
\sum_{v\in\operatorname{Int}(T)}\pi_v F(d_v)
+
\sum_{\ell\in\operatorname{Leaf}(T)}\pi_\ell D(\widetilde f_\ell).
\tag{2.5}
\]

Every nonroot leaf is safe, hence a **sufficient** missing implication for full FEI at `C^dagger` is:

> every noncharacter Boolean function in the surviving minimum-counterexample class admits one finite physical original-coordinate tree with
> \(\sum_v\pi_v F(d_v)\ge0\).

No such universal tree-selection theorem is claimed here. Equation (2.5) is only the compact compiler exposing the exact gap. The substantive work below proves a new depth-two part of that missing selector.

## 3. A universal lower bank for one bad low-influence pivot

For `0<=d<=1/2`, put

\[
\phi(d)=\Theta(1-2d).
\]

B14 proves

\[
\phi'(d)\ge-{2\over\ln2},
\qquad
\phi(0)=1.
\tag{3.1}
\]

Therefore

\[
F(d)
\ge
A d-h_2(d),
\qquad
A:=C^\dagger-{2\over\ln2}.
\tag{3.2}
\]

The binary log-partition identity gives

\[
\min_{0\le d\le1}\{Ad-h_2(d)\}
=-\log_2(1+2^{-A}).
\tag{3.3}
\]

Indeed the maximum of `h_2(d)-Ad` occurs at
`d=(1+2^A)^{-1}` and equals `log_2(1+2^{-A})`.
Define

\[
M:=\log_2(1+2^{-A}).
\tag{3.4}
\]

Then every root pivot in the B14 hard core obeys

\[
\boxed{F(d_i)\ge-M.}
\tag{3.5}
\]

A short exact estimate gives

\[
\boxed{M<0.118.}
\tag{3.6}
\]

For completeness: the positive `atanh(1/3)` expansion gives `ln2>0.693`, hence `A>3.63`. Put `t_0=0.63*0.693=0.43659`. Since `e^t>1+t+t^2/2`,

\[
2^{0.63}>1+t_0+t_0^2/2
={30637908281\over20000000000}.
\]

Using `ln(1+x)<x`,

\[
M< {2^{-3.63}\over\ln2}
< {2500000000000\over21232070438733}
< {59\over500}=0.118.
\tag{3.7}
\]

This is the finite bank that one or two profitable second-level pivots must repay.

## 4. Exact depth-two adaptive selector inequality

Fix an original root coordinate `i`. For branch `b` and remaining coordinate `j`, set

\[
e_{b,j}:=\operatorname{Inf}_j(f_{i=b}).
\tag{4.1}
\]

Define the best **positive** second-level payment available in that branch by

\[
P_b(i):=
\max\left\{0,\max_{j\ne i}F(e_{b,j})\right\},
\tag{4.2}
\]

with the inner maximum interpreted as `0` when no coordinate remains.

Construct the following genuine adaptive physical tree:

1. reveal `i` at the root;
2. in branch `b`, reveal a coordinate attaining the inner maximum in (4.2) if that maximum is positive;
3. otherwise stop that branch.

All leaves are proper restrictions of `f`, so their lifted defects are nonnegative. Applying (2.5) gives

\[
D(\widetilde f)
\ge
F(d_i)+{P_0(i)+P_1(i)\over2}.
\tag{4.3}
\]

Because the root is a counterexample, `D(tilde f)<0`. Thus every root coordinate in a minimum counterexample must satisfy the **exact necessary condition**

\[
\boxed{
F(d_i)+{P_0(i)+P_1(i)\over2}<0.
}
\tag{4.4}
\]

Combining with (3.5),

\[
\boxed{
P_0(i)+P_1(i)<2M<0.236
\quad\text{for every }i.
}
\tag{4.5}
\]

This is the new selector implication. It is not a fixed-coordinate erasure claim: the second coordinate can be chosen separately in the two physical branches, and every branch label is an actual restriction outcome.

## 5. Two numerical-free-threshold consequences

The exact rational-log checker beside this report certifies

\[
h_2(0.262)<0.83,
\qquad
h_2(0.312)<0.896.
\tag{5.1}
\]

Using `A>3.63` in (3.2),

\[
F(0.262)
>3.63(0.262)-0.83
={6053\over50000}
=0.12106
>0.118>M,
\tag{5.2}
\]

and

\[
F(0.312)
>3.63(0.312)-0.896
={2957\over12500}
=0.23656
>0.236>2M.
\tag{5.3}
\]

B14's monotonicity of `F` on `[0.1741,1]` now turns (4.5) into two structural theorems.

### Theorem 5.1 — no one-branch amplification to 0.312

For every root coordinate `i`, every branch `b`, and every remaining coordinate `j`,

\[
\boxed{
\operatorname{Inf}_j(f_{i=b})<0.312.
}
\tag{5.4}
\]

Otherwise `P_b(i)>=F(0.312)>2M`, contradicting (4.5).

This is genuinely stronger than the trivial influence martingale consequence of B14, which only gives
`Inf_j(f_{i=b})<2(0.1741)=0.3482`.

### Theorem 5.2 — one child of every pivot is 0.262-diffuse

Let

\[
m_b(i):=\max_{j\ne i}\operatorname{Inf}_j(f_{i=b}).
\]

Then for every root coordinate `i`,

\[
\boxed{
\min\{m_0(i),m_1(i)\}<0.262.
}
\tag{5.5}
\]

Indeed if both maxima were at least `0.262`, then by monotonicity and (5.2),

\[
P_0(i)+P_1(i)>2M,
\]

again contradicting (4.5).

## 6. Required obstruction checks

- **Addressing.** Standard unbiased addressing has genuine address coordinates of influence `1/2`, so it is already removed by B14's root threshold. The present argument does not revive the false prescribed-coordinate payment claim.
- **Majority.** Large odd majority has root and one-step conditional influences of order `n^{-1/2}`. It survives (5.4)--(5.5), as it must; this theorem does not disguise a majority proof as universal coverage.
- **Tribes.** Balanced tribes likewise remains in the low-influence residual regime after a single typical restriction. No claim of full coverage is made.
- **Sparse defects.** A rare defect can keep all one-step influences below the new thresholds; it survives unless it creates a large conditional pivot. The result uses the actual Boolean posterior credit, not defect density alone.
- **Tensor/self-composition.** Diffuse tensor constructions can survive the two-level thresholds. No every-critical-core shell hypothesis is used.
- **Biased limits.** The argument returns to the original uniform-cube FEI through the exact fresh-character lift. It does not assert the full off-center product-bias `(G)` inequality.
- **Known 18-input shared-core seed.** The named fleet03/B17 theorem (1.5) is applied directly: the seed and all 3139 balanced auxiliary-only descendants are strictly safe at `C^dagger`, so they do not provide a hidden exception to the minimum-counterexample reduction.

## 7. Old and new missing implications

**Old first missing implication.** After B14, a hypothetical minimum counterexample could still lie anywhere in the diffuse cofactor-prime class

\[
\max_i\operatorname{Inf}_i(f)<0.1741,
\qquad
f_{i=b}\text{ noncharacter for every }i,b,
\tag{7.1}
\]

with no quantitative control on one-step conditional amplification beyond the trivial martingale ceiling `0.3482`.

**New proved inference.** Every such minimum counterexample must satisfy the exact depth-two payment budget (4.5), hence the stronger one-step restrictions (5.4)--(5.5): all one-step child influences are `<0.312`, and for every first pivot at least one child has all remaining influences `<0.262`. Together with fleet04/B17, both children remain noncharacter.

**New first missing implication.** Prove that every function satisfying the strengthened hard-core constraints

\[
\operatorname{Inf}_i(f)<0.1741,
\quad
f_{i=b}\text{ noncharacter},
\quad
\operatorname{Inf}_j(f_{i=b})<0.312,
\quad
\min_b\max_j\operatorname{Inf}_j(f_{i=b})<0.262
\tag{7.2}
\]

admits a deeper finite physical restriction tree with nonnegative total `F`-payment in (2.5), or derive a further source-valid structural reduction. Majority/tribes/tensor-like diffuse mechanisms still inhabit (7.2), so this remains a genuine universal gap.

A natural next attack is no longer another one-step threshold optimization. It is to exploit the exact branchwise budget (4.5) over a **three-level greedy tree**, where the one `0.262`-diffuse child supplied by every root pivot can be chosen as the low-risk continuation and the opposite child's positive payment is retained rather than discarded.

## 8. Certificate and status

`CHECKER.py` uses only standard-library exact `Fraction` arithmetic. Logarithms are enclosed by the positive-remainder `atanh` expansion. It certifies `ln2>0.693`, `A>3.63`, the hand bound `M<0.118`, both entropy bounds in (5.1), and the payment inequalities (5.2)--(5.3). The preserved output is `CHECK_OUTPUT.txt` and prints `PASS`.

**Outcome:** `ESSENTIAL_STEP_APPLIED`.

This is a real target-level restriction-policy strengthening but not a universal selector theorem. **Full FEI remains OPEN / NOT PROVED.**

Scoped privacy review: only FEI mathematics, logical account/slot labels, private-repository-relative source paths, source hashes, and nonsecret constants are present. No credentials, scheduler identifiers, machine paths, unrelated private material, email/Drive actions, paid/remote compute, public posting, workflow dispatch, or permission changes are included.
