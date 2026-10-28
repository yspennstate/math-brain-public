SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B13, 2026-09-23T20:01:30.753454Z.
attacking: the finite-hub diagonal-plus-symmetric-rank-two chamber from partner account03/B13 r33: absorb the retained rough Frobenius twist into a product-valid pair-volume estimate rather than delete it.

# account02/B13 — pair-volume half-potentials, single-bi-star obstruction, and rough-tail absorption

Programme: `QFORM-DENSITY-3EIG-20260922`. Role: extremal product laws / complementary constructions. Execution: `WITHOUT_VERIFIED_BRAIN`.

Status: **NEW PROVED FRACTIONAL-VOLUME THEOREM + NEW TARGET-LEVEL SCALAR-PIVOT BI-STAR DICHOTOMY + NEW ROUGH-TAIL HALF-POTENTIAL RECEIVER / FULL QFORM OPEN / CONTINUITY OPEN**.

The first unpaid implication after this run is:

`QFORM-SHARED-INPUT-THIRD-SMOOTHING-GLUE-v1`.

After the latest account03/B13 finite-hub reduction, the diffuse nondegenerate symmetric-rank-two carrier now absorbs the full `O(rho^{-3/2})` Frobenius twist inside a uniform half-potential estimate. What remains is to convert that half-potential into a density bound when the third smoothing direction shares original inputs with the rank-two carrier/hubs, or else route the localized/rank-one carrier branches through a paid physical pivot. No small quadratic remainder may be deleted on arbitrary fragmented/unbounded supports.

No moment, support, log-concavity, centered-law, single-interval, bounded-fragment-count, diagonal-basis, or post-rotation-independence assumption is used.

## 1. Fresh source state and exact dependencies


The required pinned source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

I read `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The completed ingredients used below are:

1. the `D_k` volume-decoupling estimate, including its Jensen parameter `q` and arbitrary self-block/outside/affine scope;
2. the fractional-potential inequality `H_alpha <= c_alpha int |t|^{alpha-1}|phi|`;
3. the scalar square peel `D(Q)<=|a|^{-1/2}H_{1/2}(Schur)`.

The pinned counterexample search reports no valid QFORM counterexample in the tested families. I do not use that numerical observation as proof.

### 1.1 Latest compatible designated partner

The latest completed account03/B13 result consumed here is

`math-open-problems@e9939918a958611972a1ab80c0d9160850fce276`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260923T193526Z-account03-B13-qform-r33/REPORT.md`,

with deterministic check output at `dfce2d8041ee087620868c485cfe0ecee2b188d0`.

Its theorem `QFORM-FINITE-HUB-SYMRANK2-RHO32-NORMAL-FORM-v1` says that if `s_3(A)>=1` and a slab has ratio `rho>c0=6sqrt(pi)`, then some set `H` of at most four original coordinates has complement `K` on which

`A[K,K]=D+R+E`,

where `D` is diagonal, `R` is symmetric of rank at most two, and `E` is symmetric zero-diagonal, with

`||E||_F <= Ksym eta^{-1/2} rho^{-3/2}`,

`eta=1-c0/rho`, `Ksym=474.83172596163683...`.

For `rho>=2c0`,

`||E||_F <= 671.5134666999717 rho^{-3/2}`.                 (1.1)

The report explicitly keeps `E` in the form: coefficient-small is not random-variable-small for arbitrary translated/fragmented product laws.

### 1.2 Product purification, no attainment

I also read the underlying account04/B13 proof

`math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260922T231352Z-account04-B13-rough-geometric-transfer-r5/REPORT.md`.

For every bounded measurable product kernel, the supremum over cap-one probability densities equals the supremum over indicators of unit-measure sets, and the latter supremum is unchanged when each set is restricted to a bounded finite union of intervals. This is equality of suprema by `L^1` approximation and finite convex mixtures, not an attained bathtub optimizer. No common support diameter or fragment count is obtained.

## 2. New theorem: pair-volume controls a half-potential up to every strict star threshold

Let `I,J` be disjoint original-coordinate banks and let

`M=A[I,J]`.

Put

`Z_2=e_2(M^T M)=sum_{|S|=|T|=2} det(M[S,T])^2>0`.        (2.1)

Under the natural squared-minor law

`w_{S,T}=det(M[S,T])^2/Z_2`,

write

`alpha_i=P_w(i in S)`, `i in I`.                         (2.2)

### Theorem 2.1 — `QFORM-D2-HALF-POTENTIAL-v1`

For every `h<1`, if

