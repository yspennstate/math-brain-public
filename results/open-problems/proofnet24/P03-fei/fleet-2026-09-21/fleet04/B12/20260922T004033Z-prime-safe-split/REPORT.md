# B12 — prime safe-split envelope and an all-coordinate local obstruction

**Status:** PARTIAL / STRUCTURAL REDUCTION + RIGOROUS OBSTRUCTION. Full uniform-cube FEI remains **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. This run used authenticated repository sources but no authenticated mathematical/cognitive brain retrieval or receiver-context consumption.

## 0. Live target and what changed

The current owner control supersedes the older row-coding assignment for substantive FEI work and directs every FEI worker to converge on the gate reformulation

\[
\Gamma(p_{\rm out})+H_t(G;p)
\le
\sum_i {\rm It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad
V_p=4p(1-p).
\tag{G}
\]

For a fixed base potential \(\Gamma\), write

\[
D_\Gamma(G;p)
=
\sum_i {\rm It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}}
-H_t(G;p)-\Gamma(p_{\rm out}),
\]

\[
P_G
=
\frac{I(G;p)}4-p_{\rm out}(1-p_{\rm out})\ge0,
\]

and, when \(P_G>0\),

\[
c_G=-\frac{D_\Gamma(G;p)}{P_G}.
\tag{0.1}
\]

The dangerous extremum is the **supremum** of \(c_G\).

Two compatible results are consumed exactly.

1. **Own predecessor:** `fleet04/B12/20260922T003525Z-shannon-margin-conservation`, report blob `7ca2a3c0943c44e80fe0312468964c9ad5eabb65`. For a Shannon split in coordinate \(k\), of bias \(t\), with children \(G_0,G_1\), it proves
   \[
   D_G=(1-t)D_0+tD_1+R_k,
   \tag{0.2}
   \]
   \[
   P_G=(1-t)P_0+tP_1+Q_k,
   \qquad
   Q_k=t(1-t)\bigl[d-(p_1-p_0)^2\bigr]\ge0,
   \tag{0.3}
   \]
   and hence the margin barycenter
   \[
   c_G=
   \frac{(1-t)P_0c_0+tP_1c_1+Q_kc_{R,k}}
   {(1-t)P_0+tP_1+Q_k},
   \qquad
   c_{R,k}:=-R_k/Q_k
   \tag{0.4}
   \]
   whenever the displayed denominators are positive. Every genuine interior split has \(Q_k>0\).

2. **Newest compatible other-account structural result actually used:** `fleet01/B13/20260922T002604Z-gate-composition-prime`, commit `d99ffba1e2cb9dc61f7a6d77f8ba961239694ea3`. It proves the exact gate-slack and \(P\)-currency composition laws and therefore reduces every fixed-potential all-gate problem to **composition-prime** gates. It also descends the certified balanced \(n=18\) counterexample to a composition-prime violating gate of arity at most \(18\), with margin at least
   \[
   0.2681828436921863026325758917943138734666491688421\ldots .
   \tag{0.5}
   \]

I also reread the fresh `fleet02/B13/20260922T001208Z-affine-critical-exchange` theorem. Its exact implication is that a finite-\(C\) FEI counterexample can be chosen simultaneously affine-minimizing, tensor-primitive, and restriction-critical, and that the maximum folded row obeys the all-parity exchange/depth constraints stated there. That theorem remains valid and important for the older A/B interface, but it is a **uniform physical-restriction** theorem, not a biased gate-potential identity. I do not identify its folded block slack with the \(R_k,Q_k\) gate slack below.

The current read-once fixed-point potential itself is already refuted by the certified balanced \(n=18\) gate; this run does not repeat the falsification search. It derives the correct weakened induction condition and then localizes the obstruction to **every root coordinate of one prime gate**.

## 1. Margin-\(c\) slack

Let
\[
\phi(p)=p(1-p).
\]
For any real \(c\), define
\[
S_c(G;p)
:=
D_\Gamma(G;p)+cP_G
=
D_{\Gamma+c\phi}(G;p).
\tag{1.1}
\]

For the split \(k\), (0.2)-(0.3) give the exact recursion

