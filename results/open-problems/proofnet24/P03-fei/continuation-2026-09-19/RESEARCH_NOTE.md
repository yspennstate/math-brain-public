# FEI continuation: corrected entropy budgets and restriction-resistant coding

19 September 2026. **Full FEI is not proved.** This note distinguishes a certified finite counterexample, analytical obstructions, and an exact reduction. It does not claim publication novelty or independent review.

> Delivery clarification, added during recovery on 19 September 2026: the mathematical text below is the saved research note from the earlier session. Section 6's failed-delivery statement describes that earlier session, not a permanent repository or fleet limitation. This note is now being preserved through the connected GitHub contents API. The original local ZIP also contains the referenced checker scripts and outputs; do not infer that those separate files were uploaded merely from the presence of this note. See the latest P03 handoff for the exact delivered-file inventory. This preservation is not a new independent mathematical audit.

## 1. Definitions and the actual universal target

For Boolean \(f:\mathbb F_2^n\to\{-1,1\}\), put
\[
a_S=\widehat f(S),\quad p_S=a_S^2,\quad
H(f)=\sum_Sp_S\log_2(1/p_S),\quad I(f)=\sum_S|S|p_S.
\]
The empty atom is included. Define
\[
j_i=\min(I_i,1-I_i),\quad J=\sum_i j_i,\quad
 t_{ij}=\tfrac14\Pr[f(x)f(x+e_i)f(x+e_j)f(x+e_i+e_j)=-1],\quad t_i=\sum_{j\ne i}t_{ij},\quad R=\sum_i\frac{j_i^2}{j_i+t_i}.
\]
Terms with zero denominator are zero. Character multiplication preserves entropy and minimizes influence to \(J\).

For uniform \(z\), write \(g_z(x)=f(x)f(x+z)\) and
\[
D_\times(f)=2H(f)-\mathbb E_zH(g_z).
\]
An admissible single-coordinate quotient restricts coordinate \(r\) with \(z_r=1\). Translation invariance of \(g_z\) makes this restriction preserve spectral entropy. All quotient choices below may depend on the entire shift.

The September 18 erasure reduction [B] remains the direct full-scope target. With spectral random vector \(S\), let
\[
B(f)=\sum_i H(S_i\mid S_{-i}),\quad
K_E=\sup_f\frac{B(f)}{I(f)},\quad C_{\rm FEI}=\sup_f\frac{H(f)}{I(f)}.
\]
Then \(K_E\le C_{\rm FEI}\le K_E+2/\ln2\), as an implication about universal constants. The pointwise assertion \(H(f)\le B(f)+(2/\ln2)I(f)\) is **not** justified and is explicitly corrected in [C]. No finite bound on \(K_E\) has been obtained here.

## 2. A nine-variable counterexample to the archived constant-eight drift proposal

Use the archived potentials
\[
\mathcal P(f)=\sum_i\psi(j_i),\qquad
\mathcal L(f)=\sum_i\frac{j_i^2\log_2(1/j_i)}{j_i+t_i},
\]
where \(\psi(s)=s-s^2\ln(1/s)\) for \(0<s\le1/8\), continued by its tangent line for \(1/8\le s\le1/2\), and \(\psi(0)=0\). The natural logarithm in \(\psi\) and base-two logarithm in \(\mathcal L\) must not be interchanged.

For a quotient rule \(Q\), let
\[
\Delta_Q\mathcal P=2\mathcal P(f)-\mathbb E\mathcal P(Q_zg_z),\qquad
\Delta_Q\mathcal L=2\mathcal L(f)-\mathbb E\mathcal L(Q_zg_z).
\]
The archived proposed inequality was \(D_\times\le4\Delta_Q\mathcal P+2\Delta_Q\mathcal L\). Its finite exploratory tests were not a universal proof [A].

**Certified counterexample.** On nine bits, take
\[
f(z,y_1,\ldots,y_8)=(-1)^{z\sum_{1\le i<j\le8}y_i y_j}.
\]
All phase arithmetic is modulo two. For every admissible single-coordinate quotient rule,
\[
D_\times(f)-4\Delta_Q\mathcal P(f)-2\Delta_Q\mathcal L(f)
\;>\;0.174606321217.
\]
The directly computed optimal residual is enclosed by
\[
[0.174606321218,\;0.174606321219].
\]
The certificate also encloses
\[
H(f)\in[5.975923544661,5.975923544662],\quad J(f)=79/32,
\]
\[
D_\times(f)\in[6.955753339323,6.955753339324],
\]
while the **largest possible** right side over all quotient rules is in
\([6.781147018104,6.781147018105]\).

