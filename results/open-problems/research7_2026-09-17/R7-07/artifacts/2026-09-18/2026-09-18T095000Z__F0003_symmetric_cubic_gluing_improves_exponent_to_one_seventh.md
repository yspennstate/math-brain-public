Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0003 — symmetric cubic gluing and the cubic random-regular singularity exponent `1/7`

Date: 2026-09-18 UTC.  
Slot: `R7-07`, native ID `6aabe8413f60819197825dd81ca138ae`.  
Target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / *Probability Surveys* 18 (2021), Section 5 immediately after Theorem 5.2.  
Primary undirected input: Jiaoyang Huang, *Invertibility of adjacency matrices for random d-regular graphs*, arXiv:1807.06465v2, Section 4.  
Imported local analytic input: Hoi H. Nguyen and Amanda Pan, *A note on the singularity probability of random directed d-regular graphs*, arXiv:2308.06461 / *European Journal of Combinatorics* (2024), Section 3. The imported calculation is used only for the one-row random walk on `U_{d,p}`, which is exactly the same row random walk appearing in Huang's undirected formula (4.3); no directed independence is imported.

Frozen metric:

\[
a_3:=\sup\{a\ge 0:\Pr(A_{n,3}\text{ singular})\le n^{-a+o(1)}\}.
\]

Metric before this artifact: **`a_3 >= 1/8`**.  
Metric after the theorem below: **`a_3 >= 1/7` — MOVEMENT.**

Methods in this iteration: **B11 DUALIZE / B25 COUNT THE SAME THING TWICE / B18 SAY IT IN ANOTHER LANGUAGE**. The immediately preceding triple was B21/B7/B30.

The source-level conjectural endpoint is still `a_3=1`, and the full source asks for exponent `d-2` for every fixed `d>=3`. This artifact is therefore **PARTIAL**, not source closure.

---

## 1. What was missing after the preceding run

The preceding R7-07 artifact established all of the following.

1. Huang's sparse third non-equidistributed class can be removed by a field-independent support sieve. For every odd prime `p` in the relevant range, the event that this class contains a nonzero finite-field kernel vector has probability
   \[
   O_d(n^{2-d}).
   \]
   The only support-two obstruction is a nonadjacent twin pair; supports from three through a fixed linear fraction are suppressed by the unique-neighbour argument.
2. For a row of Huang's equidistributed formula, the logarithmic characteristic function can retain the explicit cubic term of Nguyen--Pan instead of discarding it. The fourth-order logarithmic remainder is
   \[
   O_d\!\left(p^{-2}\|s\|_2^4+p^{-1}\sum_j s_j^4\right).
   \]
3. The exact congruence correction can be chosen with Frobenius norm `O_d(p^{3/2})`, and the unconstrained symmetric count lattice has covering radius `O(p)`.

The remaining obstruction was global: after applying the one-row cubic saddle estimate, Huang must sum over a **symmetric** edge-count matrix `M=(m_{ij})`. Taking an absolute worst-case bound on every row's cubic correction loses the desired scale. This artifact proves that the global cubic correction is harmless after the rows are glued: under Huang's limiting Gaussian it is an odd cubic polynomial with a very small coefficient, and symmetry cancels its first-order contribution.

---

## 2. Exact variables for the symmetric gluing problem

Fix `d>=3`. Let `p` be an odd prime, `p\nmid d`. For a symmetric equidistributed matrix `M` in Huang's notation define

\[
A_{ij}:=\frac{m_{ij}}{dn}-\frac1{p^2},
\qquad
r_i:=\sum_j A_{ij}=\frac{n_i}{n}-\frac1p.
\]

Thus

\[
\sum_{i,j}A_{ij}=0,
\qquad
\|A\|_F^2\le \mathfrak b\frac{\log n}{n},
\qquad
\|r\|_2^2\le p\|A\|_F^2.
\]

For the `i`-th row random walk, its target empirical distribution is

\[
q_{ij}:=\frac{m_{ij}}{dn_i}.
\]

Introduce

\[
u_{ij}:=pA_{ij}-r_i,
\qquad
U_i:=\sum_j u_{ij}^2.
\]

The central algebraic identity is exact, not asymptotic:

\[
\boxed{
q_{ij}-\frac1p=\frac{u_{ij}}{1+pr_i}.
}
\tag{2.1}
\]

Indeed,

