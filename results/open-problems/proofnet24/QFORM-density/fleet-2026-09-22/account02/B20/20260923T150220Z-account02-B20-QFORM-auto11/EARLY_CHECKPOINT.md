# Early checkpoint — self-replication of the nested absolute-rank-one tube

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains open.

Source state used: newest completed designated partner account03/B20 r33 (`math-open-problems@82fb3ecce909f03acbbe69b2e9d0def93f85194b`). Its unpaid nested packet is an ORIGINAL-coordinate cut `S sqcup T=[n]` with `M=A[S,T]`, `E=||M||_F^2`, `S4>(63/64)E`, `s2(M)<1/64`, and initially `E>1241405/2097152`.

## New calculation

Set `tau=1/64`. Let `M1=s1 u v^T` be the top singular component. Since `s2(M)<tau`, the symmetric off-diagonal matrix with cross block `M1` has rank at most two and the residual cross operator norm is `<tau`. Since `s3(A)>=1`, Eckart--Young gives

`max(||A[S,S]||op,||A[T,T]||op)>1-tau=63/64`.

On a side `C` with this norm, the zero-diagonal part has operator norm `>1-2tau=31/32`, hence Frobenius square `>961/1024`. A random two-colouring `C=P sqcup Q` therefore has a realization with

`||A[P,Q]||_F^2>961/4096`.

Relabel the colours so that the appropriate top singular vector of the old cross block has squared mass at least `1/2` on `P`. Strong-top-four plus `s2<1/64` gives

`s1(M)^2>(63/64)E-3/4096`.

Thus the arm from `P` to the old opposite bank has operator norm squared greater than one half of this quantity. The new literal cross block `M'=A[P,P^c]` therefore satisfies

`||M'||_F^2 > 961/4096 + (1/2)[(63/64)E-3/4096]
              = 1919/8192 + (63/128)E =:F(E)`.

The affine map has the exact fixed point

`E_inf = (1919/8192)/(1-63/128)=1919/4160=0.461298076923...`.

Hence every unpaid rank-one-tube reproduction with `E>=E_inf` again has `E'>E_inf`. For the partner's initial `E_*=1241405/2097152`, the first reproduced cross has

`E'>141090307/268435456=0.525602351874...`.

This is a dimension-free non-degradation statement; no random variable is rotated and no small quadratic tail is discarded. Next: route every reproduced cut through the pinned D5 / grouped-rank-three / E2 gates, then isolate the finite first curvature-flip packet forced because consecutive same-side reproductions strictly shrink a nonempty physical bank.
