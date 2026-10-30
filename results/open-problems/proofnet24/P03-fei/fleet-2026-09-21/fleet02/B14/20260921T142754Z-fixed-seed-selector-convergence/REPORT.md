# B14 — fixed balanced-seed recursion cannot make the potential-free selector diverge

**Run:** 2026-09-21T14:27:54Z, fleet02/B14  
**Role:** FEI erasure and selector proof  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no authenticated brain retrieval or receiver-context use occurred.  
**Status:** PARTIAL / new structural theorem. **Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Fresh scientific master used:** initially `3cb9106df20e50bbe05aa92d17024b03d9d053b4`, then refreshed through `7572f80714866112f28fbfedc1f4c1c8696601bd`; the intervening commits contained no newer fleet02/B14 or fleet02/B18 result superseding the dependencies below.  
**Immediate predecessor:** `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B14/20260921T141815Z-recursive-selector-barrier/REPORT.md`.

This run uses FLEET_RULES moves **#3 (prove something stronger: treat every fixed balanced seed rather than only Numaro's seed), #18 (say the obstruction in the language of discrete derivatives / spectral purity), #20 (find why the recursive algorithm fails: its tail is summable), and #29 (add the infinite-depth boundary and prove the finite minima converge)**. These differ from the predecessor's #5/#19/#24 construction moves.

No publication-priority claim is made. The Numaro seed and its certified FEI lower bound are external prior work. The composition recursion used as input was proved in the immediate predecessor; the theorem below is a new-to-this-run consequence for the fleet.

## 1. Exact object and the open question left by the preceding run

For a nonconstant Boolean function `f`, write

\[
\rho_0(f):=\min_{j:\operatorname{Inf}_j(f)>0}
\frac{\Delta_j H(f)}{\operatorname{Inf}_j(f)},
\qquad
\Delta_jH(f):=H(f)-\frac{H(f_{j,+})+H(f_{j,-})}{2}.
\]

A dimension-independent upper bound on `rho_0` would prove FEI by physical-restriction induction. The preceding B14 run took Numaro's balanced 18-variable seed `G`, recursively composed it on fresh disjoint blocks,

\[
F_1=G,\qquad F_{r+1}=G(F_r^{(1)},\ldots,F_r^{(18)}),
\]

and rigorously certified

\[
\rho_0(F_4)>7.0518528350,\qquad
\rho_0(F_5)>7.0960606187.
\]

It therefore killed every potential-free restriction-step proof with constant below `7.096...`, but explicitly left open whether the same fixed-seed recursion can make `rho_0(F_r)` diverge.

This report answers that question **no**, and proves a general theorem for every fixed balanced non-dictator outer seed.

## 2. Inherited exact one-coordinate composition recursion

Let

\[
G:\{-1,1\}^m\to\{-1,1\}
\]

be balanced, and delete irrelevant logical coordinates. For each relevant logical coordinate `i`, set

\[
\alpha_i:=\operatorname{Inf}_i(G),
\qquad
s_i:=|\widehat G(\{i\})|.
\tag{2.1}
\]

The predecessor proved an exact finite function `K_i(q)` from the Fourier pairs of `G` such that, if a physical leaf in a balanced inner function has influence `p`, singleton-Fourier magnitude `q`, and local restriction ratio

\[
R=\Delta H/p,
\]

then placing that inner function in logical coordinate `i` of `G` gives

\[
p'=\alpha_i p,
\qquad
q'=s_iq,
\qquad
R'=R+\frac{K_i(q)}{\alpha_i p}.
\tag{2.2}
\]

For completeness, if for `K subseteq[m]\\{i}` we put

\[
a_K=\widehat G(K),\qquad b_K=\widehat G(K\cup\{i\}),
\]

then with `phi(x)=-x log_2 x`, `phi(0)=0`,

\[
\widetilde H_i(q)
=\sum_K\Bigl[
\phi((a_K+qb_K)^2)+
\phi((1-q^2)b_K^2)
\Bigr]
\]

and

\[
K_i(q)
=H(G)-\frac{\widetilde H_i(q)+\widetilde H_i(-q)}2
+\alpha_i h_2(q^2).
\tag{2.3}
\]

In particular `K_i(0)=0`.

Every physical coordinate of the depth-`r` self-composition corresponds to a word `w=(i_1,...,i_r)` of logical coordinates. Iterating (2.2) gives

\[
p_t=\prod_{u=1}^t\alpha_{i_u},
\qquad
q_t=\prod_{u=1}^t s_{i_u},
\tag{2.4}
\]

and its local ratio is its depth-one ratio plus the successive `K/(alpha p)` increments.

No FEI hypothesis and no every-coordinate payment assertion enters this recursion.

