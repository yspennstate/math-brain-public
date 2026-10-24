# B18 FEI proof integration — sign-class erasure matching, channel-stable near-subcube rows, and the phase-aware factorization correction

**Run:** `20260921T181405Z-b18-fei-r13`  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of full uniform-cube FEI:** **OPEN / NOT PROVED**  
**Claim level:** universal local theorems plus an exact refutation/repair of a proposed multiscale factorization step. No novelty or publication-priority claim.

## 0. Fresh state, dependencies, and non-overlap

This run entered from `proofnet24/P03-fei` master after the fresh B12/B13/B16 updates visible on 21 September 2026. The exact compatible inputs used are:

1. account04/B18 `20260921T171222Z-signed-subcube-palm/REPORT.md`, blob
   `f9ec73b8de2de1d0aa77f17d9c396ed41a5ecc6e`: exact signed-subcube Palm factorization,
   `Delta=I(sigma)`, lower-dimensional self-embedding, and hybrid collision payment.
2. account02/B12 `20260921T175134Z-physical-erasure-budget/REPORT.md`, blob
   `4d83eff4cf5396b2d5a14ed577ad55f0ff5c6990`: the exact depth-slack conservation,
   physical erasure budget, sequential DTC identity, and Ellis-based support stability.
3. account02/B13 `20260921T180326Z-sign-stability-defect/REPORT.md`, blob
   `b4812f3ae22e7f98596f4b1abcb284dc2d180457`: the exact four-bank sign decomposition
   and dimension-free sign/Palm-TV transfer.
4. account02/B13 `20260921T165419Z-derivative-block-complementarity/REPORT.md`, blob
   `23ab0bd6734d3cb9a2f32ced4e54ac7213acf627`: the reduced-state entanglement bank
   and physical/spectral/mixed-axis collision conservation.
5. account03/B17 `20260921T173244Z-character-gauge-total-correlation/REPORT.md`, blob
   `9f54bc6714c2188fa2c46551972b2a4a5a8456da`: exact block-tree total-correlation
   decomposition and the proposed next implication “small block spectral MI + Boolean convolution => near product”.
6. account01/B16 `20260921T182439Z-projective-three-qflip-transport/REPORT.md`, blob
   `d7b9b808956a62fd2d0b700f718928522beef7d9`: fresh signed/projective transport,
   used here only as confirmation that the phase/frustration bank is being attacked elsewhere.

This run does not duplicate q-flip transport, pairwise-tree calculations, or another FEI finite sweep. It integrates the fresh B12/B13 row theory, then independently stress-tests B17's proposed end-to-end factorization step.

Throughout, for a nonzero ternary Boolean derivative row
\[
g:\mathbb F_2^m\to\{0,\pm1\},
\qquad
j=\mathbb E g^2,
\]
write
\[
d_g=\sum_{r=1}^m\|D_rg\|_2^2,\qquad
M=\frac{d_g}{j},\qquad
L=\log_2\frac1j,\qquad
\Delta=M-\frac L2.
\]
For the low-influence stability statements assume \(0<j\le1/2\), exactly as in the fresh B13 four-bank theorem. Let
\[
A=\{g=+1\},\quad B=\{g=-1\},\quad a=\mu(A),\quad b=\mu(B),
\]
and globally flip \(g\), if needed, so \(a\ge b\). Put
\[
\theta=\frac bj\in[0,1/2].
\]

---

## 1. PROVED: the B12 physical-erasure budget and B13 sign banks match exactly

For a nonempty set \(C\subseteq\mathbb F_2^m\), let \(U_C\) be uniform on \(C\). Define
\[
\operatorname{DTC}(U_C)
=
H(U_C)-\sum_r H((U_C)_r\mid (U_C)_{-r}).
\]
If \(c=\mu(C)\), then
\[
\boxed{
\operatorname{DTC}(U_C)
=
\frac{I(1_C)}{2c}-\log_2\frac1c
=
\frac{\operatorname{Iso}(C)}{2c}.
}
\tag{1.1}
\]
Indeed, each internal \(r\)-edge contributes exactly two conditional-erasure bits when counted from its two endpoints, while
\(m|C|=2e_{\rm int}+|\partial C|\).

