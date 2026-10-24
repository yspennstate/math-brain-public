# The Gaussian extremal hard edge: full Gumbel law via the second factorial moment

Agent note, 2026-06-29. Target: upgrade `conj:gumbel` to a THEOREM for the source Gaussian
ensemble. With the r-point collapse (`gumbel_kpoint.md`) the whole law reduces to the second
factorial moment at the centered scale:
```
  E[(N_t)_2] = sum_{(T1,T2) ordered distinct} P{ smin(A_{T1}) <= t_m, smin(A_{T2}) <= t_m } -> lambda^2,
```
where N = gamma m, t_m = e^{x-b_m}, lambda = e^{d_F x}, E[N_t] -> lambda, and b_m the centering of
`conj:gumbel`. This note isolates exactly what is rigorous for GAUSSIAN A and what is not.

NOTATION. F in {R,C}, d_F in {1,2}. A in F^{N x m} iid standard (proper for C) Gaussian, rows
a_1,...,a_N in F^m. For an m-subset T, A_T is the m x m row submatrix. Pairs are classified by the
SUBSET CODIMENSION
```
  D := m - |T1 ∩ T2|,    1 <= D <= m   (distinct ordered pairs).
```
(Beware: the manuscript's "D" in the prob:pc / (m-1)-normal picture is shifted by one from this
clean subset codimension; here D = number of private rows on each side, |T_i \ (T1∩T2)| = D.)
Write p_1 = P{smin(A_T) <= t_m} = F_m(t_m), so binom(N,m) p_1 = lambda (1+o(1)).

================================================================================
## 1. The EXACT reduction (rigorous, distribution-free, no two-projection lemma needed)

Fix a pair (T1,T2) with |T1∩T2| = m-D. Let S = T1∩T2 (the shared rows), P_i = T_i \ S (the D
private rows of side i), so the three blocks A_S, A_{P_1}, A_{P_2} are INDEPENDENT (disjoint rows).
Condition on A_S. The two events
```
  E_i = { smin(A_{T_i}) <= t_m },   i = 1,2,
```
depend on A_S and on the disjoint private blocks A_{P_1}, A_{P_2} respectively, hence are
CONDITIONALLY INDEPENDENT given A_S, and (by exchangeability of the iid private rows) identically
distributed. Writing the single deterministic function
```
  q(A_S) := P{ smin(A_{S∪P}) <= t_m | A_S }      (P a generic fresh D-row private block),
```
we get the EXACT identities
```
  P{E_1 ∩ E_2} = E_{A_S}[ q(A_S)^2 ],     p_1 = E_{A_S}[ q(A_S) ].
```
Define the conditional second-moment ratio (the "association" / overlap moment)
```
  M_m(D) := P{E_1 ∩ E_2} / p_1^2 = E[q^2]/(E q)^2 = 1 + Var(q)/(E q)^2  >= 1.
```
This is EXACT for any ensemble; only the value of M_m(D) is model-dependent. Note M_m(D) depends on
the scale t_m and on m (write M_m(D, t_m) when needed); it is NOT yet the limiting Beta moment.

Counting ordered pairs by codimension (choose T1, then c = m-D shared from its m rows and D fresh
from the other N-m):
```
  #{ ordered (T1,T2) : codim D } = binom(N,m) binom(m,D) binom(N-m,D).
```
The codimension law of a uniform pair is the hypergeometric / Vandermonde weight
```
  P_Vand(D) = binom(m,D) binom(N-m,D) / binom(N,m),   sum_{D=0}^m P_Vand(D) = 1
```
(Vandermonde: sum_D binom(m,D) binom(N-m,D) = binom(N,m)). Therefore, summing the per-pair
probability over all ordered distinct pairs and pulling out the COMMON factor (binom(N,m) p_1)^2,
```
  E[(N_t)_2] = sum_{D=1}^m binom(N,m) binom(m,D) binom(N-m,D) p_1^2 M_m(D)
             = (binom(N,m) p_1)^2 * sum_{D=1}^m P_Vand(D) M_m(D)
             = lambda^2 (1+o(1)) * E_Vand[ M_m(D) ].
```
**This reduction is rigorous and exact.** The entire problem is now
```
  (GOAL)   E_Vand[ M_m(D) ] = sum_{D=1}^m P_Vand(D) M_m(D)  ->  1.
```
Since M_m(D) >= 1 and sum P_Vand = 1, GOAL is equivalent to the UPPER bound
E_Vand[M_m(D)] <= 1 + o(1): everything reduces to upper-bounding the conditional overlap moment
M_m(D), uniformly enough in D.

