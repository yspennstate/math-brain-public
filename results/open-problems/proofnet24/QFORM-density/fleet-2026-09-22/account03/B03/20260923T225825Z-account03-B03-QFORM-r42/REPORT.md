SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B03, 2026-09-23T22:58:25Z.
attacking: the critical rank-one hub time integral — prove a dependence-safe whole-copy half-Riesz estimate with arbitrary bank-local phases, sharpen it for an exactly linear hub, and spend that sharpened estimate through one genuinely independent square to recover linear small-ball scaling.

# account03/B03 r42 — critical rank-one hub time integral, linear-hub half-Riesz, and square transduction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Classification:** `NEW SUPPORTING THEOREM / CURRENT SMALL-LEAK BRANCH APPLIED / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted QFORM conjecture remains OPEN. This report proves a critical weighted Fourier estimate that is uniform over arbitrary rough bank-local phases, then proves a stronger one-copy estimate when the hub is exactly linear. The latter converts one genuinely independent square into a bounded continuous density and a linear interval small-ball estimate. No pointwise quadratic van-der-Corput bound, no post-rotation independence, no moment/support hypothesis, and no conditional cap for a conjugate sum/difference variable is used.

## 1. Fresh source boundary and current obstruction

Fresh `math-research-brain/main` controls were read at this actual invocation. OWNER CONTROL remains revision `2026-09-22.15`, programme `QFORM-DENSITY-3EIG-20260922`, with no pause/stop for account03/B03. The current owner continuation is `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`. The live `CURRENT_RESEARCH.md`, `CLAIMS.json`, `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and `assignments/account03/B03.json` were reread. Full QFORM and full-target continuity remain OPEN.

Corrections retained in every argument below:
- law-uniform pointwise decay for one-dimensional quadratic phases is false;
- rotating to spectral coordinates does not preserve independence;
- one member of the conjugate pair `X-X'`, `X+X'` does not retain a cap-one conditional density after conditioning on the other;
- arbitrary-joint coarea caps and naive fiber-supremum reductions are unavailable;
- a small coefficient multiplying an unbounded rough random variable is not a small random perturbation without additional hypotheses.

Two current supporting sources are used with their exact scopes.

1. The arbitrary-rank crossing report

`yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`

proves the exact-rank crossing Plancherel estimate with arbitrary internal measurable phases. The rank-one case is a critical, non-`L^1_t` endpoint; Section 2 below computes the weighted `|phi|^2` integral that remains finite at that endpoint.

2. The current physical-leaf theorem

`yspennstate/math-open-problems@634657eab2dee8269481af6aa10369a520153609`

`proofnet24/QFORM-density/interactive/20260923T222500Z-two-physical-leaf-pair-arbitrary-hub/REPORT.md`

proves, for the canonical original-product quadratic `2HL+beta L^2+V^2+2 epsilon LP`, an all-level density bound from any two physical leaves with nonzero `(L,V)` determinant. Section 6 gives a separate continuity upgrade for its planar lemma.

The designated partner is account04/B03:

`yspennstate/math-open-problems@05ff82a8d052b024ae584e60dffb7b198fcd7db4`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B03/20260923T183012Z-account04-B03-dependent-riesz-r2/REPORT.md`.

Its dependence-safe fractional-budget theorem is applied to an actual joint-window inequality in Section 5.

## 2. Critical rank-one local-phase Plancherel

The first theorem allows arbitrary measurable phases on both sides of a genuine rank-one product crossing. Its pointwise Fourier estimate is the rank-one specialization of the completed crossing theorem; the new item needed by B03 is the exact critical whole-copy weighted time integral.

### Theorem 2.1 — `QFORM-RANK1-LOCALPHASE-WHOLECOPY-HALFRIESZ-v1`

Let `H` be a real random variable with probability density `f_H<=1`. Let `X=(X_1,...,X_m)` be independent of `H`, with independent scalar coordinates of density at most one. Let `ell in R^m`, `ell!=0`, put

`L=ell.X`,

and let `F:R->R`, `R:R^m->R` be arbitrary measurable functions for which

`S=F(H)+R(X)+2 tau H L`,   `tau!=0`,                              (2.1)

is finite almost surely. Then

