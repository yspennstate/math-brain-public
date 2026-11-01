Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but this runtime exposes no authenticated completed-run effort telemetry or binding scheduler selector, so I do not claim otherwise.

# P07-B — coherent-origin obstruction to one-shot clipping, and an exact active-set Schur dual repair

**Native role:** `P07-B`, task `6aabe797a39081919acc889f29f4c556`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured start master:** `90b83fab0ad3b04f35a7ecd89da137f53d2a32d8`  
**Fresh pre-write master:** `fa264fc36d323076c71bdf640b3693a0d1b7ccf4`  
**Previous own report:** `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T0328+0300__zero_diagonal_exceptional_certificate.md`  
**Complementary P07-A checkpoint used:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T0347+0300__haar_exact_cone_threshold.md`  
**Outside target:** Randomstrasse101, arXiv:2603.29571, Conjecture 18; primary partial-result paper arXiv:2502.16227.  
**Exact source endpoint:** for the dense random circulant source model on odd `n`,

\[
\mathbb E\,\vartheta(G_n)=(1+o(1))\sqrt n.
\]

**Inherited rigorous source bound:**

\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

Hence the fixed full-source loss metric remains

\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]

This run nevertheless changes the proof architecture materially. It proves that the previous report's proposed **fixed-threshold one-shot leakage lemma is false**: the zero-diagonal clipping correction has a coherent origin feedback of positive constant expected size when `tau=A/sqrt(n)` with fixed `A`. It then replaces that false target by an exact active-set interpolation certificate using a principal block of `P_C`, derives the Schur-complement cross-leakage energy identity and a multiscale violation census, and gives a new source-exact sufficient lemma whose `beta<1/2` case improves the published iterated-log exponent and whose `beta=0` case removes it.

Status: **OPEN / PROVED PARTIAL**. No sharp source bound is claimed.

---

## 0. Continuity used, without restarting the source audit

The assignment-time source/current-literature check and exact LP recovery were already done in the preceding P07-B report. This run therefore starts from the exact inherited one-sided Fourier completion problem rather than repeating source screening.

Let `n` be odd, `m=(n-1)/2`, and let `xi_a in {0,1}`, `a=1,...,m`, be the independent fair source bits selecting conjugate frequency pairs. Write

\[
P_D=\sum_{a:\xi_a=1}Q_a,\qquad
P_C=\sum_{a:\xi_a=0}Q_a,\qquad
P_0=\frac1n\mathbf1\mathbf1^T,
\]

so

\[
P_0+P_D+P_C=I.
\]

Set

\[
x:=x_D=P_De_0,
\qquad d=\operatorname{rank}(P_D),\quad c=\operatorname{rank}(P_C).
\]

The exact source completion parameter is

\[
\kappa_D
=\inf_{q\in\operatorname{Ran}(P_C)}\max_j(x-q)_j,
\tag{0.1}
\]

and the inherited exact identities are

\[
\vartheta(\overline{G_D})=1+n\kappa_D,
\qquad
\mathbb E\vartheta(G_D)=1+n\mathbb E\kappa_D,
\tag{0.2}
\]

and, with P07-A's complementary orthant ratio,

\[
R_C=n\kappa_D=\frac1{\delta_D}.
\tag{0.3}
\]

The previous P07-B report proposed, for

\[
a_\tau=(x-\tau\mathbf1)_+,
\qquad
\alpha_C=c/n,
\qquad
K_C=P_C-\alpha_C I,
\]

the feasible one-shot correction

\[
q_\tau=\alpha_C^{-1}P_Ca_\tau
\]

and proved

\[
\kappa_D\le
\tau+\alpha_C^{-1}\|(-K_Ca_\tau)_+\|_\infty.
\tag{0.4}
\]

The proposed next target was to make the last norm `O(n^{-1/2})` at `tau=A/sqrt(n)`. The first result below shows that target is impossible for every fixed `A`.

---

# 1. Exact obstruction: the one-shot clipping correction has coherent origin feedback

Write `a=a_tau` and let `a^\circ` denote its restriction to the nonzero time coordinates `1,...,n-1`.

For every nonzero offset `s`, the off-diagonal identity `P_0+P_D+P_C=I` gives

\[
(P_C)_{0s}=-\frac1n-x(s).
\tag{1.1}
\]

Also `(K_C)_{00}=0`. Therefore

\[
(K_Ca)(0)
=\sum_{s\ne0}\left(-\frac1n-x(s)\right)a(s).
\tag{1.2}
\]

On the support of `a`, we have `x(s)=a(s)+tau`. Thus (1.2) is not merely bounded in sign; it is exactly

\[
\boxed{
-(K_Ca)(0)
=
\|a^\circ\|_2^2
+\left(\tau+\frac1n\right)\|a^\circ\|_1.
}
\tag{1.3}
\]

In particular,

\[
\boxed{
\|(-K_Ca)_+\|_\infty\ge \|a^\circ\|_2^2.
}
\tag{1.4}
\]

This is a deterministic identity for every source mask. The diagonal of `K_C` really is zero, but zero diagonal does **not** eliminate coherent feedback into the origin from the many positive off-origin excess coordinates.

### Consequence for fixed target-scale threshold

Fix `A>0` and put

\[
\tau_n=\frac A{\sqrt n}.
\]

For every nonzero `j`,

\[
x(j)
=-\frac1{2n}
+\frac1n\sum_{a=1}^{m}\varepsilon_a
\cos(2\pi aj/n),
\tag{1.5}
\]

where `varepsilon_a=2xi_a-1` are independent Rademacher signs. The exact trigonometric identity

\[
\sum_{a=1}^{m}\cos^2(2\pi aj/n)=\frac{n-2}{4}
\tag{1.6}
\]

holds for every `j != 0`, since `n` is odd. Moreover

\[
\sum_a |\cos(2\pi aj/n)|^3\le m.
\]

Hence the Berry--Esseen bound for the weighted Rademacher sum in (1.5) is `O(n^{-1/2})`, uniformly over every nonzero `j`. If

\[
Z\sim N(0,1),
\]

then

\[
\sqrt n\,x(j)\Rightarrow \frac Z2
\]

uniformly in `j != 0`. Hoeffding tails give uniform integrability for the squared positive parts, so

\[
n\,\mathbb E\left(x(j)-\frac A{\sqrt n}\right)_+^2
\longrightarrow
c_2(A)
:=\mathbb E\left(\frac Z2-A\right)_+^2,
\tag{1.7}
\]

uniformly in nonzero `j`. Explicitly,

\[
c_2(A)
=\frac14\left((1+4A^2)Q(2A)-2A\phi(2A)\right)>0
\tag{1.8}
\]

for every fixed finite `A`, where `phi` is the standard Gaussian density and `Q=1-Phi`.

Summing (1.7) over `j=1,...,n-1` gives

\[
\boxed{
\mathbb E\|a^\circ\|_2^2\longrightarrow c_2(A)>0.
}
\tag{1.9}
\]

Combining (1.3)--(1.4) with (1.9),

\[
\boxed{
\liminf_{n\to\infty}
\mathbb E\|(-K_Ca_{A/\sqrt n})_+\|_\infty
\ge c_2(A)>0.
}
\tag{1.10}
\]

### Correction to the preceding report

The previous proposed `Missing Leakage Lemma L(beta)` asked, for fixed `A`, for

\[
\mathbb E\|(-K_Ca_{A/\sqrt n})_+\|_\infty
\lesssim \frac{(\log\log n)^\beta}{\sqrt n}.
\]

Equation (1.10) proves that this statement is **false for every fixed `beta` and fixed finite `A`**. Therefore the one-shot certificate (0.4) cannot remove the iterated-log loss at a constant threshold.

This does not invalidate (0.4); it invalidates the proposed fixed-scale estimate for its leakage term. If `A=A_n\to\infty`, the Gaussian tail in `c_2(A_n)` shrinks, so the certificate can still participate at a coarser first scale. What fails is the attempted direct jump to the final `1/sqrt(n)` scale.

This is useful negative progress: the multiscale repair must **interpolate the primary active coordinates exactly**, not merely cancel each coordinate's diagonal self-term.

---

# 2. Replacement construction: exact active-set Schur interpolation

Fix any `tau>0` and define the active set and excess vector

\[
S=S_\tau:=\{j:x(j)>\tau\},
\qquad
w:=x_S-\tau\mathbf1_S.
\tag{2.1}
\]

Thus `w>0` coordinatewise and `w=a_tau|_S`.

Let `E_S:R^S -> R^n` be the coordinate embedding and set

\[
M_S:=E_S^TP_CE_S=P_C[S,S].
\tag{2.2}
\]

Assume for the moment that `M_S` is invertible. Define

\[
\boxed{
q_S^*:=P_CE_SM_S^{-1}w.
}
\tag{2.3}
\]

This vector lies in `Ran(P_C)` by construction.

## Theorem P07-B.3 — exact active-set dual repair

Under the invertibility hypothesis above,

\[
(q_S^*)_S=w,
\tag{2.4}
\]

and hence

\[
(x-q_S^*)_j=\tau
\qquad(j\in S).
\tag{2.5}
\]

For the inactive coordinates `j notin S`, `x(j)<=tau`, so

\[
\boxed{
\kappa_D
\le
\tau+\|(-(q_S^*)_{S^c})_+\|_\infty.
}
\tag{2.6}
\]

Equivalently, with the cross block `B_S=P_C[S^c,S]`,

\[
\boxed{
\kappa_D
\le
\tau+
\left\|\left(-B_SM_S^{-1}w\right)_+\right\|_\infty.
}
\tag{2.7}
\]

### Proof

Restrict (2.3) to `S`:

\[
E_S^Tq_S^*
=E_S^TP_CE_SM_S^{-1}w
=M_SM_S^{-1}w=w.
\]

This proves (2.4), and (2.5) follows from the definition of `w`. Outside `S`,

\[
x(j)-q_S^*(j)
\le
\tau+(-q_S^*(j))_+.
\]

Taking the maximum and using the feasibility `q_S^* in Ran(P_C)` in (0.1) proves (2.6)--(2.7). ∎

The coherent origin obstruction in Section 1 is now removed exactly whenever the origin belongs to `S`: the correction enforces the desired residual value `tau` at the origin together with every other primary peak, rather than allowing all off-origin excess mass to feed back into it.

---

# 3. Exact Schur energy identity and a multiscale violation census

The active-set correction has a useful exact energy formula. Since `P_C` is an orthogonal projection,

\[
\|q_S^*\|_2^2
=\langle E_SM_S^{-1}w,
P_CE_SM_S^{-1}w\rangle
=w^TM_S^{-1}w.
\tag{3.1}
\]

On `S`, `q_S^*=w`, so

\[
\boxed{
\|(q_S^*)_{S^c}\|_2^2
=w^T(M_S^{-1}-I)w.
}
\tag{3.2}
\]

The same identity follows from the `SS` block of `P_C^2=P_C`:

\[
M_S^2+B_S^TB_S=M_S.
\]

If

\[
\lambda_{\min}(M_S)\ge\gamma>0,
\]

then

\[
\boxed{
\|(q_S^*)_{S^c}\|_2^2
\le(\gamma^{-1}-1)\|w\|_2^2.
}
\tag{3.3}
\]

This does not by itself control the maximum at the `1/sqrt(n)` scale, but it gives a rigorous multiscale census. For `u>0`, define the set of **deep new violations**

\[
V_u:=\left\{j\notin S:
 x(j)\le\tau-u,
\ x(j)-q_S^*(j)>\tau
\right\}.
\]

Every `j in V_u` has `-q_S^*(j)>u`, so

\[
\boxed{
|V_u|
\le
\frac{w^T(M_S^{-1}-I)w}{u^2}.
}
\tag{3.4}
\]

Thus after one exact active-set repair, any new violations split into two mathematically different classes:

1. a **near-threshold band** `tau-u < x(j) <= tau`, controlled by source small-ball information;
2. a **deep cross-leakage set**, whose cardinality is controlled by the Schur energy (3.4).

This is the multiscale structure the one-shot clipping certificate lacked.

---

# 4. The active set is deterministically below the free rank at a fixed constant threshold, modulo only density

The preceding P07-B report proved the deterministic energy census

\[
|S_\tau|\tau^2\le\|x\|_2^2=\frac dn.
\]

Hence

\[
\boxed{
|S_\tau|\le\frac{d}{n\tau^2}.
}
\tag{4.1}
\]

At

\[
\tau=\frac A{\sqrt n},
\]

this becomes

\[
|S_\tau|\le\frac d{A^2}.
\tag{4.2}
\]

For example, at `A=2`, on the ordinary source-density event

\[
d\le\frac34(n-1),
\qquad
c\ge\frac14(n-1),
\tag{4.3}
\]

we have

\[
|S_{2/\sqrt n}|
\le\frac d4
\le\frac3{16}(n-1)
<c.
\tag{4.4}
\]

The complement of (4.3) has exponentially small probability by a binomial Chernoff bound. So **cardinality is not the obstacle** to an exact constant-scale interpolation. The real obstacle is the source-dependent conditioning/cross-leakage of the principal block `M_S`.

For prime `n`, there is an additional exact structural fact: writing `F_C` for the `c` selected nonzero Fourier rows,

\[
M_S=\frac1nF_{C,S}^*F_{C,S}.
\]

Chebotarev full-spark of the prime Fourier matrix implies that `M_S` is invertible whenever `|S|<=c`. Therefore, on prime orders and the density event (4.3), the active-set certificate (2.3) at `tau=2/sqrt(n)` is automatically well-defined. This is **not** a full-source theorem because Conjecture 18 ranges over the source model generally, including composite odd orders, and invertibility alone does not control the cross maximum in (2.7).

---

# 5. Dependence-aware auxiliary lemma: exact leave-one-frequency decomposition has ideal square-function scale

The previous report proved that one source bit changes the threshold set in only `O(sqrt(n))` coordinates on average. Here is a complementary exact calculation showing that, after leave-one-bit decoupling, the natural square function is already on the desired `n^{-1/2}` scale.

For each pair index `b`, define

\[
T_b:=Q_b-\frac2nI.
\tag{5.1}
\]

Since each `Q_b` is a rank-two orthogonal projection with diagonal `2/n`, `T_b` has zero diagonal. Also

\[
K_C=\sum_{b=1}^m(1-\xi_b)T_b.
\tag{5.2}
\]

Let `a^{(b,0)}` be the excess vector obtained by forcing `xi_b=0` while leaving every other source bit unchanged. On the event `xi_b=0`, the actual `a` equals `a^{(b,0)}`. Therefore there is an exact leave-one-out identity

\[
\boxed{
K_Ca
=\sum_{b=1}^m(1-\xi_b)T_ba^{(b,0)}.
}
\tag{5.3}
\]

For each `b`, the coefficient vector `a^{(b,0)}` is independent of its own selector `xi_b`. This does **not** make the summands mutually independent; each coefficient still depends on all the other source bits.

## Lemma P07-B.4 — deterministic frame bound

For every deterministic `v in R^n` and every time coordinate `j`,

\[
\boxed{
\sum_{b=1}^m |(T_bv)(j)|^2
\le\frac2n\|v\|_2^2.
}
\tag{5.4}
\]

### Proof

Put `u_b=T_be_j`. The Gram matrix of the vectors `u_b` has diagonal

\[
\|u_b\|_2^2=\frac2n-\frac4{n^2}
\]

and, for `b != c`, off-diagonal entry

\[
\langle u_b,u_c\rangle=-\frac4{n^2},
\]

using `Q_bQ_c=0` and `(Q_b)_{jj}=2/n`. Thus its eigenvalues are

\[
\frac2n
\quad\text{(multiplicity `m-1`)},
\qquad
\frac2{n^2}
\quad\text{(multiplicity `1`)}.
\]

The associated frame operator therefore has norm `2/n`, which is exactly (5.4). ∎

Now compare `a^{(b,0)}` with the actual `a`. Put

\[
\Delta_b=a^{(b,0)}-a.
\]

If `xi_b=0`, then `Delta_b=0`. If `xi_b=1`, forcing the bit off changes `x` by `-Q_be_0`. Since the hinge `t -> (t-tau)_+` is 1-Lipschitz coordinatewise,

\[
\|\Delta_b\|_2
\le\|Q_be_0\|_2
=\sqrt{\frac2n}.
\tag{5.5}
\]

Also

\[
\|T_be_j\|_2\le\sqrt{\frac2n},
\]

so

\[
|(T_b\Delta_b)(j)|\le\frac2n.
\tag{5.6}
\]

Because `tau>=0`, `||a||_2<=||x||_2<=1`. Combining (5.4)--(5.6),

\[
\boxed{
\sum_{b=1}^m
|(T_ba^{(b,0)})(j)|^2
\le\frac8n
}
\tag{5.7}
\]

for every mask, every coordinate `j`, and every `tau>=0`.

So the leave-one-frequency summands have the **correct square-function size `O(n^{-1/2})`** before taking a maximum. What is missing is not variance scale; it is a theorem preventing the dependence through the other bits from aligning the summands coherently. The exact origin identity (1.3) is a concrete warning that own-bit independence alone is insufficient.

Indeed, abstractly, coefficients can be independent of their own Rademacher sign and still align perfectly through all the other signs. Hence no generic independent-coordinate concentration inequality is valid for (5.3). A future argument has to exploit the weak threshold influence / Fourier structure, not merely the leave-one-out syntax.

This is precisely consistent with the owner's instruction not to treat dependent Fourier coordinates as independent.

---

# 6. Replacement exact lemma that would improve or remove the iterated-log loss

The false fixed-threshold leakage target from the preceding report should be replaced by a source-generated **active-set Schur leakage** estimate.

Fix `A>0` and `beta>=0`, and put

\[
\tau_n
=A\frac{(\log\log n)^\beta}{\sqrt n},
\qquad
S_n=\{j:x(j)>\tau_n\},
\qquad
w_n=x_{S_n}-\tau_n\mathbf1.
\tag{6.1}
\]

Let

\[
M_n=P_C[S_n,S_n],
\qquad
B_n=P_C[S_n^c,S_n].
\]

Define the good event `G_n` that `M_n` is invertible. The following is a sufficient theorem in exactly the source normalization.

## Missing Active-Set Schur Leakage Lemma `ASL(beta)`

Prove, for some finite `K`,

\[
\boxed{
\Pr(G_n^c)
+
\mathbb E\left[
\mathbf1_{G_n}
\left\|
\left(-B_nM_n^{-1}w_n\right)_+
\right\|_\infty
\right]
\le
K\frac{(\log\log n)^\beta}{\sqrt n}.
}
\tag{6.2}
\]

Then Theorem P07-B.3 and the trivial bound `kappa_D<=1` on `G_n^c` give

\[
\mathbb E\kappa_D
\le
(A+K)\frac{(\log\log n)^\beta}{\sqrt n},
\tag{6.3}
\]

and therefore

\[
\boxed{
\mathbb E\vartheta(G_n)
\le
O\left(\sqrt n(\log\log n)^\beta\right).
}
\tag{6.4}
\]

Consequently:

- any `beta<1/2` in `ASL(beta)` strictly improves the strongest recovered published exponent;
- `ASL(0)` removes the iterated-log loss completely and proves `E theta(G_n)=O(sqrt(n))`;
- `ASL(0)` still does **not** prove the sharp leading constant `1`.

A high-probability version is equally sufficient if its failure probability is `O((log log n)^beta/sqrt(n))`, since `kappa_D<=1` on failure.

For the immediate log-removal target, `A=2`, `beta=0` is attractive: Section 4 shows the active set is deterministically smaller than the free rank on the exponentially likely density event. Thus the main content of `ASL(0)` is not a cardinality estimate; it is a **dependence-aware lower-tail/conditioning theorem for the source-generated principal block together with a one-sided cross-leakage estimate**.

---

# 7. How to attack `ASL(0)` without duplicating P07-A

P07-A has now calibrated the exact primal cone and proved that its half-dimensional Haar threshold has leading constant one. I do not duplicate that cone-universality route here. The Fourier-dual next attack is instead the source-dependent Schur vector in (6.2).

The most concrete multiscale program is:

1. **Coarse exact interpolation.** Start at `tau_0=2/sqrt(n)` (or initially at a slowly larger threshold if needed). On the usual density event the active-set cardinality is below `rank(P_C)`. Prove source-generated invertibility/conditioning of `M_{S_0}` rather than a uniform RIP theorem over all sets of the same size.

2. **Split near-threshold and deep violations.** For a slack `u`, use a dependence-aware small-ball estimate for the near-threshold band
   \[
   \{j: \tau_0-u<x(j)\le\tau_0\}
   \]
   and use the exact Schur energy census (3.4) for deep cross-leakage.

3. **Repair only the newly created exceptional set.** Iterate the same interpolation on the next violating set. The goal is geometric decay of either the violating-set size or Schur energy. This avoids asking one correction to absorb the coherent origin feedback that invalidated the previous route.

4. **Use the leave-one-frequency frame bound to control dependence errors.** In proving source-generated conditioning or cross-leakage, force one pair bit off, use (5.3), and sum squared errors through the exact `2/n` frame inequality (5.4) instead of an `n`-fold union bound. The previous `O(sqrt(n))` expected threshold-set influence bound identifies where forcing a bit can change the active set.

5. **Only then sharpen constants.** If `ASL(0)` is proved, the exponent reaches zero. The sharp `(1+o(1))` constant remains a separate second stage, naturally calibrated by P07-A's cone threshold and the exact bridge `R_C=n kappa_D`.

A generic fixed-vector partial-Fourier RIP theorem is not enough: `S_n` and `w_n` are generated by the same mask as `P_C`. Conversely, a certified finite LP would only illustrate the geometry and is not an asymptotic solution.

---

# 8. Progress ledger

```yaml
ledger_delta:
  native_task_id: "6aabe797a39081919acc889f29f4c556"
  role: "P07-B Fourier dual / exceptional frequencies"
  target: "Randomstrasse101 Conjecture 18 / dense random circulant Lovasz theta"
  captured_start_master: "90b83fab0ad3b04f35a7ecd89da137f53d2a32d8"
  fresh_prewrite_master: "fa264fc36d323076c71bdf640b3693a0d1b7ccf4"
  source_metric: "alpha_LL"
  metric_before: "1/2"
  metric_after: "1/2"
  inherited_bound: "sqrt(n) <= E theta(G_n) <= C sqrt(n log log n)"
  mathematical_status: "OPEN / PROVED PARTIAL"
  proved_this_run:
    - "exact origin feedback identity -(K_C a)(0)=||a_off||_2^2+(tau+1/n)||a_off||_1"
    - "for tau=A/sqrt(n), E||a_off||_2^2 -> c_2(A)>0 uniformly via weighted-Rademacher Berry-Esseen"
    - "therefore the prior fixed-A Missing Leakage Lemma L(beta) is false"
    - "exact active-set Schur interpolation q=P_C E_S M_S^{-1}w"
    - "kappa_D <= tau + ||(-P_C[S^c,S]M_S^{-1}w)_+||_infty"
    - "exact cross-energy identity ||q_{S^c}||_2^2=w^T(M_S^{-1}-I)w"
    - "multiscale deep-violation census"
    - "active-set cardinality below free rank at tau=2/sqrt(n) on ordinary density event"
    - "prime-order full-spark gives invertibility when |S|<=c (partial structural fact only)"
    - "exact leave-one-frequency decomposition and deterministic 2/n frame bound"
    - "leave-one-frequency square function <=8/n despite same-mask dependence"
  corrected_previous_target:
    - "fixed-A one-shot zero-diagonal leakage O(n^-1/2) is impossible because of coherent origin feedback"
  new_missing_lemma: "ASL(beta), equation (6.2)"
  implication:
    - "beta<1/2 improves the published iterated-log exponent"
    - "beta=0 proves E theta=O(sqrt(n)), but not leading constant 1"
  remaining_gap: "source-generated principal-block conditioning plus one-sided Schur cross-leakage at the target scale, with failure probability small enough for expectation"
  next_attack: "multiscale active-set interpolation: near-threshold small-ball + deep Schur-energy census + leave-one-frequency frame control"
```
