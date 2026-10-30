SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B14, 2026-09-23T07:03:36Z.
attacking: translation-safe aggregate localization—derive an unnormalized kernel-leakage/mixture inequality that survives fragmented and unbounded product laws, then test it against the latest partner and Fourier-volume exits.

# QFORM-DK-SUBPROBABILITY-HOMOGENEITY-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `fleet02/B14`  
Run: `20260923T070336Z-fleet02-B14-QFORM-r27`  
Status: **PROVED SUPPORTING LOCALIZATION THEOREM + TARGET-VALID PROOF-ORDER OBSTRUCTION; FULL QFORM OPEN.**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication and sources actually applied

The B14 obligation is to retain arbitrary translations, conditioning-generated affine terms, distant fragments and unbounded supports without moments. The first unpaid localization question is:

> If a surviving matrix has a valid Claude cross-volume certificate, may one first split the active product law into small fragments/fibres, invoke the volume theorem on each normalized/local piece, and then sum without paying a fragmentation tax?

This report proves the exact homogeneity of the volume certificate on product subprobabilities. The answer is **no in general**: the volume theorem loses precisely a fraction `alpha_i/k` of one mass power on row coordinate `i` and `beta_j/k` on column coordinate `j`. If all volume-active coordinates are split into `N` equal pieces, the black-box certificate loses exactly `N^2`, independently of the volume order `k` and independently of the Holder/Jensen parameter used to relax the marginal gate.

Three completed sources are used at equations.

1. Claude Fourier/volume source `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. Its `FOURIER_ROUTE_REPORT.md` proves the general `D_k` calculation, including `D'` and the no-marginal-gate `D_5` theorem, and its `RESULTS.md` proves the underlying decoupling/Brascamp--Lieb determinant argument.
2. The same source proves the cap-one Fourier `L^p` lemma

   `int |fhat|^p <= 4 pi / sqrt(p),   p>=2`,

   for a probability density `f<=1`.
3. Designated partner fleet03/B14 r29, `yspennstate/math-open-problems@f79df5706245c49d305aa7cfcf0e4c70f9c6e8de`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260923T063425Z-fleet03-B14-QFORM-r29/REPORT.md`, proves the whole-bank square theorem

   `||p_Q||_infinity <= |c|^{-1} H(2|c|/(|d|||a||_2^2))`

   for `Q=2cX_1X_2+(d/2)(a^T V-beta)^2+` arbitrary affine pair terms, uniformly over all rough supports and outside conditioning. Section 6 below applies it to a genuinely diffuse, arbitrarily fragmented target-valid bank.

No rotation is used to create independent coordinates. Every conditioning step below is on original coordinate blocks. No support radius, fragment count, location, moment or log-concavity parameter occurs.

## 2. A subprobability Fourier lemma with the exact mass power

Let `0<=f<=1` be an integrable one-dimensional subdensity with mass

`m=int f in (0,1]`.

For every `p>=2`,

`boxed( int_R |fhat(s)|^p ds <= (4 pi/sqrt(p)) m^(p-1). )`            (2.1)

### Proof

Define `h(y)=f(my)`. Then `0<=h<=1` and

`int h(y)dy = m^{-1} int f(x)dx =1`,

so `h` is a cap-one probability density. The change of variables `x=my` gives

`fhat(t)=m hhat(mt)`.

Therefore

`int |fhat(t)|^p dt = m^(p-1) int |hhat(s)|^p ds`,

and the completed Claude `L^p` lemma for `h` proves (2.1). QED.

This scaling is exact for intervals and is the source of the mass exponents below.

## 3. Main theorem: exact subprobability homogeneity of `D_k`

Let `I,J` be disjoint sets of original coordinates and let `M=A_{I,J}`. On `I union J`, let

`nu(dx)=prod_{i in I} f_i(x_i) prod_{j in J} f_j(x_j) dx`,

where `0<=f_l<=1` and

`m_l=int f_l in (0,1]`.

Let `Q` be any real quadratic polynomial whose `I x J` cross block is `M`; the self blocks on `I` and `J` and all affine and constant terms are arbitrary.

Fix an integer `k>=1` with

`Z_k=e_k(M^T M)=sum_{|S|=|T|=k} det(M_ST)^2 >0`.

Let

`w_ST=det(M_ST)^2/Z_k`

be volume sampling and write

`alpha_i=P_w(i in S),    beta_j=P_w(j in T)`.

Thus

`sum_i alpha_i=sum_j beta_j=k`.                                     (3.1)

Choose `q` such that

`q>=1,    q<k/2,    alpha_i<=q/2 for every i`.                       (3.2)

Put

`a=k/(2q)>1`,

`C_(k,q)=2 sqrt(e) [a/(a-1)] q^(-1/2)`.                              (3.3)

### Theorem 3.1 — `QFORM-DK-SUBPROBABILITY-HOMOGENEITY-v1`

The pushforward finite measure `Q_#nu` has a bounded continuous density and

