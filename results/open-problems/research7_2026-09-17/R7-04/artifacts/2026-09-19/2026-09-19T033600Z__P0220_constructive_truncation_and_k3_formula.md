Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0220 — constructive Fredholm truncation, positive partition algorithm, and an exact k=3 joint formula

Status: **OPEN / PARTIAL under the campaign closure protocol**. This note strengthens the source-matching stationary-law description but does not claim novelty, source closure, publication priority, or independent audit completion.

## 1. Inherited setup

David Aldous's maintained problem page *A one-dimensional drift-jump particle process* asks for a fairly explicit description of the unique stationary distribution of the consistent finite-k process. The previous R7-04 work established the source-matched representation

\[
(X_1,X_2,\ldots)\overset d=(\tau_1,\tau_2,\ldots),
\qquad
\tau_k:=\inf\{t:\Lambda_1(t)\ge k\},
\tag{1}
\]

where \(\Lambda(t)\) is rate-one poissonized Plancherel growth, together with the explicit extended Schur/discrete-Bessel kernel

\[
K((t,x),(s,y))
=
\frac1{(2\pi i)^2}
\oint\!\oint
\frac{e^{z-t/z-w+s/w}}{z-w}
 z^{-x-1/2}w^{y-1/2}\,dw\,dz,
\tag{2}
\]

with the standard two contour nestings according as \(t\ge s\) or \(t<s\). For

\[
H_k=\{k-\tfrac12,k+\tfrac12,k+\tfrac32,\ldots\},
\]

this gave

\[
\Pr(X_{k_a}>t_a\ \forall a)
=
\det(I-K)_{\bigsqcup_a\{t_a\}\times H_{k_a}},
\tag{3}
\]

defined by finite half-line truncations.

This run uses B8 / B19 / B26 to make (3) quantitatively constructive and to attack the first genuinely nontrivial three-coordinate case independently.

---

## 2. B8 — finite determinant hierarchy with an explicit certified error bound

Fix finitely many constraints \((k_a,t_a)\), merge duplicate times by retaining the smallest \(k\), and omit \(t_a=0\). For an integer \(L\ge\max_a k_a\), define

\[
H_{k}^{(L)}:=\{j-\tfrac12:j=k,k+1,\ldots,L\}
\]

and

\[
A_L:=\bigsqcup_a\{t_a\}\times H_{k_a}^{(L)}.
\]

Let

\[
D_L:=\det(I-K|_{A_L}).
\]

By the finite determinantal gap identity,

\[
D_L
=
\Pr\{\mathcal S(\Lambda(t_a))\cap H_{k_a}^{(L)}=\varnothing\ \forall a\}.
\tag{4}
\]

The events in (4) decrease as \(L\to\infty\), and their intersection is exactly the full event in (3). Hence

\[
D_L\downarrow S:=\Pr(X_{k_a}>t_a\ \forall a).
\tag{5}
\]

The previous note used (5) only as a definition of the Fredholm limit. Here is the quantitative error estimate.

### Theorem 2.1 — Poisson-tail control of the Fredholm truncation

For every \(L\ge\max_a k_a\),

\[
\boxed{
0\le D_L-S
\le
\sum_a \Pr\{\operatorname{Pois}(t_a)\ge L+1\}.
}
\tag{6}
\]

#### Proof

The difference event between the truncated and full gaps requires, for at least one sampled time \(t_a\), a Maya particle in the omitted tail

\[
\{L+\tfrac12,L+\tfrac32,\ldots\}.
\]

If a Maya particle lies at or to the right of \(L+\tfrac12\), then the largest Maya particle satisfies

\[
\Lambda_1(t_a)-\tfrac12\ge L+\tfrac12,
\]

so \(\Lambda_1(t_a)\ge L+1\). Since \(\Lambda_1(t_a)\le |\Lambda(t_a)|\), and the total number of boxes in rate-one poissonized Plancherel growth is exactly \(N(t_a)\sim\operatorname{Pois}(t_a)\), the omitted-tail event is contained in \(\{N(t_a)\ge L+1\}\). A union bound over the finitely many sampled times proves (6). QED.

Thus the full stationary joint law is approximated by an ordinary finite matrix determinant of dimension

\[
\sum_a (L-k_a+1)
\]

with a completely explicit a priori error. For any prescribed \(\varepsilon>0\), it is enough to choose \(L\) so that the right side of (6) is at most \(\varepsilon\). If desired one may use the standard Chernoff bound

