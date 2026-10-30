# r62 derivation A — decoupled time integral and all finite Lp

Work in normalized units: independent coordinate densities <=1, s_3(A)>=1, and no pivot for eta=1/12, zeta=1/256.

The corrected five-eigenvalue paper proves, by a dependence-safe whole-bank decoupling, that for a physical cut with crossing matrix M,
[
 |phi_Q(t)|^2
 <= (sqrt(2) pi e)^ell omega(ell)^(1/2)
    E_ell(M)^(-1/2)|t|^(-ell).
]
Proposition 6.4 with m=2 gives a cut for which
[
 E_2(M)>gamma_2^4,qquad
 gamma_2=(44-15sqrt(2))/96.
]
Since omega(2)=2, taking square roots gives
[
 |phi_Q(t)|
 <=min(1,a_*/|t|),qquad
 a_*={2^(3/4) pi eover gamma_2}.
]

For -1<sigma<1, split at a_*:
[
egin{aligned}
 I_sigma
 &:=
 int_R |t|^sigma |phi_Q(t)|^2dt\
 &<=2int_0^{a_*}t^sigma dt
   +2a_*^2int_{a_*}^infty t^{sigma-2}dt\
 &=2a_*^(1+sigma)
   left({1over1+sigma}+{1over1-sigma}ight)\
 &={4a_*^(1+sigma)over1-sigma^2}.
end{aligned}
]
At sigma=-1/2 this is
[
 I_-<={16over3}sqrt{a_*}
 =41.48595888463038...
]

If Q' is an independent copy of the **complete scalar output**, then
[
 phi_{Q-Q'}(t)=|phi_Q(t)|^2>=0.
]
The one-dimensional Riesz identity in the paper's Fourier convention therefore gives exactly
[
 I_-=sqrt{2pi},E|Q-Q'|^(-1/2).
]
No coordinatewise difference is ever separated from its dependent conjugate sum.

For the Lp statement, let p>=2 and q=p/(p-1). The critical envelope gives
[
egin{aligned}
 ||phi_Q||_q^q
 &<=2int_0^{a_*}1,dt
   +2a_*^qint_{a_*}^{infty}t^{-q}dt\
 &=2a_*left(1+{1over q-1}ight)
 =2a_*p.
end{aligned}
]
To avoid assuming a density, convolve the law with a centered Gaussian of variance epsilon. Its characteristic function is phi_Q times the Gaussian multiplier. Inverse Hausdorff--Young, obtained by interpolation between L1-to-Linfinity and Plancherel, gives
[
 ||p_epsilon||_p
 <=(2pi)^(-1/q)||phi_Q||_q
 <=(C_*p)^(1-1/p),
quad C_*=a_*/pi.
]
Since p>1, bounded sets in Lp are weakly compact. Along a weakly convergent subsequence, the Gaussian-smoothed probability measures also converge weakly to the original law, so the weak Lp limit is its density. This proves
[
 ||p_Q||_p<=(C_*p)^(1-1/p).
]

Holder on an interval J yields
[
 P(Q in J)<=(C_*p|J|)^(1-1/p).
]
Let x=C_*|J|<=e^-2 and choose p=log(1/x)>=2. Then
[
 (xp)^(1-1/p)
 =e^{-p+1}p^(1-1/p)
 <=e x p
 =e C_*|J|log(1/(C_*|J|)).
]

Numerically:
gamma_2=0.23736246421253723,
a_*=60.50688695779367,
C_*=19.25994030087079,
e C_*=52.35394573706311.

The current paper's final order-two example has a logarithmically divergent density. Therefore the blow-up as sigma approaches 1 and the linear-in-p Lp growth are the correct endpoint class for a receiver that remembers only E_2.