`boxed(
 ||p_(Q#nu)||_infinity
 <= C_(k,q) Z_k^(-1/(2k))
    prod_{i in I} m_i^(1-alpha_i/k)
    prod_{j in J} m_j^(1-beta_j/k).
 )`                                                                  (3.4)

The exponent of every mass is independent of `q`.

### Proof

Let

`Phi(t)=int exp(itQ(x)) dnu(x)`.

The trivial bound is

`|Phi(t)|<=W:=prod_{i in I}m_i prod_{j in J}m_j`.                    (3.5)

Use Cauchy--Schwarz in the original `I` coordinates exactly as in Claude `D_k`. The self-quadratic and affine terms on `I` cancel inside the modulus; after expanding the square, the remaining `J` phases have modulus one. Hence

`|Phi(t)|^2
 <= m_I int_R^J prod_{i in I}|fhat_i(2t(Mw)_i)| prod_{j in J} g_j(w_j) dw`, (3.6)

where

`m_I=prod_{i in I}m_i`,

and

`g_j=f_j * f_j_tilde`.

Each `g_j` has mass `m_j^2` and

`||g_j||_infinity <= ||f_j||_infinity ||f_j||_1 <= m_j`.             (3.7)

Set

`F(w)=prod_i |fhat_i(2t(Mw)_i)|`.

The product measure `prod_j g_j(w_j)dw` has total mass `m_J^2`, where `m_J=prod_jm_j`. Holder on this finite measure gives

`int F prod_jg_j
 <= (int F^q prod_jg_j)^(1/q) m_J^(2-2/q)`.                   (3.8)

Apply the same volume-sampling Brascamp--Lieb determinant bound as in Claude `D_k` to `F^q`. For the row input indexed by `i`, use (2.1) with

`p=q/alpha_i>=2`.

After the change of frequency variable,

`(int |fhat_i(2ts)|^(q/alpha_i) ds)^alpha_i
 <= (4pi/(2|t|))^alpha_i (alpha_i/q)^(alpha_i/2)
    m_i^(q-alpha_i).`                                                (3.9)

For a column input, interpolation between (3.7) and its `L^1` mass gives

`||g_j||_(1/(1-beta_j))
 <= m_j^beta_j (m_j^2)^(1-beta_j)
 =m_j^(2-beta_j).`                                                    (3.10)

The Gaussian Brascamp--Lieb determinant constant is the same one used in the probability proof,

`Z_k^(-1/2)
 prod_i alpha_i^(-alpha_i/2)
 prod_j(1-beta_j)^(-(1-beta_j)/2).`                                  (3.11)

The `alpha_i` factors in (3.9) cancel those in (3.11), `sum alpha_i=k`, and

`prod_j(1-beta_j)^(-(1-beta_j)/2) <= exp(k/2)`                       (3.12)

because `-x log x<=1-x` and `sum beta_j=k`. Therefore

`int F^q prod_jg_j
 <= e^(k/2)(2pi/|t|)^k q^(-k/2) Z_k^(-1/2)
    prod_i m_i^(q-alpha_i) prod_j m_j^(2-beta_j).`                   (3.13)

Combining (3.6), (3.8), (3.13) and taking square roots gives

`|Phi(t)|
 <= B_(k,q) |t|^(-a)
    prod_i m_i^(1-alpha_i/(2q))
    prod_j m_j^(1-beta_j/(2q)),`                                     (3.14)

where

`B_(k,q)=e^(k/(4q))(2pi)^(k/(2q))q^(-k/(4q))Z_k^(-1/(4q))`.

Because `a>1`, (3.5) and (3.14) imply `Phi in L^1`. The elementary exact integral

`int_R min(W,C|t|^-a)dt
 =2[a/(a-1)] C^(1/a) W^(1-1/a)`                                     (3.15)

and Fourier inversion give a continuous output density. For coordinate `i`, its total mass exponent after (3.15) is

`(1-alpha_i/(2q))/a + 1-1/a
 =1-alpha_i/k`,                                                       (3.16)

and similarly for `j`. The numerical factors simplify to (3.3). This proves (3.4). QED.

### Checks against the completed probability theorems