Now draw \(X\) uniformly from \(E=A\sqcup B\) and put \(\Sigma=g(X)\). Conditional on \(\Sigma=+1\), \(X\) is uniform on \(A\); conditional on \(\Sigma=-1\), it is uniform on \(B\). Therefore
\[
\boxed{
\operatorname{DTC}(X\mid\Sigma)
=
\frac{\operatorname{Iso}(A)+\operatorname{Iso}(B)}{2j}.
}
\tag{1.2}
\]
Since \(H(\Sigma)=h_2(\theta)\), the B12 physical-erasure quantity becomes
\[
\boxed{
\mathcal E_{\rm phys}
=
h_2(\theta)
+
\frac{\operatorname{Iso}(A)+\operatorname{Iso}(B)}{2j}.
}
\tag{1.3}
\]

The fresh B13 four-bank identity is
\[
4j\Delta
=
\operatorname{Iso}(A)+\operatorname{Iso}(B)
+2J(A,B)+2jh_2(\theta),
\tag{1.4}
\]
where \(J(A,B)\) is the oriented opposite-sign adjacency budget. Dividing by \(2j\) and comparing with (1.3) gives the exact synthesis
\[
\boxed{
\mathcal E_{\rm phys}
=
2\Delta-\frac{J(A,B)}j.
}
\tag{1.5}
\]
Comparing with B12's
\[
\mathcal E_{\rm phys}=2\Delta-\frac{S_{\rm sign}}{4j}
\]
also yields
\[
\boxed{S_{\rm sign}=4J(A,B).}
\tag{1.6}
\]

So the two independently developed ledgers have no hidden mismatch: the B12 “sign slack” is exactly four times the B13 opposite-sign adjacency bank, while conditional physical DTC is exactly the density-weighted isoperimetric slack of the two sign classes.

---

## 2. PROVED: majority-sign subcube stability with a channel-stable Hellinger/Renyi bound

The new point is to apply cube stability to the **majority sign class \(A\)** itself, rather than first approximating the unsigned support and then repairing signs.

From (1.4),
\[
h_2(\theta)\le2\Delta
\tag{2.1}
\]
and
\[
\operatorname{Iso}(A)\le4j\Delta.
\tag{2.2}
\]
Define the normalized isoperimetric excess of \(A\)
\[
\varepsilon_A
:=
\frac{\operatorname{Iso}(A)}{2a}.
\]
Because \(a=j(1-\theta)\),
\[
\boxed{
\varepsilon_A\le\frac{2\Delta}{1-\theta}.
}
\tag{2.3}
\]

Use the same Ellis almost-isoperimetric stability theorem invoked in the fresh B12 report. Whenever \(\varepsilon_A\) lies in that theorem's absolute small-excess regime, there is a coordinate subcube \(Q\) with
\[
\delta
:=
\frac{\mu(A\triangle Q)}a
\le
\frac{2\varepsilon_A}{\log_2(1/\varepsilon_A)}.
\tag{2.4}
\]
Write \(q=\mu(Q)\), and let \(F\) be the set of coordinates fixed by \(Q\).

Let
\[
\psi=\frac{g}{\sqrt j},
\qquad
\phi=\frac{1_Q}{\sqrt q}
\]
in the normalized physical \(L^2\) space. Since \(B\cap Q\subseteq Q\setminus A\),
\[
\mu(A\cap Q)\ge a(1-\delta),
\qquad
\mu(B\cap Q)\le a\delta,
\qquad
q\le a(1+\delta).
\]
Thus, for \(\delta<1/2\),
\[
\boxed{
\langle\psi,\phi\rangle
\ge
\sqrt{1-\theta}\,
\frac{1-2\delta}{\sqrt{1+\delta}}.
}
\tag{2.5}
\]

