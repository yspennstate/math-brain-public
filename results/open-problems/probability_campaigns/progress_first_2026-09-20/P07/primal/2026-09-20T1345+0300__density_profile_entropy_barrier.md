Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but authenticated completed-run effort telemetry is unavailable, so I do not claim otherwise.

# P07-A — density-profile barrier, entropy-optimal soft tilt, and a new prime flat-support theorem

**Native role:** `P07-A`, task `6aa7b46f70a8819184095c277974c256`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured pre-write master:** `bef813d47cd06e18e1b465073e016df65027c59d`  
**Previous own substantive checkpoint:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T1245+0300__adjacent_mask_one_harmonic_fourth_collision.md`.  
**Complementary P07-B checkpoint consulted:** `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T1311+0300__near_sqrt_support_barrier.md`; the empirical-MGF input below is inherited from P07-B's earlier `2026-09-20T0927+0300__gibbs_radial_exceptional_frequencies.md`. P07-B owns the Fourier-dual / exceptional-frequency attack. The present report stays on primal positive certificates, support geometry and information projection.

**Outside target:** Bandeira et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 18.  
**Primary partial-result paper:** A. S. Bandeira, J. Błasiok, D. Dmitriev, U. Faure, A. Kireeva, D. Kunisky, *The Lovász number of random circulant graphs*, arXiv:2502.16227.  
**Exact source model:** odd `n`; the `(n-1)/2` conjugate nonzero difference pairs are selected independently with probability `1/2`.  
**Endpoint:**
\[
\mathbb E\,\vartheta(G_n)=(1+o(1))\sqrt n.
\]
The bounded assignment-time/current check on 20 September 2026 again found the primary paper describing the exact asymptotics as open and retaining the upper bound only up to the iterated-log loss,
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]
This is bounded evidence, not a worldwide novelty certificate.

The fixed full-source metric is therefore unchanged:
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
Status: **OPEN / PROVED PARTIAL**. The prime-order theorems below are restricted results. The density/entropy statements below are high-probability structural results and do not by themselves prove the expectation endpoint. External novelty is **UNVERIFIED**.

---

## 0. Preserved predecessor handoff: SRG69 remains OPEN / PARTIAL

The reassigned predecessor is preserved under

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/rotations/SHPECTOROV-ZHAO-2026-SRG69/`

with frozen `R_SRG69=1`, status **OPEN / PARTIAL**. Preserve its no-Cayley theorem, rooted `L/B/C` feasibility system, centered spectral transfer, endpoint/cycle filters, block-moment and Gram reductions, low-rank residual work and star-complement handoff. Nothing here edits that root or calls SRG69 solved.

---

# 1. Source notation and the inherited Gaussian radial field

Put
\[
M=\{1,\dots,m\},\qquad m=(n-1)/2,
\]
and let `D\subset M` be the random selected pair set, `d=|D|`. For a pair site `j\in M`, define
\[
\phi_a(j)=\cos(2\pi aj/n),
\qquad
X_D(j)=\frac1{\sqrt n}\sum_{a\in D}\phi_a(j).
\tag{1.1}
\]
Let `q_0` denote the uniform probability on the pair sites `M`. Since `X_D(j)=X_D(-j)`, this is exactly the same empirical law as the uniform law on `Z_n\setminus\{0\}` used by P07-B.

If `w` is a probability on the pair sites whose selected cosine moments are exactly flat,
\[
\sum_{j\in M}w_j\phi_a(j)=-\delta
\qquad(a\in D),
\tag{1.2}
\]
then summing over `a\in D` gives the exact radial identity
\[
\boxed{
\mathbb E_w X_D=-\frac{d\delta}{\sqrt n}.
}
\tag{1.3}
\]
Under the fair source law,
\[
\frac dn\xrightarrow{\mathbb P}\frac14.
\tag{1.4}
\]

