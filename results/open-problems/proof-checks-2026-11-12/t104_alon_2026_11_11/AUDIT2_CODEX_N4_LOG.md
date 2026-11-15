# Referee log

Task: “You are refereeing a short mathematical note” — received 2026-11-11, work started 07:25 +04 (Asia/Tbilisi).

## Setup
Read-only inspection outside this folder is permitted; all writes stay here. No brain, mesh, checklist, hook, memory, math-store or git mutation will be made, as required by the specific instructions for this run. No browsing and no agents. Compute state reports CPU saturation without distress; numerical work will use one thread, nice 10, small matrices, and a hard runtime limit below five minutes. No code outside this folder will be read or reused for numerical checks.

## Step 1 — match to the paper: CORRECT, with an extraction limitation
The note uses nonnegative weights, L(G,nu)=sum w_ij(I-rho_nu((ij))), the smallest eigenvalue on the whole Specht module (including zero), sigma dominating tau, and 2/3. This is the paper's conjecture. Dominance means sum_{i<=r} sigma_i >= sum_{i<=r} tau_i for each r. Equal partitions are harmless if included.

Paper lines used (line numbers in ALON_2610.22151.txt):
- 24: “Let G = ([n], wij) be a weighted graph with nonnegative weights.”
- 30–37: “Here min(G,  ) means the minimum eigenvalue of the Laplacian matrix” / “L(G,  ) =  ( wij(id - (ij)))” / “i<j” / “where  : Sn  GLd (R) is the irreducible representation, or the Specht module, corresponding to  .”
- 273–278: “module, an R[Sn] module which realizes the corresponding irrep. It is equipped with an invariant inner product” / “L(G, ) = wij I - ((ij))”.
- 291–295: “The minimum eigenvalue is the minimum of this quotient:” / “min(G, ) = min RG,(f ).”
- 64–65: “where  is the standard dominance relation among partitions” followed by row-prefix sums.
- 85–97: “Conjecture 1.5. For all [n] =    , we have” / “C(, )” / “2” / “3”; “This conjecture means that an inequality similar to (1) holds” / “weighted graph G:” / “min(G,  )  3 min(G, ).” (The numerator 2 is printed on line 96.)
- 113–115: “Clearly, (2) holds for any graph G when the Aldous order ... holds” / “the case  = [n - 1, 1] covered by the Caputo–Liggett–Richthammer theorem.”

The supplied text loses Greek letters and relation glyphs in displayed mathematics; the quotes above preserve that damage rather than inventing literal glyphs. Direction is also checked against the paper's standard-module case (24–28), its zero-kernel/dominance proof (327–360), and its star example (740–765): the more dominant partition is the denominator. No PDF or web source was consulted.

## Step 2 — Proposition 1: CORRECT
Line 20: finite-dimensional self-adjoint L(G,tau) has a unit least-eigenvalue eigenvector. Lines 21–22: multiplication by w_ij >= 0 preserves inequalities; summation gives the stated trace, and tr(rho L) >= lambda_min(L) because rho is positive with trace one. The sign c>0 is used.

Lines 24–26: for n>=2 the first set is Delta={w in R^{n(n-1)/2}: w>=0, sum w=1}, compact and convex; the second is D={rho=rho*, rho>=0, tr rho=1}, compact and convex in the finite-dimensional real vector space of Hermitian matrices (or real symmetric matrices). The function is continuous, linear in w, and affine in rho. “Bilinear” is harmless shorthand here: replace each scalar constant by that constant times tr(rho), obtaining an actual bilinear extension. The finite-dimensional convex-concave minimax theorem applies with these exact min/max directions. Both extrema are attained.

Line 27: min_rho tr(rho L_sigma)=lambda_min(L_sigma), and <psi,L_tau psi> >= lambda_min(L_tau); the two inequality signs and c are correct. Line 28: the attained minimizer of max_w f has max_w f<=0. It is a SINGLE rho for the fixed psi, independent of w. Testing every simplex vertex then yields ALL i<j inequalities at once. Unnormalised weights and W=0 cause no problem; only normalised weights are needed for this direction. The proposition also holds trivially for n=1, although the displayed simplex proof presupposes n>=2 and should mention this vacuous case.

