Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# C0031 — Bernoulli-skeleton reduction and a polynomial-LCD bridge at one stretched-exponential scale

Date: 2026-09-19 UTC  
Worker: `R7-05 Sharp Inequality Research`  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Canonical target: `C0031`, Bordenave–Chafaï heavy-tailed circular-law almost-sure upgrade  
Methods: **B1 / B11 / B30**  
Captured pre-write master: `85915e86c485d15ae8d1461d306ed4c54c147092`

## 1. Cumulative starting point and exact recovery action

The frozen source metric is `BC_AS`: it is 1 only if the full Bordenave–Chafaï source-scope almost-sure theorem is proved without the bounded-density hypothesis, and 0 otherwise. It enters this run at 0.

The preceding STUCK1 diagnosis isolated, for every fixed Hermitization shift `z` and every `q` with `0<q<q_*`, the sole remaining lower-log defect

`U_{n,q}(z) = (1/n) sum_i log(1/s_i(A_n(z))) 1_{s_i(A_n(z))<exp(-n^q)}`,

where `A_n(z)=a_n^{-1}X_n-zI`. All logarithmic mass above `exp(-n^q)` is already controlled almost surely. A sufficient endpoint is therefore the eventual floor

`s_min(A_n(z)) >= exp(-n^q)`.

STUCK1 selected exactly one recovery action: start with the source-valid symmetric discrete-Pareto benchmark, write each entry as a heavy magnitude times an independent sign, freeze the magnitudes, and attack the remaining sign problem through random-normal arithmetic. This run executes that recovery action without replacing it.

For the benchmark, fix `0<alpha<2` and let

`P(xi=k)=P(xi=-k)=c_alpha k^(-1-alpha),  k=1,2,...`,

where `c_alpha=(2 zeta(1+alpha))^{-1}`. Equivalently

`xi = epsilon R`,

where `epsilon` is an independent Rademacher sign and

`P(R=k)=k^(-1-alpha)/zeta(1+alpha)`.

In particular

`p_* := P(R=1)=1/zeta(1+alpha)>0`.

This law is purely atomic and belongs to the symmetric alpha-stable domain of attraction. For it, `log a_n=O(log n)`.

## 2. B1 — change category: extract a clean Bernoulli skeleton

### 2.1 Obstruction first: larger amplitudes are not monotonically better for anti-concentration

It is false that replacing Rademacher coefficients by larger absolute coefficients can only decrease concentration. With two signs,

`epsilon_1 + 3 epsilon_2`

has four distinct values, each with mass `1/4`, while

`3 epsilon_1 + 3 epsilon_2`

has an atom of mass `1/2` at zero. Thus the pointwise fact `R_j>=1` does **not** permit comparison of the weighted sign sum with the all-unit Rademacher sum. Any valid argument has to preserve an actual independent constant-amplitude subfamily or use weighted arithmetic structure.

### 2.2 Exact unit-magnitude thinning lemma

For a finite coefficient vector `v=(v_1,...,v_n)` and independent pairs `(epsilon_j,R_j)`, define

`J={j:R_j=1}`.

Let

`Q(Y,r)=sup_w P(|Y-w|<=r)`

be the Lévy concentration function (real or complex disk, as appropriate).

**Lemma 1 (unit-atom thinning).** Conditional on `v` and all magnitudes `(R_j)`, for every `r>=0` and every deterministic translation `w`,

`P(|sum_j epsilon_j R_j v_j-w|<=r | v,R)
 <= Q(sum_{j in J} epsilon_j v_j,r)`.

**Proof.** Split the sum into `S_J+T`, where `S_J=sum_{j in J}epsilon_j v_j` and `T=sum_{j notin J}epsilon_j R_j v_j`. Conditional on `v,R` and on all signs outside `J`, `T-w` is a deterministic translation. Hence the conditional probability is at most `Q(S_J,r)`. Average over the outside signs. QED.

This removes every heavy magnitude in the **tested** column from the small-ball problem. The heavy tail remains only indirectly, through the distribution of the random normal vector determined by the other columns.

### 2.3 Random-matrix form

For this section take a fixed **real** shift `z`; this is a deliberately restricted benchmark, not the full Hermitization problem. Put

`M_n(z)=X_n-a_n z I`, so `A_n(z)=a_n^{-1}M_n(z)`.

