# C0052 — statement only (for the independent adversary)

Source: Hugo Duminil-Copin, *Lectures on the Ising and Potts models on the hypercubic lattice*, 2017, Conjecture 6 and equations (7.1)–(7.2), printed p. 94. https://www.ihes.fr/~duminil/publi/2017PIMS.pdf

The three-dimensional half asks: “Prove that the three-dimensional Ising model is non-trivial”. This is the nearest-neighbor ferromagnetic Ising model on Z^3, at zero field, with the free infinite-volume state and beta approaching beta_c from below. Put G_beta(x)=<sigma_0 sigma_x>, chi(beta)=sum_x G_beta(x), and xi(beta)=(lim_n[-log G_beta(n e_1)/n])^(-1). Use U4(x1,x2,x3,x4)=<sigma_x1 sigma_x2 sigma_x3 sigma_x4>-G12 G34-G13 G24-G14 G23. The positive convention is g_+(beta)=-sum_{x2,x3,x4}U4(0,x2,x3,x4)/(chi(beta)^2 xi(beta)^3). The source prints a signed coupling; vanishing is invariant under this sign change. The source's non-triviality target is that this coupling does not tend to zero as beta increases to beta_c. A uniform positive liminf is a stronger sufficient conclusion, not an identical reformulation.

The 4D half of the 2017 conjecture was subsequently settled by Aizenman–Duminil-Copin (arXiv:1912.07973). No 3D solution has been verified here. Current openness: UNKNOWN after a bounded search; historical source status: open.

Independent-adversary boundaries: check the original normalization, the difference between a critical block marginal and this subcritical global coupling, and any claimed bound's exact hypotheses. This packet contains no proposed proof. Local intake record: probability_1000_intake_claude_20260907/problems.jsonl, C0052, locator p. 94.
