# B15 — the one-sided Fourier magnitude gradient is stable under fixed balanced composition

**Status: OPEN / PARTIAL. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval or receiver-context use occurred in this mathematics.  
**Route:** unequal Fourier magnitudes / spectral-lattice arithmetic remainder, continuing the B15 restriction-gradient target and then switching explicitly to APPROACHES route 13 (Booleanity constraints) when the universal selector did not close.  
**Novelty:** no publication-priority claim is made.

## 1. Exact statement attacked

For a coordinate `i`, write, for `T` not containing `i`,

\[
u_T=\widehat f(T),\qquad v_T=\widehat f(T\cup\{i\}),
\]

and retain the preceding B15 one-sided magnitude-gradient cost

\[
L_i(f)=\sum_{T:v_T\ne0}v_T^2\log_2^+\frac{|u_T|}{|v_T|}.
\tag{1}
\]

The preceding run proved

\[
\Delta_iH\le \frac3{\ln2}\operatorname{Inf}_i(f)+2L_i(f).
\tag{2}
\]

Hence the following remains a sufficient universal target:

> **OPEN selector target.** Is there a finite universal `kappa` such that every nonconstant Boolean `f` has a relevant coordinate `i` with
> \[
> L_i(f)\le\kappa\operatorname{Inf}_i(f)?
> \tag{3}
> \]

A positive answer proves full FEI with constant `3/ln 2 + 2 kappa`. The recovered strict lower bound `C_FEI>6.521845710923046575` already forces any proof using only (2)--(3) to have `kappa>1.096880294...`.

The purpose of this run was to attack (3) on the two strongest current obstructions: recursive balanced composition and the rare-tribes family that makes the arithmetic remainder `D` itself unpayable by one coordinate.

## 2. PROVED: exact balanced-composition recursion for `L`

Let `G:{-1,1}^m->{-1,1}` and `H:{-1,1}^n->{-1,1}` be balanced Boolean functions. Put

\[
F=G(H_1,\ldots,H_m),
\]

where the `H_j` are disjoint copies of `H`. Fix a physical coordinate `x` in the `i`th inner block. Define

\[
\alpha_i=\operatorname{Inf}_i(G),\qquad
s_i=|\widehat G(\{i\})|,
\]

\[
p=\operatorname{Inf}_x(H),\qquad
q=|\widehat H(\{x\})|.
\]

For `K subseteq [m]\{i}`, write

\[
a_K=\widehat G(K),\qquad b_K=\widehat G(K\cup\{i\}),
\]

and, for `q>0`, define

\[
M_i(q)=\sum_{K:b_K\ne0}b_K^2
\log_2^+\frac{|a_K|}{|b_K|q}.
\tag{4}
\]

If `q=0`, set the correction below to zero.

### Theorem 2.1

For the leaf `x` in `F`,

\[
\boxed{
\operatorname{Inf}_x(F)=\alpha_i p,
\qquad
|\widehat F(\{x\})|=s_iq,
\qquad
L_x(F)=\alpha_iL_x(H)+q^2M_i(q).
}
\tag{5}
\]

Equivalently, when `p>0`,

\[
\boxed{
\frac{L_x(F)}{\operatorname{Inf}_x(F)}
=
\frac{L_x(H)}p
+
\frac{q^2}{p}\frac{M_i(q)}{\alpha_i}.
}
\tag{6}
\]

### Proof

Balanced disjoint composition has the exact Fourier factorization

\[
\widehat F\!\left(\bigsqcup_{j\in A}S_j\right)
=\widehat G(A)\prod_{j\in A}\widehat H(S_j),
\]

for nonempty inner frequencies `S_j`.

Consider an upper Fourier label containing `x`.

* If its inner label `S_i` contains another variable besides `x`, deleting `x` leaves block `i` active. The same outer coefficient multiplies the upper and lower inner coefficients, so the logarithmic ratio in (1) is exactly the corresponding ratio for `H`. Summing all outer labels containing `i` and all spectra of the other blocks contributes the factor
  \[
  \sum_{A\ni i}\widehat G(A)^2=\alpha_i,
  \]
  giving `alpha_i L_x(H)`.
