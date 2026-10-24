# Logarithmic Fourier packets and Boolean influence capacity

Research continuation for Yitzchak Shmalo — 20 September 2026.

**Full Friedgut–Kalai FEI is not proved in this continuation.** The new estimates below apply to selected Fourier edges of *every* exactly Boolean function, without restricting its other coefficients. They include a sharp abstract logarithmic packet bound, a physical-influence bound for packets with controlled incidence, and a quantitative obstruction to low-energy Boolean repairs retaining the preceding real counterexample's spectrum. The unresolved step is a dimension-independent payment for all remaining overlapping packets. Sharpness of an abstract scalar bound is not sharpness among Boolean spectra. Independent review, proof-assistant verification, and publication-priority clearance are not claimed.

## 1. Target and conventions

For Boolean f on the uniform cube, put a_S=fhat(S), p_S=a_S^2,

    H(f)=sum_S p_S log_2(1/p_S),
    I_i(f)=Pr[f(x) != f(x+e_i)],
    I(f)=sum_i I_i(f)=sum_S |S|p_S.

Let E(r,s)=r log_2(1+s/r)+s log_2(1+r/s), with continuous zero conventions. Then the retained erasure functional is

    B(f)=sum_i sum_{S not containing i} E(p_S,p_{S+i}).

The earlier erasure reduction shows that a bound B<=K I for every Boolean function would imply full FEI with coefficient K+2/ln 2. It does not give the false pointwise inequality H<=B+(2/ln 2)I. We do not count repeating this reduction as mathematical progress.

The preceding `2026-09-20-booleanity-order` report constructs real, non-Boolean functions that defeat finite-order/small-defect relaxations. Here the Boolean hypothesis is retained exactly. The elementary but essential consequence is

\[
\boxed{|a_S|\le I_j(f)\quad(j\in S).}
\tag{1.1}
\]

Indeed, D_j f=(f-f^{\oplus j})/2 takes values 0,+1,-1, and a_S=E[D_j f chi_S] whenever j is in S. Thus |a_S|<=E|D_j f|=I_j. For real-valued functions the last equality with squared Dirichlet energy fails. Equation (1.1) is a standard Fourier consequence, not claimed new here.

## 2. The sharp abstract logarithmic packet bound

Define, for r>=0,

\[
F(r)=\mathcal E(r^2,1),\qquad
\Theta(r)=
\begin{cases}
2r,&0\le r\le1,\\
F(r),&r\ge1.
\end{cases}
\tag{2.1}
\]

Equivalently, for r>=1,

    F(r)=(1+r^2)log_2(1+r^2)-r^2 log_2(r^2).

The functions in this section concern nonnegative arrays, not necessarily Boolean spectra.

### Lemma 2.1

Theta is the least concave majorant of F on [0,infinity), and is increasing. Moreover

\[
\Theta(r)=2\log_2 r+\frac1{\ln2}+O(r^{-2})\quad(r\to\infty).
\tag{2.2}
\]

**Proof.** First, the binary-entropy inequality h_2(t)<=2 sqrt(t(1-t)) gives F(r)<=2r, with equality at r=0,1. Here is a calculus proof of that inequality, included to avoid an unproved scalar premise. Put x=1-2t in [0,1] and

    q(x)=sqrt(1-x^2)-h_2((1-x)/2).

Its endpoints vanish. The sign of q'(x) is the sign of

    sqrt(1-x^2) atanh(x)/x - ln 2.

The function before minus ln 2 decreases from 1 to 0: its derivative is

    [x-atanh(x)]/[sqrt(1-x^2)x^2] < 0.

Thus q first increases and then decreases to zero, proving q>=0; symmetry handles all t.

For r>0, differentiation gives

    F'(r)=2r log_2(1+r^(-2)),
    F''(r)=[2 ln(1+r^(-2))-4/(1+r^2)]/ln 2.

If r>=1, set u=r^(-2)<=1. The inequality ln(1+u)<=2u/(1+u) follows by differentiation: the difference has derivative (1-u)/(1+u)^2>=0 and vanishes at zero. Therefore F''<=0 on [1,infinity). At r=1, F(1)=F'(1)=2, so the linear part and F join with equal slopes. This proves concavity and monotonicity of Theta. Any concave majorant of F must lie above the chord from (0,0) to (1,2), and above F for r>=1, proving minimality. Finally expand

    F(r)=[ln(1+r^2)+r^2 ln(1+r^(-2))]/ln 2

at infinity. QED.

### Theorem 2.2

