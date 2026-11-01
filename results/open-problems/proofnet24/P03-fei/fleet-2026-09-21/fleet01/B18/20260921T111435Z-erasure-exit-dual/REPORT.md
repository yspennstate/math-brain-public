# B18 FEI: random-erasure EXIT/Bayes dual for the proper-block selector

**Date:** 21 September 2026  
**Status:** **PARTIAL / PROVED structural reduction. Full Fourier entropy--influence (FEI) remains OPEN / NOT PROVED.**  
**Route:** APPROACH 11/12 (influence-greedy restriction / decision-tree entropy payment and a restricted-potential dual).  
**Execution label:** `WITHOUT_VERIFIED_BRAIN`. No authenticated mathematical/cognitive-brain retrieval or receiver-context use was available or used.  
**Novelty:** no publication-priority claim. This is a new-to-this-repository synthesis pending literature review.

## 1. Input used at its exact scope

Let `f:{-1,1}^R->{-1,1}` be Boolean after deleting irrelevant coordinates, and let `X` be its Fourier spectral sample:
\[
\Pr[X=S]=\widehat f(S)^2.
\]
Write
\[
H=H(X),\qquad p_i=\Pr[i\in X]=\operatorname{Inf}_i(f),\qquad I=\sum_i p_i.
\]

Two currently proved ingredients are used.

1. For every physical block `A subseteq R`, the restriction package gives
   \[
   \Delta_AH:=H(f)-2^{-|A|}\sum_{a\in\{-1,1\}^A}H(f_a)
   =B_A+R_A,
   \]
   where
   \[
   B_A:=H(X_A\mid X_{A^c}),
   \]
   and the block prediction-error theorem gives
   \[
   0\le R_A\le c_*M_A,\qquad c_*:=\frac2{\ln2}.
   \tag{1.1}
   \]
   Here
   \[
   M_A
   :=
   \sum_{i\in A}
   \mathbb E\!\left[
      \min\{\Pr(X_i=1\mid X_{A^c}),\Pr(X_i=0\mid X_{A^c})\}
   \right]
   \tag{1.2}
   \]
   is the Bayes Hamming error for predicting the erased spectral bits from the un-erased spectral coordinates.

2. If `g` maximizes `H/I` among all nonconstant physical restriction descendants, and
   \[
   r(g):=\frac{H(g)}{I(g)},
   \]
   then every nonempty physical block is restriction-critical:
   \[
   \Delta_AH(g)\ge r(g) I_A(g),
   \qquad
   I_A:=\sum_{i\in A}p_i.
   \tag{1.3}
   \]
   The same continuation proves the exact adaptive influence lifetime identity and the proper-block selector compiler.

No conditional signed-transport compiler is used below. In particular, no open R32/T-join-to-flux representation is silently promoted.

The question of this run is: can APPROACH 11/12 replace a search over all `2^{|R|}` blocks by a **one-parameter dual family of random erasures**, while retaining the block recombination payment (1.1)?

The answer is yes. The remaining obstruction becomes a quantitative Booleanity statement about an erasure curve.

## 2. Bernoulli random-block erasure

For `0<=t<=1`, let `A_t subseteq R` contain each coordinate independently with probability `t`. Define
\[
F_f(t):=\mathbb E\,B_{A_t},
\qquad
G_f(t):=\mathbb E\,M_{A_t},
\qquad
\overline\Delta_f(t):=\mathbb E\,\Delta_{A_t}H.
\tag{2.1}
\]

Averaging (1.1) immediately gives the first universal estimate:
\[
\boxed{
\overline\Delta_f(t)\le F_f(t)+c_*G_f(t).
}
\tag{2.2}
\]
Also
\[
\boxed{
\mathbb E\,I_{A_t}=tI(f).
}
\tag{2.3}
\]

The useful point is that both `F` and `G` have direct sequential-prediction interpretations.

## 3. PROVED: an EXIT identity for spectral erasure

### Theorem 3.1 — exact derivative of the block-erasure entropy

