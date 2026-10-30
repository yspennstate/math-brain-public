SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B15, 2026-09-24T09:15:16Z.
attacking: bounded-size physical localization versus diffuse spectral banks; quantify how many original coordinates are required to retain three curvatures, apply the full-law Fresnel theorem, and re-audit the ruled rough-input bridge.

# fleet02/B15 — bounded physical localization is quantitatively impossible on a uniformly bounded diffuse target family

Programme: QFORM-DENSITY-3EIG-20260922.  
Role: absolute continuity and regularity; complementary constructions/source-valid counterexamples.  
Status: NEW STRUCTURAL OBSTRUCTION / REQUIRED SOURCE APPLIED / PARTNER APPLIED / FULL QFORM OPEN.  
Execution: WITHOUT_VERIFIED_BRAIN.

## 1. First unpaid implication

The remaining B15 debt is not rough-input passage or output continuity. It is a product-preserving **aggregate-before-localization** statement: a universal proof must retain a diffuse bank of original coordinates until its collective spectral volume has been paid. The theorem below shows that no bounded number of physical coordinates can carry a uniform three-curvature certificate, even on a family whose full quadratic output has a universal density bound. The second part shows that an operator-small discarded tail cannot in general be justified by law/height continuity under the owner's unbounded-support hypotheses.

This is a proof-interface obstruction, not a counterexample to QFORM.

## 2. Diffuse three-bank target and exact principal-block spectrum

Fix `m>=2`. Split `3m` original independent coordinates into three disjoint banks and define

`u_1=m^{-1/2}(1,...,1,0,...,0)`,
`u_2=m^{-1/2}(0,...,0,1,...,1,0,...,0)`,
`u_3=m^{-1/2}(0,...,0,1,...,1)`

with disjoint supports of size `m`. Put

`A_m=u_1u_1^T+u_2u_2^T-u_3u_3^T`

so, in physical coordinates,

`A_m=J_m/m \oplus J_m/m \oplus (-J_m/m)`.

The vectors `u_1,u_2,u_3` are orthonormal, hence

`spec(A_m)={1,1,-1,0,...,0}`.                                      (2.1)

Thus this is an exact owner-target matrix for every `m`.

Let `S` be any physical coordinate subset of cardinality `r`, and let `k_j` be the number of selected coordinates in bank `j`. Then

`(A_m)_{S,S}=J_{k_1}/m \oplus J_{k_2}/m \oplus (-J_{k_3}/m)`.        (2.2)

Since `J_k` has one eigenvalue `k` and `k-1` zero eigenvalues, the nonzero eigenvalues of (2.2) are exactly

`k_1/m,  k_2/m,  -k_3/m`.                                           (2.3)

Consequently, writing `s_3(B)` for the third largest eigenvalue magnitude,

`s_3((A_m)_{S,S})=min(k_1,k_2,k_3)/m`,                              (2.4)

with the right side interpreted as zero when a bank is absent. Maximizing subject to `k_1+k_2+k_3=r` gives the exact formula

`boxed: max_{|S|=r} s_3((A_m)_{S,S})=floor(r/3)/m.`                  (2.5)

In particular, a physical principal block with three eigenvalue magnitudes at least `c>0` must contain at least

`boxed: |S| >= 3 c m`                                                (2.6)

original coordinates (up to the obvious integer rounding). Every fixed-size physical localization therefore has three-curvature scale tending to zero as `m->infinity`.

There is a complementary quantitative statement. If `S^c` denotes the omitted physical coordinates, then the three bank eigenvalues of `(A_m)_{S^c,S^c}` are

`(m-k_1)/m, (m-k_2)/m, -(m-k_3)/m`,

so

`boxed: s_3((A_m)_{S^c,S^c})=1-max(k_1,k_2,k_3)/m >= 1-r/m.`         (2.7)

