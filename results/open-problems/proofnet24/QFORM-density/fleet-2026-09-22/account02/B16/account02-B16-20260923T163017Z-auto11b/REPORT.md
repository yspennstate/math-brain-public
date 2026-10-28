SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B16, 2026-09-23T16:30:17Z.
attacking: the true-near-coloop small-innovation endpoint—first cancel the longitudinal leakage exactly in the nonzero-hub Schur complement, then test whether any translation-uniform square peel or projected-crossing certificate can survive the punctured null limit without retaining the original hub source weight.

# account02/B16 — diffuse Schur remainder and an admissible near-null square-envelope barrier

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `NEW SUPPORTING THEOREM + TARGET-VALID MECHANISM OBSTRUCTION / FULL QFORM OPEN`  
**Regularity:** the new estimates below establish essential density bounds in their stated scopes; no new global continuity claim is made.  
**Owner continuation consumed during this run:** `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`.  

## 1. First unpaid implication

The exact target remains open: arbitrary finite dimension, independent original-coordinate real variables with one-dimensional densities at most one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No support, moment, log-concavity, identical-law, diagonal-basis, post-rotation-independence, or continuity hypothesis is introduced.

The newest completed designated-partner input actually applied here is account03/B16 r30,

`yspennstate/math-open-problems@3b18a20df2659c5c26d6853e69ceae081a3abc7e`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260923T162348Z-account03-B16-QFORM-r30/REPORT.md`.

After its already-paid exits, the true-near-coloop exact-rank-three survivor has a physical hub row of leverage above `63/64`, every residual transverse row has squared norm below `1/64`, and the leaves can be split into two genuine original-coordinate banks with transverse Grams between `I_2/4` and `3I_2/4`. Its newer projected-crossing exit pays the branch when a bank's full three-dimensional Gram determinant `nu_B` is not too small; the remaining state has two small longitudinal innovations that cannot simply be deleted for unbounded source laws.

The new conclusion of this run is that, for a nonzero hub pivot, **all transverse rank-two curvature is already uniformly quantitative after exact Schur completion**. The only singularity left by that route is the scalar near-null translation. A fully admissible target family then shows that replacing the translating original-coordinate hub density by its height cap creates a logarithmic divergence even while the true density stays below a universal constant. Thus the next implication is

**`QFORM-TWO-BANK-SMALL-INNOVATION-SOURCE-ADAPTED-HUB-v1`:** retain the two small longitudinal innovations inside the unnormalised original-product hub translation until the order-one transverse curvature has been paid, or obtain the missing half-power by a phase-sensitive crossing estimate before taking absolute values. A theorem depending only on the Schur-remainder law plus a translation-uniform square envelope cannot be uniform.

This is closely aligned with the newest Claude continuation `c4c23b784395630c094ba299a50712209921d1ae`, whose adapted-hub functional `(SP)` is still explicitly OPEN for arbitrary cap-one product inputs. The independently checked Gaussian/scale-mixture continuation at `math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401` proves restricted adapted-hub cases and also proves that projection-density caps alone cannot settle `(SP)`; none of those restricted positive results is promoted here to the arbitrary-law endpoint.

## 2. Source-valid completed inputs used at equations

The required pinned package is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

I use three completed pieces from it:

1. the two-dimensional product-projection theorem: an orthonormal two-dimensional projection of independent cap-one original coordinates has joint density at most `2`; this is never upgraded to independence of the two projected coordinates;
2. the fractional-potential estimate: if `|phi_Z(t)| <= min(1,B/|t|)`, then
   `H_{1/2}(Z):=sup_s E|Z-s|^{-1/2} <= 8 B^{1/2}/sqrt(2 pi)`;
3. its localized three-variable theorem A: for three independent cap-one variables, a real symmetric `3 x 3` quadratic matrix whose eigenvalues all have modulus at least `sigma`, with arbitrary linear terms, has output density at most `6 sqrt(pi)/sigma`.

I also apply the newest checked projected-crossing theorem from

`math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

