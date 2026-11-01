# H0024 — exact barrier-series comparison and a factor-two improvement

Model actually running: **GPT-5.6 Sol; reasoning level UNVERIFIED**. GPT-6 / maximum reasoning was requested, but authenticated runtime telemetry and binding model/effort selectors are not exposed.

Status: **PARTIAL / OPEN**. This note proves a genuine improvement of the source's critical-line extinction region; it does **not** determine the full critical-line phase diagram.

Target: `H0024`, Oshiro de Carvalho–Machado–Ramírez-González, arXiv:2607.27082v1, Theorem 3.5(ii) / Remark 3.6.

Admission: `research7_2026-09-17/R7-05/admissions/2026-09-17T224725Z__H0024.md`.

Canonical claim: `operations/claims/H0024.md`.

Frozen metric on admission: `G_crit=4`.

## 1. Source normalization and the exact point to attack

At the critical line `beta=1/r`, the source proves

\[
 n\,\mathbb P(D^\to\ge n)\sim \kappa\,\ell(n^r).
\]

Write `m=E[eta_0]`. The source's sufficient conditions are

\[
\liminf \ell(n^r)>\frac1{m\kappa}\quad\Longrightarrow\quad\text{survival},
\]

and

\[
\limsup \ell(n^r)<\frac1{4m\kappa}\quad\Longrightarrow\quad\text{extinction}.
\]

Thus the frozen constant-gap metric is

\[
G_{\rm crit}=\frac{1}{1/4}=4.
\]

The source defines, at each site,

\[
I_x^*:=\max_{1\le i\le \eta_x}D^*_{x,i},
\]

and couples the frog model from above by the bidirectional firework process `BFW(I*)` in which an informed site `x` informs the entire symmetric interval `[x-I_x^*,x+I_x^*]`.

The key observation is that the source's Theorem 3.1(i) uses a coarse sufficient criterion for this upper process. The upper process itself has a sharper barrier-series criterion. Exploiting that criterion removes one of the source's two factors of two.

## 2. B2 — attack the negation: the factor four is not intrinsic

The first obstruction check is to ask whether `1/4` is forced by the source coupling. It is not.

A previous repository memo informally wrote `P(D^*>=n)~2P(D^->=n)`. That is stronger than what the source proves and must not be imported. Source equation (3.1) only gives, by symmetry,

\[
\mathbb P(D^*\ge n)
\le 2\,\mathbb P(D^\to\ge n).
\tag{2.1}
\]

Nothing below needs asymptotic equality.

The useful counter-observation to the apparent `1/4` barrier is that `BFW(I*)` can be analyzed directly. Its extinction threshold for an iid symmetric radius with `1/n` tail coefficient is `1`, rather than the `1/2` constant used inside source Theorem 3.1(i). Hence the source's symmetric-radius domination can already give a factor-two stronger result.

## 3. B11 — dualize to the barrier product

For an iid nonnegative integer radius `I=(I_x)_{x in Z}`, define

\[
q_j:=\mathbb P(I_0>j),\qquad
 a_n:=\prod_{j=0}^{n}(1-q_j)=\prod_{j=0}^{n}\mathbb P(I_0\le j).
\tag{3.1}
\]

For the bidirectional one-radius rumour/firework process on `Z`, the exact barrier criterion is

\[
\mathbb P(\text{infinite informed cluster})=0
\quad\Longleftrightarrow\quad
\sum_{n\ge1}a_n=\infty.
\tag{3.2}
\]

This criterion is Proposition 3.1 of Roy–Saha, *How Fast do Rumours Spread?*, J. Stat. Phys. 191 (2024), 130. Their Section 2 places a `1+epsilon` moment assumption on the surrounding model, but the proof of Proposition 3.1 itself does not use that assumption: it uses only iid radii, the product (3.1), independent layer copies (legitimate because each newly informed vertex broadcasts exactly once), and Borel–Cantelli. Thus the same proof establishes (3.2) for arbitrary iid nonnegative radii, including `1/n` tails. This is a hypothesis audit, not an appeal to a finite-moment statement outside its scope.