\[
\Pr\{\operatorname{Pois}(t)\ge n\}
\le e^{-t}\left(\frac{et}{n}\right)^n,
\qquad n>t,
\tag{7}
\]

to choose such an \(L\) without evaluating an infinite tail.

This makes the Fredholm formula operational rather than merely formal.

---

## 3. B19 — a positive finite partition recursion with a sharper one-tail certificate

The determinant route is not the only constructive algorithm. The exact nested Plancherel formula gives a positive dynamic program that has no oscillatory kernel and whose truncation error is controlled by a single Poisson tail at the largest observation time.

Let

\[
0<t_1<\cdots<t_r=T,
\qquad \Delta_j=t_j-t_{j-1},\quad t_0=0,
\]

and at time \(t_j\) impose the width constraint

\[
\Lambda_1(t_j)<k_j.
\]

For partitions \(\lambda\subseteq\mu\), write \(f^{\mu/\lambda}\) for the number of standard Young tableaux of the skew shape \(\mu/\lambda\). Define positive weights recursively by

\[
A_0(\varnothing)=1,
\]

and for \(j\ge1\),

\[
\boxed{
A_j(\mu)
=
\mathbf 1_{\{\mu_1<k_j\}}
\sum_{\lambda\subseteq\mu}
A_{j-1}(\lambda)
\frac{f^{\mu/\lambda}\Delta_j^{|\mu|-|\lambda|}}
{(|\mu|-|\lambda|)!}.
}
\tag{8}
\]

Then the exact joint survival probability is

\[
\boxed{
S=e^{-T}
\sum_{\mu}
A_r(\mu)\frac{f^\mu}{|\mu|!}.
}
\tag{9}
\]

### Proof

Expanding (8) recursively over nested diagrams

\[
\varnothing=\lambda^{(0)}\subseteq\lambda^{(1)}\subseteq\cdots\subseteq\lambda^{(r)}=\mu
\]

produces exactly the product of skew-tableau factors and interval powers in the already proved finite-dimensional Plancherel weight

\[
e^{-T}\frac{f^{\lambda^{(r)}}}{|\lambda^{(r)}|!}
\prod_{j=1}^r
\frac{f^{\lambda^{(j)}/\lambda^{(j-1)}}\Delta_j^{|\lambda^{(j)}|-|\lambda^{(j-1)}|}}
{(|\lambda^{(j)}|-|\lambda^{(j-1)}|)!}.
\]

The indicators in (8) impose exactly the required first-row constraints at the observation times. Summing gives (9). QED.

For a finite cutoff \(N\), restrict every partition in (8)-(9) to size at most \(N\), and call the result \(S_N\). Because partition size is nondecreasing along Plancherel growth, this removes exactly trajectories with final box count greater than \(N\). Therefore

\[
\boxed{
0\le S-S_N\le \Pr\{\operatorname{Pois}(T)>N\}.
}
\tag{10}
\]

This is sharper than the union bound (6) and turns every finite-threshold stationary probability into a finite positive computation with a certified error.

The skew dimensions in (8) themselves admit a finite determinant formula,

\[
f^{\mu/\lambda}
=d!\det\!\left[
\frac1{(\mu_i-\lambda_j-i+j)!}
\right]_{i,j=1}^{\ell},
\qquad d=|\mu|-|\lambda|,
\tag{11}
\]

with \(1/q!:=0\) for negative integers \(q\), after padding the partitions with zeros. Thus (8)-(10) are an explicit constructive algorithm involving only finite partition enumeration, integer tableau counts, powers of the requested time increments, and one scalar exponential factor.

### Corollary 3.1 — an all-k two-coordinate formula

The hitting-time representation gives a particularly clean family that extends the historical k=2 calculation. For \(k\ge2\), define

\[
D_{k-1}(u):=
\det[I_{i-j}(2\sqrt u)]_{i,j=1}^{k-1}.
\]

Then for \(s,t\ge0\),

\[
\boxed{
\Pr(X_1>s,X_k>t)
=
\begin{cases}
 e^{-s},&s\ge t,\\[3pt]
 e^{-t}D_{k-1}(t-s),&s<t.
\end{cases}}
\tag{12}
\]

Indeed, when \(s<t\), the event \(X_1>s\) means that no Poisson arrival has occurred before \(s\). After time \(s\), the process restarts from the empty diagram with independent increments, and the remaining event is exactly that a fresh Plancherel diagram at time \(t-s\) has first row less than \(k\). The scalar Bessel determinant from the first P0220 run gives (12).

