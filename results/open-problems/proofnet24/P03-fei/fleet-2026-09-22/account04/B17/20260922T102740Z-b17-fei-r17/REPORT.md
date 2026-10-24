# account04/B17 — exact suspension transport from Path C surplus to Path B dependence KL

**Run:** `20260922T102740Z-b17-fei-r17`  
**Classification:** `ESSENTIAL_STEP_APPLIED / CROSS_PATH_DEFICIT_TRANSPORT / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Current owner assignment and source scope

The active owner programme is `FEI-ALL-TEAM-20260922T095941Z`, control revision `2026-09-22.3`. It supersedes the older Interface-D/B15-only prompt. The current `account04/B17` assignment is **Cross-path deficit transport**: relate a Path C critical-core entropy surplus to a canonical Path B KL/dependence deficit in original coordinates, preserving the Fourier constant mode and every reference mismatch.

The exact sources used are:

1. **IPROJ:** account02/B15, `20260922T0829Z-influence-iprojection-kl/REPORT.md`, source commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`. It proves the maximum-entropy nonempty occurrence I-projection and the Pythagorean split of conditional-product KL.
2. **Partner result actually applied:** account01/B17, `20260922T084426Z-signed-convolution-packet/REPORT.md`, creation commit `ecc0bd6b5505ff115efe7a1c9e5beb75b9df0087`, report blob `05944643d0ebef5a5cfe592c94fcd7851c69dfec`. Its source-valid theorem lower-bounds KL to a radial Gibbs law by simultaneously using all two-coordinate Boolean convolution equations. Its historical fixed-potential framing is not used.
3. **Path C state:** account04/B18, `20260922T091529Z-surplus-hidden-curvature/REPORT.md`, creation commit `200e3fd37fe201f78d882ba8809414d201efb829`. It uses the median-character gauge, folded influence `J`, correction `P`, and critical numerator `F=H-P`.
4. **Critical-core/gauge identity:** account02/B13, `20260921T232801Z-critical-core-tensor-tax/REPORT.md`, for `J(f)=min_T I(chi_T f)` and exact character-gauge invariance of spectral entropy.
5. **Mandatory preflight:** account03/B18, `20260922T100641Z-lowlevel-projection-barrier/REPORT.md`, commit `bff0d7b6c21485f386841c42582eb04f32705046`, which refutes fixed/low-depth labelled KL payment on recursive ternary majority.

No obsolete fixed potential, raw-`U4` shortcut, unweighted convolution `L2` payment, benchmark data, or non-Boolean relaxation is used below.

## 1. Setup in the exact folded gauge

Let `f:{-1,+1}^n->{-1,+1}` be Boolean. Choose a median character `chi_T` and put

\[
g=\chi_T f,
\qquad
p(S)=\widehat g(S)^2=\widehat f(S\triangle T)^2.
\]

Let `X~p` and

\[
q_i=\Pr(i\in X)\le\tfrac12,
\qquad
J=\sum_i q_i.
\]

Write

\[
\mathfrak j(q)=1-h_2\!\left(\frac12+\sqrt{q(1-q)}\right),
\qquad
\mathcal P=\sum_i\mathfrak j(q_i),
\qquad
\mathcal F=H(g)-\mathcal P.
\]

Character multiplication only permutes the full Fourier law, so `H(g)=H(f)`. Importantly, the atom `p(\varnothing)=\widehat g(\varnothing)^2` is retained throughout.

## 2. Main theorem — a balanced suspension converts Path C surplus to canonical Path B KL

Introduce one fresh unbiased Boolean coordinate `y` and define

\[
F(y,x)=y\,g(x).
\tag{2.1}
\]

Then `F` is balanced and its Fourier coefficients satisfy

\[
\widehat F(\{y\}\cup S)=\widehat g(S),
\qquad
\widehat F(A)=0\quad(y\notin A).
\tag{2.2}
\]

Thus the entire full spectral law `p`, **including its constant atom**, becomes a nonempty spectral law: the old constant atom is exactly the singleton atom `\{y\}`.

The coordinate-occurrence marginals of this nonempty law are

\[
r_y=1,
\qquad
r_i=q_i.
\tag{2.3}
\]

Because `r_y=1`, the maximum-entropy nonempty I-projection from IPROJ is simply the law with `y` forced present and the original coordinate-membership bits independent Bernoulli(`q_i`). Call it `Q_susp`. Hence

\[
H(Q_{\rm susp})=\sum_i h_2(q_i)
\]

and the canonical Path B dependence credit of the suspension is exactly

\[
\boxed{
K_{\rm susp}:=D_{\rm KL,2}(P_F\Vert Q_{\rm susp})
=\sum_i h_2(q_i)-H(g).
}
\tag{2.4}
\]

Define the scalar reserve

\[
B_\rho(q):=
\sum_i\bigl[h_2(q_i)-\mathfrak j(q_i)-\rho q_i\bigr].
\tag{2.5}
\]