P07-B proved, for every fixed real `beta`, the empirical moment-generating convergence
\[
A_D(\beta):=\mathbb E_{q_0}e^{-\beta X_D}
\xrightarrow{\mathbb P}e^{\beta^2/32},
\tag{1.5}
\]
with the first two derivatives on compact `beta` intervals. In particular the empirical measure of `X_D` converges in probability to
\[
N(0,1/16).
\tag{1.6}
\]
The exponential-moment convergence gives the uniform integrability needed below for fixed lower-tail quantiles. This report uses (1.5) as a shared lemma and does not reprove P07-B's dual argument.

---

# 2. New all-order lemma: zero frequency is a largest spectral atom of every optimal circulant primal

This is independent of the probabilistic source and will be useful when translating certificate spread back to the theta optimizer.

Let `f:Z_n->R` be a cyclically averaged optimal theta primal for a circulant graph, normalized by
\[
f(0)=1,
\]
with `f` zero on the edge differences. Let
\[
\mu(k)=\frac{\widehat f(k)}n.
\]
Positive definiteness gives `mu>=0`, evenness gives `mu(k)=mu(-k)`, and `sum_k mu(k)=1`. The objective is
\[
T:=\vartheta(G)=\sum_xf(x)=n\mu(0).
\tag{2.1}
\]

## Theorem P07-A.25 — spectral peak at zero

For every `k in Z_n`,
\[
\boxed{\mu(k)\le\mu(0)=T/n.}
\tag{2.2}
\]
Consequently
\[
\boxed{
\sum_{x\in Z_n}f(x)^2\le T.
}
\tag{2.3}
\]

### Proof

For fixed `k`, define
\[
f^{[k]}(x):=f(x)\cos(2\pi kx/n).
\tag{2.4}
\]
It still satisfies `f^[k](0)=1` and still vanishes on every edge difference. Its spectral probability is
\[
\mu^{[k]}(j)=\frac12\bigl(\mu(j-k)+\mu(j+k)\bigr)\ge0,
\tag{2.5}
\]
so `f^[k]` is positive definite and is another feasible theta primal. Its objective is
\[
\sum_x f(x)\cos(2\pi kx/n)=\widehat f(k)=n\mu(k).
\]
Optimality of `f` therefore implies `n mu(k)<=T=n mu(0)`, proving (2.2).

Parseval and `sum mu=1` give
\[
\sum_xf(x)^2=n\sum_k\mu(k)^2
\le n\|\mu\|_\infty\sum_k\mu(k)
=T,
\]
proving (2.3). `square`

For a graph and its complement, vertex transitivity gives `T T^c=n`; hence their optimal spectral laws satisfy the exact min-entropy complementarity
\[
\boxed{
\|\mu_G\|_\infty\,\|\mu_{\bar G}\|_\infty=1/n.
}
\tag{2.6}
\]
This does not yet control the fourth-collision term from the preceding P07-A report, but it is a new deterministic spread constraint on every optimal spectrum.

---

# 3. New prime theorem: every exact flat positive certificate uses at least `d` nonzero frequency pairs

Now specialize only this section to an odd prime `p`. Let
\[
P=\{1,\dots,(p-1)/2\},\qquad D\subset P,\qquad d=|D|.
\]
Consider an arbitrary symmetric probability on `Z_p`, allowed to have an atom at the origin. Aggregate its nonzero mass into pair weights `w_j>=0`, `j in P`, and let
\[
S=\{j\in P:w_j>0\},\qquad k=|S|.
\]
Assume its selected moments are exactly flat at a strictly negative level,
\[
w_0+\sum_{j\in S}w_j\cos(2\pi aj/p)=-\delta
\qquad(a\in D),
\qquad \delta>0.
\tag{3.1}
\]

## Theorem P07-A.26 — prime flat-support lower bound

Every certificate satisfying (3.1) obeys
\[
\boxed{k\ge d.}
\tag{3.2}
\]

### Proof