\[
q_{ij}=\frac{p^{-2}+A_{ij}}{p^{-1}+r_i}
       =\frac{p^{-1}+pA_{ij}}{1+pr_i}.
\]

Also

\[
\boxed{
\sum_iU_i=p^2\|A\|_F^2-p\|r\|_2^2.
}
\tag{2.2}
\]

To see (2.2), expand

\[
\sum_{i,j}(pA_{ij}-r_i)^2
=p^2\|A\|_F^2-2p\sum_i r_i\sum_jA_{ij}+p\sum_i r_i^2.
\]

Since `sum_j A_ij=r_i`, this is exactly the displayed expression.

These identities are the B25 step: they perform the row-by-row quadratic count and the global symmetric count in the same variables, before any rowwise error is maximized.

---

## 3. B25 — the quadratic denominator loss is only a `1/7` loss

Nguyen--Pan's one-row contour estimate, applied to the identical `U_{d,p}` random walk with sample size `N=n_i`, has Gaussian exponent

\[
-\frac{d n_i p}{2}\sum_j\left(q_{ij}-\frac1p\right)^2.
\]

Using (2.1) and `n_i=n(p^{-1}+r_i)=n(1+pr_i)/p`, this exponent is **exactly**

\[
-\frac{dn}{2}\frac{U_i}{1+pr_i}.
\tag{3.1}
\]

The leading part is `-(dn/2)U_i`. By (2.2), after multiplying by Huang's Stirling factor (4.4), that leading part gives precisely Huang's final quadratic form

\[
Q(A):=\frac{dnp^2}{4}\|A\|_F^2
      -\frac{(d-1)np}{2}\|r\|_2^2.
\tag{3.2}
\]

The difference between (3.1) and its leading part is

\[
E_2(A):=
\frac{dn}{2}\sum_i U_i\frac{pr_i}{1+pr_i}.
\tag{3.3}
\]

On the equidistributed ball,

\[
\max_i|pr_i|
\le p\|r\|_2
\le \sqrt{\mathfrak b\,p^3\log n/n}=o(1)
\]

for `p=n^{1/7-o(1)}`. Hence `|1+pr_i|>=1/2` for large `n`, and

\[
|E_2(A)|
\le C_dn p\sum_i |r_i|U_i
\le C_dn p\|r\|_2\sum_iU_i.
\]

Now

\[
\|r\|_2\le \sqrt{\mathfrak b p\log n/n},
\qquad
\sum_iU_i\le p^2\|A\|_F^2
\le \mathfrak b\frac{p^2\log n}{n}.
\]

Therefore

\[
\boxed{
|E_2(A)|
\le C_{d,\mathfrak b}
\frac{p^{7/2}(\log n)^{3/2}}{\sqrt n}.
}
\tag{3.4}
\]

Thus the exact row normalization does not force Huang's previous `1/8` restriction. With a polylogarithmic loss from `n^{1/7}`, (3.4) is `o(1)` uniformly throughout the equidistributed domain.

---

## 4. The one-row cubic saddle bound, with aggregate errors tracked

Let

\[
t_{ij}:=q_{ij}-\frac1p.
\]

Nguyen--Pan's Section 3 computation uses the same `U_{d,p}` variable as Huang's row probability. Replacing their global sample size by the present row sample `n_i` gives, after the same contour shift, the positive upper bound

\[
\Pr(S_{n_i}=m_i)
\le \mathcal N_i
\exp\left\{
-\frac{d n_i p}{2}\sum_j t_{ij}^2
+C_{d,p}n_i p^2\sum_jt_{ij}^3
+\varepsilon_i
\right\}
+	ext{outer tail},
\tag{4.1}
\]

where `C_{d,p}=d+O_d(p^{-1})`, `\mathcal N_i` is the same Gaussian normalization used by Huang, and the errors can be aggregated over all rows as follows.

### 4.1 Fourth-order logarithmic remainder

The preceding R7-07 characteristic-function lemma gives

\[
|R(s)|\le C_d\left(p^{-2}\|s\|^4+p^{-1}\sum_js_j^4\right).
\]

Huang restricts the central Fourier region to

\[
\|s\|^2\le C p^4\log n/n.
\]

Since `n_i\asymp n/p`, the fourth-order exponent error in one row is at most

\[
C_d\frac{n}{p^2}
\left(\frac{p^4\log n}{n}\right)^2
=O_d\left(\frac{p^6(\log n)^2}{n}\right).
\]

