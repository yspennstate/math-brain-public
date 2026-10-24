# account02/B15 — exact Choquet continuity transfer without a common modulus, and a target-valid counterexample to uniform equicontinuity

**Run:** `20260922T130201Z-account02-B15-qform-r2`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner-control revision `2026-09-22.5`  
**Assignment:** `Absolute continuity and regularity`  
**Method:** complementary constructions / source-valid counterexamples  
**Classification:** `ESSENTIAL_STEP_APPLIED / REGULARITY-BRIDGE-CHANGED / FULL_TARGET_OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target, partner result, and first unpaid implication

The sole target remains: for every dimension `n`, every independent real `X_i` with measurable densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has an essentially bounded density with one universal finite bound, or give a valid counterexample. The additional continuous-density conclusion is separate and may not be used to infer the central `L^infinity` estimate.

The completed assigned-partner result actually used is:

- `account03/B15`, canonical source `yspennstate/math-open-problems@40946450aa2bfb06068a2c688d4407be10470c22`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260922T122718Z-account03-B15-qform-r11/REPORT.md`.

That report proves the exact central extremal transfer: with

`M(mu)=sup_I mu(I)/|I|`, one has `M(mu)<infinity` iff `mu=p dx` with `p in L^infinity`, and `M(mu)=||p||_infinity`; moreover `M` is convex and TV-lower-semicontinuous. Combining this with the completed convex-hull/finite-fragment theorem reduces the universal bounded-density target exactly to a uniform interval small-ball bound on product indicators of measure-one sets, even bounded finite unions of intervals. It also gives a sufficient continuity-transfer theorem under a **common modulus of continuity** on all extreme output densities.

The first unpaid regularity implication is therefore not absolute continuity. My preceding B15 report `yspennstate/math-open-problems@60e7f51716e67553ce759519f9801ff3674dcce9` already proves:

1. `X^TAX` is absolutely continuous for every nonzero symmetric `A` whenever the joint input law is absolutely continuous; no three-eigenvalue hypothesis is needed.
2. For every fixed symmetric `A` of rank at least three, `X^TAX` has an essentially bounded density, with a finite matrix-dependent principal-pivot certificate.
3. What remains central is uniformity of the `L^infinity` constant over the target spectral class.

For the stronger continuity conclusion, the partner's common-modulus condition is sufficient but, as shown below, cannot hold uniformly even on the easiest fixed target matrix `A=I_3` and finite-fragment extreme laws. The substantive task is thus to replace common equicontinuity by a weaker exact transfer mechanism.

All live corrections are retained: law-uniform pointwise quadratic Fourier decay is false; rotation does not preserve independence; naive fiber suprema lose dimension; a cross minor alone does not close the shell; conditional caps do not replace independence; a single Schur rank-two extraction is not forced; and bounded-diameter/single-interval localization is false. None is used as a premise here.

---

## 2. Exact implications among AC, essential boundedness, and continuity

Under the target hypotheses the current rigorous implication ledger is:

- **Absolute continuity is already automatic.** Since the product input law has an `L^1` density and `A` is nonzero, the active spectral-coordinate coarea argument gives `Q<<dx`. This conclusion is strictly qualitative and supplies no uniform density bound.
- **Essential boundedness implies absolute continuity**, tautologically through interval domination, but the universal essential bound is still the main open problem. For every fixed target matrix a finite, generally nonuniform, `L^infinity` certificate is already known.
- **Continuity is not a legitimate substitute for essential boundedness.** A continuous probability density need not have a universal bound, and no continuity statement proved here is used to pay the central interval estimate.
- **A common `L^infinity` bound alone does not transfer continuity through arbitrary TV approximation**; this was already correctly noted by the partner. Section 3 strengthens that warning: even within the exact QFORM target there is no law-uniform modulus of continuity on the extreme class, so a common-modulus closure is impossible.
- **Nevertheless a common modulus is not necessary.** Section 4 proves an exact Choquet/barycentric transfer: if every extreme product-indicator output is individually continuous and all such outputs obey the same `L^infinity` bound `C`, then every admissible measurable product density has a continuous output density bounded by `C`, with no shared modulus assumed.

Thus the central and stronger conclusions can be ordered without smuggling one into the other:

`universal extreme interval bound  => universal L^infinity for all admissible laws => absolute continuity`,

while continuity can be appended by the independent condition “each extreme output has a continuous representative,” via the exact barycentric theorem below.

---

## 3. Target-valid obstruction: no common continuity modulus even for `A=I_3`