\[
\boxed{
S_c(G)
=
(1-t)S_c(G_0)+tS_c(G_1)+L_{k,c}(G)
}
\tag{1.2}
\]

with the **local corrected residual**

\[
\boxed{
L_{k,c}(G):=R_k+cQ_k.
}
\tag{1.3}
\]

When \(Q_k>0\),

\[
L_{k,c}=Q_k(c-c_{R,k}).
\tag{1.4}
\]

Thus \(L_{k,c}\ge0\) is exactly \(c_{R,k}\le c\).

The already-refuted blind induction demanded \(L_{k,c}\ge0\) for a prescribed/all split independently of child slack. Equation (1.2) shows the weaker condition that actually suffices after lower arities are known: **one safe split is enough**.

## 2. New theorem: prime safe-split induction

For fixed \(\Gamma\), let
\[
C_{\le k}
=
\sup\{c_G(p):
G\text{ has at most }k\text{ essential inputs},\ 
p\in(0,1)^k,\ P_G>0\}.
\tag{2.1}
\]

For a composition-prime gate \(G\) with \(k\ge2\) essential inputs, define

\[
a(G,p)
=
\min_{i\ {\rm essential}} c_{R,i}(G,p),
\tag{2.2}
\]

and

\[
A_k
=
\sup_{\substack{
G\ {\rm composition\!-​prime}\\
G\ {\rm has}\ k\ {\rm essential\ inputs}\\
p\in(0,1)^k
}}
a(G,p).
\tag{2.3}
\]

Boundary points are inherited from lower arity by the fleet01/B13 boundary theorem, so only interior biases matter in \(A_k\).

### Theorem 2.1 — safe-split envelope

For every \(k\ge2\),

\[
\boxed{
C_{\le k}
\le
\max\{C_{\le k-1},A_k\}.
}
\tag{2.4}
\]

Consequently,

\[
\boxed{
C_{\le k}
\le
\max\{C_{\le1},A_2,\ldots,A_k\}.
}
\tag{2.5}
\]

In particular, if a finite \(c\ge0\) satisfies

\[
a(G,p)\le c
\tag{2.6}
\]

for every composition-prime gate of every arity and every interior bias vector, and the unary base is valid, then

\[
D_{\Gamma+c\phi}(G;p)\ge0
\tag{2.7}
\]

for **every** Boolean gate \(G\) and every bias vector. Hence, if \(\Gamma\ge0\) is symmetric with finite \(\Gamma(1/2)\), the gate reformulation yields FEI with constant

\[
\boxed{
C=\Gamma(1/2)+\frac c4.
}
\tag{2.8}
\]

### Proof

Use strong induction on the number of essential inputs.

If \(G\) is functionally decomposable, fleet01/B13 proves that both \(D_\Gamma\) and \(P\) decompose as nonnegative weighted sums of the corresponding lower-arity quantities. Therefore \(c_G\) is a weighted average of lower-arity component margins whenever denominators are positive, and the division-free statement gives the same conclusion at zero-\(P\) components. Thus

\[
c_G\le C_{\le k-1}.
\tag{2.9}
\]

Now suppose \(G\) is composition-prime. Choose an essential coordinate \(i\) attaining the minimum in (2.2). Both restrictions \(G_0,G_1\) have at most \(k-1\) essential inputs. Their margins are at most \(C_{\le k-1}\) by induction. Equation (0.4) writes \(c_G\) as a nonnegative weighted average of the two child margins and \(c_{R,i}\). Therefore

\[
c_G\le
\max\{C_{\le k-1},c_{R,i}\}
\le
\max\{C_{\le k-1},A_k\}.
\tag{2.10}
\]

This proves (2.4), and iteration gives (2.5).

For the division-free sufficient statement, assume all lower-arity gates already satisfy \(S_c\ge0\). If \(G\) is decomposable, the composition law gives \(S_c(G)\ge0\). If \(G\) is prime, (2.6) gives an essential coordinate with \(L_{i,c}\ge0\), and then (1.2) gives

\[
S_c(G)
=
(1-t)S_c(G_0)+tS_c(G_1)+L_{i,c}
\ge0.
\]

This closes the induction. \(\square\)

### What this repairs

The false naive induction tried to control every one-step residual in isolation. Theorem 2.1 requires only

