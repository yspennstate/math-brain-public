# B20 / A097 — dual-envelope GU assembly and signed row-mismatch mechanism

Run: 20261020T004530Z-fleet01-B20-a097-signed-row-chi-square-assembly  
Primary packet: A097. Stable gap: G-GU-SIGNED-KL-LOG-NORMALIZATION-LEAF-v2.  
Frozen candidate: for every genuine Boolean f on every finite uniform cube, G(f) <= 4 I(f) + (3/4) U(f).  
Model / effort: GPT-6 / UNKNOWN. Fixed endpoint: 2026-10-21T19:15:57Z, unchanged.

**Outcome: STRICT_REDUCTION_PROVED_GU_OPEN.** This run reconstructs the complete strict dual-envelope reduction from source-bound inputs and changes the mechanism for higher rows. It does not claim universal GU, full FEI, independent acceptance of the new assembly, or native Brain ingestion.

## Mathematical assembly

Let
\[
D_{\ge2}=\sum_i(B_i-\Gamma_i)+\sum_i\sum_{|A|\ge2}K_{i,A},\quad
M_1=\sum_i\min\{p(\varnothing),p(\{i\})\},
\]
\[
W_d=\sum_{|S|=d}p(S),\qquad Q_{\ge3}=I-M_1-W_2
=(W_1-M_1)+W_2+\sum_{d\ge3}dW_d.
\]
For each singleton j, set
\[
r_j=\sum_{i\ne j}p(\{i,j\}),\quad
s_j=\sum_{\substack{|S|\ge3\\j\in S}}p(S),
\]
\[
V_j=\sum_{i\ne j}(p(\{j\})+p(\{i,j\}))
 \log_2\frac{\pi(\{j\})}{p(\{j\})+p(\{i,j\})},
\]
\[
L_j=\sum_{i\ne j}(p(\{j\})+p(\{i,j\}))\log_2\pi(\{j\})\le0,
\quad V_1=\sum_jV_j.
\]
Zero-mass summands are omitted.

The exact signed identity is \(G=D_{\ge2}+K^{(0)}+K^{(1)}\). The sharp root payment is \(K^{(0)}\le(2/\ln2)M_1\). The complete singleton-layer payment gives \(K^{(1)}\le V_1/2+(2/\ln2)W_2\). Thus the independently reviewed high-degree branch is
\[
G\le D_{\ge2}+E_{\rm HD},\quad
E_{\rm HD}=V_1/2+(2/\ln2)(I-Q_{\ge3}).
\]

The corrected rowwise singleton proof gives
\[
\sum_{i\ne j}K_{i,\{j\}}\le
\min\{V_j/2+L_j/2+r_j/\ln2,\ (9/\ln2)(2r_j+s_j)\}.
\]
Consequently
\[
G\le D_{\ge2}+E_{\rm row},\quad
E_{\rm row}=(2/\ln2)M_1+
\sum_j\min\{V_j/2+L_j/2+r_j/\ln2,\ (9/\ln2)(2r_j+s_j)\}.
\]
Both are upper bounds for the same G and retain the same signed remainder, so
\[
\boxed{G\le D_{\ge2}+\min\{E_{\rm HD},E_{\rm row}\}.}
\]
This is a strict reduction relative to either predecessor branch alone. The two branches are alternatives, not additive credits. The signed base, every |A|>=2 KL row, root reserve, normalization cost, and single-use influence accounting remain intact.

For the frozen pair, tensor additivity and the independently reviewed degree-at-most-two theorem reduce the remaining obligation to
\[
\boxed{D_{\ge2}+\min\{E_{\rm HD},E_{\rm row}\}\le4I+\tfrac34U}
\]
only for tensor-prime genuine Boolean functions with R=G-4I-3U/4>0 and Fourier degree at least three. This leaf remains OPEN.

## Exact strictness witness

For the three-bit one-point defect, p(empty)=9/16 and every nonempty Fourier mass is 1/16. Hence I=3/4, M1=3/16, W2=3/16, Q_ge3=3/8; for each j, V_j=1/4, L_j=-1/2, r_j=1/8, s_j=1/16. The old first singleton branch is 0.305336880111..., while retaining L_j/2 gives 0.055336880111.... After the root payment, the old active global branch is 1.457021280667... and the corrected row branch is 0.707021280667...; the exact decrease is 3/4. The high-degree branch equals the old branch on this witness. This is not a GU counterexample.

## Changed mechanism for higher rows

For nonempty A not containing i, set a=fhat(A), b=fhat(A union {i}), m=a^2+b^2, M=pi(A), and
C=sum over T superset A with i notin T of fhat(T)fhat(T union {i}). With alpha=2ab/m and beta=2C/M, the exact row is
K_iA=m D2(Ber((1+alpha)/2) || Ber((1+beta)/2)).
Bernoulli KL <= chi-square/ln2 yields, for |beta|<1,
\[
K_{i,A}\le\frac4{\ln2}
\frac{(abM-Cm)^2}{m(M^2-4C^2)}.
\]
If |beta|=1, one conditional second moment is zero; Cauchy-Schwarz forces the matching child mean to be zero, so both posteriors coincide and K_iA=0. The signed C is retained until the mismatch abM-Cm is formed.