* If `S_i={x}`, deleting `x` removes block `i` from the active outer set. For a fixed `K` on the other blocks, the lower and upper coefficient magnitudes differ by the factor
  \[
  \frac{|a_K|}{|b_K|q}.
  \]
  The upper squared mass is `q^2b_K^2` times the spectra of the other blocks, whose masses sum to one. Summing gives `q^2 M_i(q)`.

The two cases partition all upper labels containing `x`, proving the third identity in (5). The first is ordinary influence multiplication under balanced block composition, and the second is singleton Fourier factorization. QED.

This recursion is exact and specifically retains the unequal-magnitude term discarded by coarser composition summaries.

## 3. PROVED: no fixed balanced non-dictator seed can make this selector diverge

For a relevant coordinate of a fixed balanced seed, put

\[
\theta_i=\frac{s_i^2}{\alpha_i}.
\]

The current B14 handoff proves `theta_i<=alpha_i<=1`, with equality `theta_i=1` only for a dictator coordinate; therefore a fixed balanced non-dictator has

\[
\theta:=\max_i\theta_i<1.
\tag{7}
\]

Also, from (4), for `0<q<=1`,

\[
M_i(q)
\le
\alpha_i\log_2(1/q)+C_i,
\qquad
C_i:=\sum_{K:b_K\ne0}b_K^2\log_2^+\frac{|a_K|}{|b_K|}<\infty.
\tag{8}
\]

Now recursively self-compose one fixed balanced non-dictator `G`. Along a physical leaf path, after `t` levels,

\[
\frac{q_t^2}{p_t}
=
\prod_{r=1}^t\theta_{i_r}
\le\theta^t.
\tag{9}
\]

If a chosen coordinate has `s_i=0`, then `q` becomes zero and all later singleton corrections vanish. Otherwise, with `s_*>0` the smallest positive singleton magnitude of the fixed finite seed,

\[
\log_2(1/q_t)\le t\log_2(1/s_*).
\tag{10}
\]

Combining (6), (8)--(10), each new correction is bounded uniformly over paths by

\[
O_G((1+t)\theta^t),
\]

whose series converges.

### Corollary 3.1

For every fixed balanced Boolean non-dictator seed `G`, the ratios

\[
L_j(F_r)/\operatorname{Inf}_j(F_r)
\]

are uniformly bounded over all depths `r` and all physical leaves `j` of its recursive self-compositions. The minimum over leaves also converges to a finite limit, because the same summable bound gives a uniform tail estimate and hence a Cauchy bound for the finite-depth minima.

This is a structured theorem, **not** a universal FEI theorem. Its role is negative/diagnostic: fixed-seed recursive amplification, including the strongest current Numaro selector obstruction, cannot by itself refute the finite-`kappa` target (3).

## 4. Decisive stress test: the `D`-selector obstruction collapses for `L`

The concurrent B15 rare-tribes theorem gives a transitive read-once family `T_{m,w}` for which `Delta_i D/Inf_i` is unbounded for every coordinate when `m=2^a+1` and then `a->infinity`. Thus paying the arithmetic remainder `D` by one restriction coordinate is rigorously dead.

For the same family we can compute (1) exactly.

Put

\[
\varepsilon=2^{-w},\qquad q=1-\varepsilon,
\qquad Q=2^w-1,
\qquad c=|2q^m-1|.
\]

For one physical coordinate `i`, the only positive logarithmic ratios occur when the lower frequency contains no other variable from `i`'s block. The empty lower frequency gives the constant-to-one-block jump, while a lower label touching `j>=1` other blocks has exact ratio `Q`. Summing the packet multiplicities gives

\[
\boxed{
L_i(T_{m,w})
=
4\varepsilon^2q^{2m-2}
\left[\log_2\frac{c}{2\varepsilon q^{m-1}}\right]_+
+
4\varepsilon^2q^{m-1}(1-q^{m-1})\log_2Q.
}
\tag{11}
\]

The exact physical influence is

\[
\operatorname{Inf}_i(T_{m,w})=2\varepsilon q^{m-1}.
\tag{12}
\]

Therefore, for every fixed `m`,

\[
\boxed{
\frac{L_i(T_{m,w})}{\operatorname{Inf}_i(T_{m,w})}\longrightarrow0
\qquad(w\to\infty).
}
\tag{13}
\]

This is the opposite behavior of the same family's arithmetic remainder:

\[
\frac{\Delta_iD}{\operatorname{Inf}_i}
\gtrsim2(m-1)\nu_2(m-1).
\]