For completeness, the part needed here can be summarized as follows. Introduce independent arrays `I_x^(k)` with the same radius law and let a site first informed in generation `k` use `I_x^(k)`. Since each site broadcasts only on its first informed generation, this relabeling has exactly the original process law. The one-generation right- and left-barrier events have probability `a_n`; using a fresh array layer makes the barrier tests independent in the Borel–Cantelli step. Divergence of `sum a_n` therefore produces blocking generations almost surely, while convergence leaves only finitely many such barriers and a positive finite cylinder event reaches beyond all of them. No moment estimate enters this argument.

We only need the extinction half of (3.2).

### Lemma 3.1 (coefficient below one forces barrier-series divergence)

If

\[
\limsup_{j\to\infty} j q_j<1,
\tag{3.3}
\]

then `sum_n a_n=infinity`, hence the bidirectional firework process dies out almost surely.

**Proof.** Choose `theta<1` and `J` so that `q_j<=theta/j` for all `j>=J`. Increase `J` so that `q_j<=1/2`. For `0<=x<=1/2`,

\[
\log(1-x)\ge -x-x^2.
\]

Therefore

\[
\begin{aligned}
\log a_n
&=\sum_{j=0}^{J-1}\log(1-q_j)+\sum_{j=J}^{n}\log(1-q_j)\\
&\ge C_0-\sum_{j=J}^{n}q_j-\sum_{j=J}^{n}q_j^2\\
&\ge C_1-\theta\sum_{j=J}^{n}\frac1j\\
&\ge C_2-\theta\log n.
\end{aligned}
\]

Hence `a_n>=C n^(-theta)` for some `C>0`. Since `theta<1`, `sum a_n` diverges. Apply (3.2). QED.

## 4. Random site maxima

Let

\[
p_n:=\mathbb P(D^*\ge n),\qquad
Q_n:=\mathbb P(I_0^*\ge n).
\]

Conditioning on `eta_0` gives the exact identity

\[
Q_n=\mathbb E\bigl[1-(1-p_n)^{\eta_0}\bigr].
\tag{4.1}
\]

Two consequences are useful.

First, the union bound gives, with no asymptotic assumption,

\[
Q_n\le m p_n.
\tag{4.2}
\]

Second, because `p_n->0` and `E eta_0=m<infinity`, dominated convergence applied to

\[
\frac{1-(1-p)^{k}}p\to k,
\qquad
0\le \frac{1-(1-p)^k}{p}\le k,
\]

shows

\[
Q_n\sim m p_n
\tag{4.3}
\]

whenever an asymptotic for `p_n` itself is available.

## 5. Main theorem: universal factor-two improvement

### Theorem 5.1

Under the hypotheses of source Theorem 3.5 at the critical line `beta=1/r`, if

\[
\boxed{
\limsup_{n\to\infty}\ell(n^r)
<\frac{1}{2\,\mathbb E[\eta_0]\,\kappa},
}
\tag{5.1}
\]

then the interval-activation frog model dies out almost surely.

This improves the source extinction constant from `1/(4m kappa)` to `1/(2m kappa)` in both the stable and finite-variance regimes covered by Theorem 3.5.

**Proof.** Let `m=E[eta_0]`. The source gives

\[
\frac{n\mathbb P(D^\to\ge n)}{\ell(n^r)}\to\kappa.
\tag{5.2}
\]

By source equation (3.1),

\[
\mathbb P(D^*\ge n)\le2\mathbb P(D^\to\ge n).
\tag{5.3}
\]

By (4.2),

\[
\mathbb P(I_0^*\ge n)
\le m\mathbb P(D^*\ge n)
\le 2m\mathbb P(D^\to\ge n).
\tag{5.4}
\]

Combining (5.1), (5.2), and (5.4) yields

\[
\limsup_{n\to\infty}n\,\mathbb P(I_0^*\ge n)<1.
\tag{5.5}
\]

Changing `>=n` to `>j` only shifts the integer index and does not affect the limsup coefficient. Lemma 3.1 therefore says that `BFW(I*)` dies out almost surely.