If every `m_l=1`, (3.4) is exactly Claude's probability `D_k` theorem. For `k=3`, taking `q=2h` gives

`C_(3,2h)=6sqrt(e)(2h)^(-1/2)(3-4h)^(-1)`,

which is `D'`. For `k=5`, `q=2` gives

`C_(5,2)=5sqrt(2e)`,

which is the no-marginal-gate `D_5` theorem.

## 4. Product-fragment localization formula and its sharp homogeneity threshold

Suppose each coordinate subdensity is decomposed into disjoint or nondisjoint positive pieces

`f_l=sum_r f_(l,r)`,

with masses

`m_(l,r)=int f_(l,r),    sum_r m_(l,r)=1`,

and one applies Theorem 3.1 separately to every Cartesian product cell and then sums the output-density bounds. Since the matrix certificate is unchanged from cell to cell, the total black-box certificate is multiplied by

`boxed(
 T=
 prod_{i in I}[sum_r m_(i,r)^(1-alpha_i/k)]
 prod_{j in J}[sum_r m_(j,r)^(1-beta_j/k)].
 )`                                                                  (4.1)

This has two immediate consequences.

### 4.1 Safe-coordinate localization

A fragmented row coordinate is **zero-tax** exactly when its volume marginal `alpha_i=0`; then its factor in (4.1) is `sum_r m_(i,r)=1`. Likewise a column coordinate is zero-tax when `beta_j=0`.

Hence a D_k certificate is fully compatible with arbitrary localization/conditioning of coordinates outside its volume support, including arbitrary translations and unbounded/distant fragments. The active volume coordinates, however, must remain aggregated through reciprocal volume payment unless a different estimate restores the missing mass powers.

This gives a precise version of “select the analytic active core before localizing its law.”

### 4.2 Equal-fragment tax is always `N^2`

If every volume-active coordinate is split into `N` equal-mass pieces, then (4.1) equals

`N^{sum_i alpha_i/k + sum_j beta_j/k}=N^2`,                           (4.2)

using (3.1). This is independent of the volume order `k` and independent of `q`.

Thus increasing the exterior-volume order, or using the Jensen relaxation `D'`, cannot by itself repair active-coordinate fragment normalization. The loss is a homogeneity issue, not a bad-marginal-gate issue.

For unequal fragment masses, (4.1) is the exact product of Renyi-type sums. Arbitrarily many tiny fragments can make it arbitrarily large, with no reference to support diameter or moments.

## 5. Target-valid Claude `D_5` obstruction: direct payment is constant, fragment-first payment is `N^2`

This section applies a completed newest-Claude theorem to a real obstruction.

Take ten original independent coordinates, split into `I={1,...,5}` and `J={6,...,10}`, and let

`Q=2 sum_{r=1}^5 X_r X_(5+r)`.                                       (5.1)

Its symmetric matrix is

`A=[[0,I_5],[I_5,0]]`,

whose spectrum is `+1` and `-1`, each with multiplicity five. It therefore satisfies the exact QFORM spectral hypothesis with room to spare.

For the cross block `M=I_5`,

`Z_5=e_5(M^TM)=1`.

Claude `D_5` applies directly to **every** cap-one product law, with no marginal condition, and gives

`boxed( ||p_Q||_infinity <= 5sqrt(2e). )`                             (5.2)

This already retains arbitrary disconnected or unbounded supports and all affine terms generated by outside conditioning.

Now choose, for every active coordinate, the cap-one probability density `1_(E_N)` where

`E_N=union_{r=1}^N [L_r,L_r+1/N]`,                                   (5.3)

and the locations `L_r` may be arbitrarily far apart. Decompose each marginal into its `N` interval subdensities. Every product cell has ten marginal masses `1/N`. Since for `M=I_5` there is only one nonzero fifth-order minor,

`alpha_i=beta_j=1`.

Theorem 3.1 gives the unnormalized density bound for one cell

`5sqrt(2e) (1/N)^(10*4/5)
 =5sqrt(2e) N^-8.`                                                    (5.4)

There are `N^10` cells. Summing the cellwise black-box bounds therefore produces

`boxed( 5sqrt(2e) N^2, )`                                            (5.5)

whereas direct whole-law `D_5` remains (5.2).

This is **not a counterexample to QFORM and not a counterexample to D_5**. It is an exact proof-order obstruction: partitioning/normalizing the active product law before the reciprocal exterior-volume payment can destroy a uniform certificate even in a matrix for which the whole-law theorem is already dimension-free and support-free.

The same construction works with arbitrarily distant fragments; no compactness or moment issue is involved.

## 6. Complementary partner application: a diffuse rank-one bank is paid before localization

