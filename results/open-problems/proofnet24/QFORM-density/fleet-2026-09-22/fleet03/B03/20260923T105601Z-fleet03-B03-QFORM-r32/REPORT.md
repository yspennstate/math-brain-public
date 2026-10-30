SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T10:56:01Z.
attacking: close the positive-disjoint-basis part of the exact angular-cancellation packet by a two-dimensional determinant-entropy Brascamp--Lieb estimate, then quantify the remaining delta->0 geometry as a near-coloop OR near-three-coordinate alternative.

# fleet03/B03 r32 — balanced-basis Fresnel estimate and weighted near-intersecting stability

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Status:** `NEW SUPPORTING THEOREMS / POSITIVE-DISJOINT-BASIS ENDPOINT PAID / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.


This report never rotates the independent physical coordinates into eigen-coordinates, never treats `X-X'` and `X+X'` as independent, never applies a conditional cap to one given the other, and never uses law-uniform pointwise van-der-Corput decay. All product Fourier estimates are performed in original coordinates.

## 1. Inputs actually used

### 1.1 One-dimensional twisted Fourier input

From the completed decoupling/Fresnel/Brascamp--Lieb package

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`,

for every cap-one probability density `f`, every measurable complex `g` with `|g|<=f`, and every `p>=2`,

`int_R |g^(hat)(s)|^p ds <= 4 pi / sqrt(p)`.                       (1.1)

This remains valid when `g` contains an arbitrary unit-modulus coordinatewise phase. It is an integrated estimate, not a pointwise decay claim.

### 1.2 Product-projection scalar cap

For every unit scalar projection `U=u.X` of an original-coordinate independent cap-one product law,

`||p_U||_infinity <= sqrt(e)`.                                     (1.2)

I use this only as a true marginal cap; no conditional projection cap is introduced.

### 1.3 Designated partner result

The designated `fleet04/B03` handoff is source-pinned to

`yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B03/20260922T193150Z-fleet04-B03-collision-l2-r1/REPORT.md`.

Its later-challenged weighted-L2 compiler is **not** used. I use only the valid elementary collision lemma

`P(|Y-Y'|<=eps) <= 2 eps ||p_Y||_2^2`                              (1.3)

for an independent copy `Y'`.

## 2. A determinant-entropy two-dimensional product estimate

Let `r_j=(h_j,v_j) in R^2`, `j in J`, span `R^2`. For each two-set `S={j,k}` write

`D_S=det(r_j,r_k)`,

and define

`E2=sum_{|S|=2} D_S^2 = det(sum_j r_j r_j^T)>0`.                  (2.1)

Let the volume-sampling law on two-sets be

`p_S=D_S^2/E2`.                                                     (2.2)

For independent `S,T~p`, set

`delta=P(S cap T=emptyset)`.                                       (2.3)

Assume first `delta>0`. Let `mu` be the law of `(S,T)` conditioned on disjointness and let `q` be either one-set marginal of `mu`. Put

`alpha_j=P_{S~q}(j in S)`.                                         (2.4)

Because `mu` is symmetric and its two sets are disjoint,

`2 alpha_j=P(j in S)+P(j in T)<=1`, hence `alpha_j<=1/2`,          (2.5)

and `sum_j alpha_j=2`.

Define the determinant-entropy certificate

`Z_q=exp(H(q)+sum_S q_S log D_S^2)`.                               (2.6)

### Lemma 2.1 — entropy survives conditioning

`boxed: Z_q >= E2 delta.`                                          (2.7)

**Proof.** Since

`d mu/d(p tensor p)=1/delta`

on the disjoint event,

`D_KL(mu || p tensor p)=log(1/delta)`.                             (2.8)

Data processing under `(S,T)->S` gives

`D_KL(q||p)<=log(1/delta)`.                                        (2.9)

Using `p_S=D_S^2/E2`,

`D_KL(q||p)=log E2-H(q)-sum_S q_S log D_S^2=log(E2/Z_q)`.          (2.10)

Exponentiating proves (2.7). QED.

### Lemma 2.2 — balanced-basis Brascamp--Lieb estimate

