SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B15, 2026-09-23T14:56:28Z.
attacking: heat-scale Dini/Cauchy closure — separate bounded height from continuity, pass new volume estimates through rough limits, and obtain endpoint heat-recovery rates without a Hölder detour.

# Heat-orbit regularity and rough-limit closure for QFORM density estimates

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Worker:** `fleet03/B15`  
**Run:** `20260923T145628Z-fleet03-B15-qform-auto21`  
**Outcome:** `PROVED_TARGET_LEVEL_REGULARITY_LEMMA / ROUGH_TRACE_COMPILER / PARTNER_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact scope and fresh sources

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. This report supplies a regularity/trace compiler for any new height estimate and applies it quantitatively to the current three-volume branch. It does not assume Gaussian, log-concave, moment-bounded, compact, connected, or post-rotation independent inputs.


The newest volume theorem actually used below is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

Its q-dependent Fourier branch proves, for an original-coordinate cross block M with `Z=e3(M^T M)>0` and third-volume row marginals `alpha_i<=q/2`, `1<=q<3/2`,

\[
 |\phi_Q(t)|\le \min\{1,K_q |t|^{-b}\},\qquad
 b={3\over2q}>1,
\tag{1.1}
\]
with
\[
 K_q=\Bigl[e^3q^{-3/2}\pi^3 Z^{-1/2}\Bigr]^{1/(2q)},
\tag{1.2}
\]
and
\[
 \|p_Q\|_\infty\le {3e\over(3-2q)\sqrt q}\,Z^{-1/6}.
\tag{1.3}
\]
For its nearby-diffuse certificate
\[
M=M_0+E,\quad s_3(M_0)\ge a,\quad
\max_i(P_{\rm range(M_0)})_{ii}\le\tfrac12,\quad
\|E\|_{\rm op}\le a/16,
\tag{1.4}
\]
it takes `q=4/3`, has `s_3(M)>=15a/16`, and obtains
\[
 \|p_Q\|_\infty\le {24\sqrt3 e\over5a}< {23\over a}.
\tag{1.5}
\]

The assigned partner actually applied below is fleet04/B15,

`yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260922T211430Z-fleet04-B15-heat-regularity-r4/REPORT.md`.

For every probability law `mu`, it proves the exact Gaussian heat-height identity
\[
 \sup_{r>0,y}(\mu*\gamma_r)(y)=\|p_\mu\|_\infty,
\tag{1.6}
\]
with value `+infinity` if no bounded density exists, and monotone recovery of the maximum when a `C_0` density exists.

## 2. Exact separation: bounded height versus continuity

Let
\[
 \gamma_r(u)={1\over\sqrt{2\pi}r}e^{-u^2/(2r^2)},\qquad
 H_r(y)=(\mu*\gamma_r)(y).
\tag{2.1}
\]
Every `H_r` lies in `C_0(R)`.

### Theorem 2.1 — `QFORM-HEAT-ORBIT-SEPARATION-v1`

For a probability law `mu`:

1. `mu` has a bounded density iff the heat orbit is uniformly bounded,
\[
 \sup_{r>0}\|H_r\|_\infty<\infty,
\tag{2.2}
\]
and the common optimal value is exactly `||p_mu||_infinity` by the fleet04/B15 theorem.

2. `mu` has a density `p in C_0(R)` iff `H_r` converges in `L^infinity` as `r downarrow0`; equivalently, iff the heat orbit is Cauchy in `C_0`:
\[
 \lim_{r,s\downarrow0}\|H_r-H_s\|_\infty=0.
\tag{2.3}
\]
In that case the uniform limit is the density `p`.

### Proof of the continuity equivalence

If `p in C_0`, Gaussian approximate identities converge uniformly to `p`, so (2.3) holds.

Conversely, if (2.3) holds, completeness of `C_0` gives a uniform limit `H_r -> p in C_0`. For every compactly supported continuous test function `varphi`,
\[
 \int \varphi(y)H_r(y)\,dy
 =\int (\varphi*\gamma_r)(z)\,d\mu(z)
 \longrightarrow \int\varphi\,d\mu,
\tag{2.4}
\]
while uniform convergence on `supp(varphi)` gives the same left side tending to `int varphi(y)p(y)dy`. Hence `mu=p(y)dy`. This proves (2.3) exactly.

Thus the central `L^infinity` conjecture and the stronger continuity assertion are mathematically different: the first is boundedness of a positive heat orbit; the second is its **sup-norm convergence**.

## 3. A quantitative Dini heat-defect criterion

Define the positive second-moment heat functional
\[
 A_r(y)=\int { (z-y)^2\over r^2}\gamma_r(z-y)\,d\mu(z).
\tag{3.1}
\]
Direct differentiation gives the exact scale identity
\[
 r\partial_r H_r(y)=A_r(y)-H_r(y).
\tag{3.2}
\]
Put
\[
 D_\mu(r)=\|A_r-H_r\|_\infty=\|r\partial_rH_r\|_\infty.
\tag{3.3}
\]

### Theorem 3.1 — `QFORM-HEAT-DINI-CLOSURE-v1`

If for one `r_0>0`
\[
 \int_0^{r_0}{D_\mu(r)\over r}\,dr<\infty,
\tag{3.4}
\]
then `mu` has a bounded density `p in C_0`, and for every `0<r<=r_0`,
\[
 \boxed{
 \|p-H_r\|_\infty
 \le \int_0^r {D_\mu(u)\over u}\,du .
 }
\tag{3.5}
\]
In particular,
\[
 \|p\|_\infty
 \le {1\over\sqrt{2\pi}r_0}
 +\int_0^{r_0}{D_\mu(u)\over u}\,du.
\tag{3.6}
\]
Hence a universal bound on the **normalized heat-scale variation** over `0<r<=1` would by itself prove both the central QFORM height theorem and continuity.

### Proof

For `0<s<r<=r_0`, the fundamental theorem of calculus in `C_b` and (3.2) give
\[
 \|H_r-H_s\|_\infty
 \le\int_s^r {D_\mu(u)\over u}\,du.
\tag{3.7}
\]
The Dini hypothesis makes `H_r` Cauchy as `r downarrow0`; Theorem 2.1 identifies its uniform limit with a `C_0` density. Letting `s downarrow0` in (3.7) gives (3.5). Since `||H_{r_0}||_infinity<=||gamma_{r_0}||_infinity`, (3.6) follows.

This criterion does **not** claim that bounded density alone implies continuity. The missing information is precisely summable scale variation.

## 4. Rough-law trace closure with no continuity assumption on the approximants' limit

The following is the precise trace statement useful when a new density estimate is first proved for regularized inputs/coefficient configurations.

### Lemma 4.1 — uniform convolution under weak convergence

If probability measures `mu_m => mu` weakly and `k in C_0(R)`, then
\[
 \|\mu_m*k-\mu*k\|_\infty\to0.
\tag{4.1}
\]

One proof approximates `k` uniformly by a bounded compactly supported Lipschitz function `g`. The translated test functions `z -> g(y-z)` have a common bounded-Lipschitz norm, so the bounded-Lipschitz metric for weak convergence controls the supremum in `y`; the uniform approximation then gives (4.1).

### Theorem 4.2 — `QFORM-ROUGH-C0-TRACE-v1`

Suppose `mu_m=>mu`, every `mu_m` has density height at most `B`, and there is a nonnegative function `psi` such that
\[
 D_{\mu_m}(r)\le\psi(r)\quad(0<r\le r_0,\;m\ge1),
\qquad
 \int_0^{r_0}{\psi(r)\over r}\,dr<\infty.
\tag{4.2}
\]
Then `mu` has a density `p in C_0` satisfying
\[
 \boxed{\|p\|_\infty\le B}
\tag{4.3}
\]
and
\[
 \boxed{
 \|p-\mu*\gamma_r\|_\infty
 \le\int_0^r{\psi(u)\over u}\,du.
 }
\tag{4.4}
\]

### Proof

For each fixed `r`, Lemma 4.1 applied to `gamma_r` gives uniform convergence `H_{m,r}->H_r`. Since convolution cannot increase the density cap, `||H_{m,r}||infinity<=B`, hence `||H_r||infinity<=B`. Applying the fleet04/B15 exact heat-height identity (1.6) to the **limit law** yields a bounded density with `||p||infinity<=B` — no absolute continuity of the limit was assumed.

Next apply Lemma 4.1 to
\[
 L_r(u)=\left({u^2\over r^2}-1\right)\gamma_r(u)\in C_0.
\tag{4.5}
\]
Thus `L_r*mu_m -> L_r*mu` uniformly, so `D_mu(r)<=psi(r)`. Theorem 3.1 gives `p in C_0` and (4.4).

This is stronger than mere weak lower semicontinuity of the height: a **uniform Dini scale estimate carries continuity through the rough limit with no loss in the height constant**.

## 5. Fourier envelopes automatically pay the Dini defect

The Dini criterion is useful even when the density proof comes from Fourier estimates because it reaches the heat-scale endpoint directly.

### Theorem 5.1 — `QFORM-FOURIER-TO-HEAT-ENDPOINT-v1`

Assume
\[
 |\phi_\mu(t)|\le\min\{1,K|t|^{-b}\},\qquad 1<b<3.
\tag{5.1}
\]
Then
\[
 \boxed{
 D_\mu(r)
 \le c_b K r^{b-1},\qquad
 c_b={2^{(1-b)/2}\Gamma((3-b)/2)\over\pi}.
 }
\tag{5.2}
\]
Consequently
\[
 \boxed{
 \|p-H_r\|_\infty
 \le {c_b\over b-1}K r^{b-1}.
 }
\tag{5.3}
\]
Combining (5.3) with the assigned partner theorem, if
\[
 M_r=\sup_yH_r(y),
\tag{5.4}
\]
then
\[
 \boxed{
 0\le\|p\|_\infty-M_r
 \le {c_b\over b-1}K r^{b-1}.
 }
\tag{5.5}
\]

### Proof

The Fourier multiplier of `r partial_r H_r=A_r-H_r` is
\[
 -r^2t^2e^{-r^2t^2/2}\phi_\mu(t).
\tag{5.6}
\]
Therefore
\[
\begin{aligned}
D_\mu(r)
&\le {1\over2\pi}\int_{\mathbb R}r^2t^2e^{-r^2t^2/2}|\phi_\mu(t)|\,dt\\
&\le {K\over\pi}r^2\int_0^\infty t^{2-b}e^{-r^2t^2/2}\,dt\\
&={K\over\pi}r^{b-1}\int_0^\infty u^{2-b}e^{-u^2/2}\,du\\
&={2^{(1-b)/2}\Gamma((3-b)/2)\over\pi}K r^{b-1}.
\end{aligned}
\tag{5.7}
\]
Theorem 3.1 gives (5.3). Equation (5.5) is the promised actual application of fleet04/B15: its exact heat-height identity says `M_r` approaches the true density height, while (5.3) supplies the quantitative error.

Notice the exponent is the **endpoint `b-1`**. No separate Hölder estimate is required first.

## 6. Application to the newest three-volume estimate

Insert the source theorem (1.1)-(1.2). For every admissible `q`, equations (5.3)-(5.5) give an explicit heat recovery rate with `b=3/(2q)`.

For the theorem's useful choice `q=4/3`,
\[
 b={9\over8},
\tag{6.1}
\]
\[
 K_{4/3}
 =\Bigl[e^3(4/3)^{-3/2}\pi^3\Bigr]^{3/8}Z^{-3/16}
 =9.4972278981\ldots\,Z^{-3/16}.
\tag{6.2}
\]
Moreover
\[
 {c_{9/8}\over1/8}
 ={8\,2^{-1/16}\Gamma(15/16)\over\pi}
 =2.5364890443\ldots .
\tag{6.3}
\]
Thus every q=4/3 volume-certified instance satisfies
\[
 \boxed{
 \|p_Q-p_Q*\gamma_r\|_\infty
 \le 24.089614515\,Z^{-3/16}r^{1/8},
 }
\tag{6.4}
\]
and, by fleet04/B15,
\[
 \boxed{
 0\le\|p_Q\|_\infty-M_r(Q)
 \le24.089614515\,Z^{-3/16}r^{1/8}.
 }
\tag{6.5}
\]
This reaches the `1/8` heat-scale endpoint. Earlier generic Hölder compilation from the same `b=9/8` envelope only gave exponents strictly below `1/8`; the scale-derivative route does not pay that loss.

### Nearby-diffuse certificate

Under (1.4), `kappa=s_3(M)>=15a/16` and `Z>=kappa^6`, so
\[
 Z^{-3/16}\le \left({16\over15a}\right)^{9/8}.
\tag{6.6}
\]
Hence the new quantitative regularity bound is
\[
 \boxed{
 \|p_Q-p_Q*\gamma_r\|_\infty
 \le25.903721636\,a^{-9/8}r^{1/8},
 }
\tag{6.7}
\]
and the assigned partner identity yields the concrete inequality
\[
 \boxed{
 0\le\|p_Q\|_\infty-M_r(Q)
 \le25.903721636\,a^{-9/8}r^{1/8}.
 }
\tag{6.8}
\]
Together with the source height estimate,
\[
 \boxed{
 \|p_Q\|_\infty\le {24\sqrt3e\over5a}<23/a.
 }
\tag{6.9}
\]

### Rough closure of the volume branch

If `mu_m` are output laws satisfying the q=4/3 theorem with a common lower bound `Z_m>=Z_0>0` and `mu_m=>mu`, then Theorem 4.2 gives **without assuming continuity of the limit**
\[
 p_\mu\in C_0,
\qquad
 \|p_\mu\|_\infty\le {9\sqrt3e\over2}Z_0^{-1/6},
\tag{6.10}
\]
\[
 \|p_\mu-\mu*\gamma_r\|_\infty
 \le24.089614515\,Z_0^{-3/16}r^{1/8}.
\tag{6.11}
\]
Likewise, a weak limit of nearby-diffuse outputs with one common `a>0` keeps both (6.9) and (6.7), even if the limiting representation sits on an algebraic boundary of the certificate. This is the requested rough-law/trace justification used by a **new density estimate**, rather than a continuity-only side result.

## 7. Sharper re-application to the fresh four-row |t|^{-3/2} branch

The immediately preceding fleet03/B15 run compiled a fresh four-row envelope with `b=3/2` through a Hölder modulus and then Gaussian heat smoothing. The present direct heat-scale mechanism strictly improves that intermediate constant.

For `b=3/2`, (5.3) gives
\[
 \|p-H_r\|_\infty
 \le {2^{3/4}\Gamma(3/4)\over\pi}K r^{1/2}.
\tag{7.1}
\]
For the four-row QFORM source used in that run,
\[
 K=\sqrt2\,\pi^{3/2}|\beta|^{-1/2}(|\alpha|C)^{-1}
 (\Delta_1\Delta_2)^{-1/2},
\tag{7.2}
\]
so
\[
 \boxed{
 0\le\|p_Q\|_\infty-M_r(Q)
 \le 2^{5/4}\sqrt\pi\,\Gamma(3/4)
 |\beta|^{-1/2}(|\alpha|C)^{-1}(\Delta_1\Delta_2)^{-1/2}r^{1/2}.
 }
\tag{7.3}
\]
The scalar coefficient is
\[
 2^{5/4}\sqrt\pi\Gamma(3/4)=5.165902753\ldots,
\tag{7.4}
\]
versus `12.365382148...` from the previous Hölder-then-heat route. The improvement comes from differentiating the Gaussian heat orbit directly, not from changing the four-row theorem.

## 8. What this does and does not close

**Closed in this run:**

- an exact functional separation of essential boundedness and continuity;
- a target-level Dini heat-scale sufficient criterion for both;
- a weak-limit theorem carrying a uniform height constant **and** continuity with no loss when a uniform heat-defect majorant is available;
- endpoint heat-recovery rates for the current volume theorem, including the explicit `r^(1/8)` nearby-diffuse estimate;
- a sharper direct heat-recovery constant for the fresh `|t|^{-3/2}` four-row branch.

**Still open:** the bare three-large-eigenvalue hypothesis has not been shown to force a universal Dini heat-defect budget, a universal three-volume certificate, or any other universal height estimate. The low-cross-rank/high-leverage/near-null survivors remain. Therefore the full QFORM conjecture is still open.

The new full-target sufficient obligation may be written compactly, after normalizing `s_3(A)>=1`, as
\[
 \boxed{
 \sup_{A,f}\int_0^1
 \left\|\,r\partial_r\,\mathbb E\gamma_r(X^TAX-\cdot)\right\|_\infty
 {dr\over r}<\infty.
 }
\tag{8.1}
\]
If proved, (3.6) gives a universal density constant and `C_0` continuity simultaneously. This is a stronger obligation than the original height theorem, so it is a proof interface, not a claimed equivalence.

No scheduler/task state, email, notification, permission, cross-account authentication, public release, paid model/API/Codex call, installation, or remote workflow was changed. The current-hour canonical B15 login already existed when this invocation began; protocol forbids overwriting it, so this run records that fact rather than fabricating a second canonical login. Model self-report is `GPT-5.6 Sol`; configured reasoning effort remains `UNKNOWN_NOT_EXPOSED`; provider reasoning-token/thinking-time counters are not exposed.