`max_i alpha_i <= h`,                                      (2.3)

then for the full quadratic polynomial

`Q=X^T A X+b^T X+c`,

with arbitrary blocks `A[I,I]`, `A[J,J]`, arbitrary remaining coordinates/couplings and arbitrary affine terms,

`H_{1/2}(Q):=sup_s E|Q-s|^{-1/2}`

satisfies

`boxed: H_{1/2}(Q) <= C_2(h) Z_2^{-1/8},`                 (2.4)

where

`C_2(h)=8 e^(1/4)` for `0<=h<=1/2`,                       (2.5)

and

`C_2(h)=4 e^(1/4)(2h)^(-1/4)/(1-h)` for `1/2<h<1`.       (2.6)

Thus a half-potential needs only a strict `h<1` pair-volume marginal gate. The density-level `D_3` theorem needs a substantially stronger exponent because a density requires more Fourier decay.

### Proof

The pinned `D_k` proof gives for general `k` and every `q>=1` with `q>=2 max alpha_i`

`E F^q <= e^{k/2}(2pi)^k q^{-k/2}|t|^{-k}Z_k^{-1/2}`,

after the physical decoupling and Brascamp--Lieb step. For `k=2`, taking square roots after the Cauchy--Schwarz decoupling yields

`|phi_Q(t)| <= B_q |t|^{-1/q}`,                           (2.7)

where

`B_q=[e(2pi)^2 q^{-1}Z_2^{-1/2}]^{1/(2q)}.`               (2.8)

Choose

`q=max(1,2h)<2`.                                           (2.9)

The pinned fractional-potential lemma, with `alpha=1/2`, `b=1/q` and `c_{1/2}=(2pi)^(-1/2)`, gives

`H_{1/2}(Q)`
` <= c_{1/2} [2b/{(1/2)(b-1/2)}] B_q^{(1/2)/b}`.          (2.10)

Since `(1/2)/b=q/2`,

`B_q^{q/2}=e^{1/4}(2pi)^{1/2}q^{-1/4}Z_2^{-1/8}`.         (2.11)

The `(2pi)^{1/2}` cancels `c_{1/2}`. Also

`2b/{(1/2)(b-1/2)}=8/(2-q)`.                              (2.12)

For `q=1`, this is (2.5). For `q=2h`, it is exactly (2.6). QED.

### Scope check

No quadratic term is deleted. In the pinned decoupling argument the self-blocks disappear from the differenced phase exactly, while the genuine physical cross block `M` remains. This is why (2.4) is safe for arbitrarily translated/unbounded product laws.

## 3. New target-level scalar-pivot theorem: pair-volume or one physical bi-star

Let `i` be an original coordinate with scalar pivot

`d=A_ii !=0`.

Complete the square in `X_i`. Let `S` be the exact Schur-complement quadratic matrix on the remaining original coordinates. Choose disjoint original-coordinate banks `I,J` in the complement of `i` and set

`M=S[I,J]`, `Z_2=e_2(M^T M)`.                              (3.1)

The pinned square peel and Theorem 2.1 give

`boxed: ||p_Q||_infinity <= C_2(h)|d|^{-1/2}Z_2^{-1/8}}`  (3.2)

whenever the natural pair-volume row marginals of `M` are at most `h<1`.

Applying the same theorem to `M^T` gives the identical bound when the column marginals are at most `h`.

### Anchored physical third-volume

For `P subset I`, `T subset J`, `|P|=|T|=2`, the bordered determinant identity is

`det A[{i} union P,{i} union T]=d det S[P,T]`.             (3.3)

Define

`W_{3,i}(I,J)`
` := sum_{|P|=|T|=2} det A[{i} union P,{i} union T]^2`
` = d^2 Z_2`.                                               (3.4)

The natural squared-minor law of `M` is exactly the normalized law of these anchored physical determinants.

Let a slab have ratio

`rho=P(Q in J0)/|J0|`.

Put the dimensionless anchored resource

`T_i := rho |d|^{1/4} W_{3,i}(I,J)^{1/8}`
`     = rho |d|^{1/2} Z_2^{1/8}.`                           (3.5)

### Theorem 3.1 — `QFORM-SCALAR-D2-SINGLE-BISTAR-v1`

If

`T_i >= 16 e^{1/4}=20.544406667003862...`,                  (3.6)

then there are a physical row `r in I` and physical column `c in J` such that, under the anchored squared-minor law,

`boxed: P(r in P and c in T) > 1 - 16 e^{1/4}/T_i.}`        (3.7)