`boxed:
 |phi_S(t)| <= min{1,
   2^(1/4) sqrt(pi) (|tau| ||ell||_2)^(-1/2) |t|^(-1/2)}.
`                                                                    (2.2)

Consequently

`boxed:
 int_R |t|^(-1/2)|phi_S(t)|^2 dt
 <= 2^(13/4) sqrt(pi) (|tau| ||ell||_2)^(-1/2)
 =16.86251784408649... (|tau| ||ell||_2)^(-1/2).
`                                                                    (2.3)

Equivalently, for an independent copy `S'`,

`boxed:
 E|S-S'|^(-1/2)
 <= 2^(11/4) (|tau| ||ell||_2)^(-1/2).
`                                                                    (2.4)

The equivalence uses the standard positive-regularized one-dimensional Riesz identity

`int_R exp(itx)|t|^(-1/2)dt = sqrt(2pi)|x|^(-1/2)`.                (2.5)

#### Proof

Push the complex measure

`exp(it R(X)) dP_X`

onto the scalar coordinate `L`. Its complex density `b_t(l)` satisfies

`|b_t(l)|<=p_L(l)`.                                                 (2.6)

The product-projection bound gives

`||p_L||_infinity <= sqrt(2)/||ell||_2`.                            (2.7)

Therefore

`||b_t||_2^2 <= ||p_L||_infinity <= sqrt(2)/||ell||_2`.            (2.8)

On the hub side let

`a_t(h)=f_H(h) exp(itF(h))`.

Since `f_H<=1` and has mass one,

`||a_t||_2<=1`.                                                      (2.9)

With Fourier convention `hat b(xi)=int exp(i xi l)b(l)dl`, Fubini gives

`phi_S(t)=int a_t(h) hat b_t(2 tau t h) dh`.                        (2.10)

Cauchy--Schwarz, the change of variables `xi=2 tau t h`, and Plancherel yield

`|phi_S(t)|
 <= [int |hat b_t(2 tau t h)|^2 dh]^(1/2)
 = [pi/(|tau t|)]^(1/2) ||b_t||_2
 <= 2^(1/4) sqrt(pi) (|tau| ||ell||_2)^(-1/2)|t|^(-1/2)`.          (2.11)

Together with `|phi_S|<=1`, this proves (2.2).

Write

`A=2^(1/4) sqrt(pi) (|tau| ||ell||_2)^(-1/2)`.                     (2.12)

The crossover of `1` and `A|t|^-1/2` is `|t|=A^2`. Hence

`int_R |t|^(-1/2) min{1,A^2/|t|}dt
 =2[ int_0^(A^2)t^(-1/2)dt
       +A^2 int_(A^2)^infinity t^(-3/2)dt]
 =8A`,                                                               (2.13)

which is exactly (2.3). Applying (2.5) to the whole-copy identity

`|phi_S(t)|^2=E exp(it(S-S'))`                                      (2.14)

through positive regularization gives (2.4). No sum/difference coordinate is conditioned or re-capped. `square`

### Scope

The arbitrary functions `F(H)` and `R(X)` may include arbitrary hub curvature, all within-bank quadratic terms, affine terms, fragmented-support effects, or any other measurable bank-local potential. This is exactly why the conclusion is stated at the **critical whole-copy half-Riesz level**, not as a bounded-density theorem: the rank-one crossing alone supplies only a `|t|^-1/2` one-copy envelope.

## 3. Exactly linear hub: a stronger one-copy half-Riesz estimate

When the hub has no extra local phase, conditioning on the genuine hub variable yields more than Theorem 2.1.

### Lemma 3.1 — capped-density half-Riesz extremum

If `Y` is a real probability density bounded by `M`, then for every `s`,

`boxed: E|Y-s|^(-1/2) <= 2 sqrt(2M).`                               (3.1)

Proof by layer cake:

`E|Y-s|^(-1/2)
 =int_0^infinity P(|Y-s|<u^(-2))du
 <=int_0^infinity min{1,2M u^(-2)}du
 =2 sqrt(2M)`.                                                       (3.2)

### Theorem 3.2 — `QFORM-LINEAR-HUB-ONECOPY-HALFRIESZ-v1`

Under the same original-product hypotheses as Theorem 2.1, let now

`Q=2 tau H L+R(X)`                                                  (3.3)

with **no additional hub-local term**. The light-bank function `R(X)` remains completely arbitrary. Then

