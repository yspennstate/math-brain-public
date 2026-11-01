SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B03, 2026-09-23T22:06:59Z.
attacking: a dependence-safe averaged conditional Hausdorff--Young identity for each independent-copy sum/difference pair, the first endpoint obstruction to using it by absolute reciprocal-coefficient integration, and a splice with the fresh fleet02/B03 marginal-free Z2 theorem.

# fleet01/B03 r34 — averaged conditional Fourier budget without conditional caps

Programme: `QFORM-DENSITY-3EIG-20260922`. Owner control revision `2026-09-22.15`. Status: **NEW SUPPORTING LEMMA + PRECISE ENDPOINT OBSTRUCTION + PARTNER SPLICE; FULL QFORM OPEN**. Full-target continuity remains **OPEN**. Execution state: `WITHOUT_VERIFIED_BRAIN`.

This run changes mechanism from the preceding selector+square optimization. The point is to go back to the exact independent-copy identity

\[
 |\phi_Q(t)|^2=\phi_{Q-Q'}(t),\qquad Q-Q'=D^TAS,
 \quad D=X-X',\ S=X+X',
\]

but to retain the true dependence of each pair \((D_i,S_i)\). The live correction `QFORM-UV-CONDITIONAL-CAP-FALSE` is therefore treated as a premise: no conditional density cap for `S_i|D_i=d` is asserted.

## 1. Exact one-pair setup

Let `X,X'` be iid with density `f`, where `0<=f<=1` and `int f=1`. Put

\[
 D=X-X',\qquad S=X+X'.
\]

The density of `D` is

\[
 h(d)=\int_{\mathbb R} f(x)f(x-d)\,dx.
\]

The joint density of `(D,S)` is

\[
 g(d,s)=\frac12 f\!\left(\frac{s+d}{2}\right)
                 f\!\left(\frac{s-d}{2}\right).
\]

For every `d` with `h(d)>0`, define the **actual** conditional density

\[
 r_d(s)=\frac{g(d,s)}{h(d)}
 =\frac{f((s+d)/2)f((s-d)/2)}{2h(d)},
\]

and its conditional characteristic function

\[
 \psi_d(u)=\int e^{ius}r_d(s)\,ds.
\]

The conditional density `r_d` can have arbitrarily large `L^infinity` norm; nothing below bounds it pointwise.

## 2. Main theorem: an all-q averaged conditional Hausdorff--Young budget

Fix `2<=q<infinity` and set

\[
 p=\frac{q}{q-1}.
\]

Let

\[
 J_p(d)=\int f(x)^p f(x-d)^p\,dx
        =(f^p*\widetilde{f^p})(d).
\]

### Theorem 2.1 — `QFORM-PAIR-AVERAGED-HY-v1`

For every admissible `f` and every finite `q>=2`,

\[
 \boxed{
 \int_{\mathbb R} h(d)^q
       \left(\int_{\mathbb R}|\psi_d(u)|^q\,du\right)\,dd
 \le \pi .}
 \tag{2.1}
\]

Equivalently, if

\[
 F_q(d):=h(d)\,\|\psi_d\|_{L^q(du)},
\]

then

\[
 \boxed{\|F_q\|_{L^q(dd)}\le \pi^{1/q}.}
 \tag{2.2}
\]

This is a dimension-free integrated replacement for the false assertion that the conditional laws `S|D=d` have a uniform density cap.

### Proof

A direct change of variables gives

\[
 \|r_d\|_p^p
 =2^{1-p}h(d)^{-p}J_p(d).
 \tag{2.3}
\]

With Fourier convention `hat r(u)=int exp(ius)r(s)ds`, Hausdorff--Young obtained by interpolating `L1->Linfinity` with Plancherel gives

\[
 \|\psi_d\|_q\le (2\pi)^{1/q}\|r_d\|_p.
\]

Raising to the `q`th power and using `q/p=q-1` and `(1-p)(q-1)=-1`,

\[
 \int |\psi_d(u)|^qdu
 \le \pi\,h(d)^{-q}J_p(d)^{q-1}.
 \tag{2.4}
\]

Hence the left side of (2.1) is at most

\[
 \pi\int J_p(d)^{q-1}\,dd.
\]

Set `r=2/p=2(q-1)/q`. Young's convolution inequality gives

\[
 \|J_p\|_{q-1}
 \le \|f^p\|_r^2.
\]

Because `pr=2`,

\[
 \|f^p\|_r=(\int f^2)^{1/r}\le1
\]

from `0<=f<=1` and `int f=1`. Therefore `int J_p^(q-1)<=1`, proving (2.1). QED.

### Scaled form

For every measurable coefficient `a(d)` with `a(d)!=0`, the same calculation and the change `u=t a(d)` give

\[
 \boxed{
 \int h(d)^q |a(d)|
       \left(\int |\psi_d(t a(d))|^qdt\right)dd\le\pi .}
 \tag{2.5}
\]

No independence between `D` and `S` is used in (2.1)--(2.5).

## 3. Exact product-pair representation for the full quadratic form

For independent input coordinates, the pairs `(D_i,S_i)` are independent **across i**, while `D_i` and `S_i` remain dependent inside each pair. Conditioning only on the whole vector `D=d` is legitimate and gives

\[
 \boxed{
 |\phi_Q(t)|^2
 =\int_{\mathbb R^n}
   \prod_i h_i(d_i)\,
   \prod_i \psi_{i,d_i}\bigl(t(Ad)_i\bigr)\,dd .}
 \tag{3.1}
\]

Equation (3.1), together with (2.1), is the exact dependence-safe decoupled starting point requested by the assignment. It is important that `(Ad)_i` may depend on all `d_j`; the theorem does not pretend that the coefficients separate after rotation.

## 4. First essential missing implication: why the obvious Minkowski closure is not uniform

One tempting next move is to take an `L^q(dt)` norm after (3.1), use Minkowski in a single difference variable, and then use the conditional Hausdorff--Young estimate. Even in the scalar coefficient model `a(d)=d`, that creates the Hardy functional

\[
 \mathcal H_{p,q}(f)
 :=\int_{\mathbb R}J_p(d)^{1/p}|d|^{-1/q}\,dd.
 \tag{4.1}
\]

Indeed (2.4) says

\[
 h(d)\,\|\psi_d(t d)\|_{L^q(dt)}
 \le \pi^{1/q}J_p(d)^{1/p}|d|^{-1/q}.
 \tag{4.2}
\]

### Proposition 4.1 — the absolute reciprocal-coefficient closure is nonuniform

For every finite `q>2` (and in particular at the natural `q=3` three-factor endpoint) there is a cap-one probability density `f` for which

\[
 \mathcal H_{p,q}(f)=\infty.
 \tag{4.3}
\]

Thus (2.1) is valid, but a proof that immediately spends it by Minkowski/absolute integration in the difference variable can lose all uniformity. This is an obstruction to that **proof interface**, not a counterexample to QFORM.

### Proof

Choose `0<eps<=p-1`, and for `k>=3` let

\[
 a_k=\frac{c}{k(\log k)^{1+\varepsilon}},
\]

with `c>0` so small that `sum a_k<1/4`. Put

\[
 A=1-\sum_{k>=3}a_k>3/4,
 \qquad I_0=[0,A],
 \qquad I_k=[4k,4k+a_k],
\]

and let

\[
 f=1_E,\qquad E=I_0\cup\bigcup_{k>=3}I_k.
\]

Then `f` is a probability density and `0<=f<=1`. Since `f^p=f`,

\[
 J_p(d)=h(d)=|E\cap(E+d)|.
\]

For

\[
 D_k=[4k-A/2,\,4k-A/4],
\]

and all large `k`, the translated interval `I_k-d` lies inside `I_0`, hence

\[
 J_p(d)\ge a_k\quad(d\in D_k).
\]

The `D_k` are disjoint, have length `A/4`, and `|d|\asymp k`. Consequently

\[
 \mathcal H_{p,q}(f)
 \ge c_A\sum_{k>=3}a_k^{1/p}k^{-1/q}
 =c'_A\sum_{k>=3}
 \frac{1}{k(\log k)^{(1+\varepsilon)/p}}.
\]

Because `1/p+1/q=1` and `eps<=p-1`, we have `(1+eps)/p<=1`, so the final series diverges. QED.

For the concrete critical choice `q=3`, `p=3/2`, one may take `eps=1/4`; the divergent lower series is

\[
 \sum_k \frac1{k(\log k)^{5/6}}.
\]

This construction is deliberately compatible with the live fragmented-support correction. The correct next use of (2.1) must average before taking the reciprocal coefficient absolutely (for example through a TT* / volume aggregate), rather than condition first and pay `|(Ad)_i|^{-1/q}` pointwise.

## 5. Designated partner fleet02/B03 applied to an actual inequality

Fresh partner source: `yspennstate/math-open-problems@68e6d8f52d904033878f6f55c376c38fd214684e`, fleet02/B03, theorem `QFORM-Z2-HALFRIESZ-MARGINAL-FREE-v1` and its square receiver.

Let a genuine original coordinate `X_j` have nonzero physical square coefficient `d=A_jj`, and complete the square without rotating the product law:

\[
 Q=d[X_j+h(W)]^2+R(W).
\]

For any original-coordinate cut `(I,J)` inside the Schur residual define

\[
 Z_2=e_2(MM^T),\qquad M=A_R[I,J].
\]

The fresh partner theorem gives, with **no two-volume row-marginal gate**,

\[
 \boxed{
 \|p_Q\|_\infty
 \le 8e^{1/4}|d|^{-1/2}Z_2^{-1/8}
 =8e^{1/4}(|d|^4Z_2)^{-1/8}.}
 \tag{5.1}
\]

Therefore the concrete scale-invariant branch

\[
 \boxed{|d|^4 Z_2\ge1}
 \tag{5.2}
\]

is completely paid by

\[
 \boxed{
 \|p_Q\|_\infty\le8e^{1/4}
 =10.2722033335019\ldots,
 \qquad
 \Pr(Q\in I)\le10.2722033335019\,|I|.}
 \tag{5.3}
\]

This is an actual one-copy linear small-ball inequality. Continuity is not supplied by this square-peel theorem and is recorded separately.

The partner's whole-copy estimate also gives

\[
 \boxed{
 \int |t|^{-1/2}|\phi_R(t)|^2dt
 \le \frac{16}{3}\sqrt{2\pi}\,e^{1/4}Z_2^{-1/8}.}
 \tag{5.4}
\]

Thus any state not paid by (5.3) at this chosen pivot/cut must satisfy the quantitative survivor inequality

\[
 |d|^4Z_2<1.
 \tag{5.5}
\]

The new pair theorem (2.1) is intended for this weak-pivot / weak-Z2 remainder, but Proposition 4.1 shows that the naive conditional-Minkowski route cannot be the missing bridge.

## 6. What is and is not proved

Proved in this run:

1. the exact all-`q` averaged conditional Fourier budget (2.1), retaining the real `(D,S)` dependence;
2. the exact product-pair representation (3.1) for `|phi_Q|^2`;
3. a rigorous fragmented-support counterexample to the first obvious reciprocal-coefficient/Minkowski closure;
4. the partner splice (5.1)--(5.5), which gives linear small-ball scaling whenever one genuine square and one residual physical Z2 aggregate satisfy `|d|^4 Z2>=1`.

Not proved:

- a universal way to force (5.2) from `s_3(A)>=1`;
- a universal integrated estimate from (2.1) in the complementary weak-pivot/weak-Z2 branch;
- the full bounded-density conjecture;
- the full-target continuity statement.

The next B03 mechanism should keep the `d`-average **inside** TT*/volume averaging long enough to avoid the divergent Hardy functional (4.1). A promising concrete target is a two-coordinate version of (2.1) in which the determinant/Jacobian is paid only after averaging squared two-volume, matching the marginal-free `Z2` invariant rather than an individual reciprocal coefficient.

## 7. Source pins and integrity


No Gaussianity, log-concavity, moments, compact support, connected support, diagonal-basis independence, conditional cap, or law-uniform pointwise quadratic decay is used. No scheduler/task/email/notification/permission/installation/public-release mutation is part of this run.