For `0<t<1`,
\[
\boxed{
F_f'(t)
=
\sum_{i\in R}
\mathbb E_{E_t^{(i)}}
H\!\left(
X_i\mid X_{R\setminus(E_t^{(i)}\cup\{i\})}
\right),
}
\tag{3.1}
\]
where `E_t^{(i)}` is an independent Bernoulli-`t` subset of `R\setminus\{i\}`.

Consequently
\[
F_f(0)=0,\qquad F_f(1)=H(f),
\tag{3.2}
\]
`F_f'` is nondecreasing, and hence `F_f` is convex:
\[
\boxed{
0\le F_f(t)\le tH(f).
}
\tag{3.3}
\]

### Proof

Since
\[
B_A=H(X_A\mid X_{A^c})=H(X)-H(X_{A^c}),
\]
the standard derivative of a Bernoulli-subset expectation gives
\[
F_f'(t)
=
\sum_i
\mathbb E_E\,[B_{E\cup\{i\}}-B_E].
\]
For `i notin E`,
\[
B_{E\cup\{i\}}-B_E
=
H(X_{R\setminus E})
-
H(X_{R\setminus(E\cup\{i\})})
=
H(X_i\mid X_{R\setminus(E\cup\{i\})}),
\]
which proves (3.1). As `t` increases, fewer coordinates remain in the conditioning sigma-field, so each conditional entropy in (3.1) is nondecreasing under the Bernoulli coupling. Thus `F'` is nondecreasing and `F` is convex. A convex function joining `(0,0)` to `(1,H)` lies below its chord, giving (3.3). QED.

Equivalently, differentiating once more in the interior gives the nonnegative conditional-mutual-information curvature
\[
F_f''(t)
=
2\sum_{i<j}
\mathbb E\,
I\!\left(
X_i;X_j
\mid X_{R\setminus(E_t^{(i,j)}\cup\{i,j\})}
\right)
\ge0,
\tag{3.4}
\]
where `E_t^{(i,j)}` is Bernoulli-`t` on the remaining coordinates.

Thus the departure from the independent linear chord is literally accumulated multiscale conditional dependence.

## 4. PROVED: Bayes-error payment is controlled by the EXIT slope

For a realized erased set `A` and `i in A`, let
\[
e_i(A\setminus\{i\})
:=
\mathbb E\!\left[
\min\{\Pr(X_i=1\mid X_{A^c}),\Pr(X_i=0\mid X_{A^c})\}
\right].
\]
Then (1.2) is
\[
M_A=\sum_{i\in A}e_i(A\setminus\{i\}).
\]
Averaging over `A_t`,
\[
G_f(t)
=
t\sum_i
\mathbb E_{E_t^{(i)}}e_i(E_t^{(i)}).
\tag{4.1}
\]

For every Bernoulli posterior `q`,
\[
h_2(q)\ge2\min(q,1-q).
\tag{4.2}
\]
Applying (4.2) conditionally in (3.1) and comparing with (4.1) yields
\[
\boxed{
G_f(t)\le\frac t2F_f'(t).
}
\tag{4.3}
\]

Combining (2.2) and (4.3) gives a purely one-dimensional universal restriction estimate:
\[
\boxed{
\overline\Delta_f(t)
\le
F_f(t)+\frac{t}{\ln2}F_f'(t).
}
\tag{4.4}
\]

No FEI hypothesis is used in (2.2)--(4.4).

## 5. The erasure-dependence deficit

Define
\[
\boxed{
D_f(t):=tH(f)-F_f(t).
}
\tag{5.1}
\]
By (3.3),
\[
D_f(t)\ge0,\qquad D_f(0)=D_f(1)=0,
\tag{5.2}
\]
and `D_f` is concave.

Two endpoint derivatives identify familiar dependence quantities:
\[
F_f'(0)=\sum_i H(X_i\mid X_{-i}),
\qquad
D_f'(0)=H-\sum_iH(X_i\mid X_{-i}),
\tag{5.3}
\]
so `D_f'(0)` is the dual total correlation of the spectral-membership vector. At the other endpoint,
\[
F_f'(1)=\sum_iH(X_i)=\sum_i h_2(p_i),
\qquad
D_f'(1)=H-\sum_i h_2(p_i)=-\operatorname{TC}(X).
\tag{5.4}
\]