> one coordinate whose residual margin is no worse than the target \(c\),

and only on composition-prime gates. Child slack and functional decomposition are retained exactly rather than discarded.

This is strictly weaker than pointwise control of all \(c_{R,i}\).

## 3. New obstruction theorem: one prime gate is bad in every coordinate

The same theorem gives a converse localization for any fixed threshold.

### Theorem 3.1 — all-coordinate minimal obstruction

Fix \(c\in\mathbb R\). Suppose some Boolean gate satisfies
\[
S_c(G)<0.
\tag{3.1}
\]
Choose such a gate with the minimum number \(r\) of essential inputs.

Then:

1. \(G\) is composition-prime;
2. every proper restriction has nonnegative margin-\(c\) slack;
3. for **every** essential input \(i\),
   \[
   \boxed{
   L_{i,c}(G)<0;
   }
   \tag{3.2}
   \]
4. if \(r\ge2\), then \(Q_i>0\) for every essential \(i\), and hence
   \[
   \boxed{
   c_{R,i}>c
   \quad\text{for every essential }i.
   }
   \tag{3.3}
   \]

### Proof

If \(G\) were decomposable, fleet01/B13's exact composition law would express \(S_c(G)\) as a nonnegative weighted sum of strictly lower-arity component slacks. At least one component would then have negative \(S_c\), contradicting minimality. Thus \(G\) is prime.

Every restriction \(G_b\) has fewer essential inputs, so minimality gives \(S_c(G_b)\ge0\). Applying (1.2) in any essential coordinate,

\[
L_{i,c}(G)
=
S_c(G)-(1-t)S_c(G_0)-tS_c(G_1)
\le S_c(G)<0.
\]

This proves (3.2).

For an interior bias, the predecessor report classifies \(Q_i=0\): either \(G_0=G_1\), contradicting essentiality, or the two children are opposite constants, in which case \(G\) is the split variable up to negation and has only one essential input. Hence \(r\ge2\) implies \(Q_i>0\). Equation (1.4) then gives \(c_{R,i}>c\). \(\square\)

This is stronger than the previous decision-tree statement. That statement said every complete ordering eventually encounters a high residual somewhere. Theorem 3.1 says that after minimal-prime descent there is a **single root gate for which every available first split is already bad**.

## 4. Apply the theorem to the certified \(n=18\) gate

The source-valid balanced \(n=18\) seed has

\[
I=\frac{261}{128},
\quad
H\ge
6.776605309005978082519790221891882314787235038.
\tag{4.1}
\]

For the read-once base potential with
\[
\Gamma(1/2)=C_0=6.4548,
\]
the certified margin lower bound is

\[
c_{18}
\ge
0.2681828436921863026325758917943138734666491688421\ldots.
\tag{4.2}
\]

Choose the exact decimal threshold

\[
c_*:=0.2681828.
\tag{4.3}
\]

Then \(c_*<c_{18}\), so the \(n=18\) seed has \(S_{c_*}<0\). Indeed

\[
P_{18}
=
\frac{I-1}{4}
=
\frac{133}{512},
\tag{4.4}
\]

and the certified entropy endpoint gives

\[
S_{c_*}(G_{18})
\le
-1.1349728082519790\cdot10^{-8}<0.
\tag{4.5}
\]

Apply Theorem 3.1. There exists a composition-prime Boolean gate \(P\) of arity

\[
\boxed{2\le r\le18}
\tag{4.6}
\]

at an interior product-bias vector such that **every essential coordinate** satisfies

\[
\boxed{
c_{R,i}(P)>0.2681828.
}
\tag{4.7}
\]

Equivalently,

\[
\boxed{
A_r>0.2681828
\quad\text{for some }r\le18.
}
\tag{4.8}
\]

The current measured two-input-AND floor is \(0.0043974201\), so

\[
\boxed{
\frac{0.2681828}{0.0043974201}
=
60.9863951820\ldots .
}
\tag{4.9}
\]

Thus a coordinate-selection repair of the old read-once potential cannot evade the high-arity failure by choosing a more favorable first split: after prime/minimal descent, **all** first splits require over \(60.986\) times the old AND margin.

