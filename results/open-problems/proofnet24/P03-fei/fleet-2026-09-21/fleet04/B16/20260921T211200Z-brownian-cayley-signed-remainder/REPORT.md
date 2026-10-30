# B16 FEI interface C — Cayley/Dirac form of the Brownian source and a necessary signed remainder

**Date:** 21 September 2026  
**Scope:** `fleet04 / B16`, joint FEI interface C  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact source-side transform and finite-window remainder identities; a no-go theorem for an unconditional positive source-to-physical contraction; exact compatibility with the authentic central parent splitter. No publication-priority claim.

## 0. Joint target and exact peer revisions consumed

This run follows `FEI-JOINT-FOUR-ACCOUNTS-2026-09-21-192650Z`, interface C. It does not audit settled FEI material. It attacks the still-open signed/PSD source-to-physical arrow while keeping the live window and the signed ledgers visible.

The required cross-account inputs used substantively are:

1. **fleet02/B16 actual parent weights**  
   `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`  
   handoff commit `e4f58c7ac32a2699fb3c50da09922a7fa77f9958`.  
   After same-syndrome signed aggregation, an odd syndrome `R` has
   \[
   q_R=|R|,\qquad k_R=\#\{\hbox{clone pairs hit oddly}\},\qquad
   r_R=(q_R-k_R)/2,
   \]
   and central multiplier
   \[
   \varepsilon_R
   =2\frac{2^{-q_R}}{q_R}
   \left(\frac{2^{-k_R}}{k_R}-\frac{2^{-q_R}}{q_R}\right).
   \tag{0.1}
   \]
   Every doubled parent `j` receives the exact share
   \[
   \mu^{\rm cen}_{R,j}=\frac{\varepsilon_R}{r_R}b_R^2,
   \qquad
   \sum_{j\ {\rm doubled\ in}\ R}\mu^{\rm cen}_{R,j}
   =\varepsilon_R b_R^2.
   \tag{0.2}
   \]
   The `r_R=0` sector has `\varepsilon_R=0` and needs no split.

2. **fleet03/B18 signed physical flag curvature**  
   `proofnet24/P03-fei/fleet-2026-09-21/fleet03/B18/20260921T185340Z-signed-flag-curvature/REPORT.md`  
   proof commit `4843e50690013fd18b85dd8763b53bdc75da79e8`.  
   In the common minimizing-character gauge,
   \[
   \kappa_i(w)=p_i(w)+4o_i(w),
   \tag{0.3}
   \]
   and under the ordered physical flag
   \[
   \sum_i\mathbb E\kappa_i(W)\le2J(f),\qquad
   \sum_i\mathbb E\kappa_i(W)^2\le4J(f),\qquad
   \sum_i\mathbb E o_i(W)\le\frac12J(f).
   \tag{0.4}
   \]
   Thus orientation and opposite-sign overlap are genuine source data and cannot be dropped.

3. **fleet03/B18 parent-side pivotization**, read at scientific master `f536a48b1ae98e22bff294a10adbc59a3b8c907e`:  
   `proofnet24/P03-fei/fleet-2026-09-21/fleet03/B18/20260921T195855Z-parent-signed-pivotization/REPORT.md`, blob `e0ad48a8bb791b0536f5ceda92e3738cc378990a`.  
   For every authentic one-subcube parent mask, opposite-orientation overlap vanishes on the mask itself, and every positive rank-two parent pair has a deterministic physical pivot with exactly the same signed derivative curvature. Consequently a positive parent-indexed pair measure of total mass at most `mu_j` is paid by `mu_j J(g_j)`. The missing arrow is the construction of that authentic positive pair measure from the live signed compiler.

4. **fleet01/B16 retained-shell radial source**:  
   `proofnet24/P03-fei/fleet-2026-09-21/fleet01/B16/20260921T204046Z-terminal-shell-feature-projector/REPORT.md`, blob `6fd80765ed5b10f52b8aaf2464d671bd29c41892`, and  
   `.../RADIAL_FINITE_DIFFERENCE.md`, blob `4e797c5e83b27f740973c3902c390a738e6489de`.  
   These identify the terminal subtraction as the exact orthogonal projector onto `C_0\setminus D_d`, keep only frustrated retained relations after the Boolean phase switch, and reduce the Brownian threshold source to same-syndrome sums of explicit binomial boundary derivatives.

