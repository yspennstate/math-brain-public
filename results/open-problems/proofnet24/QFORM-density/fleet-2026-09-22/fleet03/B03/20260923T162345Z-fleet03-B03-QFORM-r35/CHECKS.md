# fleet03/B03 r35 deterministic checks

Run: `20260923T162345Z-fleet03-B03-QFORM-r35`.

## Algebraic completion checks

Write

`Q=(h+h_j x+h_c w)^2/a + 2 sigma u (v x-q w)`

and impose only

`m=q h_j+v h_c`,

which follows from

`h_j=beta v+m q`, `h_c=-beta q+m v`, `v^2+q^2=1`.

### Complete in `w`

With

`ell_w=h_c(h+h_jx)/a-sigma q u`,

subtracting `a ell_w^2/h_c^2` from the non-`w` part gives exactly

`R_w=2 sigma (m/h_c)u x
    +2 sigma(q/h_c)u h
    -a sigma^2 q^2 u^2/h_c^2`.

A symbolic expansion of `R_w(actual)-R_w(target)` reduces identically to zero after the substitution `m=q h_j+v h_c`.

### Complete in `x`

With

`ell_x=h_j(h+h_cw)/a+sigma v u`,

subtracting `a ell_x^2/h_j^2` from the non-`x` part gives exactly

`R_j=-2 sigma(m/h_j)u w
    -2 sigma(v/h_j)u h
    -a sigma^2 v^2 u^2/h_j^2`.

Again the symbolic difference reduces identically to zero after `m=q h_j+v h_c`.

## Exact-coloop frame check

For a Parseval two-frame `sum_k z_k z_k^T=I_2` and a row `z_j` with `||z_j||=1`,

`sum_{k!=j} z_k z_k^T=I_2-z_jz_j^T=w_jw_j^T`,

where `w_j` is a unit vector orthogonal to `z_j`. For any vector parallel to `z_j`, the quadratic form of the left side is zero, hence every `z_k`, `k!=j`, is orthogonal to `z_j`. Thus `z_k=c_k w_j` and `sum c_k^2=1`. This validates the normalized aggregate projection `W=sum c_k X_k` used in the report.

## Scalar Riesz constants

For a probability density bounded by `M`, the centered-interval extremizer gives

`M int_{-1/(2M)}^{1/(2M)} |x|^(-1/2) dx =2 sqrt(2M)`.

For `R=S+2bUY`, with selector density cap `M_Y`, coefficient marginal cap `M_U`, conditioning on the full background gives

`sup_s E|R-s|^(-1/2)
 <=4 sqrt(2 M_Y M_U/|b|)`.

Plancherel gives

`|phi_R(t)|^2 <= min(1,A/|t|)`,
`A=pi M_U M_Y/|b|`.

The weighted time integral is checked exactly by splitting at `t=A`:

`2 int_0^A t^(-1/2)dt + 2A int_A^infinity t^(-3/2)dt
 =4 sqrt(A)+4 sqrt(A)=8 sqrt(A)`.

## Target-scale constant arithmetic

Using `L0=sqrt(e)`:

- `4 sqrt(2) L0 = 9.326575926388498...`;
- `4 sqrt(2) L0^(3/2) = 11.97556054015085...`;
- if `M=max(|h_j|,|h_c|)>=m/sqrt(2)`, then the packet scale gives
  `sqrt(|a|/(|sigma|mM)) <=2^(3/4)/s_3(A)`;
- `2^(3/4)=1.681792830507429...`;
- therefore
  `2^(13/4)e^(3/4)=20.140411857733373...`;
- the partner collision coefficient is twice this,
  `2^(17/4)e^(3/4)=40.280823715466745...`.

All constants in `REPORT.md` agree with these values.

`QFORM_B03_R35_CHECK_PASS`
