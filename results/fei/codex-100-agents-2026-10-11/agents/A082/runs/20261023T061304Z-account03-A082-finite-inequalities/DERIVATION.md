# Independent phase-refund reconstruction and exhaustive controller certificate

All costs are in bits. This is a supplied-reference continuation theorem. FEI remains OPEN.

## 1. Reconstruct the complete cost identity

Let a take values in {-1,0,1}, b=1-a^2, and h be any Boolean function of disjoint fair bits. Write A=ahat, B=bhat, beta=E b, m=E h, and sigma in {-1,1}. Parseval gives sum AB=E ab=0 and sum B^2=beta. The physical Boolean wrapper is g=a+sigma b h.

For a normalized finite-cost reference R on seed frequencies with R(0)=m^2, its complete coherent reference is

Q(U,0)=(A_U+sigma m B_U)^2; Q(U,T)=B_U^2 R(T), T nonempty.

Both Q and the actual spectrum normalize because the signed cross term sums to zero. Query seed bit j. Write Pbar=M_j P and Qbar=M_j Q, using full frequency deletion. The physical child spectra average to Pbar. The exact cross-entropy chain, obtained by expanding logarithms in each frequency fiber, is

B_j + average CE(P_child,Qbar)-CE(P,Q) = -D_occ,

where D_occ=D(P||Q)-D(Pbar||Qbar)>=0 by the conditional KL chain rule. This identity includes all reference-only mass and both physical children.

Calibrate Qbar to each child's actual masses on individual (U,seed-empty) atoms and on one block containing the full nonempty seed tail. Its conditional law on that tail is (B_U^2/beta) times the current inherited seed-tail law. The resulting coherent reference Qc is exactly the prescribed vacuum-calibrated seed reference, and its complete refund is

r_child=CE(P_child,Qbar)-CE(P_child,Qc)=D(pi P_child||pi Qbar)>=0.

Zero true blocks contribute zero; finite inherited CE forbids an occupied zero-reference block. Empty tails and beta=0 are handled without division. Thus the transaction before a profile change is exactly -D_occ-average r_child. This independently reconstructs the A079 block identity used by A096, without importing either author's checker.

## 2. Physical phase lower bound, with its constant

Put d=E[h x_j], so child means are m+d and m-d, up to outcome labeling. Their coarse vacuum half-difference at U is 2d B_U(sigma A_U+m B_U). Let

V(m,sigma)=sum B_U^2(sigma A_U+m B_U)^2=C+2sigma m D+m^2 E,
C=sum A_U^2 B_U^2, D=sum A_U B_U^3, E=sum B_U^4.

For distributions v,q, Pinsker in bits gives D(v||q)>=||v-q||_1^2/(2 ln2)>=||v-q||_2^2/(2 ln2). One elementary proof groups indices with v_i>q_i by log-sum, then uses binary KL second derivative 1/[p(1-p)ln2]>=4/ln2 and its zero value and first derivative at p=q. Endpoint statements follow by limits or infinite KL.

Both children compare to the SAME coarse inherited law q. The Euclidean identity average ||v_child-q||^2 >= ||(v_plus-v_minus)/2||^2, followed by retaining just the vacuum coordinates, yields

average r_child >= 2 d^2 V(m,sigma)/ln2.

If E>0, complete the square:
V=E(m+sigma D/E)^2+Gamma, Gamma=C-D^2/E>=0.
If E=0, B=0 and V=Gamma=0. This proves A096's weaker bound with V replaced by Gamma, for arbitrary finite seed dimension, without an exhaustive finite seed assumption.

After calibration, let the child's actual full tail mass be tau=beta(1-m_child^2). Replacing its current conditional seed-tail reference M by (1-epsilon)M+epsilon S, for any prescribed nonempty law S, costs at most tau log2(1/(1-epsilon)). For x=Gamma d^2 and epsilon=x/(tau+x), this is <=x/ln2 by ln(1+u)<=u. At x=0 or tau=0 choose no change. Averaging BOTH child charges and subtracting the refund gives

B_j+average CE(P_child,Qnew)-CE(P,Q) <= -D_occ-x/ln2.

The exact same proof permits the stronger current-state choice x=d^2 V(m,sigma). This is an extraction of the displayed phase inequality, not an assumption of a uniform positive refund. Both choices recompute from the CURRENT seed and controller. The coherent invariant survives; controller restrictions are paid by calibrating individual vacuum atoms and one tail block per remaining U. Ordinary marginal steps may be interposed if the coherent invariant is restored by its paid block calibration before the next phase transaction. Finite-tree induction with physical reach weights preserves the original supplied account and all old debits. No first refund is reissued.

