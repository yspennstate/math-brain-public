TASK: B13 ACCOUNT: account02 RUN: 2026-09-21T18:03:26.753511Z — derivative sign-stability defect decomposition and Palm-row transfer

MODEL: GPT-5.6 Sol (self-report)  
THINKING LEVEL: UNKNOWN; requested=maximum actually supported; configured/runtime selector not exposed  
THINKING USAGE: provider reasoning tokens/time NOT_EXPOSED  
RESEARCH EXECUTION: WITHOUT_VERIFIED_BRAIN. No authenticated brain retrieval or receiver-side brain context was consumed.

# Status

**Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**

This run follows the later direct owner order `FEI-SEVEN-TASKS-2026-09-21` and B13's assigned FEI approach 2/13: Boolean block-influence/correlation profiles and two-sided Booleanity constraints. No publication-priority claim is made.

The new result closes one precise subproblem left open by the newest B12 Palm-row handoff. B12 isolated the Boolean derivative depth defect

\[
\Delta_i=\mathbb E[|Y_i|]-\frac12\log_2\frac1{j_i}\ge0,
\]

where `j_i=Inf_i(f)` and `Y_i` is the normalized derivative's spectral Palm row, and showed that exact equality forces a constant-sign subcube derivative. It explicitly left the quantitative sign-stability step open. The present run proves an exact four-bank decomposition of `4 j_i Delta_i` that isolates sign mixing, and obtains a dimension-free transfer bound from the actual signed Palm row to the unsigned-support Palm row. This does not finish the support-stability or reverse-data-processing step.

It also reconciles B13's earlier point-gated arbitrary-residual obstruction with B12's depth programme: in that family the entire depth defect is exactly the residual Boolean influence, so the bent/signed-coherent obstruction is not a near-equality row.

# 1. Setup and normalization

Let `f:F_2^n->{-1,+1}` and fix a coordinate `i`. On the remaining `m=n-1` coordinates define

\[
g(y)=\frac{f(0,y)-f(1,y)}2\in\{-1,0,1\}.
\tag{1.1}
\]

Write

\[
j=\mathbb E g^2=\operatorname{Inf}_i(f),
\qquad
A=\{g=+1\},\quad B=\{g=-1\},\quad E=A\sqcup B,
\tag{1.2}
\]

with densities `a`, `b`, `j=a+b`. Throughout the stability statement assume

\[
0<j\le\frac12.
\tag{1.3}
\]

For a real function `u` on the `m`-cube use

\[
D_r u(x)=\frac{u(x)-u(x+e_r)}2,
\qquad
d_g=\sum_{r=1}^m\|D_rg\|_2^2.
\tag{1.4}
\]

For a set `C` let

\[
I(C)=\sum_r\Pr[1_C(x)\ne1_C(x+e_r)].
\tag{1.5}
\]

Then `4 sum_r ||D_r 1_C||_2^2=I(C)`. Let

\[
J(A,B)=\sum_r\Pr[\{x,x+e_r\}\text{ has one endpoint in }A\text{ and one in }B].
\tag{1.6}
\]

The probability in (1.6) is taken with uniform oriented `x`; this is the same normalization as (1.5).

The derivative Palm law is

\[
P_g(S)=\frac{\widehat g(S)^2}{j}
=\Pr_\mu[T\setminus\{i\}=S\mid i\in T],
\tag{1.7}
\]

and Parseval gives

\[
\mathbb E_{S\sim P_g}|S|=\frac{d_g}{j}.
\tag{1.8}
\]

Define the B12 depth defect

\[
\Delta=\frac{d_g}{j}-\frac12\log_2\frac1j.
\tag{1.9}
\]

Finally put

\[
\theta=\frac{\min(a,b)}j\in[0,1/2].
\tag{1.10}
\]

Thus `theta` is the minority-sign fraction on the sensitive fibres.

# 2. PROVED: exact four-bank decomposition of the depth defect

For a set `C` of density `c<=1/2`, define its weak edge-isoperimetric slack

\[
\operatorname{Iso}(C)=I(C)-2c\log_2\frac1c\ge0,
\tag{2.1}
\]

with `Iso(empty)=0`.

## Theorem B13-SIGN-DEFECT-01

For every derivative `g` satisfying (1.3),

\[
\boxed{
4j\Delta
=
\operatorname{Iso}(A)+\operatorname{Iso}(B)
+2J(A,B)
+2j h_2(\theta).
}
\tag{2.2}
\]

All four terms on the right are nonnegative.

### Proof