**Certificate construction.** `checks/certify_nine_variable.py` constructs the actual 512-entry Boolean truth table, computes integer Walsh transforms, evaluates every one of the 512 shifts and every one of the 2,304 admissible quotients, and checks the exact spectral-mass bijections. Each quotient's actual lower-dimensional truth table is used, rather than assuming a formula for its potential. For each shift the script encloses the maximum quotient gain and sums these enclosures. Because a rule chooses independently within the admissible coordinates of each shift, this maximizes over every deterministic rule; randomization cannot improve it.

Accepted comparisons use rational arithmetic only. To enclose logarithms, reduce the argument to \(1\le q\le2\), set \(u=(q-1)/(q+1)\), and use
\[
\ln q=2\sum_{j=0}^{M-1}\frac{u^{2j+1}}{2j+1}+E_M,
\quad0\le E_M\le\frac{2u^{2M+1}}{(2M+1)(1-u^2)},\quad M=64.
\]
The other assertions are finite integer or rational identities. This is a reproducible computational certificate, not an independent audit.

**Scope.** This disproves that proposed drift estimate. It does not disprove FEI, rule out larger coefficients, or rule out a different potential or a multiple-coordinate quotient.

## 3. Majority forces a logarithmic marginal payment

Let \(f=\operatorname{Maj}_n\) for odd \(n=2r+1\ge3\). Put \(b_r=4^{-r}\binom{2r}{r}\). Then
\[
j_i=b_r,\qquad t_{ij}=b_r/2,\qquad
R(f)=\frac{2n b_r}{n+1},\quad\sum_i j_i^2=n b_r^2.
\]
In particular \(R+\sum_i j_i^2<4\). Nevertheless,
\[
D_\times(\operatorname{Maj}_n)\ge\frac{\log_2 n-6}{1728}
\qquad(n\ge65\text{ odd}). \tag{1}
\]
Thus no finite universal constant can make \(D_\times\le C(R+\sum_i j_i^2)\) true.

### Proof of the lower bound

For independent spectral samples \(S,T\), let \(U=S\triangle T\). Drawing a spectral sample from \(g_z\) and forgetting its shift gives the law of \(U\), by Parseval in \(z\). Consequently
\[
D_\times=H(S\mid U)+I(z;U)\ge H(S\mid U). \tag{2}
\]
The mutual information here uses the derivative-mixture coupling, not the independent-samples coupling.

Conditional on its size, the spectral sample of majority is uniform. Its exact level weights are
\[
\Pr(|S|=2s+1)=\frac{n b_r b_s b_{r-s}}{2s+1},\qquad0\le s\le r. \tag{3}
\]
To derive (3), differentiate majority in one coordinate. The derivative is that coordinate times the indicator that the other \(2r\) signs sum to zero. On a balanced sign vector, the expected product of \(2s\) specified coordinates is \((-1)^s\binom r s/\binom{2r}{2s}\), obtained by comparing coefficients of \((1-t^2)^r\). Squaring the resulting coefficient and multiplying by \(\binom n{2s+1}\) gives (3).

The recurrence \(b_{r+1}/b_r=(2r+1)/(2r+2)\) proves
\(1/(2\sqrt r)\le b_r\le1/\sqrt{r+1}\) for \(r\ge1\). For a dyadic integer \(a\ge1\) with \(64a^2\le n\), (3) therefore gives
\[
\Pr(2a+1\le |S|\le4a-1)\ge\frac1{36\sqrt a}. \tag{4}
\]
Indeed sum (3) over \(a\le s\le2a-1\); the three lower bounds on the \(b\)'s give each summand at least \(1/(16\sqrt2\,a^{3/2})\).

