# VDH-8.3-DUALITY — giant-scale truncated susceptibility and erasure of unique-largest conditioning

**Status:** R14 theorem-sized self-check / **PARTIAL** source-level progress. This is not an independent audit, not a novelty certificate, and not by itself a repository closure claim.

## 1. Purpose

The previous R14 step isolated the exact conditioning issue. For a deterministic candidate giant vertex set `S`, with `T=V\S`, conditioning a uniform configuration-model pairing on `S` being the unique largest component changes the fresh pairing law on `T` only by

\[
L_1(CM(d|_T))<|S|.
\]

Indeed, writing `G_S` for the event that `S` is the unique largest component,

\[
\mathcal L(X_T\mid G_S)
=
\mathcal L\bigl(CM(d|_T)\mid L_1(CM(d|_T))<|S|\bigr),
\]

and therefore

\[
d_{\rm TV}\!\left(\mathcal L(X_T\mid G_S),CM(d|_T)\right)
=
\mathbb P_{CM(d|_T)}(L_1\ge |S|).
\tag{1.1}
\]

Thus it is enough to prove a very weak subcritical bound: the largest component of a degree sequence with reflected drift `-delta` is `o_p(n delta)` whenever `n delta^3 -> infinity`. No sharp `delta^{-2} log(n delta^3)` theorem is needed for this conditioning step.

The point of this note is that this giant-scale bound follows from an elementary simple-path / truncated-susceptibility argument with **no maximum-degree hypothesis at all**.

---

## 2. Deterministic theorem

Let `d=(d_1,...,d_n)` be a deterministic graphical half-edge sequence with even

\[
\ell=\sum_{i=1}^n d_i,
\]

and let `CM(d)` be the configuration multigraph. Put

\[
\mu=\frac{\ell}{n},
\qquad
\nu=\frac{1}{\ell}\sum_{i=1}^n d_i(d_i-1)=1-\delta,
\qquad 0<\delta\le \frac12.
\tag{2.1}
\]

For a graph `G`, let `B_r(v)` denote the set of vertices at graph distance at most `r` from `v`, and define the truncated susceptibility

\[
\chi_r(G)=\frac1n\sum_{v=1}^n |B_r(v)|.
\tag{2.2}
\]

### Theorem 2.1 (giant-scale subcritical bound)

Fix constants `0<m<=M<infinity`. There is a constant `C=C(M)` such that, for every deterministic degree sequence satisfying

\[
m\le \mu\le M,
\tag{2.3}
\]

and every integer

\[
1\le K\le \frac{\delta\ell}{16},
\tag{2.4}
\]

one has

\[
\boxed{
\mathbb E\chi_K(CM(d))\le 1+\frac{C}{\delta}
}
\tag{2.5}
\]

and

\[
\boxed{
\mathbb P\bigl(L_1(CM(d))\ge K+1\bigr)
\le
\frac{Cn}{\delta(K+1)^2}.
}
\tag{2.6}
\]

Consequently, for any sequence with (2.3), `delta_n -> 0`, and

\[
n\delta_n^3\longrightarrow\infty,
\tag{2.7}
\]

we have

\[
\boxed{
\frac{L_1(CM(d^{(n)}))}{n\delta_n}
\xrightarrow{\mathbb P}0.
}
\tag{2.8}
\]

No bound on `d_max`, no fourth moment, and no Cramer collar is used in this theorem.

### Proof

For `k>=1`, let `P_k(v)` be the number of **half-edge-labelled simple vertex paths** of length `k` starting from `v`. Every vertex at distance exactly `k` from `v` is reached by at least one such path, so deterministically

\[
|B_K(v)|
\le 1+\sum_{k=1}^K P_k(v).
\tag{2.9}
\]

Let `U` be uniform on `[n]`, independent of the random pairing. For distinct vertices

\[
v_0,v_1,\dots,v_k,
\]

the number of choices of half-edges realizing the ordered path is

\[
d_{v_0}d_{v_k}\prod_{j=1}^{k-1}d_{v_j}(d_{v_j}-1).
\tag{2.10}
\]

For any fixed choice of the `k` prescribed disjoint pairs, the probability that a uniform perfect matching contains all of them equals

\[
\frac{1}{(\ell-1)(\ell-3)\cdots(\ell-(2k-1))}.
\tag{2.11}
\]

Therefore, after summing over distinct vertex sequences and then dropping the distinctness restriction (all summands are nonnegative),

\[
\begin{aligned}
\mathbb E P_k(U)
&\le
\frac1n\,
\frac{\ell^2\bigl(\sum_v d_v(d_v-1)\bigr)^{k-1}}
{(\ell-1)(\ell-3)\cdots(\ell-(2k-1))}\\
&=
\mu\,\nu^{k-1}
\prod_{j=1}^k
\left(1-\frac{2j-1}{\ell}\right)^{-1}.
\end{aligned}
\tag{2.12}
\]

