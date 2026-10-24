# B18 FEI proof integration — exact restriction-tree debit/reserve ledger

**Date:** 21 September 2026  
**Fleet scope:** account04/B18  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** **PARTIAL / PROVED universal decomposition and finite-degree reserve bridge. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Priority:** no publication-priority claim is made.

## 0. Fresh state and the one lemma attacked

This run used fresh `proofnet24/P03-fei` state during the active 21 September proof/numerics sprint. The current owner correction is important: Hod's/read-once value `6.4547837...` is not the current unrestricted lower bound; the recovered external Numaro seed gives `C_FEI > 6.521845710923046575`. That numerical correction is not used in the proof below.

The compatible inputs are:

1. account04/B14, `2026-09-21T111505Z-js-strong-concavity-selector/REPORT.md` (blob `6e88e3464112a642fb6707f2f22f1eec3779543b`): for each coordinate, with fibre minority parameter `s`,
   `JS_i <= c_*(M_i-Q_i/3)`, where `c_*=2/ln 2`, `M_i=sum w s`, and `Q_i=sum w s^2`;
2. account04/B15, `20260921T124151Z-valuation-reserve/REPORT.md` (blob `2a2f6f2c8e1f2453c8bf43c865ae732c8edcd25f`): tensor collision in the arithmetic remainder is exactly a reserve transfer, so the remaining universal difficulty should be attacked under **restriction**, not by paying tensor infection as a new cost;
3. account03/B18, `20260921T120954Z-top-degree-parity-endpoint/REPORT.md`: top-degree parity eliminates the exact scalar endpoint but leaves a weighted-stability problem;
4. account04/B18, `20260921T121307Z-weighted-top-chain-dichotomy/REPORT.md` (blob `ebdbf27679f09b75a7f50a2d3bb4a7e1f7ebd2b0`): every degree-`d` nonconstant Boolean function has an oriented Fourier edge with posterior
   `q >= q_d := 1/(1+2^(2-2/d))`
   and upper mass at least `4^(1-d)`.

The precise unpaid lemma attacked here was:

> **Can the erasure cost, recombination curvature, upward-orientation slack, and the exact influence spent along restrictions be put into one globally summable ledger, so the previous scalar/orientation dichotomy becomes a single nonnegative resource rather than two unrelated branches?**

The answer is yes. The resulting ledger is exact and tensor-compatible. It does **not** yet give the missing dimension-independent bound.

## 1. Local exact debit/reserve identity

Let `f:{-1,1}^n->{-1,1}` be Boolean and write

`p_S = hat f(S)^2`.

Fix a coordinate `i`. For each `T` not containing `i`, put

`x_T=p_T`, `y_T=p_{T union {i}}`, `w_T=x_T+y_T`,

and, when `w_T>0`,

`q_T=y_T/w_T`, `s_T=min(q_T,1-q_T)`.

Thus

`p_i := Inf_i(f) = sum_T w_T q_T`,

`B_i = sum_T w_T h_2(s_T)`,

`Q_i = sum_T w_T s_T^2`,

and the exact restriction-entropy identity is

`Delta_i H = B_i + JS_i`,

with

`JS_i = sum_T w_T j(s_T)`,

`j(s)=1-h_2(1/2+sqrt(s(1-s)))`.

Put

`c_* = 2/ln 2`.

Define the **rebated erasure debit**

`E_i := B_i - (c_*/3) Q_i`,

and the **recombination/orientation reserve**

`R_i := c_* p_i - (c_*/3)Q_i - JS_i`.

Then there is an exact identity

\[
\boxed{\Delta_iH=c_*p_i+E_i-R_i.}
\tag{1.1}
\]

Both new terms are nonnegative:

\[
\boxed{E_i\ge0,\qquad R_i\ge0.}
\tag{1.2}
\]

### Proof

Equation (1.1) is algebra:

`c_*p_i + [B_i-c_*Q_i/3] - [c_*p_i-c_*Q_i/3-JS_i] = B_i+JS_i`.

For `E_i`, binary-entropy concavity on `[0,1/2]` gives `h_2(s)>=2s`, while `s^2<=s/2`. Hence each fibre contributes

`h_2(s)-(c_*/3)s^2 >= (2-c_*/6)s >=0`.

For `R_i`, use the B14 quadratic strong-concavity consequence

