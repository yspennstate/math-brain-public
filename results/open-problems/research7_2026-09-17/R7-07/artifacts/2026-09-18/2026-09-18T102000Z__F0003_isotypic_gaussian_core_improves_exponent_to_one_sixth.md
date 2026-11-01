Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0003 — an isotypic Gaussian core and the cubic random-regular singularity exponent `1/6`

Date: 2026-09-18 UTC.  
Slot: `R7-07`, native ID `6aabe8413f60819197825dd81ca138ae`.  
Target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / *Probability Surveys* 18 (2021), Section 5 immediately after Theorem 5.2.  
Primary undirected input: Jiaoyang Huang, *Invertibility of adjacency matrices for random d-regular graphs*, arXiv:1807.06465.  
Local row input: Hoi H. Nguyen and Amanda Pan, *A note on the singularity probability of random directed d-regular graphs*, arXiv:2308.06461 / *European Journal of Combinatorics* (2024), used only for the one-row `U_{d,p}` characteristic-function calculation already transferred in the preceding R7-07 artifacts.

Frozen metric:

\[
a_3:=\sup\{a\ge0:\Pr(A_{n,3}\text{ singular})\le n^{-a+o(1)}\}.
\]

Metric before this artifact: **`a_3 >= 1/7`** from `2026-09-18T095000Z__F0003_symmetric_cubic_gluing_improves_exponent_to_one_seventh.md`.  
Metric after the theorem below: **`a_3 >= 1/6` — MOVEMENT.**

Methods in this iteration: **B14 FIND THE GROUP ACTING / B6 DEFORM TO A SOLVED POINT / B29 ADD THE POINTS AT INFINITY.** The immediately preceding triple was B11/B25/B18.

The source-level target remains `a_3=1`, and full source closure requires exponent `d-2` for every fixed `d>=3`. This artifact is **PARTIAL**, not source closure.

---

## 1. Starting point and the two apparent `1/7` barriers

The preceding artifact proved, for every fixed `d>=3`,

\[
\Pr(A_{n,d}\text{ singular})\le O_d(n^{2-d})+n^{-1/7+o(1)}.
\]

After the symmetric cubic gluing was handled, the two largest bounds in that argument were

\[
O\!\left(\frac{p^{7/2}(\log n)^{3/2}}{\sqrt n}\right)
\tag{1.1}
\]

for the exact row-normalization denominator, and

\[
O\!\left(\frac{p^7(\log n)^2}{n}\right)
\tag{1.2}
\]

for the aggregate fourth-order row remainder when the remainder was bounded uniformly on Huang's entire Fourier ball. The congruence correction also had a pointwise quadratic cross-term of order `p^(7/2)/sqrt(n)`.

All three losses are worst-case losses. The new observation is that Huang's quadratic form has an exact `S_p`-isotypic diagonalization. Once the symmetric Gaussian is written in those coordinates, the configurations that saturate (1.1) and (1.2) have exponentially small Gaussian weight. For the congruence lattice, one must average a Gaussian translate rather than bound the translate pointwise.

---

# 2. B14 — exact `S_p` isotypic diagonalization

As in the preceding artifact, let `A=A^T` have total entry sum zero, put

\[
r=A\mathbf1,
\qquad
u_{ij}=pA_{ij}-r_i,
\]

and let

\[
Q(A)=\frac{dnp^2}{4}\|A\|_F^2-
      \frac{(d-1)np}{2}\|r\|_2^2.
\]

Because `1^T r=0`, define

\[
B(r):=\frac{r\mathbf1^T+\mathbf1r^T}{p},
\qquad
H:=A-B(r).
\]

Then

\[
H\mathbf1=0,
\qquad
\langle H,B(r)\rangle_F=0,
\qquad
\|B(r)\|_F^2=\frac{2}{p}\|r\|_2^2.
\tag{2.1}
\]

Consequently

\[
\boxed{
Q(A)=\frac{dnp^2}{4}\|H\|_F^2+
      \frac{np}{2}\|r\|_2^2.
}
\tag{2.2}
\]

This is the exact decomposition into the row-sum-free symmetric representation and the standard representation of `S_p`. Moreover

\[
\boxed{u=pH+\mathbf1r^T}
\tag{2.3}
\]

and hence

\[
\boxed{
\|u\|_F^2=p^2\|H\|_F^2+p\|r\|_2^2.
}
\tag{2.4}
\]

