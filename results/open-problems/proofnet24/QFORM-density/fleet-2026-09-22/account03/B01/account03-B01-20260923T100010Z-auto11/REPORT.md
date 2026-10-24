SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B01, 2026-09-23T10:00:10Z.
attacking: upgrade the rank-two curved-bicore plus source-disjoint square receiver from one L3 exponent to a full translation-uniform Lp family, optimize it to logarithmic weak-square loss, and transfer the result to signed Fejer.

# account03/B01 — source-disjoint square Lp compiler and logarithmic receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `account03-B01-20260923T100010Z-auto11`  
Classification: `PROVED SUPPORTING TARGET-LEVEL ANALYTIC THEOREM / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: the new branch has a continuous `C_0(R)` density.

## 1. Exact target and correction boundary

The unrestricted target remains open: for every dimension, every family of independent real inputs with probability densities at most one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal essential bound for the density of `X^T A X`, or give a target-valid counterexample.

The phase-aligned fragmented-support correction remains binding. For any prescribed `s>0` and small `delta>0`, the set

`{x : dist(s x^2,2 pi Z)<=delta}`

has infinite Lebesgue measure. Choose a finite union `E` inside it with `|E|=1` and set `f=1_E`. Then

`Re int exp(i s x^2) f(x) dx >= cos(delta)`.

Hence no law-uniform positive-power pointwise scalar Fresnel decay can hold under only `f<=1`. Nothing below asserts such a bound. The proof uses a joint rank-two physical cross estimate only under a time integral, and spends an independent square through its full `L^p(dt)` norm.

Fresh control at the start was `yspennstate/math-research-brain@76c1df03ebf6db6627bf678b5c34bdf99e781d2d`, OWNER CONTROL revision `2026-09-22.15`; prepublication refresh was `yspennstate/math-research-brain@47bd085011f5a75f5d6d2fec80120d9fce0db532`, with the same owner revision and QFORM-only scope. The live correction inbox blob remained `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`.

Source-pinned inputs actually used:

1. This slot's preceding source-disjoint square theorem, `yspennstate/math-open-problems@ba000d70d1d4f523a2396155a24d5088d5c94802`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T073210Z-auto11/REPORT.md`. It proves the joint rank-two cross envelope with arbitrary curvature on both active banks and the `p=3` square closure.
2. This slot's translated scalar Fresnel work, source-pinned at `yspennstate/math-open-problems@c65e53a795f4f47c223a21698549857342bd1b5f`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T052757Z-auto11/REPORT.md`. The present report rederives the scalar-square `L^p` estimate with a sharper constant, so no challenged pointwise statement is imported.
3. Designated partner account04/B01, canonical `yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`, proving the exact signed-Fejer identity `||p_mu||_infinity=sup_(T,y) D_T mu(y)` with the extended-value convention.
4. The source-valid one-dimensional product-projection bound used throughout the current proof tree: for independent cap-one coordinates and `a!=0`, `||p_(a^T X)||_infinity<=sqrt(2)/||a||_2`.

A source search before publication found the previous `L^3` source-disjoint-square receiver and the different overlapping/transverse `L^p` receiver, but no completed source-disjoint-square full-`L^p` logarithmic optimization matching the theorem below.

## 2. Setup

Partition the ORIGINAL independent coordinates into pairwise disjoint banks `I,J,D,W`. Condition on `X_W=w`. Assume the conditional form can be written

`Q_w = F_w(X_I)+G_w(X_J)+2 X_I^T K X_J`
`      + lambda (a^T X_D+h(w))^2+c(w)`,                            (2.1)

where

* `K` has exact rank two, with nonzero singular values `kappa_1>=kappa_2>0`;
* `a!=0`, `sigma=||a||_2`;
* `lambda!=0`;
* `F_w,G_w` are arbitrary real measurable functions (in QFORM they may contain all same-bank quadratic self-curvature and affine leakage);
* `h(w),c(w)` are arbitrary.

Put

`Delta=kappa_1 kappa_2`,                                          (2.2)
`rho=|lambda| sigma^2`.                                           (2.3)