This rowwise bound is proved but not an aggregate payment. No dimension-free bound for the sum of these quotients together with sum_i(B_i-Gamma_i) is established; near-endpoint cancellation and higher-row multiplicities remain unpaid. The changed mechanism is the signed covariance/chi-square mismatch, not a renamed gap.

## Source-verified GU-to-FEI reduction

The actual U-universal referee proof was read. The Boolean G-key lemma uses that d_S f is a multiple of 2^(1-|S|), hence |d_S f| <= 2^(|S|-1)(d_S f)^2. Averaging and Parseval yield |fhat(S)| <= 2^(|S|-1) pi(S). Splitting H=sum p log2(1/pi)+U gives the source inequality H <= 2(I-Var(f))+2U <= 2I+2U.

If universally G<=aI+bU with 0<=b<1, weighted averaging of sum_i Delta_i U=G against sum_i Inf_i=I gives a relevant i with Delta_i U <= (aI+bU) Inf_i/I. Induct on both physical children and set C*=a/(1-b), r=U/I, t=Inf_i/I>0. Then r <= C*(1-t)+(a+br)t = C*+bt(r-C*), so (1-bt)(r-C*)<=0 and U<=aI/(1-b). Therefore H <= (2+2a/(1-b))I. For (4,3/4), this would give U<=16I and H<=34I, conditional on closing GU. Constants and zero masses are separate.

## Bounded delivery reconciliation

- B20/A097 rowwise-min REPORT and proof match canonical and Brain blobs exactly: 48f5caa890472037a6226c3206e8bd32ec3cbbcf and 685ac8300e47a92cda18417e882fe6fad1cfeec8.
- Corrected rowwise-log proof, CHECK.out, and CLAIMS.json exist canonically (5d93539c42b68d1208bd5a9e5f8925a689504b0e; 2a680daf5a19f0827ecac7e968a42bf774dde2ff; 8c17788dec8a5293e5187953d6091b1d6a428eb8) but their designated Brain copies returned NOT_FOUND. Exact copies are included under RECOVERED_ORIGINAL_* in this new run. No missing old REPORT, PROGRESS, delta, source pins, or checker code was fabricated.
- The newer 15 October dual-envelope run is only partially saved: canonical PACKET_DELTA, SOURCE_PINS, COMMANDS and DUAL_ENVELOPE_CHECK exist; its REPORT, CLAIMS, PROGRESS and DUAL_ENVELOPE_ASSEMBLY.tex were NOT_FOUND at both checked destinations. Available partial artifacts are preserved unchanged here. The new assembly is explicitly a reconstruction, not the missing original.
- B02/A006's latest canonical REPORT is only 1001 bytes and states a restricted threshold-family result (blob 6b6104379add591bf6ab005e01e27af729b68f43); its designated Brain REPORT path is NOT_FOUND. The expected full proof/code/check/pins/claims/progress/delta bundle was not found in the bounded check. Its summary is not a universal GU input.
- B08/B13 targeted searches surfaced no newer fleet01 GU-specific run. The existing recovery note (blob a40f586b4ed6b914715aa5e55ecaa2fc91f766dd) says original proof bytes are unavailable; historical statements are not upgraded to accepted universal claims.
- B06/A028 REPORT is not stale in the checked paths: canonical and Brain blobs both equal 24a520e015babc95003835c729d735b1fdcc6db2; its prior receipt records ten nonempty matched files.
- B18/A090 independently accepted the high-degree reserve at its exact scope; B18/A086 independently accepted the degree-two exclusion. The B18/A090 dual-envelope reconstruction repaired the natural-log/base-two issue and is therefore a contributor to the repaired helper, not an independent approver of this assembly.

The established non-held owner request was read. Inbox index/README paths were NOT_FOUND and targeted searches surfaced no current GU-LASER request. The held REQ-2026100617117951 and held 19:38 reroute payload were not opened. No schedule fields were changed, no task was forced or created, and no email, public release, protected-source access, or live-store/graph write was attempted. Native Brain ingestion is NOT OBSERVED.

## Review status and next action

The dual envelope is a source-bound reduction, not universal GU. Full FEI still lacks the universal GU pair and two independent end-to-end reviews. The material normalization repair disqualifies that contributor from independently accepting the repaired helper.

Next action: prove a dimension-free aggregate payment for the signed mismatch quotient together with the exact signed base, or certify the precise failed estimate and pivot mechanism. Keep endpoint-zero rows separate; do not split off the signed base or reuse influence.