Given sizes \(k,l\) in that band, independence and the union bound give
\(\Pr(S\cap T=\varnothing\mid k,l)\ge1-kl/n\ge3/4\). Conditional additionally on disjointness and \(U\), the set \(S\) is uniform among the \(k\)-subsets of \(U\), so its entropy is \(\log_2\binom{k+l}{k}\ge\min(k,l)\ge2a\). The dyadic band events are disjoint. Conditioning further can only decrease entropy, so each band contributes at least
\((3/4)(2a)/(36^2a)=1/864\) to (2). There are at least \((\log_2n-6)/2\) such bands. This proves (1).

The displayed pivotal formulas follow by inspecting the threshold faces. The same Wallis bounds give \(R\le2/\sqrt{r+1}\) and \(n b_r^2<2\). More generally, for every fixed \(0\le\beta<1\),
\[
R+\sum_i j_i^2[\log_2(1/j_i)]^\beta=O((\log n)^\beta),
\]
so (1) also refutes every such sublogarithmic budget.

For completeness, \(D_\times=O(\log n)\) follows as well. Equation (3) gives \(\Pr(|S|\ge u)\le C/\sqrt u\): sum the \(s\le r/2\) terms using their \(O((s+1)^{-3/2})\) bound, and sum the remaining terms using \(O(((r+1)\sqrt{r-s+1})^{-1})\). Let \(K=|S|,L=|T|,A=|S\cap T|\). Conditional on \(K,L,A,U\), the choice of \(S\) costs at most
\[
\log_2\binom nA+\log_2\binom{K+L}{K}.
\]
Here \(\mathbb EA=n b_r^2<2\), so the first expectation is \(O(\log n)\). For the second, split \(\min(K,L)\) into dyadic bands \([2^h,2^{h+1})\), and \(\max(K,L)\) into bands with upper scale \(2^{h+d+1}\). The cost is \(O((d+2)2^h)\), and independence and the tail bound give probability \(O(2^{-h-d/2})\). Summing over \(d\ge0\) and \(h\le\log_2n\) gives \(O(\log n)\). Encoding \((K,L,A)\) also costs only \(3\log_2(n+1)\). Thus \(H(S\mid U)=O(\log n)\). The archived Walsh-uncertainty identity [A, B00f] gives \(D_\times\le2H(S\mid U)\), proving the upper bound.

## 4. An asymptotically lossless, restriction-resistant coding reduction

**Proposition.** Given a Boolean \(g\) on \(N\) bits and a binary matrix \(A\in\mathbb F_2^{r\times N}\), define
\[
F(x,z)=g(x+A^Tz),\qquad C(s)=(s,As).
\]
Then the nonzero Fourier coefficients are exactly
\(\widehat F(C(s))=\widehat g(s)\), and
\[
H(F)=H(g),\qquad I(g)\le I(F)\le I(g)+r. \tag{5}
\]
If the systematic code \(C\) has minimum distance greater than \(d\), every physical restriction fixing \(a\le d\) coordinates preserves spectral entropy exactly. In every resulting restriction, every block of \(b\) spectral coordinates with \(a+b\le d\) is determined by its complement. Its conditional block entropy is therefore zero.

**Proof.** Expand \(g\) in characters to obtain the coefficient formula. The additional \(r\) marginal influences are each at most one, giving (5). Distinct codewords remain distinct after deleting any \(a\le d\) coordinates. Restriction therefore changes each nonzero coefficient only by a sign; it does not merge coefficients. After deleting another \(b\) coordinates with \(a+b\le d\), injectivity still holds. This proves both the entropy preservation and the conditional-entropy statement. Surviving coordinate influences are also preserved for each assignment, not just on average.

Such codes exist with redundancy \(r=O(d\log(N/d))=o(N)\) whenever \(d=o(N)\). For a random matrix \(A\), \(As\) is uniform for every nonzero \(s\). The expected number of nonzero codewords of weight at most \(d\) is at most
\[
2^{-r}\sum_{j=0}^d\binom{N+r}{j}. \tag{6}
\]
Take \(r=\lceil2d\log_2(2eN/d)\rceil+2\). Eventually \(r\le N\), and the elementary Hamming-ball bound makes (6) less than one. Therefore some matrix has no such codeword. This is an existence proof; efficient deterministic construction with these exact parameters is not asserted.