Let `Psi_j` be arbitrary twisted characteristic functions coming from cap-one one-dimensional laws. For arbitrary translations `c_j`,

`boxed:
 int_{R^2} prod_j |Psi_j(h_j s+v_j eta+c_j)| ds d eta
 <=16 pi^2 Z_q^(-1/2)
 <=16 pi^2 (E2 delta)^(-1/2).
}`                                                                  (2.11)

**Proof.** For positive Gaussian parameters `d_j`, Cauchy--Binet gives

`det(sum_j d_j r_j r_j^T)=sum_S D_S^2 prod_{j in S} d_j`.          (2.12)

Weighted AM--GM with weights `q_S` yields

`det(sum_j d_j r_j r_j^T)
 >= exp(H(q)+sum_S q_S log D_S^2) prod_j d_j^(alpha_j)
 = Z_q prod_j d_j^(alpha_j).`                                      (2.13)

The rank-one Brascamp--Lieb Gaussian variational formula therefore bounds the BL constant for data `(r_j,alpha_j)` by

`Z_q^(-1/2) prod_j alpha_j^(-alpha_j/2)`.                          (2.14)

For every `alpha_j>0`, set `F_j=|Psi_j|^(1/alpha_j)`. Then the integrand in (2.11) is `prod F_j^(alpha_j)`. Since `alpha_j<=1/2`, (1.1) at `p=1/alpha_j` gives

`int F_j = int |Psi_j|^(1/alpha_j) <=4 pi sqrt(alpha_j).`          (2.15)

The factors `sqrt(alpha_j)` cancel exactly against (2.14), and `sum alpha_j=2`, so

`int prod |Psi_j| <= Z_q^(-1/2)(4pi)^2=16pi^2 Z_q^(-1/2)`.        (2.16)

Coordinates with `alpha_j=0` are dropped using `|Psi_j|<=1`. Translation invariance of the rank-one BL inequality makes the bound uniform in all `c_j`. QED.

The point of conditioning on **two disjoint sampled bases** is that it creates the admissible `alpha_j<=1/2` exponents without selecting one fragile physical pair.

## 3. Exact angular-cancellation packet: integrable one-copy Fourier bound

I now apply Lemma 2.2 to the exact-rank-three one-sided packet used in the preceding B03 work:

`Q=a^(-1) H^2 + 2 sigma U V`,                                      (3.1)

`H=a X_i+h_L.X_L+h_R.X_R+h_K.X_K`,
`U=u.X_L`, `V=v.X_R`,                                              (3.2)

with `X_L` and `X_R` disjoint original-coordinate product banks,

`h_R=beta v+m q`, `q perpendicular v`, `||q||=||v||=1`,           (3.3)

`m=rho y`, `y^2>1/2`, and

`(rho^2/|a|)|sigma| >= s_3(A)^2`.                                 (3.4)

In the exact heavy-row angular-cancellation sub-branch carried from the preceding packet, the heavy row also gives

`|sigma|>s_3(A)/2`.                                                 (3.5)

Consequently

`boxed: sigma^2 m^2/|a| >= s_3(A)^3/4.`                           (3.6)

Indeed `(sigma^2 m^2/|a|)=(|sigma|rho^2/|a|)|sigma|y^2`, and (3.4), (3.5), `y^2>1/2` give (3.6).

Let `r_j=(h_R,j,v_j)`. Then

`E2=det([h_R,v]^T[h_R,v])=m^2`.                                   (3.7)

Condition only on the original coordinates `X_i,X_K`. Fresnel-linearize the square in (3.1) **before** completing away any right coordinate. After taking the right-bank product expectation, the left bank enters only through the genuine scalar `U`. Using the true marginal cap `||p_U||_infinity<=L0`, changing variables `eta=2t sigma U`, and then applying (2.11), one obtains for `t!=0`

`|phi_Q(t)|
 <= [sqrt(|a|)/(2 sqrt(pi|t|))]
    [L0/(2|t sigma|)]
    [16 pi^2/(m sqrt(delta))]`                                     (3.8)

and therefore