Equivalently, any bad high-ratio witness obeys the dichotomy

* either

`W_{3,i}(I,J) < (16 e^{1/4}/rho)^8 |d|^{-2}`,               (3.8)

* or its anchored third-volume is quantitatively concentrated on one physical row and one physical column as in (3.7).

#### Proof

Write

`K=4e^{1/4}`.                                                (3.9)

Assume `T_i>=4K` and set

`epsilon=2K/T_i <=1/2`, `h=1-epsilon`.                      (3.10)

For `h>=1/2`, (2.6) gives

`C_2(h)=K(2h)^(-1/4)/epsilon <=K/epsilon=T_i/2`.             (3.11)

If all row marginals were at most `h`, (3.2) would imply

`T_i<=C_2(h)<=T_i/2`,                                       (3.12)

a contradiction. Hence some row marginal exceeds `h`. Apply the same argument to `M^T`; some column marginal exceeds `h`. If `A` and `B` are the two inclusion events under the common squared-minor law, inclusion-exclusion gives

`P(A cap B)>=P(A)+P(B)-1>2h-1=1-2epsilon`
` =1-4K/T_i=1-16e^{1/4}/T_i`.                              (3.13)

This proves (3.7). If (3.6) fails, (3.8) is just (3.5) rearranged. QED.

### What is new here

The previous third-volume structural alternatives only reached fixed marginal gates such as `<3/4`, or several row/column hubs. A half-potential needs less Fourier decay, so the pair-volume argument reaches **every strict gate `h<1`**. Consequently the only way a substantial scalar-Schur pair-volume can evade payment is asymptotic concentration on a single physical row and a single physical column.

This is a real inequality-level application of the required pinned Fourier source.

## 4. New rough-tail theorem for the partner's symmetric-rank-two survivor

The partner r33 survivor has the form, on a physical complement `K`,

`A[K,K]=D+R+E`,                                               (4.1)

with `D` diagonal, `R` symmetric of rank at most two, and `E` retained in the actual form.

The issue is that `||E||_F` small does not imply `X^T E X` small for arbitrary translated laws. The next theorem instead places `E` inside the actual physical cross block to which Theorem 2.1 is applied.

Assume for this section that `R` has rank exactly two, with spectral representation

`R=U Lambda U^T`, `U^T U=I_2`,                              (4.2)

and

`min(|lambda_1|,|lambda_2|)>=sigma>0`.                       (4.3)

Let the physical row leverage be

`ell_j=||U_{j,*}||_2^2`.                                     (4.4)

### Lemma 4.1 — physical random-cut paving in dimension two

If

`max_j ell_j<=delta<=1/32`,                                  (4.5)

there is a physical partition `K=I union J` such that, with

`G_I=U_I^T U_I`, `G_J=U_J^T U_J=I_2-G_I`,

one has

`lambda_min(G_I),lambda_min(G_J)>=g_delta`,                  (4.6)

where

`g_delta=(1-sqrt(2delta))/2 >=3/8`,                           (4.7)

and every normalized leverage in either bank is at most

`ell_j/g_delta <=1/12`.                                      (4.8)

#### Proof

Take independent signs `epsilon_j in {+1,-1}` and put

`S=sum_j epsilon_j u_j u_j^T`.                               (4.9)

Since the cross terms vanish after sign expectation,

`E||S||_F^2=sum_j ||u_j u_j^T||_F^2=sum_j ell_j^2`
` <=delta sum_j ell_j=2delta`.                               (4.10)

Hence some sign choice satisfies `||S||_op<=||S||_F<=sqrt(2delta)`. Taking `I={epsilon_j=+1}` and `J={epsilon_j=-1}` gives

`G_I=(I_2+S)/2`, `G_J=(I_2-S)/2`,                            (4.11)

which proves (4.6)-(4.7). The projection leverage of row `j` in bank `I` is `u_j^T G_I^{-1}u_j<=ell_j/g_delta`; similarly for `J`. QED.

### Theorem 4.2 — `QFORM-DIFFUSE-SYMRANK2-FROB-TWIST-HALFPOTENTIAL-v1`

Suppose (4.1)-(4.5) hold and

`||E||_F <= sigma g_delta/8`.                                (4.12)

Then, for the **full ambient quadratic polynomial**, including arbitrary physical hubs outside `K`, arbitrary hub-to-`K` couplings, arbitrary diagonal `D`, and arbitrary affine terms,

`boxed: H_{1/2}(Q) <= 64 e^{1/4}/sqrt(21 sigma)`
`                    <17.933 sigma^{-1/2}.`                  (4.13)