For `r=o(m)`, a bounded physical localization therefore sees vanishing three-curvature while its complement retains asymptotically all three unit spectral directions. This is stronger than the earlier three-coordinate obstruction: no bounded physical dimension can serve as a universal localization scale.

## 3. Nevertheless the full output is uniformly bounded for arbitrary cap-one laws

For arbitrary independent cap-one inputs define the disjoint-bank sums

`Y_j=m^{-1/2} sum_{a in bank j} X_a`,

so

`Q_m=X^T A_m X=Y_1^2+Y_2^2-Y_3^2`.                                  (3.1)

The three variables `Y_1,Y_2,Y_3` are independent because their original-coordinate banks are disjoint. The one-dimensional Rogozin/Ball projection bound for a unit coefficient vector gives

`||p_{Y_j}||_infinity <= sqrt(2)`.                                  (3.2)

Therefore, for `s>0`,

`p_{Y_j^2}(s)=[p_{Y_j}(sqrt(s))+p_{Y_j}(-sqrt(s))]/(2sqrt(s))
             <= sqrt(2)/sqrt(s)`.                                   (3.3)

Convolving the first two same-sign squares gives, pointwise for `t>0`,

`p_{Y_1^2+Y_2^2}(t)
 <=2 int_0^t [u(t-u)]^{-1/2} du
 =2 pi`.                                                            (3.4)

Convolution with the independent probability law of `-Y_3^2` cannot increase `L^infinity`, hence

`boxed: ||p_{Q_m}||_infinity <= 2 pi`                               (3.5)

for every `m` and for every admissible cap-one product law. This is an essential-height estimate obtained directly from convolution; continuity is not used.

Thus the ratio between the best bounded-size physical three-curvature scale and the actual output-height control diverges: for fixed `r`, the local scale is only `floor(r/3)/m`, while the full law remains bounded by `2pi`.

## 4. Required e5f71d79... result applied to the same full law

I independently applied the completed Fresnel--Brascamp--Lieb Theorem F from
`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`.

Write

`A_m=sum_{j=1}^3 lambda_j u_j u_j^T`, `lambda=(1,1,-1)`,

and take the theorem's coordinate set `I` to be all `3m` coordinates and its residual matrix `B=0`. The row vector `rho_i` of the spectral frame has squared norm `1/m`; moreover

`G_I=sum_i rho_i rho_i^T=I_3`.

Hence every normalized leverage is

`rho_i^T G_I^{-1} rho_i=1/m<=1/2`,

and `det G_I=1`. Theorem F therefore gives the actual full-output inequality

`boxed: ||p_{Q_m}||_infinity <= 12`                                 (4.1)

uniformly in `m` and in all cap-one input laws. The direct bank convolution (3.5) improves the constant to `2pi`; (4.1) is an independent payment using the required completed source rather than a restatement of its hypotheses.

The same required source's ruled Theorem C also gives on the majority sheet

`boxed: P(Q_m in I, Q_m>=0) <= pi sqrt(2) |I|`                       (4.2)

for every interval `I`. This will be used below only as an interval-height statement; no continuity premise is imported.

## 5. Same-family obstruction to bounded localization plus operator-small truncation

The newest designated partner fleet03/B15 result
`QFORM-OPNORM-RANKCOLLAPSE-TV-HEIGHT-BARRIER-v1`
shows that small matrix operator norm is not a law/height continuity mechanism under arbitrary remote cap-one supports, even modulo deterministic output translation. Its proof mechanism can be applied verbatim to the diffuse bank family above, producing one family where the two structural failures coexist.

Adjoin one more original coordinate and put

`A_{m,0}=A_m \oplus [0]`,
`A_{m,e}=A_m \oplus [e]`,                                           (5.1)

where

`0<e<min(delta,m^{-2})`.

Both matrices remain exact owner targets and

`||A_{m,e}-A_{m,0}||_op=e<delta`.                                   (5.2)

