# B17 — one-tail price adversary and exact KL tail-ladder replacement

**Run:** `20260922T054229Z-b17-fei-r19`  
**Role:** account04/B17, FEI adversarial constructions / remainder adversary and replacement.  
**Classification:** `ESSENTIAL_STEP_APPLIED / ONE_TAIL_SHORTCUT_REFUTED / SOURCE_PRICE_CREDIT_COMPRESSED`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository controls and mathematical sources were read directly; no authenticated native brain receiver context was used.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Exact predecessor consumed and target

The newest compatible other-account B15 result consumed is account02/B15

`proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T054027Z-packet-price-kl-numaro/REPORT.md`,

scientific commit `ced68a2ce5439e3dae47e31667ee6ec83cefb69e`, report blob `8f6afebd4c7f6ba33533a660e380fd06aefe6488`.

For a balanced Boolean source with spectral sample `S`, level `K=|S|`, influence marginals `j_i`, total influence `I`, and `q_i=j_i/I`, that report defines the level-conditioned source law `pi_k` and the q-weighted without-replacement law

\[
\nu_k(A)=\frac{\prod_{i\in A}q_i}{e_k(q)}.
\]

It proves the exact identity

\[
H(f)=H(K)+C_{\rm coll}(f)-D_{\rm lev},
\qquad
D_{\rm lev}=\sum_k W_kD_{\rm KL,2}(\pi_k\|\nu_k),
\tag{0.1}
\]

and the exact packet/coordinate-price sufficiency