This reconstruction accepts A096-PHYSICAL-PHASE-FUNDED-NONEMPTY-RESET@1 unchanged, at its supplied-reference scope. It supplies no influence-priced initial R.

## 3. Exact finite certificate and theorem of exhaustiveness

Fix a0=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1), with truth-table indices in little-endian physical bit order. For each pattern in {-1,0,1}^4, -1 leaves that coordinate free and 0/1 fixes it. Compute all Fourier coefficients by integer character sums divided by the exact remaining cube size. The saved 81 rows contain a,A,B,C,D,E,Gamma,beta as rational numbers. No symmetry quotient is taken.

The exact multiset of Gamma is

Gamma | multiplicity
--- | ---
0 | 53
9/3584 | 1
93/3584 | 2
9/448 | 3
1/64 | 2
3/64 | 4
1/8 | 16

Thus every restriction with positive Gamma has Gamma>=9/3584, sharply, with equality at the original unrestricted controller. Negative sigma changes D's sign in the completed square and leaves Gamma unchanged.

EXHAUSTIVENESS THEOREM. Every controller obtained from a0 by any finite sequence of restrictions of physical controller coordinates is represented by one of these 81 faces, up to relabeling the remaining coordinates. Proof: each original coordinate is either still free or has one fixed value; restrictions of different coordinates commute. The final truth table is exactly the corresponding pattern. Relabeling permutes Fourier indices and preserves C,D,E,Gamma. Seed restrictions do not alter a,b. Therefore the finite certificate applies at every inherited physical controller state in any adaptive tree based on this controller. It does NOT exhaust arbitrary new controllers, arbitrary wrapper modifications, or all Boolean seeds. The latter quantifier is handled by sections 1-2.

## 4. Exact zero-sector diagnosis

For EVERY complementary controller, Gamma=0 iff C=0. If E=0 this is immediate. Otherwise equality in Cauchy-Schwarz says A_U B_U=lambda B_U^2 for all U. Summing and using sum AB=0 gives lambda beta=0. Since E>0 implies beta>0, lambda=0 and C=0. The converse is immediate, with D=0. Thus zero Gram means disjoint supports of A and B.

The actual phase energy is more informative than its uniform-mean lower bound. If beta>0, V(m,sigma)=0 iff m=0 and C=0. Indeed a zero sum of squares forces B_U(sigma A_U+m B_U)=0 for every U. Summing gives m beta=0, hence m=0, then C=0. Conversely these conditions give zero. On any zero-Gamma face with beta>0, V=m^2 E. Consequently the stronger CURRENT-state choice x=d^2 V can still pay a real change when m and d are both nonzero, even though A096's uniform Gamma choice authorizes none. This does not help balanced seeds with d=0, and the quantitative value may shrink without a universal floor.

## 5. Independent parity obstruction and its scope

For h parity on k>=3 seed coordinates, take R=P_h. Its singleton d and mean m vanish. After any seed query, both children are signed parity on k-1 coordinates with the same squared spectrum. Their full wrapper law equals the inherited frequency marginal. Each physical frequency fiber contains only one occupied seed choice, so B_j=0; D_occ=0 because Q=P; both block refunds are zero. Replacing the conditional seed-tail point law by (63/64) of that point plus (1/64) at a distinct nonempty singleton costs beta log2(64/63)>0 in EACH child whenever beta>0. At the fixed controller beta=3/8. This independently accepts A096-ZERO-PHASE-QUERY-REFUND-OBSTRUCTION@1 unchanged. It excludes funding every fixed-strength change from current query refund. It is not a counterexample to FEI.

For k=2 the children have only one nonempty seed frequency; no distinct target exists in that seed frequency space. The checker explicitly records this endpoint rather than inventing a ghost frequency outside the physical domain.

## 6. First unsupported universal line

No cheap influence-priced initial nonpoint reference for arbitrary h has been supplied. Neither Gamma nor V must be positive; parity has a relevant query with no available current refund. A prescribed transport in that sector still needs actual unused original surplus or a justified inherited occupancy payment, retaining all prior debits and both complete terminals. No displayed finite-domain exhaustiveness theorem resolves this missing supplier.