For \(k=2\), (12) is the previously matched historical formula

\[
e^{-t}I_0(2\sqrt{t-s}).
\]

For \(k=3\), it gives

\[
e^{-t}\bigl(I_0(2\sqrt{t-s})^2-I_1(2\sqrt{t-s})^2\bigr).
\]

A related structural consequence of (1) is that \(X_1=\tau_1\), the first Poisson arrival time, is independent of the entire future growth after that first arrival. Hence

\[
\boxed{
X_1\ \perp\ (X_2-X_1,X_3-X_1,\ldots).
}
\tag{13}
\]

The k=2 independence found in the 1993 notes is therefore the first case of an all-coordinate regeneration statement.

---

## 4. B26 — exact three-coordinate survival series and a sporadic-normalization hunt

The first nontrivial ordered joint event is

\[
S_3(s,t,u):=\Pr(X_1>s,X_2>t,X_3>u),
\qquad 0\le s\le t\le u.
\]

Put

\[
a=t-s,\qquad b=u-t.
\]

On \(X_1>s\), the diagram is empty at time \(s\). The constraint \(X_2>t\) forces the diagram at time \(t\) to have first row less than 2, hence it must be a column

\[
\mu=(1^m),\qquad m\ge0.
\]

The constraint \(X_3>u\) forces the final shape to have first row at most 2, so write

\[
\lambda=(2^q,1^r),\qquad q,r\ge0.
\]

Containment \(\mu\subseteq\lambda\) is exactly \(0\le m\le q+r\). Let

\[
n=2q+r,\qquad d=n-m.
\]

The ordinary hook formula gives

\[
\boxed{
f^{(2^q,1^r)}
=
\frac{(2q+r)!(r+1)}{q!(q+r+1)!}.
}
\tag{14}
\]

The required skew-tableau count also has a closed form.

### Lemma 4.1 — two-chain ballot formula

For \(0\le m\le q+r\),

\[
\boxed{
f^{(2^q,1^r)/(1^m)}
=
\binom{2q+r-m}{q}
-
\binom{2q+r-m}{q-m-1},
}
\tag{15}
\]

where the second binomial is zero when its lower index lies outside \([0,2q+r-m]\).

#### Proof

After deleting the first \(m\) cells of the first column, the remaining skew diagram is the union of two vertical chains: the \(q\) cells in column 2 and the \(q+r-m\) remaining cells in column 1. A standard tableau is an interleaving of these two chains. The row constraints say that at every prefix the number of chosen column-2 cells may exceed the number of chosen remaining column-1 cells by at most \(m\). Without the bound there are \(\binom{d}{q}\) interleavings. By the reflection principle, paths that first cross the level \(m+1\) are counted by \(\binom{d}{q-m-1}\). Subtraction gives (15). QED.

Combining the two-time Plancherel weight with (14)-(15) yields a fully positive explicit triple-survival series.

### Theorem 4.2 — exact k=3 joint law

For \(0\le s\le t\le u\),

\[
\boxed{
\begin{aligned}
S_3(s,t,u)
&=e^{-u}
\sum_{q,r\ge0}
\sum_{m=0}^{q+r}
\frac{f^{(2^q,1^r)}}{(2q+r)!}
\frac{a^m}{m!}
\frac{f^{(2^q,1^r)/(1^m)}b^{2q+r-m}}
{(2q+r-m)!}.
\end{aligned}}
\tag{16}
\]

Equivalently, substituting (14)-(15), every coefficient is an explicit rational number times \(e^{-u}\).

#### Proof

Condition on the nested pair of shapes \(\Lambda(t)=\mu=(1^m)\subseteq\Lambda(u)=\lambda=(2^q,1^r)\). The interval \([0,s]\) contributes the no-arrival factor \(e^{-s}\), and the shifted two-time Plancherel formula on intervals of lengths \(a\) and \(b\) contributes

\[
e^{-(u-s)}
\frac{f^\lambda}{|\lambda|!}
\frac{f^\mu a^{|\mu|}}{|\mu|!}
\frac{f^{\lambda/\mu}b^{|\lambda|-|\mu|}}
{(|\lambda|-|\mu|)!}.
\]

Since \(f^{(1^m)}=1\), multiplication by \(e^{-s}\) gives exactly the summand in (16). Summing over all admissible \(q,r,m\) proves the theorem. QED.

### Two exact boundary reductions

1. If \(u=t\), then \(b=0\), forcing \(q=0\) and \(m=r\). Formula (16) reduces to

