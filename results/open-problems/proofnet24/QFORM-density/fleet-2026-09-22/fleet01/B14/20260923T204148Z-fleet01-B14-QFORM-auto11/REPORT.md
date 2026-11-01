SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B14, 2026-09-23T20:41:48Z.
attacking: exact quantile-expansion localization plus a whole-law opposite-square/receiver synthesis of the completed fleet02/B14 r41 theorem, with arbitrary translations, remote fragments and unbounded supports retained before reciprocal-score payment.

# fleet01/B14 — exact quantile localization and a rough opposite-square receiver branch

Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`.  
Role: translations and localization.  
Status: **NEW ZERO-LOSS LAW-CLASS LOCALIZATION THEOREM + NEW STRICT-TARGET ROUGH-LAW BRANCH + DESIGNATED-PARTNER APPLICATION. FULL QFORM OPEN.**  
Continuity: separate; only essential boundedness is asserted below.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 0. Fresh control and exact sources


The completed designated-partner theorem actually used below is fleet02/B14 r41, read from the source snapshot

`yspennstate/math-open-problems@71480f46e12acc9037cef4379ae74e07b3e55ea5`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260923T173217Z-fleet02-B14-QFORM-r41/REPORT.md`.

Its `QFORM-PREJENSEN-RECEIVER-MIXTURE-v1` states the following. For `4/3<r<2`, `p=r/(r-1)`, independent cap-one original-coordinate driver `Z`, receiver `W`, a conditional core `T_z` independent of `W`, and

`Q=T_Z+s(Z)+dW^2+(2c^T Z+e)W`,

put `R0=sqrt(d^2+||c||_2^2)`. If `K(z)=||p_{T_z}||_p` and `E K(Z)^p<infinity`, then

`||p_Q||_infinity <= 2^[3(r-1)/(2r)] (2-r)^(-1/r) R0^[-(r-1)/r] [E K(Z)^p]^(1/p)`.       (0.1)

The partner's same report also proves exact mass homogeneity when an unnormalised score cap scales linearly with fragment mass, so distant fragments may be summed without loss when a whole receiver/driver anchor is retained.

I also use fleet02/B14's later Gaussian-mixture localization barrier, read in the same source snapshot at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260923T183045Z-fleet02-B14-QFORM-auto11/REPORT.md`.

It supplies the smooth cap-one random-center family `X_N=M_N+(2N)^(-1)G`, with `M_N` uniform on `{4,8,...,4N}`, final density `<0.799`, but latent Gaussian inverse-scale budget `E T_N^(-1/2)=2N` for `T_N=1/(4N^2)`.

## 1. Exact quantile-expansion characterization of every cap-one marginal

### Theorem 1.1 — `QFORM-QUANTILE-EXPANSION-LOCALIZATION-v1`

A Borel probability measure `mu` on `R` has a density `f` satisfying `0<=f<=1` a.e. if and only if there exists a nondecreasing measurable map

`T:(0,1)->R`

such that

`T(v)-T(u) >= v-u` for every `0<u<v<1`,                         (1.1)

and

`mu=T_# Unif(0,1)`.                                               (1.2)

Thus the class of arbitrary cap-one laws is **exactly** the class of monotone one-expanding images of one unit interval. Jumps of `T` encode arbitrary gaps / distant fragments, and divergence of `T(u)` as `u` approaches an endpoint encodes unbounded support. No moment, support-radius, diameter, connectedness, smoothness, or finite-fragment hypothesis is present.

#### Proof: cap-one law implies expansion

Let `F(x)=mu((−infinity,x])`. Since `f<=1`,

`0<=F(y)-F(x)<=y-x` for `x<y`;                                   (1.3)

hence `F` is continuous and one-Lipschitz. Let

`T(u)=inf{x:F(x)>=u}`.                                             (1.4)

Continuity of `F` gives `F(T(u))=u` for `0<u<1`, and the probability integral/quantile identity gives (1.2). For `u<v`,

`v-u=F(T(v))-F(T(u)) <= T(v)-T(u)`,                              (1.5)

which is (1.1).

#### Proof: expansion implies cap one

Conversely, let `U` be uniform on `(0,1)` and `X=T(U)` with `T` nondecreasing and satisfying (1.1). For every finite interval `I=(a,b)`, the set `T^{-1}(I)` is an interval (possibly empty). If `u<v` both belong to it, then

`v-u <= T(v)-T(u) < b-a`.                                        (1.6)

