# account01/B02 r45 addendum — sharp scalar-chirp L3, Schur two-cross density, and one-sided-pivot/two-sided-rank2 Fourier L1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Integrated Fourier estimate  
Status: **PROVED SUPPORTING THEOREMS / NEWEST account02-B02 RESULT APPLIED / FULL QFORM OPEN / TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**

This addendum continues the same actual-hour canonical run `20260924T042342Z-account01-B02-qform-auto11-r45`. It strengthens the scalar-chirp estimate in `REPORT.md` and changes mechanism again: rather than force another physical E3/E5 packet, it combines a physical scalar square with a critical rank-two crossing *before* frequency integration. All variables below are literal original-coordinate variables or orthonormal coefficient projections whose density caps come from the already reviewed product-projection theorem. No post-rotation independence is used.

## 1. Fresh newest partner actually consumed

Newest completed designated partner now available:

- repository `yspennstate/math-open-problems`
- commit `master` report content pinned in brain handoff at `math-research-brain@10d46f323d41719150b0dde94e63b59bd447324d`
- path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260924T041549Z-account02-B02-QFORM-auto11/REPORT.md`.

Its theorem `QFORM-TWOPAIRS-ONESIDED-TWIST-L1-v1` proves, for literal independent `U1,U2,V1,V2` with cap-one densities and arbitrary same-side function on the U-bank,

`int_R |phi_Q(t)| dt <= 8*pi/sqrt(|ab|)`

for

`Q=F(U1,U2)+(2aU1+c1)V1+(2bU2+c2)V2+d`,

and also `||p_Q||_infinity <=2/sqrt(|ab|)`. It explicitly records that arbitrary quadratic twists on *both* endpoints cannot be handled by simply tensoring per-pair `L2_t` estimates: the Gaussian identity `(U+V)^2` gives a logarithmically divergent `L2_t` characteristic function.

The same partner supplies the exact-target stress family

`Q_eps=X0^2+2Y1Z1+2Y2Z2+2 eps Y3Z3`,

for which every physical `E5` is zero and the best physical `E3` is `eps^2`, yet the theorem gives uniformly

`int |phi_(Q_eps)| <=8*pi`, `||p_(Q_eps)||_infinity <=2`.

I use this exact inequality again in Section 5 as the partner baseline and then prove a receiver allowing arbitrary two-sided curvature once a third physical square couples to at most one of the two crossing banks.

## 2. Sharpening the scalar-square integrated estimate

Let `X` have any probability density `0<=f<=1`, let `c` be arbitrary, and put

`F_c(s)=E exp(i s (X+c)^2)`.

The earlier report proved `int |F_c|^3 <=32*pi`. The following sharp envelope argument improves the constant by exactly a factor two.

### Theorem 2.1 — `QFORM-SCALAR-CHIRP-L3-SHARPENED-v1`

Uniformly in every admissible `f` and shift `c`,

`boxed: int_R |F_c(s)|^3 ds <=16*pi.`                            (2.1)

Consequently

`boxed: ||F_c||_3 <=(16*pi)^(1/3).`                              (2.2)

#### Proof

For `Y=(X+c)^2`, its density on `(0,infinity)` is

`g(y)=[f(sqrt(y)-c)+f(-sqrt(y)-c)]/(2 sqrt(y))`,

so `int g=1` and

`0<=g(y)<=h(y):=y^(-1/2)`.                                      (2.3)

Let `T=1/4`. Then `int_0^T h=1`. Put

`delta=int_0^T(h-g)=int_T^infinity g`.                           (2.4)

For `0<=g<=h`, writing `r=g/h` gives

`h^(3/2)-g^(3/2)=h^(3/2)(1-r^(3/2))
                  >=h^(3/2)(1-r)=h^(1/2)(h-g)`.                 (2.5)

Since `h^(1/2)=y^(-1/4)>=T^(-1/4)` on `[0,T]`,

`int_0^T g^(3/2)
 <=int_0^T h^(3/2)-T^(-1/4) delta`.                              (2.6)

On the tail, `g^(3/2)<=g h^(1/2)<=T^(-1/4)g`, hence

`int_T^infinity g^(3/2)<=T^(-1/4)delta`.                         (2.7)

The deficit cancels, so

`int_0^infinity g^(3/2)
 <=int_0^(1/4)y^(-3/4)dy
 =2 sqrt(2).`                                                     (2.8)

Thus `||g||_(3/2)<=2`. With Fourier convention `hat g(s)=int e^(isy)g(y)dy`, interpolation between `L1->Linf` and Plancherel gives

`||hat g||_3 <=(2*pi)^(1/3)||g||_(3/2)<=2(2*pi)^(1/3)`,          (2.9)

whose cube is `16*pi`. QED.

The envelope step is sharp: centered uniform `X` has `g(y)=y^(-1/2) 1_(0,1/4)(y)`.

### Corollary 2.2 — physical pivot L3

For a general full quadratic form, complete one ORIGINAL nonzero physical diagonal `a=A_ii`:

`Q=a(X_i+h(Z))^2+R(Z)`.

Minkowski and (2.1) give

`boxed: ||phi_Q||_3^3 <=16*pi/|a|.`                              (2.10)

This is a true integrated estimate but, alone, does not imply Fourier `L1`.

## 3. Bounded-density splice: one scalar pivot plus a Schur rank-two cross packet

This theorem allows arbitrary two-sided residual curvature and arbitrary pivot couplings. It is a bounded-density theorem, not a continuity theorem.

Write a nonzero physical scalar pivot as

`A=[[a,b^T],[b,C]]`, `a!=0`,

and its Schur complement as

`S=C-bb^T/a`.                                                     (3.1)

Let `Z` be the remaining original independent coordinates and

`R(Z)=Z^T S Z` (arbitrary affine terms may also be present).

Suppose some literal disjoint physical banks `I,J` among the remaining coordinates have Schur cross block

`B=S[I,J]`

with two positive singular values `sigma1>=sigma2>0`; put

`Delta=sigma1 sigma2`.                                           (3.2)

The completed translation-uniform two-cross theorem gives

`H_(1/2)(R):=sup_u E|R-u|^(-1/2)<=8 Delta^(-1/4)`.               (3.3)

Completing the ORIGINAL pivot square,

`Q=a(X_i+a^(-1)b^TZ)^2+R(Z)`.                                   (3.4)

For fixed `Z`, the conditional density of the square term obeys

`p_(a(X_i+h)^2 | Z)(v)<=|a|^(-1/2)|v|^(-1/2)`                   (3.5)

on the appropriate half-line, hence everywhere after dropping the indicator. Averaging (3.5) gives the density of the full law and therefore

### Theorem 3.1 — `QFORM-PIVOT-SCHUR-TWOCROSS-DENSITY-v1`

`boxed: ||p_Q||_infinity <=8 |a|^(-1/2) Delta^(-1/4).`           (3.6)

No residual coefficient is deleted. All pivot couplings to both banks are retained exactly through the Schur complement.

### Exact overlap-one minor form

Let `I={r1,r2}`, `J={c1,c2}` be disjoint from each other and from the pivot coordinate `i`. The Schur determinant identity is

`D:=det A[{i,r1,r2},{i,c1,c2}]
   =a det S[I,J]`.                                                (3.7)

This is ordinary block Gaussian elimination; no probabilistic change of variables is made. Since a `2x2` matrix has product of singular values equal to the absolute determinant,

`Delta=|det S[I,J]|=|D/a|`.

Thus (3.6) becomes

`boxed: ||p_Q||_infinity <=8 (|a D|)^(-1/4).`                    (3.8)

This is a direct receiver for an overlap-one third-compound minor whenever the overlap coordinate also has a quantitative nonzero physical diagonal. It explains exactly why the remaining grouped-pivot packet is difficult when the overlap diagonal tends to zero: (3.8) has the correct explicit singular dependence and cannot simply be declared uniform.

Continuity is **not** claimed from (3.6)-(3.8).

## 4. New Fourier theorem: a physical square coupled to one bank upgrades an arbitrary rank-two two-sided crossing to L1

The newest partner's one-sided-twist theorem permits arbitrary curvature on only one endpoint bank. The next theorem allows arbitrary quadratic/measurable internal phases on **both** crossing banks, provided a third physical square is present and its shift depends on at most one crossing bank. This is the first nontrivial piece of `QFORM-OVERLAP1-TWOPAIRS-TWOSIDED-CURVATURE-L1-v1` obtained without per-pair `L2` tensorization.

Let `W`, a bank `X`, and a bank `Y` be mutually independent collections of ORIGINAL variables. `W` is scalar with density at most one. After conditioning any further outside original coordinates, assume the phase can be written

`Q=a(W+h(X))^2+F(X)+2 X^T B Y+G(Y)+d`,                           (4.1)

where `a!=0`, `h` is arbitrary measurable (linear in the quadratic-form application), `F,G` are arbitrary real measurable functions, and `B` has **exact rank two**. Write its nonzero singular values as `s1,s2` and

`Delta=s1 s2`.                                                    (4.2)

Let the two-dimensional orthogonal coefficient projections associated with the SVD of `B` have density caps `M_X,M_Y`. For product cap-one original banks the reviewed projection theorem gives `M_X,M_Y<=2`.

### Theorem 4.1 — `QFORM-ONESIDED-PIVOT-RANK2-TWOSIDED-L1-v1`

`boxed:
 int_R |phi_Q(t)|dt
 <= (16*pi/3) 6^(1/4)
    (M_X M_Y)^(3/8)
    |a|^(-1/4) Delta^(-3/8).
}`                                                                  (4.3)

Consequently the law has a continuous `C0` density and

`boxed:
 ||p_Q||_infinity
 <= (8/3) 6^(1/4)
    (M_X M_Y)^(3/8)
    |a|^(-1/4) Delta^(-3/8).
}`                                                                  (4.4)

For original product banks, `M_X,M_Y<=2`, so numerically

`boxed: int|phi_Q| <44.103 |a|^(-1/4) Delta^(-3/8),`             (4.5)

`boxed: ||p_Q||_infinity <7.020 |a|^(-1/4) Delta^(-3/8).`        (4.6)

#### Proof

Integrate only the physical scalar `W` first. Put

`m_t(X)=E_W exp(i a t(W+h(X))^2)`.                               (4.7)

Let `B=U diag(s1,s2)V^T`. Push the complex measure

`m_t(X) exp(i t F(X)) dP_X`

onto `u=U^T X`, obtaining complex density `A_t(u)`. Disintegration and Cauchy--Schwarz give

`|A_t(u)|^2
 <=p_U(u)^2 E(|m_t(X)|^2 | U^T X=u)
 <=M_X p_U(u) E(|m_t(X)|^2 | U^T X=u)`.

Therefore

`||A_t||_2^2 <=M_X E_X |m_t(X)|^2`.                              (4.8)

Likewise, pushing `exp(i tG(Y))dP_Y` onto `v=V^T Y` gives density `B_t(v)` with

`||B_t||_2^2<=M_Y`.                                               (4.9)

The exact-rank-two crossing Plancherel identity then yields

`|phi_Q(t)|
 <=pi (M_X M_Y)^(1/2) Delta^(-1/2)
     |t|^(-1) r(t)`,                                              (4.10)

where

`r(t)=[E_X |m_t(X)|^2]^(1/2)`.                                   (4.11)

The key is that `r` has a genuine integrated gain. Since (2.1) is uniform in every shift,

`int |m_t(X)|^3 dt <=16*pi/|a|`

for every fixed `X`. Moreover

`||r||_3^2
 =||E_X |m_t(X)|^2||_(3/2)
 <=E_X || |m_t(X)|^2 ||_(3/2)
 <=(16*pi/|a|)^(2/3)`,                                           (4.12)

so

`||r||_3 <=(16*pi/|a|)^(1/3)`.                                  (4.13)

For any `T>0`, use `|phi_Q|<=1` on `|t|<=T`. On the tail, Holder with exponents `3` and `3/2` in (4.10) gives

`int_(|t|>T)|phi_Q(t)|dt
 <=pi(M_XM_Y)^(1/2)Delta^(-1/2)||r||_3
   [int_(|t|>T)|t|^(-3/2)dt]^(2/3)
 <=B T^(-1/3)`,                                                    (4.14)

with

`B=2^(8/3) pi^(4/3)(M_XM_Y)^(1/2)
   Delta^(-1/2)|a|^(-1/3)`.                                      (4.15)

Thus

`int |phi_Q| <=2T+B T^(-1/3)`.                                  (4.16)

The minimizer is `T=(B/6)^(3/4)`, and substitution gives

`(4/3)6^(1/4) B^(3/4)`, exactly (4.3). Fourier inversion gives (4.4) and continuity. QED.

### Scope boundary

The proof still requires that the scalar-square shift in (4.1) depend on at most the X-bank (and conditioned outside variables), not simultaneously on both X and Y. If the pivot couples to both crossing banks, `m_t` becomes a genuine two-bank multiplier and (4.8) no longer isolates it on one side of the crossing Plancherel operator. That is the exact remaining interface, not a hidden independence assumption.

## 5. Equation-level application of the newest account02/B02 result and comparison

Apply the newest partner theorem to its exact-target family

`Q_eps=X0^2+2Y1Z1+2Y2Z2+2eps Y3Z3`.

With `a=b=1` in `QFORM-TWOPAIRS-ONESIDED-TWIST-L1-v1`, its actual inequality is

`boxed: int |phi_(Q_eps)| <=8*pi`, `boxed: ||p_(Q_eps)||inf<=2`  (5.1)

for every `eps`, including `eps=0`. This is a completed partner result used at an actual displayed inequality.

The new Theorem 4.1 is deliberately broader but has a weaker constant: use the physical square `W=X0`, `a=1`, the exact rank-two crossing on `(Y1,Y2)|(Z1,Z2)` with `Delta=1`, and product-projection caps `M_X=M_Y=1` on these literal two-coordinate banks. It gives

`int |phi_(Q_eps)| <=(16*pi/3)6^(1/4) <26.224`,                  (5.2)

uniformly in `eps`. More importantly, (5.2) remains valid after adding *arbitrary quadratic/measurable internal phases* `F(Y1,Y2)` and `G(Z1,Z2)` and arbitrary coupling of `X0` to the Y-bank through the shift `h(Y1,Y2)`. Those two-sided twists lie outside the partner theorem's one-sided form.

The bounded-density Schur theorem also applies to the same stress family with pivot `a=1` and residual physical rank-two crossing `diag(1,1)`, giving the independent, correction-safe estimate

`||p_(Q_eps)||inf<=8`.                                            (5.3)

This comparison makes the mechanism distinction explicit: partner (5.1) is sharper on its one-sided source-separated carrier; (4.3) survives arbitrary curvature on both crossing banks; (3.6) survives even two-sided pivot coupling but gives only essential boundedness.

## 6. Consequence for the live proof graph

The newest partner identified the first unpaid edge

`QFORM-OVERLAP1-TWOPAIRS-TWOSIDED-CURVATURE-L1-v1`.

This addendum pays two substantial pieces of it:

1. **quantitative overlap pivot + Schur two-cross:** if the overlap coordinate has `a!=0` and the incident overlap-one `3x3` determinant is `D`, equation (3.8) gives a full-law density payment `8(|aD|)^(-1/4)` with arbitrary two-sided curvature and arbitrary pivot couplings;
2. **one-sided pivot coupling + arbitrary two-sided rank-two curvature:** equation (4.3) gives genuine unweighted Fourier `L1` and a continuous `C0` density.

The genuinely first unpaid local interface is now sharper:

`QFORM-OVERLAP1-BOTH-SIDED-PIVOT-COUPLING-L1-v1` — the overlap coordinate has significant couplings to *both* rank-two crossing banks while its own diagonal may be zero or arbitrarily small. A successful proof must retain the resulting two-bank chirp multiplier jointly; it cannot return to the refuted per-pair `L2` tensorization, cannot delete a small tail, and cannot assume conditional projection caps.

The unrestricted target remains **OPEN**. Full-target continuity remains **OPEN**. No exact-target counterexample to universal unweighted Fourier `L1` was found.