`boxed:
 |phi_Q(t)| <= min(1,K |t|^(-3/2)),
 K=4 pi^(3/2) L0 sqrt(|a|)/(|sigma| m sqrt(delta)).
}`                                                                  (3.9)

No duplicated coordinate has been split into independent sum/difference pieces. This is a one-copy Fourier estimate obtained from original-coordinate product structure.

### 3.1 Density and continuity

For an envelope `min(1,K|t|^(-3/2))`, with crossover `T=K^(2/3)`, direct integration gives

`int_R |phi_Q(t)| dt <= 6 K^(2/3)`.                                (3.10)

Hence Fourier inversion gives a continuous `C_0` density in this branch and

`boxed: ||p_Q||_infinity <= (3/pi) K^(2/3).}`                      (3.11)

Using `L0<=sqrt(e)` and (3.6),

`boxed:
 ||p_Q||_infinity
 <=12 e^(1/3) s_3(A)^(-1) delta^(-1/3)
 =16.747349101033073... s_3(A)^(-1) delta^(-1/3).
}`                                                                  (3.12)

Thus for every fixed positive disjoint-basis probability `delta`, the packet has the desired **linear small-ball scaling**, and in fact a continuous density.

### 3.2 Independent-copy time integrals

The same envelope gives

`int_R |phi_Q(t)|^2 dt <=3 K^(2/3)`,                               (3.13)

so

`boxed: ||p_Q||_2^2 <= (3/(2pi)) K^(2/3).}`                        (3.14)

