# C0052 statement for the independent adversary

Author: w477. Recipient: w478. This file contains no proposed proof.

The dated intake title is "Non-triviality of the scaling limit of the three-dimensional Ising model" (tier 5, attempted_un). Here "non-trivial" means non-Gaussian, not merely a nonzero variance.

EXACT PRIMARY FORMULATION (PIMS 2017, arXiv:1707.00520v1, printed p.94, equations 7.1-7.2 and Conjecture 6): in the free, zero-field nearest-neighbour Ising state on Z^3 at 0<beta<beta_c, put G_beta(x)=E_beta[sigma_0 sigma_x], chi(beta)=sum_x G_beta(x), xi(beta)=[lim_{n->infinity} -(1/n) log G_beta(n e1)]^{-1}, U4=E[sigma_1 sigma_2 sigma_3 sigma_4]-G12 G34-G13 G24-G14 G23, and g(beta)=sum_{x2,x3,x4} U4(0,x2,x3,x4)/(chi(beta)^2 xi(beta)^3). Prove that g(beta) does not tend to zero as beta increases to beta_c. The source's sign convention has g(beta)<=0. A positive lower bound on -g along a sequence beta_n increasing to beta_c suffices for this definition; a uniform near-critical lower bound is stronger.

My first working formulation used critical smeared-field cumulants. Those are a related auxiliary target; an equivalence with the source's near-critical coupling has not been proved here. The source-faithful packet must keep the two normalizations separate.

Primary source verified directly: https://arxiv.org/pdf/1707.00520 , printed p.94. Short source quote: "Prove that the three-dimensional Ising model is non-trivial". Supporting current identity: Aizenman-Duminil-Copin, arXiv:1912.07973v4, section 3.2. Current openness remains UNKNOWN after the bounded literature and named-prior-work check; no novelty claim is made.

Please freeze your independent first objection before reading my ATTEMPT.md. No success claim is being made.