Thus `D_f` continuously interpolates between the two standard multivariate-correlation deficits, while its curvature (3.4) resolves those deficits by erasure scale.

## 6. PROVED: a one-parameter dual certificate for a proper descending block

Define, for `t>0`,
\[
Q_f(t)
:=
\frac{F_f(t)+c_*G_f(t)}{tI(f)}.
\tag{6.1}
\]

### Theorem 6.1 — random-erasure proper-block certificate

If
\[
Q_f(t)<r(f):=\frac{H(f)}{I(f)}
\tag{6.2}
\]
for some `0<t<1`, then there exists a **nonempty proper** physical block
\[
\varnothing\ne A\subsetneq R
\]
such that
\[
\boxed{
\frac{\Delta_AH(f)}{I_A(f)}
\le Q_f(t)<r(f).
}
\tag{6.3}
\]

Equivalently, the strict dual witness
\[
\boxed{
\Phi_f(t):=D_f(t)-c_*G_f(t)>0
}
\tag{6.4}
\]
certifies a proper block whose restriction decrement per unit influence is smaller than the parent ratio.

### Proof

By (2.2), (2.3), and (6.1),
\[
\mathbb E[\Delta_{A_t}H-Q_f(t)I_{A_t}]\le0.
\]
The empty block contributes zero. The full block `A=R` has
\[
\frac{\Delta_RH}{I_R}=\frac HI=r(f)>Q_f(t),
\]
so the nonpositive expectation cannot be supplied solely by the empty and full blocks. Therefore some nonempty proper block has `Delta_AH-QI_A<=0`, proving (6.3). The equivalence of (6.2) and (6.4) follows from `tH=r\,tI`. QED.

This is the requested APPROACH 11/12 synthesis: a greedy/block descent can be certified by a scalar erasure parameter rather than by an unrestricted potential or an exhaustive block search.

## 7. PROVED: every maximal-ratio counterexample core must stay inside an erasure tube at every scale

Let `g` be a nonconstant physical restriction descendant maximizing
\[
r:=\frac{H(g)}{I(g)}
\]
among all descendants. By the inherited all-block criticality (1.3),
\[
\Delta_AH(g)\ge rI_A(g)
\]
for every nonempty `A`, with equality also valid for the empty block after setting both sides to zero. Averaging over `A_t` gives
\[
tH(g)=rtI(g)\le\overline\Delta_g(t).
\]
Together with (2.2):
\[
\boxed{
D_g(t)\le c_*G_g(t)
\qquad\text{for every }0<t<1.
}
\tag{7.1}
\]

