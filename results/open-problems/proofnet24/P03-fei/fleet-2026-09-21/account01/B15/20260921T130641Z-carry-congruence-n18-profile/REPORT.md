# B15 — carry congruences and exact n=18 packet profile

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** The current control plane and FEI repository were read through authenticated GitHub access. No authenticated cognitive-brain retrieval/context was used in the mathematics.

**Route:** spectral magnitude / arithmetic structure, owner-directed APPROACH 4/8.  
**Research frontier read before this work:** private `master` was re-resolved at `46cbf7cac909b5fd91c72d402c8a84b6534d89fe`; the required `TASKS_2026-09-21.md`, `REPORT.md`, and `APPROACHES.md` were read from the fresh frontier before computation. This run does **not** rerun the settled read-once certificate.

The current owner handoff correctly retires the old conjecture that Hod's `beta(1/2)=6.4547837...` is the universal sharp FEI constant. Numaro's published 18-variable balanced monotone seed gives the certified lower bound

\[
C_{\rm FEI}>6.521845710923046575.
\]

That is external prior work, not a new lower-bound claim here. The purpose of this run is different: profile the **arithmetic carry geometry** of that exact record seed and prove a structural lemma explaining what a packet valuation can and cannot do.

## 1. Exact signed-packet carry criterion

Let \(A\subseteq 2^{[n]}\) be nonempty and attach signs \(\epsilon_S\in\{\pm1\}\). Put

\[
V(x)=\sum_{S\in A}\epsilon_S(-1)^{\langle S,x\rangle},
\qquad x\in\{0,1\}^n,
\]

and define

\[
r(V)=\min_{V(x)\ne0}\nu_2(V(x)).
\]

For \(T\subseteq[n]\), define the signed upper-incidence sum

\[
M_T=\sum_{\substack{S\in A\\S\supseteq T}}\epsilon_S.
\]

### Lemma 1 (exact carry-moment characterization)

For every integer \(r\ge1\),

\[
\boxed{
r(V)\ge r
\iff
2^{\,r-|T|}\mid M_T
\quad\text{for every }T\subseteq[n],\ |T|<r.
}
\tag{1}
\]

**Proof.** Write the input bits as \(x_i\in\{0,1\}\). Since

\[
(-1)^{\langle S,x\rangle}
=\prod_{i\in S}(1-2x_i)
=\sum_{T\subseteq S}(-2)^{|T|}x_T,
\]

where \(x_T=\prod_{i\in T}x_i\), we have the multilinear integer polynomial identity

\[
V(x)=\sum_{T\subseteq[n]}(-2)^{|T|}M_Tx_T.
\tag{2}
\]

For an integer multilinear polynomial \(P(x)=\sum_T c_Tx_T\) on the Boolean cube, all values \(P(x)\) are divisible by \(2^r\) iff all coefficients \(c_T\) are divisible by \(2^r\). One direction is immediate. The other follows by Boolean-cube Möbius inversion,

\[
c_T=\sum_{U\subseteq T}(-1)^{|T|-|U|}P(1_U).
\]

Applying this to (2) gives exactly (1). \(\square\)

Thus low carry depths have completely explicit congruence meanings:

- \(r(V)\ge1\) iff \(\sum_S\epsilon_S\) is even;
- \(r(V)\ge2\) iff \(\sum_S\epsilon_S\equiv0\pmod4\) and every signed coordinate-incidence sum \(\sum_{S\ni i}\epsilon_S\) is even;
- \(r(V)\ge3\) additionally requires the total signed count mod \(8\), every signed coordinate-incidence sum mod \(4\), and every signed pair-incidence sum mod \(2\).

This criterion keeps the **actual signs** and therefore does not replace unequal-magnitude/carry geometry by an unsigned support count.

## 2. A dimension-free obstruction to deep carry

Let \(m=|A|\) and \(q=|\{x:V(x)\ne0\}|\).

### Lemma 2 (valuation forces packet multiplicity)

\[
\boxed{m\ge 2^{r(V)}.}
\tag{3}
\]

**Proof.** Parseval for the unnormalised Walsh transform gives

\[
\sum_xV(x)^2=2^n m.
\tag{4}
\]

Every nonzero value is a multiple of \(2^{r(V)}\), hence

\[
2^n m\ge q\,4^{r(V)}.
\tag{5}
\]

Also \(mq\ge2^n\). For completeness, this uncertainty inequality follows without an external theorem: for any \(S\in A\),