Let `C_i` be column `i` of `M_n(z)` and `H_i=span{C_j:j!=i}`. Choose a unit real vector `v_i` orthogonal to `H_i`. Since column `i` is independent of the other columns, `v_i` is independent of all random variables in column `i`. Moreover

`dist(C_i,H_i) >= |<C_i,v_i>|`

(with equality when `H_i` is a hyperplane), and

`<C_i,v_i> = sum_j epsilon_{ji}R_{ji}v_{i,j} - a_n z v_{i,i}`.

Therefore Lemma 1 gives the exact conditional bound

`P(dist(C_i,H_i)<=r | v_i,(R_{ji})_j)
 <= Q(sum_{j in J_i} epsilon_{ji} v_{i,j},r)`,          (2.1)

where `J_i={j:R_{ji}=1}`.

The crucial gain is conceptual: the tested-column heavy tail has vanished from (2.1). What remains is a Rademacher concentration problem for a random normal restricted to an independent Bernoulli(`p_*`) coordinate mask.

### 2.4 A general Bernoulli-component extension exists

The above constant-amplitude skeleton is especially clean for the discrete-Pareto benchmark. It is not an isolated phenomenon. Aizenman–Germinet–Klein–Warzel, *On Bernoulli Decompositions for Random Variables, Concentration Bounds, and Spectral Localization* (PTRF 143 (2009), arXiv:0707.0095), prove that any non-degenerate real law admits a representation of the form

`X = W + b(W) sigma`

with `W` independent of a Bernoulli sign variable and with the conditional Bernoulli variance uniformly positive for a suitable parameter choice. Thus a Bernoulli-skeleton strategy can in principle reach far beyond symmetric discrete Pareto. The source-level obstacle becomes weighted random-normal arithmetic because `b(W)` need not be constant or bounded above. I do not use that general decomposition to claim the full endpoint here.

## 3. B11 — dualize: distance to a random span and isolate the exact arithmetic property

The next issue is whether enough of the random normal survives the independent unit-magnitude mask, and how much arithmetic unstructure is actually required.

### 3.1 Stretched-scale delocalization of random normals for the real-shift benchmark

Fix the same `q` as above. Set

`rho_n = exp(-n^q/8)`.

A vector is `rho_n`-compressible on `delta n` coordinates if it lies within Euclidean distance `rho_n` of a vector supported on at most `delta n` coordinates.

The following uses only a published strict-rectangular no-moment theorem plus an elementary heavy-tail maximum bound.

**Lemma 2 (stretched-scale spread).** For the real discrete-Pareto benchmark there exists `delta>0` such that, almost surely for all sufficiently large `n`, simultaneously:

1. any unit vector `x` for which `||M_n(z)x|| <= a_n exp(-n^q)` has at least `delta n` coordinates satisfying

   `|x_j| >= rho_n/sqrt(n)`;

2. for every `i`, every unit normal `v_i in H_i^perp` has at least `delta n` coordinates satisfying

   `|v_{i,j}| >= rho_n/sqrt(n)`.

**Proof.** Because the entry law is non-degenerate, after a fixed deterministic rescaling it satisfies a concentration bound of the form

`sup_lambda P(|xi-lambda|<=1) <= 1-beta`

for some `beta>0`. Tikhomirov's strict-rectangular theorem (*The smallest singular value of random rectangular matrices with no moment assumptions on entries*, Israel J. Math. 212 (2016), arXiv:1409.7975) then supplies constants `u,v>0` such that any `(n-1) x s` or `n x s` submatrix with `s<=delta n` has smallest singular value at least `u sqrt(n)` except with probability `exp(-v n)`, uniformly over the deterministic real diagonal shift, provided `delta` is chosen small enough. Union over the deleted column and all supports costs at most

`n sum_{s<=delta n} binom(n,s) = exp((H(delta)+o(1))n)`.

Choose `delta` with `H(delta)<v/2`. Borel–Cantelli therefore gives, almost surely eventually, the simultaneous tall-block lower bound for all these supports.

Independently, the Pareto tail and a union bound give

`P(max_{j,k}|xi_{jk}| > exp(n^q/64)) <= C n^2 exp(-alpha n^q/64)`,

which is summable. Hence, almost surely eventually,

`||M_n(z)|| <= exp(n^q/16)`,