For a physical subset `S` of size `r`, the nonzero eigenvalues of `(A_{m,e})_{S,S}` are a subcollection of

`k_1/m, k_2/m, -k_3/m, e`.

Hence

`boxed: s_3((A_{m,e})_{S,S}) <= max(floor(r/3)/m,e).`                (5.3)

So every fixed-size physical carrier still degenerates as `m->infinity`.

Now specialize the three banks to iid `Uniform[-1/2,1/2]`. Then

`Y_j in [-sqrt(m)/2,sqrt(m)/2]`,

and therefore the base output

`Q_{m,0}=Y_1^2+Y_2^2-Y_3^2`

is supported on

`E_m=[-m/4,m/2]`, `|E_m|=3m/4`.                                    (5.4)

Let the added independent coordinate be

`X_0~Uniform[R,R+1]`,

choose

`L >= 3m/(4 eta)`, `R=L/(2e)`,                                     (5.5)

and write `Z=eX_0^2`. Since the map `x -> e x^2` is increasing on that interval,

`p_Z(z)=1/(2 sqrt(ez)) 1_[eR^2,e(R+1)^2](z)`,

so

`||p_Z||_infinity=1/(2eR)=1/L`.                                    (5.6)

The perturbed output is

`Q_{m,e}=Q_{m,0}+Z`,

with independent summands, hence

`boxed: ||p_{Q_{m,e}}||_infinity <= 1/L <= 4 eta/(3m).`              (5.7)

For every deterministic translation `c`, the translated perturbed law still has density cap `1/L`; therefore

`(tau_c Law(Q_{m,e}))(E_m) <= |E_m|/L <= eta`,

whereas `P(Q_{m,0} in E_m)=1`. Thus

`boxed: inf_{c in R} d_TV(Law(Q_{m,0}), tau_c Law(Q_{m,e})) >= 1-eta.`  (5.8)

Equations (5.2), (5.3), and (5.8) give a single diffuse target family with both features:

1. every bounded physical localization has vanishing three-curvature scale; and
2. an arbitrarily small additional operator coefficient cannot be discarded by any law-uniform continuity principle, even after arbitrary output recentering.

Again, this is not a QFORM counterexample. In fact both outputs are harmless in height: (3.5) bounds the unperturbed law by `2pi`, and (5.7) makes the perturbed law even flatter. The obstruction is specifically to a proof architecture that first localizes to `O(1)` physical coordinates and then throws away the remaining operator-small part by output-law continuity.

The partner's key affine-amplification identity is visible here too: writing `X_0=R+U`,

`eX_0^2=eR^2+L U+eU^2`.                                             (5.9)

Thus tiny quadratic curvature can create an arbitrarily large random affine scale because supports are unrestricted. Any valid tail absorber must therefore be uniform in conditioning-generated translations; operator norm alone is insufficient.

## 6. Independent audit of the ruled geometry and rough-input bridge

The required ruled theorem is a smooth geometric statement first, so the rough passage must be made at the interval-measure level rather than by evaluating an arbitrary rough density on a ruling.

For the standard signature `(1,1,-1)` form

`q_0(z)=z_1^2+z_2^2-z_3^2`,

use the ruling

`F(theta,t)=sqrt(s)e_theta+t(e_theta^perp+e_3)`, `s>=0`.

A direct differentiation gives

`F_theta x F_t=(1/2) grad q_0(F)`,

and hence the coarea quotient is exactly

`boxed: d sigma/|grad q_0|=(1/2) dtheta dt.`                         (6.1)

After spectral scaling with curvature magnitudes `(lambda_1,lambda_2,mu)`, the ruling direction is

`v_theta=(-sin(theta)/sqrt(lambda_1),
           cos(theta)/sqrt(lambda_2),
           1/sqrt(mu))`.                                            (6.2)

The parameter `t` is not arclength, so the line estimate contributes the indispensable reciprocal speed `1/|v_theta|`. The two-dimensional product-projection cap `2` then cancels the coarea factor `1/2`, recovering exactly