There are `p` rows, so

\[
\boxed{
\sum_i|\varepsilon_i^{(4)}|
=O_d\left(\frac{p^7(\log n)^2}{n}\right).
}
\tag{4.2}
\]

### 4.2 Contour-shift remainder

In the normalized one-dimensional contour argument, the cubic coefficient is

\[
\sigma_i=O_d\!\left(\sqrt{p/n_i}\right)=O_d(p/\sqrt n),
\]

and the normalized target coordinate is `O_d(\sqrt n\,t_{ij})`. The harmless contour factor is therefore bounded by

\[
\exp\{C_dp|t_{ij}|\}.
\]

Summing over all `p^2` row coordinates gives exponent

\[
C_dp\sum_{i,j}|t_{ij}|
\le C_dp^2\|t\|_F.
\]

By (2.1), for large `n`,

\[
\|t\|_F\le2\|u\|_F
\le2p\|A\|_F
\le C p\sqrt{\log n/n}.
\]

Hence the aggregate contour error is

\[
\boxed{
O_d\left(p^3\sqrt{\log n/n}\right)=o(1)
}
\tag{4.3}
\]

at the `1/7` scale.

The outer-frequency contribution remains exponentially small by Huang's characteristic-function decay: the same cutoff gives `exp(-c p^2\log n)` per relevant row, and Huang's choice of the large cutoff constant absorbs the `exp(O(p^2\log n))` number of symmetric matrices. No directed row independence is used here.

### 4.3 Exact form of the cubic correction

Using (2.1) again,

\[
\begin{aligned}
C_{d,p}n_i p^2\sum_jt_{ij}^3
&=C_{d,p}n p\,
\frac{\sum_j u_{ij}^3}{(1+pr_i)^2}.
\end{aligned}
\]

Thus the global cubic correction is

\[
C(A):=C_{d,p}np
\sum_{i,j}\frac{u_{ij}^3}{(1+pr_i)^2}.
\tag{4.4}
\]

Combining (3.4), (4.2) and (4.3), the only non-uniformly-small new term in the central symmetric `M`-sum is `C(A)` itself.

---

## 5. B18 — translate the global symmetric sum into a Gaussian cubic moment

Discard the denominators in (4.4) momentarily and set

\[
C_0(A):=C_{d,p}np\sum_{i,j}u_{ij}^3.
\]

Let

\[
z_{ij}:=\sqrt n\,u_{ij},
\qquad
T(z):=\sum_{i,j}z_{ij}^3,
\qquad
\lambda:=C_{d,p}\frac{p}{\sqrt n}.
\]

Then

\[
\boxed{C_0(A)=\lambda T(z).}
\tag{5.1}
\]

Consider the centered Gaussian measure on the real vector space of symmetric `A` with total sum zero whose density is proportional to `e^{-Q(A)}`. Huang's diagonalization of `Q` gives

\[
Q(A)\ge \frac{np^2}{4}\|A\|_F^2.
\tag{5.2}
\]

Consequently every linear coordinate of `z=\sqrt n\,(pA-r\mathbf 1^T)` has variance bounded by a constant depending only on `d`. Indeed the linear map `A\mapsto u` has operator norm `O(p)`, while the covariance operator of `A` is `O((np^2)^{-1})` by (5.2).

The equidistributed ball is symmetric under `A\mapsto-A`. Moreover

\[
\|z\|_F^2=n\|u\|_F^2
\le np^2\|A\|_F^2
\le \mathfrak b p^2\log n.
\tag{5.3}
\]

Let

\[
M(z):=\max_{i,j}|z_{ij}|.
\]

Then on this ball

\[
|T(z)|\le M(z)\|z\|_F^2
\le \mathfrak b p^2\log n\,M(z).
\tag{5.4}
\]

Because the domain and Gaussian density are symmetric and `T` is odd,

\[
\int e^{-Q}e^{\lambda T}\mathbf1_E
=\int e^{-Q}\cosh(\lambda T)\mathbf1_E.
\tag{5.5}
\]

Use

\[
0\le\cosh x-1\le\frac{x^2}{2}e^{|x|}.
\]

Set

\[
\theta:=C\frac{p^3\log n}{\sqrt n}.
\]