\[
e^{-t}\sum_{m\ge0}\frac{(t-s)^m}{(m!)^2}
=e^{-t}I_0(2\sqrt{t-s}),
\]

which is exactly the k=2 joint survival law.

2. If \(s=t\), then \(a=0\), forcing \(m=0\). Formula (16) becomes

\[
e^{-u}
\sum_{\lambda:\lambda_1\le2}
\frac{(f^\lambda)^2(u-s)^{|\lambda|}}
{(|\lambda|!)^2}
=
 e^{-u}\bigl[I_0(2\sqrt{u-s})^2-I_1(2\sqrt{u-s})^2\bigr],
\]

which is exactly the k=3 scalar Bessel determinant shifted by the no-arrival interval.

These two independent boundary collapses probe both time directions of the three-coordinate formula and found no sign or normalization defect.

---

## 5. Exact finite validation

The analytic derivation above was written first. Afterward an exact checker was executed using only Python integers, `Fraction`, and exhaustive linear-extension counting for the finite skew shapes.

Checker:

`research7_2026-09-17/R7-04/artifacts/2026-09-19/2026-09-19T033500Z__P0220_k3_exact_check.py`

Creation commit: `3814250929b5832ab32b2290893063b87d8a1156`.

Archived output:

`research7_2026-09-17/R7-04/artifacts/2026-09-19/2026-09-19T033500Z__P0220_k3_exact_check.out`

Creation commit: `5712cc46225f66a74bafe03b51afa7c2538a32c7`.

The checker verifies through total final size 9:

- 30 two-column hook-dimension instances;
- 165 skew-shape counts, comparing exhaustive poset linear extensions with the ballot formula (15);
- 55 bivariate series coefficients in \(a,b\), comparing the closed triple formula with independently brute-counted skew tableaux;
- the full \(b=0\) reduction to the k=2 \(I_0\) series through degree 9;
- the full \(a=0\) reduction to the k=3 \(I_0^2-I_1^2\) determinant series through degree 9.

The archived output ends with

`ALL_EXACT_CHECKS_PASS`.

This is a finite validation of the new closed-form combinatorics, not an independent audit and not a substitute for the proof.

---

## 6. Dated source and prior-art status, 2026-09-19

The maintained Berkeley page was checked again on 2026-09-19 and still states the problem: give a fairly explicit stationary distribution. Current bounded searches using the exact title, `stationary distribution`, `leftmost Hammersley`, `patience sorting`, `Gamma(B(1))`, `Schur process`, and `Fredholm determinant` did not locate a later source-specific published solution.

The main ingredients remain known prior art:

- Aldous--Diaconis: the stationary `Gamma(B(i))` representation and the full k=2 calculation;
- Okounkov--Reshetikhin: Schur-process determinantal correlations;
- Borodin--Olshanski: dynamical Plancherel/discrete-Bessel structure;
- Nica: poissonized Robinson--Schensted as a Schur process/nonintersecting Poisson walkers.

Accordingly, this note claims neither the kernel machinery nor the general integrable-probability framework as new. The source-specific composition and the explicit constructive forms above remain **novelty UNVERIFIED**. A search miss is not an openness or priority certificate.

---

## 7. Frozen metric and remaining obligation

The frozen admission metric is

`K_Bessel := sup{k: a finite Toeplitz/Bessel determinant formula for P(X_k>x), all x>=0, is rigorously derived and source-matched}`.

It was already saturated at infinity before this run and remains

`K_Bessel: infinity -> infinity` (**NO MOVEMENT**).

The mathematics nonetheless strengthened the all-coordinate answer in three ways:

1. the Fredholm law now has a finite-determinant approximation with an explicit Poisson-tail error (6);
2. every finite set of thresholds has a positive partition dynamic program with the sharper single-tail certificate (10);
3. the first genuinely three-coordinate ordered survival law has the explicit positive formula (16), with exact finite checks and correct k=2/k=3 boundary reductions.

The remaining campaign obligations are not another scalar formula. They are source-specific prior-art resolution, an independent P26 full-proof audit, a distinct OTHER-track full-proof audit, and a self-contained source-scope paper package. P0220 therefore remains **OPEN / PARTIAL** under campaign terminology.

Because this is the third consecutive ordinary P0220 run with no movement of the frozen metric after saturation, the next R7-04 iteration on P0220 must be the Section-I **thinking-only stuck diagnosis**. It should not add another constructive formula before diagnosing whether the real remaining block is mathematical, bibliographic, or protocol-level.
