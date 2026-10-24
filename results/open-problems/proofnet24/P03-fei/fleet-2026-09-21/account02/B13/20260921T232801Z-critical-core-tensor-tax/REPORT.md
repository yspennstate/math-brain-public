TASK: B13 ACCOUNT: account02 RUN: 2026-09-21T23:28:01.447921Z — exact FEI critical-core reduction and a tensor tax for folded cooling

MODEL: GPT-5.6 Sol (self-report)  
REQUESTED EFFORT: maximum actually supported  
CONFIGURED / KNOWN REASONING LEVEL: UNKNOWN / NOT_EXPOSED  
PROVIDER REASONING USAGE: null / NOT_EXPOSED  
EXECUTION: WITHOUT_VERIFIED_BRAIN

# Outcome

**ESSENTIAL_STEP_APPLIED at the critical-core/tensor-quantifier interface; full uniform-cube FEI remains OPEN / NOT PROVED.**

The later `FEI-PROOF-EXECUTION-20260921T230620Z` reset changes account02/B13's immediate assignment to Campaign A: prove the exact minimum-dimensional critical-core reduction and the property actually needed by the restriction argument, with tensor and character-gauge quantifiers checked rather than assumed.

This report does two things.

1. It gives an exact fixed-constant minimal-counterexample reduction for the original folded FEI defect `H-CJ`.  A minimal violating Boolean function is simultaneously **strictly restriction-critical for every nonempty physical block, tensor-primitive, and character-gauge invariant**.  Thus Campaign A may legitimately center such a core without changing any child defect or block drift.  This reduction has no tensor tax because `H` and `J` are exactly additive on disjoint Boolean products.

2. It consumes account01/B18's completed folded-cooling potential and checks the tensor quantifier that its report did not claim.  The dimension-cooled activation potential is **not tensor additive**.  A genuine four-bit Boolean tensor product already makes its `G_lambda/J` ratio strictly larger than the ratios of its two identical factors.  I prove an exact common-scale product formula and a one-shot universal repair:

\[
G_\lambda(f_1\otimes\cdots\otimes f_m)
\le \sum_r G_\lambda(f_r)+\kappa\lambda J(f),
\qquad
\kappa=2e^{-1/2}-1<0.214.
\]

Consequently a finite `G_lambda/J` bound `R` on tensor-primitive Boolean functions implies the full universal bound

\[
\boxed{
H(f)\le \left[R+(1+\kappa)\lambda+\frac2{\ln2}\right]J(f)
\le \left[R+(1+\kappa)\lambda+\frac2{\ln2}\right]I(f).
}
\]

This makes the primitive reduction for the account01 folded-cooling candidate mathematically legitimate with an explicit finite tax.  It does **not** prove that a restriction-maximizer of `G_lambda/J` is primitive; the strict Boolean witness shows that assertion is false without an additional argument.  The remaining Campaign-A implication is therefore the selector/certificate on the exact original `C`-critical core, or a surgery lemma that reconciles restriction-criticality with the `kappa lambda` tensor tax.

# 1. Fresh state and the completed other-account result actually used

The scientific repository was refreshed before the attack.  The named completed other-account result used here is

`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260921T2205Z-folded-cooling-compiler/REPORT.md`, report blob

`9f2bb40584be20e5e440e7f3913873c34858bc91`.

Its definitions are retained exactly.  If `X` is the Fourier spectral sample, `p_i=Pr(i in X)`,

\[
j_i=\min(p_i,1-p_i),\qquad J(f)=\sum_i j_i,
\]

and for `0<=z<=1`

\[
\Phi_z(k)=1+z+\cdots+z^{k-1},\qquad \Phi_z(0)=0,
\]

then its folded activation potential is

\[
\mathcal A_z(f)
=\min_{T\subseteq[d]}\mathbb E\,\Phi_z(|X\triangle T|).
\tag{1.1}
\]

The peer proves

\[
0\le \mathcal A_z(f)\le J(f),
\qquad
\mathcal A_1(f)=J(f),
\tag{1.2}
\]

monotonicity in `z`, exact character invariance, and a physical restriction telescope that remains valid when every descendant chooses its own minimizing character gauge.  It then uses the dimension-cooling scale

\[
z_d=1-\frac1d
\tag{1.3}
\]

inside an activation-refunded crossing compiler.  Its corrected entropy functional is