5. **fleet02 interactive half-band obstruction**, read at scientific master `f536a48b1ae98e22bff294a10adbc59a3b8c907e`:  
   `proofnet24/P03-fei/fleet-2026-09-21/fleet02/interactive/20260921T204926Z-threshold-contraction/HALFBAND_COLLISION_EXTENSION.md`, blob `2efc5dedf145a262700649c6e711c6a6fb91d622`.  
   It proves on genuine Boolean data that the exact positive current, including the actual active orbit and retained half-band terminal code, can have live-window size divided by `J(f)` tending to infinity. Therefore an unconditional dimension-free PSD contraction of the **positive current alone** into (0.4) cannot exist.

The purpose of the present calculation is to identify the exact signed operator sitting between the terminal shell and any eventual physical contraction, and to state precisely where a compensating signed remainder has to enter.

---

## 1. Brownian threshold coefficient as a Cayley transform

Let `N=2^n` be even. For even retained relation weight `k>=2`, fleet01 proves that, away from threshold endpoints of measure zero,
\[
\lambda_k^{\rm th}(u)
=2^{1-k}\,\nabla^{k-1}p_{N-k}(a(u)),
\qquad
p_m(a)=2^{-m}\binom ma.
\tag{1.1}
\]
Define
\[
d_{N,k}(a):=2^{1-k}\nabla^{k-1}p_{N-k}(a),
\qquad 0\le a\le N-1.
\tag{1.2}
\]

### Theorem 1.1 — `P03-B16-BROWNIAN-CAYLEY-GENERATOR` — PROVED

The ordinary generating function is
\[
\boxed{
D_{N,k}(z):=\sum_{a=0}^{N-1}d_{N,k}(a)z^a
=2^{1-N}(1-z)^{k-1}(1+z)^{N-k}.
}
\tag{1.3}
\]
Hence, for arbitrary real coefficients `c_k` supported on even `k`, define
\[
B_a:=\sum_k c_kd_{N,k}(a),
\qquad
P(t):=\sum_k c_kt^{k-1}.
\tag{1.4}
\]
Then
\[
\boxed{
\sum_{a=0}^{N-1}B_az^a
=2^{1-N}(1+z)^{N-1}
P\!\left(\frac{1-z}{1+z}\right).
}
\tag{1.5}
\]
Moreover, because every active `k` is even,
\[
\boxed{B_{N-1-a}=-B_a.}
\tag{1.6}
\]

### Proof

The generating function of `p_{N-k}` is `((1+z)/2)^{N-k}` and each backward difference `nabla` multiplies it by `1-z`. Multiplying by `2^{1-k}` gives (1.3), and summing against `c_k` gives (1.5). Reciprocal substitution in (1.3) gives
\[
z^{N-1}D_{N,k}(1/z)=(-1)^{k-1}D_{N,k}(z)=-D_{N,k}(z),
\]
which proves (1.6). \(\square\)

This is an exact transform of the **same-syndrome signed sum**. It is not a coefficientwise estimate and does not destroy terminal-shell cancellation.

---

## 2. Exact Brownian norm = an absolute number-operator form

The threshold interval attached to `a=0,...,N/2-1` has length
\[
\Delta u_a=\frac{4(N-2a-1)}{N^2}.
\tag{2.1}
\]
Therefore the Brownian same-syndrome energy
\[
\mathcal I(c)
:=\int_0^1\left(\sum_kc_k\lambda_k^{\rm th}(u)\right)^2du
\tag{2.2}
\]
is exactly
\[
\mathcal I(c)
=\frac4{N^2}\sum_{a<N/2}(N-2a-1)B_a^2.
\tag{2.3}
\]

Let `L` be the diagonal number operator on coefficient space,
\[
(LB)_a=(N-1-2a)B_a.
\tag{2.4}
\]
Since `N` is even, the spectrum of `L` consists of nonzero odd integers.

### Theorem 2.1 — `P03-B16-BROWNIAN-DIRAC-RESOLVENT` — PROVED

\[
\boxed{
\mathcal I(c)=\frac2{N^2}\langle B,|L|B\rangle.
}
\tag{2.5}
\]
Equivalently,
\[
\boxed{
\mathcal I(c)
=\frac4{\pi N^2}
\int_0^\infty
\left\langle LB,(L^2+t^2)^{-1}LB\right\rangle dt.
}
\tag{2.6}
\]
Every integrand in (2.6) is nonnegative, but **all signed relation-weight cancellation has already happened inside `B` before the square**.

### Proof

Equation (1.6) pairs `a` with `N-1-a` and turns (2.3) into (2.5). For a nonzero real scalar `ell`,
\[
|\ell|=\frac2\pi\int_0^\infty\frac{\ell^2}{\ell^2+t^2}dt.
\]
Apply this to the diagonal operator `L`. \(\square\)