The matrix `E` is not deleted or replaced by a random error.

#### Proof

Choose the partition from Lemma 4.1. The actual physical cross block is

`M=A[I,J]=M_0+F`,                                             (4.14)

where

`M_0=U_I Lambda U_J^T`, `F=E[I,J]`.                          (4.15)

The diagonal part contributes no cross entries; arbitrary outside coordinates are not in this block.

Both nonzero singular values of `M_0` are at least

`a:=sigma g_delta`.                                          (4.16)

Indeed the smallest singular values of `U_I` and `U_J` are at least `sqrt(g_delta)`, while the smallest singular value of `Lambda` is at least `sigma`.

Also

`||F||_op<=||F||_F<=||E||_F=:epsilon<=a/8`.                  (4.17)

Weyl gives

`s_2(M)>=a-epsilon>=7a/8`.                                   (4.18)

Let `P_0` be the projection onto `range(U_I)`, and let `P` be the projection onto the top two left singular vectors of `M`. If `Y,V,S_2` are the corresponding truncated SVD factors, then

`(I-P_0)Y=(I-P_0)F V S_2^{-1}`.                              (4.19)

Therefore

`||P-P_0||_op <= x:=epsilon/(a-epsilon)<=1/7`.               (4.20)

Every diagonal entry of `P_0` is at most

`h_0:=delta/g_delta<=1/12`.                                  (4.21)

Thus

`P_{jj} <= (sqrt(h_0)+x)^2`.                                 (4.22)

Now use the pinned singular-vector formula for the natural `2`-volume row marginals of an arbitrary-rank matrix. If `s_m` are the singular values of `M` and

`p_m=s_m^2 sum_{l!=m}s_l^2 / e_2(s^2)`,                      (4.23)

then

`alpha_j=sum_m p_m u_m(j)^2`, `0<=p_m<=1`, `sum_m p_m=2`.   (4.24)

Let

`Ttail=sum_{m>=3}s_m^2`.                                     (4.25)

Since `M_0` has rank two, Eckart--Young gives

`Ttail<=||F||_F^2<=epsilon^2`.                               (4.26)

Put

`tau=sum_{m>=3}p_m`.                                         (4.27)

Writing `a_m=s_m^2`, the numerator in `tau` is at most

`Ttail(a_1+a_2)+Ttail^2`,                                   (4.28)

while the denominator is at least `a_1a_2`. Hence

`tau<=2 Ttail/a_2 +(Ttail/a_2)^2`
`   <=2x^2+x^4`.                                             (4.29)

Consequently every row marginal obeys

`alpha_j <= (sqrt(1/12)+1/7)^2+2/49+1/2401`
`          =0.22745292614134735... <1/2`.                   (4.30)

The same estimate holds on the column side, although only one side is needed.

Theorem 2.1 can therefore be used with `h=1/2`, giving

`H_{1/2}(Q)<=8e^{1/4} Z_2(M)^{-1/8}`.                        (4.31)

Since

`Z_2(M)=e_2(M^TM)>=s_1(M)^2s_2(M)^2>=s_2(M)^4`,             (4.32)

(4.18) implies

`Z_2(M)^{-1/8}<=(7a/8)^(-1/2)`.                              (4.33)

Using `g_delta>=3/8` gives

`H_{1/2}(Q)`
` <=8e^{1/4} sqrt(8/(7 sigma g_delta))`
` <=64e^{1/4}/sqrt(21 sigma)`
` =17.932628316095357... sigma^{-1/2}`.                       (4.34)

The full cross block `M=M_0+F` is used throughout, so the rough residual has been absorbed rather than perturbatively removed. QED.

### Why this handles the separated-support obstruction

The proof never estimates `X^TEX` in probability or moments. Arbitrary translations only modify affine terms after conditioning, and the pinned decoupling theorem is uniform in those terms. Smallness of `E` is used solely to prove that the **actual physical pair-volume geometry** of `M=R[I,J]+E[I,J]` retains two diffuse singular directions. Thus the earlier example where `||E||_F ->0` but `X^TEX` stays order one on remote supports does not challenge Theorem 4.2.

## 5. Actual application to the partner r33 high-slab survivor

For `rho>=2c0`, r33 gives (1.1). Suppose its complementary carrier has rank exactly two, both eigenvalues of modulus at least `sigma`, and maximum range leverage at most `1/32`.

Condition (4.12) is guaranteed once

`671.5134666999717 rho^{-3/2} <= 3 sigma/64`,                 (5.1)

i.e.

