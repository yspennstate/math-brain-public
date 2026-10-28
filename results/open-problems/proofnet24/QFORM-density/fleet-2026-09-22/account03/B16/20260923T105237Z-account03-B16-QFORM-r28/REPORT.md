SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-23T10:52:37Z.
attacking: derive a dimension-free structural bridge from the near-coloop shared-bank geometry to either a fresh-square atom or a two-source determinant bank, using the partner fixed-pair mass identity quantitatively.

# account03/B16 r28 — XOR-balanced basis law closes the leakage-dominant branch away from the true coloop

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Run:** `20260923T105237Z-account03-B16-QFORM-r28`  
**Status:** `NEW SUPPORTING THEOREM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Regularity:** the new paid branch has a continuous `C_0` density. The full target and global continuity remain open.

## 1. Source boundary and inherited hard chamber

The owner target is unchanged: for arbitrary finite `n`, independent real original-coordinate variables with densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal bound for the density of `X^T A X`, or give a valid counterexample.


The analytic input is account01/B18 `QFORM-FRESNEL-CAPPED-BASIS-WEIGHTS-v1`, canonical source

`yspennstate/math-open-problems@8c04ccbc1f032d1a82ad505223f08e3c344bde74`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/20260922T225705Z-qform-B18-a01-r19/REPORT.md`.

It states: if `A=R Lambda R^T`, `R^T R=I_3`, and there is a probability law `w` on nonsingular physical three-coordinate bases whose coordinate marginals are all at most `1/2`, then with

`Z_w=exp(H(w)+sum_S w_S log det(R_S)^2)`

one has, for arbitrary independent cap-one original-coordinate inputs and arbitrary affine terms,

`||p_Q||_infinity <=3e (|det Lambda| Z_w)^(-1/3)`,               (1.1)

and the density is continuous and vanishes at infinity.

The B16 predecessor `20260923T035222Z-account03-B16-QFORM-r25` fixed one physical row

`r_i=sqrt(c)e`, `a=1-c`,

and wrote every residual row as

`r_k=s_k e+w_k`, `w_k perpendicular e`, `h_k=||w_k||^2`,

with exact Parseval identities

`sum_(k!=i) s_k^2=a`,
`sum_(k!=i) w_k w_k^T=I_2`,
`sum_(k!=i) s_k w_k=0`.                                          (1.2)

Its balanced basis law paid the branch

`h_k+s_k^2/(2a)<=1/2 for every k!=i`.                             (1.3)

If (1.3) fails at `j`, and the preceding transverse escape has already imposed `h_j<1/64`, then

`s_j^2/a>1-2h_j>31/32`.                                          (1.4)

The purpose of this run is to show that this failure is itself still paid by a different capped basis law whenever `a` is not in the genuine near-coloop collar.

## 2. Exact four-category Pluecker ledger

Let

`v_S=det(R_S)^2`, `|S|=3`.

Cauchy--Binet gives `sum_S v_S=1`, so `v` is the natural volume-sampling basis law. Fix the gate-failing `j`, abbreviate

`s=s_j`, `w=w_j`, `h=||w||^2`,

and let `K` denote the remaining indices outside `{i,j}`.

The exact two-coordinate category masses are

`P_v(i in S, j in S)=c h`,                                       (2.1)

`P_v(i in S, j notin S)=c(1-h)=:P_10`,                          (2.2)

`P_v(i notin S, j in S)=s^2+a h=:P_01`,                         (2.3)

`P_v(i notin S, j notin S)=a(1-h)-s^2`.                         (2.4)

Equation (2.3) follows from `P_v(j in S)=s^2+h` and (2.1). The gate failure (1.4) implies

`P_01=s^2+a h>a(1-h)`.                                           (2.5)

Thus both XOR classes in (2.2)-(2.3) have positive mass.

## 3. New XOR-balanced basis law

Define a probability law `w^xor` on physical bases by discarding the `00` and `11` classes and putting half of the probability on each XOR class:

`w^xor_S = v_S/(2P_10)` if `i in S, j notin S`,

`w^xor_S = v_S/(2P_01)` if `i notin S, j in S`,

and `w^xor_S=0` otherwise.                                       (3.1)

Immediately

`alpha_i=alpha_j=1/2`.                                           (3.2)

The nontrivial point is that every remaining marginal is much smaller than `1/2` despite the original duplicated gate failure.