using `log a_n=O(log n)`.

Now suppose a unit vector `x` is within `rho_n` of an `S`-supported vector `x_S`, `|S|<=delta n`. Then

`||M_n(z)x||
 >= ||M_n(z)_{[:,S]}x_S|| - ||M_n(z)|| rho_n
 >= u sqrt(n)||x_S|| - exp(-n^q/16)`.

For large `n` this exceeds `u sqrt(n)/3`, far larger than `a_n exp(-n^q)`. Thus no near-kernel vector is `rho_n`-compressible. If fewer than `delta n` coordinates of a unit vector had magnitude at least `rho_n/sqrt(n)`, deleting those coordinates would leave Euclidean norm below `rho_n`, contradicting non-compressibility. This proves (1).

For a normal `v_i`, use the same argument with `H_i^*v_i=0` and the `(n-1) x s` tall blocks of `H_i^*`: a `rho_n`-compressible unit normal would force

`u sqrt(n)|| (v_i)_S|| <= ||H_i^*|| rho_n <= exp(-n^q/16)`,

an impossibility for large `n`. The same coordinate-count argument proves (2). QED.

**Scope caution.** Tikhomirov's quoted theorem is stated for real random matrices and real deterministic deformation. The above lemma is therefore claimed only for the fixed real-shift benchmark. Extending this exact step to arbitrary complex `z`, or replacing it by a complex no-moment theorem, remains part of the source-level work.

### 3.2 The independent mask captures stretched-scale normal mass

Let `S_i` be any `delta n` coordinates of `v_i` satisfying Lemma 2. Since `J_i` belongs to the tested column, it is independent of `v_i`. Conditional on `v_i`,

`|J_i cap S_i| ~ Binomial(delta n,p_*)`.

Chernoff therefore gives

`P(|J_i cap S_i| < p_* delta n/2 | v_i) <= exp(-c n)`.

On the complementary event,

`||(v_i)_{J_i}||_2
 >= sqrt(p_* delta n/2) rho_n/sqrt(n)
 = c_0 rho_n`.                                      (3.1)

Thus the random unit-magnitude skeleton does not lose the normal vector: it retains at least stretched-exponential mass with exponentially high probability.

### 3.3 The arithmetic target is only polynomial LCD, not stretched-exponential LCD

This is the main correction to the preceding STUCK diagnosis.

For a nonzero real vector `y`, write `LCD_{L,gamma}(y/||y||)` for the Rudelson–Vershynin least common denominator

`inf{theta>0: dist(theta y/||y||,Z^m)<min(gamma theta,L)}`.

The standard LCD small-ball theorem for independent Rademacher signs implies, for a unit vector `u`,

`Q(sum_j epsilon_j u_j, eps) <= C eps + C exp(-c L^2)`

whenever `eps >= c_1/LCD_{L,gamma}(u)`. By monotonicity of the concentration function, if `D=LCD_{L,gamma}(u)` and a desired radius `t` is **smaller** than `c_1/D`, then

`Q(sum_j epsilon_j u_j,t)
 <= Q(sum_j epsilon_j u_j,c_1/D)
 <= C/D + C exp(-cL^2)`.                              (3.2)

Hence one does **not** need LCD of order `exp(n^q)`. It is enough to prove a polynomial bound

`LCD_{L_n,gamma}((v_i)_{J_i}/||(v_i)_{J_i}||) >= n^(1+eta)`       (3.3)

for any fixed `eta>0`, with a summable failure probability, taking `L_n=K sqrt(log n)` with `K` large enough. Equation (3.2) then gives an `O(n^(-1-eta))` tested-column concentration probability.

This lowers the arithmetic milestone by an exponential amount relative to the STUCK1 heuristic.

## 4. B30 — one scale only: a complete conditional bridge to the desired floor

We now combine the geometric and arithmetic reductions at exactly one scale.

Let

`tau_n = a_n exp(-n^q)`

be the desired raw least-singular threshold. On the good event of Lemma 2, if some unit `x` satisfies `||M_n(z)x||<=tau_n`, then it has a set `I(x)` of at least `delta n` coordinates with `|x_i|>=rho_n/sqrt(n)`.

For each `i in I(x)`, writing `H_i` for the span of all other columns,

`dist(C_i,H_i)
 <= ||M_n(z)x||/|x_i|
 <= tau_n sqrt(n)/rho_n
 =: r_n`.