For one genuine original hub and projected crossing two-volume `Z_2` with its row-marginal gate, it gives the continuous-density estimate

`||p_Q||_infinity < 9.4 (|w_J|^2 Z_2)^(-1/6)`.

The partner r30 exact Pluecker identity inserts this theorem into the actual near-coloop bank geometry below.

## 3. New theorem: the hub Schur remainder is a uniformly diffuse rank-two form

### `QFORM-HUB-SCHUR-DIFFUSE-CROSS2-v1`

Let

`A=R Lambda R^T`, `R^T R=I_3`,

with the three eigenvalues of `Lambda` all of modulus at least one. Suppose one physical row is

`r_0=sqrt(c) e`, `c>63/64`,

and write every leaf row as

`r_j=s_j e+w_j`, `w_j perpendicular e`,

with

`||w_j||^2<1/64` for every leaf. Parseval gives

`sum_j w_j w_j^T=I_2`,
`sum_j s_j w_j=0`.

Write `Lambda` in the spectral splitting `R e direct-sum e^perp` as

`Lambda=[[alpha,b^T],[b,C]]`.

Then `A_00=c alpha`. Assume `A_00 !=0`. Let `W` be the leaf matrix whose rows are `w_j`, and let `s` be the column of longitudinal coefficients. The leaf-hub coupling is

`ell=A_{L0}=sqrt(c)(alpha s+Wb)`.

The exact Schur complement of the hub is

`S=A_LL-ell ell^T/A_00`.

A direct expansion gives the identity

`boxed: S=W K W^T,  K=C-bb^T/alpha.`                               (3.1)

Every occurrence of the longitudinal leakage row `s` cancels. This is exact, not perturbative.

Because a nonzero scalar Schur pivot removes one dimension from an exact-rank-three form, the completed Schur-complement interlacing lemma leaves two eigenvalues of modulus at least one in `S`. Since `W^T W=I_2`, the two nonzero eigenvalues of `S` are those of `K`. Hence

`boxed: |lambda_1(K)|,|lambda_2(K)|>=1,  |det K|>=1.`              (3.2)

### A deterministic two-bank partition

Give each leaf an independent Rademacher sign and set

`H=sum_j epsilon_j w_j w_j^T`.

Then

`E ||H||_F^2=sum_j ||w_j||^4
 <=(1/64) sum_j ||w_j||^2
 =1/32`.                                                           (3.3)

Thus some signing has

`||H||_op<=||H||_F<=1/sqrt(32)<1/4`.

Let `I` and `J` be the positive and negative sign banks. Their transverse Gram matrices are

`G_I=(I_2+H)/2`, `G_J=(I_2-H)/2`,

so in particular

`boxed: G_I,G_J >=(3/8) I_2.`                                     (3.4)

For the Schur cross block

`M=S_{I,J}=W_I K W_J^T`,

its two nonzero singular values satisfy the exact product identity

`s_1(M)s_2(M)=|det K| sqrt(det G_I det G_J) >=9/64.`               (3.5)

The preceding account02/B16 theorem `QFORM-CROSS2-ARBITRARY-SELFBLOCK-L32-v1` is source-valid for arbitrary same-side curvature and uses only the joint two-dimensional projection cap on each disjoint original-coordinate bank. It therefore gives

`|phi_S(t)|
 <=min(1, 2pi/(|t| sqrt(s_1s_2)))
 <=min(1,16pi/(3|t|)).`                                            (3.6)

Applying the pinned fractional-potential theorem to (3.6),

`boxed:
 H_{1/2}(S)
 <=8(64/9)^(1/4)
 =13.0639452948... .`                                              (3.7)

Finally the pinned scalar square peel at the physical hub pivot gives

`boxed:
 ||p_Q||_infinity
 <=13.0639452949 / sqrt(|A_00|).`                                  (3.8)

