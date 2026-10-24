# B07 fixed-multiplicity audit r11

Objective: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924.

## Source pins
Historical 17: commit 7c0d6e60946b19423e6400a12d34b473cf0591e2, manuscript blob 183ccd294763214e6a707e8d4749ff9a8cf7006d, SHA-256 9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69.
Owner-pinned nine/400: commit eeb752c8943536541b34b42b8bf48e924f4d3d2f, paper blob 19fb119877426b640b2c0dae19ec2f78a399fe11, SHA-256 bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3.
Separate nine reconstruction: paper blob 823201f05363fcc60c38cce0feb5abb636f081d7, SHA-256 ea56bc35cff9815db71a9f5a620e0160e3a39cf53ff60c789707294d53240eba.
Fresh multiplicity-eight candidate: commit 90324fd3d44f85c40830a954d6e867ab034c1377, corrected proof blob 9436ae220343cc5984224f874b94d116cef47a40.

## Verdict
- Historical 17: PASS after two local repairs.
- Owner-pinned nine/400: PASS after one local repair.
- Separate nine reconstruction: PASS after the same local repair.
- Fresh multiplicity-eight candidate: PASS after the same local repair.
- False theorem statement found: none.
- PDF rendering, fresh Lean execution and exhaustive priority review: UNCHECKED.

## Local gaps
Historical product projection, lines 258-282: after zero-beta factors are dropped, the retained-index sum is at most the full sum d. Insert the missing inequality. No constant changes.

Hyperbolic-pair proof, historical lines 437-482 and owner-pinned-nine lines 563-608: the two exponential coefficient vectors have equal Euclidean norm but need not have the same large physical coordinate. Choose one physical coordinate for the positive tail and independently another for the negative tail. The same cutoff estimate holds on both tails, so the envelope and all downstream constants are unchanged.

## Ordered-minor audit
For increasing S,T, nonsingular B=A[S,T], and distinct exterior l,m,
det A[S+l,T+m] equals the Schur residual times det(B), with sorting parity determined by the insertions of l and m. Squaring removes that parity exactly.

For each ordered disjoint child (U,V), let c(U,V) count deleted row/column pairs having a nonsingular parent. Then the determinant-weighted parent residual sum equals the child sum weighted by c(U,V), and c(U,V) is at most (r+1)^2. Singular parents explain strictness. Weighted averaging proves existence of one good seed, not a universally good seed.

Fresh exact diagnostics: 14,796 signed bordered identities; 100 aggregate parent/child identities; 81 strict cases versus the crude upper bound; Cauchy blocks attain parent multiplicities 4,9,16,25 at r=1,2,3,4. Also 90 exact two-anchor bank identities, 1,350 leave-one-column identities, 270 leverage-marginal checks, and 270 one-exception rank checks passed.

## Multiplicity-eight structural closure
Use d=3/40, p=1/400 and kappa=4/625. Under no pivot and s_8(A)>=1, order two gives V_2>=kappa^2. If V_3<kappa^3, good determinant-weighted order-two seeds carry more than half of V_2 and have completion error squared at most 18 kappa.

Rank six plus s_8 forces two complement diagonal defects. Their physical two-set H satisfies
|det A[S,H] det A[H,T]| > (3/20)|det A[S,T]|.
Carrying determinant weights through the assignment to H gives one literal pair with
g=det(A[H,Hc] A[H,Hc]^T) > 9/800.

The rank-two determinantal leverage law then has at most one coordinate above 2/3: two would force a literal 2 by 2 cross minor squared above 3/800, while the no-pivot entry cap forces it below 4/14641.

The exact leave-one-column identity and one-exception completion imply W_dis > g/50 > 9/40000. The restricted remainder has rank at most two; otherwise three large diagonal coefficients form a strictly diagonally dominant 3 by 3 block, with exact margin 7/2200.

Every term of W_dis is already a literal disjoint order-three minor, so W_dis<=V_3. But
9/40000 - (4/625)^3 = 3511529/15625000000 > 0.
Thus the assumed V_3<kappa^3 is impossible. Therefore no pivot and s_8>=1 imply V_3>=(4/625)^3.

A fair physical cut and the audited order-three receiver give density below 375 in the no-pivot branch. The paid pivot branches are below 383, 80 and 392.5 after the local hyperbola repair. Hence a complete safe replacement theorem is
s_8(A)>=s > 0 implies essential density < 393 K^2/s.

Multiplicity seven and the unrestricted multiplicity-three problem remain open.

## Seven-direction proof-interface obstruction
A single shared-anchor overlap minor cannot simply be turned into a one-hub/two-residual crossing. For the symmetric 5 by 5 matrix
[[0,0,1,0,1],[0,0,0,1,0],[1,0,0,0,1],[0,1,0,0,0],[1,0,1,0,0]],
the seed rows 1,2 and columns 3,4 form the identity, while adding coordinate 5 to both sides gives determinant -1. Yet projecting the seed crossing orthogonally off the hub row (1,0) leaves rank one and zero residual order-two volume. The opposite orientation fails identically.

Appending a 2 by 2 identity gives seven eigenvalue moduli at least one. Tensoring with the rank-one averaging matrix J_m/m preserves those seven nonzero eigenvalues and, for m>=29, enters the no-pivot chamber. This is a counterexample to that proof interface, not to a seven-eigenvalue density theorem.

## UNCOMPILED Lean proposals
- sorted_bordered_det_sign
- sampling_exact_parent_multiplicity
- hyperbola_two_tail_coordinates
- s8_no_pivot_V3_lower
