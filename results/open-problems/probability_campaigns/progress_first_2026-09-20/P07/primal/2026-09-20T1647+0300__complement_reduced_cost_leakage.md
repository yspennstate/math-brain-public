Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but authenticated completed-run effort telemetry is unavailable, so I do not claim otherwise.

# P07-A — complementary optimizer as the exact reduced-cost vector, and the overlap/leakage barrier

**Native role:** `P07-A`, task `6aa7b46f70a8819184095c277974c256`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured pre-write master:** `b7b02358738d2344eb6f0c8b35890a3ab1d045e8`  
**Previous own substantive checkpoint:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T1544+0300__affine_barrier_buffered_hinge_repair.md`, blob `ab7f004a1866a54476af5a3b0190f27c17b13dd2`.  
**Complementary checkpoint read:** P07-B `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T1610+0300__quadratic_energy_concentration_collision_reduction.md`. P07-B owns Fourier-dual / exceptional-frequency interpolation. This report stays on the primal pair-LP, support geometry and exact candidate-loss identities.

**Outside target:** Bandeira et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 18.  
**Primary partial-result paper:** A. S. Bandeira, J. Błasiok, D. Dmitriev, U. Faure, A. Kireeva, D. Kunisky, *The Lovász number of random circulant graphs*, arXiv:2502.16227.  
**Exact source model:** odd `n`; the `(n-1)/2` conjugate nonzero difference pairs are selected independently with probability `1/2`.  
**Endpoint:**
\[
\mathbb E\,\vartheta(G_n)=(1+o(1))\sqrt n.
\]
A bounded current-source check on 20 September 2026 again found the primary paper stating that the exact asymptotics remain open and proving only square-root scale up to the `sqrt(log log n)` loss. No later source-matching sharp-constant proof was found in that bounded check. This is not a worldwide novelty certificate.

The fixed full-source metric therefore remains
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
Status: **OPEN / PROVED PARTIAL**. Nothing below is represented as an arbitrary-`n` solution of Conjecture 18.

---

## 0. Preserved predecessor handoff: SRG69 remains OPEN / PARTIAL

The reassigned predecessor remains archived under

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/rotations/SHPECTOROV-ZHAO-2026-SRG69/`

with frozen `R_SRG69=1`, status **OPEN / PARTIAL**. Preserve its no-Cayley theorem, rooted `L/B/C` system, centered spectral transfer, endpoint/cycle filters, block-moment and Gram reductions, low-rank residual work and star-complement handoff. Nothing here edits that root or calls SRG69 solved.

---

# 1. A full pair-cosine inverse valid for every odd order

Let
\[
M=\{1,\dots,m\},\qquad m=(n-1)/2,
\]
and let the full folded cosine matrix be
\[
\mathcal C_{ab}=\cos(2\pi ab/n),\qquad a,b\in M.
\tag{1.1}
\]
The preceding P07-A report used the folded Fourier identities
\[
\mathcal C\mathbf 1=-\frac12\mathbf1,
\qquad
\mathcal C\mathcal C^T=\frac n4I-\frac12J.
\tag{1.2}
\]
Because `mathcal C` is symmetric, these immediately give a useful exact inverse that was not previously exploited here.

## Lemma P07-A.33 — exact inverse of the odd pair-cosine transform

For every odd `n`,
\[
\boxed{
\mathcal C^{-1}=\frac4n(\mathcal C-J).
}
\tag{1.3}
\]

### Proof

Using (1.2),
\[
\mathcal C(\mathcal C-J)
=\left(\frac n4I-\frac12J\right)
-\mathcal C\mathbf1\mathbf1^T
=\frac n4I-\frac12J+\frac12J
=\frac n4I.
\]
Multiplying by `4/n` proves (1.3). `square`

The point of (1.3) is that a dual slack vector supported on one column block can be solved explicitly through the complementary row block. On prime order, where the preceding exact-support theorem identifies those two complementary blocks with the two theta optimizers, this gives an exact primal sensitivity identity.

---

# 2. Prime pair LP and the two complementary optimal bases