\[
1=|\epsilon_S|
=\left|2^{-n}\sum_xV(x)(-1)^{\langle S,x\rangle}\right|
\le 2^{-n}\sqrt q\left(\sum_xV(x)^2\right)^{1/2}
=\sqrt{\frac{qm}{2^n}}.
\]

Combining with (5) gives \(m^2\ge4^{r(V)}\), proving (3). \(\square\)

For a Fourier magnitude packet
\[
A_a=\{S:|\widehat f(S)|=a\},
\]
with signs \(\epsilon_S=\operatorname{sgn}\widehat f(S)\), this yields

\[
\boxed{r_a\le \log_2 |A_a|.}
\tag{6}
\]

Consequently, with packet mass \(p_a=|A_a|a^2\),

\[
R(f):=\sum_a p_ar_a
\le \sum_a p_a\log_2|A_a|.
\tag{7}
\]

Equation (7) is **not FEI**: the right side is the conditional entropy inside equal-magnitude packets and is not yet controlled by influence. What it does prove is that a very deep 2-adic carry packet is impossible unless the equal-magnitude packet itself has exponentially large multiplicity. The remaining unrestricted difficulty therefore lies in a joint bound on packet multiplicity/label entropy and influence, not in an unconstrained carry tower.

## 3. Exact packet profile of the published n=18 record seed

I reconstructed Numaro's published \(n=18\) seed from the ten factual 512-bit slices already preserved in the private continuation. The reconstruction is accepted only after matching the published complete truth-table SHA-256

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

The exact integer Walsh transform gives:

\[
I=\frac{261}{128},\qquad
|\operatorname{supp}\widehat f|=2770,
\]

and only **10 distinct nonzero Fourier magnitudes**.

Using the inherited packet notation
\[
b_a=a2^{r_a},\qquad
R=\sum_ap_ar_a,\qquad
D=\sum_ap_a\log_2(1/b_a),
\]
the exact arithmetic data are

\[
\boxed{R=\frac{39021}{32768}=1.190826416015625}
\tag{8}
\]

and

\[
\boxed{N:=\sum_a\frac{p_a}{b_a^2}=\frac{19523}{8}=2440.375.}
\tag{9}
\]

The already-certified entropy interval from the independent external-seed continuation is

\[
6.776605309005978082519790221891882314787235038
\le H
\le
6.776605309005978082519790221891882314787235039.
\]

Since the packet identity \(H=2R+2D\) is exact, this turns the descriptive floating-point value into the rigorous interval

\[
\boxed{
2.197476238487364041259895110945941157393617519
\le D\le
2.1974762384873640412598951109459411573936175195.
}
\tag{10}
\]

The packet-KL identity \(2D=\log_2N-K\) gives the descriptive value
\(K\approx6.857934664111188\), again showing that raw normalizer size is not a usable substitute for the retained KL credit.

### Valuation bands

| valuation \(r\) | exact spectral mass | coefficient count | packet count | exact \(N\)-contribution | descriptive \(D\)-contribution |
|---:|---:|---:|---:|---:|---:|
| 0 | `15827/32768` | 2422 | 2 | 2422 | 1.2614816757 |
| 1 | `81/32768` | 18 | 1 | `9/2` | 0.0133855602 |
| 2 | `1455/4096` | 186 | 5 | `93/8` | 0.6191269867 |
| 3 | `1305/8192` | 144 | 2 | `9/4` | 0.3034820159 |

There is **no carry depth above 3**. The new feature relative to the earlier \(n=14\) record is an order-one \(r=3\) band of mass

\[
\frac{1305}{8192}=0.1593017578125.
\]

The two depth-3 packets each have multiplicity 72, comfortably above the rigorous lower bound \(2^3=8\). The checker independently computes the pointwise valuation and the congruence depth from Lemma 1 for every one of the ten packets; all ten agree.

## 4. The record improvement is again a large R/D transfer

The preceding B15 run profiled the merged \(n=14\) seed:

\[
I_{14}=\frac{521}{256},\qquad
R_{14}=\frac{189797}{262144},
\]
with amplified ledger
\[
L_R^{(14)}=\frac{2R_{14}}{I_{14}-1}
=\frac{189797}{135680}
=1.398857606132075\ldots,
\]
\[
L_D^{(14)}=5.091255237391319\ldots,
\qquad
L^{(14)}=6.490112843523394\ldots.
\]

For the \(n=18\) record,

\[
L_R^{(18)}
=\frac{2R_{18}}{I_{18}-1}
=\frac{39021}{17024}
=2.2921170112781954887\ldots,
\tag{11}
\]

while (10) gives

\[
4.2297286996448510869\ldots
\le L_D^{(18)}
\le
4.22972869964485108694\ldots.
\tag{12}
\]