Thus

`r_n = a_n sqrt(n) exp(-7 n^q/8)`.                         (4.1)

A deterministic averaging argument gives

`1_{s_min(M_n(z))<=tau_n and Lemma-2-good}
 <= (1/(delta n)) sum_{i=1}^n 1_{dist(C_i,H_i)<=r_n}`.       (4.2)

There is no extra union-bound factor `n` after taking expectations; the prefactor `1/(delta n)` cancels it. This point is important for summability.

On the mask-mass event (3.1), the radius in the normalized Rademacher sum is

`t_n := r_n/||(v_i)_{J_i}||
 <= C a_n sqrt(n) exp(-3 n^q/4)
 = exp(-3n^q/4+O(log n)).                                  (4.3)

In particular `t_n << n^{-A}` for every fixed `A`.

### Theorem 3 (one-scale polynomial-LCD bridge)

Fix a real `z`, `0<q<q_*`, and `eta>0`. Suppose that for some sufficiently large constant `K` and the independent tested-column mask `J_i`, a random normal `v_i` satisfies

`P( LCD_{K sqrt(log n),gamma}((v_i)_{J_i}/||(v_i)_{J_i}||) < n^(1+eta),
       ||(v_i)_{J_i}|| >= c_0 rho_n ) =: b_n`,

with

`sum_n b_n < infinity`.                                    (4.4)

Then for the real discrete-Pareto benchmark,

`sum_n P(s_min(A_n(z)) < exp(-n^q)) < infinity`,             (4.5)

and consequently

`s_min(A_n(z)) >= exp(-n^q)`

almost surely for all sufficiently large `n`.

**Proof.** The failures of Lemma 2 and of mask mass (3.1) are summable. On their complement, (4.3) is smaller than `c n^(-1-eta)` for large `n`. If the LCD is at least `n^(1+eta)`, apply (3.2) with `L_n=K sqrt(log n)` and choose `K` so that `exp(-cL_n^2)<=n^(-1-eta)`. Then (2.1) gives

`P(dist(C_i,H_i)<=r_n | good arithmetic data)
 <= C n^(-1-eta)`.

The arithmetic-bad event contributes `b_n`. Average over columns using (4.2):

`P(s_min(M_n(z))<=tau_n)
 <= b_n + C n^(-1-eta) + (summable stretched/exponential errors)`.

The right side is summable by (4.4). Borel–Cantelli proves the eventual floor. Since `s_min(A_n)=a_n^{-1}s_min(M_n)`, this is exactly the displayed normalized statement. QED.

### What Theorem 3 changes

Before this run the recovery action was phrased as needing random-normal anti-structure at denominator scale roughly `exp(n^q)`. Theorem 3 shows that this is far too strong. At the one scale relevant to C0031, **any polynomial LCD exponent strictly bigger than 1 is enough**, provided its failure probability is summable.

The reason is twofold:

1. the desired radius is already stretched-exponentially tiny, so it lies far below `1/LCD` for polynomial LCD;
2. invertibility-via-distance averages over the `delta n` spread coordinates rather than paying an extra factor `n`.

This is the sharpest reduction obtained in the current recovery cycle.

## 5. Exact remaining gap

The discrete-Pareto benchmark is **not solved** here. The remaining theorem is now precise:

> For the random normal `v_i` to the span of the other heavy-tailed columns, and the independent Bernoulli coordinate mask `J_i={j:R_{ji}=1}`, prove for some `eta>0`
>
> `LCD_{K sqrt(log n),gamma}((v_i)_{J_i}/||(v_i)_{J_i}||) >= n^(1+eta)`
>
> outside a sequence of events with summable probabilities.

For real shifts, stretched-scale spread and mask mass are already supplied by Lemma 2 and (3.1). The unresolved issue is therefore genuinely **arithmetic**, not geometric delocalization and not the heavy magnitude in the tested column.

Known finite-second-moment/random-rounding theorems do not automatically provide this for the fixed infinite-variance law. Livshyts's 2018 random-rounding theorem requires moment budgets in its square-matrix conclusion; its own Remark 1.5 notes that a fixed infinite-variance law generally falls outside the convenient i.i.d. corollary. Livshyts–Tikhomirov–Vershynin (2019/2021) likewise assume a Hilbert–Schmidt second-moment budget. The strict-rectangular Tikhomirov theorem is exactly what made Lemma 2 possible, but it does not by itself control the arithmetic structure of the one-dimensional square normal.

## 6. Dated source / prior-art check (2026-09-19 UTC)

- Charles Bordenave and Djalil Chafaï, *Around the circular law*, Probability Surveys 9 (2012), arXiv:1109.3343v4: the heavy-tail theorem gives the general convergence in probability and adds bounded-density regularity for the almost-sure upgrade; the discussion identifies slow control of the smallest singular values as the obstruction.
- Konstantin Tikhomirov, *The smallest singular value of random rectangular matrices with no moment assumptions on entries*, Israel J. Math. 212 (2016), arXiv:1409.7975: strict rectangular aspect ratio, arbitrary deterministic deformation, no moment assumptions; used above only in its stated real rectangular regime.
- Mark Rudelson and Roman Vershynin, *The Littlewood–Offord problem and invertibility of random matrices*, Adv. Math. 218 (2008): LCD small-ball machinery and random-normal arithmetic paradigm.
- Galyna Livshyts, *The smallest singular value of heavy-tailed not necessarily i.i.d. random matrices via random rounding*, arXiv:1811.07038: strong square estimates under explicit moment budgets; fixed infinite-variance distributions are not covered by the simple i.i.d. corollary.
- Galyna Livshyts, Konstantin Tikhomirov, Roman Vershynin, *The smallest singular value of inhomogeneous square random matrices*, Ann. Probab. 49 (2021), arXiv:1909.04219: RLCD plus a Hilbert–Schmidt second-moment budget.
- Michael Aizenman, François Germinet, Abel Klein, Simone Warzel, *On Bernoulli Decompositions for Random Variables, Concentration Bounds, and Spectral Localization*, PTRF 143 (2009), arXiv:0707.0095: any non-degenerate real law has a Bernoulli component with uniformly positive conditional variance.
- Michail Louvaris, *Universality of the least singular value and singular vector delocalisation for Lévy non-symmetric random matrices*, AIHP 61 (2025): exact alpha-stable square ensemble, principally unshifted least-singular universality, not the full shifted stable-domain source class.
- Yi Han, *The smallest singular value for rectangular random matrices with Lévy entries*, arXiv:2412.06246: very-high-confidence heavy-tail bounds for strict aspect ratio `N/n -> a>1`, including deterministic deformation; still not the square hard edge.

A bounded fresh search did not expose a theorem settling the full Bordenave–Chafaï no-density almost-sure endpoint. This is negative evidence only, not an openness or novelty certificate.

## 7. Metric, status, and next attack

Frozen metric: `BC_AS`.

Before: `0`.

After: `0` (**NO MOVEMENT**).

Mathematical status: **PARTIAL / SOURCE OPEN**. This run proves a nontrivial real-shift benchmark reduction: (i) exact heavy-tail-to-unit-sign thinning in the tested column, (ii) stretched-scale spread of both near-kernel vectors and random normals from strict rectangular no-moment invertibility, (iii) exponential-probability mask mass capture, and (iv) a complete bridge showing that a **polynomial** random-normal LCD lower bound `n^(1+eta)` with summable failure already forces the desired stretched-exponential least-singular floor. It does not prove that random-normal LCD statement, does not cover arbitrary complex `z`, and therefore does not settle C0031.

This is ordinary unchanged C0031 research run **4** after the STUCK1 recovery report; the ordinary unchanged count moves `3 -> 4`.

Next nonrepeating Section-B triple: **B24 / B18 / B27**.

- **B24 (extremal object):** characterize the normal vectors for which the thinned LCD is `< n^(1+eta)` and isolate the extremal additive pattern compatible with `H_i^*v_i=0`.
- **B18 (change language):** translate low thinned LCD into additive-energy / generalized-arithmetic-progression structure of a positive-density coordinate subset, then ask whether the independent heavy-tailed rows can annihilate such a structured vector with summable probability.
- **B27 (swap quantifiers):** exploit that Hermitization only needs Lebesgue-a.e. `z`; test whether an estimate integrated over the shift can make the low-LCD exceptional set summable even when a uniform-in-`z` random-normal theorem is too strong.

No independent P26 or distinct OTHER-track audit is claimed.