Define the even function on `Z_p`
\[
h(a)=w_0+\sum_{j\in S}w_j\cos(2\pi aj/p)
\tag{3.3}
\]
and
\[
g(a)=h(a)+\delta.
\tag{3.4}
\]
By (3.1), `g` vanishes on every element of `+-D`, so
\[
|\operatorname{supp}g|\le p-2d.
\tag{3.5}
\]
Also
\[
g(0)=1+\delta>0,
\]
so `g` is nonzero. Its Fourier support is contained in
\[
\{0\}\cup(\pm S),
\]
hence
\[
|\operatorname{supp}\widehat g|\le1+2k.
\tag{3.6}
\]
For prime cyclic groups, the Chebotarev/Tao uncertainty principle gives every nonzero `g` the sharp support inequality
\[
|\operatorname{supp}g|+|\operatorname{supp}\widehat g|\ge p+1.
\tag{3.7}
\]
Combining (3.5)--(3.7),
\[
(p-2d)+(1+2k)\ge p+1,
\]
which is exactly `k>=d`. `square`

### Meaning

This is stronger than a statement about an optimizer: **every** exact-flat positive certificate on prime order has nonzero pair support at least the number of selected constraints. In the fair source model,
\[
d=(1/2+o_{\mathbb P}(1))\frac{p-1}{2},
\]
so every such certificate uses asymptotically at least half of all pair sites. A sparse hard-support construction cannot be the sharp primal mechanism on prime orders.

---

# 4. New density-profile theorem: bounded-density flat certificates cannot reach constant one

The support theorem by itself does not distinguish a uniform measure on a large support from a soft nonuniform tilt. The source Gaussian field does.

For a probability `w` on the pair sites define its density cap relative to `q_0` by
\[
L(w):=m\|w\|_\infty.
\tag{4.1}
\]
Thus `L=1` is the uniform law, while a uniform law on a fraction `q` of the pair sites has `L=1/q`.

Let `phi` and `Phi` denote the standard normal density and distribution functions and set, for fixed `L>=1`,
\[
\boxed{
\lambda(L):=L\,\phi\!\left(\Phi^{-1}(1/L)\right).
}
\tag{4.2}
\]

## Theorem P07-A.27 — source density-cap barrier

Fix `L>=1`. Under the exact fair random-circulant source law, with probability tending to one, simultaneously for every pair-site probability `w=w(D)` satisfying
\[
m\|w\|_\infty\le L
\tag{4.3}
\]
and the exact-flat equations (1.2),
\[
\boxed{
\sqrt n\,\delta\le\lambda(L)+o(1).
}
\tag{4.4}
\]
The `o(1)` is source-probabilistic and is uniform over all such adaptive `w` for fixed `L`.

### Proof

Condition on a realized mask `D` and abbreviate the `m` real numbers in (1.1) by
\[
x_j=X_D(j),\qquad j\in M.
\]
Among all weights satisfying
\[
w_j\ge0,\qquad \sum_jw_j=1,\qquad w_j\le L/m,
\tag{4.5}
\]
the minimum of `sum_j w_j x_j` is obtained by placing mass `L/m` on the smallest `m/L` values, with at most one fractional boundary weight. This is the elementary rearrangement/linear-program rule for a capped simplex.

Let `F_D` be the empirical distribution of the `x_j`. By (1.5)--(1.6), `F_D` converges in probability to the law of
\[
X=Z/4,\qquad Z\sim N(0,1),
\]
and the fixed exponential moments from (1.5) make the lower-tail first moments uniformly integrable. Therefore the capped-simplex minimum converges in probability to
\[
L\int_0^{1/L}F_X^{-1}(u)\,du.
\tag{4.6}
\]
Writing `z_L=Phi^{-1}(1/L)` and using
\[
\int_{-\infty}^{z}t\phi(t)\,dt=-\phi(z),
\]
(4.6) is
\[
-\frac L4\phi(z_L).
\tag{4.7}
\]
Hence every `w` satisfying (4.3) obeys, uniformly,
\[
-\mathbb E_wX_D\le\frac14\lambda(L)+o_{\mathbb P}(1).
\tag{4.8}
\]
If `w` is also exactly flat, (1.3) gives
\[
\sqrt n\,\delta
=\frac nd\bigl(-\mathbb E_wX_D\bigr).
\]
Since `n/d=4+o_P(1)`, (4.4) follows. `square`

### The critical cap

