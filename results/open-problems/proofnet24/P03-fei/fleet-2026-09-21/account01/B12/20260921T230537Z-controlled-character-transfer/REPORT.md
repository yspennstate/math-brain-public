# B12 FEI compression route — controlled-character spectral projection and exact macro-label transfer

**Status:** **PARTIAL. Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**

**Route:** APPROACH 1, spectral-sample compression / sequential prediction, with a mechanism change from rowwise companion-address charging to a hierarchical branch-label code.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated GitHub control and research artifacts were consumed, but no authenticated native mathematical-brain retrieval/context engine was used.

**Priority:** no novelty or publication-priority claim.

## 0. Fresh compatible inputs actually used

This run used the live joint FEI order and substantively consumed the following completed results.

1. **account03/B12**, `proofnet24/P03-fei/fleet-2026-09-21/account03/B12/20260921T221106Z-component-conditioned-prefix/REPORT.md`, blob `71b06f7a3a5876ef8b0c8ab3561c676b5c95b913`.

   That report gives a genuine Boolean selector-of-parities family for which the stop-conditioned coordinatewise total-correlation remainder is `Theta(m^2)` even though the function itself has spectral entropy exactly two bits. Its exact repair is to expose a terminal component label once and then code conditionally inside the component. The lesson used below is: **a common branch/component variable must be paid once, before coordinatewise tensorization.**

2. **account04/B13**, `proofnet24/P03-fei/fleet-2026-09-21/account04/B13/20260921T2225Z-proxy-gauge-closure/REPORT.md`, blob `1ec1555932e690e403f7d4320640040628697b96`.

   After one nonreusing physical reveal block, that report constructs an explicit branch-dependent character
   \[
   T(z)\subseteq B
   \]
   and Boolean gauged children
   \[
   g_z(y)=\chi_{T(z)}(y)f_z(y)
   \]
   satisfying
   \[
   \mathbb E_z I(g_z)=\sum_r e_r\le \mathcal D(f).
   \]
   It explicitly leaves the Shannon/information cost of the branch character label `T(z)` unpaid.

3. **account01/B13**, `proofnet24/P03-fei/fleet-2026-09-21/account01/B13/20260921T223500Z-label-boundary-curvature/REPORT.md`, blob `7ef3c7b171d03943818ba28cc96f71442b9d30fa`.

   For any deterministic finite-valued label `T(Z)` on a uniform physical cube,
   \[
   H(T)\le I_{\rm phys}(T).
   \]
   In the source-frontier proxy gauge, at relative error `delta=1/16`,
   \[
   H(T)\le {17\over8}J+{15\over14}\mathcal P_{\rm ext}.
   \]
   This converts the macro-label tax into genuine mixed Boolean boundary/curvature, with no ambient alphabet factor.

4. **account04/B12**, `proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260921T220950Z-harmonic-companion-row-code/REPORT.md`.

   Its exact companion normal form reduces the robust rowwise address problem to an off-trigger exception entropy plus the nonrobust companion entropy. The present argument deliberately bypasses that rowwise exception channel: it pays the common branch label first and then works with the gauged residual projection.

The newest account01/B14 adaptive pivotality-selector theorem is compatible with the result below: it reduces full FEI to a bounded corrected-entropy cost for a determining physical tree. The theorem below gives an exact way to separate the branch-character label tax from the residual spectral mixture at each reveal.

## 1. Setup

Split the physical coordinates as a disjoint union
\[
A\sqcup B.
\]
Write a point as `(z,y)`, with `z in {-1,1}^A` and `y in {-1,1}^B`, and let
\[
f:\{-1,1\}^{A\sqcup B}\to\{-1,1\}.
\]
For a revealed value `z`, write
\[
f_z(y)=f(z,y).
\]

Let `Z` be uniform on the `A`-cube. Conditional on `Z=z`, draw a spectral sample
\[
R\subseteq B,\qquad
\Pr(R=R_0\mid Z=z)=\widehat{f_z}(R_0)^2.
\tag{1.1}
\]

