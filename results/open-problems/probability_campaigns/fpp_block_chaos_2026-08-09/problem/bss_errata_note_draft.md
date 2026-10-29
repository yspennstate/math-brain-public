
---

Note on two displays in "Rotationally invariant first passage percolation: Breaking the n/log n variance barrier" (arXiv:2604.01214)

In the proof of Theorem 2.13, the display asserting E[(G_ij(t))^2] >= 2 E[(H_ij(t))^2] cannot hold as stated. At t = 1, the conditional variance identity together with the exchangeability of (X_Mn, X^{ij}_Mn) given the remaining blocks gives E[(H_ij(1))^2] = E[(G_ij(1))^2], so the display would force E[(G_ij(1))^2] = 0 for every block and hence Var(X_Mn) = 0, contradicting Theorem 2.1. The derivation preceding the display in fact yields E[(G_ij(t))^2] >= (1/2) E[(H_ij(t))^2]; the factor 2 belongs on the other side. The argument that follows is unaffected, since (11) uses only Var(X_Mn) <= 2 Sum_ij E[(G_ij(T_ij))^2], which follows from the correct direction.

A small bookkeeping issue then remains at display (14): combining (9), (11), (12) and (13) as printed gives (1/2) M Var(X_n) + 2 C'' M^{-1} Q_n^2 + 2 Sum_ij E[(E[...])^2], with the factors of 2 inherited from (11). Two repairs are available. One can sharpen (11) to constant one - retaining the cross term in the expansion of E[(G-tilde_ij)^2] = 2 E[(H_ij)^2] and using the involution that swaps the block with its resampling copy shows Sum_ij Int_0^1 E[(H_ij(t))^2] dt <= Sum_ij Int_0^1 E[(G_ij(t))^2] dt - after which (14) holds exactly as printed, with kappa = 1/ceil(4 C_1) as chosen. Alternatively one keeps the factor 2 and takes kappa = 1/ceil(8 C_1), doubling the chaos and far-block terms. Theorem 2.13 and everything downstream are unaffected either way.

We record this partly because the constant-one form of the inequality is what makes the variance-reduction engine of Sections 2.3-2.4 carry over verbatim to lattice models with independent block resampling, where the analogous statements admit elementary proofs; details are available on request.
