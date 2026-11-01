# B01 / A003 — minimal universal endpoint interfaces

Run: `20261011T210729Z-fleet01-B01-minimal-target-a003`  
Primary packet: `A003` (Minimal target formulation)  
Stable gaps: `G-J-COST`, `G-R-SELECT`, `G-BOOLEANITY`  
Status: **PROVED synthesis pending independent review; full FEI remains OPEN**

## 1. Exact bounded objective and movement

The previous state contained three valid but separately stated routes: the conditioned posterior-forest residual, existential restriction selection, and full signed Booleanity. The tracked quantity was the first dimension-independent constant actually needed on each route; none was bounded.

This run freezes all three interfaces with every quantifier, proves an exact constant sandwich for the restriction/erasure route, and proves a second constant sandwich for the signed downward functional. The new mathematical statement is

\[
 C_{\rm FEI}\le C_{\rm step}\le C_{\rm FEI}+\frac2{\ln2},
 \qquad
 C_L\le C_{\rm FEI}\le C_L+\frac3{\ln2}.
\]

Thus the existential physical-coordinate step target and the full-signed downward target are source-valid finiteness equivalences, with explicit additive losses. This is a sharper implication map, not a bound on any of the constants. The posterior-forest target remains only a structurally stronger sufficient condition; no converse from FEI is claimed.

The exact proofs and endpoint definitions are in `ENDPOINT_INTERFACES.tex`. `OPEN_LEMMAS.json` records the unpaid leaves.

## 2. Conventions

Let \(f:\{-1,1\}^n\to\{-1,1\}\), let \(S\) have law \(P_f(A)=\widehat f(A)^2\), and put

\[
 H(f)=H(S),\qquad I(f)=\mathbb E|S|,\qquad \alpha_i=I_i(f)=\Pr(i\in S).
\]

For a relevant coordinate \(i\) (meaning \(\alpha_i>0\)), let \(f_{i,+},f_{i,-}\) be the two physical restrictions and define

\[
 \Delta_iH(f)=H(f)-\tfrac12\{H(f_{i,+})+H(f_{i,-})\}.
\]

All logarithms are base two. Empty terms use \(0\log(1/0)=0\).

## 3. PROVED: restriction-step equivalence with constants

Write \(E_i=H(1_{\{i\in S\}}\mid S\setminus\{i\})\). If \(a_T=\widehat f(T)\) and \(b_T=\widehat f(T\cup\{i\})\), then the two child spectral laws are \(r_\pm(T)=(a_T\pm b_T)^2\), their midpoint is \(q(T)=a_T^2+b_T^2\), and direct entropy expansion gives

\[
 \Delta_iH=E_i+\operatorname{JS}(r_+,r_-).
\]

The scalar inequality

\[
 \frac{(1+t)\log_2(1+t)+(1-t)\log_2(1-t)}2
 \le \frac{1-\sqrt{1-t^2}}{\ln2},\quad |t|\le1,
\]

applied with \(t=2a_Tb_T/(a_T^2+b_T^2)\), yields

\[
 0\le\operatorname{JS}(r_+,r_-)
 \le\frac2{\ln2}\sum_T\min(a_T^2,b_T^2)
 \le\frac2{\ln2}\min\{\alpha_i,1-\alpha_i\}.
\]

Also

\[
 I(f)-\tfrac12\{I(f_{i,+})+I(f_{i,-})\}=\alpha_i.
\]

Define

\[
 C_{\rm step}=\sup_{f\ {m nonconstant}}
 \min_{i:\alpha_i>0}\frac{\Delta_iH(f)}{\alpha_i}.
\]

If \(C_{\rm step}\le K\), strong induction on the number of relevant coordinates chooses the stated relevant coordinate and telescopes the last two displays, giving \(H(f)\le K I(f)\). Hence \(C_{\rm FEI}\le C_{\rm step}\).

Conversely, \(B(f):=\sum_iE_i\le H(S)\), because in any fixed order
\(H(S_i\mid S_{-i})\le H(S_i\mid S_1,\ldots,S_{i-1})\). If FEI holds with \(C\), then \(B(f)\le CI(f)\), so some relevant \(i\) has \(E_i\le C\alpha_i\). The JS estimate gives \(\Delta_iH\le(C+2/\ln2)\alpha_i\). Therefore