### Theorem 3.1 — `QFORM-XOR-BALANCED-BASIS-v1`

Assume

`0<h<1/64`, `h_k<1/64` for every `k in K`,                       (3.3)

and the duplicated gate fails at `j`:

`h+s^2/(2a)>1/2`.                                                 (3.4)

Then every coordinate marginal of `w^xor` is at most `1/2`. In fact, for every `k in K`,

`alpha_k <95/4032 <1/40`.                                        (3.5)

Its determinant-entropy score is exactly

`boxed: Z_xor=2 sqrt(c(1-h)(s^2+a h))`,                          (3.6)

and therefore, using (3.4),

`boxed: Z_xor>2(1-h)sqrt(ca)`.                                   (3.7)

Consequently the exact-rank-three quadratic form has a continuous `C_0` density satisfying

`boxed:
 ||p_Q||_infinity
 <=3e [2(1-h)sqrt(ca)|det Lambda|]^(-1/3).`                      (3.8)

The same statement permits arbitrary affine terms.

### Proof

#### 3.1. The class `10`

Condition on a volume-sampled basis containing `i` but not `j`. Since

`det(r_i,r_k,r_l)^2=c det(w_k,w_l)^2`,                            (3.9)

the remaining pair is exactly two-dimensional volume sampling from the frame `{w_k:k in K}`. Its Gram matrix is

`G_10=sum_(k in K) w_k w_k^T=I_2-w w^T`.                         (3.10)

Because `h<1`, `G_10` is positive definite and

`G_10^(-1) <=(1-h)^(-1) I_2`.                                   (3.11)

The conditional inclusion probability of coordinate `k` is the ordinary leverage

`m_k^(10)=w_k^T G_10^(-1) w_k
 <=h_k/(1-h)
 <(1/64)/(63/64)=1/63`.                                         (3.12)

#### 3.2. The class `01`

Gate failure implies `s!=0`. For every `k in K` define the adjusted transverse row

`u_k=w_k-(s_k/s)w`.                                              (3.13)

Subtracting `(s_k/s)r_j` from `r_k` inside a determinant gives

`det(r_j,r_k,r_l)=s det(u_k,u_l)`.                               (3.14)

The exact Gram of the adjusted frame is

`U=sum_(k in K) u_k u_k^T=I_2+(a/s^2) w w^T`.                    (3.15)

Indeed, from (1.2), after deleting `i,j`,

`sum_K w_k w_k^T=I_2-w w^T`,
`sum_K s_k w_k=-s w`,
`sum_K s_k^2=a-s^2`,

and direct expansion of (3.13) yields (3.15). Hence `U>=I_2` and

`U^(-1)<=I_2`.                                                    (3.16)

Cauchy--Binet gives

`sum_(k<l in K) det(r_j,r_k,r_l)^2
 =s^2 det U
 =s^2+a h=P_01`,                                                 (3.17)

so the conditional `01` law is exactly two-dimensional volume sampling from `{u_k}`. Thus

`m_k^(01)=u_k^T U^(-1)u_k<=||u_k||^2`.                           (3.18)

From (3.4),

`a-s^2<2a h`,                                                     (3.19)

and therefore, for every `k in K`,

`|s_k/s|^2 <=(a-s^2)/s^2
 <2h/(1-2h)`.                                                     (3.20)

Using `sqrt(h_k)<1/8` and `sqrt(h)<1/8`,

`||u_k||
 <=sqrt(h_k)+|s_k/s|sqrt(h)
 <1/8+h sqrt(2/(1-2h))`.                                         (3.21)

At `h<=1/64`, the second term is at most `1/(8sqrt(31))`; hence

`m_k^(01)
 <[(1+1/sqrt(31))/8]^2
 <1/32`.                                                          (3.22)

#### 3.3. Marginals

The XOR law mixes the two conditional laws with weights `1/2,1/2`, so for `k in K`,

`alpha_k=(m_k^(10)+m_k^(01))/2
 <(1/63+1/32)/2
 =95/4032
 <1/40`.                                                         (3.23)

Together with (3.2), every marginal is at most `1/2`.

#### 3.4. Determinant-entropy score

On the `10` half of the law,

`v_S/w^xor_S=2P_10`,

while on the `01` half,

`v_S/w^xor_S=2P_01`.

Therefore

`log Z_xor
 =1/2 log(2P_10)+1/2 log(2P_01)`,                               (3.24)

which proves