For any finite pairs (u_e,v_e) of nonnegative amplitudes, set

\[
E=\sum_e v_e^2,\qquad L=\sum_e u_ev_e,\qquad
\mathcal B=\sum_e\mathcal E(u_e^2,v_e^2).
\]

If E>0, then

\[
\boxed{\mathcal B\le E\Theta(L/E).}
\tag{2.3}
\]

If E=0, B=0. This bound is optimal among unrestricted nonnegative arrays with the prescribed E,L.

**Proof.** Terms with v_e=0 contribute nothing. Weight the remaining ratios r_e=u_e/v_e by v_e^2/E. Since E(u_e^2,v_e^2)=v_e^2 F(r_e), Jensen and Lemma 2.1 give (2.3). For L/E>=1, one pair with v=sqrt(E), u=(L/E)sqrt(E) attains equality. For q=L/E<=1, use the two pairs

    (u_1,v_1)=(sqrt(qE),sqrt(qE)),
    (u_2,v_2)=(0,sqrt((1-q)E)).

They have the stated E,L and entropy 2qE=E Theta(q). These are sharpness examples for arrays, not claims of Boolean realizability. QED.

A simpler consequence, useful without the piecewise function, is

\[
\boxed{\mathcal B\le\frac E{\ln2}+2E\log_2(1+L/E).}
\tag{2.4}
\]

Indeed E(u^2,v^2)<=v^2/ln2+2v^2 log_2(1+u/v), and another Jensen application proves (2.4). This retains logarithmic growth. Replacing it globally by a positive power is already known to fail in this project.

## 3. Matrix packets: a logarithmic and a constant-coefficient payment

Let the first amplitude in each pair depend only on a row z, denoted a_z>=0, and let the second amplitudes be b_zi>=0. Define

\[
A=\sum_z a_z,\quad C=\sum_i\max_z b_{zi},\quad
E=\sum_{z,i}b_{zi}^2,\quad L=\sum_{z,i}a_zb_{zi}.
\tag{3.1}
\]

Then L<=AC. Theorem 2.2 immediately gives

\[
\boxed{\mathcal B\le E\Theta(L/E)\le E\Theta(AC/E).}
\tag{3.2}
\]

Two complementary bounds are

\[
\boxed{\mathcal B\le\min\{2AC,\ 4\sqrt{ACE}\}.}
\tag{3.3}
\]

The first follows from E(a^2,b^2)<=2ab. We prove the second fully.

For all a,b>=0,

\[
\mathcal E(a^2,b^2)\le4a^{1/2}b^{3/2}.
\tag{3.4}
\]

For positive b, put r=a/b. When r>=1,

    F(r)<= [2 ln r+2]/ln2,
    F(r)/sqrt(r) <= 4/(sqrt(e) ln2) <4.

The maximum in the middle is obtained at ln r=1. The last strict inequality follows, for example, from e>9/4 and ln2>2/3. When r<=1, use F(r)=r^2 F(1/r). With x=ln(1/r)>=0,

    F(r)/sqrt(r) <= (2x+2)e^(-3x/2)/ln2 <=2/ln2<4.

Continuous conventions handle zero amplitudes. Now m_i=max_z b_zi gives

\[
\begin{aligned}
\sum_{z,i}a_z^{1/2}b_{zi}^{3/2}
&\le\sum_{z,i}\sqrt{a_zm_i}\,b_{zi}\\
&\le\sqrt{\left(\sum_{z,i}a_zm_i\right)
                 \left(\sum_{z,i}b_{zi}^2\right)}
=\sqrt{ACE}.
\end{aligned}
\]

This proves (3.3). The constant four in (3.4) is a convenient proved constant, not asserted optimal. Most importantly, (3.4) is used only where the row/column capacities can be paid. It is **not** a universal positive-power edge estimate.

## 4. Application to arbitrary Boolean functions, including other high-degree terms

Let C and D be disjoint sets of physical coordinates. Choose distinct nonempty spectral labels C_z contained in C, and consider only the edges

    (C_z, C_z union {i}),       i in D.

For an arbitrary Boolean f, put

    a_z=|fhat(C_z)|,
    b_zi=|fhat(C_z union {i})|.

No other Fourier coefficient of f is assumed zero or restricted. In particular, f may have arbitrary additional high-degree terms involving several control groups, repeated overlaps, and all remaining coordinates.

Let q_zj>=0, supported on j in C_z, with sum_j q_zj=1 for each row. Define the incidence loads