## 3. PROVED: strict spectral-purity contraction for every fixed non-dictator seed

Define the coordinate spectral-purity parameter

\[
\theta_i:=\frac{s_i^2}{\alpha_i}.
\tag{3.1}
\]

### Lemma 3.1

For every relevant coordinate of every Boolean `G`,

\[
0\le \theta_i\le \alpha_i\le1.
\tag{3.2}
\]

If `G` is not a dictator (up to sign), then

\[
\boxed{\theta:=\max_i\theta_i<1.}
\tag{3.3}
\]

### Proof

For a fixed `i`, write the oriented pair derivative on the remaining cube as

\[
d_i(y):=\frac{G(+1,y)-G(-1,y)}2\in\{-1,0,1\}.
\]

Then

\[
\mathbb E d_i=\widehat G(\{i\}),
\qquad
\mathbb E|d_i|=\mathbb E d_i^2=\operatorname{Inf}_i(G)=\alpha_i.
\]

Hence

\[
s_i=|\mathbb E d_i|\le\mathbb E|d_i|=\alpha_i,
\]

so `s_i^2/alpha_i <= alpha_i <=1`. If `theta_i=1`, both inequalities force `alpha_i=s_i=1`. Thus `|E[Gx_i]|=1`, so the two Boolean variables `G` and `sign(E[Gx_i])x_i` agree everywhere. Hence `G` is a dictator up to sign. A fixed non-dictator has finitely many relevant coordinates, so its maximum `theta` is strictly below one. QED.

### Near-dictator meaning of the escape `theta_i -> 1`

The same calculation gives an exact geometric interpretation. Since the correlation of `G` with the best signed dictator on coordinate `i` is `s_i`,

\[
\operatorname{dist}_{\rm Ham}(G,\pm x_i)=\frac{1-s_i}{2}.
\tag{3.4}
\]

From `theta_i<=alpha_i` we get `s_i=sqrt(theta_i alpha_i)>=theta_i`; therefore

\[
\boxed{
\operatorname{dist}_{\rm Ham}(G,\pm x_i)
\le\frac{1-\theta_i}{2}.
}
\tag{3.5}
\]

So a sequence of outer gates whose purity tends to one is quantitatively forced toward a dictator in that coordinate. This will be one concrete escape regime for any future nonstationary composition attack.

## 4. PROVED: the composition correction is only quadratic-logarithmic near zero bias

The second ingredient is the cancellation created by the `+q/-q` average in (2.3).

### Lemma 4.1 — finite-seed small-bias bound

For every fixed balanced Boolean seed `G` there are constants `q_0>0` and `C_G<infinity` such that for every relevant coordinate `i` and every `|q|<=q_0`,

\[
\boxed{
|K_i(q)|\le C_G q^2\bigl(1+\log(1/|q|)\bigr).
}
\tag{4.1}
\]

At `q=0` the right side is interpreted by continuity and `K_i(0)=0`.

### Proof

Use `phi(x)=-x log_2 x`. There are finitely many Fourier pairs `(a_K,b_K)`.

If `a_K\ne0`, choose `q_0` small enough, uniformly over all nonzero pairs and coordinates, that

\[
|q b_K|\le |a_K|/2.
\]

Then `(a_K +/- q b_K)^2` stays in a compact interval bounded away from zero. Taylor's theorem for `phi` applies there. In the symmetric average

\[
\frac12\{\phi((a_K+qb_K)^2)+\phi((a_K-qb_K)^2)\},
\]

the term linear in `q` cancels, so the change from `phi(a_K^2)` is `O_G(q^2)`. The companion mass `phi((1-q^2)b_K^2)` also differs from `phi(b_K^2)` by `O_G(q^2)`.

If `a_K=0`, the first mass is exactly `q^2b_K^2`, and

\[
\phi(q^2b_K^2)=O_G(q^2(1+\log(1/|q|))).
\]

The companion mass again changes by `O_G(q^2)`. Finally

\[
h_2(q^2)=O(q^2(1+\log(1/|q|))).
\]

Summing the finitely many pair bounds and taking the maximum over the finitely many relevant coordinates proves (4.1). QED.

A more precise expansion is possible, but the order in (4.1) is exactly what the recursion needs.

## 5. MAIN THEOREM: fixed balanced-seed recursive self-composition has a finite selector limit

### Theorem 5.1 — uniform summability of every leaf path

Let `G` be a fixed balanced Boolean non-dictator with all irrelevant coordinates removed, and let `F_r` be its depth-`r` self-composition on disjoint fresh blocks. Then there is a finite constant `M_G` such that for **every** depth `r` and **every** physical coordinate `j` of `F_r`,

