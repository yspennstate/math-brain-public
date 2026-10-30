# Exact/scalar checks for fleet01/B04 r20

Run: `20260923T212739Z-fleet01-B04-QFORM-auto11-r20`.

These checks corroborate the analytic proof; they are not a substitute for it.

## 1. Gaussian small-ball constant

From

`K=2^(3/4) sqrt(pi) Z1^(-1/4)`

and

`1_{|x|<rho} <= e^v exp(-v x^2/rho^2)`,

Fourier inversion gives

`Q_R(rho) <= [e^v Gamma(1/4)/(sqrt(2pi) v^(1/4))] K sqrt(rho)`.

The derivative of `v-log(v)/4` vanishes uniquely at `v=1/4`, so

`H1=2^(3/4)e^(1/4)Gamma(1/4)=7.829376757708328417...`.

Then

`C*=4 sqrt(2H1)=2^(23/8)e^(1/8)sqrt(Gamma(1/4))`

`=15.828457165708428873...`.

## 2. Stress-family algebra

`B=[[1,3],[3,1]]`, so

`det B=-8`, `D=8`, `spec(B)={4,-2}`, `kappa=2`,

and

`B^(-1)=[[-1/8,3/8],[3/8,-1/8]]`.

For `u=(1,1)`, `v=(1,-1)`:

`u^T B^(-1)u=1/2`,
`v^T B^(-1)v=-1`,
`u^T B^(-1)v=0`.

Let `V=I_4-J_4/2`. Since `J_4^2=4J_4`,

`V^2=I_4-J_4+J_4=I_4`,

so `V` is orthogonal. Therefore

`N_eps=diag(2,eps,eps,eps)V`

has singular values `(2,eps,eps,eps)` and all entries nonzero for `eps>0`.

Consequently

`Z1=||N_eps||_F^2=4+3eps^2`,

`E3(N_eps)=3*(4 eps^4)+eps^6=12eps^4+eps^6`.

## 3. Dense completion

With `delta=10^(-3)`, `eta=10^(-2)`, and E having four rows `delta u` followed by four rows `delta v`,

`E^T E=8 delta^2 I_2`, hence `||E||_op=sqrt(8)delta`.

Because `||B^(-1)||_op=1/2`,

`||E B^(-1) E^T||_op <=4 delta^2`.

The exact cross block of `E B^(-1)E^T` between the first and last residual four-coordinate banks vanishes because `u^T B^(-1)v=0`. Thus the Schur complement residual cross block is exactly `N_eps`, and the ambient residual cross block is also exactly `N_eps`.

All ambient matrix entries are nonzero:

- B: entries `1,3`;
- E: entries `+/-delta`;
- first residual same-side block: every entry `eta+delta^2/2`;
- second residual same-side block: every entry `eta-delta^2`;
- residual cross block: entries of `N_eps`, all nonzero.

## 4. Spectral target

For

`A0=diag(B,[[0,N_eps],[N_eps^T,0]])`,

the eigenvalues include `4,-2,+2,-2`; the remaining six are `+/-eps` with multiplicity three each. Hence `s_4(A0)=2`.

The perturbation satisfies

`||A_eps-A0||_op <= 4eta+sqrt(8)delta+4delta^2`

`=0.04+0.002828427124746190...+0.000004`

`=0.04283242712474619...`.

Therefore

`s_4(A_eps) >= 1.9571675728752538... >1`,

so at least four eigenvalues of the symmetric `A_eps` have modulus greater than one.

## 5. Numerical stress point eps=10^(-6)

New theorem:

`C* (D kappa)^(-1/4) Z1^(-1/8)`

`=15.828457165708429 * 16^(-1/4) * (4+3e-12)^(-1/8)`

`=6.655046444819971...`.

Designated partner support-defect theorem:

`6*4^(1/6)*(12e-24+e-36)^(-1/6)`

`=49960.99065933556...`.

Ratio partner/new:

`7507.233957506526...`.

## 6. Scaling check

Under `A -> cA`,

`D -> c^2 D`, `kappa -> |c| kappa`, `Z1 -> c^2 Z1`.

Thus

`(D kappa)^(-1/4) Z1^(-1/8)`

scales as `|c|^(-3/4)|c|^(-1/4)=|c|^(-1)`, exactly as a density bound must.
