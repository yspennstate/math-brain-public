# B16 FEI interface C — finite-resolvent sine RKHS, quartic first-separator, and co-located R16 remainder

**Date:** 21 September 2026  
**Scope:** `account04 / B16`, joint FEI interface C  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact precompression source identities and a new local ledger decomposition. No publication-priority claim.

## 0. Why this run changes the interface-C target

The fresh joint state has two hard constraints which must be respected simultaneously.

First, account02's genuine half-band Boolean counterfamily refutes any universal `O(J)` contraction of the **complete positive current** into the physical flag bank. Second, account02/B16's codimension-normalization theorem shows that compressing the authentic source to scalar parent masses `mu_j` and then reconstructing an independent positive parent-pair measure can cost at least `c_j/2` per parent. So the missing map must stay before scalar parent compression and must insert the compensating signed R16/entropy/terminal terms before the final positivity step.

This run supplies one exact piece of that missing map. It places the original finite small-resolvent window and its high-resolvent refund in a single positive sine-kernel/RKHS calculus **at the genuine gate correlation level**, before total variation and before the `mu_j` compression. The same calculation also identifies the first surviving source coefficient after the distance-four cancellation: it is exactly the positive count of first-separated frustrated weight-four relations; every degree `>=6` term remains in one signed remainder with the R32 `0 mod 4 / 2 mod 4` phase intact.

The old P03 report `proofnet24/P03-fei/runs/2026-09-15/2026-09-15_20-29-28__run-report.md` already proved the low/high Borel multiplier formulas and R16/R32 equivalence. The new material here is the **PSD polarization in the actual two-cell gate correlations**, its exact quartic first-separator coefficient, and the resulting parent-local no-reuse ledger identity when composed with the current four-account interface.

## 1. Fresh peer revisions consumed

Scientific master immediately before this package was

`06c8f7e9f5ef388e79719afa72aedecca5db4003`.

The required current inputs used substantively are:

1. **account02/B16 actual parent weights**  
   `proofnet24/P03-fei/fleet-2026-09-21/account02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`, handoff commit `e4f58c7ac32a2699fb3c50da09922a7fa77f9958`.  
   For an odd active syndrome `R`, with `q_R=|R|`, odd-block degree `k_R`, and `r_R=(q_R-k_R)/2`, the authentic central multiplier is
   \[
   \varepsilon_R
   =2\frac{2^{-q_R}}{q_R}
   \left(\frac{2^{-k_R}}{k_R}-\frac{2^{-q_R}}{q_R}\right),
   \]
   and every doubled parent receives the exact share
   \[
   \mu^{\rm cen}_{R,j}=\frac{\varepsilon_R}{r_R}b_R^2.
   \]
   Same-syndrome signed cancellation is already inside `b_R` before this square.

2. **account02/B16 precompression warning**  
   `proofnet24/P03-fei/fleet-2026-09-21/account02/B16/20260921T193735Z-codimension-normalization-parent-bridge/REPORT.md`.  
   It proves that a direct postcompression positive/TV lift through a codimension-`c_j` parent plaquette costs at least `c_j/2` unless a new codimension-weighted moment is paid. The present calculation therefore remains at the signed gate packet before `mu_j` is inverted into any physical pair law.

3. **account03/B18 signed physical flag curvature**  
   `proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260921T185340Z-signed-flag-curvature/REPORT.md`, proof commit `4843e50690013fd18b85dd8763b53bdc75da79e8`.  
   In the minimizing-character gauge,
   \[
   \kappa_i(w)=p_i(w)+4o_i(w),
   \]
   with
   \[
   \sum_i\mathbb E\kappa_i(W)\le2J(f),\qquad
   \sum_i\mathbb E\kappa_i(W)^2\le4J(f),\qquad
   \sum_i\mathbb Eo_i(W)\le\frac12J(f).
   \]
   The opposite-orientation term is not discarded below.

4. **account03/B16 signed square-root resolvent**  
   `proofnet24/P03-fei/fleet-2026-09-21/account03/B16/20260921T211732Z-signed-square-root-resolvent/REPORT.md`, read at master `c2e41988aeaa46ff773905a305106124a72c14d2`.  
   It gives the exact active-syndrome factorization
   \[
   \mathbb E|D_\phi|^2
   =4\sum_j\|\partial_jL^{-1/2}F_\phi^-\|_2^2
   \]
   and locates the required signed refund insertion **before** the final local square is sent to physical curvature.

