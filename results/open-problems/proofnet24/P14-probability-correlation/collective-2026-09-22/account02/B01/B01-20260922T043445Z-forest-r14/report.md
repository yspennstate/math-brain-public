# FOREST / account02 B01 — exact 3-terminal K4 response synthesis criterion

**Run:** `B01-20260922T043445Z-forest-r14`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Role:** alternative separator/deletion-contraction route, retaining the actual boundary-connectivity distribution and induced weights.

## 1. Fresh source state and peer result applied

Fresh owner control was reread from `yspennstate/math-research-brain` main. The active owner revision is `2026-09-22.2`; new installation/benchmark work is stopped and account02/B01 remains on FOREST.

The latest complete lead version read was account01/B01
`proofnet24/P14-probability-correlation/collective-2026-09-22/account01/B01/20260922T030948Z-b01-forest-auto11/report.md`,
blob `58b8b1d8ac522a4eda7479400820e590c12f22aa`,
candidate `FOREST-KN-COCKS-RECONCILED-v3`. It records a complete-graph Hermite proof plus the fixed-graph Cocks upgrade and minor closure, and classifies the resulting all-graphs chain as an internal `FULL_PROOF_CANDIDATE`, not a public theorem claim.

The named OTHER-account result consumed and applied here is account03/B02
`proofnet24/P14-probability-correlation/collective-2026-09-22/account03/B02/20260922T032505Z-account03-B02-r11/source_closure_review.md`,
blob `75028150088c9c6b931032a22760e762c58daffb`.
It independently source-checks the final Semple--Welsh note stating the fixed-graph Cocks implication and Proposition 3.5 minor closure. I use that result only to legitimize positive induced separator weights in the alternative route; I do not treat the lead's full candidate as a substitute for the separator derivation below.

## 2. Conditional end-to-end alternative route

The separator/deletion-contraction route can be organized as follows.

1. Exact 0/1-separations factor.
2. Exact two-terminal gluing replaces the opposite side by its true response `C/D`; with the fixed-graph weighted upgrade, all induced positive virtual-edge weights are legitimate.
3. At a genuine three-terminal side `B` with boundary vertices `1,2,3`, retain all five actual boundary partition weights `d,a,b,c,t` for `1|2|3`, `12|3`, `13|2`, `23|1`, `123`.
4. Replace `B`, if possible, by a four-vertex weighted `K4` gadget on the three terminals plus one Steiner vertex. Equality of these five boundary weights up to a common factor is enough to preserve the full forest polynomial of every opposite side and hence every same-side marked-edge Rayleigh sign.
5. The new theorem below gives an exact necessary-and-sufficient scalar criterion for this replacement. Thus the previous unresolved mixed residual is not arbitrary: it is exactly a two-inequality boundary-realizability question.
6. A complete separator proof would still need to prove those two inequalities for every source-valid three-terminal forest side (or derive a marked analogue for cross-side marked pairs) and then choose a strict induction measure for gadget replacement. I do not assume either unpaid step.

## 3. Exact three-terminal gluing data

For a forest of `B`, record only the connectivity partition induced on terminals `1,2,3`. Let

- `d` = total weight of forests inducing `1|2|3`;
- `a` = total weight inducing `12|3`;
- `b` = total weight inducing `13|2`;
- `c` = total weight inducing `23|1`;
- `t` = total weight inducing `123`.

For any opposite side `A`, these five numbers are the complete unmarked boundary response: two sides with proportional vectors `(d,a,b,c,t)` give proportional global forest polynomials for every `A`.

Define the residual
`tau = d*t - (a*b + a*c + b*c)`.

The previous triangle-only compression corresponds to `tau=0`. The unit three-spoke star has `(d,a,b,c,t)=(4,1,1,1,1)` and `tau=1`, so `tau` is exactly the obstruction missed by triangle-only compression.

## 4. New K4 response-synthesis theorem

