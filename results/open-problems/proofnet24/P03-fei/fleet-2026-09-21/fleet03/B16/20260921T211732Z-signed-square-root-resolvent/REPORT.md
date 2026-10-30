# B16 FEI signed transport — terminal-projector square-root resolvent and local q-flip polarization

**Date:** 21 September 2026  
**Scope:** `fleet03 / B16`, joint FEI interface C  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact signed source decomposition and a refuted generic shortcut. No publication-priority claim.

## 0. What changed

The joint interface-C gap is the authentic signed compiler-to-physical-flags transfer, including the live Borel window, terminal subtraction, dual-code multiplicity, negative credits, and no-reuse bookkeeping.

This run uses a materially different method from a positive parent-pair lift. It keeps the terminal signed projector *inside* a function on the genuine active-syndrome cube, takes the global Boolean phase switch there, and factors its square by the square root of the active-syndrome number operator. The result is an exact sum of positive **local q-flip squares**, but each local square still contains the original terminal signs and same-syndrome cancellation before squaring.

This is designed to respect the fresh no-go from fleet04/B16: the complete positive live current is not universally `O(J)`, so a universal positive contraction of that whole current into the physical flag sink cannot exist. The signed correction has to be inserted before the final positive physical payment.

## 1. Fresh peer results consumed

### 1.1 fleet01/B16 terminal-shell feature projector

Consumed

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B16/20260921T204046Z-terminal-shell-feature-projector/REPORT.md`

and its `RADIAL_FINITE_DIFFERENCE.md` supplement.

For `E=D_d <= C_0=RM(1,n)^perp`, with

`P_0=C_0^perp=RM(1,n)` and `P_1=E^perp`, fleet01 proves that

`alpha = uniform(P_0) - uniform(P_1)`

is the exact orthogonal Fourier projector onto the retained shell `C_0\E`. For every scalar radial feature

`vartheta_phi(q)=phi(m(q)^2)`, `m(q)=N^{-1} sum_x (-1)^{q_x}`,

the phase-switched retained feature has Fourier coefficient

`1_{A in C_0\E} (f_A-1) lambda_|A|^phi`.

After averaging the genuine active syndrome, its square is the exact same-syndrome square; no relationwise absolute value or multiplicity truncation is used.

### 1.2 fleet04/B16 signed Brownian/Cayley handoff

Consumed the newer

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B16/20260921T211200Z-brownian-cayley-signed-remainder/HANDOFF.md`.

It proves that the Brownian finite-difference transform keeps the R32 `0 mod 4 / 2 mod 4` sign before squaring, and records the decisive authentic obstruction: the complete positive half-band current divided by `J(f)` is unbounded on a genuine Boolean family, while the physical signed flag bank is `O(J)`. Hence the missing bridge cannot be a universal PSD contraction of the *whole* positive current. It also keeps the live window as

`live = full-line - T(W^c)`, with `T(W^c)>=0`,

rather than silently replacing the finite window by its full-line majorant.

The present run applies both results to the same explicit source object.

## 2. Authentic active-syndrome function

Let `M` be the active ordered q-flip coordinates and let `S subseteq M` index the genuine dual phase `g_S=(-1)^{q_S}`. The compiler dictionary gives

`q_{S triangle M} = q_S + b_f` modulo an affine character,

where `b_f` is the truth-table word of the actual Boolean phase `f`.

For any scalar feature `phi`, define on the active syndrome cube

\[
F_\phi(S)
:=\sum_r \alpha(r)\,
\phi\!\left(m(q_S+r)^2\right).
\tag{2.1}
\]

The affine-character ambiguity is harmless because `alpha` and the squared correlation feature are affine-gauge invariant.

Fleet01's phase-switched source difference is therefore exactly

\[
\boxed{
D_\phi(S)=F_\phi(S\triangle M)-F_\phi(S).
}
\tag{2.2}
\]

If

\[
F_\phi(S)=\sum_{R\subseteq M} b_R^\phi(-1)^{|S\cap R|},
\tag{2.3}
\]

then each `b_R^phi` is the **signed same-active-syndrome aggregate** of the retained radial coefficients. Translation by the all-active vector has eigenvalue `(-1)^|R|`, hence

\[
\boxed{
\mathbb E_S |D_\phi(S)|^2
=4\sum_{|R|\;\mathrm{odd}} |b_R^\phi|^2.
}
\tag{2.4}
\]

This is the source quantity that must be transported. Terminal subtraction, dual-code multiplicity and relation-size signs are all still inside `F_phi` before the square.

## 3. PROVED — square-root number-operator factorization

For `j in M`, let

\[
\partial_j=\frac{I-\tau_j}{2},
\qquad
L=\sum_{j\in M}\partial_j,
\tag{3.1}
\]

where `tau_j` flips active syndrome coordinate `j`. On the Walsh character indexed by `R`, `L` has eigenvalue `|R|`.

