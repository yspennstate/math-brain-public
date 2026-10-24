# B18 FEI proof integration — transverse near-subcube payment and almost-free elimination

**Run:** `20260921T184125Z-b18-fei-r13`  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of full uniform-cube FEI:** **OPEN / NOT PROVED**  
**Claim level:** universal Boolean local theorems and a new bounded-incidence reduction. No novelty or publication-priority claim.

## 0. Fresh state and non-overlap

This run started from fresh `proofnet24/P03-fei` master and was refreshed again after account02/B17's self-XOR/Hellinger continuation appeared. The compatible inputs used are:

1. account04/B18 `20260921T181405Z-phase-aware-row-stability/REPORT.md`, blob `1fd1a564b387bd27938bc127964f778733d355d6`: exact B12/B13 sign-ledger matching, majority-sign near-subcube stability, channel-stable Palm Hellinger control, off-axis leakage, and the correction that spectral block MI does not control phase entanglement;
2. account02 interactive `20260921T174421Z-centered-critical-budget/REPORT.md`: exact centered restriction budget `D_A`, telescoping, and primitive centered ratio-critical cores;
3. account02/B13 `20260921T180326Z-sign-stability-defect/REPORT.md`, blob `b4812f3ae22e7f98596f4b1abcb284dc2d180457`: the exact four-bank depth-defect identity and dimension-free sign stability;
4. account02/B13 `20260921T165419Z-derivative-block-complementarity/REPORT.md`, blob `23ab0bd6734d3cb9a2f32ced4e54ac7213acf627`: physical/spectral/mixed-axis complementarity;
5. account01/B16 `20260921T182439Z-projective-three-qflip-transport/REPORT.md`, blob `d7b9b808956a62fd2d0b700f718928522beef7d9`: projective three-q-flip payment by bounded original-coordinate incidence;
6. account02/B17 `20260921T184622Z-self-xor-hellinger-difference/REPORT.md`, blob `e1c8e0a427a25e8c67fd576addf164a0fa1d29ca`: the additive character-invariant self-XOR/Hellinger bridge `H(P)<=B(P)` and the warning that destroying the joint difference law loses an unbounded factor;
7. `continuations/2026-09-20-concave-restriction/REPORT.md`, blob `b586723862b68d32dda97e0085b9868023fffa46`: the exact single-coordinate restriction formula and concave cap `Delta_i H <= Psi(j_i)`.

The newest centered-core package says the missing global implication is an existential centered block payment on a primitive core. The preceding B18 report says low-depth derivative rows are close to signed subcubes but left their rare address entropy unpaid. The point here is to use the **physical square geometry of the derivative support** rather than continuity of its spectral law. The result gives a dimension-free transverse payment for the bad coordinate and an almost-free elimination statement. It does not duplicate B16's q-flip transport or B17's self-XOR bridge.

Throughout let

\[
f:\mathbb F_2^n\to\{-1,+1\},
\]

fix a coordinate `i`, and on the remaining `m=n-1` coordinates put

\[
g(y)=\frac{f(0,y)-f(1,y)}2\in\{0,\pm1\},
\qquad
E=\{y:g(y)\ne0\},
\qquad
j=\mu(E)=\operatorname{Inf}_i(f).
\]

Assume `0<j<=1/2`, as on a median-character-folded centered core. For every residual coordinate `k`, put

\[
p_k=\operatorname{Inf}_k(f),\qquad q_k=\min(p_k,1-p_k).
\]

For a subset `C` of the residual cube use the oriented coordinate boundary probability

\[
I_k(C)=\Pr_y[1_C(y)\ne1_C(y+e_k)].
\]

Finally let

\[
\Delta_i H(f)=H(f)-\frac{H(f^{i=0})+H(f^{i=1})}{2}.
\]

The inherited concave restriction theorem gives

\[
\Delta_i H(f)\le \Psi(j),
\]

where

\[
\Psi(t)=h_2(t)+1-h_2\!\left(\frac12+\sqrt{t(1-t)}\right),
\]

and also the useful scalar estimate

\[
\Psi(t)\le h_2(t)+\frac{2t}{\ln2}.
\tag{0.1}
\]

## 1. PROVED: derivative-support boundary forces folded transverse influence