\[
\mathcal F(f)=H(f)-\mathcal C(f),
\qquad
0\le \mathcal C(f)\le \frac2{\ln2}J(f),
\tag{1.4}
\]

where `C` is a sum of coordinatewise functions of `j_i`, hence `F`, `C`, and `J` are additive on disjoint products.  For `lambda>=0` put

\[
G_\lambda(f)=\mathcal F(f)-\lambda\mathcal A_{z_d}(f).
\tag{1.5}
\]

The peer's restriction theorem resolves the **gauge** problem for (1.5).  The new work below resolves the separate **tensor** quantifier up to a universal explicit tax, and shows by a Boolean witness why a zero-tax primitive assertion would be wrong.

# 2. Required comparison with the last THREE substantive B13 reports

The last three completed substantive own reports are:

1. `20260921T215826Z-cross-plaquette-tensor-correction`: proved a sharp signed direct-product correction.  For every physical cut there is an actual anchor child and a Boolean correction whose conditional physical Shannon entropy is at most half the oriented cross-support boundary.  It left the physical-to-Fourier Shannon transfer open.
2. `20260921T211122Z-block-holevo-support-boundary`: proved that the restriction mixture information and spectral block mutual information are at most the bipartite phase entropy, itself at most the oriented Boolean support-boundary bank; exact zero bank is multiplicative tensor factorization.
3. `20260921T195704Z-tensor-amortized-incidence`: proved that the proposed global harmonic layer-incidence residual bound is already full-FEI-strength under tensor powers, forcing that harmonic route away from an all-functions residual theorem and toward primitive critical cores.

## FULL-PROBLEM CHANGE

**Before:** B13 had established useful tensor-aware block structure and had already warned that a global harmonic residual payment is FEI-hard.  However, the exact critical-core quantifiers demanded by the new Campaign-A reset were not compiled against the newest folded-cooling potential.  In particular there was no proof that a `G_lambda/J` critical object could be taken tensor-primitive.

**After:** the original FEI defect admits an exact no-loss minimum-dimensional reduction: a minimal `H-CJ>0` counterexample is simultaneously all-block restriction-critical and tensor-primitive in every character gauge.  For the **different** folded-cooling numerator `G_lambda`, exact tensor primitivity is false; the report replaces it by a proved one-shot tax `kappa lambda`, `kappa=2e^{-1/2}-1`.  A finite primitive `G_lambda/J` bound now has a proved transfer all the way back to original `H/I` with explicit coefficient.

**Full-bound status:** NO FULL-BOUND MOVEMENT.  No finite value of the remaining primitive bound `R` is proved here.  The universal block selector/certificate is still missing, so FEI remains open.

## MECHANISM CHANGE

**Before:** actual truth-table direct-product testing, cross-plaquette Poincare, and physical child clustering.

**After:** (i) fixed-constant minimal-counterexample induction in the original folded defect, and (ii) a Laplace transform of spectral Hamming distance whose maximizing character center factorizes exactly under disjoint products.  This is a different Boolean mechanism from the preceding three reports.

Creative moves from `FLEET_RULES.md`: **#5 add a parameter** (`z` and the Laplace transform), **#12 find what is conserved** (exact character invariance and additive `H,J,F`), and **#27 swap the quantifiers** (first prove the original minimal-counterexample core, then quantify the separate tensor tax for the auxiliary potential instead of silently identifying the two notions of criticality).

# 3. Exact folded FEI equivalence

For a Boolean function `f:{0,1}^d->{-1,+1}` let

\[
p_S=\widehat f(S)^2,
\qquad
H(f)=\sum_S p_S\log_2\frac1{p_S},
\qquad
I(f)=\sum_i p_i,
\]

where `p_i=Pr(i in X)` for `X~p`.  Define

\[
J(f)=\sum_i \min(p_i,1-p_i).
\tag{3.1}
\]

Multiplication by a character `chi_T` shifts the spectral sample by `X -> X triangle T`.  Hence `H` is invariant and

\[
I(\chi_Tf)
=\sum_{i\notin T}p_i+\sum_{i\in T}(1-p_i).
\]

Minimizing coordinatewise gives

\[
\boxed{J(f)=\min_T I(\chi_Tf).}
\tag{3.2}
\]

Therefore the optimal universal constants in

\[
H(f)\le C I(f)
\quad\hbox{and}\quad
H(f)\le C J(f)
\]

are identical.  The forward implication to `I` uses `J<=I`; conversely, apply an `I`-bound to a minimizing character multiple.  Everything below may therefore work with `J` and transfer back to the original FEI statement with no constant loss.