By (5.4), `|\lambda T|<=\theta M`. Since the `p^2` Gaussian coordinates of `z` each have uniformly bounded variance, a union bound on Gaussian tails gives, for `\theta=o(1)`,

\[
\mathbb E[M^2e^{\theta M}]=O_d(\log p).
\tag{5.6}
\]

Therefore the cubic perturbation of the truncated Gaussian mass is bounded by

\[
\begin{aligned}
\frac{\int_E e^{-Q}(e^{\lambda T}-1)}{\int e^{-Q}}
&\le C\theta^2\,\mathbb E[M^2e^{\theta M}]\\
&=O_d\left(\frac{p^6(\log n)^2\log p}{n}\right).
\end{aligned}
\tag{5.7}
\]

The Gaussian mass outside `E` is `e^{-\Omega(p^2\log n)}` once `\mathfrak b` is chosen as in Huang. Hence (5.7) proves the symmetric cubic-gluing estimate

\[
\boxed{
\int_E e^{-Q(A)+C_0(A)}\,dA
=(1+o(1))\int_Ee^{-Q(A)}\,dA
}
\tag{5.8}
\]

whenever, for example,

\[
\frac{p^6(\log n)^3}{n}=o(1).
\]

The important point is the cancellation in (5.5): a pointwise estimate of `|C_0(A)|` loses the scale, whereas the symmetric Gaussian average kills the first odd term.

---

## 6. Restoring the exact row denominators

Write `C=C_0+D`. On `E` put

\[
\rho:=\max_i|pr_i|
\le C\sqrt{p^3\log n/n}=o(1).
\]

Since

\[
\left|(1+x)^{-2}-1\right|\le C|x|
\quad(|x|\le1/2),
\]

we have

\[
|D(A)|
\le C_dnp\,\rho\sum_{i,j}|u_{ij}|^3.
\]

Using `\sum|u|^3<=\|u\|_2^3` and

\[
\|u\|_2\le p\|A\|_F
\le Cp\sqrt{\log n/n},
\]

we obtain the uniform bound

\[
\boxed{
|D(A)|
\le C_d\frac{p^{11/2}(\log n)^2}{n}=o(1)
}
\tag{6.1}
\]

at `p=n^{1/7-o(1)}`. Therefore (5.8) remains true with `C(A)` in place of `C_0(A)`.

---

## 7. The old congruence and Riemann steps remain valid with the cubic weight

The preceding R7-07 artifact constructed, for every residue class needed to pass from Huang's unconstrained lattice `\widetilde E` to the exact congruence lattice `E`, a symmetric integer correction `\Delta` satisfying

\[
\|\Delta\|_F=O_d(p^{3/2}).
\tag{7.1}
\]

Normalize `h=\Delta/(dn)`. Then

\[
\|h\|_F=O_d(p^{3/2}/n),
\qquad
\|u(h)\|_F=O_d(p^{5/2}/n).
\tag{7.2}
\]

For any vectors `u,v`,

\[
\left|\sum (u+v)^3-\sum u^3\right|
\le3\|u\|_2^2\|v\|_2
  +3\|u\|_2\|v\|_2^2
  +\|v\|_2^3.
\tag{7.3}
\]

Using `\|u\|^2<=Cp^2\log n/n` and (7.2), the leading contribution to the change in the cubic exponent `np\sum u^3` is

\[
O_d\left(
np\frac{p^2\log n}{n}\frac{p^{5/2}}n
\right)
=
\boxed{O_d\left(\frac{p^{11/2}\log n}{n}\right)=o(1).}
\tag{7.4}
\]

The denominator factors in (4.4) have the same stability because `\rho=o(1)`. The preceding artifact already proved that the corresponding change in the quadratic exponent is

\[
O_d\left(
\frac{p^{7/2}\sqrt{\log n}}{\sqrt n}+\frac{p^5}{n}
\right)=o(1).
\tag{7.5}
\]

Thus every congruence coset has the same cubic-weighted Gaussian mass up to `1+o(1)`, so Huang's factor `d^{p-1}p^p` for the exact congruences is unchanged asymptotically.

For the Riemann step, the preceding lattice-covering lemma gives count-coordinate cell radius `O(p)`, hence normalized `A`-radius `O(p/n)` and `u`-radius `O(p^2/n)`. Applying (7.3) gives cubic cell distortion

\[
\boxed{O_d(p^5\log n/n)=o(1).}
\tag{7.6}
\]