Because `K<=delta ell/16<=ell/32`, every factor in (2.12) has `(2j-1)/ell<=1/16`. The elementary inequality

\[
-\log(1-x)\le 2x
\qquad (0\le x\le1/2)
\tag{2.13}
\]

gives

\[
\log\prod_{j=1}^k
\left(1-\frac{2j-1}{\ell}\right)^{-1}
\le
\frac{2}{\ell}\sum_{j=1}^k(2j-1)
=
\frac{2k^2}{\ell}
\le
\frac{\delta k}{8}.
\tag{2.14}
\]

Also

\[
\nu^{k-1}=(1-\delta)^{k-1}
\le e^{-\delta(k-1)}.
\tag{2.15}
\]

Combining (2.12)--(2.15),

\[
\mathbb E P_k(U)
\le
\mu e^{\delta}
\exp\left\{-\frac78\delta k\right\}.
\tag{2.16}
\]

Using (2.9), summing the geometric series, and `mu<=M`,

\[
\begin{aligned}
\mathbb E\chi_K
&=\mathbb E|B_K(U)|\\
&\le
1+Me^{1/2}
\sum_{k\ge1}e^{-7\delta k/8}\\
&\le
1+\frac{8Me^{1/2}}{7\delta}.
\end{aligned}
\tag{2.17}
\]

This proves (2.5), for example with `C=8Me^{1/2}/7` after harmless enlargement.

Now suppose a connected component `C` has at least `K+1` vertices. For every `v in C`, either every vertex of `C` lies within distance `K` of `v`, or there is a geodesic of length at least `K` starting at `v`. In either case

\[
|B_K(v)|\ge K+1.
\tag{2.18}
\]

Hence on `{L_1>=K+1}`,

\[
\chi_K
\ge
\frac{(K+1)^2}{n}.
\tag{2.19}
\]

Markov's inequality and (2.5) give (2.6).

Finally, choose any fixed

\[
0<a<\frac{m}{32}
\]

and put `K=floor(a n delta)`. For large `n`, (2.3) implies

\[
K\le a n\delta\le \frac{\delta\ell}{16},
\]

and `K>=a n delta/2`. Thus