In particular,

\[
Q(A)\ge \frac n2\|u\|_F^2
\tag{2.5}
\]

for every fixed `d>=3`.

Normalize

\[
X:=\sqrt n\,pH,
\qquad
Y:=\sqrt{np}\,r,
\qquad
Z:=\sqrt n\,u.
\]

Under the continuous Gaussian density proportional to `e^{-Q(A)}`, (2.2) says that `X` and `Y` are independent centered Gaussian vectors on their respective invariant subspaces, with

\[
Q=\frac d4\|X\|_F^2+rac12\|Y\|_2^2,
\qquad
Z=X+\mathbf1(Y/\sqrt p)^T.
\tag{2.6}
\]

Every coordinate of `Z` therefore has variance bounded by a constant depending only on `d`.

For row energies

\[
S_i:=\sum_j Z_{ij}^2,
\]

standard Gaussian norm concentration gives, for a sufficiently large fixed `K=K(d)`,

\[
\Pr\left(\|Y\|^2>Kp\log p\right)
+
\Pr\left(\max_i S_i>Kp\log p\right)
\le e^{-c_dp\log p}.
\tag{2.7}
\]

Call the complementary event the **isotypic Gaussian core**.

---

## 3. The row-normalization term is `1/6`-harmless on the Gaussian core

The exact denominator correction from the preceding artifact is

\[
E_2(A)=\frac{dn}{2}\sum_iU_i\frac{pr_i}{1+pr_i},
\qquad U_i=\sum_ju_{ij}^2=\frac{S_i}{n}.
\tag{3.1}
\]

On the core,

\[
\rho:=\max_i|pr_i|
\le p\|r\|_2
=\sqrt{p/n}\,\|Y\|_2
\le C_dp\sqrt{\frac{\log p}{n}},
\tag{3.2}
\]

and

\[
\sum_iU_i
=\frac1n\sum_iS_i
\le C_d\frac{p^2\log p}{n}.
\tag{3.3}
\]

Thus, once `rho<=1/2`,

\[
\boxed{
|E_2(A)|
\le C_d\frac{p^3(\log p)^{3/2}}{\sqrt n}.
}
\tag{3.4}
\]

This is the first decisive gain: the previous `p^(7/2)` bound came from simultaneously saturating the total Frobenius radius and the row-sum norm, while (2.2) shows those are separate Gaussian sectors.

Outside the core but inside Huang's equidistributed ball,

\[
|E_2(A)|\le C_d\rho Q(A),
\qquad
\rho\le C p^{3/2}\sqrt{\log n/n}=o(1)
\tag{3.5}
\]

at the scale used below. Hence the correction cannot destroy the Gaussian tail, and (2.7) remains negligible after inserting `e^{E_2}`.

---

# 4. B29 — integrate the fourth-order Fourier remainder instead of maximizing it

The preceding local logarithmic characteristic-function lemma is

\[
\log\phi(s)
=-\frac d{2p}\|s\|^2
-i\frac{C_{d,p}}{6p}\sum_js_j^3
+R(s),
\]

with

\[
|R(s)|\le C_d\left(p^{-2}\|s\|^4+p^{-1}\sum_js_j^4\right).
\tag{4.1}
\]

For row `i`, the real Gaussian variable after the contour shift has coordinate variance `O_d(p^2/n)` and dimension `p`. Thus

\[
\mathbb E\|s\|^4=O_d(p^6/n^2),
\qquad
\mathbb E\sum_js_j^4=O_d(p^5/n^2).
\tag{4.2}
\]

Since `n_i\asymp n/p`, multiplying (4.2) by the coefficients in `n_i R` gives a **per-row** integrated remainder

\[
O_d(p^3/n),
\]

hence

\[
O_d(p^4/n)
\tag{4.3}
\]

after all `p` rows.

We must also include the imaginary contour shift. In Huang's equidistributed domain the analytic saddle map gives

\[
\|\eta_i\|\le C_dp\|t_i\|,
\qquad
 t_{ij}=q_{ij}-1/p=\frac{u_{ij}}{1+pr_i}.
\tag{4.4}
\]

Writing again `S_i=\sum_jZ_{ij}^2`, the target-only fourth-order terms sum to at most

\[
C_d\left[
\frac p n\sum_iS_i^2+
\frac{p^2}{n}\sum_{i,j}Z_{ij}^4
\right].
\tag{4.5}
\]