Inspect one cube edge. If the edge joins a nonzero value of `g` to zero, its contribution to `4||D_rg||_2^2` is exactly one, equal to its contribution to `I(A)+I(B)`. If it joins `+1` to `-1`, its contribution to `4||D_rg||_2^2` is four, while its contribution to `I(A)+I(B)` is two. Hence, exactly,

\[
4d_g=I(A)+I(B)+2J(A,B).
\tag{2.3}
\]

Because `a,b<=j<=1/2`, the weak cube edge-isoperimetric inequality applies separately to `A` and `B`. Also

\[
a\log_2\frac1a+b\log_2\frac1b
=j\log_2\frac1j+jh_2(\theta).
\tag{2.4}
\]

Substitute

\[
I(A)=2a\log_2(1/a)+\operatorname{Iso}(A),
\quad
I(B)=2b\log_2(1/b)+\operatorname{Iso}(B)
\]

into (2.3), use (2.4), and subtract `2j log_2(1/j)`. Since

\[
4j\Delta=4d_g-2j\log_2\frac1j,
\]

(2.2) follows. QED.

## Relation to the preceding B12 identity

B12 wrote the same total defect as

\[
4j\Delta=
\underbrace{(4d_g-I(E))}_{\text{sign slack}}
+
\underbrace{(I(E)-2j\log_2(1/j))}_{\text{support isoperimetric slack}}.
\tag{2.5}
\]

Equation (2.2) is a strict refinement of the bookkeeping in (2.5): it resolves the total defect into two separate sign-set isoperimetric slacks, actual opposite-sign adjacency, and an explicit binary sign-mixing entropy bank. No new assumption is introduced.

# 3. PROVED: dimension-free sign stability

Dropping the first three nonnegative terms from (2.2) gives

\[
\boxed{h_2(\theta)\le2\Delta.}
\tag{3.1}
\]

Since `h_2(theta)>=2 theta` for `0<=theta<=1/2`,

\[
\boxed{\theta\le\Delta.}
\tag{3.2}
\]

Choose the majority sign `sigma in {-1,+1}` on `E`. Then

\[
\|g-\sigma1_E\|_2^2=4j\theta,
\]

so

\[
\boxed{
\frac{\|g-\sigma1_E\|_2^2}{j}
=4\theta\le4\Delta.
}
\tag{3.3}
\]

This is the missing quantitative sign-stability statement in physical `L^2`: a derivative row whose mean spectral depth is within `Delta` of the sharp Boolean minimum is automatically close to constant sign on its support, without any dimension factor.

# 4. PROVED: dimension-free transfer to the spectral Palm row

Let

\[
P_E(S)=\frac{\widehat{1_E}(S)^2}{j}
\tag{4.1}
\]

be the normalized squared Fourier law of the unsigned support. The normalized physical vectors `g/sqrt(j)` and `sigma 1_E/sqrt(j)` have inner product

\[
1-2\theta.
\tag{4.2}
\]

A Walsh measurement cannot decrease classical fidelity below the squared-state overlap. Equivalently, directly by Parseval and the triangle inequality,

\[
\sum_S\sqrt{P_g(S)P_E(S)}\ge1-2\theta.
\tag{4.3}
\]

The standard fidelity--total-variation inequality then gives

\[
\boxed{
\operatorname{TV}(P_g,P_E)
\le2\sqrt{\theta(1-\theta)}
\le2\sqrt{\Delta}.
}
\tag{4.4}
\]

Every stochastic postprocessing contracts total variation. Therefore (4.4) remains valid after **every coordinate projection, random-prefix thinning, block erasure, or other fixed Markov channel** applied equally to the two row laws.

This is exactly the form needed to combine a support-stability theorem with B12's sequential/Palm programme: sign instability no longer costs an ambient-dimension factor.

## Support-proxy assembly

For any comparison set `C` of density `c>0`, let

\[
P_C(S)=\frac{\widehat{1_C}(S)^2}{c}.
\]

The normalized support states have overlap

\[
\frac{|E\cap C|/2^m}{\sqrt{jc}}.
\]

Thus, by a triangle inequality through `P_E`,

\[
\boxed{
\operatorname{TV}(P_g,P_C)
\le
2\sqrt{\theta(1-\theta)}
+
\sqrt{1-\frac{\Pr(E\cap C)^2}{jc}}.
}
\tag{4.5}
\]

In the particularly relevant equal-density case `c=j`, if

\[
\eta=\Pr(E\triangle C),
\]

then `Pr(E cap C)=j-eta/2`, and