\[
\left|\frac{\Delta_jH(F_r)}{\operatorname{Inf}_j(F_r)}\right|
\le M_G.
\tag{5.1}
\]

Consequently

\[
\boxed{\sup_r\rho_0(F_r)<\infty.}
\tag{5.2}
\]

Moreover the finite-depth minima themselves converge:

\[
\boxed{\rho_0(F_r)\longrightarrow \rho_*(G)<\infty.}
\tag{5.3}
\]

### Proof

Let

\[
\alpha_*:=\min_i\alpha_i>0,
\qquad
\theta:=\max_i s_i^2/\alpha_i<1
\]

from Lemma 3.1. Along any length-`t` leaf path, (2.4) gives

\[
\frac{q_t^2}{p_t}
=\prod_{u=1}^t\frac{s_{i_u}^2}{\alpha_{i_u}}
\le\theta^t.
\tag{5.4}
\]

In particular `q_t^2<=theta^t`, so `q_t->0` uniformly over all paths. If some `s_{i_u}=0`, then `q_t=0` from that level onward and every later correction vanishes because `K_i(0)=0`. Otherwise, because the seed has only finitely many positive `s_i`, put

\[
s_*:=\min_{i:s_i>0}s_i>0.
\]

Then

\[
\log(1/q_t)\le t\log(1/s_*).
\tag{5.5}
\]

For all sufficiently large `t`, uniformly over paths, Lemma 4.1 applies. The next increment in (2.2) therefore satisfies

\[
\begin{aligned}
\left|
\frac{K_{i_{t+1}}(q_t)}{\alpha_{i_{t+1}}p_t}
\right|
&\le \frac{C_G}{\alpha_*}
\frac{q_t^2}{p_t}\bigl(1+\log(1/q_t)\bigr)\\
&\le C'_G(1+t)\theta^t.
\end{aligned}
\tag{5.6}
\]

The series

\[
\sum_{t\ge0}(1+t)\theta^t
\]

converges. The finitely many initial levels have a finite maximum because `G` is fixed. Hence the complete correction series along **every** leaf path converges absolutely, with a tail bound independent of the path. This proves (5.1)-(5.2).

For (5.3), let `m_r=rho_0(F_r)` and let `T_r` be the uniform absolute tail bound obtained from (5.6), so `T_r->0`. Any depth-`s` leaf path, `s>=r`, can be truncated to its inner depth-`r` suffix, and the corresponding local ratios differ by at most `T_r`. Hence

\[
m_s\ge m_r-T_r.
\]

Conversely, extend a depth-`r` minimising path arbitrarily to depth `s`; the extension changes its ratio by at most `T_r`, so

\[
m_s\le m_r+T_r.
\]

Thus `|m_s-m_r|<=T_r` for all `s>=r`. The sequence is Cauchy and has a finite limit. QED.

### Corollary 5.2 — the erasure part is also bounded on every fixed-seed recursion

With the exact decomposition

\[
\Delta_jH=B_j+JS_j,
\qquad JS_j\ge0,
\]

we have `B_j<=Delta_jH`. Therefore Theorem 5.1 also gives a seed-dependent uniform bound on every local erasure ratio `B_j/Inf_j` throughout the fixed recursion. In particular, recursively iterating one fixed balanced non-dictator seed cannot by itself prove `K_E=infinity` for the singleton erasure-selector constant.

## 6. Numaro specialization and what changed

For the external balanced Numaro 18-variable seed, the predecessor's exact Walsh calculation gave two coordinate classes:

\[
\alpha_C=s_C=57/256,
\qquad
\alpha_A=s_A=1/256.
\]

Hence

\[
\theta_C=57/256,
\qquad
\theta_A=1/256,
\qquad
\boxed{\theta=57/256\approx0.22265625.}
\tag{6.1}
\]

The contraction is therefore far from the near-dictator boundary `theta=1`. Theorem 5.1 proves, without extrapolating a finite numerical table, that the recursive selector obstruction certified in the predecessor **must converge to a finite limit**.

The existing rigorous finite certificate remains

\[
\rho_0(F_5)>7.096060618744925556\ldots.
\]

A separate high-precision exploratory evaluation in this run (not directed-rounding certified and not used in Theorem 5.1) gives the all-core values

\[
\begin{array}{c|c}
r& R(C^r)\\ \hline
6&7.10772847577248\ldots\\
7&7.11073268180429\ldots\\
8&7.11149204888970\ldots
\end{array}
\]

and a compressed two-class dynamic program suggests a limiting minimum near

\[
7.111618180511835\ldots,
\]

with an inner `C^5` core followed, asymptotically, by very small auxiliary-layer corrections. **This decimal is exploratory only**: this run proves finiteness/convergence, not that this is the exact limiting minimizer or a newly certified strict lower bound.