A useful degenerate case is exact: `J(f)=0` implies that every coordinate-membership bit of the spectral sample is deterministic, so the spectral sample is a single set.  Thus `H(f)=0` and `f` is a character up to sign.

# 4. PROVED: exact minimum-dimensional `C`-critical core

Fix any finite `C>0` and define the original folded FEI defect

\[
\delta_C(f):=H(f)-C J(f).
\tag{4.1}
\]

### Theorem 4.1 — minimum-dimensional FEI core

If some Boolean function has `delta_C(f)>0`, then there is such a function `g` of minimum ambient dimension with all of the following properties.

1. **No dummy/zero-cost coordinates.** `J(g)>0`, and no coordinate can be deleted without changing `g` up to multiplication by a character.
2. **Strict physical restriction criticality.** For every nonempty physical block `A` and every child `g_{A=a}`,
   \[
   \delta_C(g_{A=a})\le0.
   \tag{4.2}
   \]
   Consequently, with
   \[
   D_A(g)=J(g)-\mathbb E_aJ(g_{A=a}),
   \qquad
   \Delta_AH=H(g)-\mathbb E_aH(g_{A=a}),
   \]
   one has the strict all-block inequality
   \[
   \boxed{
   \Delta_AH-C D_A
   =\delta_C(g)-\mathbb E_a\delta_C(g_{A=a})
   \ge\delta_C(g)>0.
   }
   \tag{4.3}
   \]
3. **Tensor primitivity.** There is no nontrivial disjoint factorization
   \[
   g(x_A,x_B)=u(x_A)v(x_B)
   \tag{4.4}
   \]
   with both coordinate blocks nonempty.
4. **Gauge invariance of the whole critical statement.** For every character `chi_R`, the function `chi_R g` has the same parent defect, the same child defects after the corresponding physical restriction, and the same `Delta_AH` and `D_A`.  Hence (4.2)--(4.3) hold in every character gauge.  In particular one may choose the median character so that every surviving spectral marginal is at most `1/2`, giving
   \[
   I(\chi_Rg)=J(g),
   \tag{4.5}
   \]
   without changing criticality.

### Proof

Choose a violating Boolean function with the fewest coordinates, deleting coordinates on which the function is independent.  Since a character has zero defect, the chosen function is noncharacter and `J>0`.

Every nonempty physical restriction removes at least one ambient coordinate.  After deleting any newly irrelevant coordinates, each child therefore has smaller dimension.  Minimality gives (4.2).  Subtracting the child defects from the parent defect gives the identity and strict inequality (4.3).

For tensor primitivity, Fourier spectral laws tensorize on disjoint products, so

\[
H(uv)=H(u)+H(v).
\tag{4.6}
\]

Each coordinate influence belongs to exactly one factor, and folding is coordinatewise, hence

\[
J(uv)=J(u)+J(v).
\tag{4.7}
\]

Thus

\[
\delta_C(uv)=\delta_C(u)+\delta_C(v).
\tag{4.8}
\]

If the parent defect is positive, at least one factor has positive defect and strictly smaller dimension, contradicting minimality.  This includes a nontrivial character factor: it has `H=J=0`, so the other factor inherits the whole positive defect.

Finally, write `R=R_A disjoint union R_{A^c}`.  On a physical child,

\[
(\chi_Rg)_{A=a}
=\sigma(a)\,\chi_{R_{A^c}}\,g_{A=a}
\tag{4.9}
\]

for a sign `sigma(a)`.  Spectral entropy and folded influence are invariant under sign and character multiplication, so every child defect is unchanged.  The parent defect and the two decrements are unchanged as well.  This proves item 4.  QED.

### Why this is the correct exact core for Campaign A

The quantifiers in Theorem 4.1 are stronger and safer than saying that **every weak ratio-critical function** is primitive; tensor replication already killed that latter claim in earlier work.  Here primitivity comes only after an existential minimum-dimension choice under the fixed original defect `H-CJ`.  The reduction therefore survives tensor powers exactly and does not claim a shell statistic or auxiliary potential automatically survives them.

# 5. The tensor question for account01/B18's folded activation

The preceding theorem does **not** automatically apply to the peer's auxiliary numerator `G_lambda`, because the activation term depends on the ambient dimension through `z_d`.  This section computes its exact tensor behavior.

For `0<=z<1`, define the folded spectral Laplace maximum