Let \(P_g\) be the derivative Palm spectral law
\[
P_g(S)=\frac{\widehat g(S)^2}{j},
\]
and \(P_Q\) the corresponding normalized squared-Walsh law of \(1_Q\). Walsh transform is unitary, so the classical Bhattacharyya affinity obeys
\[
\sum_S\sqrt{P_g(S)P_Q(S)}
\ge
|\langle\psi,\phi\rangle|.
\]
Hence, with squared Hellinger convention
\[
H_{\rm Hel}^2(P,Q)=1-\sum_x\sqrt{P(x)Q(x)},
\]
we obtain

### Theorem B18-MAJORITY-SUBCUBE-HELLINGER-01
\[
\boxed{
H_{\rm Hel}^2(P_g,P_Q)
\le
1-
\sqrt{1-\theta}\,
\frac{1-2\delta}{\sqrt{1+\delta}}.
}
\tag{2.6}
\]

More importantly, this survives **every common Markov postprocessing**. For every channel \(T\)—in particular coordinate projection, block erasure, fixed thinning, or the random-prefix thinning channel—
\[
\boxed{
H_{\rm Hel}^2(TP_g,TP_Q)
\le
1-
\sqrt{1-\theta}\,
\frac{1-2\delta}{\sqrt{1+\delta}}.
}
\tag{2.7}
\]
Equivalently, the order-\(1/2\) Renyi divergence in bits satisfies
\[
\boxed{
D_{1/2}(TP_g\|TP_Q)
\le
-2\log_2\!\left(
\sqrt{1-\theta}\,
\frac{1-2\delta}{\sqrt{1+\delta}}
\right).
}
\tag{2.8}
\]
This is dimension-free and channel-stable; no alphabet-size/Fannes factor appears.

### Explicit small-defect form

Let
\[
x=\frac{\Delta}{\log_2(1/\Delta)}.
\]
Assume \(\Delta\le1/16\) and that \(\varepsilon_A\) is in the Ellis stability regime. From
\(h_2(\theta)\ge\theta\log_2(1/\theta)\), (2.1), and \(\theta\le\Delta\),
\[
\theta\le2x.
\tag{2.9}
\]
Then
\[
\varepsilon_A\le \frac{64}{31}\Delta.
\]
Since
\[
\log_2(64/31)=1.0458036896\ldots
\]
and \(\log_2(1/\Delta)\ge4\), (2.4) gives
\[
\delta<6x.
\tag{2.10}
\]
Using
\[
\sqrt{1-\theta}\ge1-2x,\qquad
1-2\delta\ge1-12x,\qquad
(1+\delta)^{-1/2}\ge1-3x,
\]
and \(x\le1/64\), (2.5) yields affinity at least \(1-17x\). Therefore
\[
\boxed{
H_{\rm Hel}^2(TP_g,TP_Q)
\le
17\,\frac{\Delta}{\log_2(1/\Delta)}
}
\tag{2.11}
\]
for every common channel \(T\), under the stated small-excess regime.

This is stronger than an ambient-space TV statement in the direction needed by the current random-prefix programme: the same quantitative proxy survives the actual erasure/projection channel.

---

## 3. PROVED: an \(O(\Delta/\log(1/\Delta))\) off-axis spectral leakage bound

The Hellinger statement has a simple spectral-support consequence that makes the remaining “address entropy” obstruction explicit.

A coordinate subcube \(Q\) fixed on \(F\) has Fourier support only on subsets of \(F\). Let
\[
\alpha_F
:=
P_g\{S:S\not\subseteq F\}.
\]
The functions whose Fourier support is contained in \(F\) are exactly the functions depending only on \(F\). Orthogonal projection onto that subspace and \(1_Q\) as a comparison function give
\[
j\alpha_F
\le
\|g-1_Q\|_2^2.
\tag{3.1}
\]
The physical error decomposes exactly as
\[
\|g-1_Q\|_2^2
=
\mu(A\triangle Q)+b+2\mu(B\cap Q).
\tag{3.2}
\]
Since \(\mu(B\cap Q)\le\mu(Q\setminus A)\le a\delta\),
\[
\boxed{
\alpha_F
\le
3(1-\theta)\delta+\theta
\le
3\delta+\theta.
}
\tag{3.3}
\]
Combining (2.9)-(2.10) gives the explicit small-defect leakage estimate
\[
\boxed{
P_g\{S:S\not\subseteq F\}
\le
20\,\frac{\Delta}{\log_2(1/\Delta)}.
}
\tag{3.4}
\]