Thus the Brownian source is itself a **small-resolvent/Hardy expenditure**, not an unrelated full-line norm. This is the exact operator requested by the current interface-C route.

---

## 3. Relation-weight recurrence and signed R32 phase

### Theorem 3.1 — `P03-B16-CAYLEY-DIRAC-RELATION-RECURRENCE` — PROVED

On the basis (1.3),
\[
\boxed{
L D_{N,k}
=(k-1)D_{N,k-1}+(N-k)D_{N,k+1}.
}
\tag{3.1}
\]
Under the Cayley coordinate `t=(1-z)/(1+z)`, this is the first-order differential operator
\[
\boxed{
\mathcal A_N=(1-t^2)\frac d{dt}+(N-1)t.
}
\tag{3.2}
\]

There is also an exact Plancherel identity:
\[
\boxed{
\sum_aB_a^2
=\frac1\pi\int_{-\infty}^{\infty}
\frac{|P(iy)|^2}{(1+y^2)^N}dy.
}
\tag{3.3}
\]
For even `k`, put
\[
Q(y):=\sum_k c_k(-1)^{k/2}y^{k-1}.
\tag{3.4}
\]
Then `|P(iy)|^2=Q(y)^2`. If
\[
G(x):=\sum_k c_k(-1)^{k/2}
\sin^k x\cos^{N-k}x,
\tag{3.5}
\]
then
\[
\boxed{
\sum_aB_a^2
=\frac2\pi\int_0^{\pi/2}
\left(\frac{G(x)}{\sin x}\right)^2dx.
}
\tag{3.6}
\]

### Proof

The coefficient operator corresponding to (2.4) is `(N-1)-2z d/dz`. Substituting (1.5) gives (3.2), and applying it to `t^{k-1}` gives (3.1). Equation (3.3) is circle Plancherel followed by `y=tan(theta/2)`. For even `k`, `P(iy)=-iQ(y)`. Substituting `y=tan x` gives (3.6). \(\square\)

### Compiler meaning

The factor `(-1)^{k/2}` in (3.4)-(3.5) is exactly the R32 `0 mod 4 / 2 mod 4` sign. Hence the negative entropy credits are not an external decoration of the Brownian source: **they are the imaginary-axis phase of its exact Cayley transform**. Any termwise absolute-value payment of the relation weights destroys this identity.

A harmless envelope, useful only for comparison, is
\[
\mathcal I(c)
\le\frac2N\sum_aB_a^2
=\frac4{\pi N}\int_0^{\pi/2}
\left(\frac{G(x)}{\sin x}\right)^2dx.
\tag{3.7}
\]
This is not asserted to be an `O(J)` bound.

---

## 4. The actual central parent splitter commutes with the Brownian/Dirac transform

Restore active syndromes. For each odd syndrome `R`, let `c_{R,k}` be the signed retained count/coefficient at physical relation weight `k` before the threshold transform, and construct `B_R` from (1.4). Let
\[
\mathcal I_R:=\frac2{N^2}\langle B_R,|L|B_R\rangle.
\tag{4.1}
\]
The fleet01 terminal-shell theorem identifies these `I_R` exactly as the same-syndrome Brownian threshold energies.

For `r_R>0` define the parent-resolvent mass
\[
\boxed{
\widetilde\mu^{\mathsf M}_{R,j}
:=\frac{\varepsilon_R}{r_R}\,\mathcal I_R
\quad(j\text{ doubled in }R).
}
\tag{4.2}
\]
If `r_R=0`, `epsilon_R=0` and put the mass equal to zero.

### Theorem 4.1 — `P03-B16-BROWNIAN-AUTHENTIC-PARENT-SPLIT` — PROVED

\[
\boxed{
\sum_{j\ {\rm doubled\ in}\ R}
\widetilde\mu^{\mathsf M}_{R,j}
=\varepsilon_R\mathcal I_R,
}
\tag{4.3}
\]
and globally
\[
\boxed{
\sum_j\widetilde\mu_j^{\mathsf M}
=\sum_R\varepsilon_R\mathcal I_R,
\qquad
\widetilde\mu_j^{\mathsf M}:=
\sum_{R:j\ {\rm doubled}}
\frac{\varepsilon_R}{r_R}\mathcal I_R.
}
\tag{4.4}
\]

This is the **Brownian image of fleet02's actual parent splitter**. It uses the same `epsilon_R/r_R` and therefore preserves both inverse-number factors and exact singleton annihilation. It is not a claim that `widetilde mu_j^M` equals the fixed-Borel-time parent mass `mu_j(s)`; the threshold/Dirac transform has already integrated a different source parameter.

