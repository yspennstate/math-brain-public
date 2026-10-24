# Deterministic checks for r43

All checks below concern the exact active three-dimensional carrier used in `REPORT.md`.

Let

`H=[[0,sigma,0],[sigma,alpha,delta],[0,delta,gamma]]`.

Direct expansion along the first row gives

`det H = -sigma^2 gamma`.

Hence if `H` is the full nonzero carrier of a rank-three symmetric matrix and `s=s_3(H)>0`, then

`|sigma^2 gamma|=|det H|=|mu_1 mu_2 mu_3| >= s^3`.

Numerical constants:

- `3*2^(5/3) = 9.524406311809198...`;
- `3*2^(2/3) = 4.762203155904598...`;
- `3*4^(2/3) = 7.559526299369239...`;
- `2*sqrt(2*pi) = 5.0132565492620005...`.

The scalar/dependent-pair receiver is used with `K<=sqrt(2)`, `M<=2`, `beta=sigma`, and pair-square coefficient `gamma`; therefore

`3(2MK)^(2/3)|beta^2 gamma|^(-1/3)
 <=3(4sqrt(2))^(2/3)s^(-1)
 =3*2^(5/3)s^(-1)`.

For the literal endpoint `A_*=[[0,1,0],[1,0,0],[0,0,1]]`, all retained variables are original coordinates, so `K<=1` and the retained pair has joint cap `M<=1`; the same receiver gives

`3*2^(2/3)=4.762203155904598...`.

These identities were also independently evaluated symbolically/numerically during the run. No probabilistic independence after rotation is used in these checks.