`C_+=(lambda_1 lambda_2 mu)^(-1/2)
      int_0^{2pi} [sin^2(theta)/lambda_1+cos^2(theta)/lambda_2+1/mu]^(-1/2) dtheta`.  (6.3)

For `lambda_1,lambda_2,mu>=1`, this gives `C_+<=pi sqrt(2)`.

Now consider an ambient form and condition on all outside original coordinates `W=w`. If the active physical `3x3` block `B` is invertible, then

`Q_w(x)=x^T Bx+2d(w)^T x+c_0(w)
       =(x+B^{-1}d(w))^T B(x+B^{-1}d(w))+c(w)`.                     (6.4)

Thus the affine-range condition is automatic in this scope, and square completion is a deterministic translation in the **original independent coordinates**, not a rotation to spectral coordinates.

For arbitrary rough active marginals, let `f_i^(eta)=f_i*rho_eta` with a nonnegative probability approximate identity. Then

`0<=f_i^(eta)<=1`, `int f_i^(eta)=1`,

and the product telescoping identity gives

`||prod_i f_i^(eta)-prod_i f_i||_1
 <= sum_i ||f_i^(eta)-f_i||_1 ->0`.                                 (6.5)

For each fixed outside value `w`, translate both the smooth and rough active product laws by the same vector `B^{-1}d(w)`. Translation preserves the `L^1` error. Restriction to the fixed conditional majority event and deterministic quadratic pushforward both contract total variation. Therefore, if the smooth positive-sheet submeasure obeys

`nu_eta(I)<=C_+(B)|I|`,

then letting `eta->0` gives directly

`boxed: nu(I)<=C_+(B)|I|`                                           (6.6)

with **zero loss**. The cone boundary creates no hidden atom: the zero set of the nonzero quadratic polynomial is Lebesgue-null. No pointwise trace of a rough `L^infinity` representative and no output continuity is used anywhere in (6.5)--(6.6).

This confirms the ruled/rough-input bridge in exactly the corrected invertible-active-block scope.

## 7. Regularity ledger

**Absolute continuity.** If `A!=0` and the joint input has an absolutely continuous density, then the pushforward by `q(x)=x^T A x+b^T x+c` is absolutely continuous. The affine critical set `{2Ax+b=0}` is empty or a proper affine subspace. On `{|grad q|>=1/k}`, coarea sends the inverse image of every one-dimensional null set to a null set; exhausting the complement of the critical set proves absolute continuity. This is qualitative and gives no universal height.

**Essential boundedness.** In this run it is paid by interval/convolution/Fourier inequalities: (3.5), the required-source estimate (4.1), the ruled submeasure estimate (4.2)/(6.6), and the perturbed convolution estimate (5.7). None uses continuity.

**Continuity.** Any current fixed-instance `C_0` compiler is downstream: it may be invoked only after a finite interval-height constant has been proved. It cannot repair the localization obstruction (2.5) or the operator-perturbation obstruction (5.8).

## 8. Exact remaining implication

The bank family proves that a universal argument cannot extract a bounded number of original coordinates carrying three uniformly large curvatures: the number required at scale `c` is at least `3cm`. The partner barrier proves that a residual operator-small term cannot then be discarded by a law/height continuity argument under arbitrary remote supports.

The surviving route must therefore do at least one of the following **before inversion/localization**:

- aggregate a growing diffuse coordinate bank into a product-valid grouped receiver;
- pay a projected crossing/volume/Fresnel quantity that remains uniform as physical minors vanish; or
- retain the tail exactly in a translation-uniform receiver.

For B15, the first unpaid implication is to obtain such an aggregate estimate also on the complementary convex/two-sheet side (the live generic-X-ray shortcut is unavailable), or to connect every remaining higher-rank matrix to another already-paid product-preserving receiver.

Full QFORM remains OPEN.