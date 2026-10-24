SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-23T17:32:17Z.
attacking: whole-active receiver-core coupling — derive a mass-homogeneous localization compiler for the newest partner quadratic-receiver theorem, and test fragment-first normalization on an exact-target separated-support family.

# Early substantive checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full QFORM remains OPEN. Continuity separate.

First unpaid implication attacked: `QFORM-RECEIVER-SCORE-MASS-HOMOGENEITY-v1`.

Let 4/3<r<2, p=r/(r-1), alpha=r-1. In the setup of account03/B14's completed `QFORM-HYBRID-QUADRATIC-RECEIVER-LP-v1`, replace the driver probability law by a positive submeasure nu of mass m while keeping the receiver W whole. Assume the conditional core densities satisfy ||p_{T_z}||_p<=K_r uniformly. For

    F_z(w)=d w^2+(2 c^T z+e)w,
    S(z,w)=2 d w+2 c^T z+e,

let sigma be the pushforward of nu(dz) P_W(dw) under S and suppose sigma has density cap L. Then the unnormalised output measure eta has

    ||p_eta||_infinity
      <= K_r 2^{2 alpha/r} (2-r)^{-1/r}
             m^{1/r} L^{alpha/r}.                    (P1)

Derivation: the one-dimensional area formula used by the partner gives

    ||p_{F_z(W)}||_r
      <= 2^{alpha/r} [E_W |S(z,W)|^{-alpha}]^{1/r}.

Holder/Jensen for the finite measure nu gives

    int ||p_{F_z(W)}||_r nu(dz)
      <= 2^{alpha/r} m^{1-1/r}
         [int |s|^{-alpha} sigma(ds)]^{1/r}.

For every finite measure of mass m with density <=L,

    int |s-a|^{-alpha} sigma(ds)
      <= [2^alpha/(1-alpha)] L^alpha m^{1-alpha},

by symmetric decreasing rearrangement. Since 1-alpha=2-r, (P1) follows.

The decisive homogeneity is therefore

    m^{1/r} L^{(r-1)/r}.                              (P2)

If every localization cell satisfies the mass-homogeneous score cap L_j<=H m_j, then (P1) becomes linear in m_j and arbitrary positive mixtures transfer with zero loss:

    sum_j ||p_{eta_j}||_infinity
      <= K_r 2^{2 alpha/r}(2-r)^{-1/r} H^{alpha/r}.

In particular, if d!=0 and W is left whole, then for an arbitrary positive decomposition nu=sum_j nu_j of the ENTIRE driver law,

    L_j <= m_j/(2|d|),

because conditional on z the score contains the scaled whole cap-one variable 2dW. Hence

    ||p_Q||_infinity
      <= K_r 2^{alpha/r}(2-r)^{-1/r}|d|^{-alpha/r},    (P3)

with exactly zero tax from the number, locations, separation, diameter or tails of the driver pieces. Likewise, if a driver coordinate Z_k with c_k!=0 is kept whole while only the other drivers are fragmented, then L_j<=m_j/(2|c_k|) and the same bound holds with |c_k|.

This is stronger than merely saying that the probability-level theorem is support-free: it identifies exactly when an arbitrary positive active-law decomposition can be summed without concavity loss. It also predicts a sharp proof-order barrier when the only available cap L_j does not scale with m_j.

The newest designated partner source used is account03/B14 auto11 at `yspennstate/math-open-problems@e786ed60fea4db8a672faaffc35531bb06eb9b57`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260923T164047Z-account03-B14-QFORM-auto11/REPORT.md`. Its Theorem 2.1 is the probability-level receiver inequality being homogenised here. The required Claude source at `e5f71d79eff325201dd0274053d20268ce65b837` has also been freshly read through RESULTS.md, FOURIER_ROUTE_REPORT.md and COUNTEREXAMPLE_SEARCH.md; a source-valid exact-target obstruction using its Theorem B will be included in the completed report.
