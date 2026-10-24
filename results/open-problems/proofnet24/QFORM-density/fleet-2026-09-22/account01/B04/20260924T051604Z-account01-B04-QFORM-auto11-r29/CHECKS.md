# account01/B04 r29 deterministic checks

Run: `20260924T051604Z-account01-B04-QFORM-auto11-r29`

These are finite arithmetic/symbolic checks for the explicit stress family in `REPORT.md`. They are not numerical evidence for the unrestricted conjecture.

## Householder carrier

Take `v=(1,2,3,4,5,6)^T`, `v^T v=91`, and `R=I-2vv^T/91`.

- `R^T R=I` exactly by the Householder identity.
- Every off-diagonal entry is `-2ij/91 !=0`.
- Diagonal entries are `1-2i^2/91`; since `2i^2` is in `{2,8,18,32,50,72}`, none equals `91`.

For `M_m` with `m` copies of each row `e_j^T R/sqrt(m)`, summing row outer products gives

`M_m^T M_m=sum_j sum_(r=1)^m m^(-1) R^T e_j e_j^T R=I_6`.

Hence the pure-cross symmetric embedding has nonzero spectrum `(+1)^6,(-1)^6`.

## Row-triple weights

Three rows from distinct direction groups are mutually orthogonal, each with squared norm `1/m`, hence

`z_S=det((1/m)I_3)=m^(-3)`.

Any triple with two rows from the same group has two identical row directions, hence `z_S=0`.

Supported triple count:

`C(6,3)m^3=20m^3`,

so

`Z=sum_S z_S=20m^3*m^(-3)=20`.

Complement-group pairing gives `10m^3` disjoint edges. Each has weight

`sqrt(z_S z_T)=m^(-3)`.

With `lambda=1` on those edges, every supported triple vertex has load exactly one and

`nu_perp>=10m^3*m^(-3)=10`.

The dual point `x_i=1` gives `G_(1/2)^*<=Z=20`; the theorem gives `G_(1/2)^*>=20`, hence equality.

Density coefficient:

`6 sqrt(e) 20^(-1/6)=6.004269244596687...`.

## Pair-anchored fourth-volume comparison

For a fixed pair of rows from two distinct groups, anchor Gram determinant is `m^(-2)`. A nonzero four-row Gram determinant requires two more distinct groups among the remaining four groups. There are `C(4,2)m^2=6m^2` choices, each determinant `m^(-4)`. Therefore

`H_ab=6m^2*m^(-4)=6/m^2`.

The account03/B04 pair-E4 coefficient would therefore scale as

`2^(17/8)(6/m^2)^(-1/8)=2^(17/8)6^(-1/8)m^(1/4)`.

This diverges with `m`; the r29 global matching bound stays constant.

## account02/B04 r19 carrier-face masses

Choose carriers from groups 1,2,3. Because every supported triple has weight `m^(-3)`:

- exact carrier triple: `W_123=m^(-3)`;
- a fixed carrier pair plus one noncarrier row: `(m-1)+3m=4m-1` choices, so `W_ij=(4m-1)m^(-3)`;
- one fixed carrier plus two noncarrier rows from distinct remaining groups: `(m-1)^2+6m(m-1)+3m^2=10m^2-8m+1`, so `W_i=(10m^2-8m+1)m^(-3)`;
- no carrier: `e_3(m-1,m-1,m-1,m,m,m)=20m^3-30m^2+12m-1`, so `W_empty=(20m^3-30m^2+12m-1)m^(-3)`.

At `m=64`, denominator `64^3=262144` and

`W_empty=5120767/262144=19.534175872802734...`,
`W_i=40449/262144=0.15430068969726562...`,
`W_ij=255/262144=0.000972747802734375`,
`W_123=1/262144=0.000003814697265625`.

The r19 complementary-face inequality gives

`G_H >=2[sqrt(W_empty W_123)+3sqrt(W_i W_ij)]
      =0.09077276176664519...`.

The resulting Theorem-D certificate is

`6 sqrt(e) G_H^(-1/6)=14.756133187970226...`.

Ratio to the r29 global matching certificate:

`14.756133187970226 / 6.004269244596687
 =2.457606843871874...`.

## Canonical disjoint-pair corollary

For arbitrary row-triple weights `z_S`, let `D_S=sum_(T disjoint S)z_T`, `Delta=sum_S z_S D_S`, and `w_S=z_SD_S/Delta`.

Under `pi(S,T)=z_Sz_T/Delta` on ordered disjoint pairs, symmetry gives the same marginal `w` on both endpoints. Since `S,T` are disjoint, for every physical row `i`,

`2P(i in S)=P(i in S)+P(i in T)=P(i in S union T)<=1`.

Thus all row marginals are at most `1/2`.

Also

`log G_row(w)=log Delta-E_w log D_S >=log(Delta/Z)`

because `D_S<=Z`. This verifies `G_(1/2)^*>=Delta/Z`.

For `G=MM^T>=0`, Hadamard-Fischer gives `det G_S det G_T>=det G_(S union T)` for disjoint triples. Each six-set has exactly `C(6,3)=20` ordered complementary decompositions, hence

`Delta>=20 e_6(G)`

and therefore

`G_(1/2)^*>=20 e_6(G)/e_3(G)`.

Marker: `QFORM_B04_R29_DISJOINT_MATCHING_CHECK_PASS`.
