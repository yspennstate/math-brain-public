# Adversarial review: `ROTATED_NONFREEZING.md`

**Verdict:** The finite-width contradiction is valid. I found no conditioning, cutoff, or uniformity gap in the later-dynamics argument. I also checked the supporting rotated joint-initialization argument in `agents/c01.md` after it appeared in this run directory; its axis reduction, separation of endpoint types, and support claims are consistent and supply the needed lemma. The theorem note should state its parameter order more explicitly. I did not audit an external model citation.

## Deterministic and probabilistic quantifiers

The clean choice order is:

1. Choose one fixed open initialization neighborhood `N` of `(r0,C0,A0)` small enough that on `N`, `r_j(0)>3/4`, `A_1>.4`, `||P||op<4`, and `int_0^2[e^(-Pt)r(0)]_1dt<-.18`. These are strict continuous inequalities at the displayed center. The joint initialization lemma and open support give `liminf P(N_m)=p_*>0` (Portmanteau).
2. By unconditional tightness of `S_m`, choose a fixed `K` with `limsup P(S_m>K)<p_*/2`, and define `E_m=N_m∩{S_m<=K}`. Then `liminf P(E_m)>=p_*/2>0`, without any independence assertion. Fix `R` bounding `||r(0)||` on `N`.
3. Choose a fixed `delta>0` sufficiently small both for `2KR delta<1/4` and for the initial-interval Duhamel error. Then choose a fixed `h>0`, with `h<.1`, so that `2R[(2K+4)delta+2h]<.08`. All of `N,K,R,delta,h` are independent of `m`; ultimately `eta=h/2` and any `0<p<liminf P(E_m)` work.

The note's prose chooses `K` before finally shrinking the neighborhood. This is readily repaired by the order above; it is not a substantive obstruction.

## Kernel and gate estimates

The orthogonal change of hidden coordinates preserves row energy, and the first-layer kernel stays exactly diagonal. The usual star-matrix bound yields, deterministically on `E_m`, `||H_m(t)||<=2K`, uniform `o(1)` drift of `C_m(t)` and of the normalized total `W_i^2`, and `max_i sup_{t<=2}|W_i(t)-W_i(0)|/a_m=O(beta_m)=o(1)`. No independence of `V_i1,V_i2` is used there.

For fixed `epsilon>0`, a large negative-`W` gate that remains active at `delta` needs `V_ij(0)>=c epsilon delta L_m`: throughout `[0,delta]` its weight remains negative with magnitude at least `epsilon a_m/2`, and the residual is at least `1/2`. The unconditional union bound is `O_{epsilon,delta}(1/log m)` because `W_i` is independent of the stable `V_ij`. Positive-`W` large gates active initially cannot die on this interval. The remaining initially small-`W` square mass obeys `limsup E Z_m,epsilon<=C epsilon^(2-alpha)`. Consequently, for every fixed `h>0`,

`P(E_m∩{||H_m(delta)-P_m||>h}) -> 0`.

The random event `E_m` causes no conditioning problem: the rare-gate probabilities and `E Z_m,epsilon` are bounded *unconditionally*, and intersecting with `E_m` can only decrease their probabilities. The correct limiting order is fixed `epsilon`, then `m->infinity`, then `epsilon->0`.

## Constant-kernel contradiction

At the center, `Jbar_1(2)=-1/3+e^(-2)-(2/3)e^(-6)≈-.19965`. The selected neighborhood makes it `<-.18` throughout `E_m`. On `B_m(h)={sup_[delta,2]||H_m-P_m||<=h}`, Duhamel with the PSD contraction `e^(-P_mt)` gives

`sup_[0,2]||r_m(t)-e^(-P_mt)r_m(0)|| <= R[(2K+4)delta+2h]`.

The `2K+4` term pays for the uncontrolled interval `[0,delta]`; it is bounded uniformly on `E_m`. Integrating gives `J_1,m(2)<-.10` on `E_m∩B_m(h)` with the fixed choices above.

For any initially active positive-`W` gate with `W_i(0)>=epsilon a_m` still active at time 2, the exact active-gate identity divided by `L_m` yields

`V_i1(2)/L_m=V_i1(0)/L_m+(W_i(0)/a_m)J_1,m(2)+O_{K,R}(beta_m)`.