### Theorem

Assume `d>0` and nonnegative `a,b,c,t`. In the nondegenerate case `tau>0` (which forces `a,b,c,t>0` under the second inequality below), the following are equivalent.

**(i)** There exist nonnegative terminal-triangle weights `x,y,z`, nonnegative Steiner-star weights `u,v,w`, and a scalar `kappa>0` such that the weighted `K4` gadget on vertices `{1,2,3,o}` has boundary signature exactly `(d,a,b,c,t)/kappa`.

**(ii)** `tau >= 0` and `tau*t <= a*b*c`.

When `tau=0`, the same assertion holds with `u=v=w=0` and a weighted terminal triangle; zero weights may equivalently be obtained as positive-weight limits. Degenerate zero sectors follow by the same limiting interpretation.

### Direct gadget algebra

For the gadget with triangle edges `x=12`, `y=13`, `z=23` and star edges `u=o1`, `v=o2`, `w=o3`, direct forest enumeration gives, with `D=1+u+v+w`,

`d_g = D,`

`a_g = D*x + u*v,`

`b_g = D*y + u*w,`

`c_g = D*z + v*w,`

and, without needing the long explicit formula for `t_g`,

`D*t_g - (a_g*b_g + a_g*c_g + b_g*c_g) = u*v*w.`

Thus `tau_g=u*v*w>=0`.

Normalize `A=a/d`, `B=b/d`, `C=c/d`, `T=t/d`, and `theta=T-(A*B+A*C+B*C)=tau/d^2`.

For any gadget set `delta=1/D`, `p=u/D`, `q=v/D`, `r=w/D`; then `delta+p+q+r=1`. Its pure-star contributions are

`alpha=p*q/delta`, `beta=p*r/delta`, `gamma=q*r/delta`, and `theta=p*q*r/delta`.

The normalized pair sectors are `A=x+alpha`, `B=y+beta`, `C=z+gamma`, while `T=A*B+A*C+B*C+theta`.

For the pure star (`x=y=z=0`) one has the exact identity

`alpha*beta*gamma = theta*(alpha*beta+alpha*gamma+beta*gamma+theta)`,

because the bracket is `p*q*r/delta^2 * (p+q+r+delta)`.

Adding nonnegative `x,y,z` can only increase
`Phi(A,B,C)=A*B*C-theta*(A*B+A*C+B*C+theta)`.
Indeed at the pure-star point
`partial_A Phi = beta*gamma-theta*(beta+gamma) = p*q*r^2*(delta+r)/delta^2 >= 0`,
and cyclically; these partial derivatives increase as the other coordinates increase because `alpha,beta,gamma >= theta` (each ratio is the reciprocal of one of `p,q,r<1`). Therefore every such gadget satisfies

`A*B*C >= theta*T`,

equivalently
`a*b*c >= tau*t`.

This proves necessity.

### Constructive sufficiency

Assume now `theta>0` and `theta*T <= A*B*C`.
Define

`L(lambda) = lambda*theta*(1/A+1/B+1/C) + lambda^3*theta^2/(A*B*C)`.

At `lambda=1`,

`L(1)=theta*T/(A*B*C) <= 1`,

while `L(lambda)` is strictly increasing and tends to infinity. Hence there is a unique `lambda>=1` with `L(lambda)=1`.

Set

`p=lambda*theta/C`,
`q=lambda*theta/B`,
`r=lambda*theta/A`,
`delta=lambda^3*theta^2/(A*B*C)`.

Then `p+q+r+delta=1` and `p*q*r/delta=theta`.

Now set

`u=p/delta`, `v=q/delta`, `w=r/delta`,

`x=A*(1-1/lambda)`,
`y=B*(1-1/lambda)`,
`z=C*(1-1/lambda)`.

All weights are nonnegative. Since `D=1/delta`,

`u*v/D = p*q/delta = A/lambda`,