Small editorial qualification outside the proposition: lines 30–31's “largest c” should allow +infinity when sigma=[n] (the denominator always vanishes). For the nontrivial pairs used here the optimal constant is finite and attained. This does not affect Proposition 1 or the n=4 result.

## Step 3 — Section 2(ii), CLR: CORRECT
The precise theorem I can confirm from memory is: for a finite connected undirected graph with nonnegative symmetric edge rates whose positive-rate support is connected, the continuous-time interchange process, with generator Q_IP f(pi)=sum_{i<j} w_ij[f((ij)pi)-f(pi)], has the same spectral gap as the continuous-time single-particle random walk with generator Q_RW g(i)=sum_j w_ij[g(j)-g(i)]. This is equality of the smallest positive eigenvalues of -Q_IP and -Q_RW in this connected setting; it is not equality of every Specht block's minimum.

The regular representation decomposes into the irreducible representations, each with its dimension as multiplicity. For connected support only the trivial representation contains kernel vectors, since positive-weight transpositions generate S_n. Consequently the interchange spectral gap is min_{nu != [n]} lambda_min(G,nu). The standard block has minimum equal to the random-walk gap. Equality of the two gaps therefore gives lambda_min(G,tau)>=lambda_min(G,[n-1,1]) for EVERY nontrivial tau. The generators have exactly the note's normalisation; no extra factor two occurs.

For disconnected support lambda_min(G,[n-1,1])=0, and positive semidefiniteness gives the desired inequality directly, including all-zero weights. One must not identify this zero with a “smallest positive eigenvalue” on a disconnected chain. Thus the note's application is valid for every nonnegative weight function. Independently, the supplied paper explicitly states this very block inequality as equation (1), lines 24–37, and invokes it again at 113–115. The original CLR paper has not been consulted (browsing prohibited), but no uncertainty about the needed statement remains.

Section 2(i): CORRECT. A transposition acts as -1 in the sign representation; each I-rho_sigma((ij)) has eigenvalues 0 or 2, so 0<=L_sigma<=2W I. “Ratio >=1” is understood only when the denominator is positive; the inequality itself always holds.

## Step 4 — Section 3 line audit

### Reduction (42–43): CORRECT
The dominance chain is [4] > [31] > [22] > [211] > [1111]. Among distinct nontrivial pairs, all except sigma=22,tau=211 have sigma=31 or tau=1111. Reflexive pairs satisfy the inequality by positivity.

### Lemma 2 (45–53): CORRECT
- Lines 45–46: a,b,c>=0, W=a+b+c, D^2=((a-b)^2+(b-c)^2+(c-a)^2)/2>=0.
- Line 49: transposing the Young diagram conjugates the representation by the sign character; (31)'=211. On transpositions rho_211=-rho_31, giving L_211=2W I-L_31.
- Line 50: the standard module is the sum-zero subspace of R^4. Its largest eigenvalue equals lambda_max(L_G), including disconnected and zero graphs (the removed constant eigenvalue is zero and all other eigenvalues are nonnegative).
- Lines 50–52: the action on the three perfect matchings has kernel the Klein four subgroup, image S_3. Its sum-zero subspace is the irreducible 22: dimension 2, character 0 at a transposition, and the three matching involutions are as listed. For example (12) fixes 12|34 and exchanges the other two matchings; (34) has the same action.
- Lines 52–53: on three matching labels these involutions generate a weighted triangle (the fixed matching labels and the triangle-edge labels may be permuted, which leaves its eigenvalues unchanged). Trace of the full triangle Laplacian is 2W and the product of its two nonzero eigenvalues is 3(ab+bc+ca); hence they are W +/- sqrt(W^2-3(ab+bc+ca))=W +/- D. Zero eigenvalues when the triangle is disconnected remain included. Both formulas in (47) follow.

