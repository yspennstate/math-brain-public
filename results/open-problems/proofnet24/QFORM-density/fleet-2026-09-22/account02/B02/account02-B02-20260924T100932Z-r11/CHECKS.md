# Deterministic checks for account02/B02 r11

Status: PASS.

## Constants

Using `e=exp(1)`:

- `4 sqrt(2e) = 9.326575926388497...`.
- `sqrt(228)*4sqrt(2e) = 140.828208184430...`.
- `sqrt(228)*8sqrt(2e)*(3/2)^(-1/4) = 254.505302160471...`.
- `8sqrt(2e) = 18.65315185277699...`.
- `pi*(1800 e^2)^(1/3) = 74.4338293313885...`.
- `(1800 e^2)^(1/3)/2 = 11.8465118713490...`.

## Exact family A_k

For each `k>=2`, `A_k` is the direct sum of:

1. scalar `[1]` on `W`;
2. a star with center `V1` and leaf vector `k^(-1/2) 1_k`;
3. a second identical star with center `V2`.

Each normalized star has spectrum `{-1,0,...,0,+1}` because the leaf vector has Euclidean norm one. Therefore the full nonzero spectrum is exactly `{-1,-1,1,1,1}`.

The leaf-to-center cross block is the `2k x 2` matrix with orthogonal columns, each of norm one, so its singular values are `1,1` and `Z2=1`.

Each nonzero `2x2` minor chooses one leaf from each star and both center columns. There are `k^2` such minors; each determinant has modulus `1/k`, so the squared-minor weights are `1/k^2` and sum to one. Each leaf occurs in exactly `k` such minors, hence its row marginal is `1/k`.

For an arbitrary disjoint physical cross cut, one normalized star contributes rank at most one: its single center coordinate cannot belong to both sides, so all crossing edges from that component have a common physical row or a common physical column. With two star components, the total cross rank is at most two; the isolated diagonal pivot contributes no disjoint cross edge. Hence `E3=E5=0` on every disjoint physical cut.

## L3 star calculation

For exterior degree one, `q=1`, `Z1=1`, the sharp volume theorem gives

`|phi_star(t)| <= min(1,B|t|^(-1/2))`, `B=sqrt(e*pi)`.

The crossover is `t0=B^2`. Therefore

`int_R |phi_star|^3`
` <=2[t0+B^3 int_(t0)^infinity t^(-3/2)dt]`
` =2[B^2+2B^2]=6e*pi`.

Combining two such factors with the completed scalar-square bound

`||phi_(W^2)||_3 <=(2pi)^(1/3)5^(2/3)`

gives

`int |phi_Qk| <=(6e*pi)^(2/3)(2pi)^(1/3)5^(2/3)`
` =pi(1800e^2)^(1/3)`.
