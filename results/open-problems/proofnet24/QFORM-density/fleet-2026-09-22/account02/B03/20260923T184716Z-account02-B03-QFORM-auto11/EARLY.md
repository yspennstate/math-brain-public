SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-23T18:47:16Z.
attacking: remove the row-volume marginal gate from the three-volume crossing route by promoting a heavy original row to a genuine hub, then iterate once and use the fresh arbitrary-rank projected crossing theorem.

# Early checkpoint — heavy-row promotion removes the 3-volume marginal gate

Programme: QFORM-DENSITY-3EIG-20260922. Status: supporting theorem in proof; full unrestricted target remains open.

Fresh sources consumed before this checkpoint:
- owner/control `math-research-brain@a18a0e7d6be444f72af154e5c9337c00fb8b9a1f`, OWNER CONTROL revision 2026-09-22.15 and continuation QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z;
- pinned `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, RESULTS / FOURIER_ROUTE_REPORT / COUNTEREXAMPLE_SEARCH;
- fresh proved arbitrary-rank projected crossing theorem `math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401:proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`;
- designated partner account03/B03 latest visible completed report `proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260923T181128Z-account03-B03-QFORM-r36/REPORT.md`, especially its dependence-safe effective-dimension Riesz compiler.

## Key algebra

Let a physical cross block be M=A[I,J], and set

    Z3 = e_3(M M^T) = sum_{|S|=3} det(M_S M_S^T).

Assume Z3>0. Give the triples volume weights w_S=det(M_S M_S^T)/Z3 and row marginals alpha_i=sum_{S contains i}w_S.

If every alpha_i<=1/2, the pinned Theorem D already yields

    ||p_Q||_infty <= 6 sqrt(e) Z3^(-1/6).

If alpha_i>1/2, promote that *original coordinate* i to a hub. Write its row m=M_i, S=||m||, and project every remaining row orthogonally off m:

    C=M_{I\{i},J}(I-P_m).

Exterior-volume expansion gives the exact identity

    S^2 e_2(C C^T) = alpha_i Z3 > Z3/2.                 (E1)

Thus it suffices to prove a one-hub/two-volume theorem with no row-marginal condition.

For that theorem, write the rows of C as c_r, Z2=e_2(CC^T). If all 2-volume row marginals are <=1/2, the new grouped projected-crossing theorem with (k,ell)=(1,2) gives

    ||p_Q||_infty <= C0 M_H^(1/3) S^(-1/3) Z2^(-1/6),
    C0=3*2^(7/6)*e^(1/3)<9.4.                            (E2)

If a row c_i has marginal a_i>1/2, promote that original coordinate too. Put d_r=P_{c_i^perp}c_r and F_i^2=sum_{r!=i}||d_r||^2. Then

    ||c_i||^2 F_i^2 = a_i Z2 > Z2/2.                    (E3)

The promoted two-hub crossing product is S||c_i|| and its ell=1 projected volume is F_i^2. If every one-volume marginal ||d_r||^2/F_i^2<=1/2, the fresh (k,ell)=(2,1) theorem gives a constant <=6 at the scale on the right of (E2).

If instead some d_j carries >1/2 of F_i^2, promote j as a third original hub. The literal three-row cross block has product of nonzero singular values

    S_3 = S ||c_i|| ||d_j|| > (S sqrt(Z2))/2.             (E4)

The exact-rank-three crossing theorem from the same source applies after conditioning all unpromoted I-coordinates. The hub-side 3D projection has density cap <=M_H and the J-side orthogonal projection has cap <=2^(3/2), so its density constant is <=3*2^(5/6), again below C0 at the scale in (E2).

Therefore the marginal condition is removable in the one-hub/two-volume branch. Combining with (E1) gives the candidate global crossing theorem

    ||p_Q||_infty <= C3 Z3^(-1/6),
    C3 = 3*2^(4/3)*e^(1/3) = 10.5501688311...             (E5)

for every physical cross block with Z3>0, with arbitrary same-side curvature and affine terms. This uses no post-rotation independence: promoted variables are genuine original coordinates; orthogonal projections are used only through joint density caps.

The partner r36 effective-dimension lemma applies case-by-case before any sum/difference separation and is expected to give

    int |t|^(-1/2)|phi_Q(t)|^2 dt
      <= (24/5)2^(2/3)sqrt(pi)e^(1/6) Z3^(-1/12)
      =15.9545754136... Z3^(-1/12),                       (E6)

hence E|Q-Q'|^(-1/2)<=6.3649546984... Z3^(-1/12), while retaining the whole independent-copy difference Q-Q'.

Remaining work in this run: write the complete conditioning/provenance proof, verify all constants, and pin the remaining structural debt. The theorem does **not** imply that the three-large-eigenvalue hypothesis furnishes a cut with Z3 bounded below; the previously corrected rank<=2 cross-cut families remain outside it.