Let
\[
T=T(Z)\subseteq B
\tag{1.2}
\]
be **any deterministic branch-dependent character label**. Define
\[
g_z(y)=\chi_{T(z)}(y)f_z(y)
\tag{1.3}
\]
and couple
\[
Y=R\triangle T(Z).
\tag{1.4}
\]

Also define the global Boolean function
\[
g(z,y)=\chi_{T(z)}(y)f(z,y).
\tag{1.5}
\]
No linear change of physical coordinates is being made; `T(z)` only chooses a character on the surviving coordinates after observing the physical branch.

## 2. PROVED: projection/mixing law

### Lemma 2.1 — restriction mixture is exactly spectral projection

Let `S_f` be the spectral sample of the parent `f`. Then
\[
\boxed{\quad
R\ \stackrel d=\ S_f\cap B.
\quad}
\tag{2.1}
\]

Likewise, if `S_g` is the spectral sample of the global Boolean `g`, then
\[
\boxed{\quad
Y\ \stackrel d=\ S_g\cap B.
\quad}
\tag{2.2}
\]

### Proof

For fixed `R_0 subseteq B`, Fourier expansion in the revealed coordinates gives
\[
\widehat f(U\cup R_0)
=
\mathbb E_z\big[\chi_U(z)\widehat{f_z}(R_0)\big].
\]
Parseval on the `A`-cube therefore yields
\[
\sum_{U\subseteq A}\widehat f(U\cup R_0)^2
=
\mathbb E_z\,\widehat{f_z}(R_0)^2.
\tag{2.3}
\]
The left side is exactly
\[
\Pr(S_f\cap B=R_0),
\]
while the right side is the mixture law in (1.1). This proves (2.1).

For every branch `z`, multiplication by the character `chi_{T(z)}` shifts Fourier labels:
\[
\widehat{g_z}(Y_0)
=
\widehat{f_z}(Y_0\triangle T(z)).
\tag{2.4}
\]
Thus the conditional law of `Y` given `Z=z` is the squared Fourier spectrum of `g_z`. Applying (2.3) to the global Boolean `g` proves (2.2). QED.

This identifies the random variables below with **actual projections of Boolean spectra**, not abstract mixture distributions.

## 3. PROVED: exact controlled-character information identity

### Theorem 3.1 — macro-label transfer

Under (1.1)--(1.4),
\[
\boxed{
H(R\mid Z)=H(Y\mid Z),
}
\tag{3.1}
\]
\[
\boxed{
H(R\mid T)=H(Y\mid T),
}
\tag{3.2}
\]
and hence
\[
\boxed{
H(R)-H(Y)
=
I(R;T)-I(Y;T).
}
\tag{3.3}
\]

Equivalently, if
\[
JS_A(f):=I(R;Z),\qquad JS_A(g):=I(Y;Z),
\]
then
\[
\boxed{
JS_A(f)-JS_A(g)
=
I(R;T)-I(Y;T).
}
\tag{3.4}
\]

Moreover the residual mixture information conditional on the branch label is **exactly invariant**:
\[
\boxed{
I(R;Z\mid T)=I(Y;Z\mid T).
}
\tag{3.5}
\]

### Proof

Given `Z=z`, the map
\[
R\longmapsto R\triangle T(z)
\]
is a bijection. Therefore (3.1) holds.

Since `T` is itself a function of `Z`, conditioning only on `T=t` still gives the deterministic bijection
\[
Y=R\triangle t.
\]
Thus the joint laws `(R,T)` and `(Y,T)` are related by a bijective relabeling inside each `T`-fiber, proving (3.2).

Now
\[
I(R;T)-I(Y;T)
=
[H(R)-H(R\mid T)]-[H(Y)-H(Y\mid T)],
\]
and (3.2) gives (3.3).

