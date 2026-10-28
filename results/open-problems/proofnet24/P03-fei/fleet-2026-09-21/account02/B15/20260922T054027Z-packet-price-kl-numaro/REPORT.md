# account02/B15 — packet/coordinate-price KL exactly recovers the ordered-occurrence loss; Numaro kills coefficient four

**Run:** `20260922T053227Z-account02-B15-r13`  
**Classification:** `ESSENTIAL_NEGATIVE_CREDIT / BOOLEAN_OBSTRUCTION / LIVE-SOURCE_PAYMENT`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Control, live target, and comparison with the last three B15 reports


\[
C_*=6.5218512,
\]

with full missing implication `D_{Gamma_*}(G;p)>=0` for every finite composition-prime Boolean gate and every interior product bias. On a balanced gate at uniform bias this is exactly

\[
D_*(f)=C_*[I(f)-1]-H(f)\ge0. \tag{0.1}
\]

The newest B-lead report read for this run is account03/B18 `20260922T051809Z-finite-pattern-fourier-dust/REPORT.md`, observed blob `a85d8993f9536d933ec796dcb9356293564c470e`; it closes bounded finite signed point-defect dilution at every balanced center `C>4` and leaves the universal all-gate inequality open.

The last three substantive account02/B15 reports before this run were:

1. `20260922T011717Z-iterated-shared-graft`: exact shared-graft lower-bound construction;
2. `20260922T015258Z` partial-branch renormalization: fixed-point lower-bound construction and exhaustion of that fixed operator;
3. `20260922T040227Z-balanced-stop-kl-fusion`: harmonic stopping plus exact root/deletion KL fusion, leaving the occurrence-entropy implication unpaid.