Let

\[
F_\phi^-:=\frac12\left(F_\phi-F_\phi\circ\tau_M\right)
\tag{3.2}
\]

be the global-odd part. It has no zero mode, so `L^{-1/2}` is unambiguous on it.

### Theorem 3.1 — `P03-B16-SIGNED-SQRT-RESOLVENT-FLAG`

For every scalar radial feature `phi`,

\[
\boxed{
\mathbb E_S |D_\phi(S)|^2
=4\sum_{j\in M}
\left\|\partial_j L^{-1/2}F_\phi^-\right\|_2^2.
}
\tag{3.3}
\]

#### Proof

Write `F_phi^- = sum_{|R| odd} b_R^phi chi_R`. Then

\[
\left\|\partial_j L^{-1/2}F_\phi^-\right\|_2^2
=\sum_{\substack{|R|\;\mathrm{odd}\\j\in R}}
\frac{|b_R^\phi|^2}{|R|}.
\]

Summing over `j` contributes exactly `|R|/|R|=1` to every odd syndrome mode. Thus the right side of (3.3) is

`4 sum_{|R| odd}|b_R^phi|^2`,

which is (2.4). QED.

### Why this is useful

There is **no path-length or ambient-dimension loss**. A mode of active-syndrome size `q` is allocated among its `q` genuinely active q-flip directions with exact weight `1/q` before the local squares are summed.

The theorem is not an unsigned-support statement: `F_phi` contains `uniform(P_0)-uniform(P_1)` and the signed relation aggregation before the operator is applied.

## 4. PROVED — positive noise representation of the inverse square root

Let `T_rho^{(-j)}` be the usual product-noise operator on all active syndrome coordinates except `j`. Put

\[
w(\rho)=\frac{1}{\sqrt\pi\sqrt{-\log\rho}},
\qquad 0<\rho<1.
\tag{4.1}
\]

This is a probability density because its integral over `(0,1)` is one.

For every mode `R` containing `j`,

\[
\int_0^1 w(\rho)\rho^{|R|-1}\,d\rho
=|R|^{-1/2}.
\tag{4.2}
\]

Therefore

\[
\boxed{
\partial_jL^{-1/2}F_\phi^-
=\int_0^1 w(\rho)\,
T_\rho^{(-j)}\partial_jF_\phi^-\,d\rho.
}
\tag{4.3}
\]

So (3.3) is an exact decomposition into **oriented local q-flip differences after positive random dual-phase smoothing**. The orientation index `j` is never forgotten. This is the same ordered q-flip coordinate whose coarse parent is the one-subcube mask in fleet02/B16's ordered-flag interface.

A useful small-resolvent corollary is the exact identity

\[
\boxed{
\sum_j\left\|\partial_jL^{-1}T_{1/\sqrt2}F\right\|_2^2
=
\sum_{R\ne\varnothing}\frac{2^{-|R|}}{|R|}|\widehat F(R)|^2.
}
\tag{4.4}
\]

Thus the recurring Hardy factor `2^{-q}/q` is itself a local q-flip square, not merely a scalar multiplier. This is a direct source-side interface to the signed small-resolvent machinery.

## 5. Exact Brownian and Laplace/Shannon consequences

For the Brownian threshold feature

`phi_u(x)=1_{u<=x}`,

fleet01/fleet02 identify the phase bank

\[
\mathcal Q_M(g_S)=\int_0^1 |D_{\phi_u}(S)|^2du.
\]

Fubini and Theorem 3.1 give the exact local decomposition

\[
\boxed{
\mathbb E_S\mathcal Q_M(g_S)
=4\sum_j\int_0^1
\|\partial_jL^{-1/2}F_{\phi_u}^-\|_2^2du.
}
\tag{5.1}
\]

For the Laplace/Shannon feature

`phi_t(x)=exp(-t x)`,

the source bank has the analogous exact form

\[
\boxed{
\mathbb E_S\mathcal Q_S(g_S)
=\frac{4}{\ln2}\sum_j\int_0^\infty
\frac{\|\partial_jL^{-1/2}F_{\phi_t}^-\|_2^2}{t^2}\,dt.
}
\tag{5.2}
\]

No Brownian threshold coefficient, Laplace coefficient, terminal-code term, or same-syndrome multiplicity is bounded separately in (5.1)--(5.2).

For the live Borel corridor, the fresh fleet04 identity is retained as

\[
\text{live bank}=\text{full-line bank}-T(W^c),
\qquad T(W^c)\ge0.
\tag{5.3}
\]

The transform above is applied to the full-line term while the complement remains an explicit **negative remainder**. It is not discarded and not relabelled as a new positive cost.

## 6. Application to joint interface C

The new chain is now:

