# fleet02/B14 — a uniform three-dimensional physical MUX tube around the exact zero-credit lines

**Classification:** `ESSENTIAL_STEP_APPLIED / PHYSICAL_TERMINAL_SELECTOR / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Fresh authenticated repository controls and scientific sources were consumed directly; no installed/native brain receiver context entered the derivation.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Novelty/priority:** unverified; no publication-priority claim.

## 0. Compact universal chain and first missing implication

The fixed Campaign-A candidate is

\[
C^\dagger=6.521851214,\qquad C_0=6.4548,\qquad
 a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(z)=\Gamma_0(z)+a^\dagger z(1-z).
\tag{0.1}
\]

The current all-gate reformulation says that

\[
D_{\Gamma^\dagger}(G;p)\ge0
\tag{0.2}
\]

for every composition-prime Boolean gate and every interior product bias implies the full uniform-cube FEI with constant `C^dagger`; the exact gate-composition cocycle then handles decomposable gates. The old AND/decomposable-extremality shortcut has already been refuted and is not used here.

The newest Campaign-A lead consumed here is the completed fleet01/B18 report

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260922T052537Z-zero-credit-mux-line/REPORT.md`

(blob `f7af04e2de78fc5f865af853cb9afce2473ca34e`). It proves the exact zero-selector-credit scalar frontier for the one-address-bit MUX. The named completed **other-account** structural input used here is fleet04/B18

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B18/20260922T045533Z-mux-joint-credit-collapse/REPORT.md`

(blob `5a73f11de979258f558b2ca2ae08483b9a7f3632`). It gives the exact six-mass biased-Walsh law, the exact MUX gate defect, and the rigidity

\[
\mathcal C_A=0
\iff t=\frac12\quad\text{and}\quad
(q_0=\tfrac12\ \text{or}\ q_1=\tfrac12).
\tag{0.3}
\]

The A lead closes the two one-dimensional lines (0.3), but explicitly leaves their three-dimensional neighbourhood and then the rest of the unequal-MUX cube open. **The first missing implication attacked in this run is therefore a source-valid, quantitative tube around those exact zero-credit lines.**

The result below gives such a tube with a fixed dimension-free width and a strictly positive physical terminal decrement.

## 1. Exact MUX form used

Let

\[
M(A;D_0,D_1)=\begin{cases}D_0,&A=0,\\D_1,&A=1,\end{cases}
\]

with independent biases
\[
t=\Pr(A=1),\qquad q_0=\Pr(D_0=1),\qquad q_1=\Pr(D_1=1),\]
put `q=1-t`,
\[
V_z=4z(1-z),\qquad
r=qq_0+tq_1,\qquad
d=q_0+q_1-2q_0q_1,
\tag{1.1}
\]
and abbreviate
\[
B(z)=\Gamma^\dagger(z)+h_2(V_z).
\tag{1.2}
\]

The fleet04/B18 exact Fourier table gives
\[
\boxed{
D_{\Gamma^\dagger}(M)
=dB(t)+qB(q_0)+tB(q_1)-\Gamma^\dagger(r)-H(w),
}
\tag{1.3}
\]
where the six spectral masses are
\[
\begin{aligned}
w_\varnothing&=(1-2r)^2,\\
w_A&=V_t(q_1-q_0)^2,\\
w_0&=q^2V_{q_0},\qquad w_1=t^2V_{q_1},\\
w_{A0}&=tqV_{q_0},\qquad w_{A1}=tqV_{q_1}.
\end{aligned}
\tag{1.4}
\]
All terms in this run therefore come from one actual Boolean MUX source; no arbitrary probability-law relaxation is substituted.

## 2. A uniform reserve on the exact zero-credit line

Fix the line
\[
t=\frac12,\qquad q_0=\frac12,\qquad q_1=s\in[0,1].\]
Fleet01/B18 proves
\[
D_{\Gamma^\dagger}(M;\tfrac12,\tfrac12,s)
=Z(s)
:=C^\dagger-2+\frac12\Gamma^\dagger(s)
-\Gamma^\dagger\!\left(\frac14+\frac{s}{2}\right)>0.
\tag{2.1}
\]
Its proof is quantitative enough to retain a uniform reserve. Specifically:

* `Z(0)=0.0167628035>1/64`;
* on `0<=s<=1/50`, its source-segment lower proxy has derivative `>2.8826172255` and starts at `Z(0)`;
* on `1/50<=s<=1/10`, its lower envelope is increasing and starts above `0.0479544`;
* on `1/10<=s<=1/2`, its concave lower envelope has endpoint values above `0.26545` and `0.31596`;
* `Z(s)=Z(1-s)`.

Consequently the completed lead theorem gives the stronger convenient form
\[
\boxed{Z(s)>\frac1{64}\qquad(0\le s\le1).}
\tag{2.2}
\]
This reserve is the resource thickened below; no selector-information credit is counted a second time.

## 3. Source-potential bounds needed for stability

The h96 source facts used by the A lead are, on the small side `0<z<=1/2`,
\[
\Gamma_0(z)=zG(\log_2(1/z)),
\quad G(1)=12.9096,
\quad |G'|<31,
\tag{3.1}
\]
and with `alpha=4.9096<5`,
\[
G(x)-\alpha x\le8.629.
\tag{3.2}
\]
The derivative in a source interpolation segment is
\[
\Gamma_0'(z)=G(x)-\frac{G'(x)}{\ln2}.
\tag{3.3}
\]
Continuity across source nodes turns any uniform segmentwise derivative bound below into a global Lipschitz bound on the stated interval.

Set
\[
\varepsilon:=2^{-14}=\frac1{16384}.
\tag{3.4}
\]

### Lemma 3.1 — center Lipschitz bound
If `|z-1/2|<=eps`, then
\[
|\Gamma^\dagger(z)-C^\dagger|<60\varepsilon.
\tag{3.5}
\]

**Proof.** By symmetry use the small representative `z_*>=1/2-eps`. Then
\[
x=\log_2(1/z_*)<1.001
\]
(the elementary bound `-ln(1-y)<=y/(1-y)` with `y=2eps` suffices). Hence
\[
|G(x)|<12.9096+31(0.001)<12.941.
\]
Using `1/ln2<3/2` and `a^dagger<0.269`, (3.3) gives
\[
|(\Gamma^\dagger)'|<12.941+46.5+0.269<60.
\]
This proves (3.5). `square`

### Lemma 3.2 — output Lipschitz bound
If `z` lies within `eps+eps^2` of `[1/4,3/4]`, then
\[
|(\Gamma^\dagger)'(z)|<91
\tag{3.6}
\]
in the global Lipschitz sense.

**Proof.** The small representative is at least `1/4-eps-eps^2`, so the same logarithmic estimate gives `x<2.001`. Therefore
\[
|G(x)|<12.9096+31(1.001)<43.941,
\]
and (3.3) gives
\[
|(\Gamma^\dagger)'|<43.941+46.5+0.269<91.
\]
`square`

### Lemma 3.3 — crude global input-price bound
For every `s in [0,1]`,
\[
0\le B(s)<9.
\tag{3.7}
\]

**Proof.** By symmetry take `s<=1/2`. From (3.2), `alpha<5`, and
\[
s\log_2(1/s)\le\frac1{e\ln2}<\frac9{16},
\]
we get
\[
\Gamma_0(s)<5\frac9{16}+8.629\frac12<7.128.
\]
The quadratic lift is at most `a^dagger/4<0.068`, so `Gamma^dagger(s)<7.196`; adding `h_2(V_s)<=1` gives (3.7). `square`

## 4. Main theorem — a full three-dimensional tube

### Theorem 4.1
For every `s in [0,1]`, if
\[
\left|t-\frac12\right|\le2^{-14},
\qquad
\left|q_0-\frac12\right|\le2^{-14},
\qquad q_1=s,
\tag{4.1}
\]
then
\[
\boxed{
D_{\Gamma^\dagger}(M;t,q_0,s)
>\frac{9}{8192}>\frac1{1000}.
}
\tag{4.2}
\]
By exchanging the two data inputs and complementing the address bit, the same conclusion holds with `q_0` and `q_1` interchanged. Thus throughout
\[
\boxed{
\left|t-\frac12\right|\le2^{-14},\qquad
\min\left\{\left|q_0-\frac12\right|,
\left|q_1-\frac12\right|\right\}\le2^{-14},
}
\tag{4.3}
\]
the live MUX defect is strictly positive.

### Proof
Write
\[
t=\frac12+\tau,\qquad q_0=\frac12+e,
\qquad |\tau|,|e|\le\varepsilon,
\tag{4.4}
\]
and let `r_0=1/4+s/2` be the output bias on the exact line. From (1.1),
\[
d=\frac12+e(1-2s),
\tag{4.5}
\]
so `d>=1/2-eps`, and
\[
r-r_0=\frac e2+\tau\left(s-\frac12-e\right),
\tag{4.6}
\]
so
\[
|r-r_0|\le\varepsilon+\varepsilon^2.
\tag{4.7}
\]

We compare (1.3) with its exact-line value (2.1).

**Address price.** By Lemma 3.1 and nonnegativity of `h_2`,
\[
B(t)\ge\Gamma^\dagger(t)>C^\dagger-60\varepsilon.
\]
Together with (4.5),
\[
dB(t)>rac12C^\dagger-(30+C^\dagger)\varepsilon.
\tag{4.8}
\]
Since `C^dagger<6.522`, the adverse loss here is `<36.522 eps`.

**First data price.** Similarly `q=1-t>=1/2-eps` and Lemma 3.1 give
\[
qB(q_0)>rac12C^\dagger-(30+C^\dagger)\varepsilon,
\tag{4.9}
\]
another loss `<36.522 eps`.

**Second data price.** Lemma 3.3 gives
\[
tB(s)\ge\frac12B(s)-9\varepsilon.
\tag{4.10}
\]

**Output potential.** Lemma 3.2 and (4.7) give
\[
-\Gamma^\dagger(r)
\ge-\Gamma^\dagger(r_0)-91(\varepsilon+\varepsilon^2).
\tag{4.11}
\]

It remains only to control the six-mass entropy continuously without assuming positivity of individual masses. Let `w^0` be (1.4) at `(t,q_0)=(1/2,1/2)`. Directly from (1.4), (4.4), and (4.7),
\[
\begin{array}{c|c}
\text{mass}&|w-w^0|\text{ upper bound}\\ \hline
\varnothing&4\varepsilon+4\varepsilon^2\\
A&\varepsilon+5\varepsilon^2\\
0&\varepsilon+3\varepsilon^2\\
1&\varepsilon+\varepsilon^2\\
A0&2\varepsilon^2\\
A1&\varepsilon^2
\end{array}
\tag{4.12}
\]
and hence
\[
\|w-w^0\|_1\le7\varepsilon+16\varepsilon^2.
\tag{4.13}
\]
Thus their total variation `theta` obeys
\[
\theta<4\varepsilon=\frac1{4096}.
\tag{4.14}
\]
Fannes--Audenaert on a six-symbol alphabet gives
\[
|H(w)-H(w^0)|
\le h_2(\theta)+\theta\log_2 5
\le\theta\log_2\frac{5e}{\theta}.
\tag{4.15}
\]
Since `e<3` and
\[
15\cdot4096=61440<2^{16},
\]
(4.14)-(4.15) imply
\[
|H(w)-H(w^0)|<64\varepsilon.
\tag{4.16}
\]

Combining (4.8)-(4.11) and (4.16), and using `eps=2^-14`, the entire adverse perturbation is strictly less than
\[
\bigl(2(36.522)+9+91(1+\varepsilon)+64\bigr)\varepsilon
<238\varepsilon.
\tag{4.17}
\]
The base reserve (2.2) therefore yields
\[
D_{\Gamma^\dagger}(M;t,q_0,s)
>\frac1{64}-238\varepsilon
=\frac{9}{8192}
>\frac1{1000}.
\tag{4.18}
\]
This proves the first half. Swapping `D_0,D_1` and replacing `A` by `1-A` preserves the Boolean MUX and sends `t` to `1-t`, so the same bound applies around the second zero-credit line. `square`

## 5. Physical selector and terminal values

The operation behind Theorem 4.1 is exactly the physical singleton reveal of the address coordinate `A`. The two children are the unary literals `D_0` and `D_1`, with their original data biases. For a unary literal `L` at any bias,
\[
D_{\Gamma^\dagger}(L)=0,
\tag{5.1}
\]
because `It/V=1`, the output bias equals the input bias, and the biased spectral entropy is exactly `h_2(V)`.

Hence (4.2) is a **one-step physical selective decrement with zero terminal debit**:
\[
D_{\Gamma^\dagger}(M)
-(1-t)D_{\Gamma^\dagger}(D_0)
-tD_{\Gamma^\dagger}(D_1)
>\frac1{1000}.
\tag{5.2}
\]
No prescribed-coordinate statement is asserted for arbitrary Boolean functions. No crossing, selector information, or posterior credit is reused: the starting reserve (2.2) is the already-complete exact-line all-gate defect, and the present argument only pays its perturbation.

## 6. Before/after and exact remaining implication

The last three substantive B14 mechanisms before this run were:

1. `20260922T0145Z-js-poincare-currency`: globally paid the coherent restriction bill in exact Poincare currency;
2. `20260922T0502Z-block-envelope-collapse`: showed unsigned block erasure/currency envelopes cannot beat the best singleton, forcing signed/exact credits;
3. `20260922T052850Z-balanced-mux-equal-data-collar`: used the exact negative posterior-entropy reserve to pay a relative unequal-data collar at balanced address.

This run is not another scalar-threshold scan. It consumes the newer fleet01/B18 closure of the exact zero-credit frontier and uses a different **uniform stability/Fannes mechanism** to thicken that frontier in *both* transverse directions at once.

**FULL-PROBLEM CHANGE:** none. Full FEI remains open.

**MECHANISM CHANGE:** yes. Before this run the exact zero-selector-credit MUX lines were closed only at
\[
t=1/2,\qquad q_0=1/2\text{ or }q_1=1/2.
\]
After this run the whole fixed-width three-dimensional neighbourhood (4.3) is closed with explicit physical terminal margin `>1/1000`.

The first MUX implication still unpaid is now the complement of the accumulated safe tubes. In particular, any MUX counterexample to the live candidate must satisfy
\[
\boxed{
\left|t-\frac12\right|>2^{-14}
\quad\text{or}\quad
\left(
\left|q_0-\frac12\right|>2^{-14}
\ \text{and}\ 
\left|q_1-\frac12\right|>2^{-14}
\right),
}
\tag{6.1}
\]
in addition to avoiding the previously closed equal-data and complementary-data/address tubes. On compact subsets separated from the two exact zero-credit lines, fleet04/B18 guarantees a positive selector-information floor by continuity, but a quantitative comparison with the source-potential loss is still required; compactness alone is not a proof.

Beyond MUX, the universal obligation remains
\[
D_{\Gamma^\dagger}(G;p)\ge0
\tag{6.2}
\]
for every composition-prime Boolean gate and every interior product bias.

## 7. Verification, literature status, and truth labels

The adjacent checker verifies only the exact arithmetic in the perturbation ledger:

* `eps=1/16384`;
* the six-mass bounds imply total variation `<1/4096`;
* `15*4096<2^16` gives the stated six-symbol entropy coefficient;
* `1/64-238/16384=9/8192>1/1000`.

It returned `PASS`. This is a sanity check for constants; the theorem-sized claim rests on the analytic proof above.

A fresh public-source check on 2026-09-22 found no universal FEI proof. González--MacManus--Pereyra (arXiv:2606.00246, 2026-05-29) still present the restriction-decrement/stopping-tree inequality as a conditional route and establish selected classes, while Potapov's arXiv:2609.21563 (2026-09-18, updated 2026-09-21) proves FEI for plateaued and partially bent classes rather than for all Boolean functions. This bounded search is status evidence, not a novelty proof.

**Truth labels:**

* **PROVED in this report:** Theorem 4.1 and the physical terminal interpretation (5.2), conditional only on the already-committed source-candidate numerical/slope facts explicitly cited in Sections 2-3.
* **OPEN:** full unequal-data MUX cube; arbitrary composition-prime all-gate inequality; full uniform-cube FEI.
* **NOT CLAIMED:** publication novelty or priority.

A scoped privacy/secret review of the changed scientific files found no credentials, scheduler identifiers, machine paths, raw transcripts, benchmark gold, unrelated private data, or publication action.
