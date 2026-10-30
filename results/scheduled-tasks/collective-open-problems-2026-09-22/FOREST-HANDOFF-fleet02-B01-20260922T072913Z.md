# FOREST handoff — fleet02/B01 — B01-20260922T072913Z-forest-r17

Outcome: `ESSENTIAL_STEP_APPLIED`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Parent FOREST target: OPEN.

Fresh owner control used in the substantive derivation: revision `2026-09-22.2`; the collective research order remains active and fleet02/B01 remains assigned to the alternative separator/deletion-contraction route. Latest complete lead input read: fleet01/B01 run `20260922T050946Z-b01-forest-auto11`, canonical report commit `79044b575c4b689248892f37b9930e983dddabca`, handoff blob `4cee205cb7d254caf785692838111988a0b8a155`. Named partner input actually applied: fleet03/B02 run `20260922T065713Z-b02-r11-forest`, report commit `6440b33cef6c36ea3ed619025bc7989abd558515`, handoff commit `2477193cc8a01f1dff962311ca13f9812d114680`.

## 1. Actual separator law + inverse covariance

For an offending same-side proper two-separator, let `O` be the outside side, `m=|E(O)|`, terminals `u,v`, `Y=1{u<->v in F_O}`, `q=EY`, and let the marked-side Rayleigh polynomial have negative interval `J=(alpha,beta)`. In probability coordinate write `ell=alpha/(1+alpha)`, `u=beta/(1+beta)`. Existing exact deletion/contraction straddling gives, for every physical outside edge `h`,

`c_h:=Cov(T_h,Y) >= k0=((q-ell)(u-q))/(u-ell)`

and `p_h=P(T_h=1) <= U:=min(1/2,q/u)`.

Let `Sigma=Cov((T_h)_h)`. Minimality gives nonpositive off-diagonal entries; empty and singleton forests make `Sigma` positive definite. Applying the fleet03/B02 inverse-M-matrix mechanism gives `Sigma^{-1}>=0` entrywise. With

`eta_O=1^T Sigma^{-1}1`,

Schur complement for `(Y,T)` yields

`boxed: k0^2 eta_O <= q(1-q)`.

Since `(Sigma^{-1})_hh>=1/Var(T_h)` and `Var(T_h)<=U(1-U)`, this sharpens the previous scalar edge-count bound to

`boxed: m k0^2 <= q(1-q) U(1-U)`.

Also `eta_O Var(|F_O|)>=m^2`, hence

`boxed: m^2 k0^2 <= q(1-q) Var(|F_O|)`.

These retain the actual boundary-connectivity distribution and the whole physical-edge covariance geometry; no arbitrary external field or complete-log-concavity assumption is used.

## 2. Mixed-length theta compression

For internally disjoint terminal paths of lengths `a_1,...,a_r`, exact unit forest enumeration gives

`D_Q=prod_i(2^{a_i}-1)`,

`C_Q=D_Q sum_i 1/(2^{a_i}-1)`,

so the exact response is

`s_Q=sum_i 1/(2^{a_i}-1)`

at unit-edge cost `sum_i a_i`. Therefore edge-minimality excludes the full mixed response semigroup from the negative interval whenever the gadget is cheaper than the actual outside:

`J intersect {sum_i 1/(2^{a_i}-1): sum_i a_i < m}=empty`.

This strictly strengthens the equal-length theta grid used previously.

## 3. Finite-cost epsilon net

For any `0<r<=1` and `0<eps<r`, repeatedly choose

`a=ceil(log_2(1+1/r_current))`

and subtract `1/(2^a-1)`. Each nonterminal residual shrinks by a factor `<2/3`, while every chosen `a` is at most `ceil(log_2(1+1/eps))`. Hence some mixed-theta response `s<=r` satisfies `r-s<=eps` with cost at most

`C(r,eps)=ceil(log_{3/2}(r/eps))*ceil(log_2(1+1/eps))`.

For the actual outside response `lambda=n+r`, `n=floor(lambda)`, let `L=lambda-alpha`. If `0<r<1`, no-hit implies `n<=alpha`, and taking `eps=L/2` gives the necessary source-valid margin bound

`boxed: m <= n + ceil(log_{3/2}(2r/L))*ceil(log_2(1+2/L))`.

There is an analogous right-margin bound whenever `n+1<m`, obtained by approximating `r+(beta-lambda)/2` within one quarter of the right margin. If `r=0`, a cheaper exact integer response exists unless `lambda=m`, so the only integer no-hit case is the extremal boundary.

## 4. Remaining first essential implication

`MIXED-THETA-HIT / REALIZABILITY-v2`:

> Prove that a genuine unit outside graph satisfying the edgewise straddling constraints and the inverse-covariance budget cannot simultaneously satisfy the finite-cost left/right no-hit bounds above; or construct an actual marked-side/outside graph pair showing that this strengthened separator mechanism fails.

This is narrower than the preceding THETA-HIT debt because both the complete mixed-length source-generated response semigroup and the exact outside covariance matrix are now paid inputs. No full-proof claim is made.

Exact regression artifact in the canonical run folder verifies six mixed-bundle count identities and the greedy residual/cost assertions; its output ends `STATUS=MIXED_THETA_EXACT_PASS`. Finite enumeration is regression only, not target closure.