### Theorem 3.1 — `QFORM-NO-COMMON-EXTREME-MODULUS-v1`

There is a sequence of product-indicator inputs satisfying the full target hypotheses for the fixed matrix `A=I_3` such that every output density is bounded and uniformly continuous, but the family admits **no common modulus of continuity**.

More explicitly, there is a constant

`epsilon_0 > 0.00105`

and for every sufficiently large integer `N` a measure-one bounded finite union of intervals `E_N` and points `s_N,t_N` with

`|s_N-t_N| -> 0`,

but for iid `X_1,X_2,X_3 ~ 1_{E_N}` and

`Q_N=X_1^2+X_2^2+X_3^2`,

its continuous density `p_N` satisfies

`p_N(s_N) >= epsilon_0`, `p_N(t_N)=0`.

Consequently no function `omega(r)->0` can satisfy

`|p_N(s)-p_N(t)| <= omega(|s-t|)`

simultaneously for all these target-valid extreme laws.

### Construction

Fix

`R=100`, `d=1000`, `R_+=sqrt(R^2+d)=sqrt(11000)`.

For `N>=2`, set

`a_k=sqrt(R^2+k d/N)`, `k=0,...,N-1`,

and

`E_N = union_{k=0}^{N-1} [a_k,a_k+1/N]`.

The intervals are disjoint. Indeed

`a_{k+1}-a_k = (d/N)/(a_{k+1}+a_k) >= d/(2R_+N) > 1/N`

because `d/(2R_+)>4.7`. Hence `|E_N|=1`, so `1_{E_N}` is an admissible extreme one-dimensional density.

Let `g_N` be the density of `X^2` for `X~1_{E_N}`. Since `E_N` lies on the positive half-line,

`g_N(y)=sum_k 1_{J_{k,N}}(y)/(2 sqrt(y))`,

where

`J_{k,N}=[R^2+k d/N, R^2+k d/N+w_{k,N}]`,

`w_{k,N}=2a_k/N+1/N^2`.

Put

`B=2R_+ + 1`.

Then every component width satisfies `w_{k,N}<=B/N`, while every component width is at least

`u_N:=2R/N`.

The density of `Q_N` is the triple convolution

`p_N=g_N*g_N*g_N`.

For triples with index sum `m`, the support lies in the cluster

`K_{m,N}=[3R^2+m d/N, 3R^2+m d/N+3B/N]`.

These clusters are disjoint because

`d-3B = 1000-3(2sqrt(11000)+1) > 367.7 >0`.

Choose `m=N-1` and let

`L_N=3R^2+(N-1)d/N`,

`s_N=L_N+u_N`.

On every `J_{k,N}`,

`g_N(y) >= c_0 1_{J_{k,N}}(y)`,

with

`c_0=1/[2(R_+ +1)]`.

For every ordered triple `k_1+k_2+k_3=N-1`, all three translated interval widths are at least `u_N`. Therefore, at offset `u_N`,

`(1_[0,w_1]*1_[0,w_2]*1_[0,w_3])(u_N)=u_N^2/2`.

There are exactly `binom(N+1,2)=N(N+1)/2` such ordered triples. Hence

`p_N(s_N)
 >= [N(N+1)/2] c_0^3 [u_N^2/2]
 = [(N+1)/N] c_0^3 R^2
 >= R^2/[8(R_+ +1)^3]`.

Numerically,

`R^2/[8(R_+ +1)^3] = 0.001053070209833...`.

Now define a point halfway through the gap after the `m=N-1` cluster:

`t_N=L_N+(3B+d)/(2N)`.

Because `d>3B`, this lies strictly between the end of cluster `K_{N-1,N}` and the start of `K_{N,N}`. Thus

`p_N(t_N)=0`.

Moreover

`|t_N-s_N|
 = [(3B+d)/2-2R]/N
 = 616.142654451.../N ->0`.

The fixed positive oscillation at a vanishing spatial scale proves the theorem.

### Every member of the counterexample family is nevertheless bounded and continuous

This obstruction is deliberately **not** a counterexample to the QFORM density conjecture or to continuity of any individual output.

Each `g_N` lies in `L^1`. The convolution of the first two independent square laws is bounded by the standard same-sign two-square beta-integral estimate (in fact the global diagonal theorem gives the weaker sufficient cap `pi`). Write

`h_N=g_N*g_N in L^infinity`.

Then

`p_N=h_N*g_N`.

Since translation is continuous in `L^1`,