Thus the one-sided magnitude gradient automatically retains the compensating valuation/mesh cancellation that a `D`-only selector throws away. This is strong evidence that (3) is a materially sharper universal target than separate payment of the arithmetic remainder.

Representative direct evaluations from the companion checker are:

| `m` | `w` | `L_i/Inf_i` | asymptotic `D`-selector obstruction |
|---:|---:|---:|---:|
| 3 | 12 | 0.0053706440 | 4 |
| 5 | 12 | 0.0053705382 | 16 |
| 9 | 12 | 0.0053703262 | 48 |
| 17 | 16 | 0.0004577590 | 128 |
| 65 | 18 | 0.0001296988 | 768 |

The last column is the known limit `2(m-1)nu_2(m-1)` for `m=2^a+1`; the `L` column is a direct floating-point evaluation of the exact formula (11).

## 5. Numaro recursive seed: the hard restriction example remains finite for `L`

The checker independently reconstructs the externally published balanced monotone 18-variable Numaro seed and rejects unless its complete truth table has SHA-256

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

Its two exact influence/singleton classes are the already recovered

\[
\alpha_C=s_C=57/256,\qquad
\alpha_A=s_A=1/256.
\]

At depth one,

\[
L_C/\alpha_C=0.6685747069331263,\qquad
L_A/\alpha_A=2.248037402874644.
\]

Using the exact recursion (6), a two-class dynamic program gives the following **exploratory floating-point** minima over all class paths:

\[
\begin{array}{c|c}
 r & \min L/Inf\\ \hline
1&0.6685747069331263\\
2&1.1866993838214746\\
3&1.3847165247437743\\
4&1.4472095845195638\\
5&1.4652216659044530\\
6&1.4701445271093643\\
7&1.4714437752933338\\
8&1.4717782919398519\\
9&1.4718628451085265\\
10&1.4718768634428125\\
15&1.4718768642634965
\end{array}
\]

The path minimizing through depth nine is all-core; at depth ten an auxiliary excursion becomes microscopically better. These decimal values are not an interval certificate and are not promoted to a theorem. The analytic boundedness/convergence statement of Corollary 3.1 does not depend on them.

This computation is useful because the same fixed seed drives the current potential-free restriction ratio beyond `7.096` and toward about `7.1116`; the more targeted one-sided magnitude-gradient ratio instead remains around `1.472`.

## 6. PROVED bridge to conditional spectral-bit entropy

Put

\[
m_T=u_T^2+v_T^2,
\qquad
q_T=\frac{v_T^2}{m_T}
\]

for nonzero fibres. Let

\[
B_i=\sum_Tm_T h_2(q_T)=H(1_{\{i\in S\}}\mid S\setminus\{i\})
\]

be the binary-fibre/erasure term in the restriction identity.

For `q<=1/2`,

\[
q\log_2\frac{1-q}{q}\le h_2(q),
\]

and for `q>1/2` the positive logarithm vanishes. Since

\[
2v_T^2\log_2^+\frac{|u_T|}{|v_T|}
=m_Tq_T\left[\log_2\frac{1-q_T}{q_T}\right]_+,
\]

we obtain the pointwise and summed bounds

\[
\boxed{2L_i(f)\le B_i.}
\tag{14}
\]

The difference in the `q<=1/2` case is exactly `-log_2(1-q)>=0`. Thus `L_i` is a one-sided subcost of the conditional spectral-membership entropy, not a new independent entropy bill.

This still does **not** prove (3): the current recursive selector work shows that `B_i/Inf_i` itself can exceed four on every coordinate of explicit finite examples.

## 7. Route 5 stalled; switch to APPROACHES route 13

The universal selector (3) did not close from generic probability inequalities. Its exact likelihood form makes clear why.

For `0<alpha_i<1`, define distributions

\[
P_i(T)=\frac{v_T^2}{\alpha_i},
\qquad
Q_i(T)=\frac{u_T^2}{1-\alpha_i}.
\]

Then

\[
\boxed{
\frac{L_i}{\alpha_i}
=
\frac12\,\mathbb E_{P_i}
\left[
\log_2\frac{(1-\alpha_i)Q_i(T)}{\alpha_iP_i(T)}
\right]_+.
}
\tag{15}
\]

