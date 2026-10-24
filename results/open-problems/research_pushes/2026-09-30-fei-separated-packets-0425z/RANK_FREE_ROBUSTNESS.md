# Rank-free Booleanity control for approximate code packets

2026-09-30 UTC. Proved structural estimate; no Fourier-entropy payment or degree-preserving rounding theorem is claimed. Full FEI remains open.

Use the code-packet notation of BOOLEAN_COMPARISON.md: f is actual Boolean, C has minimum distance D, g is its Fourier truncation to C+B(0,d), delta=||f−g||_2^2, and h_z(x)=sum_c chi_c(z)u_c(x) is the decoded field.

## Theorem

If D>6d, then

    E_(x,z)(|h_z(x)|−1)^2
      <=E_(x,z)(h_z(x)^2−1)^2
      <=sqrt(delta)[5^(d/2)+1]^3.                        (1)

The constant is independent of ambient dimension and code rank. It is exponential in packet radius d. Pointwise sign rounding gives Boolean functions within the displayed average squared error, but those rounded functions need not have degree at most d.

## A genuine Boolean fiber bound

Let W=C-perp. Fix a coset x_0+W, with syndrome z. For two different frequencies S,T of weight at most d, S+T is nonzero of weight at most 2d, hence is not in C. Therefore the characters chi_S restricted to this coset form an orthonormal family.

The coefficient of the actual Boolean f against chi_S on this coset is

    E_(x in x_0+W) f(x)chi_S(x)
       =sum_(c in C) fhat(c+S)chi_c(x_0)
       =hzhat(S).                                      (2)

The last equality uses unique decoding, D>2d. Bessel's inequality on the coset and f^2=1 give, for every z separately,

    ||h_z||_2^2=sum_(|S|<=d)hzhat(S)^2<=1.               (3)

This is stronger than just the averaged normalization E_z||h_z||_2^2=1−delta. It removes code-rank dependence from the following norm bound.

## Moment matching and the sixth norm

For each integer 0<=k<=6,

    E_x g(x)^k = E_(x,z) h_z(x)^k.                       (4)

To verify (4), expand products of packet terms. Their code-center sum lies in C and the total residual degree is at most kd. A nonzero code-center sum has weight at least D>kd, so it cannot be cancelled by those residual frequencies in the physical expectation. Thus precisely the zero code sums survive, exactly as when averaging over independent z. This is an exact finite algebraic identity.

Since h_z has ordinary degree at most d in x, standard Boolean-cube hypercontractivity and (3) give

    ||h_z||_6<=5^(d/2)||h_z||_2<=5^(d/2).

Moment matching at k=6 implies

    ||g||_6<=5^(d/2).                                   (5)

Only the x-variable degree is used, not d plus the code rank.

## Booleanity defect

Set u=||g|−1| and v=|g|+1. Since f is Boolean, pointwise u<=|g−f|, so ||u||_2<=sqrt(delta). Also u<=v. Therefore, by Cauchy–Schwarz,

    E(g^2−1)^2=E u^2 v^2
                <=E u v^3
                <=||u||_2 ||v||_6^3
                <=sqrt(delta)[5^(d/2)+1]^3.             (6)

The second and fourth moment identities in (4) transfer the left side of (6) exactly to E_(x,z)(h_z^2−1)^2. Finally (|h_z|−1)^2<=(h_z^2−1)^2 pointwise, proving (1).

## What has and has not been obtained

The proof uses the actual Boolean source on each affine coset, not a finite-moment relaxation of arbitrary amplitudes. Consequently it is compatible with earlier no-go results for approximate Booleanity plus only finitely many autocorrelations: the code-fiber projection hypothesis is additional structure.

The result produces a rank-free bound tending to zero with off-packet mass. It does not bound the entropy cost of rounding, and sign rounding may introduce large real degree or influence. Thus it does not yet turn the exact paid degree reduction into an approximate FEI induction. Low-degree Boolean stability theorems may supply a separate repair step, but no such theorem is silently imported here.

The parent independently checked the coset coefficients, orthonormality/Bessel step, moment matching, hypercontractive normalization, and inequality (6) before publication. Standard hypercontractivity is credited; novelty of this particular structural application is unverified. No executable script or numerical certificate is included.