The quadratic cell distortion was already shown to be

\[
O_d\left(p^3\sqrt{\log n/n}+p^4/n\right)=o(1).
\]

Therefore Huang's exact lattice-to-Gaussian normalization survives the retained cubic correction.

---

## 8. B11 — exact character dualization of the congruences

This route is not needed for the `1/7` theorem, but it gives an exact dual formulation for pushing farther.

On the unconstrained symmetric lattice, collect Huang's congruences into the finite homomorphism

\[
\mathcal L(M)=
\left(
(\sum_jm_{ij}\bmod d)_i,
(\sum_jjm_{ij}\bmod p)_i
\right).
\]

The row-sum residues have one global dependency, so the image group has size

\[
|G|=d^{p-1}p^p,
\]

which is the same factor appearing in Huang's coset argument. Fourier inversion on this finite group gives the exact identity

\[
\boxed{
\mathbf1_{\{\mathcal L(M)=0\}}
=\frac1{|G|}\sum_{\chi\in\widehat G}\chi(\mathcal L(M)).
}
\tag{8.1}
\]

Thus the constrained Gaussian sum is a finite family of theta transforms. The trivial character is precisely the Gaussian mass evaluated above. A quantitative lower bound on the dual distance of every nontrivial character would give a second way to suppress the congruence error and may remove the `p^{7/2}` deterministic translation loss. No such new dual-distance theorem is asserted here; (8.1) is recorded as the next structural route, not as metric movement beyond `1/7`.

---

## 9. Extended equidistributed estimate at the `1/7` scale

Collect the errors in the equidistributed calculation:

\[
\begin{array}{rcl}
\text{Huang Stirling error} &:& O(p^3(\log n)^{3/2}/\sqrt n),\\
\text{exact quadratic denominator error} &:& O(p^{7/2}(\log n)^{3/2}/\sqrt n),\\
\text{aggregate fourth-order row error} &:& O(p^7(\log n)^2/n),\\
\text{aggregate contour error} &:& O(p^3\sqrt{\log n/n}),\\
\text{cubic Gaussian average error} &:& O(p^6(\log n)^3/n),\\
\text{congruence quadratic distortion} &:& O(p^{7/2}\sqrt{\log n/n}+p^5/n),\\
\text{congruence cubic distortion} &:& O(p^{11/2}\log n/n),\\
\text{Riemann cubic distortion} &:& O(p^5\log n/n).
\end{array}
\tag{9.1}
\]

Take

\[
x_n:=\frac{n^{1/7}}{(\log n)^2}.
\]

By Bertrand's postulate, for all large `n` there is a prime `p_n\in[x_n,2x_n]`. Since `d` is fixed, eventually `p_n>d`, hence `p_n\nmid d`. Every term in (9.1) is `o(1)` for this choice.

Huang's remaining outer-frequency term is exponentially small, and the cubic-weighted lattice sum has the same `1+o(1)` Gaussian normalization by Sections 5--7. Consequently the contribution of the equidistributed nonzero finite-field null vectors is `O_d(1)` for this `p_n` (in fact the same leading normalization as in Huang's odd-prime calculation).

---

## 10. Non-equidistributed classes at `p=n^{1/7-o(1)}`

Nothing new is needed here beyond the source and the preceding R7-07 sieve.

* Huang's first and second non-equidistributed regimes are exponentially small in `p^2\log n` after the number of types is included.
* Huang's fourth regime is
  \[
  \exp\{-c n/p^2+O(p^2\log n)\}=o(n^{-K})
  \]
  for every fixed `K` at `p=n^{1/7-o(1)}`.
* Huang's third, sparse regime was the sole source of the old cubic `1/9` restriction. The preceding R7-07 field-independent support theorem replaces its vector count by the event bound
  \[
  O_d(n^{2-d}).
  \]
  Here its support cutoff is `O(p^3\log n)=n^{3/7+o(1)}=o(n)`, so it remains inside that theorem's range.

Thus if `N_ns(G)` is the number of nonzero finite-field kernel vectors outside the sparse event, then under the uniform simple `d`-regular law

\[
\mathbb E N_{ns}=O_d(1).
\tag{10.1}
\]

The conditioning-on-simplicity step is exactly the one already written in the preceding R7-07 artifact; the simple-configuration probability tends to a positive `d`-dependent constant.

---

## 11. The metric theorem

### Theorem 11.1