The function `lambda(L)` is increasing from `0` to infinity. The equation
\[
\lambda(L_*)=1
\tag{4.9}
\]
has the equivalent form
\[
\frac{\phi(z_*)}{\Phi(z_*)}=1,
\qquad L_*=1/\Phi(z_*),
\]
and numerically
\[
\boxed{
z_*\approx-0.30263084,\qquad
L_*\approx2.62408233.}
\tag{4.10}
\]
Therefore a sharp-depth certificate
\[
\delta\ge(1-o(1))/\sqrt n
\]
must have density peak at least
\[
\boxed{m\|w\|_\infty\ge L_*-o(1).}
\tag{4.11}
\]
This is a structural necessity, not a construction.

---

# 5. Prime obstruction to all uniform-on-support certificate strategies

Combine Theorems P07-A.26 and P07-A.27. Let `p` be prime and suppose an exact-flat pair-site certificate is **uniform on its support** `S`, with `k=|S|`. Then
\[
L(w)=m/k.
\]
The prime uncertainty theorem gives `k>=d`. In the fair source model `d/m->1/2`, hence
\[
L(w)\le \frac md=2+o_P(1).
\tag{5.1}
\]
Applying the density-cap theorem at any fixed `2+epsilon` and then sending `epsilon` down to zero gives
\[
\boxed{
\sqrt p\,\delta
\le\lambda(2)+o_P(1)
=\sqrt{\frac2\pi}+o_P(1)
\approx0.79788456+o_P(1).
}
\tag{5.2}
\]
Consequently the theta upper certificate generated by any such uniform-support flat law is no better than
\[
1+\frac1\delta
\ge
\left(\sqrt{\frac\pi2}-o_P(1)\right)\sqrt p,
\qquad
\sqrt{\frac\pi2}\approx1.25331414.
\tag{5.3}
\]

**Important interpretation.** Equation (5.3) is **not** a lower bound on the actual Lovasz number and is **not** evidence against Conjecture 18. It is a barrier for a whole proof strategy: choose a support and put essentially uniform mass on it. Even the optimally chosen lower half of the asymptotically Gaussian radial field reaches only the coefficient `sqrt(2/pi)`. The sharp constant requires genuinely nonuniform positive weights.

This also explains why a hard-threshold construction suggested by the earlier support-entropy work cannot close the conjecture on primes. The Gaussian lower-tail fraction needed to produce coefficient one under an ideal capped selector is
\[
1/L_*\approx0.3811,
\]
but exact prime flatness requires at least asymptotic pair fraction `1/2` in the support.

---

# 6. New entropy theorem: the sharp certificate has a universal information cost of at least one half nat

The preceding density theorem says the weights must be nonuniform. The correct soft nonuniformity is identified by relative entropy.

Keep the pair-site uniform law `q_0` and let `w` be any pair-site probability satisfying the exact-flat equations (1.2). For fixed `beta>0`, the Gibbs variational inequality gives
\[
D_{KL}(w\|q_0)
\ge
-\beta\,\mathbb E_wX_D-\log A_D(\beta).
\tag{6.1}
\]
Using the exact radial identity (1.3),
\[
D_{KL}(w\|q_0)
\ge
\beta\frac{d\delta}{\sqrt n}-\log A_D(\beta).
\tag{6.2}
\]

## Theorem P07-A.28 — entropy cost of source-scale flat depth

Suppose along a source-typical sequence of masks
\[
\sqrt n\,\delta\to c>0.
\]
Then
\[
\boxed{
D_{KL}(w\|q_0)\ge\frac{c^2}{2}-o_P(1).
}
\tag{6.3}
\]
In particular every sharp-depth certificate `c=1` has
\[
\boxed{
D_{KL}(w\|q_0)\ge\frac12-o_P(1).
}
\tag{6.4}
\]

### Proof

By (1.4)--(1.5), the right side of (6.2) converges for fixed `beta` to
\[
\frac{\beta c}{4}-\frac{\beta^2}{32}.
\tag{6.5}
\]
The maximum over `beta>=0` occurs at
\[
\beta=4c
\]
and equals `c^2/2`. `square`