This is not the desired near-null endpoint because it diverges as `A_00 ->0`. Its value is structural: after exact completion, neither transverse degeneracy nor projected dependence is responsible for that divergence. The only unpaid quantity is the translating source hub itself.

## 4. A fully shared target family inside the true near-coloop collar

The following family tests that remaining interface without introducing a pure transverse atom.

Let

`0<delta<1/64`, `c=1-delta`,

let `m>=512` be divisible by four, and choose sign pairs

`(epsilon_j,tau_j) in {+1,-1}^2`

so that all four pairs occur exactly `m/4` times. Define the Parseval rows

`r_0=(sqrt(c),0,0)`,

`r_j=m^(-1/2)(sqrt(delta),epsilon_j,tau_j)`.                       (4.1)

Then `R^T R=I_3`. For `epsilon>0`, put

`b=sqrt(1+epsilon)`,

`Lambda_epsilon=[[epsilon,b,0],[b,0,0],[0,0,1]].`                 (4.2)

Its eigenvalues are exactly

`boxed: {1+epsilon,-1,1},`                                        (4.3)

because `sqrt(epsilon^2+4(1+epsilon))=epsilon+2`. Therefore

`A=R Lambda_epsilon R^T`

is an exact-rank-three member of the target for every `epsilon>0`.

For arbitrary independent cap-one original inputs define

`T=m^(-1/2)sum_j X_j`,
`U=m^(-1/2)sum_j epsilon_j X_j`,
`V=m^(-1/2)sum_j tau_j X_j`,

and

`Y=sqrt(c)X_0+sqrt(delta)T`.

Then

`boxed: Q_epsilon=epsilon Y^2+2 sqrt(1+epsilon) YU+V^2.`           (4.4)

The pair `(U,V)` is an orthonormal two-dimensional projection of the same leaf product law. It generally has dependent coordinates; no independence between `U` and `V` is asserted or used.

### 4.1 The family passes the physical superdiffuse gates

The physical entries are

`A_00=c epsilon`,

`A_0j=sqrt(c)/sqrt(m) [epsilon sqrt(delta)+b epsilon_j]`,

`A_jj=m^(-1)[1+epsilon delta+2b sqrt(delta) epsilon_j]`.           (4.5)

For `m>=512`, `delta<1/64`, and, say, `epsilon<2^-13`, these obey the inherited small diagonal/star gates. The normalized hub-star atom is

`p_j=
 [epsilon sqrt(delta)+b epsilon_j]^2 /
 [m(epsilon^2 delta+b^2)]
 <2/m<=1/256<1/251.`                                               (4.6)

More strongly, every hub-leaf physical pair is indefinite with the exact determinant

`boxed: det A[{0,j}]=-c/m.`                                       (4.7)

Thus the negative hub-pair mass is order one and diffuse across all leaves, exactly the kind of resource used in partner r30.

For a balanced half-bank `B` containing equal numbers of all four sign pairs,

`sum_(j in B) r_j r_j^T
 =diag(delta/2,1/2,1/2)`,

so partner r30's full-bank determinant is

`boxed: nu_B=delta/8.`                                            (4.8)

Its transverse Gram is exactly `G_B=I_2/2`.

With `D=|det Lambda_epsilon|=1+epsilon`, partner r30's exact projected-crossing identity gives

`||A_{0,B}||^2 Z_2
 =D^2 c det(G_{B^c}) nu_B
 =D^2 c delta/32.`                                                 (4.9)

Hence the newest completed one-hub projected-crossing theorem yields the legitimate estimate

`boxed:
 ||p_Q||_infinity
 <9.4 [D^2 c delta/32]^(-1/6).`                                   (4.10)

This is an actual application of the latest projected-crossing result to a surviving physical partition. It deteriorates like `delta^(-1/6)`. If

`D^2 delta/8<2^-12`,                                               (4.11)

then **both** balanced banks lie exactly in partner r30's remaining two-small-innovation state. Thus (4.10) does not close the endpoint, exactly as the theorem's stated scope warns.

