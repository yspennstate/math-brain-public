# B17 — exact Boolean barrier to higher even-moment universal repairs

**Run:** `20260922T090815Z-B17-fei-r11`  
**Classification:** `CANDIDATE_REFUTED / AUXILIARY_ONLY / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Current target and mechanism change

The live owner target is the all-gate inequality.  For a symmetric potential `Gamma`, write

\[
D_\Gamma(G;p)=\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
  \bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
  -\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\]

The normalized quadratic gate margin is

\[
c_G(p)=-{D_{\Gamma_0}(G;p)\over I(G;p)/4-p_{\rm out}(1-p_{\rm out})}.
\]

This run does **not** repeat the previous finite dyadic bias slices.  It attacks a proposed analytic proof mechanism for the same all-gate target: extend the known universally safe quadratic/quartic repair directions to a hierarchy of even moments.

The named compatible cross-account result consumed is fleet04/B17,

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B17/20260922T071535Z-quartic-universal-repair/REPORT.md`.

That report proves for

\[
\eta_4(u)=u(1-u)(1-2u(1-u))={1-(1-2u)^4\over8}
\]

that every Boolean gate and every product bias satisfy

\[
\sum_i \alpha_i\eta_4(p_i)-\eta_4(p_{\rm out})\ge0,
\qquad
\alpha_i={\operatorname{It}_i(G;p)\over V_{p_i}},
\]

so adding a positive multiple of `eta_4` can only improve every gate defect.  The ordinary quadratic direction

\[
\eta_2(u)=u(1-u)={1-(1-2u)^2\over4}
\]

has the analogous property by Poincare.  A natural possible route to a richer globally safe potential cone is therefore the pure even-moment family

\[
\boxed{\eta_r(u)={1-(1-2u)^r\over 2r}},\qquad r=2,4,6,8,\ldots .
\tag{0.1}
\]

The result below kills that extension exactly from degree six onward on one four-input admissible Boolean gate.

## 1. Exact Boolean witness

Take one selector bit `s` with bias

\[
\Pr[s=1]={3\over8}
\]

and three independent unbiased data bits `y=(y_1,y_2,y_3)`.  Define a `+-1` child gate `h` by

\[
h(y)=+1\quad\Longleftrightarrow\quad
 y\in\{000,001,010\},
\]

and `h(y)=-1` on the other five data inputs.  Define the four-input gate

\[
G(s,y)=\begin{cases}
-1,&s=0,\\
h(y),&s=1.
\end{cases}
\tag{1.1}
\]

This is a genuine finite Boolean truth table under a product bias, not a non-Boolean spectral relaxation.

The child mean and coordinate influences are exact:

\[
\mathbb Eh=-{1\over4},
\qquad
(\operatorname{Inf}_{y_1}h,\operatorname{Inf}_{y_2}h,\operatorname{Inf}_{y_3}h)
=\left({3\over4},{1\over4},{1\over4}\right).
\tag{1.2}
\]

The parent mean is

\[
\mu={5\over8}(-1)+{3\over8}\left(-{1\over4}\right)
=-{23\over32},
\]

so in the source true-probability convention

\[
\boxed{p_{\rm out}={55\over64}.}
\tag{1.3}
\]

The pivotal probabilities `alpha_i=It_i/V_{p_i}` are

\[
\boxed{
\alpha_s={3\over8},\qquad
(\alpha_{y_1},\alpha_{y_2},\alpha_{y_3})
=\left({9\over32},{3\over32},{3\over32}\right).
}
\tag{1.4}
\]

Indeed the selector is pivotal exactly on the three positive rows of `h`, while a data coordinate can matter only on the active selector branch, so its pivotal probability is `(3/8) Inf_i(h)`.

## 2. Exact defect of every pure even-moment repair

For an even `r`, define the change in the all-gate defect caused by adding one unit of `eta_r`:

\[
\Delta_r(G;p)
:=\sum_i\alpha_i\eta_r(p_i)-\eta_r(p_{\rm out}).
\tag{2.1}
\]

For the witness (1.1), all three data biases are `1/2`, the selector bias is `3/8`, and `p_out=55/64`.  Substitution into (0.1) gives the closed form

\[
\boxed{
2r\,\Delta_r
=g_r:=\left({23\over32}\right)^r-{5\over32}-{3\over8}\,4^{-r}.
}
\tag{2.2}
\]

The first exact values are

\[
\Delta_2={345\over4096}=0.084228515625>0,
\]

\[
\Delta_4={114465\over8388608}
=0.0136452913284301758\ldots>0,
\]

but

\[
\boxed{
\Delta_6=-{6611525\over4294967296}
=-0.0015393656212836504\ldots<0.
}
\tag{2.3}
\]

Further values are

\[
\Delta_8=-{93493998015\over17592186044416}
=-0.0053145184901381981\ldots,
\]