Then substitution of (2.4) gives the exact transport identity

\[
\boxed{
\mathcal F-\rho J=B_\rho(q)-K_{\rm susp}
}
\tag{2.6}
\]

for every real `rho`.

### Consequence for a Path C critical core

If `rho=\mathcal F/J>4`, then

\[
\boxed{K_{\rm susp}=B_\rho(q)}
\tag{2.7}
\]

and at the threshold `4`,

\[
\boxed{
K_{\rm susp}
=B_4(q)-(\rho-4)J
<B_4(q).
}
\tag{2.8}
\]

So a Path C ratio-`>4` obstruction is equivalently a **shortfall of one canonical Path B dependence KL against the scalar reserve `B_4(q)`**. This is not an inequality or a relaxed proxy: it is an identity for an actual balanced Boolean suspension.

### Proof

Equation (2.2) follows from multiplying by the fresh character `y`. The I-projection statement follows because a coordinate with occurrence marginal one is deterministic; maximizing entropy subject to the remaining marginals makes the other membership bits independent. Therefore (2.4) is the maximum-entropy identity `K=H_max-H`. Finally,

\[
B_\rho(q)-K_{\rm susp}
=H(g)-\sum_i\mathfrak j(q_i)-\rho\sum_iq_i
=\mathcal F-\rho J.
\]

This proves (2.6), and (2.7)-(2.8) are immediate. `QED`.

## 3. Exact constant-mode and reference-mismatch decomposition

The suspension in Section 2 is canonical but it is useful to separate the three pieces that disappear if one first conditions away the constant Fourier atom.

Put

\[
a=p(\varnothing),\qquad v=1-a.
\]

For `v>0`, let `P^+` be `p` conditioned on `S\ne\varnothing`. Its occurrence marginals are

\[
r_i^+=q_i/v.
\]

Let `Q^+` be the exact maximum-entropy nonempty I-projection matching `r^+`, and define

\[
K_{\rm anchor}:=D_{\rm KL,2}(P^+\Vert Q^+).
\tag{3.1}
\]

Let `R_q` be the **unconditioned** independent Bernoulli product law on the original membership bits with marginals `q_i`, and let

\[
c_0=R_q(S\ne\varnothing)=1-\prod_i(1-q_i),
\qquad
R_q^+=R_q(\cdot\mid S\ne\varnothing).
\tag{3.2}
\]

Since `K_susp=D(p||R_q)`, binary KL chain rule at the empty/nonempty branch gives

\[
K_{\rm susp}
=d_2(v\Vert c_0)+vD(P^+\Vert R_q^+).
\tag{3.3}
\]

Both `Q^+` and `R_q^+` are conditional-product laws. Their log-likelihood ratio is affine in the coordinate indicators on the nonempty state space, while `P^+` and `Q^+` have the same coordinate marginals. The IPROJ Pythagorean identity therefore gives

\[
D(P^+\Vert R_q^+)
=K_{\rm anchor}+D(Q^+\Vert R_q^+).
\tag{3.4}
\]

Combining (3.3)-(3.4):

\[
\boxed{
K_{\rm susp}
=
\underbrace{d_2(v\Vert c_0)}_{\text{constant-mode / branch KL}}
+
\underbrace{vK_{\rm anchor}}_{\text{canonical nonempty dependence KL}}
+
\underbrace{vD(Q^+\Vert R_q^+)}_{\text{reference mismatch}}.
}
\tag{3.5}
\]

The natural `mu=1` IPROJ boundary is included by its singleton-law definition; the character case `J=0` is degenerate and has zero entropy. All three terms in (3.5) are nonnegative, and none is silently discarded.

Combining (2.6) and (3.5) gives the requested exact cross-path map:

\[
\boxed{
\mathcal F-\rho J
=B_\rho(q)
-d_2(v\Vert c_0)
-vK_{\rm anchor}
-vD(Q^+\Vert R_q^+).
}
\tag{3.6}
\]

Thus a Path C critical core with ratio `rho>4` can exist only if the **sum of the branch KL, canonical nonempty dependence KL, and conditional-product reference mismatch** is strictly smaller than `B_4(q)`.

## 4. Applying the newest account01/B17 signed-convolution packet theorem

This section applies the named partner result to an actual equation rather than merely citing it.

Let the suspension dimension be `d=n+1`. For `z>0` define the radial law on nonempty subsets

\[
\rho_z(A)=\frac{z^{|A|}}{(1+z)^d-1}.
\tag{4.1}
\]

The partner theorem supplies, whenever its packet quantity is positive and for any moment exponent `s>4`, a source-valid bound

\[
D_{\rm KL,2}(P_F\Vert\rho_z)
\ge L_{\rm pkt}(d,z,s),
\tag{4.2}
\]

where `L_pkt=d_*^2/ln 2` and `d_*` is the unique positive root in account01/B17 equations (2.6)-(2.9). The exact numerical shape of that theorem is not rederived here; only its proved KL lower bound is used.