Therefore

`P(X in I)=|T^{-1}(I)| <= |I|`.                                  (1.7)

By decomposition of open sets into countably many disjoint intervals and regularity, `mu(E)<=Leb(E)` for every Borel set `E`. Hence `mu` is absolutely continuous and its Radon--Nikodym density is at most one a.e. QED.

### Corollary 1.2 — exact product-law reformulation of full QFORM

Let `U_1,...,U_n` be iid `Unif(0,1)`. The admissible independent product laws in the owner target are exactly

`X_i=T_i(U_i)`,                                                   (1.8)

with the `T_i` nondecreasing and one-expanding. Consequently, if `D(n,A,T)` denotes the essential density height of

`T(U)^T A T(U)`,                                                   (1.9)

then the full optimal QFORM constant satisfies the exact identity

`C_QFORM = sup { D(n,A,T) : n>=1, s_3(A)>=1, each T_i satisfies (1.1) }`.   (1.10)

There is **no approximation loss and no localization constant** in (1.10). The spectral hypothesis is untouched because the matrix `A` is untouched.

This reformulation is deliberately compatible with the live bounded-diameter and fixed-fragment-count counterexamples: (1.1) permits arbitrarily many and arbitrarily large jumps. It therefore does not smuggle in either refuted reduction.

## 2. Exact translation gauge: reduce to median zero with arbitrary affine terms

For each `T_i`, define

`m_i=T_i(1/2)`, `S_i(u)=T_i(u)-m_i`.                              (2.1)

Every `S_i` remains nondecreasing and one-expanding, and `S_i(U_i)` has median zero. With `m=(m_i)`,

`T(U)^T A T(U)
 = S(U)^T A S(U) + (2Am)^T S(U) + m^T A m`.                       (2.2)

Therefore:

### Corollary 2.1 — `QFORM-MEDIAN-GAUGE-ZERO-TAX-v1`

If one proves, with constant `C`, the density bound

`||p_{X^T A X+b^T X+c}||_infinity <= C`                          (2.3)

for all independent **median-zero** cap-one inputs, all `s_3(A)>=1`, and arbitrary `b,c`, then the original unrestricted target follows with the **identical** constant `C`.

Arbitrarily large coordinate translations are thus exactly removable without moments. What cannot be removed is the resulting arbitrary affine vector `b`; it is part of the legal localized target. This is the correct translation interface for conditioning arguments.

## 3. A translation-uniform L^p bound for an opposite-square core

The next lemma is the analytic input used to apply the designated partner theorem.

### Lemma 3.1 — `QFORM-OPPOSITE-SQUARE-LP-v1`

Let `X,Y` be independent real variables with densities at most one. Let `a,b>0`, and let `xi,eta` be arbitrary real shifts. For every `p>1`, set

`T=a(X-xi)^2-b(Y-eta)^2`.                                        (3.1)

Then for every `p>1` (and in particular for the range `2<p<4` used below),

`boxed:
 ||p_T||_p
 <= 2^(-2/p) (p+1)^((p+1)/p)
    (ab)^(-(p-1)/(2p)). }`                                       (3.2)

The estimate is uniform in `xi,eta` and uses no support or moment information.

#### Proof

For `U=a(X-xi)^2`, its density `g_a` on `(0,infinity)` obeys

`g_a(u) <= (a u)^(-1/2)`, `int g_a=1`.                            (3.3)

Fix `1<q<2`. Among probability densities under the decreasing envelope `(a u)^(-1/2)`, the `L^q` norm is maximized by filling the envelope from zero until mass one. Since

`int_0^(a/4) (a u)^(-1/2) du=1`,                                 (3.4)

we obtain

`||g_a||_q <= [2^(q-1)/(2-q)]^(1/q) a^(-(q-1)/q).`               (3.5)

The same holds for `g_b`. The density in (3.1) is the convolution of `g_a` with the reflected `g_b`. Choose

`q=2p/(p+1)`, so `1+1/p=2/q`.                                    (3.6)

Young's inequality and (3.5) give

`||p_T||_p
 <= ||g_a||_q ||g_b||_q
 <= 2^(-2/p)(p+1)^((p+1)/p)(ab)^(-(p-1)/(2p))`,                  (3.7)

which proves (3.2). QED.

At the especially simple choice `p=3`,

`boxed: ||p_T||_3 <= 4 (ab)^(-1/3).`                              (3.8)

