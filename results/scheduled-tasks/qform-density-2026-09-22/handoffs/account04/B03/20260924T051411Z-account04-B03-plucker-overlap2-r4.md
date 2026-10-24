# account04/B03 handoff — Plucker localization of exact-rank-three overlap-two mass

Run: `20260924T051411Z-account04-B03-plucker-overlap2-r4`  
Status: supporting theorem proved; full conjecture open; continuity not claimed.

For an exact-rank-three matrix
[
A=ULambda U^T,qquad U^TU=I_3,qquad Delta=|detLambda|,
]
define the Plucker weights (w_S=det(U_S)^2), so (sum_S w_S=1). If
[
eta=rac{E_2(A)}{Delta^2},
]
then the overlap-two sector obeys the dimension-free dichotomy
[
oxed{
max_{|H|=2}J_2(H)gerac{E_2(A)^2}{18Delta^2}
quad	ext{or}quad
max_{|S|=3}|det A[S,S]|>rac{E_2(A)}{6Delta}.
}
]

The proof keeps the diagonal subtraction exactly. For (q_H=sum_{Ssupset H}w_S), (r_H=sum_{Ssupset H}w_S^2), one has
[
J_2(H)=Delta^2(q_H^2-r_H),qquad sum_Hq_H=3.
]
Thus some (q_Hgeeta/3). If (w_*=max_Sw_Sleeta/6), then
[
q_H^2-r_Hge q_H(q_H-w_*)geeta^2/18;
]
otherwise the maximizing Plucker atom gives the principal-triple alternative.

Applying completed account01/B03 r41 at the literal inequality
[
|p_Q|_{infty,mathrm{ess}}le129.924435862525374,J_2(H)^{-1/6}
]
gives, whenever (Deltage1), (etage1/4), and (w_*leeta/6),
[
oxed{|p_{X^TAX}|_{infty,mathrm{ess}}<333.880.}
]
This is for every cap-one product law, all signatures, and arbitrary dimension, within the exact-rank-three class.

In the complementary branch a genuine physical triple has determinant at least (1/24). This is not claimed to imply a uniform smallest singular value. With the additional deterministic anisotropy gate (|A|_{mathrm{op}}^2/Deltale K), the physical-triple theorem gives (|p_Q|_inftyle144sqrtpi K).

Canonical report: `yspennstate/math-open-problems@5f93186cf8952b2b8b0255e08a78fd8506c613e4`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B03/20260924T051411Z-account04-B03-plucker-overlap2-r4/REPORT.md`.

Source pins:
- designated Claude base: `e5f71d79eff325201dd0274053d20268ce65b837`;
- current Claude-directory blobs: RESULTS `62e20ee976ddeb3f42d3ee5befd6ed49edc917a5`, FOURIER `9da148eed6cd43b1046a6f91d0f9329e12921cb4`, COUNTEREXAMPLE `ee721b237e206f31298b1871979faaab37a1bac2`;
- completed account01/B03 r41: `7dc6d6841e318a88174fb41ddaa1c88e223aacf4`, checks `1629c2f5ee835709c7dcbef2a0ebe44e36486e3f`.

Exact remaining gap: in exact rank three, pay the dominant-Plucker-atom branch without a spectral-anisotropy hypothesis; in higher rank, replace the lost rank-one Plucker factorization by a cancellation-safe localization.
