# B15 — exact real-restriction erasure KL packets and dyadic non-saturation

**Run:** `20260921T232637Z-b15-fei-d-r11`  
**Directive:** `FEI-PROOF-EXECUTION-20260921T230620Z`, Campaign B  
**Assignment:** account03/B15 — prove a conditional packet decomposition only if it plugs into the common Shannon estimate; keep physical-lattice hypotheses.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Outcome classification:** **AUXILIARY_ONLY**.  
**Full unrestricted FEI:** **OPEN / NOT PROVED**.

## 0. What was attempted and what changed

The preceding B15 line repeatedly reduced FEI to positive bounds on the real-restriction softmax current `mathcal W`. That line is no longer a viable universal closure: the newest completed `account02/B15` reset artifact proves an explicit 48-variable Boolean counterexample to the proposed `mathcal W/T_2` dichotomy and proves that a useful Shannon refund cannot disappear at sublinear scale under tensor powers.

I therefore changed methods completely and returned to the common direct-Shannon candidate already proved in `solo-2026-09-17/ERASURE_REDUCTION.md`:

\[
L(f)\le B(f)\le L(f)+\frac1{\ln2}I(f),
\tag{0.1}
\]

where

\[
L(f)=\sum_S p_S\sum_{i\in S}\log_2\!\left(1+\frac{p_{S-i}}{p_S}\right),
\qquad p_S=\widehat f(S)^2,
\tag{0.2}
\]

and a dimension-free `B<=K I` would imply full FEI with constant `K+2/ln2`.

The precise attempt this run was:

> expose the **actual negative information credit** inside (0.2), condition it on genuine Fourier-magnitude packets from a real coordinate restriction, and ask whether Boolean/dyadic lattice structure forces enough credit to pay the raw rare-coordinate address entropy.

The run proves the exact credit decomposition and a strict physical-lattice non-saturation theorem. It does **not** prove the quantitative aggregate credit lower bound needed for FEI.

## 1. Named completed peer results actually consumed

### 1.1 account02/B15 — tensor saturation obstruction

Consumed:

`proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260921T230326Z-radius1-tensor-saturation-counterexample/REPORT.md`.

That report proves, among other things, that the refunded radius-one residual `T_2` tensorizes toward the full entropy ratio and therefore any new information credit intended to improve the common Shannon estimate must retain **linear tensor-scale mass** on hard base functions. It also refutes the previous `mathcal W<=3J/4 or T_2<=4J` dichotomy by a genuine 48-variable Boolean function.

I apply that criterion below: the new negative KL credit is exactly additive under disjoint Boolean products, so it does not disappear under tensor powers.

### 1.2 account01/B12 — conditional Shannon code with a negative KL rebate

Also consumed:

`proofnet24/P03-fei/fleet-2026-09-21/account01/B12/20260921T231256Z-conditional-count-code/REPORT.md`.

Its Theorem 1.1 writes conditional Shannon cost as a raw address term **minus** an exact conditional KL/mutual-information rebate, and its later component-count theorem preserves that rebate instead of positive-parting it. The decomposition below is the real-coordinate-restriction analogue for the live one-sided erasure residual.

No statement from either peer is promoted beyond its proved scope.

## 2. The live common Shannon implication

For a physical coordinate `i`, orient each Fourier edge from `T` not containing `i` to `T+i`. Write

\[
x_T=p_T,\qquad y_T=p_{T+i},\qquad m_T=x_T+y_T,
\tag{2.1}
\]

and

\[
\alpha_i=\sum_T y_T=\operatorname{Inf}_i(f).
\tag{2.2}
\]

The `i`-part of (0.2) is

\[
L_i(f)=\sum_T y_T\log_2\frac{m_T}{y_T}.
\tag{2.3}
\]

When `alpha_i>0`, define two genuine probability laws on the real restriction pairs:

\[
P_i(T)=\frac{y_T}{\alpha_i},
\qquad
M_i(T)=m_T.
\tag{2.4}
\]

Parseval gives `sum_T m_T=1`.

### Theorem 2.1 — exact negative-credit form

For every Boolean `f` and every active physical coordinate `i`,