On the entire original equidistributed ball,

\[
\sum_iS_i=\|Z\|_F^2=n\|u\|_F^2
\le C p^2\log n.
\tag{4.6}
\]

Therefore, without any typicality assumption,

\[
\sum_iS_i^2\le Cp^4(\log n)^2,
\qquad
\sum_{i,j}Z_{ij}^4\le Cp^4(\log n)^2.
\tag{4.7}
\]

The target part is consequently

\[
O_d\left(\frac{p^5(\log n)^2}{n}
+rac{p^6(\log n)^2}{n}\right).
\tag{4.8}
\]

Mixed real/imaginary quartic terms are bounded by Cauchy--Schwarz and give at most

\[
O_d(p^4\log n/n)+O_d(p^6(\log n)^2/n).
\]

Equivalently, one may restrict each real Fourier integral to

\[
\|s\|^2\le Kp^3\log p/n,
\qquad
\max_j|s_j|^2\le Kp^2\log p/n,
\tag{4.9}
\]

whose Gaussian complement is `e^{-c p\log p}`, apply (4.1) uniformly there, and use Huang's characteristic-function decay outside. Either route yields the aggregate replacement

\[
\boxed{
\varepsilon_4
=O_d\left(
\frac{p^4\log n}{n}+
\frac{p^6(\log n)^2}{n}
\right),
}
\tag{4.10}
\]

instead of the old `O(p^7(log n)^2/n)` bound.

This is the second decisive gain. The old `p^7` came from asking every one of the `p` row Fourier variables to sit simultaneously on the boundary of a ball sized for the worst row.

---

# 5. The cubic correction still averages out at the `1/6` scale

The preceding artifact wrote the leading global cubic correction as

\[
C_0(A)=\lambda T(Z),
\qquad
\lambda=C_{d,p}\frac p{\sqrt n},
\qquad
T(Z)=\sum_{i,j}Z_{ij}^3.
\tag{5.1}
\]

On the symmetric Gaussian lattice/continuum, `T` is odd. The previous cosh argument gave

\[
\frac{\int e^{-Q+C_0}}{\int e^{-Q}}
=1+O_d\left(\frac{p^6(\log n)^3}{n}\right).
\tag{5.2}
\]

The exact row denominators change `C_0` by

\[
O_d\left(\frac{p^{11/2}(\log n)^2}{n}ight).
\tag{5.3}
\]

Both (5.2) and (5.3) are `o(1)` at `p=n^{1/6}` with any fixed logarithmic slack.

For tail domination, (2.5) and `max|u|<=p||A||` give on the original equidistributed ball

\[
|C(A)|\le o(1)Q(A)
\tag{5.4}
\]

at the scale below. Thus the cubic perturbation also cannot amplify the complement of the isotypic core into a main term.

---

# 6. B6 — Gaussian coset deformation removes the pointwise congruence loss

The previous artifact constructed for every required congruence class a symmetric integer correction `Delta` with

\[
\|\Delta\|_F=O_d(p^{3/2}).
\tag{6.1}
\]

The old argument bounded the cross-term in `Q(A+Delta/(dn))` pointwise and thereby paid `p^(7/2)/sqrt(n)`. That is unnecessary for a Gaussian sum.

Work in count coordinates `X=dnA`. By (2.2), the quadratic form in `X` has all eigenvalues between `c_dp^2/n` and `C_dp^2/n` on the symmetric total-sum-zero space.

The exact character identity already established in the preceding artifact is

\[
\mathbf1_{\{\mathcal L(X)=0\}}
=\frac1{|G|}\sum_{\chi\in\widehat G}\chi(\mathcal L(X)),
\qquad |G|=d^{p-1}p^p.
\tag{6.2}
\]

For a nontrivial character, at least one independent count-coordinate frequency is a nonzero multiple of `1/p` (or `1/d`); modulo the dual of the unconstrained symmetric lattice its Euclidean distance is at least `c_d/p`. Poisson summation therefore gives

\[
\left|rac{S_\chi}{S_1}\right|
\le
\exp\left\{C_dp^2\log p-c_d\frac{n}{p^4}\right\}
\tag{6.3}
\]

for the pure Gaussian theta sums. The `Cp^2 log p` term is simply a packing bound for dual-lattice points in dimension `O(p^2)`. Since `log|G|=O(p\log p)`, (6.2)--(6.3) imply