Now let `p` be an odd prime and keep `M={1,...,(p-1)/2}`. Let `D subset M` be the edge-pair row set and put
\[
A=M\setminus D.
\tag{2.1}
\]
For any vector `z>=0` on `M` satisfying
\[
\mathcal C_{D,M}z=-\mathbf1_D,
\tag{2.2}
\]
define
\[
T(z)=\frac p{1+\mathbf1^Tz}.
\tag{2.3}
\]
Then setting Fourier eigenvalues
\[
h_0=T(z),\qquad h_j=h_{-j}=\frac{T(z)}2z_j
\tag{2.4}
\]
gives a valid cyclic theta-primal certificate for `G_D`: (2.2) gives the edge zeros, nonnegativity gives PSD, and (2.3) gives total spectral mass `p`. Hence maximizing the primal objective is exactly the pair LP
\[
\boxed{
\min\{\mathbf1^Tz:\mathcal C_{D,M}z=-\mathbf1,\ z\ge0\}.
}
\tag{2.5}
\]

The earlier prime exact-support/uniqueness theorem gives a unique optimal pair support `H subset M` with
\[
|H|=|D|,
\qquad K=M\setminus H,
\tag{2.6}
\]
and a strictly positive optimal basic vector
\[
x=-B^{-1}\mathbf1>0,
\qquad B:=\mathcal C_{D,H}.
\tag{2.7}
\]
Write
\[
t:=\vartheta(G_D),
\qquad
\mathbf1^Tx=\frac pt-1.
\tag{2.8}
\]

For the complement graph, the earlier complementary-support theorem says its unique optimal pair support is exactly `K`. Put
\[
G:=\mathcal C_{A,K},
\qquad
v:=-G^{-1}\mathbf1>0.
\tag{2.9}
\]
If `s=theta(bar G_D)`, vertex transitivity gives `ts=p`, so
\[
\boxed{
1+\mathbf1^Tv=t.
}
\tag{2.10}
\]
Thus the two positive basic vectors `x` and `v` are not merely separate certificates: the next theorem shows that `v` is exactly the reduced-cost profile of `x`.

---

# 3. Main new theorem: complement weights are the exact primal reduced costs

Let
\[
E:=\mathcal C_{D,K}.
\]
For the basis `H`, define the standard LP dual vector
\[
y:=B^{-T}\mathbf1,
\tag{3.1}
\]
and its nonbasic reduced-cost vector
\[
u:=\mathbf1_K-E^Ty.
\tag{3.2}
\]

## Theorem P07-A.34 — complementary reduced-cost identity

For every prime-order circulant graph in the normalization above,
\[
\boxed{
 u=\frac{p}{2t}\,v.
}
\tag{3.3}
\]
In particular every nonbasic reduced cost is **strictly positive**.

### Proof

Extend `y` by zero from the row block `D` to all of `M`, writing `tilde y_D=y`, `tilde y_A=0`. Extend `u` by zero from `K` to all columns, writing `tilde u_H=0`, `tilde u_K=u`. By (3.1)--(3.2),
\[
\mathcal C\widetilde y=\mathbf1-\widetilde u.
\tag{3.4}
\]
Apply the exact inverse (1.3):
\[
\widetilde y
=\frac4p(\mathcal C-J)(\mathbf1-\widetilde u)
=-2\mathbf1-\frac4p(\mathcal C-J)\widetilde u,
\tag{3.5}
\]
where `(mathcal C-J)1=-(p/2)1` was used.

Restrict (3.5) to the complementary row block `A`, where `tilde y_A=0`. Since `tilde u` is supported on `K`,
\[
0=-2\mathbf1_A-\frac4p\left(G u-(\mathbf1^Tu)\mathbf1_A\right),
\]
so
\[
G u=\left(\mathbf1^Tu-\frac p2\right)\mathbf1_A.
\tag{3.6}
\]
Using `v=-G^{-1}1`,
\[
u=\left(\frac p2-\mathbf1^Tu\right)v.
\tag{3.7}
\]
Let `V=1^Tv=t-1` by (2.10), and `U=1^Tu`. Summing (3.7) gives
\[
U=\left(\frac p2-U\right)V,
\]
hence
\[
\frac p2-U=\frac{p}{2(1+V)}=\frac p{2t}.
\]
Substitution into (3.7) proves (3.3). Since every coordinate of the complement basic vector `v` is strictly positive, every coordinate of `u` is strictly positive as well. `square`

### Interpretation