`j(s) <= c_*(s-s^2/3)`.

Since `q>=s`, each fibre has nonnegative reserve density

\[
\rho(q):=c_*(q-s)+\left[c_*(s-s^2/3)-j(s)\right]\ge0,
\qquad s=\min(q,1-q),
\tag{1.3}
\]

and exactly

\[
R_i=\sum_T w_T\rho(q_T).
\tag{1.4}
\]

This proves (1.2). QED.

The point of (1.3) is that the two previously separate resources are now one object. If `q<=1/2`, reserve comes from recombination curvature. If `q>1/2`, the extra term `c_*(q-s)=c_*(2q-1)` is precisely the upward-orientation reserve.

## 2. Exact summation on every adaptive restriction tree

Take any complete adaptive **physical restriction tree**. At an internal node `v`, let `f_v` be the current restricted Boolean function, choose a remaining coordinate `i(v)`, and give the node reach weight

`mu_v=2^{-depth(v)}`.

Write `p_v,E_v,R_v` for the quantities above at that state/coordinate.

Two exact telescoping facts hold.

First,

\[
H(f)=\sum_{v\text{ internal}}\mu_v\,\Delta_{i(v)}H(f_v),
\tag{2.1}
\]

because `Delta_i H = H(f)-[H(f^+)+H(f^-)]/2` and terminal constants have zero Fourier entropy.

Second,

\[
I(f)=\sum_{v\text{ internal}}\mu_v p_v.
\tag{2.2}
\]

Indeed

`I(f)=Inf_i(f)+[I(f^+)+I(f^-)]/2`:
for every `j!=i`, conditioning the physical `j`-edge disagreement event on the restricted `i`-bit gives the average child influence exactly.

Summing (1.1) on the tree yields the main identity of this run.

### Theorem 2.1 — exact global restriction-tree ledger

For **every** complete adaptive physical restriction tree,

\[
\boxed{
H(f)=c_* I(f)+\mathcal E_{\mathcal T}(f)-\mathcal R_{\mathcal T}(f),
}
\tag{2.3}
\]

where

\[
\mathcal E_{\mathcal T}(f)=\sum_v\mu_vE_v\ge0,
\qquad
\mathcal R_{\mathcal T}(f)=\sum_v\mu_vR_v\ge0.
\tag{2.4}
\]

Thus the entire unrestricted problem can be viewed as a competition between a **rebated erasure debit** and a **summable recombination/orientation reserve**, after the exact influence budget `c_* I` has already been paid once and only once.

This is stronger structurally than demanding a successful one-coordinate inequality at every state. Bad local nodes may be compensated by reserve accumulated on other branches or later depths. No every-coordinate selector is asserted.

## 3. A Bellman potential that exactly respects tensor products

Define

\[
\Phi(f):=\min_{\mathcal T}\mathcal E_{\mathcal T}(f),
\tag{3.1}
\]

where the minimum is over complete adaptive restriction trees. It obeys the finite Bellman recursion

\[
\boxed{
\Phi(f)=\min_i\left[E_i(f)+\frac12\Phi(f^+_i)+\frac12\Phi(f^-_i)\right],
}
\tag{3.2}
\]

with `Phi(constant)=0`. Since `R_T>=0`, Theorem 2.1 immediately gives the universal reduction

\[
\boxed{H(f)\le c_* I(f)+\Phi(f).}
\tag{3.3}
\]

Therefore a dimension-independent theorem

`Phi(f) <= K I(f)`

would prove full FEI with constant `K+c_*`. That bound is **OPEN**.

The potential has a useful exact compatibility absent from several killed routes.

### Theorem 3.1 — tensor additivity

For Boolean functions `f,g` on disjoint coordinate sets,

\[
\boxed{\Phi(f\otimes g)=\Phi(f)+\Phi(g).}
\tag{3.4}
\]

### Proof

The squared Fourier law of `f tensor g` is the product law. For a coordinate `i` belonging to `f`, every fibre weight is multiplied by a `g`-spectral mass, while its posterior `q` and minority parameter `s` are unchanged. Summing over the `g` label gives

`B_i(f tensor g)=B_i(f)` and `Q_i(f tensor g)=Q_i(f)`, hence `E_i(f tensor g)=E_i(f)`.

