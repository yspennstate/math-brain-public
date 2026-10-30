# B12 FEI sprint: region-2 two-block cancellation and exact x monotonicity

Status: **new rigorous enclosure identities and bounded executable drivers delivered; the assigned M=96, c=0.003 x in [1,2] shard is NOT claimed certified in this run. Full FEI remains OPEN.**

## Live state consumed

The current owner sprint assigns fleet01/B12 the unfinished read-once region 2, x in [1,2], for the pinned M=96, K=40, C0=6.4548, c=0.003 candidate. The authenticated candidate is `cert_vi_h96k40.npz`, 70,354 bytes, Git blob `1e2a1a5c293fa7b6ec9885b7a410910d6589be80`. The previous B12 run already derived the exact secant identity for the A term and a joint A+F derivative bound, but did not execute the pinned binary candidate in its native environment.

The newest TASKS correction is also incorporated: the unrestricted FEI target 6.4547837 is stale because the externally recovered Numaro seed exceeds it, while the read-once upper-bound calculation is a different restricted-class statement. Likewise, the earlier universal cancellation target `B_can <= 2.227... I` is refuted by the supplied composition construction. Nothing below uses either stale universal target.

## 1. Start from the exact region-2 decomposition

Write

- `p = 2^-x`, with `1 <= x <= 2` for this account's shard;
- `v = 2^-y`, so the second probability is `q = 1-v > 1/2`;
- `lambda = -log2(1-v) = v ell(v)/ln 2`;
- `Ghat(t) = G_num(t) + c(1-2^-t)`.

The existing certificate algebra gives

```
Phi/v = A + B + C + D + E + F + G,
A = [Ghat(x)-Ghat(x+lambda)]/v,
B = Ghat(y)/(1-v),
C = -8 p x,
D = -8(1-v)(1-p)ell(v)/ln2,
E = -8(1-p),
F = [Psi(p)-Psi(p(1-v))]/v,
G = Psi(1-v)/v.
```

The previous enclosure improved A and A+F, but still intervalized the candidate-margin pieces and the y-only smooth terms in separate blocks.

## 2. Exact two-block identity

Define

```
K0(t) = G_num(t) + Psi(2^-t).
```

Because `2^-lambda = 1-v`, the margin contribution in A is exactly `-c p`, while the margin contribution in B is exactly `+c`. Hence their total is exactly `c(1-p)`. Also `p(1-v)=2^{-(x+lambda)}`. Therefore

```
A + F = [K0(x)-K0(x+lambda)]/v - c p,
B       = G_num(y)/(1-v) + c.
```

Combining C+E gives the exact identity

```
Phi/v = [K0(x)-K0(x+lambda)]/v + J(x,y),

J(x,y) = G_num(y)/(1-v) + Psi(1-v)/v
         + c(1-p) - 8[1+p(x-1)]
         - 8(1-p)(1-v)ell(v)/ln2.
```

This is algebraic; no approximation or candidate-specific monotonicity is used.

For the first divided-difference block,

```
[K0(x)-K0(x+lambda)]/v
 = -(ell(v)/ln2) average_{t in [x,x+lambda]} K0'(t),
K0'(t) = s_j - (ln2) 2^-t Psi'(2^-t)
```

on a candidate segment of slope `s_j`. This keeps the G/Psi correlation while removing the certificate margin from the derivative enclosure entirely.

## 3. New exact x-monotonicity lemma

The second improvement is specific to the B12 domain and is stronger than minimizing its pieces separately.

**Lemma.** For fixed y and `1 <= x <= 2`, the function J(x,y) above is strictly decreasing in x for `c=0.003`.

**Proof.** Put

```
a(v) = 8(1-v)ell(v)/ln2 > 0.
```

Only the last three terms of J depend on x. Since `p=2^-x`, differentiation gives

```
dJ/dx = p { c ln2 - 8[1-ln2(x-1)] - a(v) ln2 }.
```

For `1 <= x <= 2`,

```
1-ln2(x-1) >= 1-ln2,
```

so, even after discarding the additional negative term `-a(v)ln2`,

```
dJ/dx <= p { c ln2 - 8(1-ln2) } < 0.
```

At `c=0.003`, the uniform positivity gap in the braces after reversing sign is

```
8(1-ln2) - c ln2 = 2.45274311398...
```

Thus the exact minimum over every x-cell in this shard is attained at its upper endpoint `x_hi`. QED.

This recovers the small positive margin that v1 had to minimize at `x_lo`, while simultaneously keeping it correlated with the much larger negative C+E+D block.

## 4. One-dimensional y block after eliminating x

Set `x*=x_hi`, `p*=2^-x*`. Then it remains to bound the one-variable function `J(x*,y)` on a y-node cell. Its derivative is