So the conjectured constant has a very specific information-geometric price: asymptotically **one half nat** of relative entropy away from the uniform nonzero-site law.

---

# 7. The radial Gibbs law pays exactly that minimum entropy cost

Define the P07-B radial Gibbs law
\[
\frac{dp_{\beta,D}}{dq_0}(j)
=\frac{e^{-\beta X_D(j)}}{A_D(\beta)}.
\tag{7.1}
\]
The derivative form of (1.5) gives
\[
\mathbb E_{p_{\beta,D}}X_D
=-\frac{d}{d\beta}\log A_D(\beta)
\xrightarrow{\mathbb P}-\frac\beta{16}.
\tag{7.2}
\]
Define its **average** selected depth by
\[
\bar\delta_{\beta,D}
:=-\frac1d\sum_{a\in D}\mathbb E_{p_{\beta,D}}\phi_a.
\]
Then (1.3), without requiring individual moments to be equal, gives
\[
\boxed{
\sqrt n\,\bar\delta_{\beta,D}
\xrightarrow{\mathbb P}\frac\beta4.
}
\tag{7.3}
\]
Also
\[
\begin{aligned}
D_{KL}(p_{\beta,D}\|q_0)
&=-\beta\mathbb E_{p_{\beta,D}}X_D-\log A_D(\beta)\\
&\xrightarrow{\mathbb P}
\frac{\beta^2}{32}.
\end{aligned}
\tag{7.4}
\]
Putting `beta=4c`,
\[
\boxed{
\sqrt n\,\bar\delta_{4c,D}\to c,
\qquad
D_{KL}(p_{4c,D}\|q_0)\to c^2/2.
}
\tag{7.5}
\]
Thus the radial Gibbs law exactly saturates the entropy lower bound from Theorem P07-A.28. At the conjectured coefficient `c=1`, the distinguished tilt is
\[
\boxed{\beta_*=4,\qquad D_{KL}\to1/2.}
\tag{7.6}
\]

This is the sharp conceptual change of this run. The radial scale is not merely correct: among all laws producing that radial displacement, the soft Gibbs tilt is asymptotically information-optimal. The only remaining issue is **transverse equalization** of its selected moments.

---

# 8. Exact information-projection gap and a sharply localized conditional closure lemma

The earlier P07-A profiled-Gibbs report constructed, for each radial parameter, a unique exactly-flat exponential-family law by minimizing over transverse tilts. In the present normalization, compare at the same `beta`:

* `p_rad,beta` has natural parameter `(beta/sqrt n) 1_D`;
* `p_flat,beta` adds the unique transverse parameter making every selected moment equal.

Because the transverse parameter is orthogonal to the flat moment vector, direct exponential-family algebra gives the exact identity
\[
\boxed{
\Gamma_D(\beta)
:=D_{KL}(p_{flat,\beta}\|p_{rad,\beta})
=\psi(\lambda_{rad})-\psi(\lambda_{flat})\ge0.
}
\tag{8.1}
\]
This is precisely the information-projection cost of enforcing exact flatness.

There is a useful deterministic/probabilistic implication near the critical tilt. Under `p_rad,beta`, the centered MGF of `X_D` is an explicit ratio of the empirical partition functions `A_D`. Since P07-B proved convergence of `A_D` and its first two derivatives on compact beta intervals, for every fixed compact interval around `beta=4`, with source probability tending to one the local cumulant curvature of `X_D` under `p_rad,beta` is bounded by an absolute constant. The entropy inequality then gives, whenever `Gamma_D(beta)` is small,
\[
\boxed{
|\mathbb E_{p_{flat,\beta}}X_D
-\mathbb E_{p_{rad,\beta}}X_D|
\le C\sqrt{\Gamma_D(\beta)}+o_P(1).
}
\tag{8.2}
\]
Indeed apply the variational inequality to `+tX_D` and `-tX_D` relative to `p_rad,beta`, use the local quadratic cumulant bound, and optimize `t`.

Therefore:

## Conditional closure target `IP4`