The complement theta optimizer is, up to the scalar `p/(2t)`, exactly the vector of opportunity costs for placing primal mass on frequencies outside the optimal support `H`. This is stronger than ordinary complementary slackness: it identifies every slack coordinate quantitatively with the opposite optimizer.

---

# 4. Exact loss formula for every feasible positive certificate

Let `z` be **any** feasible vector in (2.5), not necessarily basic. The optimal objective is `1^Tx`; strong duality with (3.1) gives
\[
\mathbf1^Tz-\mathbf1^Tx
=(\mathbf1-\mathcal C_{D,M}^Ty)^Tz
=u^Tz_K.
\tag{4.1}
\]
Combining Theorem P07-A.34 with (2.8) yields the exact candidate-quality identity.

## Corollary P07-A.35 — weighted leakage is exactly the theta loss

For every feasible `z>=0` satisfying `mathcal C_{D,M}z=-1`,
\[
\boxed{
\mathbf1^Tz-\left(\frac pt-1\right)
=\frac p{2t}\,v^Tz_K,
}
\tag{4.2}
\]
and therefore
\[
\boxed{
\frac{t}{T(z)}-1
=\frac12\,v^Tz_K.
}
\tag{4.3}
\]
Equivalently,
\[
\boxed{
T(z)=\frac{t}{1+\frac12v^Tz_K}.
}
\tag{4.4}
\]

This gives a quantitative alternative proof of uniqueness: equality `T(z)=t` forces `z_K=0` because `v>0`; then the square system `Bz_H=-1` forces `z_H=x`.

For a positive basis `J`, (4.3) says its entire deficit from the optimum is carried by the coordinates `J cap K`. In particular, a one-column positive pivot from `H` into `K` has an exact objective penalty equal to one half of the entering primal mass times the corresponding complement weight.

The symmetric statement holds for the complement: if `w` is any feasible pair vector for the row set `A`, then
\[
\boxed{
\frac{s}{T_A(w)}-1
=\frac12\,x^Tw_H,
\qquad s=p/t.
}
\tag{4.5}
\]
Thus each optimizer is the exact leakage-price vector for the other.

---

# 5. Deterministic spread bounds for the reduced costs

The previous all-order spectral-peak theorem states that zero frequency is a largest spectral atom of an optimal circulant primal and implies `sum physical^2 <= theta`. Applied to the complement optimizer, whose paired nontrivial eigenvalues are `s v_k/2`, this gives
\[
s^2\left(1+\frac12\sum_{k\in K}v_k^2\right)\le ps.
\]
Since `p/s=t`,
\[
\boxed{
\sum_{k\in K}v_k^2\le2(t-1).
}
\tag{5.1}
\]
Also the spectral-peak bound directly gives
\[
\boxed{0<v_k\le2.}
\tag{5.2}
\]
Consequently the reduced costs obey
\[
\boxed{
\sum_{k\in K}u_k=\frac p2\left(1-\frac1t\right),
}
\tag{5.3}
\]
\[
\boxed{
\sum_{k\in K}u_k^2
\le\frac{p^2(t-1)}{2t^2},
\qquad
0<u_k\le\frac pt.
}
\tag{5.4}
\]
In particular their `l1^2/l2^2` effective support satisfies
\[
\boxed{
\frac{(\sum_Ku_k)^2}{\sum_Ku_k^2}
\ge\frac{t-1}{2}.
}
\tag{5.5}
\]
This does not locate the reduced costs sharply enough to prove the conjecture, but it rules out concentration of essentially all objective slack onto fewer than theta-scale many nonbasic coordinates.

---

# 6. Exact complement anti-symmetry of the radial field

Return temporarily to arbitrary odd `n`. For the centered radial field from the preceding report,
\[
Z_D(j)=\frac4{\sqrt n}\left(\sum_{a\in D}\cos(2\pi aj/n)+\frac{|D|}{2m}\right),
\tag{6.1}
\]
let `A=M\setminus D`. Since
\[
\sum_{a\in M}\cos(2\pi aj/n)=-\frac12
\]
for every pair site `j`, one has the exact identity
\[
\boxed{Z_A(j)=-Z_D(j)\quad\text{for every }j.}
\tag{6.2}
\]