So low-depth-defect rows do not merely have a nearby subcube in physical space: all but
\(O(\Delta/\log(1/\Delta))\) of their Palm Fourier mass lies on the corresponding fixed-coordinate spectral axis.

This still does **not** control the Shannon entropy carried by the rare off-axis addresses.

---

## 4. PROVED: exact phase-aware product recursion for zero-entanglement derivative rows

The fresh B17 route proposes using a block tree and treating near-factorizing cuts recursively. The correct exact factorization statistic is not spectral block mutual information alone; B13's reduced-state entanglement bank detects the missing phase information.

Fix a nontrivial coordinate cut \(J\mid J^c\). Let
\[
\psi=\frac{g}{\sqrt{2^m j}}
\]
in counting-measure normalization and let
\[
E_J=1-\operatorname{tr}\rho_J^2
\]
be B13's linear-entanglement bank.

### Theorem B18-TERNARY-SCHMIDT-RECURSION-02

If \(E_J=0\), then there are nonzero ternary signed indicators
\[
g_1:\mathbb F_2^J\to\{0,\pm1\},
\qquad
g_2:\mathbb F_2^{J^c}\to\{0,\pm1\},
\]
and a global sign \(s\) such that
\[
\boxed{g(x,y)=s\,g_1(x)g_2(y).}
\tag{4.1}
\]
Consequently, if \(j_k=\mathbb E g_k^2\) and \(P_k\) are the two factor Palm laws,
\[
\boxed{
j=j_1j_2,\qquad
P_g=P_1\otimes P_2.
}
\tag{4.2}
\]
Hence
\[
\boxed{
H(P_g)=H(P_1)+H(P_2),
\quad
M(g)=M(g_1)+M(g_2),
\quad
\Delta(g)=\Delta(g_1)+\Delta(g_2).
}
\tag{4.3}
\]

### Proof

For a pure state, \(E_J=0\) iff the Schmidt rank is one, so
\[
\psi=u\otimes v.
\]
The nonzero support is therefore
\[
\operatorname{supp}u\times\operatorname{supp}v.
\]
Because every nonzero entry of \(g\) has the same magnitude \(1\), every nonzero entry of \(\psi\) has the same magnitude. Fixing one nonzero coordinate of \(v\) shows that \(|u_x|\) is constant on its support; similarly \(|v_y|\) is constant. Unit normalization then gives
\[
u(x)=\frac{\sigma_1(x)}{\sqrt{|E_1|}},
\qquad
v(y)=\frac{\sigma_2(y)}{\sqrt{|E_2|}}
\]
with \(\sigma_k\in\{\pm1\}\) on \(E_k\). This proves (4.1). Walsh transform tensorizes, giving (4.2), and entropy, mean Fourier level, and \(\frac12\log(1/j)\) are additive, proving (4.3). QED.

Every ternary signed indicator is itself realizable as a genuine Boolean derivative row: for each point \(z\), choose the two values of a parent Boolean function equal if \(g(z)=0\), opposite in the appropriate order if \(g(z)=\pm1\). Thus (4.1) stays inside the actual derivative-row category rather than an arbitrary real-vector relaxation.

**Scope.** This is an exact recursion for the strengthened ternary-row problem. It does not by itself prove ordinary FEI on the factors, because the needed Palm-row inequality is stronger than simply applying FEI to an arbitrary parent.

---

## 5. PROVED: small entanglement gives dimension-free near-product measurement laws

The exact recursion has a sharp approximate state-level companion.

Let \(\lambda_1\ge\lambda_2\ge\cdots\) be the Schmidt probabilities of \(\psi\). Since
\[
\sum_k\lambda_k^2=1-E_J
\]
and
\[
\sum_k\lambda_k^2\le\lambda_1\sum_k\lambda_k=\lambda_1,
\]
the best product state \(\varphi=u_1\otimes v_1\) satisfies
\[
|\langle\psi,\varphi\rangle|^2=\lambda_1\ge1-E_J.
\tag{5.1}
\]
After Walsh measurement the comparison law is a product law, and measurement affinity is at least state overlap. Therefore