\[
M_z(f):=\max_{T\subseteq[d]}\mathbb E\,z^{|X\triangle T|}.
\tag{5.1}
\]

Since

\[
\Phi_z(k)=\frac{1-z^k}{1-z},
\]

the peer potential is exactly

\[
\boxed{
\mathcal A_z(f)=\frac{1-M_z(f)}{1-z}.
}
\tag{5.2}
\]

This representation exposes a tensor structure invisible in the linear `Phi_z` notation.

### Lemma 5.1 — exact common-scale tensor identity

For disjoint Boolean factors `f_1,...,f_m` and one common `z`,

\[
\boxed{
M_z\!\left(\bigotimes_r f_r\right)=\prod_r M_z(f_r).
}
\tag{5.3}
\]

Equivalently,

\[
\boxed{
1-(1-z)\mathcal A_z\!\left(\bigotimes_r f_r\right)
=\prod_r\left[1-(1-z)\mathcal A_z(f_r)\right].
}
\tag{5.4}
\]

### Proof

The product Fourier law makes the factor spectral samples independent.  Every character center on the product splits uniquely into centers `T_r` on the factor coordinate blocks, and

\[
z^{|X\triangle T|}=\prod_r z^{|X_r\triangle T_r|}.
\]

The expectation factorizes, and maximizing a product of nonnegative independent factor terms separates into the product of the individual maxima.  Substitute (5.2).  QED.

At the dimension-cooling parent scale `z_d=1-1/d`, where `d=sum_r d_r`, set

\[
a_r:=\mathcal A_{z_d}(f_r),\qquad
x_r:=\frac{a_r}{d}.
\tag{5.5}
\]

Then (5.4) becomes

\[
\boxed{
\mathcal A_{z_d}\!\left(\bigotimes_r f_r\right)
=d\left[1-\prod_r(1-x_r)\right].
}
\tag{5.6}
\]

The peer monotonicity and (1.2) give

\[
\mathcal A_{z_{d_r}}(f_r)\le a_r\le J(f_r),
\qquad
s:=\sum_r x_r\le\frac{J(f)}d\le\frac12.
\tag{5.7}
\]

# 6. PROVED: one-shot tensor tax for dimension-cooled activation

Define

\[
\kappa:=2e^{-1/2}-1=0.213061319425\ldots<\frac14.
\tag{6.1}
\]

### Theorem 6.1 — folded activation tensor tax

For every disjoint Boolean factorization `f=otimes_r f_r`, with each factor evaluated at its **own** dimension-cooling scale,

\[
\boxed{
\sum_r\mathcal A_{z_{d_r}}(f_r)
-\mathcal A_{z_d}(f)
\le \kappa J(f)
<\frac14J(f).
}
\tag{6.2}
\]

### Proof

By (5.7), replacing each own-scale activation by `a_r` only increases the left side.  Therefore (5.6) gives

\[
\sum_r\mathcal A_{z_{d_r}}(f_r)-\mathcal A_{z_d}(f)
\le d\left[s-1+\prod_r(1-x_r)\right].
\tag{6.3}
\]

For `x_r>=0`,

\[
\prod_r(1-x_r)\le e^{-s},
\]
so the right side is at most

\[
d(s-1+e^{-s}).
\tag{6.4}
\]

For `s>0`, write

\[
r(s)=\frac{s-1+e^{-s}}s
=1-\frac{1-e^{-s}}s.
\]
Then

\[
r'(s)=\frac{1-(1+s)e^{-s}}{s^2}\ge0
\]
by `e^s>=1+s`.  Since `s<=1/2`,

\[
r(s)\le r(1/2)=2e^{-1/2}-1=\kappa.
\]

Also `ds=sum_r a_r<=J(f)`.  Combining these inequalities proves (6.2); `kappa<1/4` is immediate numerically, or from a standard elementary bound for `e^{-1/2}`.  QED.

The tax is **one-shot over all tensor factors at once**.  It does not accumulate once per recursive factorization depth.

# 7. Application to the peer's activation-refunded numerator

Let `F` be the account01/B18 corrected entropy functional (1.4).  It is additive on disjoint products because `H` is additive and its correction is a sum of coordinatewise functions of `j_i`.  Put

\[
G_\lambda(f)=F(f)-\lambda\mathcal A_{z_d}(f).
\]

### Corollary 7.1 — primitive-to-global transfer

For every disjoint tensor factorization into noncharacter tensor-primitive factors,