Crucially, (4.4) still does **not** manufacture the missing authentic positive parent-pair measure. Fleet03's pivotization theorem becomes applicable only after a source-valid pair representation is derived. No singular or synthetic pair law is inserted here.

---

## 5. Live finite window = full PSD bank minus an exact positive tail remainder

Let `W` be the actual live Borel window. Apply the square-first theorem after the positive syndrome multiplier `epsilon_R` is inserted. Define
\[
\mathcal T_{\rm cen}(W^c)
:=\int_{(0,\infty)\setminus W}
\frac{\mathcal E_{\rm cen}(s)}{s^3}\,ds\ge0.
\tag{5.1}
\]
Then identically
\[
\boxed{
\int_W\frac{\mathcal E_{\rm cen}(s)}{s^3}ds
=
\int_0^\infty\frac{\mathcal E_{\rm cen}(s)}{s^3}ds
-\mathcal T_{\rm cen}(W^c).
}
\tag{5.2}
\]

The sharp full-line restriction-kernel comparison from the current source line gives
\[
\int_0^\infty\frac{\mathcal E_{\rm cen}(s)}{s^3}ds
\le\frac{\pi^2}{2}N^2\sum_R\varepsilon_R\mathcal I_R.
\tag{5.3}
\]
Combining (2.6), (4.4), and (5.2):
\[
\boxed{
\int_W\frac{\mathcal E_{\rm cen}(s)}{s^3}ds
\le
2\pi\sum_R\varepsilon_R
\int_0^\infty
\langle LB_R,(L^2+t^2)^{-1}LB_R\rangle dt
-\mathcal T_{\rm cen}(W^c).
}
\tag{5.4}
\]

Equation (5.4) is the desired **finite-window-plus-remainder** form. The complement of the live window is retained as an explicit negative credit; it is not silently discarded by full-line extension.

However, the fleet02 half-band collision theorem shows that even this finite live positive current can exceed every universal constant times `J(f)`. Therefore the tail term in (5.4), by itself, is not the missing FEI cancellation.

---

## 6. NO-GO — an unconditional positive interface-C contraction cannot exist

The fleet03 physical sink (0.4) is universally `O(J)`. The fleet02 half-band theorem gives a genuine Boolean family, at the actual half-band terminal cutoff, for which
\[
\frac{\displaystyle\int_W\mathcal E_{\rm cen}(s)s^{-3}ds}{J(f)}\to\infty.
\tag{6.1}
\]
The same family has bounded `H/I`, so it is not an FEI counterexample.

### Theorem 6.1 — `P03-B16-POSITIVE-INTERFACE-C-NOGO` — PROVED

There is no universal constant `C` for which the complete live positive central current can, for all Boolean functions, satisfy a PSD contraction of the form
\[
\int_W\frac{\mathcal E_{\rm cen}(s)}{s^3}ds
\le C\sum_i\mathbb E\kappa_i(W_i)^2
\tag{6.2}
\]
or the corresponding linear-curvature form with `sum_i E kappa_i`, for any authentic physical flag law to which the fleet03 bounds apply.

### Proof

The right side of (6.2) is at most `4CJ(f)` by (0.4), while (6.1) makes the left/right ratio unbounded. The linear version is identical using the `2J(f)` bound. \(\square\)

This pinpoints the logical location of the missing cancellation. **The contraction must occur after a signed correction has been combined with the positive current, not from the positive current alone.** The correction must come from one or more ledgers the live owner route requires us to preserve: R16/moment refunds, negative entropy credits not already absorbed by same-syndrome aggregation, and/or the terminal/boundary response. The counterexample proves this is a source gate, not a weakness of fleet03's physical sink.

For the four-point family in the half-band extension, the positive full-current asymptotic is `4/(27 n^3)`, while replacing the triple multiplier `4/9` by the central `11/288` gives
\[
\boxed{
\int_W\frac{\mathcal E_{\rm cen}(s)}{s^3}ds
\sim\frac{11}{864n^3},
}
\tag{6.3}
\]
whereas `J(f)=8n/2^{n+1}` in that notation. Thus any all-Boolean signed compiler inequality that reduces the central sector to `O(J)` has to cancel essentially all of this polynomial-scale packet on that family.

---

## 7. Exact candidate shape for the necessary signed correction: Ward multiplier gap

