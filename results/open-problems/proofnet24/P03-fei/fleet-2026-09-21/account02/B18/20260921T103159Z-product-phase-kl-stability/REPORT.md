TASK: B18 ACCOUNT: account02 RUN: 2026-09-21T10:31:59.209473+00:00 — product-phase total-correlation stability and universal obstruction integration

# Status

**Full uniform-cube FEI: OPEN / NOT PROVED.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** No authenticated mathematical/cognitive brain retrieval or receiver-context use occurred in this derivation.  
**Role:** FEI proof integration.  
**Source frontier:** this report was derived from fresh `master` state through the current 21 September FEI continuations, including the product-spectrum classification, all-block critical selector compiler, erasure/signed-overlap critical-core reductions, packet free-energy/KL route, signed transport/plaquette route, and signed diagonal shared-variable comparison. None of their hypotheses is removed here.

The main new result is a quantitative stability theorem for the exact product-spectrum endpoint. It converts Booleanity of the Fourier *sign phase* into a lower bound on the total correlation of the spectral sample. This does not close FEI, because the bound is Hellinger-scale rather than the KL scale needed in the worst rare-coordinate regime. It does, however, isolate the remaining obstruction more sharply as a **KL-scale curl-free biased phase-discrepancy inequality**.

## 1. Starting identity: FEI defect as product-marginal excess minus total correlation

Let `f:{-1,1}^n->{-1,1}` be Boolean, with normalized Walsh coefficients

\[
a_S=\widehat f(S),\qquad \mu(S)=a_S^2.
\]

Let

\[
p_i=\Pr_{S\sim\mu}[i\in S]=\operatorname{Inf}_i(f),
\]

and let `Q` be the product law with the same marginals,

\[
Q(S)=\prod_{i\in S}p_i\prod_{i\notin S}(1-p_i).
\]

The product-spectrum continuation records the exact total-correlation identity

\[
\operatorname{TC}(\mu)
:=D_{\rm KL,2}(\mu\|Q)
=\sum_i h_2(p_i)-H(f).
\tag{1}
\]

Hence for every candidate FEI coefficient `C`,

\[
\boxed{
H(f)-CI(f)
=\sum_i\bigl(h_2(p_i)-Cp_i\bigr)-\operatorname{TC}(\mu).
}
\tag{2}
\]

Thus the exact universal job in this coordinate system is to force enough dependence in a Boolean spectral law to pay the positive product-marginal entropy excess.

The exact-product endpoint is already classified: if `TC=0`, every nondegenerate marginal is `1/2` and the function is, after a character factor, bent on the half-marginal coordinates. That gives `H/I<=2`. The missing step is quantitative stability away from that endpoint.

## 2. PROVED: Boolean product-phase autocorrelation forces total correlation

For every Fourier label choose a sign `eps_S in {+1,-1}` with

\[
\varepsilon_S=\operatorname{sgn}(a_S)
\quad\text{whenever }a_S\ne0,
\]

and choose it arbitrarily when `a_S=0`. Define the **product-magnitude phase surrogate**

\[
b_S=\varepsilon_S\sqrt{Q(S)}.
\tag{3}
\]

For `U subseteq [n]`, let `T_U` be xor translation on coefficient vectors,

\[
(T_Ux)_S=x_{S\triangle U},
\]

and define

\[
R_U:=\langle b,T_Ub\rangle
=\sum_S b_Sb_{S\triangle U}.
\tag{4}
\]

Finally set

\[
t:=\|b-a\|_2^2
=\sum_S\bigl(\sqrt{\mu(S)}-\sqrt{Q(S)}\bigr)^2.
\tag{5}
\]

This is twice the squared Hellinger distance under the convention `Hellinger^2=1-affinity`.

### Theorem B18-PRODUCT-PHASE-STABILITY-01

For every Boolean `f`,

\[
\boxed{
\sum_{U\ne\varnothing} (|R_U|-t)_+^2\le4t.
}
\tag{6}
\]

Consequently, if `Phi(R)` is the unique nonnegative solution `tau` of

\[
\sum_{U\ne\varnothing} (|R_U|-\tau)_+^2=4\tau
\tag{7}
\]

(with `Phi=0` when all off-zero `R_U` vanish), then

\[
\boxed{
t\ge\Phi(R),\qquad
\operatorname{TC}(\mu)\ge\frac{\Phi(R)}{\ln2}.}
\tag{8}
\]