For arbitrary probability laws `P_i,Q_i`, the first moment constraint alone permits a logarithmic blowup as `alpha_i->0`; so a purely distributional argument does not supply a dimension-free constant.

This is the point where I switch explicitly to **APPROACHES route 13: Booleanity constraints**. For the two restrictions in coordinate `i`, put pointwise

\[
g=(f_++f_-)/2,\qquad h=(f_+-f_-)/2.
\]

Then `g,h` are ternary, have disjoint physical support, and satisfy

\[
gh=0,\qquad g^2+h^2=1.
\tag{16}
\]

Their Fourier coefficient arrays are exactly `u` and `v`. Hence, under Fourier convolution on the remaining cube,

\[
\boxed{u*v=0,\qquad u*u+v*v=\delta_\varnothing.}
\tag{17}
\]

These algebraic constraints are absent for arbitrary `P,Q`. They are the next usable Boolean input.

A concrete **OPEN** next lemma is therefore:

> Find a universal finite `kappa` such that every Boolean `f` has a coordinate whose pair `(u,v)` satisfying (17) also satisfies the one-sided likelihood bound (15) by `kappa`.

The numerical target `kappa=3/2` is currently attractive but **UNPROVED**: it would imply FEI with constant

\[
3/\ln2+3=7.3280851226\ldots,
\]

is compatible with the known lower bound, survives the exact rare-tribes obstruction above, and survives the present Numaro recursion experiment through depth fifteen. No universality claim is made from those tests.

## 8. Literature/provenance check

A fresh 21 September 2026 primary/current-source check still finds unrestricted FEI open. González--MacManus--Pereyra (arXiv:2606.00246, 29 May 2026) develop the restriction/stopping-tree route and explicitly leave the universal restriction inequality as the missing step. Potapov (arXiv:2609.21563, 18 September 2026) proves FEI for plateaued functions with sharp class constant four and for partially bent functions, not arbitrary unequal-magnitude spectra. The current public optimization record lists the strict lower bound `>6.521845710923046575` from Numaro's 18-variable balanced monotone seed and no finite universal upper bound. No publication-priority claim is made for the lemmas in this report.

## 9. Exact status ledger

**PROVED in this run**

1. Exact balanced-composition recursion (5)--(6) for the one-sided Fourier magnitude gradient.
2. Uniform boundedness and convergence of all `L/Inf` leaf ratios under recursive self-composition of any fixed balanced non-dictator seed.
3. Exact rare-tribes formula (11) and `L_i/Inf_i -> 0` for fixed `m`, despite the same family's divergent `D`-selector obstruction.
4. The pointwise conditional-entropy domination `2L_i<=B_i`.
5. Exact Boolean convolution constraints (17) for the lower/upper Fourier pair of a physical coordinate.

**REFUTED / dead at exact scope**

- Paying `D` alone by an existential coordinate was already refuted by rare tribes and is not revived here.
- A generic likelihood-ratio argument that ignores Boolean convolution constraints cannot by itself control (15) uniformly as influence tends to zero.

**OPEN / CONDITIONAL**

- The finite universal selector (3), including the stronger exploratory target `kappa=3/2`.
- A route-13 theorem extracting a bounded one-sided likelihood coordinate from the Boolean convolution constraints (17).
- Full uniform-cube FEI.

## 10. Reproducibility and next attack

The companion checker reconstructs the external seed only after matching the preserved full-table SHA-256, reproduces its two `L/Inf` coordinate classes, iterates (6) over the two coordinate classes through depth fifteen, and directly evaluates (11) on representative rare-tribes parameters.

Checker SHA-256: `c9b783eedf37734ad2cb3fc9cdf470a11602d163586ab9d8ffa268d23d8a7e38`  
Output SHA-256: `860b9d9e433be29dbee8b2294e61d03d24c5f0b1659db27de3a4638edccc00f1`

**Next attack:** stay on route 13. Use `u*v=0` and `u*u+v*v=delta` before any positive-part or triangle inequality. The first concrete target is a level-set estimate for the likelihood ratio in (15) that gains a Boolean cancellation factor over the generic bound `sum_{|u|>=2^t|v|}v^2 <= 2^{-2t}(1-alpha)`. If that fails on an explicit Boolean family, record the counterexample and move to APPROACHES route 10 with the same signed likelihood quantity smoothed by noise rather than returning to a `D`-only payment.
