# account03/B03 r51 checks

Run: `20260924T091514Z-account03-B03-QFORM-auto11-r51`.

## Algebraic constant check

Main proof uses

`A=2 M sqrt(N)/sqrt(|ab|)`, `B=N/(2|b|)`

and the cutoff estimate

`4 A sqrt(R)+B/R`.

The derivative vanishes at

`R=(B/(2A))^(2/3)`.

At this value,

`4 A sqrt(R)+B/R
 =3*2^(2/3) A^(2/3)B^(1/3)`.

Also

`A^(2/3)B^(1/3)
 =2^(1/3) M^(2/3)N^(2/3)|a|^(-1/3)|b|^(-2/3)`.

Therefore the exact product is

`6 M^(2/3)N^(2/3)|a|^(-1/3)|b|^(-2/3)`.

## Half-Riesz scalar check

For a one-dimensional probability density `f<=N`, the symmetric decreasing extremizer under the cap/mass constraints is `N 1_[ -1/(2N), 1/(2N)]`, and

`N int_(-1/(2N))^(1/(2N)) |x|^(-1/2) dx
 =2 sqrt(2N)`.

After scaling by `2br`,

`sup_x int f(v)|x-2brv|^(-1/2)dv
 <=2 sqrt(N)/sqrt(|br|)`.

Multiplying by the square Jacobian `|a|^(-1/2)` gives the report's

`2 sqrt(N)/(sqrt(|ab|)sqrt(|r|))`.

## Product-projection specialization

Using

`M=2/(rho sigma)`, `N=sqrt(2)/tau`,

Theorem 1 gives

`6 * [2/(rho sigma)]^(2/3) * [sqrt(2)/tau]^(2/3)
 =12 (rho sigma tau)^(-2/3)`.

Thus

`||p_Q||_infinity <=12 (rho sigma tau)^(-2/3)|a|^(-1/3)|b|^(-2/3)`.

For unit norms and `a=b=3`,

`12*(3*9)^(-1/3)=12/3=4`.

## Whole-copy time check

If `||p_Q||_infinity<=H`, then `||p_(Q-Q')||_infinity<=H`. The cap-to-half-Riesz bound is

`E|Q-Q'|^(-1/2)<=2sqrt(2H)`.

With the programme convention

`int |t|^(-1/2)|phi_Q(t)|^2dt=sqrt(2pi)E|Q-Q'|^(-1/2)`,

we obtain

`int |t|^(-1/2)|phi_Q(t)|^2dt<=4sqrt(pi H)`.

For `H=4`, this is

`8sqrt(pi)=14.179630807244127...`.

## Strict-target spectral check

For

`B_*=[[3,0,3],[0,0,3],[3,3,0]]=3 B_0`,

`det(B_*)=-27` and the characteristic polynomial of `B_0` is

`p(mu)=mu^3-mu^2-2mu+1`.

Sign evaluations:

- `p(-2)=-7`, `p(-1)=1`, so one root lies in `(-2,-1)`;
- `p(1/3)=7/27>0`, `p(1)=-1`, so one root lies in `(1/3,1)`;
- `p(1)=-1`, `p(2)=1`, so one root lies in `(1,2)`.

Therefore the three eigenvalues of `B_*` lie in `(-6,-3)`, `(1,3)`, `(3,6)` and all have modulus greater than one.

## Plucker / designated-partner check

For

`s=(1/sqrt(2),1/sqrt(2),0,0)`,
`t=(1/sqrt(6),-1/sqrt(6),2/sqrt(6),0)`,
`v=e_4`,

the only nonzero squared `3x3` minors are

`w_124=w_134=w_234=1/3`.

For `H={1,4}`,

`q_H=2/3`, `r_H=2/9`.

With `Delta=27`,

`J_2(H)=Delta^2(q_H^2-r_H)=729*(2/9)=162`.

Partner density constant:

`129.924435862525374 * 162^(-1/6)
 =55.64656197133566...`.

Whole-copy conversion:

`4sqrt(pi*55.64656197133566...)
 =52.88762884254536...`.

## Boundary sanity checks

- `a ->0`: the theorem's bound diverges like `|a|^(-1/3)`, consistent with the logarithmically singular pure hyperbolic product endpoint.
- `b ->0`: the bound diverges like `|b|^(-2/3)`, consistent with a lone square having an unbounded `y^(-1/2)` density.
- No bound on `p_(R|S)` or `p_(S|R)` is used.
- The same-bank shear `R=T+cS` has determinant one, so it does not change the joint density cap.
- The independent-copy identity is applied only to the whole scalar output `Q-Q'`.

`QFORM_B03_R51_CHECK_PASS`