If one proves
\[
\boxed{\Gamma_D(4)=o_P(1),}
\tag{8.3}
\]
(or a uniform version in a fixed neighborhood of `4`), then the exactly-flat profiled certificate satisfies
\[
\boxed{
\sqrt n\,\delta_{flat}(4)=1-o_P(1),
}
\tag{8.4}
\]
and hence
\[
\sqrt n\,\delta_D\ge1-o_P(1).
\tag{8.5}
\]
This yields the sharp constant in probability for the corresponding theta side. It does **not**, by itself, close the requested expectation theorem: an exceptional-tail / uniform-integrability estimate is still required. The preceding P07-A reciprocal-tail and weighted fourth-collision criteria are available for that final expectation step.

The significance is that `IP4` is now the exact primal bottleneck. A generic partial-Fourier RIP theorem is unnecessary. A hard-support selector is provably incapable of reaching the coefficient. The correct candidate is the entropy-optimal soft tilt at `beta=4`, and the missing theorem is that flattening its transverse moments costs asymptotically zero additional information.

---

# 9. What changed, what did not, and why this is progress

### Newly proved in this run

1. **All odd `n`: spectral peak theorem.** For every cyclically averaged optimal theta primal, zero frequency is a largest spectral atom, and `sum_x f(x)^2<=theta(G)`.
2. **Prime order: exact flat-support theorem.** Every positive exact-flat certificate uses at least `d` nonzero conjugate frequency pairs.
3. **Exact source high probability: density-cap theorem.** Any exact-flat pair-site certificate with density cap `L` has depth coefficient at most `lambda(L)=L phi(Phi^{-1}(1/L))`.
4. **Prime source method obstruction.** Uniform-on-support flat certificates are capped at `sqrt(2/pi)` in depth and therefore cannot produce a theta certificate with leading constant below `sqrt(pi/2)≈1.2533`.
5. **Entropy barrier.** Depth coefficient `c` costs at least `c^2/2` nats relative to the uniform pair law.
6. **Entropy optimality of the soft radial tilt.** The Gibbs law at `beta=4c` attains both radial coefficient `c` and entropy cost `c^2/2`; the conjectured coefficient singles out `beta=4` and cost `1/2`.
7. **Localized remaining lemma.** It is enough on the primal side to show that the information projection from the `beta=4` radial Gibbs law to the exactly-flat profile has `KL=o_P(1)`, followed by a quantitative expectation-tail step.

### Not proved

* No arbitrary-`n` improvement of `C sqrt(n log log n)` is claimed.
* `Gamma_D(4)=o_P(1)` is not proved here.
* High-probability depth alone is not claimed to imply the expectation endpoint.
* The prime uniform-support obstruction is a statement about a certificate strategy, not a lower bound on `theta` and not a counterexample to Conjecture 18.
* External publication novelty of these structural lemmas is unverified.

---

# 10. Next primal attack and complementary P07-B handoff

The next P07-A attack should stay at the critical soft tilt rather than return to sparse-support constructions.

1. Write the exact projection cost as `Gamma_D(4)=psi(lambda_rad)-varphi(s_*)`, with `s_*=4 sqrt(d/n)=2+o_P(1)` in the profiled coordinates.
2. Use the previous exact transverse covariance Schur-complement formula and the P07-B second-order residual identities to bound `Gamma_D(4)` directly, rather than demanding a global minimum singular value for the whole Fourier system.
3. A sufficient quantitative target is a source-high-probability estimate `Gamma_D(4)=o(1)` plus a tail strong enough that the earlier reciprocal / weighted fourth-collision criterion upgrades probability to expectation.
4. If `Gamma_D(4)` does not vanish, quantify its positive limit. By (8.2), that would produce a genuine obstruction to the sharp constant for this entire Gibbs-profile mechanism and force a new certificate family.

**Shared exact handoff to P07-B:** the primal side has now identified `beta=4` as the unique entropy-optimal critical radial tilt and proved that hard/uniform support selection is structurally subcritical on prime source masks. P07-B can continue to own exceptional-frequency and interpolation estimates at that fixed tilt; P07-A owns the information-projection/positive-certificate conversion and expectation upgrade. No P07-B source claim is taken here.