### Theorem 3 (55–58): CORRECT
- Lines 55–58: substitution from Lemma 2 makes the two inequalities algebraically equivalent: 2W-lambda_max >= (2/3)(W-D) iff lambda_max <= (4/3)W+(2/3)D.
- Lines 60–62: |Pv|^2=a^2+b^2+c^2-W^2/3=(2/3)D^2. Cauchy–Schwarz on the sum-zero unit ball gives the displayed support formula, including Pv=0.
- Lines 63–68: if (*) holds, for each x its weighted energy is bounded by the expression for its chosen u, hence by the maximum over u, exactly (4/3)W+(2/3)D. Maximising over x proves the result. This is a sufficient condition, and no illicit interchange of maxima or quantifiers occurs.
- Lines 70–72: all three e vectors are unit, mutually orthogonal and sum zero. Direct coordinate subtraction gives all six listed differences, with the displayed signs.
- Lines 73–76: max{(q+r)^2,(q-r)^2}=(|q|+|r|)^2, and similarly for the other matchings. Replacing coordinates by absolute values and permuting them merely permutes the three constraints and the allowed u coordinates; invert that permutation at the end. The lower bounds u_m>=sqrt(3/2)t_m have the correct scaling and order.
- Numbered inequality (1), line 78: CORRECT. The sum is 2(pq+qr+rp)-2, and pq+qr+rp<=p^2+q^2+r^2=1 by a sum of squares.
- Numbered inequality (2), line 79: CORRECT. (p+q)^2<=2(p^2+q^2)<=2; equality requires p=q=1/sqrt(2),r=0 in this ordering.
- Numbered inequality (3), lines 80–83: CORRECT. The sum of squares is 1+p^2+2p(q+r); q+r<=sqrt(2)*sqrt(1-p^2). Put p=cos(theta), 0<=theta<=pi/2. The trigonometric bound has amplitude sqrt(1/4+2)=3/2, giving upper bound 3. Subtract 8/3. This bound is sharp at p=sqrt(2/3), q=r=1/sqrt(6), which respects the order.
- Case 1, line 85: CORRECT. All t_m<=0, so u=0 satisfies every constraint.
- Case 2, lines 87–88: CORRECT. The sum is zero; t_a<=t_b<=-t_c/2 gives both lower bounds. The norm is (3/2)(1/4+1/4+1)t_c^2=(9/4)t_c^2<=1 by (2).
- Case 3, lines 90–94: CORRECT. The first coordinate exceeds its bound by (1). The norm expands to 3(t_b^2+t_b*t_c+t_c^2), and the second displayed expression is identical. Here 0<t_c/2<t_b+t_c<=1/3 and 0<=t_c-t_b<(3/2)t_c<=1. These bounds give norm squared <=1 (in fact <1 in this case). The three cases are exhaustive and handle their boundaries.
- Equality, line 96: CORRECT. For the unit star, spec(L_G)={0,1,1,4}, W=3, a=b=c=1, D=0. Thus lambda_min(211)=2 and lambda_min(22)=3, ratio 2/3. Scaling all three star edges by any h>0 preserves equality and has positive denominator; therefore the optimal constant really is 2/3. This is an asserted equality example, not a claim to classify all equality graphs. A single edge also makes the Laplacian upper bound an equality, but both compared minima vanish; it does not determine the optimal ratio.