Therefore

\[
\boxed{
H(f)-CI(f)
\le
\sum_i(h_2(p_i)-Cp_i)-\frac{\Phi(R)}{\ln2}.
}
\tag{9}
\]

In particular, FEI with coefficient `C` holds for every Boolean function satisfying

\[
\Phi(R)\ge
(\ln2)\sum_i\bigl(h_2(p_i)-Cp_i\bigr).
\tag{10}
\]

### Proof

Booleanity gives `f^2=1`. In Fourier variables this is the exact convolution identity

\[
\sum_S a_Sa_{S\triangle W}=\mathbf1_{\{W=\varnothing\}}.
\tag{11}
\]

Therefore all xor translates of `a` form an orthonormal basis of the `2^n`-dimensional coefficient space:

\[
\langle T_Ua,T_Va\rangle
=\sum_Sa_{S\triangle U}a_{S\triangle V}
=\mathbf1_{\{U=V\}}.
\tag{12}
\]

Put `e=b-a`, so `||e||_2^2=t`. For every nonempty `U`, (11) gives

\[
\begin{aligned}
R_U
&=\langle a+e,T_U(a+e)\rangle\\
&=2\langle e,T_Ua\rangle+\langle e,T_Ue\rangle.
\end{aligned}
\tag{13}
\]

Write

\[
L_U=\langle e,T_Ua\rangle,
\qquad Q_U=\langle e,T_Ue\rangle.
\]

By the orthonormal basis (12), Parseval/Bessel gives

\[
\sum_U L_U^2=t,
\tag{14}
\]

while Cauchy--Schwarz gives

\[
|Q_U|\le t.
\tag{15}
\]

Hence for every nonempty `U`,

\[
(|R_U|-t)_+\le2|L_U|.
\]

Squaring and summing, then discarding the `U=empty` term in (14), proves (6).

The left side of

\[
F(\tau)=\sum_{U\ne\varnothing}(|R_U|-\tau)_+^2-4\tau
\]

is continuous and strictly decreasing in `tau` unless all `R_U=0`; it is nonnegative at `0` and negative at `max_U|R_U|`. Thus (7) has the stated unique root. Inequality (6) says `F(t)<=0`, so monotonicity gives `t>=Phi(R)`.

It remains to compare `t` with KL. Let

\[
A=\sum_S\sqrt{\mu(S)Q(S)}.
\]

Because the signs in `b` agree with those of `a` on the support of `mu`,

\[
t=2-2A.
\tag{16}
\]

Monotonicity of Renyi divergence at order `1/2` gives, in natural-log units,

\[
D_{\rm KL}(\mu\|Q)\ge -2\ln A.
\]

Since `-ln A >= 1-A`,

\[
D_{\rm KL}(\mu\|Q)\ge2(1-A)=t.
\tag{17}
\]

Dividing by `ln 2` gives `TC>=t/ln2>=Phi/ln2`. Substituting into (2) proves (9)--(10). QED.

### Interpretation

An arbitrary product random set can have many tiny independent marginals and huge entropy per expected size. A Boolean Fourier spectrum cannot simply choose arbitrary signs on those product magnitudes: Booleanity forces its true signed coefficient vector to have *zero off-origin xor autocorrelation*. If the product-magnitude surrogate carrying the same signs has substantial off-origin autocorrelation, then the true spectral law must move a definite Hellinger/KL distance away from the product law. The exact-product classification is the endpoint `t=TC=0`; Theorem 01 is a quantitative stability statement around it.

## 3. PROVED: a phase-free singleton corollary

The theorem above uses the actual Fourier sign phase. For singleton shifts one can obtain an explicit lower bound from the product marginals alone whenever the residual product law has a dominant atom.

Fix coordinate `i`. For `T subseteq[n]\{i}`, define

\[
d_i(T)=\varepsilon_T\varepsilon_{T\cup\{i\}}\in\{\pm1\}.
\]

Pairing the two labels in (4) gives the exact formula

\[
\boxed{
R_{\{i\}}
=2\sqrt{p_i(1-p_i)}\,
\mathbb E_{T\sim Q_{-i}}d_i(T).
}
\tag{18}
\]

Let

\[
\operatorname{disc}(Q_{-i})
:=\min_{d:\,2^{[n]\setminus\{i\}}\to\{\pm1\}}
|\mathbb E_{Q_{-i}}d|
=2\min_A|Q_{-i}(A)-1/2|.
\tag{19}
\]