The split is dictated by the Vandermonde mass. P_Vand concentrates at the typical codimension
Dbar = m(1-1/gamma) = Theta(m) with O(sqrt m) spread; the small-D range is a lower-tail
large-deviation event with EXPONENTIALLY small mass: for D = o(m),
P_Vand(D) = binom(m,D)binom(N-m,D)/binom(N,m) <= (e^2 (gamma-1) m^2 / D^2)^D / binom(N,m), and for
fixed D, P_Vand(D) = Theta(m^{2D} / binom(N,m)) = Theta(m^{2D} e^{-h(gamma) m}). Fix epsilon in
(0, beta_c) with the rarity rate R(epsilon) > d_F s_crit (`IIB_overlap_smallD.md` Sec.4; here
s_crit = h(gamma)/d_F is the critical exponent, so there is NO exponential room left -- see Sec.3).
Split GOAL at D = epsilon m:
```
  E_Vand[M_m] = sum_{D >= epsilon m} P_Vand(D) M_m(D)   (BULK)
              + sum_{1 <= D < epsilon m} P_Vand(D) M_m(D)   (SMALL-D, incl. near-diagonal D=1,2).
```

================================================================================
## 2. BULK (D >= epsilon m): the lambda^2, rigorous for Gaussian

Here the shared block A_S is (m-D) x m with D = Theta(m), hence WELL-CONDITIONED whp
(smin(A_S) ~ sqrt m - sqrt(m-D) = Theta(sqrt m), no hard-edge heavy tail), and the two
least-singular-value events reduce cleanly to the two-projection picture. Conditioning on A_S, the
shared orthocomplement W = span(A_S)^perp ⊂ F^m has dim D; by Gaussian rotational invariance the
private rows project to iid standard Gaussians on W, and the two near-null directions u_1, u_2 ∈ W
(bottom right singular vectors of the two private Gram blocks in W) are INDEPENDENT and, again by
bi-unitary invariance of the Gaussian, HAAR-UNIFORM on the unit sphere of W ≅ F^D and independent of
the singular magnitudes. Hence their overlap is EXACT:
```
  |rho|^2 = |<u_1,u_2>|^2 ~ Beta( d_F/2, d_F(D-1)/2 )   (exactly, Gaussian).
```
The Gaussian two-slab/two-disk estimate (source ACHA Lemma, eqs. real-cond/complex-cond; the
non-Gaussian analogue is `IIB_lemma_2D.md`, proved) gives, for normals at fixed overlap rho with
|rho| <= 1-kappa_0,
```
  P{E_1 ∩ E_2 | A_S, rho} = (1+o(1)) p_1^2 (1-|rho|^2)^{-d_F/2},   uniformly in such rho.
```
Averaging the EXACT Beta overlap reproduces the closed-form enhancement
```
  M(D) := E[(1-|rho|^2)^{-d_F/2}]
        = Gamma(d_F(D-2)/2) Gamma(d_F D/2) / Gamma(d_F(D-1)/2)^2     (D >= 3)
        = 1 + d_F/(2D) + O(D^{-2}).
```
[Check: 1-|rho|^2 ~ Beta(d_F(D-1)/2, d_F/2); E[Y^{-d_F/2}] = B(b-a,a)/B(b,a) =
Gamma(b-a)Gamma(b+a)/Gamma(b)^2 with a=d_F/2, b=d_F(D-1)/2, b-a=d_F(D-2)/2, b+a=d_F D/2; the ratio
~ exp(a^2/b) = 1 + (d_F/2)/(D-1) + ... = 1 + d_F/(2D) + O(D^{-2}). Finite iff b>a iff D>=3.]

So for D >= epsilon m, M_m(D) <= (1+o(1)) M(D) = 1 + O(1/m), UNIFORMLY. There is one rare event to
absorb: |rho| > 1-kappa_0 even at D >= epsilon m. Its Beta probability is
P{1-|rho|^2 < kappa_0} ~ kappa_0^{d_F(D-1)/2} <= e^{-c(kappa_0) epsilon m}, and on it we use the
trivial q <= p_1, i.e. M_m(D) <= 1/p_1 = binom(N,m)/lambda <= e^{h(gamma) m}/lambda. Choosing
kappa_0 small enough that c(kappa_0) epsilon > h(gamma) (possible: c(kappa_0) = (d_F/2)log(1/kappa_0)
-> infty as kappa_0 -> 0, epsilon fixed) makes this contribution e^{-(c epsilon - h(gamma)) m} -> 0.
Therefore
```
  BULK = sum_{D >= epsilon m} P_Vand(D) M_m(D)
       in [ (1-o(1)) * 1 ,  (1+o(1)) * sum_{D>=epsilon m} P_Vand(D) ]  ->  1,
```
using M_m(D) >= 1 for the lower bound and M_m(D) <= 1+o(1) plus sum_{D>=epsilon m} P_Vand <= 1 for
the upper. **The bulk is in place for Gaussian and supplies exactly the lambda^2.**