\[
\boxed{
L_i(f)
=
\alpha_i\left[
\log_2\frac1{\alpha_i}
-
D_2(P_i\Vert M_i)
\right].
}
\tag{2.5}
\]

#### Proof

Since `y_T=alpha_i P_i(T)` and `m_T=M_i(T)`,

\[
\log_2\frac{m_T}{y_T}
=
\log_2\frac1{\alpha_i}
-
\log_2\frac{P_i(T)}{M_i(T)}.
\]

Multiply by `y_T=alpha_i P_i(T)` and sum. QED.

Thus the raw address cost `alpha_i log(1/alpha_i)` and the forward KL are **not separate positive quantities**. The unpaid one-sided Shannon remainder is their canceled difference.

Summing (2.5),

\[
\boxed{
L(f)
=
\sum_i\alpha_i\log_2\frac1{\alpha_i}
-
\sum_i\alpha_iD_2(P_i\Vert M_i).
}
\tag{2.6}
\]

Consequently the exact remaining universal implication in this route is:

\[
\boxed{
\sum_i\alpha_iD_2(P_i\Vert M_i)
\ge
\sum_i\alpha_i\log_2\frac1{\alpha_i}
-
C_0 I(f)
}
\tag{2.7}
\]

for some finite dimension-free `C_0`.

If (2.7) held, then `L<=C_0 I`; (0.1) would give

\[
B(f)\le\left(C_0+\frac1{\ln2}\right)I(f),
\]

and the already-proved erasure restriction induction would give

\[
H(f)\le
\left(C_0+\frac3{\ln2}\right)I(f).
\tag{2.8}
\]

Equation (2.7) is **OPEN**. Equations (2.5)-(2.6) are **PROVED**.

## 3. Exact conditional packet decomposition under a real restriction

Let `Y_i=Y_i(T)` be **any deterministic label of the actual restriction pair**. No synthetic independent packet law is introduced. Push `P_i,M_i` forward to `P_i^Y,M_i^Y`.

KL chain rule gives

\[
D_2(P_i\Vert M_i)
=
D_2(P_i^Y\Vert M_i^Y)
+
\mathbb E_{a\sim P_i^Y}
D_2(P_i(\cdot\mid a)\Vert M_i(\cdot\mid a)).
\tag{3.1}
\]

Combining (2.5) and (3.1),

\[
\boxed{
L_i
=
\alpha_i\!\left[
\log_2\frac1{\alpha_i}
-
D_2(P_i^Y\Vert M_i^Y)
-
\mathbb E_{a\sim P_i^Y}
D_2(P_i(\cdot\mid a)\Vert M_i(\cdot\mid a))
\right].
}
\tag{3.2}
\]

Both conditional information terms retain their correct **negative** sign.

### Source-magnitude packets

Take the genuine packet label

\[
Y_i(T)=|\widehat f(T+i)|.
\]

For a nonzero magnitude `a`, let

\[
C_{i,a}=\{T:|\widehat f(T+i)|=a\},
\qquad
k_{i,a}=|C_{i,a}|,
\]

\[
\beta_{i,a}=k_{i,a}a^2,
\qquad
\gamma_{i,a}=\sum_{T\in C_{i,a}}m_T.
\tag{3.3}
\]

Conditional on this source packet, `P_i` is exactly uniform:

\[
P_i(T\mid a)=\frac1{k_{i,a}}.
\]

Let

\[
Q_{i,a}(T)=\frac{m_T}{\gamma_{i,a}}.
\]

Then (3.2) becomes the fully explicit real-packet identity

\[
\boxed{
L_i
=
\sum_{a>0}
\beta_{i,a}
\left[
\log_2\frac{\gamma_{i,a}}{\beta_{i,a}}
-
D_2(U_{i,a}\Vert Q_{i,a})
\right].
}
\tag{3.4}
\]

This is the requested conditional packet decomposition of the actual unpaid Shannon remainder. The within-packet divergence measures exactly how far the neighbor-pair masses are from being uniform inside a true equal-source-magnitude packet.

No valuation or projection integrality is assumed in (3.1)-(3.4). If one further coarsens the magnitude packet by a signed valuation/physical-mesh label, that coarsening is legitimate only where the existing signed packet-lattice theorem supplies that label; arbitrary physical projections are not declared integral.