The only structural restriction is source disjointness of the square bank `D` from the two active cross banks and the exact decomposition (2.1). There is no moment, support, log-concavity, connected-support, Gaussian, identical-law, or post-rotation independence assumption.

## 3. Joint rank-two cross envelope

The predecessor projected-Plancherel argument is recalled because it is the first half of the new compiler. Take a thin SVD

`K=P diag(kappa_1,kappa_2) R^T`,                                  (3.1)

and set `U=P^T X_I`, `V=R^T X_J`. The banks `I,J` are independent original-coordinate banks. Their two-dimensional projection densities are bounded by two. If

`A_(t,w)(u)=p_U(u) E[e^{itF_w(X_I)} | U=u]`,
`B_(t,w)(v)=p_V(v) E[e^{itG_w(X_J)} | V=v]`,                      (3.2)

then `||A_(t,w)||_2,||B_(t,w)||_2<=sqrt(2)`. Two-dimensional Plancherel applied only to the physical cross phase therefore gives

`|psi_w(t)| <= min{1, 2 pi/(|t| sqrt(Delta))}.`                    (3.3)

This is JOINT in the two banks and remains valid with arbitrary curvature in both `F_w` and `G_w`; it is not a product of false scalar pointwise Fresnel estimates.

## 4. Sharper translation-uniform scalar-square `L^p` theorem

### Lemma 4.1 — `QFORM-SCALAR-SQUARE-LP-SHARPENED-v1`

Let `Y` have a probability density bounded by `m`, let `b` be arbitrary, let `lambda!=0`, and let `p>2`. Then

`boxed:
 || E exp(it lambda (Y+b)^2) ||_(L^p(dt))
 <= S_p (m^2/|lambda|)^(1/p),`                                    (4.1)

where

`S_p=(4 pi)^(1/p) ((p-1)/(p-2))^((p-1)/p).`                      (4.2)

#### Proof

Scale `Z=m(Y+b)`. Its probability density `r` is bounded by one. Let `S=Z^2` and let `q` be the density of `S`. For `s>0`,

`q(s)=[r(sqrt(s))+r(-sqrt(s))]/(2 sqrt(s)) <= s^(-1/2).`          (4.3)

Let `p'=p/(p-1)` and `beta=p'-1=1/(p-1)`. Since `q<=s^(-1/2)`,

`q(s)^(p') <= q(s) s^(-beta/2).`                                  (4.4)

Therefore

`int q(s)^(p') ds <= E |Z|^(-beta).`                              (4.5)

Among probability densities bounded by one, the integral against the symmetric decreasing kernel `|z|^(-beta)` is maximized by the unit-length interval centered at zero. Hence

`E|Z|^(-beta) <= int_(-1/2)^(1/2) |z|^(-beta) dz`
`               = 2^beta/(1-beta).`                               (4.6)

Taking the `1/p'` power and using `beta=1/(p-1)` gives

`||q||_(p') <= 2^(1/p) ((p-1)/(p-2))^((p-1)/p).`                 (4.7)

For the nonunitary Fourier transform `hat q(t)=int e^{its}q(s)ds`, Hausdorff-Young gives

`||hat q||_p <= (2 pi)^(1/p)||q||_(p')`
`             <= S_p.`                                            (4.8)

Finally

`lambda(Y+b)^2=(lambda/m^2)S`,                                    (4.9)

so frequency scaling contributes `(m^2/|lambda|)^(1/p)`, proving (4.1). QED.

At `p=3`, `S_3=2(2pi)^(1/3)`, recovering the scalar constant used in the earlier `L^3` receiver. The lemma is translation-uniform and integrated in frequency; it makes no pointwise decay claim.

## 5. Full source-disjoint-square `L^p` compiler

For `Y=a^T X_D`, the one-dimensional product-projection theorem gives

`m:=||p_Y||_infinity <= sqrt(2)/sigma.`                            (5.1)

Hence Lemma 4.1 implies, uniformly in `w`,

`G_p:=|| E_D exp(it lambda(a^T X_D+h(w))^2)||_p`
`    <= S_p 2^(1/p) rho^(-1/p).`                                  (5.2)

