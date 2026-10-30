SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B02, 2026-09-24T08:06:56Z.
attacking: QFORM-R47-STRONGHUB-TWOSIDED-CURVATURE-OR-DIFFUSE-E2-L1-v1; test whether genuine two-sided curvature can be paid by a local unweighted Fourier-L1 receiver, and if not spend the third physical smoothing direction through a fractional-potential interface.

# Early calculation — two-sided 2x2 Fourier criticality and a target-valid third-square repair

Let U1,U2,V1,V2 be independent Uniform[-1/2,1/2] and

Q4=(U1+V1)^2+(U2+V2)^2.

In the U=(U1,U2), V=(V1,V2) block decomposition the two same-bank quadratic blocks and the physical cross block are all I2: Q4=U^T U+2U^T V+V^T V. Thus the cross block is literally invertible, det C=1, but both product banks carry quadratic curvature.

Put Z=U1+V1. Its density is h(z)=(1-|z|)1_{|z|<=1}. Hence

g(t)=E exp(it Z^2)=2 int_0^1 exp(it z^2)(1-z) dz
=2 int_0^1 exp(it z^2) dz-(exp(it)-1)/(it).

The Fresnel tail integration-by-parts estimate gives

2 int_0^1 exp(it z^2) dz=e^{i pi/4} sqrt(pi) t^{-1/2}+O(t^{-1}),  t->+infinity.

Therefore

g(t)=e^{i pi/4} sqrt(pi) t^{-1/2}+O(t^{-1}),
|g(t)|^2=pi/t+O(t^{-3/2}).

Since the two coordinate pairs are independent, phi_Q4(t)=g(t)^2 and

int_R |phi_Q4(t)| dt=infinity.

So a literal invertible physical 2x2 crossing does NOT admit a universal local unweighted Fourier-L1 theorem once arbitrary quadratic curvature is retained on both banks. This is a mechanism obstruction, not a QFORM counterexample: Q4 has only two nonzero eigenvalues.

Embed it into the exact target by adding an independent W~Uniform[-1/2,1/2]:

Q5=(U1+V1)^2+(U2+V2)^2+W^2.

The physical coefficient matrix has eigenvalues 2,2,1,0,0. On the r47 full cut L={U1,U2}, R={V1,V2,W}, the cross block is [I2  0], so x1*x2=1>247/576. Every disjoint physical cross block of the full five-coordinate matrix has rank at most two (the only off-diagonal edges are U1--V1 and U2--V2), hence every physical E3 and E5 is exactly zero: D', the reviewed E3 sharp-HY receiver, and D5 have no currency anywhere on this exact-target family.

Nevertheless Y1=U1+V1, Y2=U2+V2, W are independent and each has density cap at most one. Thus Q5 is a diagonal three-square form in three genuinely independent grouped variables. The proved scalar-square L3/Hölder mechanism gives int |phi_Q5| <= 50 pi, while the diagonal density theorem gives ||p_Q5||_infinity<=pi. The third independent square repairs the logarithmic local Fourier divergence without any false pointwise-decay step.

This suggests changing mechanism: the remaining r47 physical-diagonal/strong-hub branch should spend a third smoothing direction through a fractional potential of the two-sided rank-two remainder, rather than demand that the two-sided 2x2 carrier itself be Fourier-L1.
