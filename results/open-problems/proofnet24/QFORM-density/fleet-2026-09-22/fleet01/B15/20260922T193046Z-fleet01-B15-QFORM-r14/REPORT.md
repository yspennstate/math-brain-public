# QFORM B15 r14 — support-aware physical-pivot regularity and the fragmented conditional-height obstruction

Status: **supporting theorem proved; full universal QFORM remains OPEN**.

Source control: `yspennstate/math-research-brain@2a07f73272566942e2ffa8620e16ccf734b29ca2`; owner control revision observed `2026-09-22.14`. Assignment: fleet01/B15, absolute continuity and regularity. Execution status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Corrections used

The full target is: independent real coordinates with densities `f_i<=1`, and a real symmetric matrix `A` with at least three eigenvalues of modulus at least one; prove one dimension- and matrix-independent density bound. Continuity is separate.

This run does **not** use any law-uniform pointwise quadratic Fourier decay, independence after spectral rotation, arbitrary-joint rank-three coarea estimate, or positive moment of scalar-conditioned spectral density height. In particular, fleet02/B15 r6 (`math-open-problems@d00907b4362875219cc3525ceb04f90186b8c065`) gives a fixed target and cap-one product sources for which every positive moment of the scalar-conditioned three-dimensional spectral density height can diverge, while the target output itself stays bounded.

## 2. Physical monotone-pivot lemma

Let `X=(X_1,...,X_n)` have independent densities `0<=f_i<=1`. Let

`Q(X)=X^T A X+2 l^T X+c`,

with real symmetric `A`. Fix a physical coordinate `i` and condition on `X_{-i}=y`. Then

`q_y(u)=a u^2+2 b(y)u+d(y)`,

where `a=A_ii` and

`b(y)=l_i+sum_{j!=i} A_ij y_j`.

Write `E_i={u:f_i(u)>0}` up to null sets and

`m_i(y)=ess inf_{u in E_i} |q_y'(u)| = ess inf_{u in E_i} |2a u+2b(y)|`.

Whenever `m_i(y)>0`, the one-dimensional area formula gives a conditional density

`h_y(t)=sum_{u in E_i:q_y(u)=t} f_i(u)/|q_y'(u)|`

for a.e. `t`. A quadratic has at most two real preimages, so

`||h_y||_infty <= 2/m_i(y)`.

Consequently, whenever the right side is integrable,

`boxed( ||p_Q||_infty <= E[ 2/m_i(X_{-i}) ] ).`             (2.1)

If for a.e. `y` the support `E_i` lies entirely on one side of the critical point `-b(y)/a` (with the evident affine interpretation when `a=0`), then `q_y` is injective on `E_i` and the factor two disappears:

`boxed( ||p_Q||_infty <= E[ 1/m_i(X_{-i}) ] ).`             (2.2)

A uniform support-aware derivative floor `m_i(y)>=delta` therefore gives `||p_Q||_infty<=2/delta`, or `1/delta` in the injective branch. This uses only original-coordinate independence and the cap `f_i<=1`.

This lemma is deliberately about the central `L^infty` assertion only. It does not claim continuity for rough `f_i`.

## 3. Exact application to the assigned partner's r6 obstruction

Use the normalized Hadamard matrix

`H=(1/2)[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]`

and

`A=H diag(1,2,-3,1/2) H^T`
` =(1/8)[[1,11,-9,5],[11,1,5,-9],[-9,5,1,11],[5,-9,11,1]].`

The spectrum is `{1,2,-3,1/2}`, so this is an exact owner-target matrix. For each integer `M>=1`, fleet02/B15 r6 takes

`E_M=union_{j=1}^M [10j,10j+1/M]`,

and independent densities

`f_1=1_{E_M}`, `f_2=f_3=f_4=1_[0,1]`.

Their proof shows that the scalar-conditioned spectral projection height has divergent positive moments as `M->infinity`. We now apply the physical-pivot lemma to the *same* sources.

Choose physical coordinate `i=2`. Direct differentiation gives

`partial_2 Q(x) = (x_2+11x_1+5x_3-9x_4)/4`.

On the exact product support,

`x_1>=10`, `0<=x_2,x_3,x_4<=1`,

and therefore

`partial_2 Q(x) >= (110-9)/4 = 101/4`.

Thus, after conditioning on `(X_1,X_3,X_4)`, the map `x_2 -> Q` is strictly increasing on `[0,1]`, and its conditional output density is at most

`4/101`.

Averaging the conditional densities proves the explicit, fragment-count-independent bound

`boxed( ||p_Q||_infty <= 4/101 < 0.04 )`                 (3.1)

for every `M` in the partner's obstruction family.

This is substantially stronger than merely knowing a fixed-matrix constant exists. It proves directly that the quantity that diverges in the scalar-conditioned spectral representation is not measuring output concentration on this family: the original-coordinate product source contains a uniformly transverse physical direction which the spectral conditioning destroys.

## 4. Continuity is separate and supplied by the completed partner theorem

The completed fleet02/B15 target-scope regularity theorem (handoff r4; canonical `math-open-problems@28ddaf28bf6779837fb1212a025d8a8b9d329f8a`) proves at worker-candidate scope that every fixed `rank(A)>=3` cap-one product target has a bounded `C_0(R)` density, using an invertible physical principal `3x3` or `4x4` block and dominated outside conditioning. Applying that theorem to the same Hadamard matrix shows that the densities in (3.1) have continuous representatives vanishing at infinity.

Thus the two assertions are cleanly separated here:

- the new physical-pivot computation gives the quantitative height `4/101`;
- the partner regularity theorem supplies `C_0` continuity;
- neither statement is promoted to the unresolved universal target.

## 5. Consequence for the live proof architecture

Fleet02/B15 r6 shows that taking `sup_b` or any positive moment of scalar-conditioned spectral projection heights can diverge on a fixed target. Equation (3.1) shows, on the exact same sources, that a physical derivative can simultaneously stay uniformly bounded away from zero and force an output height below `0.04`.

Hence a viable full proof cannot normalize away the original-coordinate derivative/translation information before paying for concentration. The correct translation-aware graph trace from fleet01/B15 r13,

`p_Q(t)=int_{R^3} G(y,t-y^T Lambda y) dy`,

must be combined with physical-pivot, pair-log, grouped-coordinate, or ridge estimates **before** conditional spectral profile maxima are taken.

A useful source-valid sufficient branch is now explicit: if some physical coordinate has an integrable inverse conditional derivative floor as in (2.1), then QFORM follows for that instance with exactly that bound. The remaining universal implication is to cover the complementary near-critical set, uniformly over every physical coordinate, by the aggregate pair/ridge/fractional-trace machinery without paying a reciprocal tiny minor.

## 6. Classification

`ESSENTIAL_STEP_APPLIED / PHYSICAL-PIVOT-COMPENSATION-EXHIBITED`.

Full QFORM: **OPEN / NOT PROVED**.