`boxed:
 sup_s E|Q-s|^(-1/2)
 <= 2^(11/4)(|tau| ||ell||_2)^(-1/2)
 =6.727171322029716... (|tau| ||ell||_2)^(-1/2).
`                                                                    (3.4)

Moreover the exact independent-copy geometry improves the assigned weighted time integral to

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2dt
 <= (16/3) pi^(3/4)(|tau| ||ell||_2)^(-1/2)
 =12.58522929287838... (|tau| ||ell||_2)^(-1/2).
`                                                                    (3.5)

#### Proof of the one-copy estimate

Fix `X`. Since `R(X)` is then a constant, the conditional law of `2 tau L H+R(X)` has density cap

`M_X = 1/(2|tau L|)`                                                (3.6)

whenever `L!=0`. The event `L=0` has probability zero because `L` is a nontrivial absolutely continuous projection. Lemma 3.1 gives

`E_H[|Q-s|^(-1/2) | X]
 <=2/sqrt(|tau L|)`.                                                (3.7)

The scalar projection density cap (2.7), followed again by Lemma 3.1 with `s=0`, yields

`E|L|^(-1/2)
 <=2 sqrt(2 * sqrt(2)/||ell||_2)
 =2^(7/4)||ell||_2^(-1/2)`.                                       (3.8)

Averaging (3.7) proves (3.4).

#### Proof of the sharper whole-copy constant

Let `(H',X')` be an independent copy and `L'=ell.X'`. Conditional on `(X,X')`,

`Q-Q'=2 tau(LH-L'H') + [R(X)-R(X')]`.                              (3.9)

The bracket is only a translation. The density of the independent linear combination

`2 tau L H-2 tau L'H'`

is at most the smaller of the two scaled hub caps, hence

`<=1/(2|tau| max{|L|,|L'|})
 <=1/(sqrt(2)|tau| sqrt(L^2+L'^2))`.                               (3.10)

Lemma 3.1 therefore gives

`E[|Q-Q'|^(-1/2) | X,X']
 <=2^(5/4)|tau|^(-1/2)(L^2+L'^2)^(-1/4)`.                         (3.11)

The independent pair `(L,L')` has planar density cap

`K <=2/||ell||_2^2`.                                                (3.12)

For any planar probability density bounded by `K`, another layer-cake calculation gives

`E (Y_1^2+Y_2^2)^(-1/4)
 <=int_0^infinity min{1,pi K u^(-4)}du
 =(4/3)(pi K)^(1/4)`.                                              (3.13)

Thus

`E|Q-Q'|^(-1/2)
 <= [2^(7/2)/3] pi^(1/4)
    (|tau| ||ell||_2)^(-1/2)`.                                    (3.14)

Multiply by `sqrt(2pi)` using the exact whole-copy Riesz identity (2.5),(2.14). The constant simplifies to `(16/3)pi^(3/4)`, proving (3.5). `square`

### Application to the current rough small-leak family

The current programme repeatedly isolates canonical forms

`Q_(beta,epsilon)
 =2 H L+beta L^2+V^2+2 epsilon L P`,                               (3.15)

where `H` is a genuine independent original hub and `L,V,P` are projections of the remaining original product bank. If `||ell||_2=1`, simply take

`R(X)=beta L^2+V^2+2 epsilon LP`.

No assumption on `beta`, `epsilon`, support shape, moments, or on the size of `P` is needed. Theorem 3.2 gives uniformly

`boxed:
 sup_s E|Q_(beta,epsilon)-s|^(-1/2) <= 2^(11/4)<6.728,
`                                                                    (3.16)

and

`boxed:
 int |t|^(-1/2)|phi_(Q_(beta,epsilon))(t)|^2dt
 <=(16/3)pi^(3/4)<12.586.
`                                                                    (3.17)

This does **not** by itself prove a bounded density for (3.15). It does remove all leakage dependence from the one-copy and whole-copy half-Riesz budgets. The remaining issue is obtaining the final independent half-power without falsely treating the dependent light square `V^2` as an independent smoother.

This is directly compatible with the current small-leak correction: the abstract full-3D bank obstruction is not being bypassed by a bank-density-only Fourier decay claim. The estimate uses the genuine physical hub and the true scalar projection density of `L` from the original product source.

## 4. One genuinely independent square gives linear small-ball scaling and continuity

The stronger one-copy estimate (3.4) can be spent immediately when a genuinely independent square exists.

### Corollary 4.1 — `QFORM-LINEAR-HUB-PLUS-INDEPENDENT-SQUARE-v1`

Let `Z` be an additional original scalar coordinate, independent of `(H,X)`, with density at most one. Let `d!=0`, `h,c` be arbitrary real constants, and set

`T=d(Z+h)^2 + Q + c`,                                               (4.1)

where `Q` is as in Theorem 3.2. Then `T` has a bounded **continuous `C_0` density** and

`boxed:
 ||p_T||_infinity
 <=2^(11/4)|d|^(-1/2)(|tau| ||ell||_2)^(-1/2).
`                                                                    (4.2)

Consequently every interval `I` satisfies the linear small-ball estimate

`boxed:
 P(T in I)
 <=2^(11/4)|d|^(-1/2)(|tau| ||ell||_2)^(-1/2)|I|.
`                                                                    (4.3)

#### Proof

The shifted square `Y=d(Z+h)^2` has an `L^1` density satisfying, on the appropriate half-line,

`p_Y(y)<=|d|^(-1/2)|y|^(-1/2)`.                                   (4.4)

Therefore, for almost every `s`,

`p_T(s)
 =E p_Y(s-c-Q)
 <=|d|^(-1/2) E|s-c-Q|^(-1/2)`.                                  (4.5)

Apply (3.4) to obtain (4.2), hence (4.3).

For continuity, first note that `Q` itself has an `L^1` density: conditional on `X`, it is a translate and nonzero scaling of the absolutely continuous hub `H` for almost every `X`. The square `Y` also has an `L^1` density. Hence `p_T=p_Q*p_Y`; convolution of two `L^1(R)` functions is continuous and vanishes at infinity. `square`

This is an end-to-end B03 compiler: the dependence-safe time integral is finite at the rank-one critical endpoint, and in the exactly linear-hub case the same geometry supplies a translation-uniform one-copy half-Riesz receiver; one genuine independent square then recovers linear output small-ball scaling with an explicit constant.

## 5. Designated partner applied to an actual inequality

The completed account04/B03 theorem is used here exactly on its valid scope. Let `X_0=(X_1,X_2)` be two independent cap-one variables and let `X_0'` be an independent copy. Put

`U=X_0-X_0'`, `V=X_0+X_0'`.                                       (5.1)

For invertible symmetric `P_-,P_+` and arbitrary affine data, define

`R_-(U)=U^T P_- U+ell_-^T U+d_-`,
`R_+(V)=V^T P_+ V+ell_+^T V+d_+`.                                (5.2)

The partner theorem gives, on the **actual dependent joint law** of `(U,V)`,

`P(|R_-(U)-s|<=rho, |R_+(V)-t|<=rho)
 <=sqrt(B(P_-)B(P_+)) rho^(1/2)`,                                 (5.3)

where in particular `B(P)<=128|det P|^(-1/4)`.

Now take an independent linear-hub-plus-square bank `(H,X,Z)` satisfying Corollary 4.1 and define

`T_*=d(Z+h)^2+2 tau H(ell.X)+R_0(X)+R_-(U)+R_+(V)`.                (5.4)

Conditioning on `(U,V)` makes `R_-+R_+` only a translation, so Corollary 4.1 gives the **uniform conditional** interval bound

`P(T_* in I | U,V)
 <= C_* |I|`,                                                       (5.5)

where

`C_*=2^(11/4)|d|^(-1/2)(|tau| ||ell||_2)^(-1/2)`.                 (5.6)

Multiplying (5.5) by the partner event and averaging gives the actual combined inequality

`boxed:
 P(T_* in I,
   |R_-(U)-s|<=rho,
   |R_+(V)-t|<=rho)
 <= C_* sqrt(B(P_-)B(P_+)) rho^(1/2)|I|.
`                                                                    (5.7)

In the natural parametrization `rho=epsilon^2`,

`boxed:
 P(T_* in I,
   |R_--s|<=epsilon^2,
   |R_+-t|<=epsilon^2)
 <= C_* sqrt(B(P_-)B(P_+)) epsilon |I|.
`                                                                    (5.8)

This is not claimed as a full-target structural extraction. It is a concrete use of the partner's dependent sum/difference theorem inside a linear output small-ball inequality, and it never declares `U` and `V` independent.

## 6. Continuity upgrade for the current physical-leaf planar lemma

The current two-physical-leaf theorem proves the uniform height bound but its displayed statement does not separately record continuity. The underlying optimized planar lemma actually yields `C_0` regularity under the same rough hypotheses.

### Proposition 6.1 — `QFORM-PLANAR-LEAF-C0-UPGRADE-v1`

Let `H` have density at most one and be independent of a planar pair `(L,W)` whose joint probability density `g(l,w)` is bounded by `K`. Let `r:R->R` be arbitrary measurable and

`Y=2HL+r(L)+W^2`.                                                   (6.1)

Then the density constructed in the physical-leaf theorem is continuous, vanishes at infinity, and retains exactly the same bound

`boxed: ||p_Y||_infinity <=3*2^(2/3) K^(2/3).`                     (6.2)

#### Proof

For a.e. fixed `l!=0`, let `m(l)=int g(l,w)dw`. Push the finite measure `g(l,w)dw` under `w->w^2`; its `L^1` density is

`q_l(u)=1_(u>0)[g(l,sqrt u)+g(l,-sqrt u)]/(2sqrt u)`,              (6.3)

with `||q_l||_1=m(l)`. Let

`h_l(y)=f_H(y/(2l))/(2|l|)`,                                       (6.4)

an `L^1` probability density. The `l`-slice output density is

`k_l(s)=(h_l*q_l)(s-r(l))`.                                       (6.5)

Since `L^1*L^1 subset C_0`, every `k_l` is continuous and vanishes at infinity.

Fix `eta>0`. For `|l|>=eta`,

`||k_l||_infinity
 <=||h_l||_infinity ||q_l||_1
 <=m(l)/(2eta)`.                                                    (6.6)

Because `int m(l)dl=1`, dominated convergence implies

`p_eta(s)=int_(|l|>=eta) k_l(s)dl`                                 (6.7)

belongs to `C_0(R)`.

The low-`|l|` calculation already proved in the physical-leaf theorem gives, uniformly in `s`,

`0<=p_Y(s)-p_eta(s)
 <=4 sqrt(2) K sqrt(eta)`.                                         (6.8)

Thus `p_eta -> p_Y` uniformly as `eta downarrow0`. A uniform limit of `C_0` functions is `C_0`, proving the continuity claim without changing the optimized height estimate (6.2). `square`

Applying this after the exact two-physical-leaf conditioning in the source theorem shows that its canonical leakage branch also has a continuous `C_0` density: the conditional `C_0` densities have the same uniform bound, so averaging over the conditioned outside originals preserves continuity and vanishing at infinity by dominated convergence.

## 7. What this does and does not close

The main new usable facts are:

1. **Arbitrary hub/local phases, critical rank-one crossing:** the whole-copy weighted integral (2.3) is uniformly finite. This is exactly the B03 independent-copy endpoint and retains every local phase.
2. **Exactly linear physical hub:** arbitrary rough light-bank curvature drops completely out of the one-copy half-Riesz budget (3.4), and the whole-copy constant sharpens to (3.5).
3. **Canonical small leakage:** `2HL+beta L^2+V^2+2epsilon LP` satisfies (3.16)-(3.17) uniformly in `beta,epsilon`; the small-leak coefficient never appears.
4. **A genuine independent square:** (4.2)-(4.3) recover a bounded continuous density and linear small-ball scaling.
5. **Physical-leaf branch:** the current all-level density theorem upgrades to `C_0` continuity with no extra hypothesis.

The unrestricted three-large-eigenvalue theorem is still OPEN. The specific remaining structural issue is that the canonical small-leak form (3.15) generally does **not** provide an independent square: `V^2` lives in the same light product bank as `L` and `P`. Spending (3.16) as though `V^2` were independent would be invalid. The next B03 mechanism should combine the uniform linear-hub half-Riesz budget with an aggregate product-preserving treatment of that dependent light square, or use a matrix reduction that exposes a truly disjoint square/second crossing at universal scale.

Full-target continuity remains OPEN even though the square-transduced and physical-leaf branches above are `C_0`.