5. **account01/B16 threshold boundary / signed-source warning**  
   `proofnet24/P03-fei/fleet-2026-09-21/account01/B16/20260921T214038Z-threshold-boundary-krawtchouk/REPORT.md`, blob `9134c75b602364abcdceed70aa9488a28b33986e` at master `c2e41988aeaa46ff773905a305106124a72c14d2`.  
   It proves that fixed shell parity cannot pay the Brownian source pointwise in threshold; the compensating ledger must remain integrated/cross-degree.

6. **account04/B16 immediately preceding handoff**  
   `proofnet24/P03-fei/fleet-2026-09-21/account04/B16/20260921T211200Z-brownian-cayley-signed-remainder/HANDOFF.md`, blob `6cfcffff21f5faef2868b2025468bcaed03cf542`.  
   It identifies the exact Brownian/Dirac source, commutation with the authentic parent splitter, and the decisive no-go for a positive-current-only closure.

## 2. Exact gate notation

Let `M` be one actual pre-gate mask code containing `RM(1,n)`, and let `g=1_Q` be the next Boolean mask bit, so in sign form `(-1)^g` flips exactly the gate face `Q`. Put

\[
D=M^\perp\subseteq C_0=RM(1,n)^\perp.
\]

Thus `D` has no nonzero word of weight two.

For `z in {0,b_f}` and `m in M`, split the normalized correlation into the two gate cells
\[
 u_z(m)=\frac1N\sum_{x\notin Q}(-1)^{z_x+m_x},
 \qquad
 v_z(m)=\frac1N\sum_{x\in Q}(-1)^{z_x+m_x}.
\tag{2.1}
\]
Then
\[
 \beta(z+m)=u_z(m)+v_z(m),
 \qquad
 \beta(z+m+g)=u_z(m)-v_z(m).
\tag{2.2}
\]

For Borel time `s`, define the signed precompression gate packet
\[
\boxed{
G_{M,g,f}(s)
:=\mathbb E_{m\in M}
\left[
\sin(su_{b_f}(m))\sin(sv_{b_f}(m))
-
\sin(su_0(m))\sin(sv_0(m))
\right].
}
\tag{2.3}
\]
This object still contains the Boolean/comparator subtraction and all relation signs. No relationwise absolute value or parent scalar compression has occurred.

## 3. PROVED — finite-resolvent polarization is a positive sine RKHS

For `T>0`, set
\[
F_T(x)=x\log(1+T/x),\quad x>0,
\qquad F_T(0)=0,
\tag{3.1}
\]
and define
\[
\boxed{
K_T(u,v)=F_T((u+v)^2)-F_T((u-v)^2).
}
\tag{3.2}
\]

### Theorem 3.1 — `P03-B16-FINITE-RESOLVENT-SINE-RKHS`

For all real `u,v`,
\[
\boxed{
K_T(u,v)
=2\int_0^\infty w_T(s)\sin(us)\sin(vs)\,ds,
}
\tag{3.3}
\]
where
\[
\boxed{
 w_T(s)=\int_0^T\sqrt t\,e^{-s\sqrt t}\,dt
 =\frac4{s^3}\left[1-e^{-s\sqrt T}
 \left(1+s\sqrt T+\frac12s^2T\right)\right]
}
\tag{3.4}
\]
for `s>0`, with `w_T(0)=2T^{3/2}/3` by continuity.

Consequently `K_T` is a positive-semidefinite scalar kernel. More generally for a finite resolvent interval `0<=A<B<infinity`,
\[
K_{[A,B]}:=K_B-K_A
=2\int_0^\infty w_{[A,B]}(s)\sin(us)\sin(vs)\,ds,
\tag{3.5}
\]
with
\[
w_{[A,B]}(s)=\int_A^B\sqrt t\,e^{-s\sqrt t}\,dt\ge0,
\]
so
\[
0\preceq K_{[A,B]}\preceq K_B.
\tag{3.6}
\]

### Proof

Since
\[
F_T(x)=\int_0^T\frac{x}{x+t}\,dt,
\]
one has
\[
K_T(u,v)=\int_0^T t\left[
\frac1{(u-v)^2+t}-\frac1{(u+v)^2+t}
\right]dt.
\]
Use
\[
\frac1{x^2+t}
=\frac1{\sqrt t}\int_0^\infty e^{-s\sqrt t}\cos(xs)\,ds
\]
and
\[
\cos((u-v)s)-\cos((u+v)s)=2\sin(us)\sin(vs).
\]
Fubini is absolute for finite `T`, giving (3.3). Equation (3.4) follows after the substitution `q=sqrt(t)`. For any finite coefficients `a_j`,
\[
\sum_{j,k}a_ja_kK_T(x_j,x_k)
=2\int_0^\infty w_T(s)
\left(\sum_ja_j\sin(x_js)\right)^2ds\ge0,
\]
which proves PSD; the interval statement is identical. QED.

