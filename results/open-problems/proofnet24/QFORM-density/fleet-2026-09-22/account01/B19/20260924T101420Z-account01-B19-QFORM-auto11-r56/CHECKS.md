# account01/B19 r56 deterministic checks

Run: `20260924T101420Z-account01-B19-QFORM-auto11-r56`.

These checks are diagnostics only. The exact proofs are in `REPORT.md`.

## Rank-three peel constants

For the parameterized peel

- `g=6/(m+1)`;
- `eta=3/(m+1)=g/2`;
- `|Hvy|<=m`;
- diffuse partner bound `12/[g(1-d)]=2(m+1)/(1-d)`;
- localization amplitude squared `>(m-5)/(m(m+1))`.

At `d=1/2`:

- `m=6`: diffuse bound `28`; localization amplitude squared `>1/42`, amplitude `>1/sqrt(42)=0.1543033499620919...`;
- `m=10`: diffuse bound `44`; localization amplitude squared `>1/22`, amplitude `>1/sqrt(22)=0.2132007163556104...`.

If the unpeeled total rank-three frame already has maximum row leverage `<=1/2`, the designated account02/B19 `k=3` theorem gives `12/(1-d)`, hence `24` at `d=1/2`.

## One-edge tetrad identities

For `s=S_ab`, `x_i=S_ai`, `y_i=S_bi`, and distinct `i,j` away from `{a,b}`,

`D_ij=s S_ij-x_j y_i=det S[{a,i},{b,j}]`.

Hence

`x_i y_j-x_j y_i=D_ij-D_ji`,

so

`sum_(i<j)(x_i y_j-x_j y_i)^2 <=2 W_dis(S)`.

With `omega=sqrt(W_dis(S))` and `tau=sqrt(2 omega)=sqrt(2)W^(1/4)`, the report's two estimates are

`eps_star <=2W^(1/4)+W^(1/2)/mu+sqrt(2)R W^(1/4)/mu`,

`eps_col <=sqrt(2)W^(1/4)+(1+sqrt(2))W^(1/2)/mu`.

The displayed common bound in REPORT.md dominates both.

## Explicit target gate

At constructed diagonal residual `<=1/2`, the rank-one collinear branch is excluded if

`sqrt(2)W^(1/4)+(1+sqrt(2))W^(1/2)/mu<1/2`.

A sufficient split is

`sqrt(2)W^(1/4)<1/4`, giving `W<1/1024`,

and

`(1+sqrt(2))W^(1/2)/mu<1/4`, giving

`W<mu^2/[16(1+sqrt(2))^2]`.

## Finite regression diagnostics

A local deterministic Python check generated signed rank-one-plus-diagonal matrices with small symmetric off-diagonal perturbations. Among 571 samples satisfying the collinear branch conditions, the explicit rank-one construction violated no bound; the maximum observed `lhs/rhs` was `0.15532647226466803`.

A separate 1000-sample star-near construction tested the pre-simplified star estimate; there were zero violations and the maximum observed `lhs/rhs` was `0.4915771808029075`.

No numerical test is used as proof.