Therefore the valuation contribution rises by the **exact** amount

\[
\boxed{
L_R^{(18)}-L_R^{(14)}
=
\frac{16119259}{18045440}
=
0.893259405146120\ldots
}
\tag{13}
\]

whereas the free-energy contribution drops by about

\[
\boxed{\Delta L_D\approx-0.861526537746468.}
\tag{14}
\]

The net record improvement is only about \(+0.03173286739965\). Thus the \(n=18\) post-Hod record is even more strongly a **valuation/free-energy transfer** than the \(n=14\) step: a nearly \(0.9\)-bit increase in the normalized valuation ledger is mostly cancelled by a nearly \(0.86\)-bit decrease in the normalized \(D\) ledger.

This rules out the hoped-for interpretation that the record gain comes from an ever-deeper uncontrolled \(D\)-tail. It does not. The new seed develops depth 3, but the total \(D\) ledger falls sharply; the gain is the small remainder of a large internal transfer.

## 5. What survives as a universal target

Combining the exact carry criterion, the multiplicity obstruction, and the record profiles gives a sharper formulation of the B15 route:

1. **Carry depth is not free.** Depth \(r\) requires a hierarchy of signed incidence congruences and at least \(2^r\) equal-magnitude coefficients.
2. **Deep carry alone is not the record mechanism.** The current record has no packet deeper than 3.
3. **Neither \(R\) nor \(D\) can be paid independently by a coarse influence bound.** Known record improvements move large amounts between them while changing \(H/(I-1)\) only slightly.
4. The correct object is the joint packet entropy. If \(M\) denotes the magnitude label of a spectral sample, then exactly
\[
H(S)=H(M)+\mathbb E[\log_2|A_M|].
\tag{15}
\]
Lemma 2 controls the valuation part by the second term, but FEI still requires a dimension-free way to charge the **magnitude-label entropy plus packet multiplicities** to \(\mathbb E|S|=I(f)\), using Booleanity across different packets.

A promising next step is to combine (1) with restriction: determine how the signed upper-incidence moments \(M_T\) of adjacent magnitude packets transform under a coordinate restriction, and look for a telescoping charge to the coordinate influence. That preserves the unequal-magnitude collision/carry obstruction instead of replacing it with a plateaued surrogate.

## 6. Primary-literature boundary checked

A current primary-source check on 21 September 2026 found:

- Numaro, NUMARO-2026-016 (22 July 2026), the public \(n=18\) certified lower bound \(>6.521845710923046575\), with PR #130 merged 2 August 2026.
- V. N. Potapov, arXiv:2609.21563 (submitted 18 September 2026; current arXiv page checked 21 September), proving FEI with sharp constant 4 for Boolean plateaued functions and sharp constant 2 for partially bent functions.

Potapov's theorem is especially relevant: a **single-magnitude** Boolean spectrum is already controlled. The present route is explicitly about the unresolved multiple-magnitude setting, where signed packets collide and their carry depths differ. No publication-priority claim is made for Lemmas 1–2 or for this packet accounting.

The live Optimization Problems constant page and Numaro report both still describe unrestricted FEI as open. Full FEI therefore remains **OPEN / NOT PROVED**.

## 7. Reproducibility

`n18_packet_carry_profile.py`:

- reconstructs the exact published truth table and rejects a digest mismatch;
- performs the integer Walsh transform and checks Parseval and \(I=261/128\);
- groups all 2770 nonzero coefficients into the 10 exact magnitude packets;
- computes each packet's pointwise valuation \(r_a\);
- independently recomputes the same depth from Lemma 1's signed incidence congruences;
- verifies \(m_a\ge2^{r_a}\) for every packet;
- computes exact \(R\), \(N\), band masses, multiplicities, and descriptive \(D,H,K\).

Native run result: **PASS**.  
Script SHA-256: `ae12076b7daf0d6df7e6d19c62a3bfd1523527f5c39e474d12365abb5b25555c`.  
Output SHA-256: `eadb7ca29e82a4feb6f90786cb5794fafc6ea4727b7dd233145d6b770458cf73`.

The one stderr warning in the local subprocess was an unrelated spreadsheet-runtime warmup timeout emitted before the script ran; the profiler itself exited code 0 and its exact checks passed.

**Next B15 target:** derive the restriction law for the signed moment hierarchy in (1), then test whether the loss of one congruence level can be charged to the corresponding coordinate's influence. If that fails, construct the smallest genuine Boolean counterexample to such a local charge and retain its unequal-magnitude packet collision.