The same bound holds pointwise in any external driver `z` if `xi=xi(z)` and `eta=eta(z)`, because the constants are completely translation-uniform.

## 4. Completed fleet02/B14 r41 applied to an actual rough-law inequality

### Theorem 4.1 — `QFORM-ROUGH-OPPOSITE-SQUARE-RECEIVER-v1`

Let `X,Y,W,Z_1,...,Z_m` be mutually independent cap-one variables. Let `a,b>0`, `d,e in R`, `c in R^m`, and put

`R0=sqrt(d^2+||c||_2^2)>0`.                                      (4.1)

Allow arbitrary measurable `xi(Z),eta(Z),s(Z)`. Define

`Q=a(X-xi(Z))^2-b(Y-eta(Z))^2+s(Z)
   +dW^2+(2c^T Z+e)W`.                                           (4.2)

Then for every `2<p<4`,

`boxed:
 ||p_Q||_infinity
 <= 2^(-1/(2p)) (p+1)^((p+1)/p)
    ((p-1)/(p-2))^((p-1)/p)
    (ab)^(-(p-1)/(2p)) R0^(-1/p). }`                             (4.3)

In particular, at `p=3`,

`boxed:
 ||p_Q||_infinity
 <= 2^(19/6) (ab)^(-1/3) R0^(-1/3)
 =8.9796963865... (ab R0)^(-1/3). }`                              (4.4)

A slightly smaller clean numerical coefficient follows by taking `p=19/6`:

`2^(-3/19)(25/6)^(25/19)(13/7)^(13/19)
 =8.95214823194...`,                                              (4.5)

with scaling `(ab)^(-13/38) R0^(-6/19)`.

#### Proof and explicit partner use

Condition on `Z=z`. The core

`T_z=a(X-xi(z))^2-b(Y-eta(z))^2`                                 (4.6)

is independent of the receiver `W`; Lemma 3.1 gives the **uniform** core budget

`K_p=2^(-2/p)(p+1)^((p+1)/p)(ab)^(-(p-1)/(2p)).`                 (4.7)

Apply fleet02/B14 r41 equation (0.1) with

`r=p/(p-1)`, so

`(r-1)/r=1/p`, `1/r=(p-1)/p`, `2-r=(p-2)/(p-1)`.                 (4.8)

Its receiver factor becomes

`2^(3/(2p)) ((p-1)/(p-2))^((p-1)/p) R0^(-1/p).`                  (4.9)

Multiplying (4.7) and (4.9) gives exactly (4.3). This is an equation-level application of the completed designated-partner theorem, not a restatement of it. QED.

### Zero-tax fragment interpretation

Every constant in (4.3) depends only on `(a,b,R0,p)`. The driver law is kept whole until the partner's score averaging is paid. Therefore arbitrary jumps in the quantile maps of the `Z_i`, arbitrarily remote fragments, unbounded supports, and absence of moments do not enter the estimate. More strongly, fleet02/B14 r41's subprobability homogeneity shows that any positive decomposition whose unnormalised score cap satisfies `L_j<=H m_j` sums linearly in the fragment masses. This is the safe localization order:

`whole cap-one law -> optional positive localization -> aggregate score -> reciprocal singularity`,

not

`active fragment -> normalize/rescale -> reciprocal singularity -> mix`.

## 5. A strict full-target branch, including a diffuse third spectral resource

The theorem above is a probability compiler. It gives a genuine QFORM branch when the shifts/functions arise from an original-coordinate quadratic form.

Consider the active homogeneous matrix

`A_* = diag(a,-b) direct_sum S`,                                  (5.1)

where

`S=[[H,c],[c^T,d]]`                                               (5.2)

on the original-coordinate bank `(Z,W)`, with `H` an arbitrary symmetric `m x m` matrix. Cross terms between `X` or `Y` and `Z` are allowed: conditioning on `Z` turns them into the linear shifts `xi(Z),eta(Z)` in (4.2), with their completed-square corrections absorbed into `s(Z)`. Arbitrary additional outside original coordinates and arbitrary couplings to the active block are also allowed after conditioning on that outside block; they only change affine terms and the shifts.

Because `S` is symmetric,

`||S||_op >= ||S e_W||_2 = sqrt(d^2+||c||_2^2)=R0`.              (5.3)

Hence if

`a>=1`, `b>=1`, `R0>=1`,                                        (5.4)