The newest designated partner result fleet03/B14 r29 shows the opposite, positive behavior when the active geometry can be compressed as a whole bank.

Let `N>=1`,

`a_N=sqrt(2/N)(1,...,1) in R^N`,

and let `X_1,X_2,V_1,...,V_N` be independent cap-one variables with **arbitrary** fragmented or unbounded supports. Consider

`Q_N=2X_1X_2 + (1/2)(a_N^T V-beta)^2
     + ell_1X_1+ell_2X_2+gamma`,                                     (6.1)

where `beta,ell_1,ell_2,gamma` are arbitrary real parameters, or arbitrary measurable functions of further outside original coordinates after conditioning.

The homogeneous active matrix has nonzero eigenvalues

`1,-1,(1/2)||a_N||_2^2 =1`.                                         (6.2)

Thus (6.1) is target-valid although every individual bank coefficient is `sqrt(2/N)->0`.

Partner r29 has

`theta=2/(||a_N||_2^2)=1`,

so its proved theorem gives, uniformly in every parameter in (6.1),

`boxed( ||p_(Q_N)||_infinity <= 4+2log 8 = 8.158883083... . )`        (6.3)

Conditioning on arbitrary outside coordinates only changes the displayed affine/translation parameters, so averaging preserves exactly the same constant. In particular (6.3) remains true if every `V_j` is uniform on a union of arbitrarily many arbitrarily separated intervals of total length one.

This is a real application of the completed partner theorem to the live localization problem: a diffuse bank that would be disastrous under single-coordinate selection is harmless if its scalar projection is aggregated **before** reciprocal pair-log payment.

## 7. The localization principle that survives the full rough-law target

Sections 3--6 separate two notions that must not be conflated.

**Safe full-mass mixture/localization.** If an analytic theorem gives the same interval bound `C|J|` for every full cap-one product probability law in a class, then convex mixtures of those laws preserve `C` exactly. Full-mass finite-fragment extreme-product localization is therefore compatible with the target whenever the analytic certificate is applied to each full probability component with the same matrix hypotheses. Arbitrary support locations and fragment counts are harmless.

**Unsafe active fragment normalization.** If instead a full marginal is first partitioned into small subprobability fragments and the reciprocal D_k certificate is paid separately on every Cartesian cell, the exact multiplier is (4.1); it can be unbounded and is `N^2` for equal fragmentation of all volume-active coordinates.

**Safe outside conditioning.** Coordinates outside the selected original-coordinate D_k active block may be conditioned/localized freely. They generate arbitrary affine terms in the active variables, and Claude D_k/D'/D_5 are uniform in those affine terms. The same is true for partner r29's whole-bank square theorem. Hence no moment or support bound on outside translations is required.

This is the target-compatible localization rule:

> **choose and pay the product-preserving active curvature/volume/bank certificate on whole active marginals; only then condition/localize outside variables. Do not normalize active thin fragments before reciprocal payment unless a separate theorem restores one full subprobability-mass power.**

## 8. What changes and the first unpaid implication

The calculation proves that the previously observed `N^2` failures of fragment-first `D_3`/`D_k` arguments are not artifacts of a special conjugate-fibre example. They are the exact universal homogeneity of the Brascamp--Lieb volume certificate:

`mass exponent = 1 - (volume marginal)/k`.                            (8.1)

The Holder/Jensen parameter does not alter (8.1), and raising `k` does not alter the total two-sided deficit `2`.

The first unpaid implication is therefore sharpened to:

**`QFORM-WHOLE-ACTIVE-CERTIFICATE-OR-MASS-RESTORATION-v1`.** In every surviving N3/no-pivot configuration, expose before active-law fragmentation either

1. a D'/D_5/near-diffuse volume certificate on whole original-coordinate active marginals;
2. a whole-bank pair/square/ridge certificate such as fleet03/B14 r29; or
3. a genuinely new unnormalized positive-copy/kernel-leakage estimate whose local bound carries at least one full power of every newly introduced subprobability mass through reciprocal inversion.

A bounded support reduction, fixed fragment count, moment estimate, post-rotation independence assertion, or “small coefficient means small random perturbation” cannot substitute for this step.

Full QFORM remains OPEN. This report neither proves nor disproves the unrestricted conjecture. It proves a supporting localization theorem and refutes a specific proof ordering inside the exact target.

## 9. Independent-review status

Theorem 3.1 and the derived localization obstruction are new supporting results in this run and have not received the two independent end-to-end reviews required for a full solution. The Claude and partner inputs are used only at their proved scopes.