### Why this is the right category

This is **not** the refuted positive-current estimate. The kernel is PSD, but the compiler evaluates it in the signed difference between the `f` packet and the comparator packet. The signed subtraction remains outside the RKHS inner product and is not replaced by total variation.

## 4. PROVED — exact compiler gate through the finite-resolvent RKHS

Let
\[
\Phi_t(x)=\frac{x}{x+t}.
\]
The exact compiler gate formula is
\[
R_M(t)-R_{M+\langle g\rangle}(t)
=\frac N2\,\mathbb E_m
\left[
\Phi_t((u_f+v_f)^2)-\Phi_t((u_f-v_f)^2)
-
\Phi_t((u_1+v_1)^2)+\Phi_t((u_1-v_1)^2)
\right].
\tag{4.1}
\]
Applying the same resolvent representation pointwise gives
\[
\boxed{
R_M(t)-R_{M+\langle g\rangle}(t)
=N\sqrt t\int_0^\infty e^{-s\sqrt t}
G_{M,g,f}(s)\,ds.
}
\tag{4.2}
\]
Hence for every finite resolvent window `[A,B]`,
\[
\boxed{
\int_A^B\left(R_M(t)-R_{M+\langle g\rangle}(t)\right)dt
=N\int_0^\infty w_{[A,B]}(s)G_{M,g,f}(s)\,ds.
}
\tag{4.3}
\]

Equation (4.3) is the authentic precompression source representation. It uses the real gate face, the real Boolean phase, the comparator, and the exact finite window. It never introduces a parent-indexed positive pair law.

## 5. PROVED — distance four kills the quadratic source and the first survivor is the physical weight-four packet

### Lemma 5.1 — exact quadratic cancellation

For each `z in {0,b_f}`,
\[
\boxed{
\mathbb E_{m\in M}u_z(m)v_z(m)=0.
}
\tag{5.1}
\]

### Proof

Expand `u_zv_z`. Every term pairs one `x notin Q` with one `y in Q`, so `x!=y`. Averaging over `m in M` gives zero unless the weight-two word `e_x+e_y` lies in `D=M^perp`. But `D subset C_0` has minimum nonzero weight at least four. QED.

Thus `G(s)=O(s^4)` at the origin. This is the same distance-four cancellation seen in the phase-switch compiler, now at the exact finite-resolvent gate kernel.

### Theorem 5.2 — `P03-B16-QUARTIC-FIRST-SEPARATOR`

Let
\[
C_4(M,g,f)
:=\#\left\{
A\in D:\ |A|=4,\ g(A)=1,\ f_A=-1
\right\},
\tag{5.2}
\]
where `g(A)=sum_{x in A} g(x) mod 2`. Then
\[
\boxed{
\mathbb E_m
\left[(u_f^3v_f+u_fv_f^3)-(u_1^3v_1+u_1v_1^3)\right]
=-\frac{12}{N^4}C_4(M,g,f).
}
\tag{5.3}
\]
Consequently
\[
\boxed{
G_{M,g,f}(s)
=\frac{2C_4(M,g,f)}{N^4}s^4+O(s^6).
}
\tag{5.4}
\]

### Proof

Expand the fourth moment. Repeated indices reduce the dual word to weight zero or two; the weight-two terms vanish as above. The surviving terms are four distinct vertices whose indicator word lies in `D`. The two monomials `u^3v` and `uv^3` select exactly those four-sets meeting `Q` in odd cardinality, namely `g(A)=1`. Each unordered four-set has `3!=6` orderings. Therefore
\[
\mathbb E(u_f^3v_f+u_fv_f^3)
=\frac6{N^4}\sum_{A\in D,|A|=4,g(A)=1}f_A,
\]
while the comparator has the same formula with `f_A=1`. Their difference is `-12/N^4` for each frustrated relation and zero otherwise. The sine Taylor expansion and (5.1) give (5.4). QED.

This identifies the first nonzero source with a genuine first-separated frustrated weight-four relation packet. There is no artificial positive generator baseline at this order.

## 6. PROVED — exact all-order signed relation formula; quartic debit plus higher signed remainder

