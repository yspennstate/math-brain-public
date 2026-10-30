SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B14, 2026-09-22T18:32:48Z.
attacking: determinant-only closure from any quantitatively nonsingular original-coordinate principal triple, uniform under outside localization.

# fleet02/B14 — determinant-only physical triple closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T183248Z-fleet02-B14-QFORM-r18`  
**Assignment:** Translations and localization  
**Status:** `PROVED SUPPORTING TARGET-LEVEL BRANCH / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. First unpaid implication and mechanism change

The previous B14 run replaced a false conditional-supremum gate by a mass-weighted half-Riesz localization ledger. The first unpaid implication was to produce a genuinely target-preserving local certificate that survives arbitrary shifts, distant fragments and unbounded supports without normalizing thin pieces.

This run changes mechanism: instead of another localization ledger, it proves a direct algebraic two-case theorem for an arbitrary **physical 3x3 principal block**. The result closes every branch having a quantitatively nonsingular original-coordinate triple, inside an arbitrary higher-rank ambient form, with a determinant-only scale and no support or moment assumptions.

The full conjecture remains open because the three-large-eigenvalue hypothesis does not force a principal 3x3 determinant bounded below by a universal constant. Section 8 gives an exact stress family.

## 2. Dependencies actually used

Three complete source-pinned arguments are used.

1. **Assigned partner fleet03/B14 r15 — zero-diagonal triple.**  
   `yspennstate/math-open-problems@49f1c21b47979575eaa8c34b90d066c8034140b4`  
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260922T173618Z-fleet03-B14-QFORM-r15/REPORT.md`  
   It proves, for the pure off-diagonal physical triple, the sharper bound
   \[
   \|p\|_\infty\le C_{\rm off}|\det B|^{-1/3},\qquad
   C_{\rm off}=21\,2^{1/3}e^{-2/3}<13.585,
   \]
   uniformly in arbitrary affine perturbations and arbitrary support geometry. That result suggested the near-zero-diagonal stability problem. The theorem below solves the stability question for **all** diagonal sizes, with a larger universal constant.

2. **Orientation-free rank-two affine half-Riesz theorem.**  
   `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`  
   `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`  
   For every invertible symmetric 2x2 matrix `S`, independent cap-one physical variables `Y=(Y1,Y2)`, and arbitrary affine term,
   \[
   \sup_t\mathbb E|Y^TSY+\ell^TY+c-t|^{-1/2}
   \le128|\det S|^{-1/4}.
   \tag{2.1}
   \]