\[
\boxed{
\operatorname{TV}(P_g,P_C)
\le
2\sqrt{\Delta}
+
\sqrt{\frac\eta j-\frac{\eta^2}{4j^2}}.
}
\tag{4.6}
\]

Therefore any quantitative cube edge-isoperimetric stability theorem that supplies `eta/j -> 0` from the support slack immediately combines with (4.6) to give a dimension-free **row-shape** approximation to the subcube Palm law. The exact constants and the subsequent information-loss payment remain to be completed; they are not claimed here.

# 5. Reconciliation with B13's point-gated arbitrary-residual obstruction

The preceding B13 derivative block-complementarity run used

\[
g(y,z)=1_{\{y=0^k\}}h(z),
\tag{5.1}
\]

where `h:F_2^d->{-1,+1}` is arbitrary. This family has identical physical sensitive-support projection law on the `z` block for every choice of `h`, yet its spectral Palm row can range from trivial to bent. That showed support-only block collisions cannot control the row.

The present defect identifies exactly where the missing information sits. Here

\[
j=2^{-k},
\]

and the conditional spectral row factors as

\[
P_g=U_{\{0,1\}^k}\otimes\mu_h.
\tag{5.2}
\]

Hence

\[
\frac{d_g}{j}=\frac k2+I(h),
\]

and therefore

\[
\boxed{\Delta=I(h).}
\tag{5.3}
\]

So the arbitrary signed residual is invisible to the physical support profile but **not** invisible to the depth defect. A constant residual has `Delta=0`; a `d`-variable bent residual has `Delta=d/2`. The large mixed-axis signed-coherence bank exhibited in the bent example is therefore automatically routed to the **large-defect regime** of B12's proposed two-regime argument.

This is useful separation: low-`Delta` rows are quantitatively almost unsigned by (3.3)--(4.4), while the known support-only counterexample with large signed residual has a correspondingly large `Delta` that can potentially pay information loss.

# 6. What this does and does not prove for full FEI

The result is universal for every Boolean derivative row with `j<=1/2`; it is not a structured-class theorem. It proves the sign half of the stable row-shape bridge requested by the newest B12 handoff.

It does **not** yet prove full FEI. Two payments remain:

1. import a quantitative support-stability estimate with constants in the exact normalization above and turn small support isoperimetric slack into a usable `eta/j` bound;
2. prove an amortized terminal-to-prefix / block-information inequality in which the large-`Delta` rows pay their own loss and the low-`Delta` rows inherit the near-subcube row shape without an alphabet-size continuity loss.

A naive use of Fannes continuity on (4.4) would reintroduce ambient dimension through `delta log |Omega|`; that is not accepted as a closure. The next step must use the actual prefix/erasure channel geometry or a source-family independent strong-data-processing estimate around the subcube row.

# 7. Executed checker

`check_sign_stability_defect.py` was executed with the Python standard library. It enumerates every Boolean function through dimension four modulo global output negation and every coordinate derivative satisfying `0<j<=1/2`.

Results:

- derivative rows: **83,192**;
- exact edge-energy identities: **83,192**;
- defect/sign-entropy identity checks: **83,192**;
- Palm-vs-support total-variation checks: **83,192**;
- total checks: **249,576**;
- maximum floating discrepancy in the logarithmic defect identity: `4.441e-16`;
- maximum TV excess over the proved bound: `0.000e+00`.

The edge identity is checked with exact rational arithmetic; only logarithm-containing identities use floating evaluation. The proof above, not the finite checker, is the mathematical basis of the result.

# 8. Coordination / next target

- **B12:** equation (2.2) resolves its open sign-stability subproblem. Equations (4.4)--(4.6) provide a dimension-free spectral-row transfer once support stability is supplied. The point-gated obstruction has `Delta=I(h)`, so it belongs to the large-defect branch rather than invalidating a low-defect stability argument.
- **B16:** the current q-flip/signed-transport work attacks signed coherence globally. Here signed derivative complexity is charged locally by the exact depth defect; no claim is made that the banks coincide.
- **B18:** its current projection/phase-packing integration can use (4.4) after any projection channel because TV contracts. No total-correlation closure is asserted.

**Next B13 target:** derive a channel-specific continuity bound for the random-prefix/erasure observable around the exact signed-subcube row whose loss is `O(Delta)` or `O(sqrt(Delta))` with no ambient-dimension multiplier, and stress-test it on one-point defects, majority derivatives, and the point-gated bent residual before attempting any universal FEI closure.