The preceding theorem is only the first term of an exact identity. Put `theta=s/N`. Character expansion over `M` gives
\[
\boxed{
G_{M,g,f}(s)
=2\sum_{\substack{A\in D\\g(A)=1\\f_A=-1}}
(-1)^{|A|/2}
\sin^{|A|}(\theta)\cos^{N-|A|}(\theta).
}
\tag{6.1}
\]

Therefore
\[
\boxed{
G_{M,g,f}(s)
=2C_4(M,g,f)\sin^4\theta\cos^{N-4}\theta
+G_{M,g,f}^{\ge6}(s),
}
\tag{6.2}
\]
where
\[
G^{\ge6}
=2\sum_{\substack{A\in D,\ |A|\ge6\\g(A)=1,\ f_A=-1}}
(-1)^{|A|/2}
\sin^{|A|}\theta\cos^{N-|A|}\theta.
\tag{6.3}
\]

The quartic piece has fixed positive R32 sign. Every `2 mod 4` shell inside `G^{>=6}` remains a genuine negative credit. No absolute value is taken on (6.3).

### Signed physical interpretation of the quartic piece

Every weight-four word of `C_0` is an affine parallelogram. On such a plaquette, write `r_f,r_g in {0,1}` for the Boolean and gate-mask frustration bits. The positive quartic event is exactly `r_f=r_g=1`, and pointwise
\[
\boxed{
1_{\{r_f=r_g=1\}}
=\frac12\left(r_f+r_g-r_{fg}\right).
}
\tag{6.4}
\]
This is the correct signed polarization. Replacing the right side by a union bound would erase the compensating `-r_{fg}` term. The final physical sink remains account03's oriented `kappa=p+4o`; (6.4) is **not** used to delete `o`.

## 7. PROVED — the small-resolvent expenditure and R16 high-resolvent correction are co-located on the same signed gate packet

For the actual cutoff `T=2`, define
\[
\boxed{
 w_{<2}(s)=\frac4{s^3}
 \left[1-e^{-\sqrt2s}(1+\sqrt2s+s^2)\right],
}
\tag{7.1}
\]
\[
\boxed{
 w_{>2}(s)=\frac4{s^3}
 e^{-\sqrt2s}(1+\sqrt2s+s^2).
}
\tag{7.2}
\]
Then
\[
w_{<2},w_{>2}\ge0,
\qquad
\boxed{w_{<2}(s)+w_{>2}(s)=\frac4{s^3}}.
\tag{7.3}
\]

The formulas (7.1)--(7.3) are the inherited low/high Borel kernels from `P03-BOREL-R32-DUALITY-76`; the point here is their exact placement in the **same precompression RKHS packet** (2.3).

For a finite compiler prefix ending at `D_d`, let
\[
\mathfrak G_d(s)
=2N\sum_{\substack{A\in C_0\setminus D_d\\f_A=-1}}
(-1)^{|A|/2}
\sin^{|A|}(s/N)\cos^{N-|A|}(s/N).
\tag{7.4}
\]
First-separation telescoping of (6.1) gives `mathfrak G_d = N sum_g G_g`. Hence
\[
\boxed{
\mathcal Q_{d,<2}
=\int_0^\infty w_{<2}(s)\mathfrak G_d(s)\,ds,
}
\tag{7.5}
\]
while the authentic high-resolvent term is
\[
\boxed{
\Delta_{d,>2}
=\int_0^\infty w_{>2}(s)\mathfrak G_d(s)\,ds.
}
\tag{7.6}
\]
Their sum is exactly
\[
\boxed{
\mathcal Q_{d,<2}+\Delta_{d,>2}
=4\int_0^\infty\frac{\mathfrak G_d(s)}{s^3}\,ds
=H_{\rm nat}(f)-R_d(f).
}
\tag{7.7}
\]

This is the no-reuse fact needed by the current interface: the R16 high-resolvent correction is not an external budget that may be spent independently after the positive current is formed. It is the **complementary positive Borel multiplier on the same signed R32 packet**. The signs are in `mathfrak G_d`, not in the multipliers.

## 8. Parent-local composition with the current three-phase field

For an authentic doubled parent `j`, the account04/account02 current field is
\[
C_j(s;h)
:=D_jF_s^{\rm odd}(h)
=\frac12\Delta_{g_{j,0}}\Delta_{g_{j,1}}\Delta_f\Psi_s(h).
\tag{8.1}
\]
The already-proved full-line entropy-curvature identity is
\[
\int_0^\infty\frac{C_j(s;h)}{s^3}\,ds
=\frac14\Delta_{g_{j,0}}\Delta_{g_{j,1}}
\left[\mathscr D_d(fh)-\mathscr D_d(h)\right].
\tag{8.2}
\]

