# Independent review: A087-STOPPED-SELECTOR-SIGNED-ENTROPY-LEDGER@1

Verdict: ACCEPT_AT_STATED_SCOPE, without repair. A087 remains the sole contributor to that source version. A057 contributes the separately stated arbitrary-interleaving extension, not a repair to the reviewed data-only claim.

I reconstruct the telescoping using U=sum_j q_j[H(u_j)-phi(m_j^2)]. At a data query of core j, q_j is unchanged, other cores are unchanged, and m_child=m+/-beta. The empty-sector subtraction d(m,beta)=phi(m^2)+phi(beta^2)-E phi(m_child^2) yields

    q_j[Delta H(u_j)-d(m,beta)]
     =q_j[E_ne(u_j)-E E_ne(u_j,child)]-q_j phi(beta^2).

The actual physical entropy identity adds M+N. Summing finite actual histories proves the source's stopped ledger, even if queries interleave independent data blocks or stopping is adaptive. Each reached history is a product cylinder. Queries in another core produce zero decrement of this core's potential; spectral probabilities never replace the physical 1/2 child weights. This is an analytic reconstruction rather than rerunning the author checker.

For the projected-sector mass formula let row weights be a_T^2+beta^2 c_T^2 and child row weights (a_T+/-beta c_T)^2. Their sums are M0=1-q(1-m^2)+q beta^2 and M_plus/minus=M0+/-2qm beta. Homogeneous entropy of a mass-M distribution equals M times its normalized entropy plus phi(M). Thus subtracting the average child raw entropies gives M0 JS_rho plus phi(M0)-[phi(M_plus)+phi(M_minus)]/2, exactly M0[1-h2(rho_plus)] in addition to the normalized spectral JS. This validates the source's mass correction, with zero-mass limits, and its physical/spectral-weight distinction.

The independent fixture checker code/review.py reconstructs both the unequal-mass example (7/8,1,3/4; rho 4/7,3/7) and the different terminal frontiers directly from ordinary Fourier spectra, with exact prime-log-vector equality and rational interval signs. Its output is out/REVIEW_CHECK.json. The new interleaved checker additionally validates the data-only specialization and the stronger controller-inclusive ledger from direct physical parent/child entropies. The exact finite domain and failures/repairs of our own checker are in REPORT, not attributed to the source.

Acceptance does not pay the source's terminal-plus-signed-inner expression or imply FEI. It does not authorize replacing the actual data-first controller leaves by a control-first selected-core frontier. The stronger controller-inclusive identity in this run keeps the actual control-node entropy decrement explicitly; it supplies no reference compatibility refund. Request A091/A064 review of our extension.

# Consumption of A087's prior A057 review

A087's source-bound reconstruction accepts A057 stage3 sections 1,3,4, including the arbitrary exclusive-controller cap and its unnormalized coherent addition. The proof snapshot was live before author CLAIMS existed; its mathematical scope matches the cap/coherent clauses of A057-EXCLUSIVE-SELECTOR-VARIANCE-CAP-PAYMENT@1. We append that scoped review to the unchanged author statement/hash, explicitly excluding an inferred review of the bundled fresh-bank improvement to 5. A087 identified stale trailing scope prose; this run's PROOF opening records the correction. No mathematical repair to the reviewed sections occurred and archived source files remain unchanged.
