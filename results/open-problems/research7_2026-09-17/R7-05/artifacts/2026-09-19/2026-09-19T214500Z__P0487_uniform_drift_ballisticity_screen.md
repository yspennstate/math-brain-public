# P0487 admission-side mathematics — a uniform-drift theorem, exact homogeneous exponent, and the remaining positive-velocity gap

Date: 2026-09-19 UTC  
Worker: R7-05  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Category sought: CLOSABLE OUTSIDE  
Candidate: `P0487`  
Shard check: `sum(ord(c) for c in "P0487") mod 7 = 4`.

## 1. Source and present scope

Repository source recovery identifies P0487 with Alexander Drewitz and Alejandro F. Ramírez, *Selected Topics in Random Walks in Random Environment* (2013 preprint / 2014 proceedings), Open Question 3.20 (repository locator PDF p.52, adjacent Theorem 3.17 on p.51):

> Under i.i.d. uniform ellipticity in dimension `d >= 2`, does positive velocity in a direction `ell` imply the polynomial ballisticity condition `(P)_M` for `M > 15d+5`?

The later theorem of Guerra--Ramírez, *A Proof of Sznitman's Conjecture about Ballistic RWRE* (first published 2019; CPAM 2020), proves that in the uniformly elliptic i.i.d. setting `(T)`, `(T')`, `(T)_gamma` for some gamma, and `(P)_M` (at the stated large-M threshold) are equivalent. This does **not** identify any one of them with mere positive velocity. Thus the modern reformulation of the source question is essentially:

`positive velocity in ell  =>  (T)|ell ?`

A bounded 2026-09-19 current-literature check did not surface a theorem proving this implication. This is negative evidence only, not a worldwide openness certificate.

The source target is theorem-scale, so this artifact is an admission screen, not an admission or closure claim.

## 2. Obstruction first: positive speed does not imply a pointwise drift margin

The most tempting route would be to deduce a uniform one-step drift from positive limiting velocity and then use an exponential supermartingale. That logical implication is false even in the one-dimensional i.i.d. uniformly elliptic model.

For a one-dimensional nearest-neighbor environment write `p_x=omega(x,+1)`, `q_x=1-p_x`, and `rho_x=q_x/p_x`. Consider i.i.d. site types

- type A with probability `4/5`: `p=9/10`, `q=1/10`, `rho=1/9`;
- type B with probability `1/5`: `p=2/5`, `q=3/5`, `rho=3/2`.

This environment is uniformly elliptic with constant `1/10`. Moreover

`E[rho] = (4/5)(1/9)+(1/5)(3/2) = 7/18 < 1`.

By the standard exact one-dimensional RWRE speed formula, the limiting speed is

`v = (1-E[rho])/(1+E[rho]) = 11/25 > 0`.

Nevertheless every type-B site has one-step drift

`p-q = -1/5 < 0`.

This is **not** a counterexample to P0487, whose source is `d>=2`. It is a source-adjacent counterdiagnostic: any proof that tries to infer a uniform local drift inequality directly from positive velocity is structurally impossible without genuinely multidimensional/global input.

## 3. B8 — discretize the asymptotic question into slab exit probabilities

Fix any nearest-neighbor transition environment on `Z^d` (randomness of the environment is not needed for the lemma below). Let

`d_omega(x) := sum_{|e|=1} omega(x,e) e`

be its local drift vector. Let `ell` be a unit vector and assume the stronger pointwise hypothesis

`d_omega(x) . ell >= delta > 0` for every x.       (3.1)

The source asks whether a global asymptotic statement (positive velocity) already forces a quantitative slab-exit estimate. Under (3.1), the finite-slab estimate can be proved directly and uniformly.

### Theorem 3.1 — uniform local drift implies exponential wrong-way slab exit

Assume (3.1). If `ell'` is any unit vector with

`|ell'-ell| <= delta/2`,

then for every `L>0`, starting at the origin,

`P_omega(H_{-L}^{ell'} < H_{+L}^{ell'}) <= exp(- theta L)`,       (3.2)

where

`H_{-L}^{ell'} := inf{n>=0: X_n . ell' <= -L}`,
`H_{+L}^{ell'} := inf{n>=0: X_n . ell' >=  L}`

and one may take the explicit constant

`theta = delta/(2e)`.                                             (3.3)

In particular this family satisfies an exponential slab ballisticity condition uniformly in a neighborhood of `ell`; hence in the uniformly elliptic i.i.d. source setting it satisfies `(T)|ell`, and therefore, by the Guerra--Ramírez equivalence theorem, `(P)_M` for the standard large-M range.

### Proof

Because `|d_omega(x)|<=1`, for every `ell'` in the indicated neighborhood,

`d_omega(x).ell' >= d_omega(x).ell - |ell'-ell| >= delta/2`.

Put `eta=delta/2` and `theta=eta/e=delta/(2e)`. For a one-step projected increment

`Z=(X_{n+1}-X_n).ell'`

we have `|Z|<=1` and, conditional on `F_n`,

`E[Z | F_n] >= eta`.

For every `z in [-1,1]`, Taylor's formula with integral remainder gives

`exp(-theta z) <= 1-theta z + (theta^2 e^theta)/2`.

Since `theta<=1/e<1`, `e^theta<=e`; hence

`E[exp(-theta Z) | F_n]
 <= 1-theta eta + theta^2 e/2
 = 1-theta eta/2
 < 1`,

where the equality uses `theta e=eta`.

Therefore

`Y_n := exp(-theta X_n.ell')`