Moreover restriction in that coordinate gives `(f_i^+ tensor g)` and `(f_i^- tensor g)`. Induct on the total number of remaining variables. Using (3.2), every candidate coordinate in the `f` block has Bellman value

`[E_i(f)+(Phi(f_i^+)+Phi(f_i^-))/2] + Phi(g)`,

whose minimum over the `f` block is `Phi(f)+Phi(g)`. The same value is obtained by minimizing over the `g` block. Therefore the overall minimum is `Phi(f)+Phi(g)`. QED.

This exactly matches B15's new tensor-conservation warning: tensoring does not manufacture a new residual difficulty in this potential. The remaining obstruction is genuinely non-product restriction geometry.

## 4. The old top-chain dichotomy collapses into one reserve bank

Let

`k(s)=c_*(s-s^2/3)-j(s)` on `[0,1/2]`.

B14 proves `j''(s)<=-4/(3 ln2)=-(2/3)c_*` and `j'(0)=c_*`. Hence

`j'(s)<=c_*(1-2s/3)`,

so

\[
k'(s)=c_*(1-2s/3)-j'(s)\ge0.
\tag{4.1}
\]

Thus `k` is nondecreasing. From (1.3),

- for `q<=1/2`, `rho(q)=k(q)`;
- for `q>=1/2`, `rho(q)=c_*(2q-1)+k(1-q)`.

On the second interval the derivative is at least `c_*>0` because `0<=k'(s)<=c_*`, so `rho` is minimized there at `q=1/2`. Consequently, for every `q_0<=1/2`,

\[
q\ge q_0\quad\Longrightarrow\quad \rho(q)\ge k(q_0).
\tag{4.2}
\]

Now invoke the proved weighted top-chain theorem from the preceding B18 run. If `f` has Fourier degree `d>=1`, then some oriented edge has

\[
q\ge q_d:=\frac1{1+2^{2-2/d}},
\qquad
p_{upper}\ge4^{1-d}.
\tag{4.3}
\]

The fibre weight is `w=p_upper/q>=p_upper`. Since every other fibre contribution to `R_i` is nonnegative, (4.2) gives:

### Theorem 4.1 — unified parity reserve seed

Every nonconstant degree-`d` Boolean function has a relevant coordinate `i` with

\[
\boxed{
R_i\ge4^{1-d}\,k(q_d).
}
\tag{4.4}
\]

No orientation case split remains. The previous “downward scalar variance versus upward-oriented mass” dichotomy is paid into the single nonnegative reserve `R_i`.

Crucially,

\[
q_d\downarrow\frac15,
\qquad
k(q_d)\downarrow k(1/5)=0.007601742187827\ldots>0.
\tag{4.5}
\]

So the **reserve density per bad-fibre mass is dimension-independent** at the parity barrier. The only exponential loss left in this bridge is the available mass floor `4^(1-d)`. This sharply isolates the missing amplification problem.

A parity-guided adaptive restriction tree can choose such a coordinate at every nonconstant node, yielding the explicit global lower bound

\[
\mathcal R_{\mathcal T}(f)
\ge
\sum_{v\text{ nonconstant}}\mu_v\,4^{1-d_v}k(q_{d_v}),
\tag{4.6}
\]

where `d_v` is the Fourier degree of the current state. Equation (4.6) is universal but can still be exponentially small and is **not** a dimension-free FEI payment.

## 5. Decisive calculations

The attached standard-library script evaluates the analytic reserve seed and the Bellman debit on a few structured examples. It is calibration, not proof.

For the parity reserve:

| degree `d` | `q_d` | `k(q_d)` | `4^(1-d) k(q_d)` |
|---:|---:|---:|---:|
| 2 | 0.3333333333 | 0.04222899317 | 1.055724829e-2 |
| 5 | 0.2480507470 | 0.01540756176 | 6.018578814e-5 |
| 15 | 0.2151976935 | 0.009647699395 | 3.594048096e-11 |
| 30 | 0.2074961548 | 0.008566781561 | 2.972199418e-20 |
| 100 | 0.2022272984 | 0.007879804469 | 1.961445744e-62 |

This confirms the analytic diagnosis: the density tends to a positive constant, while the seed mass carries the exponential loss.

For width-two tribes with `s=1,...,5` tribes, exact Walsh evaluation plus Bellman recursion gives respectively