Now fix any nonconstant Boolean seed \(h\), apply the construction to \(g=h^{\otimes q}\), and let \(q\to\infty\). Its dimension is \(N=q\dim h\), so \(r=o(q)\). Equation (5) gives
\[
\frac{H(F)}{I(F)}\longrightarrow\frac{H(h)}{I(h)}.
\]
Consequently a dimension-free FEI bound on this restriction-resistant class would imply full FEI **with the same constant**. This sharpens a factor-two parity-lift reduction and shows why local erasure vanishing, even after a sublinear number of restrictions, does not remove the universal difficulty. It is a reduction, not a solution.

`raw_work/robust_coding_certificate.py` checks a systematic [8,4,4] example on 320 distinct Boolean seeds, 41,280 physical restrictions, 3,031,040 signed coefficient identities, and 387,840 zero block-erasure tests. These exact finite checks support the identities; (6) supplies the all-dimensional argument. An earlier progress message gave 318 seeds; the saved final certificate reports 320.

## 5. A surviving logarithmic candidate and its necessary constant

Let \(Q_{\log}=\sum_i j_i^2\log_2(1/j_i)\). The estimate
\[
D_\times\le K(R+Q_{\log}) \tag{7}
\]
is **unproved**. The majority obstruction does not refute it. For the complete quadratic phase on even \(m\) coordinates, direct Walsh calculation gives
\[
D_\times=2m,\quad R=m/(m+1),\quad Q_{\log}=m/4.
\]
Thus any universal \(K\) in (7) must satisfy
\[
K\ge\sup_{m\text{ even}}\frac{8(m+1)}{m+5}=8.
\]
The exploratory script made 843 evaluations and found no violation of \(K=8\); those floating computations do not prove (7). Even a proof of (7) would require a further valid telescoping payment for its right side before it could finish FEI. The failed constant-eight drift inequality in Section 2 must not be substituted for that missing payment.

## 6. Sources, reading coverage, and original session delivery status

[A] `FEI_research_handoff_2026-09-13.pdf`, 136 pages: the complete extracted text was read, including root marginal and phase notes, A01–A15, B01–B13, lead notes, numerical records, and continuation queues. Relevant parts include the root potential, the exploratory drift proposal, and B00f's uncertainty identity.

[B] `proofnet24/P03-fei/solo-2026-09-17/ERASURE_REDUCTION.md`, Git blob `770f1fc8438b360549ed89480cb260768d839923`.

[C] `research_pushes/2026-09-18-sidorenko-fei-ising/FEI.md`: prior correction separating universal constants from a false pointwise inequality.

[D] The 1,506-page `FEI_complete_research_record_2026-09-13.pdf` was recovered from the actual September 13 backup email, with its original PDF and full extracted text saved. Recovery and extraction are not the same as a complete line-by-line mathematical review. This session has **not established exhaustive reading of every page of that volume or every scheduled-worker report**.

[E] Additional directly read September 18 repository notes include `FINAL_HANDOFF`, `README`, `COMPOSITION_AND_BARRIERS`, `ADDRESSING_BARRIER`, `SIGNED_BALANCE_AND_LINEAR_BASIS_BARRIER`, `BLOCK_RESTRICTION_IDENTITY`, `ERASURE_SYNERGY_AND_DUALITY`, `INTERFERENCE_PATCHING_THEOREM`, `BOUNDED_COLLISION_PARITY_MULTIPLEXERS`, `NAND_LOG_POTENTIAL`, and `UNEQUAL_NAND_CONTRACTION`. Their date-stamped filenames are preserved in the repository. Prior obstructions are not reclassified as new results.

The original local package preserves all new local scripts and recorded outputs under `raw_work/`. Their exploratory metadata is not an independent audit and is not itself a proof of additional universal claims. The direct nine-variable certificate in `checks/` and the proofs in Sections 3–4 are the principal continuation results.

**Historical delivery record from the earlier session:** GitHub was not changed during that session. The assistant reported that the available GitHub connector exposed read actions but no write action, and that a local `git ls-remote` attempt failed because `github.com` could not be resolved. An add-only patch and intended P03 handoff paths were supplied. That report did not establish a fleet-wide permission problem. In this subsequent recovery, GitHub `create_file`, `update_file`, `create_blob`, `create_tree`, `create_commit`, and `update_ref` actions are exposed. No new schedule is created or modified by preserving this note.