Given `w`, the square bank is independent of the `I,J` bicore, so the conditional characteristic function factors. Let `p'=p/(p-1)`. For every `T>0`, use `|phi|<=1` at low frequency, (3.3) at high frequency, and Holder on BOTH tails simultaneously:

`int_R |phi_(Q|w)(t)|dt`
` <= 2T + 2pi Delta^(-1/2) G_p`
`      * [int_(|t|>T)|t|^(-p')dt]^(1/p')`
` = 2T + B_p Delta^(-1/2) rho^(-1/p) T^(-1/p),`                  (5.3)

where

`int_(|t|>T)|t|^(-p')dt=2(p-1)T^(-1/(p-1))`,                    (5.4)

and the constants simplify to

`B_p=4 pi S_p (p-1)^((p-1)/p).`                                  (5.5)

The minimizer of `2T+C T^(-1/p)` is

`T=(C/(2p))^(p/(p+1))`,                                          (5.6)

at which the minimum is `2(p+1)T`. The estimate is uniform in `w`; averaging over `W` and using Tonelli preserves it. Therefore `phi_Q in L^1`, so Fourier inversion gives a continuous density in `C_0(R)`.

### Theorem 5.1 — `QFORM-RANK2-CROSS-PLUS-SQUARE-LP-v2`

For every real `p>2`, the form (2.1) satisfies

`boxed:
 ||p_Q||_infinity
 <= K_p Delta^(-p/[2(p+1)]) rho^(-1/(p+1)),`                     (5.7)

where

`K_p=(p+1)/pi [B_p/(2p)]^(p/(p+1))`                              (5.8)

and `B_p,S_p` are given by (5.5),(4.2).

The scaling is exact: if the entire quadratic form is multiplied by `c`, then `Delta` scales by `c^2`, `rho` scales by `|c|`, and the right side scales by `|c|^(-1)`.

It is useful to rewrite (5.7) as

`boxed:
 ||p_Q||_infinity
 <= K_p Delta^(-1/2)
       (sqrt(Delta)/rho)^(1/(p+1)).`                              (5.9)

This makes the weak-square optimization transparent.

## 6. Two quantitative improvements

### 6.1 Improved fixed-exponent constant

At `p=3`,

`B_3=16 pi^(4/3)`                                                (6.1)

and (5.8) simplifies exactly to

`K_3=4(8/3)^(3/4)=8.347117760390866... .`                        (6.2)

Thus the preceding source-disjoint `L^3` theorem is sharpened from `<9.927` to

`boxed:
 ||p_Q||_infinity
 <8.348 Delta^(-3/8) rho^(-1/4).`                                (6.3)

The gain comes from applying Holder on the two time tails simultaneously, rather than separately and then using the triangle inequality.

### 6.2 Logarithmic weak-square loss

Set

`R=sqrt(Delta)/rho`, `L=log_+ R.`                                 (6.4)

For `p>=4`, (5.5) admits the exact rearrangement

`B_p/(2p)
 =2pi (4pi/p)^(1/p)
      (1+1/[p(p-2)])^((p-1)/p).`                                 (6.5)

For `p>=4`, the first factor after `2pi` is at most `pi^(1/4)<4/3`, while the second is at most `9/8`. Hence

`B_p/(2p)<3pi`,                                                   (6.6)

and therefore

`K_p<3(p+1).`                                                     (6.7)

Also a direct substitution gives

`K_4=9.342982047116381... <10.`                                  (6.8)

If `0<=L<=4`, choose `p=4`. Then

`R^(1/5)<=exp(L/5)<=1+L`,                                        (6.9)

so (5.9) and (6.8) give `<10 Delta^(-1/2)(1+L)`.

If `L>4`, choose the real exponent `p=L`. Then `p>=4`,

`R^(1/(p+1))=exp(L/(L+1))<e<3`,                                 (6.10)

and (6.7) gives

`||p_Q||_infinity<9 Delta^(-1/2)(1+L).`                           (6.11)

Combining both regimes proves:

### Corollary 6.2 — `QFORM-RANK2-CROSS-PLUS-SQUARE-LOG-v1`

Under (2.1),