`Phi/I = 0.75955, 0.95172, 1.20764, 1.47983, 1.71321`,

while the accumulated reserve on the minimizing tree is

`R/I = c_*+Phi/I-H/I = 1.64494, 1.62019, 1.35468, 1.07989, 0.91308`.

This is only a structured-family demonstration that the reserve is a real, branch-summable quantity; it is not a class-optimality or full-FEI claim.

A separate tensor check used a 2-bit width-two-tribe factor and a 3-bit majority factor and obtained

`Phi(f)=0.7595508265185061`,

`Phi(g)=0.7595508265185061`,

`Phi(f tensor g)=1.5191016530370123=Phi(f)+Phi(g)`

to the displayed arithmetic precision, in agreement with Theorem 3.1.

Script SHA-256 from the executed source: `8f4376829b0bff578d3112b33a3bf1d4a50a2903c19e776dae971cc464de4a17`.  
Output SHA-256: `0fbf7e4654166b4ecbf216f37d7305ace0427a69927f52ca5a3f0dd8e1ff94a0`.

## 6. Exact remaining implication

The unrestricted conjecture is still open. The decomposition removes one ambiguity from the current proof state.

The next universal target is now the **single summable inequality**

\[
\boxed{
\mathcal E_{\mathcal T}(f)
\le K I(f)+\mathcal R_{\mathcal T}(f)
}
\tag{6.1}
\]

for a dimension-independent `K` and a source-admissibly chosen complete restriction tree (equivalently, prove it for the Bellman-optimal debit with the corresponding reserve). Combining (6.1) with (2.3) gives `H(f)<= (K+c_*)I(f)`.

What remains hard is no longer the sign/orientation split: Theorem 4.1 pays both into `R`. The unresolved step is to show that **low-posterior erasure debit cannot accumulate faster than influence plus this reserve**. B15's valuation/free-energy work is the natural next interface because low posterior means a large amplitude/mesh ratio, while its newest theorem says tensor collision itself is not the obstruction.

The next B18 attack should therefore be non-product and source-exact: derive a restriction-level packet/valuation lower bound on `R` or an upper bound on `E` that is summable under (2.2), retaining cross-packet negative credits. Another exact-endpoint audit or tensor-infection estimate would not address (6.1).

## 7. Claim ledger

### PROVED in this run

- The exact local debit/reserve identity `Delta_i H = c_* p_i + E_i - R_i` with `E_i,R_i>=0`.
- The exact global restriction-tree identity `H = c_* I + E_T - R_T` for every complete adaptive physical restriction tree.
- The Bellman residual potential `Phi=min_T E_T` and universal reduction `H<=c_* I+Phi`.
- Exact tensor additivity `Phi(f tensor g)=Phi(f)+Phi(g)` for disjoint-variable Boolean factors.
- The fibrewise reserve density `rho(q)` unifies curvature and upward orientation.
- Combining B14 strong concavity with the already-proved B18 weighted top-chain theorem gives the universal degree-`d` reserve seed `R_i>=4^(1-d)k(q_d)`, with `k(q_d)` tending to the positive constant `k(1/5)=0.007601742...`.

### CONDITIONAL / inherited dependencies

- The local bound `j(s)<=c_*(s-s^2/3)` uses the proved B14 strong-concavity theorem.
- The existence of an edge with `q>=q_d` and upper mass `>=4^(1-d)` uses the preceding B18 weighted top-chain theorem, whose top-degree granularity input comes from account03/B18.
- The current unrestricted lower-bound correction `>6.521845710923046575` is recovered external work and is used only to avoid calibrating a universal proof to an obsolete smaller target.

### OPEN

- A dimension-independent proof of (6.1), or any equivalent bound on the accumulated low-posterior erasure debit.
- Amplification of the parity reserve seed from `4^(1-d)` scale to the scale of total influence, unless a different packet/valuation bank pays the complementary debit.
- The full uniform-cube Fourier entropy-influence conjecture.

### REFUTED / NOT CLAIMED

- Exact endpoint nonattainment is not a uniform quantitative FEI rebate.
- The finite-degree seed in Theorem 4.1 is not `Omega(I)`.
- The width-two-tribes and tensor calculations are not universal proofs.
- No new sharp FEI constant, publication priority, or full FEI proof is claimed.

**Brain status:** `WITHOUT_VERIFIED_BRAIN`.