### Density-disc interpretation (98–102): CORRECT with wording qualifications
The three reflection matrices in the 22 model sum to zero and form three directions at 120 degrees in the plane of real symmetric traceless 2x2 matrices. For a density matrix, their expectation vector s has sum zero and |s|^2<=3/2; conversely every such vector is realised by a real density matrix. For complex density matrices, the full state space is a Bloch ball and this disc is its projection, or one may simply restrict to real density matrices. With u=sqrt(2/3)s, the Proposition 1 inequalities become exactly (*), because 211 edge energy is 2-(x_i-x_j)^2. The piecewise formula is affine in the six squared differences (their maximum in each matching is piecewise linear); “piecewise linear” is reasonable on the unit-sphere domain since sum_{i<j}(x_i-x_j)^2=4 supplies the constant as a linear function. In any event it is not globally linear. For the displayed unsorted p=0,q=r=1/sqrt(2), t=(2/3,-5/6,-5/6), its centred vector is (1,-1/2,-1/2), squared norm 3/2; u_a>=sqrt(2/3) together with sum u=0 forces |u|>=1. The constructed u attains 1. After sorting this is Case 2 with a coordinate permutation. “Single edge” describes the vector, and the graph with just that edge is consistent with it.

Verdicts reached so far: no substantive gap or wrong numbered statement. Historical numerical claims in Section 4 have not been accepted as evidence; Step 5 will replace them independently.

Step 5a: independent Young orthogonal representations built; dimensions [1, 3, 2, 3, 1]. Coxeter relations and full S4 character table passed; maximum relation residual 1.1102230246251565e-16.

Step 5b: saved 32072 graphs, including 32000 random graphs in eight families and all 64 unweighted supports, to sampled_graphs.npz. Seed 261022151.

Step 5 progress: 512/32072 graphs; 0 counterexamples; elapsed 0.19 s.

Step 5 progress: 4608/32072 graphs; 0 counterexamples; elapsed 0.24 s.

Step 5 progress: 8704/32072 graphs; 0 counterexamples; elapsed 0.28 s.

Step 5 progress: 12800/32072 graphs; 0 counterexamples; elapsed 0.33 s.

Step 5 progress: 16896/32072 graphs; 0 counterexamples; elapsed 0.37 s.

Step 5 progress: 20992/32072 graphs; 0 counterexamples; elapsed 0.41 s.

Step 5 progress: 25088/32072 graphs; 0 counterexamples; elapsed 0.47 s.

Step 5 progress: 29184/32072 graphs; 0 counterexamples; elapsed 0.55 s.

Step 5 COMPLETE: 32000 random / 32072 total graphs; 0 counterexamples. Formula error 2.74e-15 at W=1. Runtime 0.60 s; peak RSS 78.6 MiB. Full results numerical_results.json.

