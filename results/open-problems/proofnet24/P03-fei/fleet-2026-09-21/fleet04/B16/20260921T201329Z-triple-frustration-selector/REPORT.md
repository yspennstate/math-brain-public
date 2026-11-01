# B16 FEI signed transport — precompression triple-frustration selector

**Date:** 21 September 2026  
**Scope:** `fleet04 / B16`, FEI signed transport / interface C  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact physical mixed-difference identity, a dimension-free double-resolvent payment for the phase-switched authentic clone pair, and a sharp scope obstruction. No novelty or publication-priority claim.

## 0. Route and fresh cross-account dependency

This run follows `FEI-JOINT-FOUR-ACCOUNTS-2026-09-21-192650Z` and substantively consumes the newest completed compatible fleet01/B16 result

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B16/20260921T190712Z-clone-pair-resolvent-transfer/REPORT.md`.

That report proves, for an authentic ordered-min one-subcube parent `g=h_0h_1` of codimension `c>=2`, an exact paired physical plaquette identity and the product-noise event estimate

\[
\mathbb E_{U_s,V_t}\Pr_y[Q_{h_0}=-1,Q_{h_1}=-1]
\le 2st(1-st)J(g),\qquad 0\le s,t\le\tfrac12.
\tag{0.1}
\]

The newest fleet02/B16 handoff then showed that *postcompressing* an authentic parent to a scalar charge and inverting the tiny parent plaquette amplitude incurs an unavoidable codimension normalization factor. It prescribed the opposite order: preserve the signed three-phase source

\[
\Delta_{h_0}\Delta_{h_1}\Delta_f\Psi_s
\tag{0.2}
\]

before any positive scalar parent reconstruction.

The new step below does exactly that on the physical side. It inserts the **actual Boolean phase switch** into fleet01's clone-pair plaquette operator *before taking an absolute value*. The resulting operator is not a sum of two separately paid backgrounds. It collapses to one signed event requiring simultaneous frustration by both clone slices and by the real Boolean phase.

No R32 coefficient is positive-parted. The terminal mixed difference is not separated or claimed paid. R16 moment refunds, negative entropy credits and terminal-band payment remain reserved.

---

## 1. Setup

Work on the dummy-enlarged physical cube. Let `H` be an arbitrary Boolean background phase and let the authentic parent slices be Boolean phases `h_0,h_1` with

\[
h_0h_1=g.
\tag{1.1}
\]

For translations `u,v`, define the plaquette sign

\[
Q_H(y;u,v)=H(y)H(y+u)H(y+v)H(y+u+v)
\tag{1.2}
\]

and the frustration probability

\[
P_H(u,v)=\Pr_y[Q_H(y;u,v)=-1].
\tag{1.3}
\]

For phase multiplication write `T_a P_H=P_{Ha}` and

\[
\Delta_a=I-T_a.
\tag{1.4}
\]

Thus fleet01's authentic clone-pair operator is

\[
\mathfrak D_{h_0,h_1}P_H
:=\Delta_{h_0}\Delta_{h_1}P_H
=P_H+P_{Hg}-P_{Hh_0}-P_{Hh_1}.
\tag{1.5}
\]

Its exact identity is

\[
\mathfrak D_{h_0,h_1}P_H
=-\frac12\,\mathbb E_y\!
\left[Q_H(1-Q_{h_0})(1-Q_{h_1})\right].
\tag{1.6}
\]

The source-side fleet04 identity from the preceding run has the same phase operator:

\[
D_jF_s^{\rm odd}
=\frac12\Delta_{h_0}\Delta_{h_1}\Delta_f\Psi_s.
\tag{1.7}
\]

The missing question is what `Delta_f` does to the *physical* clone-pair object.

---

## 2. PROVED — exact triple-frustration selector

### Theorem 2.1 — `P03-B16-TRIPLE-FRUSTRATION-SELECTOR`

For every Boolean `H,f,h_0,h_1` and every physical translation pair `u,v`,

\[
\boxed{
\Delta_f\mathfrak D_{h_0,h_1}P_H(u,v)
=-\frac12\,\mathbb E_y\!
\left[
Q_H
(1-Q_{h_0})(1-Q_{h_1})(1-Q_f)
\right].
}
\tag{2.1}
\]

Equivalently,

\[
\boxed{
\Delta_f\mathfrak D_{h_0,h_1}P_H(u,v)
=-4\,\mathbb E_y\!
\left[
Q_H\,
\mathbf 1_{\{Q_{h_0}=Q_{h_1}=Q_f=-1\}}
\right].
}
\tag{2.2}
\]

Consequently

\[
\boxed{
\left|\Delta_f\mathfrak D_{h_0,h_1}P_H(u,v)\right|
\le 4\Pr_y[Q_{h_0}=Q_{h_1}=Q_f=-1]
\le4\Pr_y[Q_{h_0}=Q_{h_1}=-1].
}
\tag{2.3}
\]

### Proof

Apply `Delta_f=I-T_f` to (1.6). Since plaquette signs multiply under phase multiplication,

\[
Q_{Hf}=Q_HQ_f.
\]

Therefore

\[
\begin{aligned}
\Delta_f\mathfrak D P_H
&=-\frac12\mathbb E Q_H(1-Q_{h_0})(1-Q_{h_1})\\
&\quad+\frac12\mathbb E Q_HQ_f(1-Q_{h_0})(1-Q_{h_1})\\
&=-\frac12\mathbb E Q_H(1-Q_{h_0})(1-Q_{h_1})(1-Q_f),
\end{aligned}
\]

which is (2.1). Each factor `1-Q` is either zero or two, giving (2.2), then (2.3). \(\square\)

### Structural meaning

The real phase switch does **not** enlarge the support of the authentic clone-pair current. It only filters the already-paid simultaneous-slice-frustration event. The background orientation `Q_H` remains signed inside the event until the last estimate.

This is the physical counterpart of the source operator in (1.7). In particular, if `f` is affine then `Q_f\equiv1`, so

\[
\boxed{\Delta_f\mathfrak D_{h_0,h_1}P_H\equiv0.}
\tag{2.4}
\]

This exactly matches the previously proved affine-character gauge invariance of q-flip frustration.

---

## 3. PROVED — phase-switched clone-pair double resolvent

Let `g=1-2 1_A` be an authentic one-subcube parent of codimension `c>=2`, and let `h_0,h_1` be its two dummy slices. Let `U_s,V_t` be the same independent product-noise translations used by fleet01, with each enlarged-cube coordinate present independently with probabilities `s,t in [0,1/2]`.

### Theorem 3.1 — `P03-B16-TRIPLE-PHASE-DOUBLE-RESOLVENT`

For every Boolean background `H` and every Boolean phase `f`,

\[
\boxed{
\mathbb E_{U_s,V_t}
\left|
\Delta_f\mathfrak D_{h_0,h_1}P_H(U_s,V_t)
\right|
\le 8st(1-st)J(g).
}
\tag{3.1}
\]

Hence

\[
\boxed{
\int_0^{1/2}\!\int_0^{1/2}
\frac{
\mathbb E\left|\Delta_f\mathfrak D_{h_0,h_1}P_H(U_s,V_t)\right|
}{st}\,ds\,dt
\le\frac{15}{8}J(g).
}
\tag{3.2}
\]

### Proof

By (2.3), the integrand is bounded by four times the simultaneous clone-slice frustration probability. Fleet01's exact geometry gives (0.1), so

\[
\mathbb E|\Delta_f\mathfrak D P_H|
\le4\cdot2st(1-st)J(g),
\]

which is (3.1). Integrating,

\[
8\int_0^{1/2}\!\int_0^{1/2}(1-st)\,ds\,dt
=8\left(\frac14-\frac1{64}\right)
=\frac{15}{8}.
\]

This proves (3.2). \(\square\)

### What this avoids

The proof never reconstructs a scalar parent charge through the small plaquette amplitude `2^(2-c)`. Thus the fleet02 codimension-normalization obstruction does not occur. The correct order is exactly the one required by that handoff:

\[
\boxed{
\text{signed source}
\to
\Delta_{h_0}\Delta_{h_1}\Delta_f
\to
\text{triple-frustration physical event}
\to
\text{double resolvent payment}.
}
\tag{3.3}
\]

The extra phase switch costs at most a factor two relative to the already proved pure clone-pair event estimate; it does not create an ambient-number-of-generators or codimension factor.

---

## 4. Conditional compiler consequence — exact remaining map stated honestly

Let `mu_j>=0` denote the authentic already-signed central parent masses obtained only **after** same-syndrome R32 cancellation, with

\[
\sum_j\mu_jJ(g_j)\le E_{\rm cen}.
\tag{4.1}
\]

Theorem 3.1 supplies the following no-reuse sink criterion.

If the still-missing source-to-physical interpolation maps each genuine precompression source atom

\[
\Delta_{h_{j,0}}\Delta_{h_{j,1}}\Delta_f\Psi_s
\]

into the matching physical operator

\[
\Delta_f\mathfrak D_{h_{j,0},h_{j,1}}P_H
\]

with its authentic positive post-cancellation weight and without separating the terminal mixed difference, then the plaquette component of that transported bank obeys

\[
\boxed{
\mathcal T_{\rm cen}^{\rm triple/plaq}
\le\frac{15}{8}\sum_j\mu_jJ(g_j)
\le\frac{15}{8}E_{\rm cen}.
}
\tag{4.2}
\]

Equation (4.2) is **conditional on that interpolation**. This run does not claim that the dual-code Borel source has already been identified with the physical plaquette functional at every live Borel time.

What is proved is the hard local fact needed by such an interpolation: once the authentic three-phase operator lands on a physical clone-pair plaquette, the actual Boolean phase switch remains inside one dimension-free simultaneous-frustration event. No unsigned support replacement or scalar parent inversion is necessary.

---

## 5. Terminal term and ledger discipline

The live Ward field is

\[
\mathcal P_{uv}
=\kappa_{g_S}(g_u,g_v)+\Delta_{uv}R_d(g_S).
\tag{5.1}
\]

Theorems 2.1–3.1 concern the **plaquette-frustration component**. They do not prove an analogous event representation for

\[
\Delta_f\Delta_{h_0}\Delta_{h_1}\Delta_{uv}R_d.
\]

Therefore the terminal mixed difference remains inside the signed compiler object and is **not** split by triangle inequality, paid again, or declared harmless. The existing terminal-band theorem remains a net signed endpoint theorem. R16 moment refunds and negative entropy credits are likewise untouched.

This is important because the generic full-line endpoint identity does not control a finite live Borel window, and termwise absolute values before the distance-four cancellation can diverge. Both shortcuts remain killed.

---

## 6. Scope obstruction retained

For an arbitrary phase `f` on the enlarged cube, the codimension-one parent obstruction survives the new operator. Take a codimension-one parent, `H=1`, choose the old constrained direction and dummy direction as `u,v`, and take `f=h_0`. Then

\[
\left|\Delta_f\mathfrak D_{h_0,h_1}P_1(u,v)\right|=4,
\qquad J(g)=0.
\tag{6.1}
\]

So Theorem 3.1 cannot be extended to arbitrary codimension-one parent phases using only `J(g)`. This is a generic physical counterexample, **not** an FEI counterexample. The authentic ordered-min noncharacter q-flip parents consumed here have codimension at least two, so it does not invalidate the intended application. Moreover, the real Boolean `f` in the compiler is lifted from the old cube, not an arbitrary dummy-dependent phase; no stronger authentic codimension-one claim is made here.

---

## 7. Exact falsification checks

`check_b16_triple_frustration.py` uses only the Python standard library and exact `Fraction` arithmetic. It was compiled and executed in this run. It verifies:

- **11,440** exact mixed-difference identities (2.1) across deterministic and exhaustive small-cube samples;
- **1,200** exact triple-event support/absolute-value inequalities (2.3);
- **1,280** exact rational product-noise inequalities (3.1) on the grid `{1/8,1/4,3/8,1/2}^2` for random signed backgrounds/phases at codimension two;
- **1,024** exact affine-phase annihilation checks (2.4);
- exact integrated envelope `15/8`;
- the generic codimension-one obstruction `4` versus parent folded influence `0`.

The largest directly tested ratio in the product-noise inequality was

\[
\frac{313}{384}=0.8151041666\ldots
\]

at `s=t=1/8` in the sampled codimension-two family. This is falsification evidence, not a sharpness claim for (3.1).

---

## 8. Exact remaining implication / next recipient

The source and sink now carry the **same three commuting phase differences**. The remaining interface-C implication is narrower:

> Construct the source-exact signed/PSD interpolation from the live dual-code triple curvature `Delta_h0 Delta_h1 Delta_f Psi_s` (with the retained `C0-Dd` terminal subtraction) to the physical triple-frustration/ordered-flag sink, through the finite Borel window, without replacing the terminal mixed difference by an absolute value.

The next useful attack is to apply the fleet03 finite-window cosine-integral kernel **after** the local triple difference and ask whether the resulting signed kernel is conditionally positive on the ordered physical flag. If that fails, preserve an authentic Boolean counterpacket identifying the component not represented by the triple-frustration sink. Do not revert to the killed scalar-parent plaquette inversion, unsigned support-only, generic endpoint-`L2`, or positive-part routes.

**Full FEI remains OPEN / NOT PROVED.**