Define the co-located small/high parent pieces
\[
S_j(h)=\int_0^\infty w_{<2}(s)C_j(s;h)\,ds,
\qquad
H_j(h)=\int_0^\infty w_{>2}(s)C_j(s;h)\,ds.
\tag{8.3}
\]
Then (7.3) and (8.2) give the exact parent ledger identity
\[
\boxed{
S_j(h)+H_j(h)
=\Delta_{g_{j,0}}\Delta_{g_{j,1}}
\left[\mathscr D_d(fh)-\mathscr D_d(h)\right].
}
\tag{8.4}
\]

For an actual Borel live window `W`, keep the complement explicit:
\[
\boxed{
\int_W w_{<2}(s)C_j(s;h)\,ds
=\Delta_{g_{j,0}}\Delta_{g_{j,1}}
[\mathscr D_d(fh)-\mathscr D_d(h)]
-H_j(h)
-\int_{W^c}w_{<2}(s)C_j(s;h)\,ds.
}
\tag{8.5}
\]

Equation (8.5) is the sought placement of the **live finite window and remainder at the same authentic parent operator**. Neither remainder is silently made positive. The kernel behind the finite small-resolvent window is PSD by Theorem 3.1, but the Boolean/comparator and terminal-code differences remain signed.

This is precisely where account03's square-root-resolvent result says a refund must be inserted: before the final local square is sent to the physical `kappa` bank.

## 9. Compatibility with account02's actual parent weights — and what is still not proved

The scalar factor `epsilon_R/r_R` in account02's authentic parent splitter depends only on the active syndrome. It therefore commutes with the radial/Borel integrations above. One may carry the same doubled-parent label `j` through (8.3)--(8.5) without reconstructing a new pair law or changing parent multiplicity.

What is **not** proved is the final inequality which would turn the signed combination on the right of (8.5) into a residual nonnegative parent-pair measure of total intensity controlled by the account03 physical bank. In particular:

- we do **not** assert that the complete positive current `sum_j mu_j` is `O(J)`; that is false on the half-band counterfamily;
- we do **not** invert a scalar `mu_j` through the tiny parent plaquette amplitude; account02 proved the codimension barrier to that shortcut;
- we do **not** discard `o_i` from `kappa_i=p_i+4o_i`;
- we do **not** positive-part `G^{>=6}` or the terminal subtraction;
- we do **not** spend the R16 high-resolvent term twice. It appears only through the co-located `H_j` / `w_{>2}` complement.

The remaining implication is now narrower:

> Starting from the local signed square-root-resolvent fields of account03/B16, insert the exact co-located operator `H_j + outside-window` from (8.5) **before** the local square, and prove that the residual quadratic form is representable by a positive parent-indexed physical pair measure whose total parent intensity is paid once by account03/B18's oriented `kappa` bank.

If this fails, the falsifier should be an authentic compiler packet for the **refunded** local form, not another example showing that the already-refuted complete positive current is too large.

## 10. Verification

`check_finite_resolvent_rkhs_refund.py` is standard-library only. It verifies:

- the exact low/high multiplier sum `w_<2+w_>2=4/s^3` at multiple scales;
- 30 numerical finite-resolvent polarization identities (3.3);
- 400 random PSD quadratic forms for `K_T`;
- 352 exact rational distance-four quadratic cancellations;
- 176 exact rational quartic first-separator identities (5.3);
- 528 direct numerical comparisons of the gate packet with the all-order relation formula (6.1).

Checker SHA-256: `beed9be67915c3cdcac8188906dd98652b9e64cdb7c53b9db4320295b1729d42`.

## 11. Classification

**PROVED:** Theorems 3.1, 4.2, 5.1, 5.2, exact relation identity (6.1), and the parent-local co-located ledger (8.4)--(8.5).

**PRESERVED SIGNED REMAINDER:** all relation sizes `>=6`, including negative `2 mod 4` R32 credits; the exact high-resolvent/R16 complement; the finite-window complement; the terminal `C_0-D_d` subtraction; opposite-sign physical overlap.

**OPEN:** the final refunded local-field-to-oriented-physical-curvature contraction.

**Full unrestricted FEI:** **OPEN / NOT PROVED**.