The source's pathwise coupling places every site activated by the frog model inside the informed set of `BFW(I*)`: every individual frog trajectory is contained in the symmetric interval of radius `D^*`, and `I_x^*` is the maximum of those radii over frogs initially at `x`. Hence extinction of the upper firework process forces extinction of the frog model. QED.

### Metric movement

The survival constant remains `C_surv=1`; Theorem 5.1 raises the full-source extinction constant from `C_ext=1/4` to `C_ext=1/2`. Therefore the frozen metric moves

\[
\boxed{G_{\rm crit}:4\longrightarrow 2.}
\]

This is genuine movement of the same metric, not a redefinition.

The target remains PARTIAL: the interval `1/2 <= z <= 1`, with `z=m kappa ell`, is still unresolved in the constant-limit normalization, and arbitrary oscillatory slowly varying factors remain outside a complete phase diagram.

## 6. Exact series sandwich for arbitrary critical-line oscillation

The constant statement above is only one consequence of a sharper formulation.

Define

\[
I_x^+:=\max_{1\le i\le\eta_x}D^\to_{x,i}
\quad\text{and}\quad
I_x^*:=\max_{1\le i\le\eta_x}D^*_{x,i}.
\]

Let

\[
S(I):=\sum_{n\ge1}\prod_{j=0}^{n}\mathbb P(I_0\le j).
\tag{6.1}
\]

The standard homogeneous one-sided firework theorem (Gallo–Garcia–Vargas Junior–Rodríguez, J. Stat. Phys. 155 (2014), Theorem 1 / equivalent homogeneous firework criterion) gives positive survival of the right-going lower process when `S(I+)<infinity`. The source coupling then implies survival of the frog model.

The bidirectional barrier criterion above gives extinction of the upper process when `S(I*)=infinity`, hence extinction of the frog model.

Therefore, without assuming that `ell(n^r)` converges,

\[
\boxed{
S(I^+)<\infty\quad\Longrightarrow\quad FM\text{ survives with positive probability},
}
\tag{6.2}
\]

and

\[
\boxed{
S(I^*)=\infty\quad\Longrightarrow\quad FM\text{ dies out almost surely}.
}
\tag{6.3}
\]

This isolates the remaining source problem: bridge the gap between the one-sided site reach `I+` and the symmetric upper radius `I*`, or analyze the actual asymmetric left/right interval process directly.

## 7. B5 — parameterize the barrier exponent and resolve its second-order boundary

The product criterion also explains exactly what happens at the coefficient-one boundary.

Suppose an iid radius satisfies, for some real `b` and `delta>0`,

\[
q_n:=\mathbb P(I_0>n)
=\frac1n+\frac{b}{n\log n}
+O\!\left(\frac1{n(\log n)^{1+\delta}}+\frac1{n^2}\right).
\tag{7.1}
\]

Then `sum q_n^2<infinity`, and

\[
\log a_n
=\sum_{j\le n}\log(1-q_j)
=-\sum_{j\le n}q_j+O(1).
\]

Using

\[
\sum_{j\le n}\frac1j=\log n+O(1),
\qquad
\sum_{j\le n}\frac1{j\log j}=\log\log n+O(1),
\]

we obtain

\[
\boxed{
a_n\asymp \frac{1}{n(\log n)^b}.
}
\tag{7.2}
\]

Consequently the exact bidirectional firework criterion yields extinction for `b<=1` and positive percolation for `b>1`.

Thus first-order information `n q_n->1` is intrinsically insufficient at equality. Any future source-level theorem that claims to settle the equality boundary using only the first-order coefficient must supply additional structure from the frog-model reach law.

## 8. A stronger restricted theorem in the Brownian finite-variance regime

The universal factor-two theorem deliberately uses only source inequality (3.1). In the finite-variance regime one can do better because the limiting one-sided and two-sided Brownian passage transforms are explicit.

Let

\[
\tau_+ := \inf\{t\ge0:\sigma B_t\ge1\},
\qquad
\tau_* := \inf\{t\ge0:|\sigma B_t|\ge1\}.
\]

