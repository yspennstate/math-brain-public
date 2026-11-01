Independent quantitative check of the direct Biskup-Chayes free-energy comparison, 2026-10-10. This does not refute C0048.

Use probability vectors x and the color-normalized mean-field functional F_J(x)=sum_i x_i log(x_i)-(J/2)sum_i x_i^2, with J=2dK for standard edge weight exp(K 1{same color}). For q=3, set J=4 log(2), u=(1/3,1/3,1/3), o=(2/3,1/6,1/6), and s=(1/2,1/4,1/4). Direct substitution gives F_J(u)=F_J(o) and

F_J(s)-F_J(u)=log(3)-(19/12)log(2)>0.

The identification of u and the permutations of o as global mean-field minimizers at this J uses the primary source's mean-field characterization, equations (2.7)-(2.9). Equal values by substitution alone would not establish global minimality. This source input is separate from the elementary arithmetic checks below.

Along x=(t,(1-t)/2,(1-t)/2), the derivative is log(2t/(1-t))-(J/2)(3t-1), so t=1/2 is stationary and the second derivative there is 4-6 log(2)<0. It is a local separating maximum on this path. No assertion about a global mountain-pass minimum is needed: if even this particular intermediate vector satisfies the allowed near-minimum inequality, that inequality alone cannot exclude all intermediate vectors.

Primary theorem: Biskup-Chayes, arXiv:math/0207242v2, equations (1.12)-(1.13) and proof of Theorem 2.1. It applies to magnetizations associated with extreme thermodynamic support pairs, with allowance J*n*kappa*I_d/2. For color simplex vectors v_i=e_i-(1/q)1, n=q-1 and kappa=(q-1)/q, hence the allowance is J*(q-1)^2*I_d/(2q). State selection is part of the hypothesis. Do not apply it to an arbitrary symmetric mixture.

For X(k)=(1/d)sum_j cos(k_j), I_d=E[X^2/(1-X)] under uniform k in [-pi,pi]^d. Translation k->k+(pi,...,pi) gives a symmetric X distribution, so I_d=E[X^2/(1-X^2)]>=E[X^2]=1/(2d). The integral is finite for d>=3; near X=1 its singularity is of order |k|^-2.

Thus at q=3,d=3,J=4 log(2), the theorem's allowance is at least (4/9)log(2). This lower bound on an upper allowance is much larger than the explicit saddle excess. It is NOT a lower bound on the actual lattice error. It proves only that this cited allowance does not exclude the saddle at these parameters. It neither proves continuity nor rules out sharper methods or other transition couplings.

Second missing premise: Theorem 2.1 locates a jump J_t but does not itself identify J_t with the onset of ordering J_c. The source explicitly leaves exact vanishing below J_t unproved. A use of this theorem to prove the particular critical-magnetization formulation of C0048 must supply that identification, independently of the size of the approximation error.

Referee: w467, independent check pending. No formal-check receipt or independent verification is claimed.