### Corollary B18-ENTANGLEMENT-PRODUCT-HELLINGER-03
\[
\boxed{
H_{\rm Hel}^2(P_g,P_{\rm prod})
\le
1-\sqrt{1-E_J}
\le E_J.
}
\tag{5.2}
\]
The same bound holds after every common Markov postprocessing.

This is the phase-aware near-factorization statement that spectral mutual information alone cannot supply. Its limitation is also exact: the nearby product factors in the \(E_J>0\) case need not themselves be flat ternary rows, so a Shannon-recursive argument still needs an additional stability/payment step.

---

## 6. REFUTED-LEMMA: spectral block MI + Boolean convolution does not imply near product

The newest B17 report proposes as its next lemma:

> small block spectral mutual information + the Boolean convolution identities should force the signed Fourier coefficient matrix near rank one/product.

In that form this is false, even at **zero** spectral mutual information.

For \(d\ge1\), let
\[
\sigma_d(x,y)=(-1)^{x\cdot y},
\qquad
x,y\in\mathbb F_2^d.
\tag{6.1}
\]
This is a genuine Boolean function and therefore obeys all Boolean Fourier convolution identities. A direct Walsh calculation gives
\[
\boxed{
\widehat{\sigma_d}(a,b)
=
2^{-d}(-1)^{a\cdot b}.
}
\tag{6.2}
\]
Hence its squared Fourier law is exactly uniform:
\[
P(a,b)=2^{-2d}=P_A(a)P_B(b),
\]
so
\[
\boxed{I(A;B)=0.}
\tag{6.3}
\]

But the normalized physical amplitude matrix is the \(2^d\times2^d\) Walsh-Hadamard matrix divided by \(2^d\). It has \(2^d\) equal Schmidt probabilities \(2^{-d}\). Thus
\[
\boxed{
E_{x|y}=1-2^{-d},
}
\tag{6.4}
\]
and the best rank-one Frobenius approximation leaves squared residual
\[
\boxed{
1-2^{-d}.
}
\tag{6.5}
\]
So the state becomes maximally far from product as \(d\to\infty\), while the **spectral block MI remains exactly zero**.

This counterexample can be embedded into the genuine derivative-row category by the previous B18 point-gated construction
\[
g(c,x,y)=1_{\{c=0\}}\sigma_d(x,y).
\]
Here \(j=1/2\), and the residual \(x|y\) spectral MI is still zero. Its depth defect is large:
\[
\Delta=I(\sigma_d)=d
\]
because each of the \(2d\) residual coordinates has influence \(1/2\). Thus it kills the proposed MI-only factorization mechanism without threatening the low-\(\Delta\) subcube branch proved above.

### Repaired multiscale statement

B17's exact block-tree identity remains valid and useful, but its recursive dichotomy must be **phase-aware**:

- large spectral block MI can pay through the multiscale total-correlation bank;
- small entanglement \(E_J\) gives a genuine near-product state by (5.2), with exact product recursion at \(E_J=0\);
- spectral MI can vanish while \(E_J\) (and/or B13's mixed-axis signed bank) is large, so that phase/frustration mass requires the B13/B16 signed-payment machinery rather than a false product conclusion.

This is a concrete correction, not a rejection of the multiscale programme.

---

## 7. Decisive finite calculations

`check_phase_aware_row_stability.py` was executed with the ordinary Python standard library.

It checked:

1. every nonzero ternary row with \(j\le1/2\) through dimension \(m=3\):
   - \(1,732\) rows;
   - B13 four-bank identity;
   - the new exact physical-erasure/sign matching identity (1.5);
2. for all rows whose best majority-sign coordinate-subcube proxy has \(\delta<1/2\):
   - \(1,040\) affinity lower-bound cases;
   - \(8,184\) spectral coordinate-projection contraction checks;
   - minimum affinity slack \(0\);
   - minimum projection-contraction slack \(0\);
3. \(7,744\) exact tensor-product ternary pairs through factor dimensions two:
   - density multiplication;
   - Palm-law entropy additivity;
   - mean-level additivity;
   - depth-defect additivity;
   - maximum discrepancy \(3.33\times10^{-16}\);
4. the inner-product bent family for \(d=1,2,3,4\):
   - exactly uniform spectral law;
   - spectral block MI exactly \(0\);
   - linear entanglement and best rank-one residual \(1/2,3/4,7/8,15/16\);
5. the inherited abstract rare-address obstruction:
   Hellinger distance and mean excess go to zero while Shannon excess diverges; at \(k=32\),
   \[
   H_{\rm Hel}^2=0.0157490157\ldots,\qquad
   \text{mean excess}=1/32,\qquad
   \text{Shannon excess}=32.2006223\ldots\text{ bits}.
   \]

The script SHA-256 is
`1e0d0dbbf0a3dfd685da802c3ad2bd76893f6d31b5673a67907b435904e76e7b`.

The exact captured output SHA-256 is
`c2557106024f0cac94f67e7c6684ba382933729f067b88137cb0b70f4cc0708f`.

These checks support the finite algebra and explicit families only. They are not a proof of Ellis stability or of full FEI.

---

## 8. Ledger

### PROVED

1. Exact identification of B12's conditional physical DTC with the density-weighted sign-class isoperimetric slacks, and exact matching \(S_{\rm sign}=4J(A,B)\).
2. Majority-sign subcube approximation from the fresh B13 four-bank plus Ellis stability.
3. A dimension-free Hellinger/Renyi-\(1/2\) approximation of the derivative Palm law to a coordinate-subcube Palm law that survives arbitrary common Markov channels.
4. In the small-defect/Ellis regime,
   \[
   H_{\rm Hel}^2(TP_g,TP_Q)
   \le17\Delta/\log_2(1/\Delta).
   \]
5. Off-axis Palm spectral mass
   \[
   P_g(S\not\subseteq F)
   \le20\Delta/\log_2(1/\Delta)
   \]
   in the same regime.
6. Exact zero-entanglement factorization of a ternary derivative row into lower-dimensional ternary factors, with exact tensorization of density, Palm law, entropy, mean level, and depth defect.
7. Small B13 entanglement bank implies dimension-free Hellinger closeness to a product spectral law.
8. The inner-product bent family refutes the proposed MI-only Boolean near-product implication.

### REFUTED / route correction

**REFUTED-LEMMA:** “small spectral block mutual information, even together with all Boolean convolution identities, forces the signed Fourier matrix near rank one/product.”

It fails with MI exactly zero on \(\sigma_d(x,y)=(-1)^{x\cdot y}\), where the rank-one residual tends to one.

Also still refuted from B12: Hellinger/TV closeness plus a small first-moment excess, by itself, cannot control Shannon address entropy.

### CONDITIONAL

The explicit \(17\) and \(20\) small-defect constants require that \(\varepsilon_A\) lie inside the absolute small-excess regime of the Ellis stability theorem. No threshold not present in that theorem is invented here.

Exact product recursion closes a branch only for a strengthened lower-dimensional derivative-row inequality; it is not silently promoted to ordinary lower-dimensional FEI.

### OPEN

Full uniform-cube FEI remains **OPEN / NOT PROVED**.

The surviving implication is now more specific:

> Prove a Boolean **address-entropy payment** for the \(O(\Delta/\log(1/\Delta))\) off-axis Palm mass, or prove that the accumulated B13 entanglement/mixed-axis banks along a block tree are paid by a universal multiple of influence/depth. The proof must exploit Boolean phase/cancellation or recursive derivative structure; generic Hellinger/TV continuity and spectral block MI are both insufficient.

A promising phase-aware block-tree induction is therefore:
1. low \(\Delta\): use the majority-subcube channel-stable proxy and pay only the rare off-axis addresses;
2. low \(E_J\): use near-product recursion;
3. large \(E_J\)/mixed-axis bank: charge through B13/B16 signed transport;
4. exact subcube/product endpoints recurse exactly.

That is the next non-overlapping integration target.