Apply the IPROJ Pythagorean theorem with `Q_susp`. Because `Q_susp` has `y` forced and independent Bernoulli `q_i` on the original coordinates,

\[
D(P_F\Vert\rho_z)
=K_{\rm susp}+M_{\rm rad}(q;z),
\tag{4.3}
\]

where the reference mismatch is explicit:

\[
\boxed{
M_{\rm rad}(q;z)
=
\log_2\bigl((1+z)^d-1\bigr)
-(1+J)\log_2 z
-\sum_i h_2(q_i).
}
\tag{4.4}
\]

Therefore

\[
\boxed{
K_{\rm susp}
\ge L_{\rm pkt}(d,z,s)-M_{\rm rad}(q;z).
}
\tag{4.5}
\]

Substituting into the threshold-4 transport identity cancels the marginal entropies and gives the new Path-C usable inequality

\[
\boxed{
\mathcal F-4J
\le
\log_2\bigl((1+z)^d-1\bigr)
-(1+J)\log_2 z
-\mathcal P-4J
-L_{\rm pkt}(d,z,s).
}
\tag{4.6}
\]

Thus any region in which the right side of (4.6) is nonpositive is excluded from being a ratio-`>4` Path C critical core. This is the first direct insertion of the partner's multiequation Booleanity packet into the folded critical-core surplus while retaining the exact I-projection mismatch.

## 5. Mandatory recursive-majority preflight — the transport keeps the rare-event logarithm

Let `M_m` be depth-`m` recursive ternary majority. The source-exact formulas are

\[
N_m=3^m,
\qquad
q_i=2^{-m},
\qquad
J_m=(3/2)^m,
\qquad
H(M_m)=4(J_m-1).
\tag{5.1}
\]

The new full-suspension dependence credit is

\[
K_{\rm susp}(M_m)
=3^m h_2(2^{-m})-4(J_m-1).
\tag{5.2}
\]

Using `h_2(x)>=x log_2(1/x)`,

\[
\boxed{
K_{\rm susp}(M_m)
\ge (m-4)J_m+4.
}
\tag{5.3}
\]

So this statistic retains an order-`mJ_m` multiscale rare-event logarithm. It does **not** collapse like the refuted fixed/low-depth labelled projection.

Meanwhile its Path C threshold surplus is exactly

\[
\boxed{
\mathcal F(M_m)-4J_m
=-4-3^m\mathfrak j(2^{-m})<0.
}
\tag{5.4}
\]

Thus recursive majority does not create a false ratio-`>4` critical core under the transport. The mandatory preflight is passed analytically, not merely numerically.

## 6. Deterministic finite check

The adjacent standard-library checker exhaustively enumerates the Fourier spectra of all Boolean truth tables through four variables modulo global sign, for `32,876` noncharacter cases checked. It verifies:

- the suspension identity (2.4) and surplus transport (2.6);
- the branch/canonical/reference decomposition (3.5) whenever the nonempty IPROJ is nondegenerate;
- the radial Pythagorean mismatch identity (4.3)-(4.4);
- recursive-majority formulas through depth `12`.

It returned

```
CROSS_PATH_TRANSPORT_EXHAUSTIVE_PASS 32876
MAX_ABS_IDENTITY_ERROR 1.776e-15
RM3_MULTISCALE_PREFLIGHT_PASS 12
ALL_CHECKS_PASS
```

Checker SHA-256: `0ac398bfa01367889a7a6b52ce35a22bd18d9ef7f48606000d6acd4814ff0d04`. Clean executed output SHA-256: `097b52846f7dbc22cacfed7b42075d492a3bfd1c8cf9f636da74bb0753a0498f`. The finite sweep is a sanity check only; Sections 2-5 are analytic identities/inequalities.

## 7. What this changes, and the remaining unpaid implication

**Before this run:** Path C's folded/character-gauged surplus and Path B's nonempty dependence KL were separate currencies. Conditioning the spectral law on nonempty sets risked losing the constant Fourier atom, and changing product references risked hiding a KL mismatch.

**After this run:** the one-bit balanced suspension gives an exact Boolean bridge. The full Path C surplus is a scalar marginal reserve minus a canonical Path B dependence KL. Conditioning back to the usual nonempty anchored law decomposes that same KL exactly into the constant-mode branch KL, the canonical anchored dependence KL, and an explicit conditional-product reference mismatch. The partner's signed-convolution packet theorem then plugs into this bridge through a second exact Pythagorean identity.

**Still unpaid:** prove that the total dependence payment in (3.5), or the packet-enhanced lower bound (4.5) together with additional multiscale information, always reaches the reserve `B_4(q)` on a hypothetical ratio-`>4` critical core. Equation (5.3) shows that any successful argument can retain the logarithmic scale demanded by recursive majority, but (4.6) is not yet known nonpositive for every critical-core marginal vector.

This is therefore a genuine cross-path reduction and a new exclusion inequality, **not** a proof of full FEI.