`||tau_u p_N-p_N||_infinity
 <= ||h_N||_infinity ||tau_u g_N-g_N||_1 ->0`.

Thus every `p_N` is uniformly continuous individually and obeys the known diagonal universal `L^infinity` bound. What fails is any **law-uniform** modulus over the extreme family.

### Consequence for the partner route

The common-modulus hypothesis in account03/B15's continuity transfer theorem is valid as a sufficient condition, but cannot be the global closure mechanism for the owner target: it already fails for fixed `A=I_3`, three eigenvalues exactly equal to one, and bounded finite-fragment extreme inputs.

This is a target-valid obstruction that changes the regularity bridge rather than merely weakening a constant.

---

## 4. Exact barycentric representation of admissible densities

The obstruction above suggests that continuity should be transferred by averaging exact continuous representatives, not by extracting an equicontinuous subsequence. The required exact mixture exists.

Let

`D={f in L^1(R): 0<=f<=1 a.e., int f=1}`.

Define the larger weak-star compact convex set

`K={g in L^infinity(R): 0<=g<=1 a.e., int g<=1}`.

Here `int g<=1` is equivalently the family of weak-star closed conditions

`int_[-R,R] g <=1` for every `R>0`,

because `g>=0`. Hence `K` is weak-star closed in the unit ball of `L^infinity=(L^1)^*`; Banach-Alaoglu makes it compact. Since `L^1(R)` is separable, this weak-star compact set is metrizable.

### Lemma 4.1 — extreme points of `K`

The extreme points of `K` are exactly

`{1_E: E measurable, |E|<=1}`.

Proof. Every such indicator is extreme: if `1_E=(g+h)/2` with `0<=g,h<=1`, then on `E` both functions equal one and off `E` both equal zero. Conversely, if `g` takes values strictly between zero and one on a set of positive measure, choose a finite-measure positive-measure subset on which `epsilon<=g<=1-epsilon`, split it into two pieces of equal measure, and perturb by `+/- delta(1_F-1_G)` with small `delta`. Both perturbed functions stay in `K`, remain distinct, and average to `g`. Thus a non-indicator is not extreme. QED.

### Theorem 4.2 — `QFORM-EXACT-INDICATOR-CHOQUET-v1`

For every `f in D`, there is a probability measure `Pi_f` on indicators `1_E` with `|E|=1` such that `f` is their weak-star barycenter:

`int phi(x) f(x) dx
 = int [int_E phi(x) dx] dPi_f(E)`

for every `phi in L^1(R)`.

Proof. By the classical Choquet theorem for compact metrizable convex subsets of locally convex spaces, `f in K` is the barycenter of a probability measure supported on `ext(K)`. Thus the representing extremes are indicators with mass at most one. Test the barycenter identity against `1_[-R,R]` and let `R->infinity`. Monotone convergence gives

`1=int f = int |E| dPi_f(E)`.

Since `|E|<=1` almost surely, necessarily `|E|=1` almost surely. QED.

This exact representation is stronger for the present purpose than an `L^1`-limit of finite convex mixtures: no common modulus is needed to pass continuity through a limiting subsequence.

For independent marginals `f_1,...,f_n`, choose the representing `Pi_i` independently. Repeated use of the barycenter identity gives the exact product-law mixture

`prod_i f_i(x_i) dx
 = int [prod_i 1_{E_i}(x_i) dx] d(Pi_1 x ... x Pi_n)(E)`

as probability measures. The identity first holds on bounded rectangles and extends by the monotone-class theorem.

---

## 5. Continuity transfer with no common modulus

### Theorem 5.1 — `QFORM-CONTINUITY-CHOQUET-TRANSFER-v1`

Fix `n` and a real symmetric matrix `A`. Assume there is a finite `C` such that for **every** measure-one product indicator `E=(E_1,...,E_n)`, the output law

`mu_E=(x^T A x)_# 1_{E_1 x ... x E_n} dx`

has an individually continuous density `p_E` satisfying

`||p_E||_infinity <= C`.

No common modulus of continuity is assumed.

Then for every admissible collection of measurable marginal densities `f_i in D`, the output law has a continuous density `p_f` satisfying

`||p_f||_infinity <= C`.

### Proof

Take the exact product barycentric measure `Pi=Pi_1 x ... x Pi_n` from Theorem 4.2. Pushforward commutes with the exact mixture:

`mu_f = int mu_E dPi(E)`.

Because every `mu_E<=C dx`, it follows immediately that `mu_f<=C dx`; this recovers the central bound without any continuity argument.