\[
\lambda_j=\sum_zq_{zj},\qquad \Lambda=\max_{j\in C}\lambda_j,
\qquad I_C=\sum_{j\in C}I_j(f),\quad I_D=\sum_{i\in D}I_i(f).
\tag{4.1}
\]

### Theorem 4.1

The selected erasure contribution B_packet obeys

\[
A\le\sum_j\lambda_j I_j(f)\le\Lambda I_C,
\qquad C\le I_D,\qquad E\le1,
\tag{4.2}
\]

and hence

\[
\boxed{
B_{\rm packet}\le E\Theta(AC/E)
\le E\Theta(\Lambda I_CI_D/E),}
\tag{4.3}
\]
\[
\boxed{
B_{\rm packet}\le
\min\{2\Lambda I_CI_D,\ 4\sqrt{\Lambda I_CI_D E}\}
\le2\sqrt\Lambda\,(I_C+I_D).
}
\tag{4.4}
\]

Zero-energy expressions are interpreted as zero.

**Proof.** For each z and j in C_z, (1.1) gives a_z<=I_j. Multiply by q_zj and sum to obtain the bound on A. For each i in D, every coefficient b_zi contains i, so max_z b_zi<=I_i, proving C<=I_D. The labels C_z union {i} are all distinct, since C and D are disjoint. Parseval therefore proves E<=1 even in the presence of arbitrary additional coefficients. Apply Section 3, and use 2 sqrt(I_C I_D)<=I_C+I_D. QED.

A simple admissible load is q_zj=1/|C_z|. Thus arbitrary overlapping centre labels are allowed, with

    Lambda=max_j sum_{z:j in C_z} 1/|C_z|.

This is a controlled-overlap statement, not an assertion that Lambda is universally bounded for every spectral family.

### Disjoint wide centres

If the C_z are pairwise disjoint and each has size at least w, then Lambda<=1/w. Consequently

\[
\boxed{
B_{\rm packet}\le
\min\left\{\frac{I(f)^2}{2w},\ \frac{2I(f)}{\sqrt w}\right\}.
}
\tag{4.5}
\]

This applies to selected coefficients of any Boolean f, not only to functions supported on those stars. It therefore survives adding arbitrary high-degree coefficients, provided the resulting function is still exactly Boolean.

A character-normalized version is available without changing the argument. Choose A_0 so that g=chi_(A_0) f has I(g)=J(f). Apply the theorem to coefficient packets around A_0: the labels are A_0 triangle C_z and A_0 triangle (C_z union {i}). Equation (4.5) then has J(f) in place of I(f). The centres are measured relative to this chosen spectral origin; no assertion is made that the same unshifted packet keeps its old interpretation.

## 5. Two complete erasure bands for every Boolean function

Let B_01 be the contribution from empty-label/singleton edges, and B_12 from singleton/two-element edges. Define

    A_1=sum_i |fhat({i})|,
    C_2=sum_i max_{j!=i}|fhat({i,j})|,
    W_2=sum_{|S|=2} fhat(S)^2.

Equation (1.1) gives A_1,C_2<=I. Each two-element label occurs twice in the matrix of edges, so its E in Section 3 is 2W_2, not W_2. Thus

\[
\boxed{B_{01}\le2|\widehat f(\varnothing)|A_1\le2I,}
\]
\[
\boxed{B_{12}\le\min\{2I^2,\ 4I\sqrt{2W_2}\}.}
\tag{5.1}
\]

There are no hypotheses on coefficients in higher layers. The bound for B_01 is the scalar estimate E(a^2,b^2)<=2ab. The bound for B_12 follows from the matrix theorem with rows j and columns i, and zero diagonal entries. It does not require those row/column coordinate sets to be disjoint; that disjointness was needed only to obtain E<=1 in Theorem 4.1, and here E is accounted for exactly.

These are unconditional estimates for parts of B, not a bound on the remaining layers. Nor does a pointwise bound on B for one function alone imply FEI for that function through the universal erasure reduction. The quantifier over all needed physical restrictions must be retained.

## 6. A quantitative cost for Boolean spectral repairs

The preceding real-valued counterexample used K=4^k disjoint control blocks C_z of size w and coefficients

    Ghat(C_z)=1/(2 sqrt K),
    Ghat(C_z union {i})=+/-1/K,
    I_spectral(G)=w+3/4.

If ANY Boolean function f on those coordinates retains the centre coefficients to a fraction rho, in the sense

    |fhat(C_z)| >= rho/(2 sqrt K)  for every z,