\[
 C_{\rm FEI}\le C_{\rm step}\le C_{\rm FEI}+2/\ln2.
\]

The relevant-coordinate clause is essential: irrelevant coordinates have \(\alpha_i=E_i=\Delta_iH=0\) and otherwise make the selector vacuous.

## 4. PROVED: full-signed downward endpoint

For a signed Boolean Fourier vector \(a_A=\widehat f(A)\), Booleanity is exactly

\[
 \sum_Aa_A^2=1,
 \qquad
 \sum_Aa_Aa_{A\triangle U}=0\quad(\varnothing\ne U\subseteq[n]).
\]

Put \(p_A=a_A^2\) and

\[
 L(f)=\sum_Ap_A\sum_{i\in A}\log_2\left(1+\frac{p_{A\setminus\{i\}}}{p_A}\right),
\]

with a zero contribution when \(p_A=0\). Pairing \(T\) and \(T\cup\{i\}\) gives

\[
 L_i\le E_i\le L_i+\alpha_i/\ln2,
 \qquad L\le B\le L+I/\ln2.
\]

The second inequality is just \(x\log_2(1+y/x)\le y/\ln2\). Let \(C_L\) be the least universal constant in \(L(f)\le C_LI(f)\) over signed arrays satisfying the complete Boolean autocorrelation system. Since \(L\le B\le H\), FEI implies \(C_L\le C_{\rm FEI}\). Conversely a universal \(L\le KI\) gives \(B\le(K+1/\ln2)I\), hence the preceding restriction proof gives FEI with \(K+3/\ln2\). Thus

\[
 C_L\le C_{\rm FEI}\le C_L+3/\ln2.
\]

This target is not valid for arbitrary probability laws; it must use the complete signed autocorrelations. Finite-prefix and unsigned relaxations remain excluded by the registered `FIXED_CONV_PREFIX` and `FIXED_CAP_PREFIX` obstructions.

## 5. CONDITIONED posterior-forest interface (exact, still unpaid)

For every admissible ordered gate representation, incidence weights \(\lambda\), and for every nonempty spectral set \(A\) a probability law \(\mathcal P_A\) on distinct actual finite partition-forest runs producing \(A\), set

\[
 \mathcal J_f=
 v(\Lambda+\log_2 Z)+
 \sum_{A\ne\varnothing}P_f(A)
 \left[\mathbb E_{r\sim\mathcal P_A}B_\lambda(A;r)-H(\mathcal P_A)\right].
\]

Here \(v=\operatorname{Var}(f)\), \(\Lambda=\sum_l\log_2(1+\lambda_l\pi_l)\), and \(Z=1-2^{-\Lambda}\). The source theorem proves

\[
 H(f)\le h_2(v)+K_{\rm ref}I(f)+\mathcal J_f,
 \qquad K_{\rm ref}=3+2\log_2 3+\log_2(6e).
\]

Therefore the exact sufficient target

\[
 \exists K<\infty\ \forall n\ \forall f\ \exists
 (\text{representation},\lambda,(\mathcal P_A)_A):
 \quad \mathcal J_f\le KI(f)
\]

implies FEI with constant \(2+K_{\rm ref}+K\). Both \(v\log Z\) (root conditioning) and \(-H(\mathcal P_A)\) (posterior witness erasure) are part of the target. Dropping either changes the route. FEI alone does not prove that this forest class contains an efficient reference, so no reverse arrow is asserted.

## 6. Mandatory falsifiers and tensor admission

### Disjoint tensors and near tensors

For \(F(x,y)=f(x)g(y)\) on disjoint variables,

\[
 H(F)=H(f)+H(g),\quad I(F)=I(f)+I(g),\quad L(F)=L(f)+L(g).
\]

For a coordinate in the \(f\)-factor, \(\Delta_iH(F)=\Delta_iH(f)\) and \(I_i(F)=I_i(f)\); similarly for \(g\). Hence tensor powers preserve the factor's local step ratios and the weighted \(L/I\) ratio. Neither minimal endpoint excludes an arbitrary seed by tensoring. The forest target also quantifies over every tensor power, but no factorized optimal forest is assumed.

### Actual prime Boolean gate