The central current multiplier and the already-proved Ward selector multiplier obey
\[
W_R:=1-\frac1{q_R},
\qquad
0\le\varepsilon_R\le\frac{11}{192}W_R,
\tag{7.1}
\]
with equality at `(q,k)=(3,1)`. Therefore define
\[
\boxed{
\rho_R:=\frac{11}{192}W_R-\varepsilon_R\ge0.
}
\tag{7.2}
\]
At every fixed source coefficient field,
\[
\boxed{
\mathcal E_{\rm cen}
=\frac{11}{192}\mathcal W-\mathcal R_{\rm Ward},
\qquad
\mathcal W:=\sum_R W_Rb_R^2,
\quad
\mathcal R_{\rm Ward}:=\sum_R\rho_Rb_R^2\ge0.
}
\tag{7.3}
\]
The same identity survives the Brownian/Cayley transform:
\[
\boxed{
\sum_R\varepsilon_R\mathcal I_R
=\frac{11}{192}\sum_RW_R\mathcal I_R
-\sum_R\rho_R\mathcal I_R.
}
\tag{7.4}
\]

Equation (7.4) is an exact **signed remainder decomposition**, and the `q=3,k=1` obstruction saturates the coefficient. It explains why the half-band example is the correct stress test for any claimed Ward/R16 compensation.

But this run does **not** spend (7.4) as if `mathcal W` were automatically a free negative term in the final entropy ledger. The source reports prove the Ward selector dissipation and its comparison with the current; they do not, by that comparison alone, certify that `11/192` of the aggregate Ward square is an unspent signed compiler credit at precisely the same live stage. That source gate remains to be proved from the exact R16/Shapley/terminal ledger. Treating a comparison bank as a booked refund would weaken the proof gate and is not done here.

What (7.4) provides is a narrow next theorem: identify, in the authentic live compiler identity, a co-located signed refund whose same-syndrome multiplier dominates `11W_R/192` (or its exact smaller `epsilon_R`), with no reuse. Once that is done, the remaining nonnegative parent mass can be passed through fleet03's exact parent pivotization and signed physical curvature bank.

---

## 8. What moved / exact next implication

### Proved here

1. Brownian threshold same-syndrome coefficients have the exact Cayley generator (1.5).
2. Their complete energy is the absolute number-operator form (2.5), equivalently the positive Dirac resolvent (2.6).
3. The imaginary-axis/Cayley phase is exactly the R32 `(-1)^{|A|/2}` sign, so `2 mod 4` credits remain inside the transform before squaring.
4. The authentic fleet02 central parent splitter `epsilon_R/r_R` commutes exactly with this transform, giving (4.4).
5. The live window has the exact full-minus-tail remainder form (5.4).
6. The fleet02 half-band Boolean family plus fleet03's signed physical sink proves that an unconditional positive current-to-physical PSD contraction is impossible.
7. The exact Ward multiplier gap (7.4) identifies a source-sized signed correction capable of cancelling the worst `q=3,k=1` central mode **if and only if** the live compiler ledger supplies that refund without reuse.

### Preserved

- original-coordinate physical orientation and opposite-sign overlap;
- same-syndrome signed aggregation;
- `0 mod 4 / 2 mod 4` R32 cancellation;
- dual-code multiplicity and exact terminal-shell projection;
- R16/moment refunds and terminal/boundary payments as unspent ledgers unless explicitly identified;
- the live finite window and its positive complement tail.

### Refuted / not retried

- positive current alone `<= C J`;
- full-line Brownian bank alone `<= C J`;
- scalar parent postcompression followed by TV/positive plaquette inversion;
- unsigned support disagreement as a substitute for signed derivative curvature;
- coefficientwise absolute payment of radial relation weights;
- dropping the live-window complement or terminal subtraction.

### Exact next implication

Prove directly from the authentic R16/Shapley/terminal identity that the live `q,k` current is accompanied, before positivity, by a signed same-syndrome correction `C_R` satisfying
\[
C_R\ge \varepsilon_R\mathcal I_R
\quad\text{(or, sufficiently, }C_R\ge\tfrac{11}{192}W_R\mathcal I_R\text{)}
\tag{8.1}
\]
for the half-band stress packet, with the corresponding parent allocation when `r_R>0`. If only part of (8.1) is available, the residual should be kept nonnegative and then pushed through the fleet03 parent-signed pivotization theorem. If (8.1) fails on the authentic compiler, preserve the resulting Boolean/R32 counterpacket and identify the uncancelled signed component rather than reverting to the already-refuted positive-current route.

Full unrestricted FEI remains **OPEN / NOT PROVED**.