```
dJ/dy = s/(1-v) - ln2 v G_num(y)/(1-v)^2
        - ln2 [Psit'(v)-Psit(v)/v]
        + 8(1-p*)[1-ell(v)],
```

where `s` is the exact candidate slope on the y segment and `Psit(v)=Psi(1-v)`.

The delivered v2 enclosure takes the best of three rigorous lower bounds:

1. direct outward interval evaluation of the whole J block;
2. endpoint evaluation when the derivative interval has a fixed sign;
3. a centred mean-value lower bound when the derivative interval straddles zero.

The result is then maxed with v1, and v1 itself maxes with the previous B12 secant enclosure. Hence each successive driver is fail-safe: it can only improve the certified lower bound, never replace an older valid bound by a weaker one.

## 5. Independent checks

Two independent high-precision checks were executed without using the certificate candidate, so they are checks of the mathematics only and are **not** promoted to certificate evidence.

`selfcheck_twoblock.py` used 4,000 random points and an arbitrary nonmonotone piecewise-linear G at 80 decimal digits. It found:

```
max |original seven-term formula - grouped two-block formula| = 6.06608190164e-75
max |explicit margin pieces - c(1-p)|                 = 1.17527181762e-78
max |analytic J_y derivative - numerical derivative|  = 3.44407808596e-76
```

`selfcheck_twoblock_v2.py` used 20,000 random `(x,y)` points at 80 digits. It found:

```
max |analytic J_x derivative - numerical derivative| = 1.68675167092e-80
largest sampled dJ/dx                              = -2.01571226783
minimum sampled easy negativity gap              =  2.4528502909
analytic uniform gap at x=2                      =  2.45274311398
```

Both checks PASS. The uniform gap is an analytic proof, not a sampling inference; the samples only check the implementation of the derivative formula.

## 6. Delivered code and exact identities

The files in this run are:

- `r2_two_block_enclosure.py`: v1 two-block regrouping and joint y block; committed Git blob `ec623c8a5a809e60ed471ec37691fa86c9a5874c`, SHA-256 `55eb8f0f6205388f79283b3a88611978aa9c9e07fd4445e7a7eacf1ed805887d`.
- `selfcheck_twoblock.py`: Git blob `4dcc998c159b7b29e35303965fc42b0a760e1d2a`, SHA-256 `c9f27246129df71b88fcd4cbd3c995cfeb0a6241169155cc1ad041ac1ba10624`.
- `selfcheck_twoblock_output.json`: Git blob `c2b196835ae6fa227310cb0dcb9ca061c31afa98`, SHA-256 `7ae3f0e13a4789ce1c17e2d210de325e6ac8b349d222bd2ee1ba0368559b7f32`.
- `r2_two_block_enclosure_v2.py`: stronger x-monotone version; Git blob `313c79561bc52f08e927e393254577332a745830`, SHA-256 `23f32eaa90d6e1379cb6b0ea15f00ffa9c9e3216d5c1111bac07810410b02b56`.
- `selfcheck_twoblock_v2.py`: Git blob `644b61d6a82a7b9383520981e4ba6d24be2002cb`, SHA-256 `af54f4731a8159e80abe9414ec79f849ecea6b384d3fbb651b077ba622110f3c`.
- `selfcheck_twoblock_v2_output.json`: Git blob `fe73331c173cef3f1a2cd22bf3c4c7bc20c191ae`, SHA-256 `dadc74ac880de456cde23485a5971d7748262c1f3bcbf8babb28a63d06a1d661`.

Both Python drivers syntax-compile in the native executor. The self-checks were actually executed there.

## 7. What is still blocked

The private GitHub connector authenticates the pinned 70,354-byte NPZ and exposes its base64 representation, but this invocation has no approved byte bridge that materializes that connector payload into the native executor. Recomputing the M=96 value-iteration candidate is not a substitute: the repository log shows it required 121 iterations and roughly 4,093 seconds in its original run, and a regenerated NPZ would not by itself prove byte identity with the pinned candidate.

Therefore I did **not** claim a production M=96 interval run, did not concatenate fictional shard logs, and did not mark x in [1,2] VERIFIED. The assigned certificate remains unfinished until the v2 driver is run against the exact pinned candidate bytes.

## 8. Next step

Run `r2_two_block_enclosure_v2.py` on small y-index shards of the exact pinned M=96 candidate. If survivors remain, export the binding cells and inspect whether the residual loss is in the K0 divided-difference range or in the one-dimensional J derivative range. The next analytic tightening should target only that binding block; in particular, a y-cell whose J' interval contains zero can be attacked by interval Newton on the explicit scalar derivative rather than further two-dimensional subdivision.

No settled FEI certificate was rerun, no audit was performed, and no statement here closes full FEI.