3. **Physical indefinite-pair logarithmic envelope.**  
   `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`  
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`  
   For an invertible indefinite physical pair `P`, with
   \(D=|\det P|\) and \(\kappa=\sigma_{\min}(P)\), after completing the pair and writing the remainder as `R`, one has for every cutoff `r>0`
   \[
   p_Q(t)\le \frac{2\sqrt2}{r}
   +D^{-1/2}\,\mathbb E\log_+\frac{2r^2}{\kappa|t-R|}.
   \tag{2.2}
   \]
   The pair shifts may depend arbitrarily on the remaining variables. Original-coordinate independence of the pair is retained.

The live corrections `QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1`, `QFORM-CONDITIONAL-PROJECTION-POSITIVE-MOMENT-FALSE-v1`, and `QFORM-SCALAR-QREST-SUP-FALSE-v1` were consumed. The proof below uses none of the refuted arbitrary-joint coarea, vector-conditioned positive-moment, or scalar-conditioned supremum gates.

## 3. Main theorem

### Theorem — `QFORM-PHYSICAL-3X3-DET-BRANCH-v1`

Let `A` be any real symmetric `n x n` matrix and let `X_1,...,X_n` be independent real variables with probability densities bounded by one. Suppose an original-coordinate triple `I={i,j,k}` has nonsingular principal block

\[
B=A_{I,I}=\begin{pmatrix}
 d_1&a&b\\
 a&d_2&c\\
 b&c&d_3
\end{pmatrix},
\qquad \Delta:=|\det B|>0.
\]

Then for every affine perturbation `q^T X+q_0`, the full ambient quadratic form

\[
Q=X^TAX+q^TX+q_0
\]

has an essentially bounded density satisfying

\[
\boxed{
\|p_Q\|_\infty
\le C_3\,\Delta^{-1/3},
\qquad
C_3=128\,2^{1/4}<152.219.
}
\tag{3.1}
\]

The bound is independent of `n`, all outside coefficients and couplings, all affine terms, translations of the input laws, support diameters, fragment counts, support separation, and every moment of the inputs.

In particular, if the target matrix has a physical principal triple with `|det B|>=1`, then that branch of the full QFORM conjecture is closed with density constant `<152.219`.

The determinant exponent `-1/3` has the correct homogeneity: replacing `B` by `tau B` multiplies the output density scale by `|tau|^{-1}` and `|det(tau B)|^{-1/3}=|tau|^{-1}|det B|^{-1/3}`.

## 4. Reduction to a three-variable affine form

Condition on every coordinate outside `I`. The three active coordinates remain independent with their original cap-one densities. The outside realization contributes only a deterministic affine vector and additive constant to the active polynomial. Thus it suffices to prove (3.1) for

\[
Q_3=x^TBx+\ell^Tx+c_0
\]

with three independent cap-one inputs, uniformly in `ell,c_0`.

Write

\[
\delta:=\Delta^{1/3},\qquad
 e:=\max_i|d_i|,\qquad
 M:=\max\{|a|,|b|,|c|\}.
\]

We split according to whether a scalar physical pivot is at least `delta/2`.

## 5. Case I: a diagonal pivot is at least `delta/2`

Assume

\[
e\ge\delta/2.
\]

After relabeling, take `|d_1|=e`. Write

\[
B=\begin{pmatrix}d_1&u^T\\u&C\end{pmatrix},
\qquad
S=C-\frac{uu^T}{d_1}.
\]

Since `det B !=0`, `S` is invertible and the Schur determinant identity gives

\[
|\det S|=\frac{\Delta}{e}.
\tag{5.1}
\]

Complete the square in the first **physical** coordinate. Conditional on `Y=(X_2,X_3)`,

\[
Q_3=d_1\bigl(X_1-h(Y)\bigr)^2+R(Y),
\]

where `R(Y)=Y^TSY+beta^T Y+gamma`. For a cap-one scalar input, the translated-square density satisfies

\[
p_{d_1(X_1-h)^2}(s)\le e^{-1/2}|s|^{-1/2}.
\]

Therefore

\[
\|p_{Q_3}\|_\infty
\le e^{-1/2}\sup_t\mathbb E|R(Y)-t|^{-1/2}.
\tag{5.2}
\]

Apply the rank-two affine half-Riesz theorem (2.1) to the two remaining original coordinates:

\[
\sup_t\mathbb E|R(Y)-t|^{-1/2}
\le128|\det S|^{-1/4}.
\]

Using (5.1),

\[
\|p_{Q_3}\|_\infty
\le128 e^{-1/4}\Delta^{-1/4}.
\]

Since `e>=delta/2` and `Delta=delta^3`,

\[
e^{-1/4}\Delta^{-1/4}
\le2^{1/4}\delta^{-1}.
\]

Hence

\[
\boxed{
\|p_{Q_3}\|_\infty
\le128\,2^{1/4}\Delta^{-1/3}.
}
\tag{5.3}
\]

Arbitrary affine terms have remained inside the source half-Riesz theorem; no centering, support, or moment condition was introduced.

## 6. Case II: every diagonal is smaller than `delta/2`

Assume now

\[
e<\delta/2.
\tag{6.1}
\]

The determinant expansion is

\[
\det B=d_1d_2d_3+2abc-d_1c^2-d_2b^2-d_3a^2.
\]

Consequently

\[
\Delta\le e^3+2M^3+3eM^2.
\tag{6.2}
\]

We claim

\[
\boxed{M>\frac9{16}\delta.}
\tag{6.3}
\]

Indeed, if `M<=9delta/16`, then by (6.1)-(6.2)

\[
\frac\Delta{\delta^3}
<\frac18+2\left(\frac9{16}\right)^3
 +\frac32\left(\frac9{16}\right)^2
=\frac{1957}{2048}<1,
\]

contradicting `Delta=delta^3`.

Choose a physical pair whose off-diagonal coefficient has magnitude `M`; after relabeling,

\[
P=\begin{pmatrix}d_1&M\\M&d_2\end{pmatrix}.
\]

Because `M>9delta/16>e`,

\[
\det P=d_1d_2-M^2<0,
\]

so `P` is invertible indefinite. Moreover, viewing `P` as the zero-diagonal matrix `[[0,M],[M,0]]` plus a diagonal perturbation of norm at most `e`, the singular-value perturbation inequality gives

\[
\kappa:=\sigma_{\min}(P)
\ge M-e
>\frac{\delta}{16}.
\tag{6.4}
\]

Let

\[
D:=|\det P|.
\]

Complete this physical pair. The remaining third original coordinate `Z` enters the remainder as a scalar quadratic

\[
R(Z)=sZ^2+\beta Z+\gamma.
\]

The scalar Schur determinant identity is exact:

\[
\det B=(\det P)s,
\qquad |s|=\frac\Delta D.
\tag{6.5}
\]

For a cap-one scalar input, completing the square shows for every `rho>0`

\[
\sup_t\Pr\{|R-t|<\rho\}
\le2\sqrt{\frac{2\rho}{|s|}}.
\tag{6.6}
\]

Indeed the inverse image of an interval of length `2rho` under a scalar quadratic of leading coefficient `s` has total length at most `2sqrt(2rho/|s|)`.

Now apply the physical-pair logarithmic envelope (2.2). For every `A_0>0`, layer cake and (6.6) give

\[
\begin{aligned}
\mathbb E\log_+\frac{A_0}{|t-R|}
&=\int_0^\infty
 \Pr\{|t-R|<A_0e^{-v}\}\,dv\\
&\le4\sqrt{\frac{2A_0}{|s|}}.
\end{aligned}
\tag{6.7}
\]

Set `A_0=2r^2/kappa`. Then (2.2) becomes

\[
p_{Q_3}(t)
\le\frac{2\sqrt2}{r}
 +\frac{8r}{\sqrt{D\kappa|s|}}
=\frac{2\sqrt2}{r}
 +\frac{8r}{\sqrt{\kappa\Delta}},
\tag{6.8}
\]

where the last equality uses (6.5).

Optimizing `A/r+Br` over `r>0` gives

\[
\boxed{
\|p_{Q_3}\|_\infty
\le8\,2^{1/4}(\kappa\Delta)^{-1/4}.
}
\tag{6.9}
\]

Finally, (6.4) and `Delta=delta^3` yield

\[
\kappa\Delta>\frac{\delta^4}{16},
\]

and therefore

\[
\boxed{
\|p_{Q_3}\|_\infty
<16\,2^{1/4}\Delta^{-1/3}
<19.028\Delta^{-1/3}.
}
\tag{6.10}
\]

This is substantially stronger than the constant needed for the theorem. Combining (5.3) and (6.10) proves (3.1).

## 7. Why this is a localization theorem, not merely a three-variable theorem

The proof is uniform in the affine vector generated by conditioning every outside coordinate. Hence the active triple can be selected **before** any support localization. For almost every deterministic outside realization `z`, the same bound

\[
\Pr\{Q\in J\mid X_{I^c}=z\}
\le C_3\Delta^{-1/3}|J|
\]

holds. Integrating `z` gives the identical constant for the original arbitrary-support product law. No outside fragment is normalized, so there is no density-cap inflation; no support location, diameter, separation, tail moment, or outside affine size appears.

This is exactly the safe select-before-localize interface required by B14. It remains valid for arbitrarily distant fragments and laws with no finite positive moments.

## 8. The determinant threshold is not forced by the spectral hypothesis

The theorem does **not** solve full QFORM because a universal lower bound on one physical triple determinant is false.

For `m>=1`, consider

\[
A_m=[1]\oplus \frac1mJ_m\oplus\left(-\frac1mJ_m\right),
\]

where `J_m` is the all-ones matrix. Its nonzero spectrum is exactly

\[
\{1,1,-1\},
\]

so `s_3(A_m)=1` for every `m`.

Every nonzero 3x3 principal determinant must select the singleton coordinate, one positive-bank coordinate, and one negative-bank coordinate. Such a block is diagonal across the three groups and has determinant

\[
-\frac1{m^2}.
\]

Every other principal triple is singular. Hence

\[
\boxed{
\max_{|I|=3}|\det (A_m)_{I,I}|=m^{-2}\to0.
}
\tag{8.1}
\]

Thus no dimension-free statement of the form “three large eigenvalues imply one physical triple with determinant at least `c>0`” can connect Theorem 3.1 to the full conjecture. On this family the new bound grows like `m^{2/3}` even though other completed bank/diffuse mechanisms control the family uniformly. This is a counterexample to a structural shortcut, not to QFORM.

The first remaining global implication is therefore an **aggregate-before-inversion** statement: combine the determinant branch proved here with ridge/diffuse/grouped-coordinate machinery so that a cloud of tiny physical triple determinants is aggregated before paying any reciprocal determinant. Merely selecting the best triple cannot be universal.

## 9. Relation to the assigned partner result

The assigned partner fleet03/B14 r15 proved the pure off-diagonal case with the sharp-to-this-method constant `<13.585`. The present theorem shows that its determinant scaling is stable under arbitrary diagonal perturbations:

* if a diagonal becomes large relative to `Delta^(1/3)`, a scalar physical pivot plus the orientation-free rank-two half-Riesz theorem closes the block;
* if all diagonals stay small, the determinant identity forces one off-diagonal physical pair to be quantitatively indefinite, and the pair-log theorem plus the exact one-dimensional Schur coefficient closes the block.

So the partner's proposed “near-zero-diagonal stability theorem” is resolved in a stronger all-diagonal form, at the cost of a larger constant. The zero-diagonal theorem remains quantitatively better and independently useful.

## 10. Correction and scope audit

This proof preserves every required target hypothesis:

* active variables are original independent coordinates, never rotated independent surrogates;
* arbitrary outside coordinates are conditioned only as deterministic parameters;
* affine terms are retained and are covered uniformly;
* no moment, centering, identical-law, smoothness, compact-support, connected-support, log-concavity or fragment-count hypothesis appears;
* no law-uniform pointwise oscillatory-decay claim is used;
* no arbitrary-joint 3D coarea estimate is used;
* no positive moment of a vector-conditioned projection density is used;
* no scalar-`Q_rest` conditional density supremum is used;
* essential boundedness is proved in the stated branch; continuity of a representative is not claimed.

The full QFORM conjecture remains OPEN. A full proof still requires a dimension-free aggregate structural reduction for matrices such as (8.1), where global spectral rank is present but every useful fixed physical minor is small.

## 11. Numerical constants

The exact constants used above are

\[
128\,2^{1/4}=152.2185107203\ldots,
\qquad
16\,2^{1/4}=19.0273138400\ldots,
\]

and the determinant forcing contradiction in Case II is the exact rational inequality

\[
\frac18+2\left(\frac9{16}\right)^3+rac32\left(\frac9{16}\right)^2
=\frac{1957}{2048}<1.
\]

These are algebraic checks only; the proof is the analytic argument in Sections 4--6.