For every fixed `d>=3`, let `A_{n,d}` be the adjacency matrix of a uniformly random simple `d`-regular graph. Then

\[
\boxed{
\Pr(A_{n,d}\text{ singular over }\mathbb R)
\le O_d(n^{2-d})+n^{-1/7+o(1)}.
}
\tag{11.1}
\]

In particular, for `d=3`,

\[
\boxed{
\Pr(A_{n,3}\text{ singular})\le n^{-1/7+o(1)},
\qquad a_3\ge\frac17.
}
\tag{11.2}
\]

#### Proof

Choose the odd prime `p=p_n=n^{1/7-o(1)}` from Section 9. Outside the sparse event, if `A_{n,d}` is singular over `\mathbb F_p`, its kernel contains at least `p-1` nonzero vectors, all counted by `N_ns`. Therefore

\[
(p-1)\mathbf1_{\{A\text{ singular over }\mathbb F_p\}\cap E_{sp}^c}
\le N_{ns}.
\]

Taking expectations and using (10.1),

\[
\Pr(A\text{ singular over }\mathbb F_p)
\le\Pr(E_{sp})+\frac{\mathbb EN_{ns}}{p-1}
\le O_d(n^{2-d})+O_d(p^{-1}).
\]

Since `A` has integer entries, singularity over `\mathbb R` means its integer determinant is zero, so it is singular modulo every prime. Hence the same upper bound applies over `\mathbb R`. Finally `p^{-1}=n^{-1/7+o(1)}`. This proves (11.1), and setting `d=3` proves (11.2). QED.

---

## 12. Scope, noncircularity, and what remains

This theorem does **not** prove Vu's sharp exponent. For `d=3`, the source-predicted value is `a_3=1`; the present bound is `a_3>=1/7`. For general fixed `d`, source closure requires `a_d=d-2`, not the universal `1/7` term in (11.1).

The dependency chain is noncircular:

1. Huang supplies the undirected symmetric edge-count formula, outer Fourier decay, non-equidistributed rate estimates, and Gaussian quadratic normalization.
2. The preceding R7-07 support theorem removes Huang's sparse third class without using the present cubic analysis.
3. Nguyen--Pan is used only for the contour computation of the same one-row `U_{d,p}` walk. Their directed global factorization is **not** used.
4. Sections 2--7 of this artifact handle the genuinely new obstruction: gluing those row cubic corrections over Huang's symmetric edge-count matrix.

No finite checker was manufactured because the new claim is an analytic asymptotic theorem, not a finite enumeration claim. The proof is written on the page instead.

---

## 13. Dated literature check — 2026-09-18

The primary Vu source continues to record the sharp fixed-degree exponent question after Huang's quantitative theorem. Huang's 2018/2021 work supplies the undirected polynomial estimate used above. Nguyen--Pan's 2023/2024 paper proves `n^{-1/3+o(1)}` for the **directed** fixed-degree model and explicitly notes that the symmetric case is more complicated. Huang--McKenzie--Yau's later random-regular rigidity/edge-universality work concerns spectral rigidity and edge behavior, not the exact-zero singularity exponent.

A bounded fresh search dated 2026-09-18 did not locate a later theorem proving

\[
\Pr(A_{n,d}\text{ singular})=n^{-d+2+o(1)}
\]

for the undirected simple fixed-`d` regular model. This is negative evidence only. Worldwide openness and publication novelty remain **UNVERIFIED**.

---

## 14. Next mathematical bottleneck

The two largest errors in (9.1) now meet at the `1/7` scale:

* the aggregate fourth-order row remainder `p^7/n`, and
* the absolute estimate of the exact quadratic denominator correction `p^{7/2}/\sqrt n`.

The next attack should not repeat B11/B25/B18. A natural nonrepeating triple is:

* **B14 FIND THE GROUP ACTING:** use the `S_p` representation of the symmetric Gaussian to diagonalize cubic/quartic tensors rather than bound coordinates absolutely;
* **B6 DEFORM TO A SOLVED POINT:** interpolate from the directed factorized Gaussian to the symmetric Gaussian and differentiate the log-normalization in the symmetry-coupling parameter;
* **B29 ADD THE POINTS AT INFINITY:** compactify the normalized error tensors and identify the extremal direction responsible for `p^7/n`.

The immediate metric target is `a_3>=1/6`; this is a milestone only, not a claim already proved.