1. retained terminal shell and phase switch -> exact radial same-syndrome square: **PROVED** by fleet01/B16;
2. live Borel square -> full-line logarithmic/restriction kernel with explicit negative complement: **PROVED** by fleet01/fleet02/fleet04;
3. full-line Brownian/Laplace source -> exact sum of local oriented q-flip square-root-resolvent fields: **PROVED HERE**, equations (3.3), (5.1), (5.2);
4. q-flip index `j` -> authentic one-subcube physical parent and deterministic physical pivot once a residual positive pair law exists: **PROVED** by fleet02/B16 and fleet03/B18;
5. **OPEN:** prove that the *signed/refunded* local fields in (3.3)--(5.2), after the authentic central multiplier and its negative remainder are inserted, produce a residual physical pair measure whose parent intensity is paid once by the physical `kappa` bank.

Step 5 cannot be replaced by a contraction of the complete positive current: the fleet02/fleet04 half-band Boolean counterfamily rigorously refutes that stronger claim.

This locates the refund insertion point more precisely: **before** the final local square is pushed to original-coordinate curvature, at the `L^{-1/2}`/small-resolvent field level, not after one has already formed the complete positive live current.

## 7. REFUTED generic shortcut — raw threshold crossings are not quadratically Lipschitz

A tempting local completion would be to bound each Brownian-threshold difference directly by a quadratic reflection/curvature energy. That generic analytic inequality is false even in three coordinates.

For `epsilon>0`, set

\[
z=(-1,0,1+3\epsilon),\qquad \bar z=\epsilon,
\]

and reflect across the constant direction:

\[
z'=z-2\bar z(1,1,1)
=(-1-2\epsilon,-2\epsilon,1+\epsilon).
\]

Let

\[
B(\epsilon)=\int_0^\infty
\left[
\frac13\sum_i1_{u\le z_i^2}
-
\frac13\sum_i1_{u\le z_i'^2}
\right]^2du.
\]

For `0<epsilon` sufficiently small, direct interval decomposition gives

\[
\boxed{
B(\epsilon)=\frac49\epsilon+\frac{10}{9}\epsilon^2.
}
\tag{7.1}
\]

But

\[
\|z-z'\|_2^2=12\epsilon^2,
\qquad
3\bar z^2=3\epsilon^2.
\]

Hence

\[
\frac{B(\epsilon)}{3\bar z^2}
=\frac{4}{27\epsilon}+\frac{10}{27}\to\infty.
\tag{7.2}
\]

Therefore there is no universal scalar inequality paying unsmoothed Brownian threshold crossings by a local quadratic reflection energy. This is only a refutation of that **generic analytic shortcut**, not an FEI counterexample and not by itself an authentic compiler obstruction. The authentic half-band obstruction from fleet02/fleet04 is stronger and source-valid.

The lesson is consistent: retain the signed/noisy resolvent structure before attempting physical payment.

## 8. Exact computation

`check_signed_square_root_resolvent.py` uses exact rational arithmetic for the discrete identities. It checked:

- 385 nonzero odd-mode/local-coordinate contributions through active dimension seven, verifying (3.3) exactly and the raw Poincare domination;
- 200 spectral checks through syndrome size 100 for the inverse-number/noisy central factor in (4.4);
- the three-coordinate threshold obstruction at `epsilon=1/100,1/1000,1/10000`.

The exact threshold-to-axis ratios were

`410/27`, `4010/27`, and `40010/27`,

showing the predicted `1/epsilon` blow-up.

These calculations are falsification/self-check evidence; the all-dimensional statements above are symbolic proofs.

## 9. Classification and next handoff

**PROVED:** equations (3.3), (4.3), (4.4), and their exact Brownian/Laplace consequences (5.1)--(5.2).

**REFUTED:** any universal *generic* pointwise Brownian-threshold-to-quadratic-reflection estimate of the form needed by the raw shortcut in Section 7.

**CONDITIONAL / OPEN:** physical payment of the signed/refunded local square-root-resolvent fields. The complete positive current cannot be the object paid, by the fresh authentic half-band counterexample.

**Full unrestricted FEI:** **OPEN / NOT PROVED**.

**consumed_peer_artifact:** fleet01/B16 `20260921T204046Z-terminal-shell-feature-projector/{REPORT.md,RADIAL_FINITE_DIFFERENCE.md}` and fleet04/B16 `20260921T211200Z-brownian-cayley-signed-remainder/HANDOFF.md`.

**applied_to_claim:** joint interface C, live-window logarithmic/polarization source -> oriented local q-flip signed square-root-resolvent fields with terminal projection and same-syndrome multiplicity intact.

**remaining_implication:** insert the authentic central multiplier's negative remainder / available no-reuse refund at this local field level and prove the residual source has a positive parent-pair pushforward paid by the fleet03/B18 physical `kappa` bank.

**next_recipient:** fleet03/B18 for integration with `20260921T195855Z-parent-signed-pivotization`, and fleet04/B16 for co-location of its `rho_R` signed remainder with the local `L^{-1/2}` factorization.