### Theorem B18-TRANSVERSE-BOUNDARY-01

For every residual coordinate `k`,

\[
\boxed{q_k\ge \frac12 I_k(E).}
\tag{1.1}
\]

### Proof

For `b in {0,1}` define the horizontal disagreement bit

\[
d_b(y)=1_{\{f(b,y)\ne f(b,y+e_k)\}},
\]

and the vertical sensitivity bit

\[
e(y)=1_E(y)=1_{\{f(0,y)\ne f(1,y)\}}.
\]

On every Boolean square with vertices `(0,y),(1,y),(0,y+e_k),(1,y+e_k)`, parity of edge disagreements gives the exact identity

\[
d_0(y)\oplus d_1(y)=e(y)\oplus e(y+e_k).
\tag{1.2}
\]

Whenever the derivative support changes across the `k`-edge, exactly one of `d_0,d_1` is one. Thus on that event both the average disagreement and average agreement over the `i`-section equal `1/2`. Averaging over `y`,

\[
p_k\ge\frac12I_k(E),
\qquad
1-p_k\ge\frac12I_k(E).
\]

Taking the smaller side proves (1.1). QED.

This is a genuinely Boolean constraint. It sees information that the squared derivative spectrum alone does not: a sharp physical boundary of the `i`-sensitive fibres must be paid by folded influence in the transverse direction.

## 2. PROVED: near-subcube geometry gives a whole transverse influence bank

Let

\[
Q=\{y_F=a\}
\]

be a coordinate subcube fixing a nonempty set `F` of `r` residual coordinates. Write

\[
q=\mu(Q)=2^{-r},
\qquad
\varepsilon=\mu(E\triangle Q).
\]

For every `k in F`, `I_k(Q)=2q`. Since coordinate boundary probability is `2`-Lipschitz in symmetric-difference measure,

\[
|I_k(E)-I_k(Q)|\le2\varepsilon.
\]

Combining with (1.1) gives

\[
\boxed{q_k\ge q-\varepsilon\qquad(k\in F).}
\tag{2.1}
\]

Suppose now

\[
\varepsilon\le\rho j,
\qquad 0\le\rho\le\frac1{16}.
\tag{2.2}
\]

Because `|q-j|<=varepsilon`,

\[
q\ge j(1-\rho),
\qquad
q\le j(1+\rho).
\]

Let `L=log_2(1/j)>=1`. Since `r=log_2(1/q)`, (2.1) yields

\[
\sum_{k\in F}q_k
\ge r(q-\varepsilon)
\ge j(1-2\rho)\left(L-\log_2(1+\rho)\right).
\tag{2.3}
\]

This estimate has no ambient-dimension factor. The fixed coordinates of the nearby subcube themselves provide the influence bank.

## 3. PROVED: exact-subcube transverse payment, constant 4

If `E=Q` exactly, then `j=q=2^{-r}` and (2.1) gives

\[
\sum_{k\in F}q_k\ge rj.
\tag{3.1}
\]

For `r=1`, `Psi(1/2)=2=4r2^{-r}`. For `r>=2`, use (0.1) and

\[
h_2(2^{-r})
\le 2^{-r}\left(r+\frac1{\ln2}\right)
\]

to obtain

\[
\Psi(2^{-r})
\le2^{-r}\left(r+\frac3{\ln2}\right)
\le4r2^{-r}.
\]

Therefore:

### Theorem B18-EXACT-SUBCUBE-TRANSVERSE-PAYMENT-02

If the `i`-derivative support is exactly a codimension-`r` coordinate subcube fixed on `F`, then

\[
\boxed{
\Delta_i H(f)
\le4\sum_{k\in F}q_k.
}
\tag{3.2}
\]

The significance is that the distinguished coordinate itself can be arbitrarily badly paid by its own influence, but its exact-subcube geometry forces enough **transverse** folded influence to pay its restriction-entropy loss with a universal constant.

This removes the logarithmic local obstruction on the exact-subcube branch without invoking Shannon continuity, spectral block mutual information, or an unsigned positive coupling.

## 4. PROVED: robust near-subcube transverse payment, constant 8

Under (2.2), the concave cap and the elementary entropy bound give

\[
\Delta_iH(f)
\le \Psi(j)
\le j\left(L+\frac3{\ln2}\right).
\tag{4.1}
\]