`boxed:
 ||p_Q||_infinity
 <= 10 Delta^(-1/2)
       [1+log_+(sqrt(Delta)/rho)].`                               (6.12)

The density is continuous and vanishes at infinity. Thus the old power deterioration `rho^(-1/4)` can be replaced by only a logarithm when the independent square strength is small compared with `sqrt(Delta)`.

Combining (6.3) and (6.12), one may use the stronger of

`boxed:
 ||p_Q||_infinity
 <= min{
   8.348 Delta^(-3/8) rho^(-1/4),
   10 Delta^(-1/2)[1+log_+(sqrt(Delta)/rho)]
 }.`                                                               (6.13)

This is the principal new quantitative output of the run.

## 7. Designated partner account04/B01 applied at the actual new inequality

The completed account04/B01 theorem defines

`D_T mu(y)=(1/(2pi)) int_(-T)^T (1-|t|/T)
              Re(e^(-ity) phi_mu(t)) dt`                           (7.1)

and proves exactly

`||p_mu||_infinity=sup_(T>0,y)D_T mu(y)`                           (7.2)

with the extended-value convention.

Applying (7.2) to (6.13) yields the requested averaged-frequency statement

`boxed:
 sup_(T>0,y) D_T law(Q)(y)
 <= min{
   8.348 Delta^(-3/8) rho^(-1/4),
   10 Delta^(-1/2)[1+log_+(sqrt(Delta)/rho)]
 }.`                                                               (7.3)

This is an equation-level use of the designated partner result. It controls exactly the signed Fejer quantity equivalent to the essential density norm, while preserving the phase-aligned counterexample to any law-uniform scalar pointwise decay.

The ordinary distribution-function consequence is also immediate: for every interval `J_0`,

`P(Q in J_0) <= |J_0|` times the right side of (7.3).               (7.4)

## 8. Target-valid control and structural significance

For

`Q_0=2X_1Y_1+2X_2Y_2+Z^2`,                                      (8.1)

with all five variables independent cap-one inputs, `Delta=rho=1` and the coefficient matrix has nonzero spectrum

`{1,-1,1,-1,1}`.                                                  (8.2)

Thus `Q_0` satisfies the full spectral target. The sharpened `p=3` case gives

`boxed: ||p_(Q_0)||_infinity<8.348,   p_(Q_0) in C_0(R).`         (8.3)

The earlier theorem gave `<9.927` on this same control. More importantly, (6.12) changes the structural price of a weak but nonzero source-disjoint square from a negative power to a logarithm. This is useful in a routing argument where the cross area `Delta` is macroscopic while the third source-disjoint curvature packet may be much smaller.

The result does not say that the bare three-large-eigenvalue hypothesis always exposes decomposition (2.1), nor that the logarithm can be paid universally without a structural lower bound or a complementary branch. Known strict-N3 constructions rule out several naive single-packet extraction rules. The full conjecture therefore remains open.

## 9. First unpaid implication

The analytic debt for a source-disjoint square is now substantially reduced. The next B01 implication is:

`QFORM-N3-THIRD-DIRECTION-ROUTING-AFTER-LOG-v1` — in the remaining strict-N3 / low-cross-rank states, prove that a target-scale rank-two cross bicore either has (i) a source-disjoint third square with enough aggregate strength to make the logarithmic receiver universal, (ii) a source-overlapping third direction paid by the existing transverse-curvature receivers, or (iii) an already-paid pair-log / hub / grouped-square / ridge / rank-three-cross / null-coloop exit. The key requirement is to aggregate before taking reciprocals; no fixed physical minor is presumed uniformly large.

Continuity is proved on the branch (2.1), but remains open for the unrestricted full target.

## 10. Status

* Full QFORM: `OPEN / NOT PROVED / NOT DISPROVED`.
* New theorem: full `p>2` source-disjoint-square compiler plus logarithmic weak-square corollary.
* Pointwise scalar Fresnel decay: explicitly not used and remains false uniformly.
* Density regularity in this branch: continuous `C_0`.
* Designated partner account04/B01: applied at (7.3).
* Native brain ingestion: `WITHOUT_VERIFIED_BRAIN`; authenticated repository retrieval is not native learned-memory ingestion.