then (1.1), summed over the disjoint control blocks, forces

\[
\boxed{I_C(f)\ge\frac{\rho w\sqrt K}{2}.}
\tag{6.1}
\]

All other coefficients of f may be arbitrary. This is not limited to the thresholding or auxiliary-bit constructions discussed in the predecessor. It is a conditional implication, not an assertion that a Boolean function with all those retained coefficients exists.

For the uniformly close predecessor U=sqrt(1+epsilon G/sqrt K), epsilon=1/(8 sqrt K), its Taylor estimate gives

    |Uhat(C_z)| >= (15/16) epsilon/(4K),
    I_spectral(U) <= (w+3/4)/[256K^2(1-epsilon)].

The first follows from sqrt(1+t)=1+t/2+R, |R|<=t^2/4, E(G/sqrt K)^2=1/K; each Fourier remainder has magnitude at most epsilon^2/(4K), which is at most 1/16 of every retained first-order amplitude. If Boolean f retains these centre lower bounds to fraction rho, then

\[
I_C(f)\ge\frac{15\rho w}{512\sqrt K},
\]
\[
\boxed{
\frac{I_C(f)}{I_{\rm spectral}(U)}
\ge\frac{15\rho}{2}\frac{w}{w+3/4}(1-\varepsilon)K^{3/2}.
}
\tag{6.2}
\]

Thus a Boolean repair preserving a fixed fraction of these specific coefficients cannot preserve the small spectral energy of the real example. This does not rule out unrelated Boolean functions or all possible repairs. The real construction remains a counterexample only to its stated non-Boolean relaxation, not to FEI.

## 7. Full-scope attempts: what works and where aggregation fails

### 7.1 The old addressing obstruction is handled at the right logarithmic scale

The inherited Boolean family has an even number m of address bits, K=2^m data bits, and a tag choosing between a bent address function and the addressed data bit. Its full signed spectrum and exact invariants are in `solo-2026-09-17/ADDRESSING_BARRIER_2026-09-18.md`.

On the DATA edges of that family there are 2K^2 pairs, all with amplitudes

    a=1/(2 sqrt K), b=1/(2K).

For this packet,

    A=sqrt K, C=1/2, E=1/2, L=sqrt K/2.

Theorem 2.2 is exact, giving

\[
B_{\rm data}=\tfrac12\Theta(\sqrt K)
=\frac{(K+1)\log_2(K+1)-K\log_2K}{2}.
\tag{7.1}
\]

In contrast, summing the power term a^(1/2)b^(3/2) gives K^(1/4)/2, while I=(m+2)/2. The latter ratio diverges. This is the PRE-EXISTING positive-power obstruction, not a new counterexample. The new logarithmic packet estimate recovers the exact data cost rather than reviving the false power target. The centres of the whole address packet are heavily overlapping and include the empty label, so the controlled-incidence payment in Section 4 is not asserted for that packet.

### 7.2 The universal allocation has not been proved

For a disjoint partition of all oriented Fourier edges into packets, their child energies satisfy sum E_packet<=I. Theorem 2.2 would close the erasure route if one could prove

    sum_packets E_packet Theta(L_packet/E_packet) <= C I

with a universal C and a suitable choice of packets for every Boolean function. We have NOT proved this. Merely writing this requirement is not a new theorem about full FEI.

Using only bounded-incidence packets can reuse the same physical influences many times. Using one large packet loses the distribution of amplitude ratios. The scalar power replacement is already false globally, so its local proof cannot be summed without its actual capacity hypotheses. The first two erasure bands do not control arbitrary higher layers. Exact Booleanity supplies (1.1), but that coefficientwise consequence alone is not asserted to imply the universal bound.

The previous shifted-threshold theorem also explains why even a coordinatewise mean-overlap bound must be treated cautiously: it gives O_i/I_i growing at least as c ln n. Applied only through Theta(O_i/I_i), the ratio of that upper envelope to I_i diverges at least on the log log n scale at every coordinate, despite that symmetric family satisfying FEI by its separate certificate. This is a consequence of the inherited overlap obstruction and (2.2), not a new FEI counterexample or a claim that the exact B_i grows at that rate.

### 7.3 Other current-turn checks not promoted to proofs

An exploratory test of the proposed improvement Delta_i H<=4j_i for j_i>=1/4 failed already for the three-variable one-point defect: its ratio is approximately 4.86766874675. No such improvement is used in this report. This is not claimed as a new counterexample or record. The calculation used floating-point entropy and is kept only in the worklog, not as an exact new certificate.