is a nonnegative supermartingale. Let

`tau = H_{-L}^{ell'} wedge H_{+L}^{ell'}`.

For every N, optional stopping for `tau wedge N` gives

`E[Y_{tau wedge N}] <= Y_0=1`.

On the event `{H_{-L}^{ell'} < H_{+L}^{ell'}, tau<=N}` we have

`X_tau.ell' <= -L`

and thus `Y_tau >= exp(theta L)`. Consequently

`P(H_{-L}^{ell'} < H_{+L}^{ell'}, tau<=N) <= exp(-theta L)`.

Letting `N->infinity` proves (3.2). No assumption that `tau` is almost surely finite is needed. QED.

### Corollary 3.2

The theorem actually holds for every deterministic nearest-neighbor environment satisfying the pointwise drift margin. I.i.d. and uniform ellipticity enter only when translating the resulting exponential slab estimate into the conventional RWRE ballisticity conditions used in the source literature.

This completely solves a strict source-valid subclass, but it does not move the source question because positive velocity alone does not supply (3.1).

## 4. B12 — find what is conserved: the exact exponential harmonic function

The preceding supermartingale is not an arbitrary trick. In the homogeneous biased case it is the deformation of an exact conserved quantity.

Take `ell=e_1` and a constant nearest-neighbor kernel with

- probability `p` to move `+e_1`,
- probability `q` to move `-e_1`,
- total probability `r=1-p-q` to take transverse steps,

where `p>q>0`. Define

`rho=q/p in (0,1)`.

Then

`f(x)=rho^(x_1)`

is exactly harmonic, because

`E[f(X_{n+1}) | X_n=x]
 = f(x) [p rho + q rho^(-1) + r]
 = f(x) [q+p+r]
 = f(x)`.

Thus `rho^(X_n.e_1)` is a true martingale. This is the exact conserved exponential quantity from which the general local-drift supermartingale descends.

The structural lesson for P0487 is sharp: the desired slab estimate follows once one can construct a positive exponential Lyapunov/harmonic object with a uniform quenched drift inequality. Positive limiting velocity is only a long-time averaged output; the missing theorem is precisely a mechanism upgrading that output to such a uniform or renormalized exponential object.

## 5. B26 — solve the homogeneous sporadic case exactly

For the homogeneous model above let

`tau = inf{n>=0: X_n.e_1 in {-L,+L}}`

with integer `L>=1`. The projected coordinate is a lazy biased nearest-neighbor walk, so `tau<infinity` almost surely. Let

`h_L=P_0(X_tau.e_1=-L)`.

Optional stopping of the bounded stopped martingale gives

`1 = h_L rho^(-L) + (1-h_L)rho^L`.

Solving,

`h_L = (1-rho^L)/(rho^(-L)-rho^L)
     = rho^L/(1+rho^L)`.

Therefore

`boxed[ P_0(H_{-L}<H_{+L}) = (q/p)^L / (1+(q/p)^L) ]`.          (5.1)

The exact wrong-way exponent is

`log(p/q)`.

The velocity is simply

`v.e_1=p-q>0`.

So P0487 is true in this fully homogeneous uniformly elliptic subclass, with an explicit sharp slab exponent. The general theorem in Section 3 replaces the exact harmonic identity by a robust superharmonic inequality but pays a crude exponent `delta/(2e)`.

## 6. What the source now reduces to conceptually

The 2019/2020 Guerra--Ramírez theorem removes one historical ambiguity: one no longer has to choose separately between `(T)`, `(T')`, `(T)_gamma`, or `(P)_M`. For P0487 the hard implication is the first bridge

`positive limiting velocity  --->  exponential/stretched-exponential slab control`.

Sections 3--5 prove that the bridge is automatic if positive velocity can be strengthened to a uniform local drift margin. Section 2 proves that such a strengthening is not a formal consequence of speed even in the closest one-dimensional i.i.d. analogue.

A genuine attack therefore needs a **renormalized** substitute for pointwise drift: e.g. a block-scale random exponential Lyapunov function, regeneration estimate, or environment-seen-from-the-particle mechanism that converts positive speed into uniformly rare backward slabs without assuming the conclusion.

This is theorem-scale HARD work, not a sharp finite certificate. P0487 is therefore **HARD / OPEN-LOOKING / NOT ADMITTED by R7-05**.

## 7. Admission and novelty accounting

- canonical ID: `P0487`;
- shard: 4;
- canonical claim file `operations/claims/P0487.md`: absent at the checked snapshot;
- source identity/locator recovered from repository source materials;
- bounded current-literature check: performed 2026-09-19;
- later equivalence theorem reconciled: yes;
- source-equivalent positive-velocity implication found: no in bounded search;
- negative-search caveat: yes;
- classification: HARD, not CLOSABLE;
- R7-05 admission: NO;
- source closure: NO;
- novelty claim: NONE.

The uniform-drift theorem is an elementary restricted result and is not asserted novel. Its purpose is to isolate the exact missing upgrade in the source question.

## 8. R7-05 state after this screen

No successor source is admitted. R7-05 remains `PENDING_ADMISSION` with no target-specific metric and no inherited stagnation count.

The preceding material lifecycle event E0011 is now definitively unavailable to R7-05: the post-release controlling claim `operations/claims/E0011-REASSIGNED-2026-09-19.md` assigns it to native slot `6aa7b4cc3c78819187a22c2c51acf674` with a fresh route and metric.

This artifact therefore records useful admission mathematics without pretending that a HARD source satisfies the CLOSABLE slot requirement.