================================================================================
## 3. SMALL-D and the NEAR-DIAGONAL: what is needed, and why it is the residual

For 1 <= D < epsilon m the mass P_Vand(D) is exp-small, so it suffices to bound M_m(D) by ANY
POLYNOMIAL in m, uniformly:
```
  (R-poly)   M_m(D, t_m) <= poly(m)   uniformly for all 1 <= D < epsilon m.
```
Given (R-poly): sum_{1<=D<epsilon m} P_Vand(D) M_m(D) <= poly(m) * P{D < epsilon m}
<= poly(m) * e^{-delta m} -> 0, where delta = R(epsilon) - 0 > 0 from the rarity rate. Together with
BULK -> 1 this gives E_Vand[M_m] -> 1, i.e. E[(N_t)_2] -> lambda^2, i.e. (with the r-point collapse)
the Gaussian Gumbel law. So the ENTIRE remaining content is (R-poly).

Why (R-poly) is NOT delivered by the bulk machinery. The two-projection estimate of Sec.2 is uniform
only for |rho| <= 1-kappa_0; at small D the Haar overlap concentrates near |rho| = 1 (Beta(d_F/2,
d_F(D-1)/2) puts mass d_F(D-1)/2 = O(1) near the right edge), and indeed the limiting moment
M(D) = E[(1-|rho|^2)^{-d_F/2}] DIVERGES at D = 2 (b = a) and at D = 1 (W is a line, u_1 = u_2,
|rho| = 1). The clean factorization q(A_S) ~ c(A_S) t_m^{d_F} likewise breaks down, because the
conditional density factor c(A_S) has a HEAVY TAIL coming from a near-singular shared block. So the
near-diagonal D = 1, 2 must be handled by a regularized, genuinely finite-m computation, NOT by the
limiting Beta moment.

### 3.1 The near-diagonal computed (D=1, real; the mechanism and the size of M_m)

This is the worst case, and it pins down the truth. Take F = R, D = 1: T1 = S ∪ {p1},
T2 = S ∪ {p2}, |S| = m-1, w = unit null direction of the (m-1) x m shared block A_S (dim W = 1).
A rank-one update / secular-equation computation gives, conditionally on A_S, the EXACT leading
hard-edge law of the completion:
```
  smin(A_{T_i}) ≈ |<a_{p_i}, w>| / sqrt(1 + R_i),   R_i = a_{p_i}^* (A_S^* A_S)^+ a_{p_i},
```
where (A_S^*A_S)^+ is the pseudo-inverse on V = span(A_S). Here <a_{p_i},w> ~ N(0,1) (it is the
W-component of the private row) and R_i (a function of the V-component) are INDEPENDENT given A_S.
The factor sqrt(1+R_i) is the inverse-participation correction: R_i ~ ||a||^2 / smin(A_S)^2 is large
exactly when A_S is near-singular. Hence
```
  q(A_S) = P{ smin(A_{T_i}) <= t | A_S } ≈ E_{R}[ min( sqrt(2/pi) t sqrt(1+R), 1 ) ],
```
the cap "min(.,1)" being the regularization that the bare factorization misses (when A_S itself is
within t of singular, the completion is singular regardless of the private row, and q saturates).