then the active principal block has the two eigenvalues `a,-b` and at least one further eigenvalue of modulus at least one. Interlacing preserves the three-large-eigenvalue count after arbitrary outside couplings are restored. Thus (4.4) yields the strict target-valid estimate

`boxed: ||p_Q||_infinity <= 2^(19/6) <8.980 }`                   (5.5)

throughout this branch, with no support, translation, tail, fragment, moment, dimension, or internal-`H` parameter.

A useful diffuse test is

`a=b=1`, `d=0`, `H=0`, `c_m=m^(-1/2)(1,...,1)`.                  (5.6)

Every individual star coefficient tends to zero, but `||c_m||_2=1`. The active matrix has nonzero spectrum

`{1,-1,1,-1}`,                                                   (5.7)

so (5.5) remains dimension free. This is not a localized-good-minor argument; the third smoothing resource is an aggregate original-coordinate bank.

## 6. Actual comparison with the partner's smooth random-center barrier

Use the completed fleet02/B14 random-center law

`X_N=M_N+(2N)^(-1)G`,                                            (6.1)

where `M_N` is uniform on `{4,8,...,4N}`. Its final marginal density is `<0.799<1`, while `T_N=1/(4N^2)` and `E T_N^(-1/2)=2N` in the latent Gaussian representation.

Take independent copies and define, for any `m>=1`,

`Q_{m,N}=X_{N,1}^2-X_{N,2}^2
        +2 X_{N,3} m^(-1/2) sum_{j=1}^m X_{N,3+j}.`               (6.2)

Its coefficient matrix is exactly the diffuse target family (5.6), with spectrum `{1,-1,1,-1,0,...}`. The whole-law rough theorem (5.5) gives

`boxed: ||p_{Q_{m,N}}||_infinity <=2^(19/6)<8.980}`              (6.3)

uniformly in both `m` and `N`, despite arbitrarily separated random centers and unbounded Gaussian tails.

Now condition first on all Gaussian component centers. Every coordinate has the same variance `T_N`. In the checked arbitrary-matrix Gaussian component compiler, with `D=T_N I` and `B=D^(1/2) A D^(1/2)=T_N A`, the four nonzero eigenvalues of `A` are `+1,-1,+1,-1`; hence

`e_3(B^2)=4 T_N^6`.                                               (6.4)

The component-first certificate is therefore

`||p_{Q_{m,N}|centers}||_infinity
 <= (I_3/(2pi))(4T_N^6)^(-1/6)
 = (I_3 2^(2/3)/pi) N^2
 =1.48678636... N^2`,                                             (6.5)

with `I_3=2.942468198...` from the completed Gaussian theorem. Averaging the conditional suprema does not remove this `N^2` factor.

Thus on the **same strict indefinite/off-diagonal target family**,

`whole cap-one law:  ||p_Q||_infinity <8.980`,

while

`component-first inverse scale: <=1.4868 N^2`.                   (6.6)

This applies the designated partner's completed localization mechanism and its later random-center barrier to an actual inequality. It isolates the issue cleanly: remote translations are harmless when the active marginal is aggregated first; the loss is generated by paying reciprocal latent scale before the translated components are recombined.

## 7. What this resolves and what remains

This run resolves B14's law-topology / translation question in an exact form stronger than bounded-support approximation:

1. **Every** cap-one marginal is exactly a one-expanding quantile image of one unit interval. No tails or fragments need be discarded.
2. Arbitrary common coordinate translations may be gauged to median zero with **zero loss**, provided arbitrary affine terms are retained.
3. The completed fleet02/B14 receiver theorem combines with an opposite-square core to pay a genuine diffuse, indefinite, strict-target family uniformly under arbitrary rough laws.
4. The partner's random-center Gaussian obstruction is bypassed on that family by aggregating the whole law before inverse-scale payment.

The **unpaid implication is structural**. From the bare hypothesis `s_3(A)>=1`, one still has to force, in original product coordinates and before active fragment normalization, either a block/conditioning pattern of the form paid in Section 5 with quantitative `a,b,R0`, or one of the already completed ridge / projected-volume / grouped-hub / pair / scalar-pivot exits. The quantile representation does not itself manufacture that matrix certificate. Therefore the unrestricted theorem is **not** claimed solved.

No uniform pointwise Fourier decay, arbitrary-joint coarea estimate, independence after rotation, bounded-diameter localization, fixed fragment-count bound, moment bound, or small-random-error perturbation was used.