The assignment's weighted independent-copy integral is

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2 dt <=(24/5) K^(1/3).
}`                                                                  (3.15)

Since

`|phi_Q(t)|^2=E exp(it(Q-Q'))`                                     (3.16)

for an independent copy `Q'`, (3.15) keeps the entire copy-difference intact; no claim of independence between any coordinate sum and difference is made.

At target scale, (3.15) becomes

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <=(48/5) sqrt(pi) e^(1/6)
   s_3(A)^(-1/2) delta^(-1/6)
 =20.101505405674022... s_3(A)^(-1/2) delta^(-1/6).
}`                                                                  (3.17)

### 3.3 Designated partner applied to an actual inequality

Applying only the valid fleet04/B03 collision lemma (1.3) to (3.14),

`boxed:
 P(|Q-Q'|<=eps)
 <=(3/pi) K^(2/3) eps
 <=12 e^(1/3) s_3(A)^(-1) delta^(-1/3) eps.
}`                                                                  (3.18)

This is a genuine linear collision small-ball estimate. The partner's challenged weighted-L2 compiler is not used.

## 4. New structural theorem: small delta means near-coloop OR near-three-coordinate

The analytic estimate above deteriorates only as `delta->0`. The next question is therefore purely structural for the rank-two physical row frame. The following quantitative lemma identifies that collar.

### Theorem 4.1 — `QFORM-WEIGHTED-2EDGE-INTERSECTION-STABILITY-v1`

Let `p` be any probability law on two-element subsets of a finite or countable vertex set and let

`delta=P_{E,F iid~p}(E cap F=emptyset)`.                            (4.1)

Let `alpha_i=P(i in E)`. Put

`c_*=(3/2)^(1/3)=1.1447142425533319...`.                           (4.2)

Then at least one of the following holds:

**(A) Near-coloop.** There is a vertex `i` with

`boxed: alpha_i >=1-delta-c_* delta^(1/3).}`                       (4.3)

**(B) Near-triangle.** There are three vertices `i,j,k` such that

`boxed:
 p_{ij}+p_{ik}+p_{jk}
 >=1-delta-c_* delta^(1/3).
}`                                                                  (4.4)

Here missing edges have mass zero.

**Proof.** Average the disjointness probability over the first edge. There exists an edge `e={i,j}` in the support such that

`O:=P(F cap e=emptyset)<=delta`.                                    (4.5)

Write

`c0=p_{ij}`,
`A_k=p_{ik}`, `B_k=p_{jk}` for `k notin {i,j}`,
`a=sum_k A_k`, `b=sum_k B_k`.                                      (4.6)

Then

`a+b+c0=1-O`.                                                       (4.7)

Fix `tau>0`. If `min(a,b)<=tau`, say `b<=tau`, then

`alpha_i=a+c0=1-O-b >=1-delta-tau`,                                (4.8)

which is (A) with loss `delta+tau`.

Assume instead `a,b>tau`. Every ordered pair consisting of an `i-k` edge and a `j-l` edge is disjoint exactly when `k!=l`. Therefore its contribution to the full ordered disjointness probability gives

`2(ab-sum_k A_k B_k)<=delta`.                                      (4.9)

Normalize `x_k=A_k/a`, `y_k=B_k/b`. Then

`s:=sum_k x_k y_k >=1-epsilon`,
`epsilon:=delta/(2ab)<=delta/(2tau^2)`.                            (4.10)

Since `sum y_k=1`, `max x_k>=s`; choose `k` with `x_k>=1-epsilon`. A slightly more conservative estimate useful without any uniqueness assumption is

`x_k>=1-2epsilon`,
`y_k>=s-(1-x_k)>=1-3epsilon`.                                      (4.11)

Thus

`c0+A_k+B_k
 >=c0+a(1-2epsilon)+b(1-3epsilon)
 >=1-O-3epsilon
 >=1-delta-3delta/(2tau^2)`,                                      (4.12)

where `a+b<=1` was used in the penultimate bound. Hence (B) holds with loss `delta+3delta/(2tau^2)`.

Choose

`tau=(3delta/2)^(1/3)=c_* delta^(1/3)`.                            (4.13)

Then `3delta/(2tau^2)=tau`, so either (A) or (B) holds with the common loss `delta+tau`. QED.

### 4.2 Application to the determinant-volume law

Return to `p_{jk}=D_{jk}^2/E2`. The incidence marginal has the exact leverage interpretation

`alpha_j=r_j^T G^(-1) r_j`,
`G=sum_l r_l r_l^T`.                                                (4.14)

This follows from the rank-two Cauchy--Binet identity

`sum_{k!=j} D_{jk}^2 = E2 r_j^T G^(-1) r_j`.                       (4.15)

Therefore, when the disjoint-basis probability `delta` is small, either

`max_j r_j^T G^(-1)r_j >=1-delta-c_*delta^(1/3)`,                  (4.16)

so the physical two-plane is quantitatively near a **coloop row**, or there is a physical triple `T` with

`boxed:
 sum_{ {j,k} subset T } D_{jk}^2
 >=[1-delta-c_*delta^(1/3)] E2.
}`                                                                  (4.17)

Thus the only obstruction to the positive-delta balanced-basis compiler is quantitatively forced into a near-coloop or near-three-coordinate collar. This is stronger than merely saying the exact `delta=0` support is pairwise intersecting.

At `delta=0`, the usual pairwise-intersecting classification is recovered exactly: the support graph is a star or a triangle. In the determinant frame this means, respectively, one physical coloop row or a three-coordinate rank-two support after zero rows are removed.

## 5. What this does and does not close

The new analytic implication is complete for the exact angular-cancellation packet whenever its rank-two determinant-volume law has `delta>0`; it yields a continuous density and the explicit bound (3.12). The independent-copy weighted time integral (3.17) is also complete in that scope.

Theorem 4.1 identifies the remaining `delta->0` failure mode without selecting a fragile individual determinant: the fleet now only needs to pay a **near-coloop** or **near-three-coordinate** packet with a constant stable as `delta->0`, using the already-developed grouped-hub / finite-coordinate / aggregate-volume mechanisms. I do not claim that this structural payment has been completed here.

Therefore:

- unrestricted QFORM bounded-density conjecture: **OPEN**;
- unrestricted continuity: **OPEN**;
- positive-disjoint-basis exact angular-cancellation branch: **continuous C_0 density proved**;
- no counterexample to the conjecture is produced.

The next B03 mechanism should splice the quantitative alternative (4.16)/(4.17) into the existing exact-coloop and grouped-coordinate currencies, rather than continue paying powers of `delta^(-1)`.