On the other hand, from (2.3), `1-2rho>=7/8` and

\[
\log_2(1+\rho)\le\log_2(17/16)<1/8.
\]

Also `3/ln2<9/2`. Hence for `L>=1`,

\[
\frac{\Psi(j)}{\sum_{k\in F}q_k}
\le
\frac{L+9/2}{(7/8)(L-1/8)}
<8.
\]

Thus:

### Theorem B18-ROBUST-TRANSVERSE-PAYMENT-03

If a derivative support `E` is within relative error `rho<=1/16` of a coordinate subcube `Q` in the sense `mu(E triangle Q)<=rho j`, then

\[
\boxed{
\Delta_iH(f)
\le8\sum_{k\in F}q_k.
}
\tag{4.2}
\]

Using the centered block decrement from the fresh primitive-core package,

\[
D_F(f)=J(f)-\mathbb E_{z_F}J(f_{z_F})
\ge\sum_{k\in F}q_k,
\]

we get the source-compatible cross-block payment

\[
\boxed{
\Delta_iH(f)\le8D_F(f).
}
\tag{4.3}
\]

For exact support, the coefficient in (4.3) improves from `8` to `4` by (3.2).

**Scope warning.** Equation (4.3) pays the entropy decrement of coordinate `i` by the centered budget of the transverse block `F`; it is not the same-block statement `Delta_F<=C D_F`. Therefore it is not yet the primitive-core closure theorem.

## 5. PROVED: restricting the transverse block almost eliminates the bad coordinate

For each assignment `c in F_2^F`, let

\[
p_c=\operatorname{Inf}_i(f_{y_F=c}).
\]

If `Q={y_F=a}`, then by the definition of symmetric difference,

\[
\varepsilon
=2^{-r}\left((1-p_a)+\sum_{c\ne a}p_c\right).
\tag{5.1}
\]

Since

\[
\min(p_a,1-p_a)\le1-p_a,
\qquad
\min(p_c,1-p_c)\le p_c\quad(c\ne a),
\]

we obtain the exact robust elimination bound

\[
\boxed{
\mathbb E_c\min(p_c,1-p_c)\le\varepsilon.
}
\tag{5.2}
\]

Applying the concave restriction cap inside each child and then Jensen,

\[
\boxed{
\mathbb E_c\Delta_iH(f_{y_F=c})
\le\Psi(\varepsilon)
}
\tag{5.3}
\]

whenever `varepsilon<=1/2`.

At the exact endpoint `varepsilon=0`, every child has `p_c` equal to `0` or `1`. Thus coordinate `i` is either irrelevant or a pure character factor after `F` is exposed. Restricting `i` then changes neither squared Fourier spectrum nor centered influence:

\[
\boxed{
\Delta_{F\cup\{i\}}H=\Delta_FH,
\qquad
D_{F\cup\{i\}}=D_F.
}
\tag{5.4}
\]

This is the promised **free elimination order** for an exact subcube derivative. In the near-subcube regime, (5.2)-(5.3) quantify how close this remains to free.

## 6. Integration with the preceding low-depth row theorem

The preceding B18 report starts from the derivative depth defect

\[
\eta
=\frac{d_g}{j}-\frac12\log_2\frac1j.
\]

In its Ellis-stability regime, for `eta<=1/16` it produces a majority-sign subcube `Q` with

\[
\theta\le2x,
\qquad
\delta<6x,
\qquad
x=\frac{\eta}{\log_2(1/\eta)},
\]

where `theta` is minority-sign mass divided by `j` and `delta=mu(A triangle Q)/mu(A)` for the majority sign class `A`.

Since `E=A disjoint_union B`,

\[
\varepsilon
=\mu(E\triangle Q)
\le\mu(A\triangle Q)+\mu(B)
\le j(\delta+\theta)
<8jx.
\tag{6.1}
\]

In particular, if `eta<=1/32`, then `x<=1/160`, so `rho=varepsilon/j<1/20<1/16`. The robust transverse theorem applies:

### Corollary B18-LOW-DEPTH-TRANSVERSE-04

In the inherited Ellis small-excess regime, every derivative row with `eta<=1/32` admits a coordinate set `F` for which