\[
\boxed{
S_{\rm congruent}
=\frac{1+o(1)}{|G|}S_{\rm unconstrained}
}
\tag{6.4}
\]

whenever

\[
\frac{n}{p^4}\gg p^2\log p.
\tag{6.5}
\]

This is much stronger than needed at the `1/6` scale with logarithmic slack.

There is also a direct translate formulation. With

\[
h:=\Delta/(dn),
\]

(6.1) and (2.2) give

\[
\boxed{Q(h)=O_d(p^5/n)=o(1)}
\tag{6.6}
\]

at the same scale. Completing the square shows that the normalized Gaussian on a congruence translate and the normalized Gaussian on the zero congruence lattice differ by an exponential linear tilt whose `L^2` cost is `e^{O(Q(h))}=1+o(1)`. Poisson summation makes this estimate uniform in the center.

This matters because the zero congruence lattice is invariant under `A->-A`. Hence the cubic cancellation of Section 5 holds **discretely** there as well. Translation by `h` changes the cubic exponent by the previously proved amount

\[
O_d(p^{11/2}\log n/n)=o(1),
\tag{6.7}
\]

and changes the normalized variables in Sections 3--4 by

\[
\|\sqrt n\,u(h)\|_F=O_d(p^{5/2}/\sqrt n)=o(1).
\tag{6.8}
\]

The subgaussian linear moment bounds obtained by completing the square in the theta sum imply the same `e^{-c p\log p}` isotypic-core tail uniformly on these translates. Consequently the denominator correction, cubic correction and integrated fourth-order correction each have normalized expectation `1+o(1)` on the **exact** congruence class. The pointwise quadratic cross-term is never paid.

---

# 7. Remaining uniform errors and choice of prime

After Sections 2--6, the equidistributed calculation has the following sufficient errors:

\[
\begin{array}{rcl}
\text{Stirling} &:& O(p^3(\log n)^{3/2}/\sqrt n),\\
\text{row denominator on core} &:& O(p^3(\log p)^{3/2}/\sqrt n),\\
\text{integrated fourth-order rows} &:& O(p^4\log n/n+p^6(\log n)^2/n),\\
\text{contour factor} &:& O(p^3\sqrt{\log n/n}),\\
\text{cubic Gaussian average} &:& O(p^6(\log n)^3/n),\\
\text{congruence theta error} &:& \exp\{Cp^2\log p-cn/p^4\},\\
\text{congruence translate energy} &:& O(p^5/n),\\
\text{congruence cubic distortion} &:& O(p^{11/2}\log n/n),\\
\text{Riemann quadratic distortion} &:& O(p^3\sqrt{\log n/n}+p^4/n),\\
\text{Riemann cubic distortion} &:& O(p^5\log n/n).
\end{array}
\tag{7.1}
\]

Take

\[
x_n:=\frac{n^{1/6}}{(\log n)^2}.
\]

By Bertrand's postulate choose a prime

\[
p_n\in[x_n,2x_n].
\tag{7.2}
\]

For fixed `d`, eventually `p_n>d`, so `p_n` is odd and does not divide `d`. Every entry of (7.1) is `o(1)`. For example,

\[
\frac{p^3(\log n)^{3/2}}{\sqrt n}
=O((\log n)^{-9/2}),
\]

\[
\frac{p^6(\log n)^3}{n}=O((\log n)^{-9}),
\]

and

\[
\frac{n}{p^4}=\Theta(n^{1/3}(\log n)^8)
\gg p^2\log p.
\]

Thus Huang's equidistributed finite-field expectation remains `O_d(1)` for this prime.

---

# 8. Non-equidistributed vectors remain below the new scale

The first, second and fourth non-equidistributed regimes retain Huang's exponentially small estimates. The R7-07 sparse-support theorem from the `1/8` run gives

\[
\Pr(E_{\rm sparse})=O_d(n^{2-d}).
\tag{8.1}
\]

Its required support range is still valid because the relevant cutoff is

\[
O(p^3\log n)
=O\left(n^{1/2}(\log n)^{-5}\right)
=o(n).
\tag{8.2}
\]

Therefore, if `N_ns` is the number of nonzero finite-field kernel vectors outside the sparse event,

\[
\mathbb E N_{ns}=O_d(1).
\tag{8.3}
\]

---

# 9. Metric theorem

## Theorem 9.1

For every fixed integer `d>=3`, if `A_{n,d}` is the adjacency matrix of a uniformly random simple `d`-regular graph, then