Sizes. The smallest singular value of the (m-1) x m wide Gaussian block has the hard-edge law
P{smin(A_S) <= g} ≈ 2 m g^2 for g << 1/sqrt m (Laguerre hard edge, real, codim-1 block: density of
smin ∝ g). Writing G_S = smin(A_S), R ≈ 1/G_S^2 and q ≈ min(c t / G_S, 1), c = sqrt(2/pi):
```
  E q  ≈ ∫ min(c t/g, 1) dP(G_S<=g) ≈ ∫_{ct}^{1/sqrt m} (c t/g) (4 m g) dg + (G_S<ct term)
       ≈ 4 c m t ∫_{ct}^{1/sqrt m} dg ≈ 4 c sqrt(m) t = Theta(sqrt(m) t) = p_1.   ✓ (matches F_m)
  E q^2 ≈ ∫_{ct}^{1/sqrt m} (c t/g)^2 (4 m g) dg + ...
        ≈ 4 c^2 m t^2 ∫_{ct}^{1/sqrt m} dg/g = 4 c^2 m t^2 log( 1/(c sqrt(m) t) ).
```
The integral ∫ dg/g produces a LOGARITHM of the scale, log(1/(sqrt m t)) ≈ b_m ≈ h(gamma) m at the
CENTERED scale t = t_m = e^{-b_m}. Therefore
```
  M_m(1) = E[q^2]/(E q)^2 ≈ [4 c^2 m t^2 * h(gamma) m] / [4 c^2 m t^2] = h(gamma) m / ... = Theta(m).
```
**M_m(1) = Theta(m): polynomial, not O(1) and not 1/p_1.** The naive limit (Beta moment) would say
"infinity"; the trivial bound says 1/p_1 = e^{Theta(m)}; the TRUTH at the centered scale is Theta(m),
the divergence cut to a single power of m by the cap, with the size set by the log of the scale
log(1/t_m) = Theta(m). Then the D=1 contribution is
```
  P_Vand(1) M_m(1) = [m(N-m)/binom(N,m)] * Theta(m) = Theta(m^3) / binom(N,m) = Theta(m^3) e^{-h m} -> 0.  ✓
```
(Complex D=1, and D=2 in both fields, are MILDER: the shared-block hard-edge exponent grows with D
[(m-D) x m block, gap D], so the inverse-Wishart tail of (A_S^*A_S)^+ is lighter -- E[tr(A_S^*A_S)^+]
is already finite for D >= 2 -- and M_m(D) is at most polylog(m) for D=2 and O(1+1/D) up to
log-of-scale corrections for D >= 3. The single power of m at D=1 is the extreme.)

### 3.2 The precise residual (R-poly), and what a rigorous proof needs

What the Sec.3.1 heuristic strongly indicates, but does NOT yet rigorously prove, is:
```
  (R-poly)  there is a fixed A < infty with  M_m(D, t_m) <= C m^A  for all 1 <= D < epsilon m and m large.
```
A rigorous proof requires, uniformly in D:
  (i) the regularized completion law smin(A_{T}) ≈ (private slab)/sqrt(1+R) with explicit, uniform
      error control, including the cap on the near-singular-A_S locus -- a finite-dim
      shared-null-space computation, D-uniform;
  (ii) the hard-edge lower-tail of the shared (m-D) x m Gaussian block,
      P{smin(A_S) <= g} <= (C sqrt(m) g)^{d_F D}, with the inverse-moment E[(A_S^*A_S)^+
      participation]^{d_F/2} controlled -- standard Laguerre hard-edge / inverse-Wishart input,
      but D-uniform and at the relevant (exp-small) scales;
  (iii) bookkeeping of the log(1/t_m) = Theta(m) factors to confirm the growth is POLYNOMIAL (a
      bounded power A of m, from a bounded number of cut-off heavy-tail integrals) and not
      exponential.
None of (i)-(iii) needs a new idea -- they are Gaussian hard-edge computations -- but they are not
written, and (i) genuinely replaces the two-projection lemma (which is void at |rho|->1). This is
the centered-scale analogue of `prop:small-D-negligible`: at the sub-critical bulk scale t=e^{-sm},
s<h/d_F, the exp room R(epsilon) - d_F s > 0 lets the TRIVIAL bound M_m <= 1/p_1 = e^{d_F s m} win
against P{D<epsilon m} = e^{-R(epsilon) m}; at the CENTERED scale d_F s = h(gamma) the room is gone,
1/p_1 = e^{h m} exactly cancels the rarity e^{-h m}, and one MUST replace the trivial 1/p_1 by the
true poly(m). That replacement is (R-poly).

================================================================================
## 4. Status and the precise theorem