## 5. Exact Schur completion on the stress family

For `epsilon>0`, complete the physical hub square in (4.4). The coefficient of `X_0^2` is `c epsilon`, and one obtains the exact identity

`Q_epsilon
 =c epsilon [X_0+(epsilon sqrt(delta)T+bU)/(epsilon sqrt(c))]^2
 +S_epsilon`,                                                      (5.1)

with

`boxed:
 S_epsilon=V^2-[(1+epsilon)/epsilon] U^2.`                         (5.2)

Again the weak longitudinal aggregate `T` cancels completely from the Schur remainder. The two-dimensional remainder actually becomes *more* curved as `epsilon` tends to zero.

The translation-uniform cap-one square envelope at level `t` is

`K_epsilon(t)
 =(c epsilon)^(-1/2)
  E[(t-S_epsilon)^(-1/2) 1_{S_epsilon<t}].`                        (5.3)

The next theorem shows that this exact envelope nevertheless diverges.

## 6. New obstruction: the translation-uniform square envelope diverges logarithmically in the actual hard chamber

### `QFORM-TRUE-NEARCOLOOP-SQUARE-ENVELOPE-LOG-BARRIER-v1`

Take, for this subsection only, iid leaf laws `Unif[-1/2,1/2]`; take the hub law cap-one as well. For fixed balanced `m>=512`, the genuine product projection `(U,V)` has a continuous joint density `rho_m` which is strictly positive in a neighbourhood of `(0,0)`. Thus there are constants `r_m,kappa_m>0` such that

`rho_m(u,v)>=kappa_m` whenever `|u|,|v|<=r_m`.                     (6.1)

Set

`k=sqrt(epsilon/(1+epsilon))`.

At `t=0`, (5.3) becomes

`K_epsilon(0)
 =1/sqrt(c(1+epsilon))
  E[(U^2-k^2V^2)^(-1/2) 1_{|U|>k|V|}].`                            (6.2)

For `k<1/8`, integrate only over

`r_m/2<=v<=r_m`,
`2kr_m<=u<=r_m/2`.

On this rectangle `u>k|v|` and

`(u^2-k^2v^2)^(-1/2)>=1/u`.

Therefore

`boxed:
 K_epsilon(0)
 >= [kappa_m r_m/(2 sqrt(c(1+epsilon)))]
      log(1/(4k))
 ->infinity`                                                       (6.3)

as `epsilon->0`.

So even the **exact one-sided translation-uniform square envelope**, after the Schur remainder has become a perfectly nondegenerate rank-two quadratic form, loses logarithmically in the punctured null limit.

This does not contradict boundedness of the true density. The square peel has replaced the actual translated source factor

`f_0(-[epsilon sqrt(delta)T+bU]/[epsilon sqrt(c)]
     +/-sqrt((t-S_epsilon)/(c epsilon)))`

by the height bound one. On the rectangle producing (6.3), the translation is typically of order `U/epsilon`; the true original-product weight therefore contains information which the envelope has discarded. This is the same source-provenance issue isolated abstractly by the newest adapted-hub work, now embedded in a strict three-large-eigenvalue product-source family and simultaneously in partner r30's two-small-innovation chamber.

The obstruction is to a proof mechanism, not to QFORM.

## 7. The same family has a universal true-density bound below 176

The crucial comparison is that the actual target family is uniformly harmless for **every** independent cap-one source law.

Group the leaf coordinates by their four sign pairs. For `sigma=(epsilon,tau)` define

`Z_sigma=(2/sqrt(m)) sum_(j in B_sigma) X_j`.

Each coefficient vector has Euclidean norm one, so the one-dimensional product-projection theorem gives

`||p_{Z_sigma}||_infinity<=sqrt(2)`.                               (7.1)

The four `Z_sigma` are genuinely independent because they use four disjoint original-coordinate banks.