For the two-bit AND sign (three outputs \(+1\), one output \(-1\)), all four Fourier masses equal \(1/4\). Thus

\[
 H/I=2,\qquad B/I=2,\qquad L/I=1,
 \qquad \min_i\Delta_iH/I_i=4.
\]

This calibrates the additive gaps and shows that the local restriction constant need not equal the global FEI ratio even in arity two.

### Addressing/multiplexer

For the whole-set addressing function, \(H=2a\), \(I=1+a/2\). The recovered forest calculation shows the coordinatewise pressure can be quadratic while one-root whole-forest accounting retains posterior/root savings and is \(O(I)\). This is why `WF(K)` uses complete actual runs and posterior entropy rather than coordinatewise witness costs.

### Sparse one-point defects and rare restrictions

The accepted B05 family and its new control-first extension have a selector packet divided by its influence asymptotic to \(k+\log_2 e\). Revealing activation controls first transports this debt rather than paying it. Our `STEP(K)` is existential, not every-coordinate, and our forest residual retains logarithmic and posterior terms; neither contradicts that no-go. Any proposed proof of `STEP(K)` must still identify another relevant coordinate or a global mechanism on this family.

### Biased prime-gate endpoint

The independently reviewed B09 lemma retains the product-biased correction. B19's proved-pending-review AND family has \(J_A-M_A=4q(1-2q)p\log_2(1/p)+O_q(p)\), so a scalar biased correction cannot be \(O(p)\). The interfaces here keep the complete entropy decrement or complete forest cost and do not replace rare logarithms by a pointwise linear tax.

## 7. Exact implication graph and unpaid leaves

Proved arrows:

1. `WF(K)` \(\Rightarrow\) `FEI(2+K_ref+K)`.
2. `STEP(K)` \(\Rightarrow\) `FEI(K)`.
3. `FEI(C)` \(\Rightarrow\) `STEP(C+2/ln 2)`.
4. `DOWN(K)` \(\Rightarrow\) `FEI(K+3/ln 2)`.
5. `FEI(C)` \(\Rightarrow\) `DOWN(C)`.

Open leaves, with no circular arrows:

- `G-J-COST`: prove `WF(K)` for one dimension-independent \(K\), including normalizer, root conditioning, ranks, labels, and posterior entropy.
- `G-R-SELECT`: prove `STEP(K)` for one dimension-independent \(K\), or an amortized complete-tree statement that implies it without spending influence twice.
- `G-BOOLEANITY`: prove `DOWN(K)` from the complete signed autocorrelation system; truncated or unsigned constraints are insufficient.

These are alternative full-FEI endpoints. Proving any one closes full FEI; this run proves only their exact logical placement.

## 8. Source pins and review state

- Recovered forest theorem: `reports/fei-2026-10-11/source_material/reductions/paper/forests.tex`, blob `3fd08d81a2bcd96acaaa268757c7f343e71e8249`.
- Three-routes audit: `proofnet24/P03-fei/continuations/2026-10-02-selection-obstructions/three_routes.md`, blob `29f8b421d3e29ab2ad00073fa27893fc591118b4`.
- Campaign plan: `reports/fei-2026-10-11/FEI_100_agent_research_plan.tex`, blob `a20c0ae48779a27dd899425f80dc33160a86eed9`.
- B05 control-first rare-log no-go: run `20261011T202804Z-fleet01-B05-rare-restrictions-a023`, report blob `4b02b427aaf3f2d683a4ec195c9b747976035272`.
- B19 biased-composition review: run `20261011T204627Z-fleet01-B19-b09-composition-review-a091`, report blob `8fd7bba68fcea917fb5f53a8084b305fd7d1f854`.

The constant-sandwich synthesis is analytically proved here but has not received independent A086/A094 review. No computation was needed; all statements are exact symbolic identities and inequalities. Full FEI remains open.

## 9. Concrete handoff

A086/A094 should independently reconstruct the two scalar bounds used above: the JS/minority-mass inequality and \(L_i\le E_i\le L_i+\alpha_i/\ln2\). Then check the induction at constant children and the tensor formulas. If accepted, A003-D1/D2 can be retired as a source-complete endpoint interface. B01 should next move to A001 or A005 and audit whether any claimed future route actually proves one of the three unpaid universal constants without reusing the consequence it is meant to establish.