and cyclically, so the normalized pair sectors are exactly `A,B,C`. Also

`u*v*w/D^2 = p*q*r/delta = theta`,

hence the normalized all-connected sector is exactly `T`.
Finally choose the overall scale
`kappa=d/D=d*delta`.
Then all five boundary weights match `(d,a,b,c,t)` exactly.

This proves sufficiency.

## 5. Consequence for the previous three-terminal residual

The previous exact identity wrote the response of `B` as a weighted terminal triangle plus the residual `(tau/d) Z_sep(A)`. The synthesis theorem shows that, whenever

`tau >= 0` and `tau*t <= a*b*c`,

the entire five-sector response is instead the ordinary forest response of one nonnegative weighted `K4` gadget. No unsupported assumption that the isolated `Z_sep` sector is Rayleigh is needed; the residual is absorbed by an explicit Steiner star with exactly the required strength.

So the first missing implication for this separator mechanism is now concrete:

> **Three-terminal response cone question.** For every finite graph side `B` with three distinguished boundary vertices under the all-forests measure, must
> `d*t >= a*b+a*c+b*c`
> and
> `(d*t-a*b-a*c-b*c)*t <= a*b*c`
> hold?

A proof would make every unmarked three-terminal response `K4`-synthesizable. A source-valid counterexample to either inequality would decisively refute this compression route while preserving the exact five-sector data.

This is strictly sharper than the prior mixed-term debt. It neither normalizes away the true boundary law nor replaces it by an arbitrary virtual-edge weight.

## 6. Exact finite regression

A standard-library exhaustive checker was run as regression evidence, not as a proof of the universal response-cone inequalities.

Artifact: `k4_response_synthesis_checker.py`  
SHA-256 `fc16cd10ed5414f297acc0731064cebe832518a855c77f1312b74a7c68e5dec9`.

Captured output: `k4_response_synthesis_checker.out`  
SHA-256 `6c62bd0e82a0cda25867b72c1177b63a93ec0d4153a4e389b121df1a415b6bbc`.

Exact output:

```text
PASS all_simple_graphs n=3 graphs=8
PASS all_simple_graphs n=4 graphs=64
PASS all_simple_graphs n=5 graphs=1024
PASS K4_response_formula grid=3^6
PASS response_cone_small_graphs total_graphs=1096 min_tau=0 min_gap=0
```

Thus all 1,096 labelled simple graphs on three, four, or five vertices, with terminals fixed as vertices `0,1,2`, satisfy both candidate response-cone inequalities. The checker also verifies the K4 formulas on all `3^6` integer weight choices in `{0,1,2}^6`. This finite census is `AUXILIARY_ONLY`; it is not universal closure.

## 7. Failures and honest boundary

I did not prove the two response-cone inequalities for arbitrary `B`, and I did not prove the marked-boundary analogue needed to make every cross-separator marked pair collapse to one K4 gadget. Those are genuine remaining mathematical debts.

A source search did not locate a ready-made theorem under this exact signature, and a search miss is not evidence of novelty or truth.

The lead's reconciled complete-graph/Cocks route is separately recorded as an internal full candidate with two existing-worker reviews. This report neither demotes nor auto-promotes that route; it develops the requested alternative separator/deletion-contraction mechanism.

No brain installation, benchmark work, benchmark gold, scheduler mutation, email, Drive, public posting, paid API/model/Codex call, remote workflow, permission change, or production activation occurred.

## 8. Status

**Classification: `ESSENTIAL_STEP_APPLIED`.**

The previous uncontrolled three-terminal residual has been converted into an exact, constructive four-vertex gadget synthesis theorem with two scalar source-side inequalities as the first essential missing implication. The immediate next mathematical action is to prove or refute those inequalities on genuine three-terminal forest signatures, preferably by deletion-contraction or a source-valid two-forest switching map; only after that should the marked cross-side analogue be attempted.
