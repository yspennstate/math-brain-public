# P0347R verdict check (an agent, 12 Nov 2026 ~22:00 laptop time)

Codex referee (gpt-6.1-sol, high, normal speed, Mac mini 1) on the P0347 report (critical beta-splitting tree,
Aldous-Janson OP10 balance indices), report sha256 3471b2d8...: **MINOR**.

Required fix, checked by hand: in Section 4 the lower logarithmic endpoint integrand
G_{p,j}(x) = (x^p log^j x + (1-x)^p log^j(1-x)) / (2x(1-x)) is not bounded by x^{p-1}|log x|^j plus its reflection:
at p=2, j=1, (1-x)^2 log(1-x) ~ -x so G -> -1/2 at 0 while both bound shapes -> 0. The replacement bound
C[x^{p-1}|log x|^j + x^{j-1}] is integrable and the proof's next sentence already handles x^{a-1}|log x|^j, a>0,
so nothing downstream changes (equation 14, the transfer lemma, all constants).

Everything else in Sections 3-8 survived documented attacks: exact tolls with parity (rational check n<=24), psi(p)=h_{p-1},
the signed transfer lemma (o and O versions), Sackin/Colless mean remainders, centered-toll variance and cubic/quartic
coefficients (70-digit quadrature), QC moment induction with coefficient k m_{k-1}, m_k <= k!, determinacy, the Laplace
fixed point and its uniqueness within laws with an exponential moment. Its n=12000 recursion values (S skew 0.7939,
kurt 4.0040; C skew 0.7670, kurt 3.9370) sit well away from the limits 0.7240 / 3.9127, as expected at L ~ 9.4;
the referee says extrapolation from this range is weak evidence and the constants rest on the analytic calculations.

Status: P0347 result accepted subject to the one-line endpoint repair. Paper material can go to an agent.
Not done by the referee: novelty search (done separately: Kolesnik 2404.16021, Chorbadzhiyska-Minchev-Savov 2608.18320,
Heng Ma 2609.14329 contain no Sackin/Colless result), Monte Carlo rerun.
