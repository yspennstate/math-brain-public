# Checks for `20260924T061035Z-account01-B14-QFORM-auto11`

These are algebra/arithmetic consistency checks for `REPORT.md`, not an independent review of the full QFORM conjecture.

## 1. Bathtub constant

For the extremizer of the abstract constraints `0<=b<=H`, `int b=M`, take

`b=H 1_[0,M/H]`.

Then

`int b(s)s^(-1/2)ds = H*2*sqrt(M/H)=2sqrt(HM)`.

So the constant in `QFORM-HALF-KERNEL-BATHTUB-v1` is exact for the abstract cap+mass problem.

## 2. Affine completion in the exact-target block

Expand

`2(W+U/2+alpha/4)^2`
`=2W^2+2WU+alpha W +(1/2)U^2 +(alpha/2)U + alpha^2/8`.

Also

`(3/2)(U+(beta-alpha/2)/3)^2`
`=(3/2)U^2 +(beta-alpha/2)U + constant`.

The two lines sum to

`2W^2+2WU+2U^2+alpha W+beta U+constant`.

And

`-4(Y-gamma/8)^2=-4Y^2+gamma Y+constant`.

Thus equation (6.1) is exact up to an output translation.

## 3. Spectrum

The `W,U` block `[[2,1],[1,2]]` has eigenvalues `3,1`. Adding the `Y` coefficient `-4` gives

`spec(A_*)={3,1,-4}`.

The diagnostic block with `Y` coefficient `-1` has spectrum `{3,1,-1}`.

## 4. Constants

With `a=2`, `d=3/2`,

`H=pi/sqrt(3)=1.8137993642342178...`.

For `|e|=4`, the third-square branch is

`2sqrt(H/4)=sqrt(H)=1.3467736870885985...`.

For `|e|=1`, its coefficient at fragment mass `m` is

`2sqrt(H)*sqrt(m)=2.693547374177197... sqrt(m)`.

The crossover with the cap branch solves

`H=2sqrt(H m)`, hence

`m=H/4=pi/(4sqrt(3))=0.45344984105855446...`.

For `N>=3`, `1/N` lies below the crossover, so `N` equal fragments give the displayed `2.693547374177197... sqrt(N)` fragment-first certificate.

## 5. Interlacing scope

If `A_*` is an original-coordinate principal submatrix of a larger symmetric `A`, Cauchy interlacing with `mu(A_*)=(3,1,-4)` gives at least two ambient eigenvalues `>=1` and at least one ambient eigenvalue `<=-4`. Thus the ambient extension lies inside the owner's exact three-large-eigenvalue target.