Condition on all original coordinates in the `(-,+)` and `(-,-)` banks. The remaining random variables enter only through the three independent source objects

`X_0, Z_(+,+), Z_(+,-)`.

Their spectral coefficient columns are

`p_0=(sqrt(c),0,0)`,

`p_+=(sqrt(delta)/2,1/2,1/2)`,

`p_-=(sqrt(delta)/2,1/2,-1/2)`.                                   (7.2)

Scale the two bank variables by

`W_+=sqrt(2) Z_(+,+)`, `W_-=sqrt(2) Z_(+,-)`,

so all three active variables have density cap one. With

`P'=[p_0,p_+/sqrt(2),p_-/sqrt(2)]`,

one has

`|det P'|=sqrt(c)/4`,                                              (7.3)

and the conditional three-variable quadratic matrix is

`B'=P'^T Lambda_epsilon P'`.

Hence

`|det B'|=c(1+epsilon)/16`.                                        (7.4)

Also `P'P'^T<=I_3`, because these active source contributions are a subcollection of the full Parseval decomposition after only shrinking two columns. Therefore

`||B'||_op<=||Lambda_epsilon||_op=1+epsilon`.

For a symmetric `3 x 3` matrix, the smallest singular value is at least determinant divided by the square of the operator norm, so every eigenvalue of `B'` has modulus at least

`boxed:
 sigma_min(B')
 >= c/[16(1+epsilon)]
 >63/1040.`                                                       (7.5)

Now apply the **required pinned completed Theorem A** from

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837/COUNTEREXAMPLE_SEARCH.md`.

It allows arbitrary affine terms generated by the conditioned banks and gives

`||p_(Q_epsilon | conditioned banks)||_infinity
 <=6 sqrt(pi)/sigma_min(B')`

`<6 sqrt(pi) (1040/63)
 =175.5573338039...`.                                              (7.6)

Averaging the conditioning proves the uniform target-level inequality

`boxed:
 ||p_{Q_epsilon}||_infinity<176`                                  (7.7)

for every `m>=512`, every admissible `delta,epsilon` above, and **every choice of independent cap-one original source laws**.

This is the required real application of a completed result from the pinned `e5f71d79...` package. The two bank variables are independent only because their ORIGINAL coordinate sets are disjoint; nowhere are the coordinates of `(U,V)` treated as independent.

For the exact signature `(+, +, -)`, the pinned ruled theorem C also supplies its sharper one-sheet estimate `p_Q(s)<=pi sqrt(2)` on its stated side and hypotheses. That geometric statement is supplementary; (7.7) is the all-level bound used here.

## 8. What this changes

The current B16 near-coloop picture is now more specific.

- Partner r30 and the newest projected-crossing theorem pay any balanced bank with quantitative full three-dimensional innovation. On the fully shared family above, that certificate is exactly of order `delta^(-1/6)` and can be forced into the remaining small-innovation chamber.
- Exact nonzero-hub Schur completion annihilates the longitudinal leakage and leaves a uniformly diffuse rank-two transverse form; there is no hidden transverse singularity left to find.
- Nevertheless, the translation-uniform square peel diverges logarithmically as the spectral hub pivot tends to zero, while the true density stays below `176` for every source law.

Therefore the missing resource is **the location of the original hub density relative to the same-bank projected translation**, not another determinant lower bound for the Schur remainder. A successful next step must keep that source weight, or equivalently its phase, until the small longitudinal innovation and the transverse curvature are paid jointly. The newest Claude `(SP)` formulation and its Gaussian-mixture proof are relevant templates, but `(SP)` for arbitrary cap-one product laws remains open and is not assumed here.

Arbitrary additional spectrum remains a separate global interface after this exact-rank-three near-coloop branch. The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

## 9. Source and correction boundary


The newest projected-crossing checkpoint and the newest adapted-hub Gaussian/obstruction checkpoint were read at the source-pinned reviewed bundle `math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`. They are supporting theorems, not a full proof.