Then

\[
|R_{\{i\}}|
\ge2\sqrt{p_i(1-p_i)}\operatorname{disc}(Q_{-i}).
\tag{20}
\]

If

\[
M_i:=\max_TQ_{-i}(T)>1/2,
\]

then any subset either contains the dominant atom or omits it, so

\[
\operatorname{disc}(Q_{-i})\ge2M_i-1.
\tag{21}
\]

Also, directly from `R_i=<b,T_ib>-<a,T_ia>` and `||a||=||b||=1`,

\[
|R_i|\le2\|b-a\|_2=2\sqrt t.
\tag{22}
\]

Combining (17), (20)--(22),

\[
\boxed{
\operatorname{TC}(\mu)
\ge
\frac{p_i(1-p_i)\operatorname{disc}(Q_{-i})^2}{\ln2}
\ge
\frac{p_i(1-p_i)(2M_i-1)^2}{\ln2}
}
\tag{23}
\]

whenever `M_i>1/2` for the last inequality.

This is a genuine universal lower bound but not a universal FEI closure: in diffuse residual product measures `M_i<=1/2` it becomes vacuous.

## 4. The multi-coordinate Boolean compatibility that remains unused

The singleton signs `d_i` cannot be selected independently. For every residual label `S` and distinct `i,j`, they obey the exact curl-free identity

\[
\boxed{
d_i(S)d_j(S\triangle\{i\})
=d_j(S)d_i(S\triangle\{j\}),}
\tag{24}
\]

because both sides equal

\[
\varepsilon_S\varepsilon_{S\triangle\{i,j\}}.
\]

This is the new universal obstruction singled out by the integration:

> **KL-scale curl-free biased phase discrepancy.** A putative high-`H/I` Boolean spectral law must have enough positive product-marginal entropy excess to threaten (2), while its single global Fourier sign phase simultaneously makes the product-magnitude xor correlations small enough to evade Theorem 01. Those derivative signs must satisfy the exact curl-free compatibility (24) across every plaquette.

This is a strictly more constrained problem than balancing each biased product law separately. The independent one-coordinate moment relaxation from the signed-overlap critical-core route already fails; (24) identifies the missing simultaneous compatibility.

At the numerical Hod lower-bound coefficient `C=6.4547837...`, the scalar function `h_2(p)-Cp` is positive only below approximately

\[
p_\star=0.0305152.
\]

Therefore any counterexample at that coefficient would need a net positive contribution from genuinely rare membership coordinates while its curl-free phase hides the corresponding product-law correlations.

## 5. Integration with the all-block critical core

The current block-selector compiler proves that if `f` violates FEI(C), a physical restriction descendant `g` can be chosen with `r(g)=H(g)/I(g)>C` and, for every nonempty proper physical block `A`,

\[
B_A(g)>\frac C2 I_A(g).
\tag{25}
\]

The coordinate critical-core route further forces low individual influences at sufficiently large `C`, large erasure payment, signed positive/negative Fourier overlap, and all-shift orthogonality. Theorem 01 applies to the **same Boolean function `g`** and adds a product-marginal dependence requirement. Consequently a universal FEI counterexample can be localized to one function satisfying all of the following simultaneously:

1. `H(g)/I(g)>C`;
2. every proper physical block is erasure-heavy as in (25);
3. the product-marginal excess in (2) exceeds `TC(mu_g)`;
4. the Fourier sign phase is curl-free as in (24);
5. its product-magnitude autocorrelation functional has `Phi(R) < (ln2) sum_i(h_2(p_i)-Cp_i)`; otherwise (10) would already rule it out.

This package is the exact integrated obstruction. No lattice, surjectivity, read-once, polynomial-core, or structured-class hypothesis has been removed.

## 6. Dead route: why this stability theorem is not full FEI

A tempting but false inference would be: “exact product spectra are rigid, and Theorem 01 is a quantitative stability theorem, therefore FEI follows.” It does not.

The reason is scale. `t=||sqrt(mu)-sqrt(Q)||_2^2<=2`, so the Hellinger payment in (17) is bounded by a constant even though `TC=D_KL,2(mu||Q)` and the product-marginal entropy excess can grow with dimension. In the dangerous regime of many tiny `p_i`, a successful universal argument must recover a **KL-scale** payment, not merely a Hellinger-scale separation.