Similarly,
\[
I(R;Z)-I(Y;Z)
=
[H(R)-H(R\mid Z)]-[H(Y)-H(Y\mid Z)],
\]
so (3.1) and (3.3) imply (3.4).

Finally, because `T` is determined by `Z`,
\[
H(R\mid Z,T)=H(R\mid Z),\qquad
H(Y\mid Z,T)=H(Y\mid Z).
\]
Combine these with (3.1)--(3.2) to obtain (3.5). QED.

### Corollary 3.2 — one macro-label bit is paid only once

Because each mutual information with `T` lies in `[0,H(T)]`,
\[
\boxed{
|H(R)-H(Y)|
=
|JS_A(f)-JS_A(g)|
\le H(T).
}
\tag{3.6}
\]

More strongly, since `R` is determined by `(Y,T)`,
\[
\boxed{
H(R)\le H(T)+H(Y\mid T).
}
\tag{3.7}
\]

Equation (3.7) is the hierarchical compression form: first encode the common branch/component label `T` **once**, then encode the gauged residual spectral projection conditionally inside that label. No coordinatewise repetition of the same common-cause information occurs.

## 4. Exact parent spectral compression inequality

Let
\[
X=S_f,\qquad R=X\cap B.
\]
The revealed spectral coordinates are `X cap A`, so the chain rule gives
\[
H(f)=H(X)
=
H(R)+H(X\cap A\mid R).
\tag{4.1}
\]
The second term is exactly the physical block-erasure Shannon cost
\[
B_A:=H(X_A\mid X_{A^c}).
\]
Combining (4.1) with (3.7) proves

### Corollary 4.1 — controlled-character compression

For every physical reveal block `A` and every deterministic branch character `T(Z) subseteq B`,
\[
\boxed{
H(f)
\le
B_A+H(T)+H(Y\mid T),
}
\tag{4.2}
\]
where `Y` is the survivor projection of the spectrum of the global branch-gauged Boolean `g` in (1.5).

The weaker but sometimes more convenient form is
\[
\boxed{
H(f)\le B_A+H(T)+H(Y).
}
\tag{4.3}
\]

This is an all-dimensional, exact-to-Shannon reduction. It contains no `log n`, Fannes continuity term, or ambient support-size term.

## 5. Source-frontier corollary: the formerly unpaid character label now has a Fourier transfer

Apply Corollary 4.1 to the one-shot source-frontier block and proxy gauge of account04/B13. Its exact theorem gives
\[
\mathbb E_z I(g_z)=\sum_{r\in S} e_r\le\mathcal D(f).
\tag{5.1}
\]
By Lemma 2.1 and the basic identity `Pr(r in spectral sample)=Inf_r`,
\[
\boxed{
\mathbb E|Y|
=
\mathbb E_z I(g_z)
=
\sum_{r\in S}e_r
\le\mathcal D(f).
}
\tag{5.2}
\]

Thus the original survivor spectral projection is encoded by

1. the macro character label `T`, and
2. a **low-mean gauged spectral projection** `Y`.

The account01/B13 physical label theorem now plugs in without any heuristic Fourier continuity step:
\[
H(T)\le I_{\rm phys}(T).
\tag{5.3}
\]
At the current `delta=1/16` source-frontier scale,
\[
\boxed{
H(T)
\le
{17\over8}J(f)
+
{15\over14}\mathcal P_{\rm ext}.
}
\tag{5.4}
\]
Therefore
\[
\boxed{
H(f)
\le
B_A
+
{17\over8}J
+
{15\over14}\mathcal P_{\rm ext}
+
H(Y\mid T).
}
\tag{5.5}
\]

This is the concrete cross-account implication of the present run. The character-label Shannon cost that account04/B13 left unpaid is now transferred into the spectral compression ledger **with coefficient one**.