This exposes a structural tradeoff in the buffered-hinge route. If
\[
S_D(\tau)=\{j:Z_D(j)\le\tau\},
\qquad
S_A(\tau)=\{j:Z_A(j)\le\tau\},
\tag{6.3}
\]
then for every `tau>=0`,
\[
S_D(\tau)\cup S_A(\tau)=M,
\qquad
S_D(\tau)\cap S_A(\tau)=\{j:|Z_D(j)|\le\tau\}.
\tag{6.4}
\]
Under the inherited empirical `N(0,1)` law for `Z_D`, the overlap fraction converges in source probability to
\[
\boxed{2\Phi(\tau)-1.}
\tag{6.5}
\]
For the concrete buffered threshold `tau=0.2` used in the preceding P07-A report, this is about `0.1585`: the linear repair surplus is accompanied by a linear complement-overlap region.

By contrast, at the median threshold `tau=0`, the two radial half-supports partition the pair sites (up to exact zeros), matching the prime theorem that the two **true** optimal supports `H,K` form a complementary partition, but leaving essentially no overcomplete linear repair freedom.

This explains the tension between the last two constructions:

1. the half-support hinge has the right complementary support geometry but is square and difficult to repair while preserving positivity;
2. the buffered hinge creates linear repair freedom but necessarily creates linear support overlap with its complement;
3. Corollary P07-A.35 shows that such overlap is not free: after exact flattening, every unit of primal mass landing on the true opposite support is charged by the corresponding complement optimal weight.

The buffered support should therefore be viewed as a **repair/search superset**, not as a candidate final optimal support.

---

# 7. What this changes, and the next attack

The headline `sqrt(log log n)` loss is not removed here. The new result instead turns the prime primal geometry into a quantitative support-selection statement:
\[
\boxed{
\text{relative candidate loss}
=\frac12\times
\text{(complement-weighted spectral leakage)}.
}
\tag{7.1}
\]
This is exact, not asymptotic.

The most useful next attack is now **support-pruning after buffered repair**, rather than demanding that the buffered density itself remain the final optimizer. Concretely:

- first obtain any nonnegative exact-flat feasible vector on the buffered support `S_D(tau)` with the sharp radial objective;
- minimize `1^Tz` over that restricted support. On prime order, a restricted optimum can be taken basic; the earlier prime flat-support lower bound then forces exactly `|D|` active pair sites;
- use (4.3) to quantify how much objective is lost by every surviving coordinate on the true opposite support `K`;
- exploit the exact anti-symmetry `Z_A=-Z_D` to couple the two restricted pruning problems and seek a complementary pair with `v^Tz_K=o(1)` and `x^Tw_H=o(1)`.

This is a narrower target than a global Fourier RIP or a uniform `l2 -> l_infinity` inverse bound. It asks for a **weighted leakage/pruning theorem on the actual positive feasible polytope**. It also stays complementary to P07-B's present high-collision / frequency-delocalized dual obstruction.

A tempting stronger claim that the prime optimal support map is an involution was explored and rejected; it is not used here. Finite diagnostics already show that no such blanket support-map involution should be assumed. No finite numerical theta value is used as an arbitrary-size theorem.

---

# 8. Obligation ledger

- **Full source:** `E theta(G_n)=(1+o(1))sqrt(n)` for the exact dense random circulant model — **OPEN**.
- **Published iterated-log loss removed?** No; `alpha_LL: 1/2 -> 1/2` remains unchanged.
- **New exact all-odd-order lemma:** full pair-cosine inverse (1.3) — **PROVED**.
- **New exact prime theorem:** the complement optimizer equals the nonbasic reduced-cost profile up to `p/(2 theta)` — **PROVED PARTIAL**.
- **New exact prime theorem:** every feasible primal certificate has loss formula (4.3) — **PROVED PARTIAL**.
- **New deterministic reduced-cost spread bounds:** (5.1)--(5.5) — **PROVED PARTIAL**.
- **New all-odd complement radial identity:** `Z_{D^c}=-Z_D`, with buffered-support overlap law under the inherited empirical Gaussian theorem — **PROVED PARTIAL**.
- **Remaining gap:** construct/repair and then prune a source-typical positive exact-flat certificate so that the complement-weighted leakage is asymptotically negligible while retaining absolute depth `delta=(1-o(1))/sqrt n`; then obtain the expectation tail/uniform-integrability step.

External novelty of the packaging and identities is **UNVERIFIED**. Candidate results remain subject to later independent review.