There is also no dimension-free rescue from the arithmetic lemma used in the exact-product classification. There the ratios `p_i/(1-p_i)` are simultaneously dyadic and rational squares, forcing an exact endpoint `p_i=1/2`. Quantitatively, however, rational squares are dense as denominators grow; exact arithmetic rigidity does not itself provide a uniform separation from small nonzero marginals.

Thus the following proposed lemma is **REFUTED AS A PROOF STRATEGY / UNSUPPORTED:** “a dimension-free Hellinger gap from every dangerous product spectral law is sufficient to prove full FEI.” The punctured-subcube packet example independently reinforces the same warning: a raw dimension-growing normalizer can be cancelled by an equally large negative KL credit, so the universal proof must preserve KL-scale information rather than collapse it to an unweighted distance.

## 7. Nonoverlapping ownership after this integration

To avoid a new shared bottleneck, the current components separate naturally:

- **B14:** restriction-critical and erasure-heavy core; signed overlap and all-shift orthogonality.
- **B15:** packet arithmetic/free energy; preserve the negative KL credit and develop mass-aware packet partitions.
- **B16:** signed transport / quotient plaquette payment; baseline-cancelled Householder profile/frustration bounds.
- **B17:** shared-variable diagonal identification; collision and sign-skew telescoping.
- **B18 (this report):** total-correlation/product-phase stability and synthesis of the exact universal obstruction. The next B18 step should attack (24) at KL scale, not duplicate B14/B15/B16/B17 checks.

A concrete next lemma is to prove a tensorizing biased log-Sobolev or relative-entropy inequality for curl-free sign derivatives `d_i` that lower-bounds

\[
D_{\rm KL,2}(\mu\|Q)
\]

by the rare-coordinate excess

\[
\sum_i[h_2(p_i)-Cp_i]_+
\]

using the Boolean convolution constraints. A successful inequality of coefficient one would close FEI(C) directly through (2). A counterexample to that precise inequality should expose what additional packet/erasure resource must be retained.

## 8. Exact claim ledger

### PROVED

1. `B18-PRODUCT-PHASE-STABILITY-01`: the thresholded off-origin product-phase autocorrelation inequality (6), the root bound `t>=Phi(R)`, and `TC>=Phi(R)/ln2`.
2. The FEI-defect consequence (9)--(10).
3. The phase-free singleton discrepancy/dominant-atom bound (23).
4. The curl-free derivative-phase identity (24).

### CONDITIONAL

1. Full FEI(C) follows for any class on which `Phi(R) >= ln(2) sum_i(h_2(p_i)-Cp_i)` universally.
2. More generally, a KL-scale curl-free phase-discrepancy inequality paying the positive part of the product-marginal excess would close the full conjecture through (2).

### OPEN

1. A dimension-independent KL-scale lower bound strong enough for all Boolean functions.
2. Whether the Hod lower-bound constant `beta(1/2)` is the sharp full-FEI constant.
3. Full uniform-cube FEI.

### REFUTED / PRESERVED DEAD ROUTES

1. Hellinger/autocorrelation stability alone is not a complete FEI proof strategy because it is bounded-scale while the required KL payment can grow with dimension.
2. Exact rational-square rigidity of product spectra does not by itself yield a uniform quantitative gap away from the exact endpoint.
3. All previously recorded counterexamples to arbitrary-coordinate payment, raw packet-normalizer bounds, short T-joins, and monotonicity under variable identification remain in force.

## 9. Literature / priority status

The current literature still treats unrestricted FEI as open. Potapov (arXiv:2609.21563, 18 September 2026) proves FEI for plateaued functions and partially bent functions, not universally. González--MacManus--Pereyra (arXiv:2606.00246) develop the restriction/stopping-tree route and state a conditional local inequality whose universal validity would imply FEI. Han's 2025 Combinatorica bound retains the coordinate profile term `sum_i Inf_i log(1/Inf_i)`. The classical O'Donnell--Tan composition theorem applies to disjoint-variable composition/read-once settings. I did not find the exact product-phase autocorrelation stability theorem above in a bounded current search, but a search miss is not evidence of novelty. **Priority: UNVERIFIED.**

## 10. Sanity check scope

As a non-proof self-check only, exhaustive Boolean truth tables for `n<=3` and sampled/small exact constructions were used to test the inequalities `t<=ln(2) TC` and `Phi(R)<=t`; no violation was observed. The universal claims in Sections 2--4 are analytic and do not depend on finite verification.