They do **not** leave one identical unpaid implication for three consecutive runs, so the forced-three-run pivot rule is not triggered here. This run stays on the Shannon/relative-entropy interface and replaces a lossy data-processing step by an exact packet/coordinate-price credit.

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`. No universal FEI constant is proved.

**MECHANISM CHANGE:** `ordered-occurrence KL -> distinctness event only` is replaced by `ordered-occurrence KL -> exact level mismatch KL -> exact spectral-magnitude-packet plus original-coordinate price decomposition`. On the actual near-extremal Numaro source, the discarded KL is quantitatively indispensable.

## 1. Named completed other-account result actually consumed

The completed result consumed substantively is account04/B17

`proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T041638Z-ordered-occurrence-collision/REPORT.md`,

observed blob `61dadb04377a950e5c39798eed5702b6115f138d`.

For a balanced Boolean function, with spectral sample `S`, level `K=|S|`, level law `W_k`, influence marginals `j_i=Pr(i in S)`, total influence `I=sum_i j_i`, and normalized occurrence law `q_i=j_i/I`, that report proves the exact ordered-occurrence identity

\[
H(f)=I H_2(q)+H(K)-\mathbb E\log_2(K!)-D_{\rm ord}, \tag{1.1}
\]

and then data-processes `D_ord` through the event that iid `q`-draws are all distinct. This gives the sufficient collision remainder

\[
H(f)\le H(K)+C_{\rm coll}(f),\qquad
C_{\rm coll}:=I H_2(q)+\mathbb E\log_2 e_K(q), \tag{1.2}
\]

where `e_k(q)` is the `k`th elementary symmetric polynomial. The peer's finite atlas suggested a natural coefficient-four candidate for `C_coll/(I-1)` but did not prove it.

This run keeps the exact KL discarded by (1.2), identifies a sufficient statistic for that KL in the spectral-packet/original-coordinate language, and then evaluates the resulting exact budget on the genuine 18-variable Numaro Boolean source.

## 2. Exact level-KL identity

For every `k` with `W_k>0`, let

\[
\pi_k(A)=\Pr(S=A\mid K=k)=\frac{\widehat f(A)^2}{W_k},\qquad |A|=k, \tag{2.1}
\]

and define the `q`-weighted without-replacement reference law

\[
\nu_k(A)=\frac{\prod_{i\in A}q_i}{e_k(q)},\qquad |A|=k. \tag{2.2}
\]

If `W_k>0`, then every set in the support of `pi_k` uses only coordinates with positive `q_i`, so (2.2) is legitimate on the source support. Put

\[
D_{\rm lev}:=\sum_k W_k D_{\rm KL,2}(\pi_k\|\nu_k). \tag{2.3}
\]

### Theorem 2.1 — exact collision/KL recombination

For every balanced Boolean `f`,

\[
\boxed{
H(f)=H(K)+C_{\rm coll}(f)-D_{\rm lev}.
} \tag{2.4}
\]

Moreover

\[
\boxed{
C_{\rm coll}
=\sum_i j_i\log_2\frac1{j_i}
+\mathbb E\log_2 e_K(j),
} \tag{2.5}
\]

where `e_k(j)` is the elementary symmetric polynomial in the actual influence marginals.

### Proof

For fixed `k`, expanding the KL in (2.3) gives

\[
\begin{aligned}
D_{\rm KL,2}(\pi_k\|\nu_k)
&=-H(\pi_k)
-\sum_{A:|A|=k}\pi_k(A)\sum_{i\in A}\log_2q_i
+\log_2 e_k(q).
\end{aligned}
\]

Hence, if `m_{i,k}=Pr(i in S | K=k)`,

\[
H(\pi_k)
=-\sum_i m_{i,k}\log_2q_i
+\log_2e_k(q)
-D_{\rm KL,2}(\pi_k\|\nu_k). \tag{2.6}
\]

Multiply by `W_k` and sum. Since `sum_k W_k m_{i,k}=j_i=I q_i`, the first term becomes `I H_2(q)`. Since `H(S)=H(K)+sum_k W_k H(pi_k)`, (2.4) follows. Finally `q_i=j_i/I`, `e_k(q)=I^{-k}e_k(j)`, and `E K=I`; the two `I log_2 I` terms cancel, proving (2.5). No inequality and no FEI input occurs in this derivation. QED.

Equivalently, if `P_k` is the peer's uniformly ordered version of `pi_k`, then the KL chain rule through the `all draws distinct` event is exact:

\[
D_{\rm KL,2}(P_k\|q^{\otimes k})
=-\log_2[k!e_k(q)]+D_{\rm KL,2}(\pi_k\|\nu_k). \tag{2.7}
\]

Thus `D_lev` is exactly the negative information credit lost by the distinctness-only data processing in (1.2).

## 3. Spectral packet + original-coordinate price is a sufficient statistic for the entire lost KL

For a `k`-set `A`, define the physical occurrence-price product

\[
L_q(A):=\prod_{i\in A}q_i, \tag{3.1}
\]

and the spectral magnitude packet label

\[
M(A):=|\widehat f(A)|. \tag{3.2}
\]

Let

\[
T_k(A):=(M(A),L_q(A)). \tag{3.3}
\]

This retains actual Fourier magnitude packets and an additive original-coordinate cost `-log_2 L_q(A)=sum_{i in A} log_2(1/q_i)`; it assumes no physical projection integrality.

### Theorem 3.1 — packet/price sufficiency

For every balanced Boolean `f` and every `k` with `W_k>0`,

\[
\boxed{
D_{\rm KL,2}(\pi_k\|\nu_k)
=D_{\rm KL,2}((T_k)_\#\pi_k\|(T_k)_\#\nu_k).
} \tag{3.4}
\]

### Proof

On the source support,

\[
\frac{\pi_k(A)}{\nu_k(A)}
=\frac{|\widehat f(A)|^2 e_k(q)}{W_k\prod_{i\in A}q_i}. \tag{3.5}
\]

The likelihood ratio depends only on `(M(A),L_q(A))`. Therefore every fibre of `T_k` has identical conditional law under `pi_k` and `nu_k`; equivalently the conditional KL term in the chain rule is zero. This proves (3.4). QED.

If coordinates are partitioned into classes on which `q_i` is constant, `L_q(A)` is determined by the vector of original-coordinate class counts. Thus (3.4) can be implemented without collapsing the coordinate geometry to an invariant linear change of basis.

There is a second exact nonnegative split. Let `D_mag` denote the KL after keeping only the magnitude packet `M`, and let `D_price|mag` be the conditional price KL. Then

\[
\boxed{D_{\rm lev}=D_{\rm mag}+D_{\rm price|mag}.} \tag{3.6}
\]

This is the requested mass-weighted negative-relative-entropy payment in literal spectral-packet/original-coordinate currency.

## 4. Genuine Boolean obstruction: the coefficient-four collision payment is false

The source table is reconstructed exactly from the committed Numaro source checker

`proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260921T181108Z-numaro-magnitude-flow-certificate/check_numaro_magnitude_flow_certificate.py`,

observed blob `df90e544f471b9053aa864522d64302d0c8a3f9e`. Its reconstructed truth-table SHA-256 is

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

The source is balanced. Exact integer Walsh calculation gives two influence classes:

\[
j_1=\cdots=j_9=\frac{57}{256},\qquad
j_{10}=\cdots=j_{18}=\frac1{256}, \tag{4.1}
\]

so

\[
I=\frac{261}{128},\qquad \beta:=I-1=\frac{133}{128}. \tag{4.2}
\]

The exact level law is

\[
\begin{array}{c|ccccccccc}
k&1&2&3&4&5&6&7&8&9\\ \hline
W_k&14625/32768&2187/8192&651/4096&675/8192&441/16384&105/8192&9/2048&9/8192&5/32768.
\end{array} \tag{4.3}
\]

Using exact rational arithmetic and rigorous atanh-series enclosures for every logarithm, the committed checker proves

\[
\boxed{4.767785544317<\frac{C_{\rm coll}}\beta<4.767785544318,} \tag{4.4}
\]

so the peer's coefficient-four collision candidate is false on a genuine balanced Boolean source.

More strongly, after refunding **all** of `D_lev`,

\[
\boxed{4.582933632790<\frac{H-H(K)}\beta<4.582933632791.} \tag{4.5}
\]

Therefore even

\[
C_{\rm coll}-D_{\rm lev}\le4\beta \tag{4.6}
\]

is false. The obstruction is not an artefact of dropping only the level-mismatch KL: this hard source has conditional spectral entropy `H(S|K)>4 beta` by itself. This does **not** refute FEI; it refutes the proposed coefficient `4` at this Shannon interface.

## 5. The same source shows exactly why the negative packet/price credit must be spent

For the Numaro source, the normalized occurrence law has

\[
q_C=\frac{19}{174}\quad(9\text{ coordinates}),\qquad
q_A=\frac1{522}\quad(9\text{ coordinates}). \tag{5.1}
\]

At fixed level `k`, the price `L_q(A)` is therefore determined by the count `c=|A cap {1,...,9}|`. The packet/price statistic can be taken as `( |hat f(A)|, c )`. The exact KL split (3.6) is certified as

\[
\boxed{0.152714804773<\frac{D_{\rm mag}}\beta<0.152714804774,} \tag{5.2}
\]

\[
\boxed{0.032137106754<\frac{D_{\rm price|mag}}\beta<0.032137106755,} \tag{5.3}
\]

and hence

\[
\boxed{0.184851911527<\frac{D_{\rm lev}}\beta<0.184851911528.} \tag{5.4}
\]

The packet-plus-price pushforward recovers `D_lev` exactly, not merely numerically: within each `(k, magnitude, price)` cell, both `pi_k` and `nu_k` are uniform, so the likelihood-ratio sufficiency proof in Theorem 3.1 applies.

Now insert this into the actual balanced-uniform all-gate defect at the B-lead center `C_*=6.5218512`:

\[
\frac{D_*}{\beta}
=C_* -\frac{H(K)}\beta-\frac{C_{\rm coll}}\beta
+\frac{D_{\rm mag}}\beta+\frac{D_{\rm price|mag}}\beta. \tag{5.5}
\]

The exact checker gives

\[
-0.184846422451
< C_* -\frac{H(K)}\beta-\frac{C_{\rm coll}}\beta
< -0.184846422450. \tag{5.6}
\]

So dropping the negative information credit makes this actual near-extremal gate look decisively **unsafe**. Restoring only the magnitude-packet KL is still insufficient:

\[
-0.032131617678
< C_* -\frac{H(K)}\beta-\frac{C_{\rm coll}}\beta+\frac{D_{\rm mag}}\beta
< -0.032131617677. \tag{5.7}
\]

Only after spending the original-coordinate price-within-packet KL as well does the true margin emerge:

\[
\boxed{
0.000005489076953
<\frac{D_*}{\beta}
<0.000005489076954.
} \tag{5.8}
\]

Thus this hard source is a concrete demonstration of the exact owner/user warning: **spectral magnitude packets alone are not enough; the negative information credit tied to original-coordinate prices is essential.** No physical projection integrality is assumed anywhere.

## 6. What changed and the first missing implication now

### Target-level movement

`OPEN -> OPEN`. The universal all-gate inequality is still unpaid. No subclass result is presented as full FEI.

### Mechanism-level movement

The distinctness-only collision bridge loses a KL term that is not negligible at the near-extremal source. The loss has now been recovered exactly and compressed to the source-valid statistic

\[
(|\widehat f(S)|,\prod_{i\in S}q_i), \tag{6.1}
\]

or, equivalently, magnitude packet plus original-coordinate occurrence price. On the Numaro gate, magnitude packets pay about `0.1527148 beta`, while the price refinement pays another `0.0321371 beta`; both are needed to recover a positive live defect of only about `5.49e-6 beta`.

### First missing Shannon implication

For the balanced-uniform slice of the live all-gate candidate, the exact source-facing inequality is

\[
\boxed{
H(K)+C_{\rm coll}-D_{\rm pp}\le C_*[I-1],
} \tag{6.2}
\]

where `D_pp` is the **explicit packet/price KL** from (3.4), equal to `D_lev`. Equation (6.2) is not claimed as new closure; it is the precise all-gate balanced defect written with the indispensable negative credit exposed rather than dropped.

A useful non-tautological next step is therefore to lower-bound a **coarser source-exact part of `D_pp`** from packet arithmetic/valuation and original-coordinate price tails, while preserving the remaining conditional KL as negative credit. Any proposed universal payment must pass the Numaro budget (5.6)--(5.8): losing more than about `5.49e-6 beta` of the exact combined credit already destroys the live certificate on this source. The coefficient-four collision shortcut is permanently retired.

The newest account01/B12 handoff at the control snapshot independently closes the dyadic selector tail for the B0 gate by retaining child slack; it is compatible with this conclusion and does not pay (6.2). The B lead's finite-pattern-dust theorem likewise removes a different adversary class but leaves the all-gate quantifier open.

## 7. Checker scope and exactness

`CHECKER.py` reconstructs the 18-variable source, checks its truth-table digest, performs an integer FWHT over all `2^18` inputs, derives exact rational level masses and influences, constructs exact elementary symmetric polynomials and packet/price cells, and encloses every logarithm by rational atanh series with an explicit tail bound. It independently checks the two computations of `D_lev` agree to far below the reported interval widths.

The captured output is `PASS` and establishes only this finite source calculation. Theorem 2.1 and Theorem 3.1 are analytic identities for every balanced Boolean source.

## 8. Literature applicability check

A current primary-source check still has unrestricted FEI open. Potapov's 18 September 2026 paper proves FEI for plateaued functions (sharp class constant `4`) and partially bent functions (sharp class constant `2`), not for arbitrary Boolean functions. González--MacManus--Pereyra give restriction/stopping-tree partial progress, and Li--Han's information-theoretic inequality retains an influence-profile entropy term. No novelty or priority claim is made here for the packet/price identity or the Numaro calculation.

## 9. Provenance and privacy

Changed files for this run contain only FEI mathematics, public bibliographic metadata, logical account/slot labels, source-bound repository paths/hashes, and deterministic scientific checker material. They contain no credentials, scheduler identifiers, machine paths, raw transcripts, benchmark gold, unrelated private data, email/Drive actions, paid/remote model calls, workflows, or permission changes. The Numaro hex constants are inherited scientific source data already committed in the private research repository; they are not authentication material.