`Z_xor=2sqrt(P_10 P_01)
      =2sqrt(c(1-h)(s^2+a h))`.                                  (3.25)

Using (2.5),

`Z_xor>2(1-h)sqrt(ca)`.                                          (3.26)

Now apply `QFORM-FRESNEL-CAPPED-BASIS-WEIGHTS-v1` to obtain (3.8) and continuity. QED.

## 4. Quantitative closure of the old gate-failure branch

Return to the r24/r25 hard chamber. There the already-proved reductions supply

`c>c_*:=643/7936`,                                                (4.1)

`h_k<1/64` for every residual coordinate,                         (4.2)

and `|det Lambda|>=1`.                                            (4.3)

Suppose additionally

`a=1-c>=1/64`.                                                     (4.4)

If the duplicated gate succeeds, r24 already gives

`||p_Q||_infinity<18.7`.                                         (4.5)

If it fails, Theorem 3.1 gives, since `1-h>63/64`,

`||p_Q||_infinity
 <3e[(63/32)sqrt(c_* /64)]^(-1/3)
 =19.7824763991...<19.8`.                                        (4.6)

Hence the duplicated-gate dichotomy is now completely paid whenever `1-c>=1/64`.

### Corollary 4.1 — `QFORM-R24-GATE-FAILURE-CLOSED-AWAY-FROM-COLOOP-v1`

Inside the exact-rank-three r24 residual chamber, after the existing partner/cross-pair exits, if

`1-c>=1/64`,

then the quadratic form has a continuous density with

`boxed: ||p_Q||_infinity<19.8`.                                  (4.7)

Therefore the only surviving branch of that B16 reduction has

`boxed: c>63/64`,                                                 (4.8)

i.e. a genuine physical near-coloop. The previous separate "leakage-dominant second coordinate" obstruction is no longer an independent branch.

This is a structural improvement rather than a new easy subclass: it removes the only non-coloop failure mode of the product-Fresnel gate in the inherited hard chamber.

## 5. Designated partner account04/B16 applied to an actual inequality

The designated partner theorem is account04/B16 `QFORM-RULED-PLUECKER-ENDPOINT-v1`, canonical report

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260922T231542Z-account04-B16-QFORM-r1/REPORT.md`.

For exact rank three it proves, with `D=|det Lambda|` and `d` the disjoint Pluecker-basis probability,

`||p_Q||_infinity <=12 D^(-1/3)d^(-1/6)`.                        (5.1)

Thus the actual threshold used by the B16 compiler gives

`d>=1/64
 => ||p_Q||_infinity
 <=12 D^(-1/3) 64^(1/6)
 <=24`.                                                          (5.2)

The new XOR argument is used only after this partner exit and after the transverse-pair exit `h_k>=1/64`. Hence the partner result is inserted into the actual branch inequality, not merely cited.

## 6. What remains

The exact-rank-three B16 obstruction is now narrower:

`QFORM-TRUE-NEAR-COLOOP-CLOSURE-v1`.

After all currently paid exits, one may assume

`c>63/64`,                                                        (6.1)

all residual transverse leverages are `<1/64`, and the old leakage-dominant/gate-failure alternative has been absorbed by Theorem 3.1 whenever `1-c>=1/64`.

In this true near-coloop collar the determinant-entropy score of any basis law with marginal `alpha_i<=1/2` must pay the rarity of bases avoiding `i`; the capped-basis route therefore naturally loses a power of `1-c`. A new mechanism must use the genuine original-coordinate near-coloop scalar directly. The sign-free dependent-pair/fresh-square theorem from B16 r27 pays this collar whenever a disjoint fresh square with quantitative `|b det B|` can be extracted. What remains is the shared-bank endpoint where no such physical scalar atom is quantitatively available.

Arbitrary additional spectrum remains a separate full-target interface. No claim here proves the unrestricted theorem or the global continuity conclusion.

## 7. Verification checklist

The accompanying deterministic checker verifies:

1. `95/4032<1/40<1/2`;
2. `[(1+1/sqrt(31))/8]^2<1/32`;
3. the exact score lower bound used in (4.6);
4. `3e[(63/32)sqrt((643/7936)/64)]^(-1/3)=19.7824763991...<19.8`;
5. the designated-partner threshold `12*64^(1/6)=24`.

No numerical experiment is used as evidence for the theorem; the checker only validates finite arithmetic appearing in the symbolic proof.