\[
\boxed{
G_\lambda(f)
\le\sum_rG_\lambda(f_r)+\kappa\lambda J(f).
}
\tag{7.1}
\]

Hence, if some finite `R` satisfies

\[
G_\lambda(g)\le R J(g)
\tag{7.2}
\]

for **every tensor-primitive Boolean `g`**, then every Boolean function satisfies

\[
G_\lambda(f)\le(R+\kappa\lambda)J(f).
\tag{7.3}
\]

Because `A_z<=J` and `C<=2J/ln2`, this transfers all the way back to the original entropy:

\[
\boxed{
H(f)
=G_\lambda(f)+\lambda\mathcal A_{z_d}(f)+\mathcal C(f)
\le
\left[R+(1+\kappa)\lambda+\frac2{\ln2}\right]J(f).
}
\tag{7.4}
\]

Finally `J<=I`, so the same coefficient proves original FEI.

### Proof

Subtract the sum of the factor `G_lambda` values from the product value.  Additivity of `F` leaves

\[
\lambda\left[
\sum_r\mathcal A_{z_{d_r}}(f_r)-\mathcal A_{z_d}(f)
\right],
\]
which is at most `kappa lambda J(f)` by Theorem 6.1.  Factor every Boolean function maximally; character factors have `H=J=A=0` after folding and may be discarded.  Sum (7.2) over the remaining primitive factors and apply (7.1), proving (7.3).  Equation (7.4) follows from the peer's universal caps.  QED.

This is a genuine full-problem transfer: **finiteness of the primitive constant `R` is enough for a finite dimension-independent FEI constant**.  The report does not prove that `R` is finite.

# 8. Genuine Boolean witness: zero-tax tensorization of `G_lambda` is false

Let `w` be the two-bit one-point defect with truth table, in lexicographic binary order,

\[
w=(1,-1,1,1).
\]

The exact checker gives

\[
\mathcal A_{z_2}(w)=\mathcal A_{1/2}(w)=\frac78,
\tag{8.1}
\]
while at the four-bit parent scale

\[
\mathcal A_{3/4}(w)=\frac{15}{16}.
\tag{8.2}
\]

For the genuine Boolean tensor square `W=w otimes w`, Lemma 5.1 gives exactly

\[
\mathcal A_{3/4}(W)
=\frac{1695}{1024}.
\tag{8.3}
\]

Therefore

\[
2\mathcal A_{1/2}(w)-\mathcal A_{3/4}(W)
=\frac{97}{1024}>0.
\tag{8.4}
\]

Since `F` and `J` are additive and `J(W)=2J(w)=2`, for every `lambda>0`

\[
\frac{G_\lambda(W)}{J(W)}
=
\frac{G_\lambda(w)}{J(w)}
+\lambda\frac{97}{2048}.
\tag{8.5}
\]

Thus an auxiliary `G_lambda/J` maximizer can be **more tensorized**, not less.  It is invalid to take account01/B18's restriction-critical `G_lambda` core and silently append “tensor-primitive” with zero loss.  This is a true Boolean obstruction, not a non-Boolean profile example.

Theorem 6.1 is the quantitative repair.

# 9. Gauge and dummy-coordinate quantifiers

Two small points are needed to keep the reduction source-exact.

**Fixed ambient dimension.** For fixed `d`, multiplication by any character simply relabels the maximizing center in (5.1), so `A_{z_d}`, `G_lambda`, `H`, and `J` are all exactly character invariant.  Physical restriction commutes with that gauge as in (4.9).  Account01/B18's re-centering theorem is therefore compatible with Theorem 4.1.

**Dropping a genuinely irrelevant/character-only coordinate.** Removing such a coordinate lowers the cooling scale from `z_d` to `z_{d-1}`.  Since `A_z` is nondecreasing in `z`, the activation penalty cannot increase after the coordinate is removed; consequently `G_lambda` cannot decrease.  Thus dummy or pure-character padding cannot create the hardest `G_lambda/J` instance.  This justifies stripping zero-cost coordinates before invoking the primitive factorization in Corollary 7.1.

This direction is important: changing the dimension parameter is not an exact invariance.  It is a monotone reduction, and the report uses only that direction.

# 10. What this says about the current Campaign-A candidate

The compact conditional end-to-end chain is now:

1. `H<=CJ` is equivalent to original `H<=CI` at the same constant by (3.2).
2. If a fixed `C` fails, Theorem 4.1 produces one **original-defect** core that is simultaneously tensor-primitive, all-block restriction-critical, and freely centerable by characters.
3. Account01/B18 supplies a character-invariant folded activation bank with total root cost at most `J` and a physical restriction telescope.
4. If the needed activation-refunded crossing/certificate estimate can be proved with finite constants on all relevant primitive cores, Theorem 6.1/Corollary 7.1 show how to restore arbitrary tensor products with only the explicit one-shot `kappa lambda` charge.
5. The peer correction term costs at most `2J/ln2`, and (7.4) returns the result to `H/I`.

The **first still-unproved implication** is not tensor primitivity any more.  It is the realizable selector/certificate itself: one must prove a finite `R` in (7.2), or prove the concrete crossing certificate that implies such an `R`, on the exact class of cores used.  If the certificate proof requires a function to be both `G_lambda`-restriction-critical and primitive, an additional surgery lemma is needed; the witness (8.5) proves that simultaneous property does not follow formally from tensor additivity.

The safer route is to formulate the selector on the exact original `C`-critical core of Theorem 4.1, where restriction criticality and primitivity coexist with no tax, and use folded activation only as a paid auxiliary bank inside that one-root contradiction.

# 11. Failed stronger claim preserved precisely

**Killed claim:** “Because folded activation is character invariant and bounded by `J`, a minimum/maximal `G_lambda/J` core may be assumed tensor-primitive with no loss.”

**Failure:** character invariance has no bearing on tensor additivity.  Equations (8.1)--(8.5) give a genuine Boolean four-bit counterexample to zero-loss tensor descent for `G_lambda` whenever `lambda>0`.

**Repair:** the exact Laplace product identity yields the finite one-shot tax (6.2).  This repair is sufficient for the primitive-to-global entropy transfer (7.4), but not by itself for a local selector that insists on simultaneous restriction-criticality and primitivity.

# 12. Executed exact checker

`verify_activation_tensor_tax.py` uses only the Python standard library and exact `Fraction` arithmetic.  It exhausts Boolean functions modulo global output sign in dimensions one and two, checks all ordered factor pairs with factor dimensions one or two, and separately checks character gauges.

Archived result: **PASS, 236 exact checks**:

- 100 exact common-scale product identities (5.4)/(5.6);
- 100 exact rational tax checks using the weaker clean corollary `tax<=J/4`;
- 36 exact character-gauge invariance checks.

The strict witness is recovered exactly:

\[
A_{1/2}(w)=7/8,
\quad
A_{3/4}(w)=15/16,
\quad
A_{3/4}(w\otimes w)=1695/1024,
\quad
\frac{2A_{1/2}(w)-A_{3/4}(w\otimes w)}{J(w\otimes w)}=97/2048.
\]

The checker is a sanity check for the algebra; the analytic proofs above establish the universal statements.

# 13. Claim ledger

- **PROVED:** optimal constants for `H<=CI` and `H<=CJ` are equal.
- **PROVED:** fixed-`C` minimum-dimensional counterexample is all-block restriction-critical, tensor-primitive, and character-gauge invariant.
- **PROVED:** exact folded spectral Laplace product identity (5.3)--(5.4).
- **PROVED:** dimension-cooled folded activation has one-shot tensor defect at most `kappa J`, `kappa=2e^{-1/2}-1<1/4`.
- **PROVED:** a finite primitive `G_lambda/J` bound transfers to full FEI with coefficient `R+(1+kappa)lambda+2/ln2`.
- **DISPROVED:** zero-loss tensor descent / automatic tensor primitivity for a `G_lambda/J` critical core.
- **OPEN:** finite primitive bound `R`, or the equivalent realizable activation-refunded selector/certificate with all branch costs.
- **OPEN:** any full dimension-independent FEI constant.

# 14. Next exact attack

The next B13 step should not add another profile.  Work on the first remaining Campaign-A arrow in the exact original critical core: combine (4.3) for the block selected by the account01/account02 crossing machinery with the folded activation drop, and derive either

\[
\Delta_AH\le C D_A
\]

for one physical block (contradicting (4.3)), or a finite primitive `G_lambda/J` bound `R` that feeds (7.4).  The two-bit tensor witness must remain in every attempted proof as the test that no zero-tax `G_lambda` primitivity assumption has slipped back in.

No novelty or publication-priority claim is made.  No brain package was installed or consulted; this was independent repository-based FEI derivation under the current joint order.