### Before / after

**Before:** the finite recursion certified `rho_0>7.096`, but it was open whether repeated composition of the same seed could send the selector ratio to infinity and thereby destroy the potential-free induction route completely.

**After:** every fixed balanced non-dictator seed has `theta<1`; the exact composition correction is only `O(q^2 log(1/q))`; and the resulting leaf correction series is uniformly summable. Therefore the Numaro fixed-seed recursion — and every other fixed balanced-seed self-composition — has a finite selector limit.

This is a negative result for one counterexample mechanism, not an upper bound for arbitrary Boolean functions.

## 7. New universal-facing implication: the escape regime is now explicit

The recursive construction search has separated two issues that were previously conflated.

1. A **fixed** balanced non-dictator gate cannot make `rho_0` diverge, no matter how many times it is self-composed.
2. To seek an unbounded selector obstruction within a composition paradigm, one must therefore leave fixed-seed self-composition. Seed-dependent quantities must degenerate along the construction. One concrete degeneration is `theta_i -> 1`, and (3.5) says that this forces the corresponding gate to become quantitatively close to a signed dictator.

This identifies a sharper next proof target than another finite recursion depth:

> **Near-dictator composition stability target.** Bound the `K_i(q)` correction uniformly in terms of the nonlinear defect of a gate from its best signed dictator, strongly enough that the slow-contraction regime `theta_i approx 1` is paid by the same defect.

A theorem of this form would close the most natural escape hatch left by Theorem 5.1. It is a composition-specific target; it is **not** the known-false claim that every prescribed coordinate of every Boolean function has a universal restriction payment.

Other possible escape parameters in a varying-seed construction include vanishing relevant influence, vanishing nonzero Fourier amplitudes (which make the seed-dependent Taylor constants large), and increasing seed dimension. Theorem 5.1 does not rule those out.

## 8. Current unrestricted numerical calibration

The live owner correction must be kept separate from the old Hod/read-once scale. Numaro's external 18-variable certificate gives the current public lower bound

\[
C_{\rm FEI}>6.521845710923046575.
\]

With

\[
c_*=2/\ln2=2.8853900817779268147\ldots,
\]

the earlier singleton-erasure compiler's corresponding raw threshold is

\[
C-c_*=3.6364556291451197602\ldots,
\]

and the concave-cap crossover solves

\[
\Psi(\tau)/\tau=C,
\qquad
\tau\approx0.1740316570325050.
\]

But the predecessor's finite recursive certificate is already stronger as a warning: its `F_5` forces **every** physical coordinate to have

\[
B_i/\operatorname{Inf}_i>4.2106705369\ldots.
\]

Thus the simple strategy “pay all JS by `2/ln2` and prove a raw singleton-erasure selector” cannot reach any `C<=7.0960606...`. A successful universal proof must exploit a potential, correlation between erasure and recombination, or a nonlocal stopping mechanism.

## 9. Literature/provenance check — no novelty claim

Fresh public checks on 21 September 2026 found:

- Numaro, `NUMARO-2026-016` (22 July 2026): the balanced monotone 18-variable seed and certified lower bound `>6.521845710923046575`, with exact influence `261/128`; this is external prior work and is not renamed here.
- González--MacManus--Pereyra, arXiv:2606.00246 (29 May 2026; updated 2 June): restriction entropy decrements and stopping binary trees as a route to FEI.
- Potapov, arXiv:2609.21563 (18 September 2026): FEI for plateaued functions with sharp class constant 4 and partially bent functions with sharp constant 2; this is structured-class progress, not full FEI.

A bounded search did not locate the fixed-seed convergence theorem above. That is **not** evidence of publication novelty or priority. The theorem should be treated as a fleet research implication until a dedicated literature review is performed.

## 10. Failed/retired routes preserved and exact remaining obligation

- The old every-prescribed-coordinate payment proposal remains false and is not used.
- Width-two tribes and the top-flip construction are no longer the numerical frontier for `rho_0`; the recursive Numaro family is stronger.
- The recursive Numaro family does **not** show `sup_f rho_0(f)=infinity`; Theorem 5.1 proves that this fixed-seed mechanism cannot do so.
- Finite depth improvements such as `7.11...` do not settle FEI and are not promoted to a universal optimum.

**Remaining universal obligation:** either prove a dimension-independent selector/stopping/potential inequality for arbitrary Boolean functions, or construct a genuinely nonstationary Boolean family escaping the fixed-seed summability mechanism. The most concrete next B14 derivation is the near-dictator stability target above: quantify `K_i(q)` by the nonlinear defect from a dictator and determine whether that payment can be amortized when the purity parameter approaches one.

**Full FEI remains OPEN.**