\[
\mathbb P(L_1\ge a n\delta)
\le
\frac{C'}{a^2 n\delta^3}
\longrightarrow0.
\tag{2.20}
\]

The same conclusion for an arbitrary fixed threshold `eta n delta` follows because, if `eta>=a`, the event `{L_1>=eta n delta}` is contained in `{L_1>=a n delta}`, while if `eta<a` we simply rerun the argument with `a` replaced by `eta/2`. Hence (2.8). `square`

---

## 3. Why the argument is useful here

The sharp subcritical results of Coulson--Perarnau require extra hypotheses when one asks for the true extreme scale. In particular, their sharp CM theorem uses a condition of the form `Delta |Q|=o(R)`, which need not hold after giant deletion under only the source's finite-third-moment assumptions. Earlier HARD7-04 work exhibited source-valid residual hubs showing this is a real mismatch.

Theorem 2.1 deliberately asks for much less. It only separates the subcritical remainder from the giant scale. At that scale the elementary path count has enough room: the negative factor `(1-delta)^k` beats the finite-pairing denominator correction for all `k<=c delta ell`, and the condition `n delta^3 -> infinity` is exactly what makes the truncated-susceptibility Markov bound vanish.

This mechanism is elementary and may be folklore; **no novelty claim is made**.

---

## 4. Application to the barely-supercritical complement

Return to the finite-third-moment barely-supercritical source regime

\[
\nu_n=1+\varepsilon_n,
\qquad
\varepsilon_n\downarrow0,
\qquad
n\varepsilon_n^3\to\infty.
\tag{4.1}
\]

Let `C_{1,n}` be the unique giant, let

\[
T_n=V\setminus C_{1,n},
\]

and let `d^{out}_n=d|_{T_n}`. The earlier HARD7-04/R14 chain supplies the following inputs in this exact source regime:

1. giant size
   \[
   |C_{1,n}|=\gamma_* n\varepsilon_n(1+o_p(1))
   \tag{4.2}
   \]
   for a constant `gamma_*>0` determined by the limiting degree law;
2. `|T_n|/n -> 1` and the residual mean degree stays bounded above and below away from zero;
3. reflected residual criticality
   \[
   \delta_n^{out}:=1-\nu_n^{out}
   =\varepsilon_n(1+o_p(1)).
   \tag{4.3}
   \]

Fix a small constant `a>0` below both the admissible constant in Theorem 2.1 and `gamma_*/8`. On the high-probability event where (4.2)--(4.3) hold with fixed-factor errors, define

\[
K_n=\left\lfloor a|T_n|\delta_n^{out}\right\rfloor.
\tag{4.4}
\]

Then

\[
K_n<|C_{1,n}|
\tag{4.5}
\]

for all large `n`, and Theorem 2.1, applied conditionally to the realized residual degree sequence, yields the **uniform** estimate

\[
\boxed{
\mathbb P_{CM(d_n^{out})}
\left(L_1\ge |C_{1,n}|\right)
\le
\frac{C}{n\varepsilon_n^3}+o(1)
=o(1).
}
\tag{4.6}
\]

The `o(1)` here only accounts for the high-probability parameter event; the deterministic conditional bound itself is `O((n epsilon_n^3)^{-1})`.

---

## 5. Literal pairing-law duality after giant deletion

For every deterministic set `S`, the previous R14 exact factorization gives

\[
\mathcal L(X_{V\setminus S}\mid S\text{ is unique largest})
=
\mathcal L\left(
CM(d|_{V\setminus S})
\mid L_1<|S|
\right).
\tag{5.1}
\]

Let `T_n=V\setminus C_{1,n}` retain its labels, and define a comparison graph `\widetilde G_n` as follows:

- first sample `T_n` with its actual marginal law;
- conditional on `T_n`, independently sample a **fresh uniform configuration model** `CM(d|_{T_n})`.

By (5.1), conditional total variation is exactly the fresh-model probability of violating the unique-largest threshold. Therefore (4.6) implies

\[
\boxed{
d_{\rm TV}\left(
\mathcal L(T_n,G_n[T_n]),
\mathcal L(T_n,\widetilde G_n)
\right)
\longrightarrow0.
}
\tag{5.2}
\]

Thus the act of selecting and deleting the unique giant produces **no asymptotically surviving pairing-law tilt** on its complement. The only first-order information left to identify is the random residual degree sequence itself.

Earlier HARD7-04 work already gives, with `xi_n` the excess-branching extinction probability,

\[
\sum_d(1+d)
\left|N_{n,d}^{out}-n_d\xi_n^d\right|
=o_p(n\varepsilon_n),
\tag{5.3}
\]

as well as

\[
\nu_n^{out}=1-\varepsilon_n+o_p(\varepsilon_n).
\tag{5.4}
\]

Equations (5.2)--(5.4) therefore provide a precise **random-degree-sequence discrete duality statement**: after the giant is deleted, the residual graph is asymptotically a fresh subcritical configuration model on its residual degree sequence, and that sequence is the extinction tilt at first order.

This is stronger than merely matching the reflected scalar drift. It still does **not** assert total variation to a single deterministic degree sequence, nor does it replace the independent audits required before repository closure.

---

## 6. Consequence for the existing second-largest proof candidate

HARD7-04 already archived a proof candidate, under the source finite-third-moment regime and the giant-removal collar proved on that track, for

\[
|C_{2,n}|
=(1+o_p(1))
\frac{2R_*}{\varepsilon_n^2}
\log(n\varepsilon_n^3).
\tag{6.1}
\]

The present result removes a distinct graph-law ambiguity left after that calculation: conditioning a candidate component to be the unique giant does not leave a non-negligible Radon--Nikodym tilt on the residual pairing. Therefore a future source-scope audit can treat the remaining graph as a fresh CM on its realized dual degree sequence, up to `o(1)` total variation.

I do **not** promote (6.1) or the full source to PROVED/CLOSED here. The existing lower/upper extreme-component chain and the new conditioning-erasure theorem still require independent proof audits, and the literature/source-scope boundary must be checked independently.

---

## 7. Method accounting

This proof uses the fresh R14 VDH triple recorded in the preceding report.

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT.** The parameter is the graph-distance cutoff `r` in `chi_r`. Its discrete derivative is controlled by the expected number of simple paths of length `r`; the resulting geometric decay is integrated up to the macroscopic cutoff `r=Theta(n delta)`.
- **#11 DUALIZE.** Instead of attacking `L_1` directly, the large-component event is converted into a lower bound on a truncated susceptibility, which is then controlled by first moments of simple paths.
- **#28 REPLACE FOR ALL WITH TYPICAL.** The deterministic theorem is uniform on a coarse parameter class. For the random post-giant degree sequence it is only necessary to enter that class with probability `1-o(1)`; no uniform sharp extreme-value theorem over every possible residual profile is needed.

All three moves materially reduce the source-level obstruction.

---

## 8. Prior-art boundary

Current checks used:

- Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated 4 August 2026, Notes on Section 8.3, which still asks whether the discrete duality principle holds in this finite-third-moment barely-supercritical CM setting;
- van der Hofstad--Janson--Luczak, *Component structure of the configuration model: Barely supercritical case*, RSA 55 (2019), DOI `10.1002/rsa.20837`;
- Coulson--Perarnau, *Largest component of subcritical random graphs with given degree sequence*, EJP 28 (2023), DOI `10.1214/23-EJP921`, arXiv `2111.11780`.

The last paper proves much sharper subcritical upper bounds under additional hypotheses; the present lemma is only a weak giant-scale estimate and should be treated as an elementary/possibly folklore mechanism unless an independent literature audit establishes otherwise.

No 2024--2026 source-matching closure was located in the bounded search performed for this run. That is negative search evidence only, not a worldwide novelty certificate.
