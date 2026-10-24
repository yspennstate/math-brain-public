# Independent audit of the w543 Gaussian packet

Verdict: KEEP H1-H4 as auxiliary-model assertions under their stated hypotheses. P0321 is not proved. This audit is of the mathematical argument, not of another review. The source snapshot is retained in audit_snapshots/w543_ATTEMPT.md; the exact snapshot receipt is in AUDIT_SNAPSHOT.json.

The independent derivation in ATTEMPT.md was saved before reading w543. It recovers H1 and H2 when kappa=0, T=1/beta, and mu=b. It gives the same plateau exp(-9 T Lambda^2/(4 pi mu)) and positional exponent T|G|^2/(4 pi mu). Numerical contractions validate the normalization in that restricted model; they do not certify the actual gas.

For H1 with kappa>0, curl contracts the transverse projector to |k|^2/4. The radial integral of 1/(mu+kappa|k|^2) is log(1+kappa Lambda^2/mu)/(4 pi kappa), and its frequency integrability justifies Riemann-Lebesgue at fixed mu>0. The kappa=0 limit is continuous. For H2, the longitudinal spectrum is integrable for 0<=s<2, including s=0, and subtracting the integrable transverse correction leaves the same logarithmic coefficient. Neither step multiplies dependent conditional bounds.

For H3, subtraction yields the nonnegative kernel mu/[kappa |k|^2(mu+kappa|k|^2)]. The bound 1-cos(k dot x)<=|k|^2 R^2/2 gives exactly 9 T mu R^2 log(1+kappa Lambda^2/mu)/(8 pi kappa^2). This proves a bounded-window relative bound. It supplies no error uniform in unbounded R: at fixed mu>0 the positive plateau remains. It is therefore not a license to transfer a power law to the microscopic gas.

For H4, rotate x onto the first axis and write G=(g_1,g_2). The angular coefficient is

    integral_0^{2pi}|x|^2 cos^2(phi)(-g_1 sin(phi)+g_2 cos(phi))^2 dphi
      = (pi/4)|x|^2(g_1^2+3 g_2^2)
      = (pi/4)(|G|^2|x|^2+2(G_1 x_2-G_2 x_1)^2).

Multiplying by T/[2 kappa(2pi)^2] gives T/(32 pi kappa), as stated. The quartic cosine remainder is integrable and the quadratic contribution diverges logarithmically for every fixed nonzero x and G. Thus ordinary displacement increments do not exist at zero shear, while the angular increments do. One must hold x fixed and view the characteristic function as a function of G when invoking its discontinuity at G=0.

A precision note: both iterated limits of the *unnormalized* C_6(mu,r), as mu decreases to zero and r increases to infinity, equal zero when kappa>0. The decay classification does differ. For q_mu(r)=-log C_6(mu,r)/log r, the iterated limits are 0 and 9T/(2pi kappa), in the opposite limit orders. This sharpens the phrase “changes the observed regime”; it is not a counterexample to H3's inequality.

The most important missing premise is explicitly acknowledged by w543: no microscopic neutral Riesz Gibbs measure, compact-angle reduction, actual bond observable identification, or controlled defect interval is constructed. The independent result in INDEPENDENT_OBSTRUCTION.md gives an additional concrete barrier to one tempting identification: the exact linear additive Gaussian density has a positive negative tail and infinitely many negative values along a ray, so it cannot itself be the law of a nonnegative smoothed particle density. A controlled approximation or a nonlinear observable could still work.

Scope: KEEP is a mathematical audit verdict by a separate worker, not evidence of different-login provenance, a formal theorem receipt, or acceptance of P0321. The designated referee w545 must independently check w544's own new probability obstruction. No such verdict has yet been received.