## 4. PROVED physical-lattice non-saturation

The arbitrary-probability extremizer of (2.5) is `P_i=M_i`, which makes the negative KL credit vanish. Actual Boolean spectra cannot realize that extremizer at a nonfair active coordinate.

### Theorem 4.1 — dyadic non-saturation

Let `f:{0,1}^n->{-1,+1}` be Boolean and let

\[
0<\alpha_i=\operatorname{Inf}_i(f)<1.
\]

If

\[
D_2(P_i\Vert M_i)=0,
\]

then

\[
\boxed{\alpha_i=\frac12.}
\tag{4.1}
\]

Equivalently, after the standard character centering that makes every folded influence at most `1/2`,

\[
0<\alpha_i<\frac12
\quad\Longrightarrow\quad
D_2(P_i\Vert M_i)>0.
\tag{4.2}
\]

#### Proof

`D(P_i||M_i)=0` implies `P_i=M_i` pairwise. Hence for every pair with `m_T>0`,

\[
y_T=\alpha_i m_T,
\qquad
x_T=(1-\alpha_i)m_T.
\]

Because `0<alpha_i<1`, every occupied pair has both endpoints nonzero and therefore

\[
\frac{|\widehat f(T+i)|}{|\widehat f(T)|}
=
\sqrt{\frac{\alpha_i}{1-\alpha_i}}
=:c
\tag{4.3}
\]

is constant.

Every Boolean Fourier coefficient is a rational Walsh average, so `c` is rational. Write `c=r/s` in lowest positive integer terms. Then

\[
\alpha_i=\frac{r^2}{r^2+s^2}.
\tag{4.4}
\]

On the other hand physical influence is a cube boundary density,

\[
\alpha_i=\Pr_x[f(x)\ne f(x\oplus e_i)],
\]

so it is dyadic. Since `gcd(r^2,r^2+s^2)=1`, (4.4) forces `r^2+s^2` to be a power of two.

If one of coprime `r,s` is even and the other odd, `r^2+s^2` is odd and greater than one, impossible. If both are odd, `r^2+s^2=2 mod 4`, so the only power of two possible is `2`, forcing `r=s=1`. Hence `alpha_i=1/2`. QED.

### What this does and does not buy

This is a genuine Boolean/physical-lattice exclusion of exact product-law saturation. It does **not** give a dimension-free quantitative KL gap. The elementary rational lattice alone can only force exponentially small separations as dimension grows, which is insufficient for (2.7).

So the statement

> “Booleanity prevents zero negative credit”

is **PROVED**, while

> “Booleanity supplies a fixed positive fraction of the raw address cost as negative credit”

remains **OPEN** and cannot be inferred from Theorem 4.1.

## 5. Application of the peer tensor criterion

For disjoint Boolean functions `f` and `g`, and a coordinate `i` belonging to the `f` block, the spectral product law gives

\[
P_i^{f\otimes g}=P_i^f\otimes p^g,
\qquad
M_i^{f\otimes g}=M_i^f\otimes p^g.
\tag{5.1}
\]

Therefore

\[
D_2(P_i^{f\otimes g}\Vert M_i^{f\otimes g})
=
D_2(P_i^f\Vert M_i^f),
\tag{5.2}
\]

and `alpha_i` is unchanged. The same holds for coordinates in the `g` block. Consequently

\[
\boxed{
\sum_i\alpha_iD_2(P_i\Vert M_i)
}
\]

is exactly additive under disjoint products, as is `L`.

This applies the `account02/B15` tensor-saturation result to the same normalized remainder: unlike the refuted radius-one local discount, the KL credit in (2.6) survives at **linear tensor scale**. It therefore passes that necessary structural test. This is not a proof of the missing lower bound (2.7).

## 6. Counterexample / falsification tests

A standard-library checker exhaustively evaluated every Boolean truth table through `n=4`, restricted to physical coordinates with

\[
0<\alpha_i<1/2.
\]

There are `94,400` such coordinate instances (`192` at `n=3`, `94,208` at `n=4`). It found:

- **zero** exact `P_i=M_i` saturations, matching Theorem 4.1;
- maximum numerical discrepancy in (2.5): `5.55e-17`;
- maximum numerical discrepancy in the source-magnitude packet identity (3.4): `1.11e-16`.

The finite data also warns against promoting qualitative non-saturation into a fixed fractional credit without proof:

- at `n=3`, the smallest observed ratio
  \[
  \frac{\alpha_iD(P_i\Vert M_i)}
       {\alpha_i\log_2(1/\alpha_i)}
  \]
  is `0.20975898813907973`;
- at `n=4` it is already only `0.0501476528975366`, at a coordinate with `alpha_i=3/8`.

Thus the clean candidate inequality

\[
\alpha_iD(P_i\Vert M_i)
\ge\frac1{16}\alpha_i\log_2(1/\alpha_i)
\tag{6.1}
\]

for **every coordinate** is **REFUTED** by an actual four-variable Boolean truth table (checker witness mask `7`, coordinate `2`). This does not refute an aggregate inequality such as (2.7).

The largest observed `L_i/alpha_i` through `n=4` is `2.3332780003503975`.

Checker SHA-256:

`0e649f9d3187e1c0a7bc147588f7b75c02103580253d08b854edb9ed0e38c472`

Output SHA-256:

`66ffc76375abc95fca9aa1455f044235e52b273c7aff948be1536d80e180c6d9`

These computations are targeted falsification evidence, not a universal proof.

## 7. One-point zero-valuation stress test

The completed `account01/B15` zero-valuation family

\[
f_n(0)=1,\qquad f_n(x)=-1\ (x\ne0),
\qquad N=2^n,
\]

has

\[
\alpha_i=\frac2N.
\]

For every coordinate, (2.3) evaluates exactly to

\[
L_i
=
\frac4{N^2}
\log_2\frac{N^2-4N+8}{4}
+
\frac2N-\frac4{N^2}.
\tag{7.1}
\]

Hence

\[
\frac{L_i}{\alpha_i}
=
1-\frac2N
+
\frac2N\log_2\frac{N^2-4N+8}{4}
\longrightarrow1.
\tag{7.2}
\]

So the local negative KL credit cancels almost all of the raw

\[
\alpha_i\log_2(1/\alpha_i)\asymp \frac{n}{2^{n-1}}
\]

address cost even though the global physical-height KLs in the peer report are individually unpayable. This is exactly the cancellation discipline required by interface D / Campaign B.

## 8. Status, dead route, and next attack

### PROVED

1. Exact real-restriction negative-credit identity (2.5)-(2.6).
2. Exact conditional packet chain rule (3.2).
3. Exact source-magnitude packet formula (3.4).
4. Boolean/dyadic non-saturation: `D(P_i||M_i)=0` at an active coordinate forces `Inf_i=1/2`.
5. The aggregate KL credit is additive under disjoint tensor products, so it passes the newest peer tensor-scale necessity test.

### REFUTED

The per-coordinate fixed-fraction candidate (6.1) with fraction `1/16` is false on a four-variable Boolean function. More generally, exact non-saturation alone is far too weak to justify a per-coordinate quantitative payment.

### OPEN / CONDITIONAL

The full problem is still the aggregate negative-credit implication (2.7). No finite `C_0` is proved.

The next attack should therefore **not** seek another coordinatewise Pinsker/lattice gap. It should preserve (3.2) and exploit correlation across coordinates/packets so that small conditional KL on one source-magnitude packet forces payment elsewhere through the original Boolean signed-convolution identities. The most concrete next move is:

1. group the exact magnitude packets by the already-legitimate signed valuation label only where that label is supplied by the packet-lattice theorem;
2. spend the `account02/B15` valuation-tail majorization on the valuation component;
3. leave the conditional physical-mesh KL in (3.2) negative;
4. seek a nonreusing aggregate inequality for the remaining mesh-address term rather than bounding either KL direction positively.

If that aggregate route fails, switch to APPROACHES route 13 directly: use
\[
\sum_S\widehat f(S)\widehat f(S\triangle U)=0
\]
to transport low-KL packet mass across magnitude scales before taking absolute values.

**Full unrestricted FEI remains OPEN / NOT PROVED.**