CLASSIFICATION: **partial -- reduced to a single uniform polynomial bound, with strong evidence it
holds.** Concretely, for the Gaussian ensemble the following are now in place (this note):

  PROVED (rigorous):
   - The exact reduction E[(N_t)_2] = lambda^2(1+o(1)) E_Vand[M_m(D)], M_m(D)=E[q^2]/(Eq)^2 >= 1,
     from conditional independence given the shared rows + Vandermonde (Sec.1). No two-projection
     lemma, no delocalization input, is used for the reduction; it is model-free and exact.
   - BULK (D >= epsilon m) -> 1 (the lambda^2), using the EXACT Gaussian Haar overlap
     |rho|^2 ~ Beta(d_F/2, d_F(D-1)/2), the closed form M(D) = 1 + d_F/(2D) + O(D^{-2}), the
     two-slab/two-disk estimate at |rho| <= 1-kappa_0, and a super-exponential tail to kill
     |rho|->1 (Sec.2).
   - The near-diagonal is genuinely regularized and POLYNOMIAL, not divergent: M_m(1) = Theta(m)
     explicitly (Sec.3.1), so its contribution Theta(m^3)/binom(N,m) -> 0.

  RESIDUAL (the one gap): the uniform polynomial bound (R-poly), M_m(D,t_m) <= C m^A for all
   1 <= D < epsilon m. Heuristically true (Sec.3.1 gives the worst case D=1 as Theta(m)); a rigorous
   proof is the D-uniform Gaussian hard-edge computation (i)-(iii) of Sec.3.2, replacing the
   two-projection lemma in the |rho|->1 corner. This is the centered-scale near-diagonal estimate
   (R2) of `gumbel_kpoint.md`, here sharpened to "poly(m) suffices" and shown achievable in size.

  IF (R-poly) is granted, the theorem is:

   THEOREM (Gaussian extremal hard edge, conditional on R-poly). Let A_m in F^{N_m x m} be iid
   standard (proper for C) Gaussian with N_m/m -> gamma > 1, and let b_m solve
   binom(N_m,m) F_m(e^{-b_m}) = 1, F_m(t) = P{smin(G_m) <= t} for one m x m Gaussian. Then the point
   process sum_{|T|=m} delta_{ log smin(A_{m,T}) + b_m } converges to the Poisson process with
   intensity d_F e^{d_F x} dx, and
        P{ log M_m^F + b_m <= x }  ->  1 - exp( -e^{d_F x} ),
   the Gumbel law with rate d_F. (Via E[N_t] -> e^{d_F x} = lambda [proved, manuscript], the
   second-moment E[(N_t)_2] -> lambda^2 [Sec.1-3 here, modulo R-poly], and the r-point collapse
   [`gumbel_kpoint.md`, Gershgorin det G_r + Chen-Stein], all r-point factorial moments converge to
   prod lambda_i, hence Poisson, hence the Gumbel law.)

NUMERICS (this note). (a) The closed form M(D) = Gamma(d(D-2)/2)Gamma(dD/2)/Gamma(d(D-1)/2)^2
matches a direct Monte-Carlo of E[(1-|rho|^2)^{-d/2}] with |rho|^2~Beta(d/2,d(D-1)/2) to 3-4 digits
for d=1,2 and D=3..200, and -> 1+d/(2D) (e.g. d=1: M(3)=1.571, M(40)=1.013; d=2: M(3)=2.000,
M(40)=1.026). (b) The headline ratio E[N_t(N_t-1)]/(E N_t)^2 = 1.18,1.13,1.04 (m=6,7,8) -> 1 and
P{N_t=0} -> e^{-lambda} are the existing full-enumeration simulations in `open_problems.tex`,
i.e. E[(N_t)_2]/lambda^2 -> 1 is already empirically confirmed. (c) A direct MC of M_m(D)=P{both}/p_1^2 at a MODERATE
threshold (p_1~0.02, real) gives all M_m(D)=O(1) with the near-diagonal most associated and the
bulk ~1: e.g. m=24 yields M(D=1)=2.08, M(2)=1.92, M(3..12)=1.0-1.4 (noisy, consistent with the
bounded Beta values 1.57,1.18,1.08,1.05), and M_m(1) is FLAT in m (2.83,2.58,2.33,2.33 for
m=5,10,20,40). CAVEAT: this neither sees nor contradicts the M_m(1)=Theta(m) claim, which is a
CENTERED-scale effect -- the Theta(m) is log(1/t_m), absent at moderate t -- and t_m=e^{-Theta(m)}
is not MC-accessible. This is exactly why (R-poly) is a centered-scale statement that cannot be read
off the bulk simulations.

HONEST BOTTOM LINE. The Gaussian case does NOT yet close as an unconditional theorem. It is reduced,
exactly and cleanly, to ONE uniform-in-D polynomial bound on the centered-scale conditional overlap
moment M_m(D) over the small-codimension (near-diagonal) range -- the residual being the
near-diagonal regularization, where the two-projection LCLT is unavailable and the shared-block
hard-edge/inverse-Wishart tail must be controlled by hand. The bulk lambda^2 and the exact overlap
moment M(D) ARE in place. The explicit M_m(1) = Theta(m) computation shows the residual is a genuine
poly(m) (not O(1), not exponential), so the bound is the right target and is very likely provable by
standard Gaussian hard-edge estimates -- but it is not proved here.