\[
\boxed{
\Delta_iH(f)\le8\sum_{k\in F}q_k\le8D_F(f),
}
\tag{6.2}
\]

and after exposing `F`,

\[
\boxed{
\mathbb E q_i(f_{y_F})
<8j\frac{\eta}{\log_2(1/\eta)},
}
\tag{6.3}
\]

\[
\boxed{
\mathbb E\Delta_iH(f_{y_F})
\le
\Psi\!\left(8j\frac{\eta}{\log_2(1/\eta)}\right).
}
\tag{6.4}
\]

This is stronger in the relevant direction than the preceding Hellinger statement: it turns near-subcube **physical geometry** into a concrete influence payment and a near-elimination order, without any alphabet-size continuity term.

## 7. PROVED: bounded-incidence aggregation

The local result interfaces exactly with B16's newest bounded-incidence philosophy.

Consider any weighted family of coordinates `i` at the same Boolean state, with weights `lambda_i>=0`. Suppose each chosen `i` is in the robust regime above and is assigned a fixed-coordinate set `F_i`. Define the transverse incidence

\[
L_k=\sum_{i:k\in F_i}\lambda_i,
\qquad
L_*=\max_k L_k.
\]

Then by (4.2),

\[
\sum_i\lambda_i\Delta_iH
\le8\sum_i\lambda_i\sum_{k\in F_i}q_k
=8\sum_k L_kq_k
\le8L_*J(f).
\tag{7.1}
\]

For exact-subcube supports, `8` improves to `4`.

### Corollary B18-TRANSVERSE-INCIDENCE-FRAME-05

A bounded-overlap selector/frame of low-depth derivative rows immediately converts their entire restriction-entropy charge into a universal multiple of centered influence.

This is **CONDITIONAL as a global FEI mechanism** because no theorem here constructs such a bounded-incidence selector through an entire adaptive restriction tree. The point is that the required missing object is now explicit and matches the independently developed projective-q-flip frame condition rather than an unrelated continuity estimate.

## 8. Primitive-core consequence and the exact residual obligation

Let `h` be a primitive centered ratio-critical core from the fresh centered-budget report, with

\[
R=\frac{H(h)}{J(h)}.
\]

For every coordinate `i`, criticality gives

\[
\Delta_iH(h)\ge R D_i(h).
\]

If its derivative row is in the robust near-subcube regime, (4.3) supplies a transverse block `F` such that

\[
R D_i(h)
\le\Delta_iH(h)
\le8D_F(h).
\tag{8.1}
\]

Thus any hypothetical primitive core with `R>8` must exhibit a strict **centered-budget escalation** from that low-depth pivot to its transverse block:

\[
\boxed{D_F(h)>D_i(h).}
\tag{8.2}
\]

At the exact-subcube endpoint the threshold `8` improves to `4`.

This does not yet contradict primitive criticality; a block can have more centered budget than one coordinate. But it sharply narrows the universal gap:

> either build a bounded-incidence / nonreusing escalation rule for these transverse blocks, or show that failure of such a rule forces the large depth / entanglement / mixed-axis / signed banks already isolated by B13 and B16.

That is a smaller and more structural obligation than “control Shannon entropy from near-subcube TV/Hellinger distance.”

The new B17 self-XOR theorem is compatible with this conclusion: it shows a valid FEI-equivalent global bridge must retain the joint difference law, while the present theorem shows that low-depth near-subcube pivots already possess a physical bounded-incidence-style payment before one invokes that joint bank.

## 9. Decisive calculations

The accompanying standard-library checker executed successfully before upload. It verifies the Boolean square lemma and the exact-subcube payment on exhaustive small cases plus deterministic dimension-four samples, and separately stress-tests the abstract near-subcube geometry.

Recorded checks:

- `11,954` folded-influence / derivative-support boundary checks;
- `871` exact-subcube payment cases, with maximum observed `Delta_iH / sum_{k in F} q_k = 4.0`, attained at the one-residual-coordinate endpoint;
- `273,156` near-subcube boundary inequalities;
- `102,756` post-`F` folded residual checks;
- all checks passed.

It also evaluates a hard exact-subcube-support family: take an even-dimensional bent phase `h` on `m` residual variables and flip one point in the other `i`-section. Then `j=2^{-m}` while the distinguished-coordinate local ratio grows:

| `m` | `Delta_iH/j` | `sum_{k in F}q_k` | `Delta_iH / transverse` |
|---:|---:|---:|---:|
| 2 | 4.8676687468 | 0.5 | 2.4338343734 |
| 4 | 8.0300138475 | 1.75 | 0.2867862088 |
| 6 | 10.2559702353 | 2.90625 | 0.0551396249 |
| 8 | 12.3101942894 | 3.96875 | 0.0121163330 |
| 10 | 14.3236208620 | 4.990234375 | 0.0028030569 |
| 12 | 16.3269695795 | 5.9970703125 | 0.0006646706 |

So direct same-coordinate payment can deteriorate rapidly even when the derivative support is an exact point subcube, while the transverse bank becomes more than sufficient. This is precisely the behavior the theorem was designed to capture.

Checker identity: 4,464 bytes, SHA-256 `51ecd92139c900f45d51b31089148a4cc450a3642d1b4bcb32437c7daca133e6`, Git blob `b5417c84bab9bf6f820e19292a46120ef80af4b5`, creation commit `1d27f8d7c4b91a6ab81093d3c158fe601f92f851`.

Verification identity: 1,124 bytes, SHA-256 `b3bdbadc045c3b0d797de9deb0389147cb12b8651432db673d4ffb92c7aef9d9`, Git blob `895315794d7d3b09aca9e0e34ddec3149ac25489`, creation commit `7b7ac947bef996d5eafd93d11d1499add259f94e`.

The finite computations are diagnostics only; Sections 1-8 are analytic.

## 10. Ledger

### PROVED

1. Boolean square parity forces `q_k >= I_k(E)/2` for every transverse coordinate.
2. If `E` is `varepsilon`-close to a coordinate subcube `Q` fixed on `F`, then `q_k>=mu(Q)-varepsilon` for every `k in F`.
3. Exact-subcube derivative support gives the universal transverse restriction-entropy payment
   \[
   \Delta_iH\le4\sum_{k\in F}q_k.
   \]
4. Relative support error at most `1/16` gives the robust payment
   \[
   \Delta_iH\le8\sum_{k\in F}q_k\le8D_F.
   \]
5. Exposing `F` leaves average folded `i`-influence at most `varepsilon` and average remaining `i` entropy decrement at most `Psi(varepsilon)`; at `varepsilon=0`, `i` becomes exactly irrelevant/character and can be removed for free.
6. The inherited low-depth/Ellis branch therefore has a dimension-free transverse payment and near-free elimination, with explicit bounds (6.2)-(6.4).
7. A bounded-incidence family of such pivots is paid by `8 L_* J`, or `4 L_* J` in the exact branch.
8. On a primitive ratio-critical core, every low-depth near-subcube pivot in a putative `R>8` core forces strict centered-budget escalation to its transverse block.

### CONDITIONAL / NOT YET GLOBAL

- Turning the bounded-incidence frame into a nonreusing adaptive restriction strategy remains unproved.
- Equation (4.3) is a cross-block payment, not the same-block primitive-core inequality `Delta_F<=C D_F`.
- The low-depth corollary uses the same absolute Ellis small-excess regime already invoked in the predecessor report; no new threshold is invented.

### REFUTED / PRESERVED ROUTE WARNINGS

- Same-coordinate payment `Delta_iH <= C q_i` is still false in general; the bent-point-flip family above makes the local ratio grow.
- Generic Hellinger/TV plus first moment still does not control Shannon address entropy.
- Spectral block MI plus Boolean convolution still does not imply a near-product signed state.
- Coordinatewise scalarization of B17's self-XOR joint law still loses an unbounded factor on one-point defects.

### OPEN

**Full uniform-cube FEI remains OPEN / NOT PROVED.**

The next integrated target is now concrete: on a primitive centered critical core, construct a nonreusing bounded-incidence selector for the transverse blocks produced by low-depth rows, while routing the complementary large-depth / high-entanglement / mixed-axis / signed cases into the existing B13/B16/B17 joint banks. A proof that those two branches exhaust the core with a universal aggregate payment would close the current centered restriction induction. This report proves the low-depth transverse branch, not that final aggregation theorem.