For the stronger conclusion, use the unique continuous representative `p_E`. For fixed `t`, `E -> p_E(t)` is measurable. One concrete representation is

`p_E(t)=lim_{m->infinity} (m/2) mu_E([t-1/m,t+1/m])`,

valid by continuity of `p_E`. The interval probabilities are Borel functions of `E`: truncate input space to bounded boxes, approximate the bounded-box shell kernel in `L^1` by finite sums of rectangles, and then let the box grow.

Define

`p_f(t)=int p_E(t) dPi(E)`.

The common bound `|p_E(t)|<=C` permits dominated convergence in the **mixture parameter**. Therefore whenever `t_j->t`,

`p_f(t_j)=int p_E(t_j)dPi(E) -> int p_E(t)dPi(E)=p_f(t)`.

So `p_f` is continuous, with `||p_f||_infinity<=C`. Finally Tonelli/Fubini gives, for every Borel set `B`,

`int_B p_f(t)dt
 = int [int_B p_E(t)dt] dPi(E)
 = int mu_E(B)dPi(E)
 = mu_f(B)`.

Thus `p_f` is the desired continuous density. QED.

### Interpretation

The theorem cleanly separates the two obligations:

1. The central conjecture is still exactly the universal extreme interval bound, as proved by the partner.
2. To upgrade that result to a continuous representative, one does **not** need a common Steklov/equicontinuity modulus. It is enough to prove individual continuity on every extreme product-indicator law and retain the same universal `L^infinity` bound.

This is strictly more permissive: Theorem 3.1 shows that a common modulus is impossible even in a fixed diagonal target family, whereas Theorem 5.1 remains applicable there.

The theorem currently requires continuity on all measurable measure-one extreme sets, not merely the finite-fragment dense subclass. Section 3 shows why finite-fragment continuity plus a common `L^infinity` bound cannot be upgraded by a uniform-modulus compactness shortcut. A further exact closure argument from finite fragments to arbitrary extremes would be a separate obligation.

---

## 6. What changed and what remains open

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`. No universal dimension- and matrix-independent density constant is proved.

**MECHANISM CHANGE:** `common-modulus/equicontinuity transfer -> exact Choquet barycentric transfer`, after a target-valid finite-fragment obstruction proves that a common modulus cannot exist even for `A=I_3`.

The exact regularity picture is now:

- AC is already proved under far weaker hypotheses (`A !=0`).
- Fixed-`A` essential boundedness is already proved for rank at least three, but with a matrix-dependent constant.
- The partner's extreme small-ball theorem is exactly equivalent to the missing universal essential bound.
- Continuity is a separate upgrade. Uniform equicontinuity of extreme outputs is false, but exact barycentric averaging shows that **individual** extreme continuity plus the universal bound is sufficient.

The first unpaid central implication remains the partner's exact shell estimate:

`|{x in prod E_i : x^T A x in I}| <= C |I|`

uniformly in target-admissible `A`, dimension, intervals `I`, and measure-one extreme sets (equivalently, for the central `L^infinity` target, finite fragments suffice by the consumed partner theorem).

The first unpaid continuity implication is now sharper and weaker than before:

> prove that every target-admissible product-indicator extreme output has an individually continuous density, or find a genuine target-valid discontinuous output density.

No law-uniform modulus should be sought: Theorem 3.1 rules it out.

## 7. Source pins and integrity

- Owner/control source at publication recheck: `yspennstate/math-research-brain@e68cdd37eb60e13d31ec1b6a5d2fa599053a89c9`; protected control blobs remained on revision `2026-09-22.5`.
- Assigned partner report: `yspennstate/math-open-problems@40946450aa2bfb06068a2c688d4407be10470c22`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260922T122718Z-account03-B15-qform-r11/REPORT.md`.
- Previous account02/B15 fixed-matrix regularity report: `yspennstate/math-open-problems@60e7f51716e67553ce759519f9801ff3674dcce9`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T120155Z-account02-B15-qform-r1/REPORT.md`.
- Compatible convex-hull source underlying the partner reduction: `account01/B13`, `yspennstate/math-open-problems@f5c63b29011eb394cd621ecc887fe3331aa485af`.

The numerical values in Theorem 3.1 were checked directly from their displayed closed forms; they are not evidence for the analytic proof. No continuity statement is used to infer an `L^infinity` bound. No moment, support, log-concavity, rotation-independence, or centered-interval assumption is introduced. Full QFORM remains **OPEN**.