### Step 5 verdict — no counterexample
Ran:
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 10 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 independent_check.py > numerical_output.txt`

The sandbox printed “nice: setpriority: Operation not permitted”; the Python check nevertheless ran successfully, with one numerical thread, 0.604 seconds elapsed and 78.6 MiB peak resident memory. No heavy or persistent process was launched. The script sets a 240-second wall alarm and a 220-second CPU limit. The priority adjustment could not be verified; the resource limits requested for this run were met by a wide margin.

Computed all five Specht minima using independently constructed Young orthogonal matrices, dimensions 1,3,2,3,1. Coxeter relations residual 1.11e-16, all five conjugacy-class characters checked. Tested 32,000 random graphs (4,000 each: bounded dense, exponential, Dirichlet with near-zero weights, sparse 25%, sparse 60%, log-uniform, one-to-three weights amplified by up to 1e8 with some edges absent, and stars perturbed by weak edges). Also tested all 64 unweighted supports and eight explicit named graphs, for 32,072 total. Includes star, path, triangle-plus-pendant, single edge, C4 and K4. Weights were normalised by W for numerical stability; original weights and every graph identifier are saved in sampled_graphs.npz.

For each sigma->tau the minimum positive-denominator ratio, verified with 70-digit mpmath matrices, is:

| sigma | tau | minimum | weights in order 12,13,14,23,24,34 |
|---|---|---:|---|
| 31 | 31 | 1 | (1,1,1,0,0,0) |
| 31 | 22 | 1 | (0,1,1,1,1,0) |
| 31 | 211 | 2 | (1,1,1,0,0,0) |
| 31 | 1111 | 3 | (1,1,1,1,1,1) |
| 22 | 22 | 1 | (1,1,0,0,0,0) |
| 22 | 211 | 2/3 | (1,1,1,0,0,0) |
| 22 | 1111 | 2 | (1,1,1,0,0,0) |
| 211 | 211 | 1 | (1,1,0,0,0,0) |
| 211 | 1111 | 3/2 | (1,1,1,1,1,1) |
| 1111 | 1111 | 1 | (1,0,0,0,0,0) |

Near ties within 1e-12 retain the first representative rather than replacing it with eigensolver noise. Exact zero denominators are identified from kernels for each support; their ratios are undefined, and their inequalities are automatic by positive semidefiniteness. Ill-conditioned positive denominators (<1e-9 after normalisation) and apparent failures are recomputed at 70 digits. No ratio below 2/3-1e-9 occurred. There are no counterexample weights to save. The largest discrepancy between Lemma 2 and the independent matrices was 2.74e-15 at W=1. Files: independent_check.py, numerical_results.json, numerical_output.txt, sampled_graphs.npz. Historical Section 4 numbers are not reproduced or certified by this new experiment.

## Step 6 — status in the supplied paper
Searched the full text for small-n statements, numerical results, and the conjecture's proved cases. The introduction (106–118) lists complete and quasi-complete graphs and pairs already in the Aldous order; it reports simulations on all unweighted graphs with n up to 7 and many random weighted graphs. No theorem asserting the conjecture for all weighted graphs at n=4 was found. Theorem 1.4 gives 1/n^3=1/64 here, not 2/3; Theorem 4.4 (714–737) gives 2/3 for quasi-complete weighted graphs only. Arbitrary weighted four-vertex graphs are not automatically quasi-complete: the unweighted four-vertex path cannot be made quasi-complete by relabelling, since a nonzero edge at the largest nonisolated label would force that vertex to join all earlier vertices; a connected quasi-complete four-vertex graph therefore has a universal vertex, whereas P4 has none. The Aldous cases do not cover sigma=22,tau=211: the star itself has ratio 2/3<1. Thus the full n=4 claim is neither explicitly proved in the supplied paper nor an immediate specialisation of its stated comparison results.

The sharpness example IS already in the paper: Theorem 4.5 (740–765), with m=2, gives tau=[2,1,1], sigma=[2,2] on K_{1,3}, ratio 2/3. The paper's notation [2^m] means m parts equal to 2, not a one-row partition of 2m (footnote 750). No novelty claim for the equality example is warranted. This search concerns the supplied version only, not later literature or unstated consequences of cited papers.

## Final independent audit before report
Re-derived the potentially tight inequality (3) without trigonometry: (p+r)^2+(p+q)^2 is the quadratic form of [[2,1,1],[1,1,0],[1,0,1]], whose eigenvalues are 3,1,0 (the antisymmetric q-r direction has eigenvalue 1, and the symmetric 2x2 block has eigenvalues 3,0). This again proves the upper bound 3. The star's ordinary Laplacian spectrum independently gives the stated Specht minima through Lemma 2 and agrees with the 70-digit Young-matrix computation. The single-edge graph has spectra 0, {0,0,2}, {0,2}, {0,2,2}, {2} in partition order 4,31,22,211,1111, consistent with the zero-denominator treatment. The numerical relation error, formula error, sign, normalisation, degeneracies, and sharpness are all consistent.

Overall verdict: SOUND for Proposition 1 and the claimed n=4 theorem. Suggested minor qualifications: the trivial n=1 proof case; infinity in the informal optimal-constant sentence when sigma is trivial; disc versus full complex Bloch ball; ratios only for positive denominators. Unchecked: the note's historical Section 4 computations and its separate n=5 search claims; these are not used in the proof.

Final artifact audit: REPORT.md written. Parsed independent_check.py, validated results JSON against all 32,072 archived weight vectors and identifiers, verified the 32,000 random count, all ten dominance-pair records, nonnegative finite weights, no counterexamples, and measured resource limits. Complete.