\[
T_k(A)=\left(|\widehat f(A)|,\prod_{i\in A}q_i\right),
\qquad
D_{\rm lev}=D((T_k)_\#\pi_k\|(T_k)_\#\nu_k).
\tag{0.2}
\]

Writing `D_lev=D_mag+D_price|mag`, its exact Numaro calculation shows that the magnitude-packet term alone leaves the live balanced-center defect negative by more than `0.032131617677 (I-1)`, whereas the price-within-packet term is

\[
0.032137106754<\frac{D_{\rm price|mag}}{I-1}<0.032137106755.
\tag{0.3}
\]

Thus essentially the entire price credit is needed. The predecessor's first missing implication is to obtain a coarser source-exact part of that price KL from coordinate-price tails while retaining the unspent conditional KL. This report attacks exactly that implication.

The live all-gate center in the predecessor is `C_*=6.5218512`; no change of normalization is made here.

## 1. Adversary: one monotone price tail per packet is not universally exact

A natural strongest first coarsening of (0.2) is: within a fixed `(k,|hat f|)` packet, keep only one binary monotone threshold of the occurrence price `L_q(A)=prod_{i in A}q_i`. If that one bit preserved the entire within-packet KL universally, the coordinate-price term would collapse to a binary tail payment.

That statement is false on an exact four-variable balanced Boolean gate.

Let `g:{0,1}^4->{-1,1}` be `-1` exactly on the integer-labelled inputs

\[
\boxed{\{0,1,2,3,4,5,10,15\}},
\tag{1.1}
\]

with bit `x_0` least significant. Its exact Walsh vector is

\[
(0,0,0,0,-4,-4,4,4,-8,0,-8,0,-4,4,4,-4),
\tag{1.2}
\]

so the influences and normalized occurrence law are

\[
(j_0,j_1,j_2,j_3)=\left(\frac14,\frac12,\frac12,\frac34\right),
\qquad I=2,
\tag{1.3}
\]

\[
q=\left(\frac18,\frac14,\frac14,\frac38\right).
\tag{1.4}
\]

At level `k=2`, the packet with raw Walsh magnitude `4` (normalized Fourier magnitude `1/4`) contains exactly the three occupied sets

\[
\{0,2\},\quad \{1,2\},\quad \{2,3\}.
\]

Their occurrence prices are respectively

\[
\frac1{32},\quad\frac1{16},\quad\frac3{32}.
\tag{1.5}
\]

Because the three squared Fourier coefficients agree, the actual conditional law inside the packet is

\[
P=\left(\frac13,\frac13,\frac13\right).
\tag{1.6}
\]

The q-weighted reference law is proportional to the prices, hence

\[
Q=\left(\frac16,\frac13,\frac12\right).
\tag{1.7}
\]

Therefore the full within-packet price KL is

\[
\boxed{
D(P\|Q)=\frac13\log_2\frac43.
}
\tag{1.8}
\]

There are only two nontrivial monotone price thresholds. The better one isolates the lowest price and gives

\[
D_{\rm one\mbox{-}tail}
=\frac13+\frac23\log_2\frac45.
\tag{1.9}
\]

The loss is exactly

\[
\boxed{
D(P\|Q)-D_{\rm one\mbox{-}tail}
=\frac13\log_2\frac{25}{24}>0.
}
\tag{1.10}
\]

The source mass of this packet is `3/16`, so the lost credit in the full level KL is exactly

\[
\boxed{\frac1{16}\log_2\frac{25}{24}}
\in(0.003680855565848,0.003680855565849).
\tag{1.11}
\]

This is a genuine Boolean counterexample, not a free probability-law relaxation. It refutes only the universal **one-tail exactness shortcut**. It does not refute (0.1), the full packet/price statistic, the all-gate candidate, or FEI.

## 2. Replacement: exact price-tail hazard ladder

The failure above has an exact replacement that preserves every negative KL credit.

Let `P,Q` be probability laws on an ordered finite price alphabet

\[
\ell_1<\ell_2<\cdots<\ell_r,
\]

with `P` absolutely continuous with respect to `Q`. Define the tails

\[
T_s=\{\ell_s,\ldots,\ell_r\},
\]

and, whenever `P(T_s)>0`, the hazards

\[
a_s=\frac{P(\ell_s)}{P(T_s)},
\qquad
b_s=\frac{Q(\ell_s)}{Q(T_s)}.
\]

Repeated application of the KL chain rule gives the exact identity

\[
\boxed{
D(P\|Q)
=\sum_{s=1}^{r-1}P(T_s)
D_{\rm KL,2}\!\left(\operatorname{Bern}(a_s)\middle\|\operatorname{Bern}(b_s)\right).
}
\tag{2.1}
\]

### Proof

Split the categorical variable into the event `L=ell_1` and its complement. The chain rule gives

\[
D(P\|Q)
=D_2(P(\ell_1)\|Q(\ell_1))
+P(T_2)D(P(\cdot\mid T_2)\|Q(\cdot\mid T_2)).
\]

Repeat inside `T_2`, then `T_3`, and so on. This yields (2.1). No inequality is used.

More generally, after retaining only the first `h` hazards,

\[
D(P\|Q)
=\sum_{s=1}^{h}P(T_s)D_2(a_s\|b_s)
+P(T_{h+1})D(P(\cdot\mid T_{h+1})\|Q(\cdot\mid T_{h+1})).
\tag{2.2}
\]

Thus a truncated price-tail payment is a rigorous lower bound **and the remainder stays explicitly as negative conditional KL**. Nothing is silently dropped.

For the four-bit adversary, the first hazard is exactly the best one-tail term (1.9). The second hazard contributes

\[
\frac23D_{\rm KL,2}\!\left(\operatorname{Bern}(1/2)\middle\|\operatorname{Bern}(2/5)\right)
=\frac13\log_2\frac{25}{24},
\tag{2.3}
\]

recovering the exact loss in (1.10). Hence two nested price hazards recover the full three-price KL exactly.

## 3. The live Numaro source collapses to exactly three binary price hazards

The replacement becomes especially sharp on the B15 live source. Reconstruct the exact 18-variable Numaro truth table with SHA-256

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

Its two influence classes are

\[
j_C=57/256\quad(9\text{ coordinates}),
\qquad
j_A=1/256\quad(9\text{ coordinates}),
\tag{3.1}
\]

so `I=261/128`, `beta=I-1=133/128`, and

\[
q_C=\frac{19}{174},\qquad q_A=\frac1{522}.
\tag{3.2}
\]

At fixed level `k`, the coordinate price is determined by

\[
c=|S\cap\{1,\ldots,9\}|,
\]

the number of high-influence coordinates. Exact Walsh enumeration shows that **every nonzero price-within-magnitude KL contribution is concentrated in exactly three packets**, all with raw Walsh magnitude `1024` (normalized Fourier magnitude `1/256`):

\[
\begin{array}{c|c|c|c}
k & \text{source packet mass} & P(c=k-1,c=k) & Q(c=k-1,c=k)\\ \hline
5 & 351/32768 & (35/39,4/39) & (35/263,228/263)\\
7 & 9/2048 & (7/8,1/8) & (7/64,57/64)\\
9 & 5/32768 & (9/10,1/10) & (3/22,19/22).
\end{array}
\tag{3.3}
\]

Every other `(k,|hat f|)` packet either has one price class or has identical actual/reference price law and therefore zero conditional price KL.

Consequently each live nonzero packet is already binary. One hazard per packet is exact, and

\[
\boxed{
\begin{aligned}
D_{\rm price|mag}
={}&\frac{351}{32768}
D_2\!\left(\frac{35}{39}\middle\|\frac{35}{263}\right)\\
&+\frac9{2048}
D_2\!\left(\frac78\middle\|\frac7{64}\right)\\
&+\frac5{32768}
D_2\!\left(\frac9{10}\middle\|\frac3{22}\right).
\end{aligned}
}
\tag{3.4}
\]

The exact checker encloses

\[
\boxed{
0.032137106754
<\frac{D_{\rm price|mag}}{\beta}
<0.032137106755.
}
\tag{3.5}
\]

This is the same indispensable credit found by B15, but now represented by only **three source-defined binary price-tail hazards**. Since the predecessor certified that magnitude packets alone miss the live target by less than `0.032131617678 beta`, (3.5) is already enough to pay that deficit. Combined with its exact packet term, these three binary hazards recover the same positive live source margin from B15 equation (5.8), about `5.489076953e-6 beta`.

This is a nontrivial compression: the full coordinate-price product is not required on this source, but one universal binary tail is also not enough in general by Section 1. The correct object is the source-defined **tail ladder**, truncated only where the retained residual KL is still carried explicitly.

## 4. Consequence for interface D

The current D-interface can be rewritten without a credit-free interpolation:

1. retain B15's exact magnitude-packet KL;
2. within each magnitude packet, order the finitely many coordinate prices and expand the remaining price KL by (2.1);
3. pay whatever initial hazards arithmetic/valuation controls can reach;
4. leave the final conditional term in (2.2) as a negative KL credit rather than dropping it.

This representation is exact for every finite Boolean source. It turns the vague request for a `price-tail` lower bound into a sequence of binary Bernoulli KL obligations with explicit source masses and no normalization change.

The four-bit gate proves that stopping after a single hazard cannot be exact universally. The Numaro calculation proves that only three binary hazards total are needed on the current near-extremal source. Therefore the next universal obligation is sharply localized: derive source-valid lower bounds on these hazard probabilities/posteriors from valuation or Boolean arithmetic, or exhibit a composition-prime Boolean source whose price alphabet forces an uncontrolled long hazard ladder.

## 5. Exact checker and scope

`check_price_tail_ladder.py` uses only the Python standard library and exact `Fraction` arithmetic, with rigorous atanh-series intervals for logarithms. It verifies:

- the exact four-bit truth table, Walsh spectrum, influences and three-price adversary;
- the strict one-tail loss and its exact value `(1/16) log2(25/24)` after packet weighting;
- the Numaro truth-table hash and influence classes;
- that exactly the three packets in (3.3) carry nonzero price-within-magnitude KL;
- the exact actual/reference rational laws in those packets;
- the interval (3.5), and that it exceeds the predecessor's packet-only deficit threshold.

This run makes no claim of full FEI, universal bounded ladder length, publication priority, or independent peer verification. The new universal price-tail hazard identity is proved analytically; the source-specific Numaro compression and four-bit adversary are machine-checked at the stated exact scope.