Since the left side is positive and `J_1,m(2)<-.10`, survival requires `V_i1(0)>=.05 epsilon L_m` for all large `m`. Its unconditional union probability is `O_epsilon(1/log m)`. Negative-`W` extremes active at time 2 have already been ruled out by the `delta` bound; initially inactive gates remain inactive by absorption. On the complement of those rare events,

`H1_1,m(2) <= Z_m,epsilon + o(1)`

uniformly on `E_m∩B_m(h)`. Thus for every `q>0`,

`limsup_m P(E_m∩B_m(h)∩{H1_1,m(2)>q}) <= C epsilon^(2-alpha)/q`.

Sending `epsilon->0` proves equation (3). This handles arbitrarily large rare `W_i` without an invalid expectation bound on their squares. Meanwhile `B_m(h)` and frozen `C_m` force `H1_1,m(2)>=A_1,m-h-o(1)>.4-h-o(1)` on `E_m`; choosing `h<.1` contradicts (3). Therefore `P(E_m∩B_m(h))->0`. Combining this with the `delta` comparison gives the asserted positive lower bound on `P(sup_[delta,2]||H_m(t)-H_m(delta)||>h/2)`.

## Dependency and scope

The separate `agents/c01.md` now exists and I checked its key steps. The positive-part reduction errors are bounded by `min(|U_1|,|U_2|)`, whose `alpha` moment is finite, so they vanish at the product normalization. The three retained output rays yield the stated independent symmetric-stable components; the hidden-coordinate square extremes yield `C=(1/2)[[S0+S1,S0],[S0,S0+S2]]`. One-row overlaps between product jumps, square endpoints, and the `W` endpoint process vanish at order `mP`, which supports the asserted primitive independence. Positive-`W` gate patterns have probability `1/4` each, and the output law has axis and diagonal stable components, hence full `R^2` support. I found no initialization error affecting the positive-probability event.

The constants check independently. If `c=c_alpha` and `b=alpha/2`, then `P(U_+>u)~c u^(-alpha)`, so `P(U_+^2>x)~c x^(-b)` and its normalized sum has Laplace exponent `c Gamma(1-b)s^b`. Division by 2 in each rotated ray gives the claimed `C` matrix and `C_12=S0/2`. Also `P(W U_+>x)~alpha c^2 x^(-alpha)log x`; at `b_m=(m log m)^(1/alpha)`, its one-sided limit tail is `c^2 x^(-alpha)`, exactly the tail of a symmetric stable law with characteristic exponent `c|t|^alpha`. Thus the output characteristic exponent is `c 2^(-b)(|t1+t2|^alpha+|t1|^alpha+|t2|^alpha)`. On the positive-`W` endpoint half-axis, squaring `z` gives Lévy tail `c x^(-b)`; thinning by one of the four activation patterns gives each `T` component exponent `(c/4)Gamma(1-b)s^b`, as `c01` states.

For independence, fixed-cutoff product jumps from the `U_1` and `U_2` rays overlap in one row with probability `O(1/(m log m))`; the positive and negative `U_2` product rays are disjoint. A product jump can overlap a `W/a_m` endpoint or a `U^2/a_m^2` endpoint only in the auxiliary large-endpoint tail or when the other independent factor exceeds a constant multiple of `L_m`; taking `m->infinity` and then the auxiliary endpoint cutoff to infinity makes `m` times each overlap probability vanish. Distinct square endpoints overlap at `O(m^(-2))` or are sign-disjoint. The small centered product jumps have `O(epsilon^(2-alpha))` variance and small positive square jumps have `O(epsilon^(1-b))` first moment, so cutoff removal preserves factorization. These are the necessary categories for joint independence of `F,C,N`; I do not see an omitted common-jump class.

Finally, each `S` and each thinned `T` is a positive stable law with full support on `(0,infinity)`. Choosing `S0≈2,S1≈S2≈1` yields `C≈C0`; choosing `T11,T10,T01≈1/4` yields `A≈(.5,.5)`. Conditional on `Z0`, `F_1,F_2` have independent everywhere-positive stable densities, so `F≈(-1,-3)` has positive probability for the theorem's `y=0`. Since these primitives are independent, their joint target neighborhood has positive probability. This closes the initialization dependency needed by the theorem.

The proof establishes positive-time order-one kernel variation with positive probability. It does not need, and does not assume, convergence to the proposed two-phase hybrid limiting process or a switching-time law. The same-sign initial residual is essential for this example: strictly mixed-sign residuals obey an exact Metzler sign-invariance argument and cannot supply this cumulative-integral crossing.