\[
\boxed{
\Pr(A_{n,d}\text{ singular over }\mathbb R)
\le O_d(n^{2-d})+n^{-1/6+o(1)}.
}
\tag{9.1}
\]

In particular,

\[
\boxed{
\Pr(A_{n,3}\text{ singular})\le n^{-1/6+o(1)},
\qquad a_3\ge\frac16.
}
\tag{9.2}
\]

### Proof

Choose `p=p_n` from (7.2). Sections 2--7 extend the finite-field equidistributed estimate used in the preceding R7-07 theorem from `p=n^(1/7-o(1))` to `p=n^(1/6-o(1))`; Section 8 preserves the non-equidistributed bound. Hence outside `E_sparse`, the expected number of nonzero `F_p` kernel vectors is `O_d(1)`.

If `A` is singular over `F_p` outside `E_sparse`, its kernel contains at least `p-1` nonzero vectors, so

\[
(p-1)\mathbf1_{\{A\text{ singular over }\mathbb F_p\}\cap E_{sp}^c}
\le N_{ns}.
\]

Taking expectations,

\[
\Pr(A\text{ singular over }\mathbb F_p)
\le O_d(n^{2-d})+O_d(p^{-1}).
\]

An integer matrix singular over `R` has determinant zero and is therefore singular modulo every prime. Thus the same upper bound applies over `R`. Since `p^{-1}=n^{-1/6+o(1)}`, (9.1) follows, and `d=3` gives (9.2). QED.

---

# 10. Scope and noncircularity

This result is a new **restricted quantitative improvement**, not the source solution. Vu's sharp prediction at `d=3` is exponent `1`, not `1/6`, and full closure requires exponent `d-2` for every fixed `d`.

The dependency chain is noncircular:

1. Huang supplies the undirected finite-field decomposition, outer-frequency decay and original non-equidistributed regime bounds.
2. Earlier R7-07 work supplies the field-independent sparse-support sieve and its `O_d(n^{2-d})` event bound.
3. Nguyen--Pan is used only for the one-row `U_{d,p}` cumulant/contour calculation already matched to Huang's row walk; no directed global independence is imported.
4. The preceding R7-07 artifact supplies the symmetric cubic gluing and exact sparse congruence representative.
5. This artifact supplies the new isotypic diagonalization, integrated fourth-order estimate and Gaussian congruence deformation that remove the two `1/7` worst-case losses.

No finite checker was produced because the new claims are analytic asymptotic lemmas with written proofs rather than finite enumeration statements.

---

# 11. Dated source/literature check — 2026-09-18

Primary source: Van Vu, arXiv:2005.02797, Section 5 after Theorem 5.2.  
Huang baseline: arXiv:1807.06465.  
Directed neighboring result: Nguyen--Pan, arXiv:2308.06461, giving a `n^{-1/3+o(1)}` directed-model bound.  
Later fixed-degree spectral work checked: Huang--McKenzie--Yau, arXiv:2412.20263, and Huang--Yau lecture notes arXiv:2602.00975; these concern rigidity/Ramanujan/edge universality, not the exact-zero singularity exponent. A fresh September 2026 directed hard-edge paper, arXiv:2609.05297, is likewise a directed model.

A bounded search on 2026-09-18 did not recover an undirected fixed-degree theorem proving `Pr(A_{n,d} singular)=n^{-d+2+o(1)}`. This is negative evidence only. Worldwide openness and publication novelty remain **UNVERIFIED**.

---

# 12. Next bottleneck

At `1/6`, three genuinely different terms now meet:

\[
p^3/\sqrt n,
\qquad
p^6/n,
\qquad
\text{the first nonvanishing even Edgeworth correction}.
\]

Thus the next run should not repeat B14/B6/B29. The next planned triple is:

* **B5 ADD A PARAMETER AND DIFFERENTIATE:** introduce a cumulant-strength parameter in the row saddle and compute the first signed even correction rather than bounding it absolutely;
* **B12 FIND WHAT IS CONSERVED:** look for a global cancellation identity for the second Edgeworth tensor after symmetric gluing;
* **B24 FIND THE EXTREMAL OBJECT:** identify the `S_p`-isotypic direction maximizing the surviving sixth-order correction and determine whether it is actually realized by a valid symmetric type.

The next metric milestone is `a_3>=1/5`; it is not claimed here.