Their Laplace transforms are

\[
\mathbb E e^{-s\tau_+}=e^{-a\sqrt{s}},
\qquad
\mathbb E e^{-s\tau_*}=\operatorname{sech}(a\sqrt{s}),
\qquad a=\frac{\sqrt2}{\sigma}.
\tag{8.1}
\]

At `beta=1/2`, the edge-mixture calculation in source Proposition 3.4 weights the limiting passage transform by `s^{-1/2}ds`. For `D*`, use the exit time `tau_n^*=inf{k:|S_k|>=n}`. Donsker convergence gives `tau_n^*/n^2 => tau_*`. The domination needed in the source integral proof is inherited from

\[
u^{\tau_n^*}=u^{\min(\tau_n^+,\tau_n^-)}
\le u^{\tau_n^+}+u^{\tau_n^-},\qquad 0<u<1,
\]

and symmetry, so every small-time / away-from-one bound used for the one-sided integral remains valid up to a factor two. Hence the same proof gives a two-sided asymptotic constant whose ratio to the source one-sided constant is

\[
\begin{aligned}
R_B
&=\frac{\int_0^\infty s^{-1/2}\operatorname{sech}(a\sqrt{s})\,ds}
{\int_0^\infty s^{-1/2}e^{-a\sqrt{s}}\,ds}\\
&=\frac{2\int_0^\infty \operatorname{sech}(at)\,dt}
{2\int_0^\infty e^{-at}\,dt}\\
&=\frac{\pi/a}{2/a}
=\boxed{\frac\pi2}.
\end{aligned}
\tag{8.2}
\]

Therefore in the finite-variance critical case,

\[
\mathbb P(D^*\ge n)
\sim \frac\pi2\,\mathbb P(D^\to\ge n)
\quad\text{at the source's mixed critical scale},
\tag{8.3}
\]

and, using (4.3), the exact upper-radius coefficient is `(pi/2)m kappa ell(n^2)`. The barrier criterion yields the stronger restricted extinction condition

\[
\boxed{
\limsup_{n\to\infty}\ell(n^2)
<\frac{2}{\pi\,m\kappa}
\quad\Longrightarrow\quad\text{extinction a.s.}
}
\tag{8.4}
\]

Since `2/pi > 1/2`, this is strictly stronger than Theorem 5.1 in the finite-variance branch.

This calculation also shows why the old repository phrase `P(D*)~2P(D^->)` must not be reused: in the Brownian critical mixture the ratio is `pi/2`, not `2`.

Equation (8.4) is a restricted theorem and does not move the frozen **full-source** metric below `2`, because the frozen metric ranges over both the stable and finite-variance source regimes.

## 9. What failed and what remains

1. **False shortcut rejected.** The old memo's unproved claim that the actual asymmetric two-sided interval process has threshold `1` is not used.
2. **False asymptotic rejected.** Source symmetry provides only `P(D*)<=2P(D^->)`, not general asymptotic equality.
3. **Upper-process ceiling.** The universal argument still loses up to a factor two by replacing the actual left/right explored interval with a symmetric radius `D*`. Closing the remaining gap requires the actual asymmetric interval process, not another sharpening of the same union bound.
4. **Equality boundary.** Even an exact `1/n` coefficient equal to one does not decide a firework process without second-order information; (7.2) makes this obstruction explicit.

## 10. Next attack

The next research triple must differ from B2/B11/B5. Use:

- **B1 — change mathematical category:** recast the actual frog closure as an oriented random interval graph with dependent left/right marks, avoiding the symmetric `D*` envelope.
- **B12 — conserved quantity / martingale search:** seek a scale function of the two moving frontiers whose drift has sign exactly at normalized coefficient `1`.
- **B25 — double-count / bijection:** encode finite extinction clusters by their minimal closed intervals and construct an injection or renewal decomposition that counts mutual left/right revivals without replacing them by `D*`.

The immediate mathematical objective is to prove extinction for normalized critical coefficient `<1` in the actual asymmetric interval process, or else produce a rigorous obstruction showing why mutual revivals can shift that threshold.