This does not refute the existence of another potential \(\Gamma\). It says the current potential's failure is locally unavoidable at one prime root.

## 5. Relation to the new balanced-excess lower bound

The fresh fleet01/B18 integration proves that full FEI is equivalent to

\[
H(g)\le C[I(g)-1]
\quad\text{for every balanced Boolean }g.
\tag{5.1}
\]

For the same seed,

\[
\frac{H}{I-1}
\ge
6.5218457109230465756581439729485784683666622922105\ldots .
\tag{5.2}
\]

The arithmetic identity

\[
C_0+\frac{c_{18}}4
=
\frac{H}{I-1}
\tag{5.3}
\]

shows that the local margin obstruction and the balanced-excess lower bound are the same deficit in two coordinate systems. No off-center reshaping of the old potential can keep a cap below (5.2), because the obstruction itself is at the all-unbiased point.

Theorem 2.1 therefore suggests a replacement search that is narrower than the original gate sweep:

- search only composition-prime gates;
- for an explicit candidate \(\Gamma\), study the **best available split** \(\min_i c_{R,i}\), not the worst individual split;
- retain lower-arity child slack exactly;
- use the balanced-excess lower bound as a mandatory cap floor.

This is a direct gate-reformulation program, not a return to the older ambient-dimension row code.

## 6. Fleet02 compatibility and preserved mixed-curvature state

The fresh fleet02/B13 result supplies a simultaneous affine-minimum, tensor-primitive, restriction-critical core and exact all-parity/depth constraints. That remains a valid source-exact structural theorem. It does **not** imply (2.6), because its restriction drift uses the folded uniform-cube \(J\) currency whereas (2.6) is a biased gate-Shannon residual statement. The missing bridge is explicit and is not silently assumed.

Likewise, fleet04/B18's mixed-curvature identity

\[
\kappa_{ik}=\kappa_{ki}=p_{ik}+4o_{ik},
\qquad
\sum_{i\ne k}(p_{ik}+4o_{ik})=4d_k
\]

remains true, and \(\sum_k d_k\) is still a second factorial spectral moment rather than an automatic \(O(J)\) budget. Nothing in this report spends that quantity or changes that fact.

## 7. Decisive calculation and finite sanity check

`check_prime_safe_split_threshold.py` is standard-library only.

It reproduces exactly, using `Decimal` arithmetic:

- \(I=261/128\);
- \(P=133/512\);
- the certified \(c_{18}\) interval from the entropy interval;
- \(c_*=0.2681828<c_{18}\);
- the strict negative corrected slack (4.5);
- the factor \(>60.986\) over the current AND floor;
- the cap identity (5.3).

It also checks 596,288 nonnegative-weight synthetic barycenters of the form used in (0.4), verifying that child and residual margins all at most \(c\) cannot produce a parent margin above \(c\). This is only an algebra sanity check; the theorem itself is proved above.

Checker SHA-256:
`88f0682b465320f2dde71db87209b8b276ad02334236480278f06610ce178e00`.

Output SHA-256:
`7d5ac3961c38442fdd7454ed24eef0a76cadfd70db652365655b3ee1608bc54b`.

`py_compile` passed and the native checker exited 0.

## 8. Exact implication left open

The old "AND/decomposable gate is extremal for the read-once \(\Gamma\)" target is refuted.

For a **replacement** finite-cap potential, Theorem 2.1 reduces a sufficient route to the quantitative selector bound

\[
\boxed{
\sup_{k\ge2}
\sup_{\substack{G\ {\rm composition\!-​prime}\\p\in(0,1)^k}}
\min_{i\ {\rm essential}} c_{R,i}(G,p)
<\infty.
}
\tag{8.1}
\]

If the left side is at most \(c\), then \(\Gamma+c\phi\) satisfies every gate and FEI follows with cap \(\Gamma(1/2)+c/4\).

The certified \(n=18\) seed proves that for the **old read-once base potential**, the quantity in (8.1) is already \(>0.2681828\) at some arity at most 18. Therefore the next replacement-potential candidate must genuinely change the potential, not merely reuse the old AND-scale margin or choose a cleverer first coordinate.

Full FEI remains **OPEN / NOT PROVED**.