It also changes the role of the account04/B12 harmonic companion obstruction. One no longer has to pay every off-trigger companion identity rowwise in order to remove common-cause branch entropy. The macro branch label is exposed once, and all subsequent address work is performed on the gauged residual projection.

## 6. Hard-family exactness: addressing and selector-of-parities

The theorem is not merely a loose upper bound on the standard common-cause obstructions.

### Addressing

Let `z in {0,1}^d` select one of `N=2^d` data bits and
\[
f(z,x)=x_z.
\]
Reveal the address block. Every child is the selected character, so the survivor spectral projection is the singleton
\[
R=\{z\},
\]
uniform over `N` possibilities. Hence
\[
H(R)=d.
\]
Choose
\[
T(z)=\{z\}.
\]
Then every gauged child is constant, so
\[
Y=\varnothing,\qquad H(Y\mid T)=0,
\]
while
\[
H(T)=d.
\]
Thus (3.7) is an **equality**:
\[
H(R)=H(T)+H(Y\mid T)=d.
\tag{6.1}
\]
The entire apparent ambient address entropy is exactly a one-time branch label.

### Selector of two parities

For the account03/B12 Boolean selector family, revealing the selector bit leaves one of two parity characters. Choosing `T` to be the selected parity support again makes every gauged child constant. Thus
\[
H(R)=H(T)=1,\qquad H(Y)=0.
\tag{6.2}
\]
This is precisely the hierarchical repair predicted by the account03 counterexample: the branch/component bit is paid once instead of being rediscovered across many prefix indicators.

## 7. Executed finite self-check

A standard-library/exact-Walsh checker in this folder exhaustively enumerates:

- all Boolean truth tables with `( |A|,|B| )=(1,2)`;
- all `2^(|B|)`-valued branch character maps `T(z)`;
- all Boolean truth tables with `( |A|,|B| )=(2,1)`;
- all branch character maps there as well.

Total `(f,T)` cases: **8,192**.

For every case it checks:

1. the parent projection identity (2.1);
2. the global gauged projection identity (2.2);
3. the exact information identity (3.3);
4. the absolute bound (3.6);
5. the hierarchical bound (3.7).

Results:

- projection-law maximum absolute error: `0`;
- gauged-projection maximum absolute error: `0`;
- information-identity maximum floating error: `<1.2e-16`;
- maximum excess in `|H(R)-H(Y)|-H(T)`: `0`;
- hierarchical-bound violations: `0`.

The same checker evaluates addressing for `d=1,...,8` and verifies the exact equality `H(R)=H(T)=d`, `H(Y)=0`.

These computations are diagnostics only; Theorem 3.1 and Corollary 4.1 are analytic.

## 8. What remains open

This does **not** prove FEI. The reduction leaves two honest terms:

1. the reveal conditional spectral entropy
   \[
   B_A=H(X_A\mid X_{A^c}),
   \]
   and
2. the gauged residual projection entropy
   \[
   H(Y\mid T).
   \]

The source-frontier theorem gives only the first moment
\[
\mathbb E|Y|\le\mathcal D(f).
\]
For an arbitrary subset law, small mean does not bound entropy; using that implication here would repeat the already-refuted rare-address shortcut. Although `Y` is an actual projection of a Boolean spectrum, a dimension-free entropy bound for this projected low-mean residual is still a genuine missing Boolean-structural step.

The newest account01/B14 adaptive selector suggests the next nonduplicative move: apply this controlled-character transfer **along a determining tree**. At each reveal, the branch-character label tax can be isolated and paid once by its physical boundary, while the residual mixture stays in the gauged channel. The target is a telescoping inequality in which

- physical label-boundary costs,
- corrected-erasure refunds, and
- the low-mean gauged residual projections

sum to `O(J)` without an ambient-dimension continuity term.

A successful proof of that tree inequality would plug directly into the adaptive compiler. No such universal tree bound is claimed here.

**Full FEI remains OPEN / NOT PROVED.**