The newest repository's Reed–Muller centroid candidate was read and considered; no all-dimensional proof or counterexample was obtained here. It remains unproved and is not a premise. Its first-layer consequence alone would not settle the weighted Fourier entropy problem, as the source worklog already explains.

## 8. Actual exact checks

Run `python verify_packets.py`. The checker needs Python 3.10+ and NumPy. It uses integer Walsh transforms, Fraction arithmetic, 48-term rational atanh-series logarithm enclosures, and exact prime-logarithm cancellation for equality cases. There is no floating-point tolerance deciding any asserted inequality.

Executed checks:

- All 65,812 Boolean functions in dimensions one through four, with 2,100,292 coefficient/influence assertions.
- 197,136 canonical singleton-control/data packets, and 65,808 checks of the first two erasure bands. The latter excludes the one-bit functions, where the second band is empty.
- 490 seeded packets in dimensions four through ten; 350 have overlapping centres and 83 have every centre of width at least two. There are 5,231 positive selected edges in these sampled packets.
- 1,089 integer-amplitude scalar comparisons.
- The actual seven-variable inherited addressing truth table, plus six evaluations of its analytic parameter formulas. Large address dimensions are not truth-table enumerations.
- Ten rational evaluations of the spectral-retention consequence (6.2).

Across the packet families 848 distinct signatures were verified; caching duplicate signatures is explicitly not an additional independent check. All assertions passed. An initial serialization attempt encountered a NumPy integer type after all assertions; it was corrected by converting the counter to a Python integer. It was not a mathematical failure or an ignored failed inequality.

The report's all-dimensional claims rest on Sections 2--6, not finite extrapolation. The original Booleanity checker was separately replayed and its output compared with the actual preceding ZIP: byte-identical, output SHA256 `eb112aa3e80a68b9a8592f24460bd0c2326ade0ef284cf1b39d1bde44924581a`. No independent audit or proof assistant was used.

## 9. Sources and precise provenance

Read in this continuation:

- Actual conversation `FEI_Exact_Booleanity_2026-09-20.md`, all 560 source lines, and the accompanying ZIP. Its real/Boolean distinction and coefficient lower bounds are retained. Its original GitHub non-delivery wording describes that session, not a claim about this session's tools.
- Current `proofnet24/P03-fei/README.md`, blob `d226f1c4a460a0f90ba25f40a8a6b6a8d03ab2e9`, including the affine-symmetric theorem and all retained scope warnings.
- `continuations/2026-09-20-affine-symmetric-stopping/REPORT.md`, main proof through Section 6: its hypotheses and scalar binary-entropy bound were reconstructed. The rest was not needed as a premise.
- `continuations/2026-09-20-affine-symmetric-stopping/WORKLOG.md`, blob `3e98b23319d234477d890e6ffdead574bfc251d2`, read in full; its centroid candidate stays unproved.
- `solo-2026-09-17/runs/2026-09-18T00-18-56Z_logarithmic-criticality.md`, blob `d3455cf9e3cfc054075a171033f1f88f362e864c`, and `solo-2026-09-17/ADDRESSING_BARRIER_2026-09-18.md`, blob `c1e52dff50095854d85c20e8b13a5385d91efaca`, both read in full. These prevent using a globally false power allocation and supply the previously proved addressing example.

Primary literature checked on 20 September 2026: Gonzalez, MacManus and Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246v2, last revised 9 June 2026, https://arxiv.org/abs/2606.00246 . Its restriction/stopping-tree method is prior art. Guy Shalev, *On the Fourier Entropy Influence Conjecture for Extremal Classes*, arXiv:1806.03646v2, https://arxiv.org/abs/1806.03646 , already treats bounded spectral L1 norm and extremal classes. We do not relabel those results as new.

Searches did not establish priority for this packet formulation. Standard entropy homogeneity, concave envelopes, Cauchy–Schwarz, and the coefficient bound (1.1) are credited as standard ingredients. The additions here are their complete packet formulation, controlled-incidence application with arbitrary other coefficients, and the explicit spectral-retention consequence. They do not yield an unrestricted representation or allocation theorem.

**Final mathematical status:** the all-dimensional statements proved here are (2.3), (3.2)--(3.3), (4.3)--(4.5), (5.1), and (6.1)--(6.2), with their stated hypotheses. The universal finite supremum B(f)/I(f) over Boolean functions is not bounded in this work. No schedules, permissions, repository visibility, or unrelated research ownership are changed by this report.