Using (4.3) gives the weaker but intrinsic differential form
\[
\boxed{
D_g(t)
\le
\frac{t}{\ln2}F_g'(t)
=
\frac{t}{\ln2}\bigl(H(g)-D_g'(t)\bigr).
}
\tag{7.2}
\]

Since trivially `M_A<=I_A`, also
\[
G_g(t)\le tI(g),
\]
hence
\[
\boxed{
F_g(t)\ge t\,[H(g)-c_*I(g)]
=t\,[r-c_*]\,I(g).
}
\tag{7.3}
\]

So a hypothetical high-ratio FEI counterexample can be replaced by a restriction-maximal core whose **entire spectral erasure curve**, at every scale, remains within a dimension-free Bayes-error tube of the independent chord:
\[
0\le D_g(t)\le c_*G_g(t)\le c_*tI(g).
\tag{7.4}
\]

This is stronger than a single-coordinate necessary condition because it must hold simultaneously for every erasure density `t`.

At `t downarrow0`, (7.1) recovers the singleton dual-total-correlation payment. The newest scalar erasure-frontier theorem strengthens that endpoint numerically; the point here is the new all-scale constraint.

## 8. PROVED: exact interior contact with the independent chord is rigid

### Proposition 8.1

If
\[
D_f(t_0)=0
\]
for any interior `t_0 in (0,1)`, then the spectral membership bits of `f` are mutually independent.

Consequently, using the already proved exact-product classification,
\[
\boxed{
\frac{H(f)}{I(f)}>2
\quad\Longrightarrow\quad
D_f(t)>0
\quad\text{for every }0<t<1.
}
\tag{8.1}
\]

### Proof

`F` is convex, `F(0)=0`, `F(1)=H`, and `F(t)<=tH`. If equality `F(t_0)=t_0H` holds at one interior point, equality in the convex chord inequality forces `F(t)=tH` throughout `[0,1]`. Therefore
\[
F'(1)=H.
\]
But (5.4) gives
\[
F'(1)=\sum_i h_2(p_i).
\]
Hence
\[
\sum_i h_2(p_i)-H=0,
\]
i.e. the total correlation vanishes and the membership bits are independent. The exact-product theorem for Boolean spectra then gives `H<=2I`. QED.

This is qualitative rigidity only. It does not give the dimension-free stability needed for FEI.

## 9. A new sufficient scalar target for full FEI

Fix a candidate constant `C`.

### Conditional closure criterion

If every Boolean `f` satisfying
\[
\frac{H(f)}{I(f)}>C
\]
has at least one `t in (0,1)` for which
\[
\boxed{
D_f(t)>c_*G_f(t),
}
\tag{9.1}
\]
then full FEI holds with constant `C`.

### Proof

If FEI failed at `C`, choose a physical restriction descendant `g` maximizing `H/I`. It still has ratio `>C`. The hypothesis would give a scale `t` satisfying (9.1), while the maximal-core theorem (7.1) forces the opposite inequality at every scale. Contradiction. QED.

For the Hod-scale candidate `C=beta(1/2) approximately 6.4547837`, (9.1) is therefore a precise one-dimensional Booleanity/stability target.

The remaining theorem is **not** a generic information inequality. An abstract product law with many rare independent coordinates has `D(t)=0`, so generic probability alone cannot produce (9.1). Booleanity must enter. The already proved exact-product rigidity shows that the zero-deficit endpoint is forbidden except for the bent/character class, while the newest one-point tensor calculation shows that a fixed multiple of global Hellinger distance loses the needed rare-event logarithm. Thus the plausible next object is genuinely KL/multiscale: use the conditional mutual informations in the curvature formula (3.4), or the hard-core/down-set endpoint from the scalar erasure frontier, to force a quantitative gap between `D` and the Bayes error `G`.

## 10. Killed shortcut and preserved conditionality

A tempting shortcut is to replace `G` by the generic upper bound `(t/2)F'` in (7.1) and try to solve the resulting differential inequality. That cannot close FEI: arbitrary rare-coordinate product laws have `D identically 0` and satisfy the differential inequality with room to spare. The missing ingredient is specifically Boolean spectral realizability, not calculus.

Likewise, the signed-noise/oriented-cut work supplies useful paid sinks but its current R32/T-join compiler remains conditional. Nothing in this report assumes that missing compiler.

## 11. Next attack

The next B18 run on this route should attack a **quantitative erasure-tube escape lemma**:

> For Boolean spectral laws with `H/I>C`, show that at some erasure density `t`,
> \[
> D_f(t)>c_*G_f(t).
> \]

Two concrete subtargets are now visible.

1. Use (3.4) to express `D` as an integral of multiscale conditional mutual informations and prove that a law staying inside `D<=c_*G` at every scale must be close, in a KL-sensitive sense, to a product spectral law; then invoke Boolean phase cancellation / product rigidity.
2. Start from the scalar-frontier equality geometry. Exact all-coordinate endpoint structure is a uniform-activity hard-core measure on a downward-closed family. Show that any Boolean-realizable proper down-set endpoint necessarily creates an erasure scale with `D>c_*G`, or else yields a proper-block selector directly.

**Full FEI remains OPEN / NOT PROVED.**