`rho >= 589.8509689968215 sigma^{-2/3}`.                     (5.2)

Therefore in this branch

`boxed: H_{1/2}(X^TAX+b^TX+c)<17.933 sigma^{-1/2}.}`         (5.3)

This is a target-level consequence for arbitrary cap-one product laws. The four physical hubs and all their couplings remain in the full ambient form and are simply part of the arbitrary outside structure permitted by Theorem 2.1.

The conclusion is a half-potential, not yet the desired density bound. That distinction is essential.

### Independent-square subbranch closes immediately

The current independently supplied `INDEPENDENT_V_BANK_THEOREM.md` at math-open-problems commit `010bf3c15ec09171b710b9c715077c5dc3805c32` proves the elementary convolution interface

`||p_{R+lambda V^2+gamma V+c}||_infinity`
` <= C |lambda|^{-1/2} H_{1/2}(R)`                            (5.4)

when the scalar square bank `V` is independent of the entire `R` bank and has density cap `C`.

Combining (5.3)-(5.4), whenever the r33 diffuse rank-two-plus-twist block is an independent bank from a scalar square direction,

`boxed: ||p_Q||_infinity <17.933 C (sigma |lambda|)^(-1/2).}` (5.5)

For an original scalar coordinate of cap one, `C=1`. For a unit projection of another independent cap-one bank, the Rogozin--Ball cap gives `C<=sqrt(2)`.

This is a scoped closure only. A general r33 hub may couple bilinearly to the rank-two bank, so it cannot be relabeled as the independent `V` in (5.4). That shared-input/coupled third smoothing direction is the first unpaid implication.

## 6. Extremal-law and counterexample consequences

The no-attainment purification theorem means that if the full QFORM conjecture is false, then for every strict bad slab ratio one may pass with arbitrarily small loss to a product of indicators of bounded finite unions of intervals of total measure one. The fragment count and diameter may diverge with the witness. Theorems 2.1, 3.1 and 4.2 require none of those localization parameters and therefore pass unchanged to such a counterexample sequence.

In particular, any hypothetical sequence with `rho_m -> infinity` now has the partner's at-most-four-hub normal form

`A_m[K_m,K_m]=D_m+R_m+E_m`,

`rank R_m<=2`, `rho_m ||E_m||_F ->0`,                         (6.1)

and must also obey:

* every usable scalar-Schur pair-volume is either of anchored size `O(rho_m^{-8}|d|^{-2})` or asymptotically concentrated on one physical row-column bi-star by Theorem 3.1;
* if the two nonzero eigenvalues of `R_m` stay above a scale `sigma_m` and its range is physically diffuse (`max leverage<=1/32`), then once `rho_m sigma_m^{2/3}->infinity` the **full retained rough form** has `H_{1/2}=O(sigma_m^{-1/2})` by Theorem 4.2;
* hence an escaping density counterexample in that diffuse branch must exploit a third smoothing resource that is coupled to the same original inputs, not merely the existence of the small Frobenius tail.

The remaining alternatives are now concrete: a rank-one/vanishing-second-eigenvalue carrier, a physically localized rank-two carrier, the genuine no-scalar-pivot chamber, or the shared-input third-smoothing glue above.

## 7. Source-validity notes

The pinned `COUNTEREXAMPLE_SEARCH.md` reports no valid counterexample and no tested peak growing with dimension; I use none of those numerics as proof.

The account03/B13 r33 checker reports zero violations in its finite deterministic tests, but Theorem 4.2 uses the analytic r33 statement, not the numerical checks as a premise.

The Fisher-information continuation was also read. It provides a strong full-matrix theorem under extra `H^1`/Fisher regularity but explicitly does not smooth arbitrary cap-one laws for free. No regularity hypothesis from that theorem enters this report.

## 8. Exact remaining gap

The unrestricted theorem and global continuity remain OPEN.

The next B13 obligation is `QFORM-SHARED-INPUT-THIRD-SMOOTHING-GLUE-v1`:

Starting from the r33 finite-hub normal form, use the new rough-tail half-potential receiver on the diffuse rank-two carrier and prove a dimension-free density bound when the remaining third spectral/smoothing direction is carried by one of the same physical coordinates or by a bilinearly coupled hub. A valid proof may use a mixed Fresnel/decoupling or rank-one-Schur exterior identity, but it must keep the actual `E` block, preserve original-coordinate product provenance, and cover the zero/near-zero scalar-pivot transition. If this fails, construct a genuine finite-union product-indicator counterexample satisfying all target hypotheses.