\[
\Delta_{10}=-{26899150376739\over4503599627370496}
=-0.0059728112182220183\ldots,
\]

\[
\Delta_{12}=-{52743128810867765\over9223372036854775808}
=-0.0057184214840425634\ldots .
\]

Thus `eta_6` already makes this exact Boolean gate *worse*.

## 3. Analytic tail: every even degree at least six fails

The failure is not a low-degree accident.  From (2.2),

\[
\begin{aligned}
g_{r+2}-g_r
&=\left({23\over32}\right)^r
\left[\left({23\over32}\right)^2-1\right]
-{3\over8}4^{-r}\left(1-4^{-2}\right)\\
&=-{495\over1024}\left({23\over32}\right)^r
+{45\over128}4^{-r}.
\end{aligned}
\tag{3.1}
\]

This is negative exactly when

\[
\left({23\over8}\right)^r>{8\over11},
\]

which in particular holds for every `r>=0`.  Hence `g_r` is strictly decreasing along the even integers.  Since

\[
g_6=-{19834575\over1073741824}<0,
\]

we obtain:

### Theorem 3.1
For the admissible Boolean gate (1.1),

\[
\boxed{
\Delta_r<0\qquad\text{for every even }r\ge6.
}
\tag{3.2}
\]

Therefore no `eta_r`, even `r>=6`, is a universally gate-safe positive repair direction.

This sharply separates the peer's quartic theorem from the naive higher-moment hierarchy: degree four is not merely the first member of an automatic sequence.

## 4. A necessary face for mixed moment repairs

The same witness gives a quantitative constraint on any nonnegative mixed repair

\[
\eta=a\eta_2+b\eta_4+c\eta_6,
\qquad a,b,c\ge0.
\]

Gate safety on this single Boolean source requires

\[
{345\over4096}a+{114465\over8388608}b
-{6611525\over4294967296}c\ge0.
\]

Clearing denominators and the common factor gives

\[
\boxed{
72,351,744\,a+11,721,216\,b\ge1,322,305\,c.
}
\tag{4.1}
\]

Thus a unit `eta_6` component requires at least

\[
\boxed{{b\over c}\ge {1322305\over11721216}
=0.1128129538778229\ldots}
\tag{4.2}
\]

if compensated only by the quartic direction, or

\[
\boxed{{a\over c}\ge {1322305\over72351744}
=0.01827606256457343\ldots}
\tag{4.3}
\]

if compensated only by the quadratic direction.

These are only necessary constraints from one gate, but they define an exact admissibility face that a future finite-dimensional potential optimization can retain.

## 5. Refutation attempt and scope

The attempted stronger bridge was:

> Every positive even-moment direction `eta_r` in (0.1) is universally gate-safe, so the all-gate potential can be repaired inside the positive cone generated by the complete even-moment hierarchy.

**REFUTED.**  The exact Boolean gate (1.1) violates that bridge for every even `r>=6`.

What this does **not** show:

- it does not give a Boolean counterexample to FEI;
- it does not show a gate whose owner-normalized `c_G` exceeds the AND extremum;
- it does not refute the peer's proven universal quadratic or quartic directions;
- it does not rule out mixed higher-degree repairs satisfying constraints such as (4.1), or a non-polynomial potential.

The full FEI target therefore remains OPEN.

## 6. Old/new missing implication and next attack

**Exact candidate version attacked.** `EVEN-MOMENT-UNIVERSAL-REPAIR-v1`: the positive cone generated independently by `eta_r=[1-(1-2u)^r]/(2r)` for every even `r` consists of universally gate-safe directions.

**Old missing implication.** Find a sufficiently rich universal repair family that preserves every already-valid gate inequality while correcting the known prime-gate obstructions, as required by the all-gate formulation.

**New result.** The independent higher-even-moment extension is false already at arity four; all pure degrees `r>=6` point in the wrong direction on one exact admissible product-biased gate.  The safe quadratic/quartic directions survive.

**Replacement obligation.** Return directly to the owner's normalized-margin problem.  The next adversarial search should use a genuinely composition-prime arity-five gate at non-dyadic/asymmetric biases and compare its `c_G` to the AND floor; if a repair basis is used, enforce (4.1) rather than assuming higher moment monotonicity.  Another dyadic balanced slice or another pure `eta_r` test would be redundant.

**Consumed peer artifact:** fleet04/B17 `20260922T071535Z-quartic-universal-repair/REPORT.md`, applied to the claim that quartic gate safety extends to higher even moments.

**Primary next recipient:** `fleet04/B17` for repair-cone design.  
**Secondary next recipient:** `fleet03/B18` for all-gate integration.

**Implication to full FEI:** one attractive universal-potential extension is rigorously removed; no target-level theorem is closed.  **Full FEI remains OPEN / NOT PROVED.**
