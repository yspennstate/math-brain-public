# Cross-role mathematical handoff — Gaussian / tensor reference-chaos lemma

Source ownership remains RS-2026-CL-A. This is a supporting lemma for the progress-first Gaussian roles P08/P09; it does not transfer or duplicate their source claims.

Let `R_n=gamma_n` be a standard Gaussian reference with Hermite chaos `L^2(gamma_n)=oplus_k H_{n,k}` and Ornstein–Uhlenbeck semigroup `T_t|H_k=e^{-tk}`. Let `P_n,Q_n << gamma_n` have densities `p_n,q_n` and define

`Lambda_n(d)=sup_{deg f<=d, f!=0} E_{Q_n} f^2 / E_{gamma_n} f^2`.

Then, with `Delta_n=p_n-q_n`,

`||Pi_{1:d} Delta_n||_2^2 <= Lambda_n(d) Adv_{Q_n}^{<=d}(P_n,Q_n)^2`.

Hence if `D_n->infinity`, source LDA is bounded through `D_n`, fixed-degree source LDA tends to zero, `sup_{d<=D_n} log_+ Lambda_n(d)/d ->0`, and `log_+ ||Delta_n||_2^2=o(D_n)`, then for every fixed `t>0`,

`TV(T_t P_n,T_t Q_n)->0`.

More quantitatively, a fixed OU time `t` suffices whenever both the low-degree norm-inflation exponent and the total `L^2(gamma_n)` pair-complexity exponent are strictly below `2t`.

Potential use for P08/P09: prove `Lambda_n(d)` from Gaussian correlation/chaining or tensor norm estimates, rather than reproving a low-degree-to-noise conversion. Hsieh et al. arXiv:2601.05850 remains close prior art in tailored Gaussian symmetric settings; this handoff is only the abstract bridge.
