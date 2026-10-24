# I0070 — endpoint time regularization

Date: 2026-10-12. The preliminary results below are proved. The full argument is written below for hostile checking; final verification status is recorded in STATUS.md.

## Verified question

Agresti–Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, NoDEA 32 (2025), article 123, DOI 10.1007/s00030-025-01090-2. Problem 6 is on printed p.130 (PDF p.131, including repository cover):

“Problem 6. (Time regularization in Hilbert spaces) Let X0 be a Hilbert space. Does the regularization result of Theorem 5.7 extend to p = 2 in the critical case (i.e. equality in (6.1) holds for some j)?”

The next reaction–diffusion paragraph is not part of this question.

The desired conclusion is almost-sure membership, on compact subintervals of (0,σ), in H^{θ,r}(X_{1−θ}) and C^{θ−ε}(X_{1−θ}), for θ∈[0,1/2), finite r≥2, and 0<ε<θ. The Hölder assertion is vacuous at θ=0. The equation is du+Au dt=F(u)dt+(Bu+G(u))dW. The p=2 critical inequalities are (2β_j−1)(ρ_j+1)≤1, with equality for some j, β_j∈(1/2,1). Retain the assumptions of Theorems 4.7 and 5.7, including linear SMR at all higher exponents and the extra growth hypothesis (5.21). Exact source excerpts are saved in source.txt and source_excerpts.txt.

## Proved preliminary lemma: interpolation at the critical exponent

Let (X0,X1) be a densely embedded Hilbert couple and H=[X0,X1]_{1/2}=(X0,X1)_{1/2,2}. For β∈(1/2,1), put a=2β−1. Reiteration of real interpolation identifies (H,X1)_{a,1} with (X0,X1)_{β,1}, up to equivalent norms. For z∈X1,

    ||z||_{β,1} ≤ Cβ ||z||_H^{1−a} ||z||_1^a.                 (I)

Here is the norm estimate explicitly. The K-functional of (H,X1) satisfies K(t,z)≤min(||z||_H,t||z||_1). Split the defining integral ∫_0^∞ t^{−a}K(t,z)dt/t at t0=||z||_H/||z||_1. Its two parts are bounded respectively by ||z||_H^{1−a}||z||_1^a/(1−a) and ||z||_H^{1−a}||z||_1^a/a. The zero case follows directly. Reiteration gives (I).

If a(ρ+1)=1, raising (I) to ρ+1 gives

    ||z||_{β,1}^{ρ+1} ≤ C ||z||_H^ρ ||z||_1.                 (II)

In particular, at criticality ρ>0. Smallness of ||z||_H, rather than a positive power of interval length, supplies smallness of the coefficient of ||z||_1.

## Proved preliminary lemma: tame growth near smooth bounded anchors

Suppose N=(F,G):X1→Y=X0×γ(U,H), with the sum norm, satisfies the locally H-bounded Lipschitz estimate of Assumption 4.1:

    ||N(x)−N(y)||_Y ≤ L_n Σ_j(1+||x||_{β_j,1}^{ρ_j}+||y||_{β_j,1}^{ρ_j})||x−y||_{β_j,1}

for ||x||_H,||y||_H≤n. Assume a_j(ρ_j+1)≤1. For every n,M,η>0 there are δ>0 and C<∞ such that

    ||N(x)||_Y ≤ η||x||_1+C                            (T)

whenever ||x||_H,||y||_H≤n, ||y||_1≤M and ||x−y||_H≤δ.

Proof. Set z=x−y. The elementary estimate (b+c)^ρ≤c_ρ(b^ρ+c^ρ) and ||y||_{β,1}≤C M reduce the displayed Lipschitz bound to a finite sum of K_{n,M}||z||_{β,1} and K_n||z||_{β,1}^{ρ+1}, plus ||N(y)||_Y. The last term is uniformly bounded by applying the same Lipschitz estimate to (y,0), since y has bounded X1 norm and N(0)∈Y. By (I), the first term is ≤K_{n,M}δ^{1−a}||z||_1^a. Because a<1, it is ≤ε||z||_1+C_ε by Young's inequality (or maximizing K t^a−εt on t≥0). For a(ρ+1)<1 the polynomial term has exactly the same sublinear-power argument, with ||z||_H≤2n. For a(ρ+1)=1, (II) bounds it by K_n δ^ρ||z||_1; here ρ>0, so δ can make this coefficient as small as desired. Choose each coefficient ≤η/(2m), sum, and use ||z||_1≤||x||_1+M. This proves (T).

These lemmas alone do not establish higher time integrability. Applying an L^r estimate to an already known L^2 solution would be circular.

## Earlier work and the repair used here

Use deterministic smoothing operators S_N:H→X1, uniformly bounded on H and converging strongly to I on H. Uniform convergence holds on each compact H-valued path range. Stop when ||u||_H exceeds n or ||(I−S_N)u||_H exceeds δ. With y=S_Nu, lemma (T) gives ||N(u)||≤η||u||_1+C_{n,N} on that interval.

The earlier R10 repository reports from 2026-09-16 already proposed this mechanism. They are saved read-only in prior_attempts.md. They were not a published solution or a certified verdict. The argument below checks the mechanism directly rather than trusting their status labels. A deterministic time cutoff avoids selecting smooth restart times or assuming higher regularity of initial data. In particular, no higher-exponent theorem is applied directly to an L^2 solution.

## Full endpoint theorem

Assume the p=2, κ=0 version of all hypotheses of Theorem 5.7, with X0 Hilbert. Thus λ0+A is sectorial on X0 for some λ0≥0, with domain X1=D(A); Assumption 4.1 holds at p=2; (A,B)∈SMR^bullet_{2,0}; u0 is strongly F0-measurable with values in H=X_{1/2}; retain (5.21) with X_{1/2,∞} and its stated exponents; and (A,B)∈SMR^bullet_{r,α} for every finite r>2 and 0≤α<r/2−1. Let (u,σ) be the maximal L^2 solution supplied by Theorem 4.7. Then the regularity conclusion of Theorem 5.7 holds, including equality in one or more criticality inequalities.

Only α=0 from the higher-exponent assumption is used. The proof actually does not need (5.21), but it is retained in the stated theorem to answer the source question without weakening or modifying its other hypotheses.

For clarity, the exact retained growth condition at p=2 is: for each n≥1 there exists C_n>0 such that, for x∈X1 with ||x||_{(X0,X1)_{1/2,∞}}≤n,

    ||F(x)||_{X0}+||G(x)||_{γ(U,X_{1/2})}
       ≤ C_n Σ_{j=1}^m (1+||x||_{(X0,X1)_{β_j,1}}^{ρ_j+1}).

The initial value hypothesis is u0∈L^0_{F0}(Ω;H), not a moment hypothesis. Equivalent Hilbert norms used below only change the numerical localization constants; they do not replace the source real interpolation spaces by different spaces.

### 1. Hilbert smoothing and progressive representatives

Equip X1=D(A) with its equivalent Hilbert graph norm. To justify equivalence even if X1 was initially given a different Banach norm: the embedding X1→X0 and A∈L(X1,X0) make the identity X1→D(A) with graph norm bounded; λ0+A is closed, so its graph domain is complete; and this identity is bijective, hence its inverse is bounded by the open mapping theorem. On Hilbert X0 the squared graph norm ||x||_0^2+||Ax||_0^2 comes from an inner product. Then H=(X0,X1)_{1/2,2}=[X0,X1]_{1/2} is Hilbert, and X1 embeds densely and continuously in H. Rescale the Hilbert norm on X1 so that ||v||_H≤||v||_1. The densely defined closed positive form q(v,w)=(v,w)_1 on H has a positive self-adjoint representing operator L≥I with D(L^{1/2})=X1 and ||L^{1/2}v||_H=||v||_1. This is the representation theorem for closed positive forms; equivalent norms do not alter any of the source spaces or hypotheses.

Set P_N=1_{[1,N]}(L), N=1,2,…. Spectral calculus gives

    ||P_N||_{H→H}≤1,   ||P_N x||_1≤N^{1/2}||x||_H,
    P_N x→x in H for x∈H, and in X1 for x∈X1.

Moreover convergence on H is uniform on compact subsets. Indeed, for a given compact K and ε>0, choose a finite ε/4-net {x_i}. For large N all ||(I−P_N)x_i||_H<ε/2. For x∈K choose i with ||x−x_i||_H<ε/4; since ||I−P_N||≤1, the error is <3ε/4. This proves the assertion without assuming that X1→H is compact or that P_N has finite rank.

Let σ_l↑σ be the source localizing times, with u continuous in H on [0,σ_l] and L^2(0,σ_l;X1) a.s. Use its H-continuous version and extend it after σ_l by its value at σ_l. Each P_N applied to this extension is a strongly progressively measurable X1-valued process. On the progressively measurable set where this sequence is Cauchy in X1, define its X1-limit, and define zero otherwise. This gives a strongly progressively measurable X1-valued representative û_l. The Cauchy set is measurable by its countable metric definition. Before σ_l, for almost every time and almost every sample, the original u belongs to X1 and spectral convergence shows û_l=u. Consequently F(û_l),G(û_l) agree with the source inhomogeneities there up to dt⊗P-null sets. This construction also handles a nonseparable ambient Hilbert space: the strongly measurable processes in question have essentially separable ranges, and their countable limits remain strongly measurable.

The representative argument has a useful pointwise strengthening. If the smoothing sequence is Cauchy in X1, its X1-limit is also its H-limit, hence equals u. Off that set û_l=0. Therefore the H-norm and spectral-tail bounds imposed on u hold pointwise for û_l as well, even at exceptional times where u has no X1 value. Setting C≥||N(0)|| then enforces the small coefficient bound at every such point; the equation identity is only needed dt⊗P-a.e.

### 2. A small adapted rank-one factorization

Fix n∈N and η>0. Apply (T) with H bound n, and choose δ=δ(n,η)>0 independent of M. Its independence follows from the proof: the only coefficients requiring a small δ are those of the critical powers of z, which depend on n and the source constants, not M. For each N, using y=P_N x with M=N^{1/2}n gives a deterministic C=C(n,N,η) such that

    ||N(x)||_Y≤η||x||_1+C

whenever ||x||_H≤n and ||(I−P_N)x||_H≤δ. Increase C if necessary so that C≥||N(0)||_Y.

For any such x write h=N(x), b=||h||_Y, and define h0=h if b≤C, and h0=(C/b)h if b>C; put h1=h−h0. Thus ||h0||≤C and ||h1||=(b−C)_+≤η||x||_1. If x≠0 set

    R_x v = (v,x)_1 h1 / ||x||_1^2,

and set R_0=0. Then R_x x=h1 and ||R_x||≤η, by Cauchy–Schwarz. Split R_x into its components c_x:X1→X0 and d_x:X1→γ(U,H), and h0 into f_x,g_x. Since the target uses the sum norm,

    ||c_x||+||d_x||≤η,
    F(x)=c_x x+f_x,   G(x)=d_x x+g_x,
    ||f_x||+||g_x||≤C.                                  (R)

The formulas are Borel on X1; they use continuous maps away from x=0, with a separately defined value at zero. On the localized sets N is continuous for the X1 norm, as follows from the source local Lipschitz bound and continuous embeddings. Along û_l all coefficient actions are strongly progressive. In fact the rank-one maps have norm-measurable essentially separable ranges: the maps (x,h1)↦R_x are continuous away from zero, and x,h1 have strongly measurable ranges. Thus they also define bounded multiplication operators on progressive L^p(Ω×I;X1).

### 3. Small linear perturbations, proved from SMR

On a deterministic finite interval I=[a0,b], let S_p(f,g) be the zero-initial-value strong solution for the original pair (A,B), for p=2 or p=r>2. Definition 3.7 gives

    ||S_p(f,g)||_{L^p(Ω×I;X1)}
       ≤M_p (||f||_{L^p(Ω×I;X0)}+||g||_{L^p(Ω×I;γ(U,H))}).    (S)

Take η with η max(M_2,M_r)<1/2. If strongly progressive c,d satisfy ||c||+||d||≤η, the map

    v ↦ S_p(cv+f,dv+g)

is a contraction on progressive L^p(Ω×I;X1). It has a unique fixed point v_p. Its equation is

    dv_p+Av_p dt=(c(t)v_p+f)dt+((B+d(t))v_p+g)dW.          (P)

The differential on the left is the Itô differential, and d(t) on the right is the small operator coefficient. All inputs are progressive and in the required spaces. The original SMR^bullet property applied to these inputs gives the stipulated time regularity of v_r. This proves the perturbation assertion used here directly; no extrapolation for a new random pair is being assumed.

We also need uniqueness against a solution with only pathwise L^2 integrability up to a stopping time τ∈[a0,b]. Suppose w has zero initial value and solves the homogeneous difference of (P) before τ, with paths in L^2(X1). Stop further at τ_m when ∫_{a0}^{t∧τ}||w||_1^2 reaches m. Then 1_{[a0,τ_m]}cw and 1_{[a0,τ_m]}dw have finite L^2(Ω×I) norms. Let W_m be the base-pair solution S_2 of those inputs on the full deterministic interval. Base-pair uniqueness on [a0,τ_m] gives W_m=w there. Consequently (S) gives

    ||1_{[a0,τ_m]}w||_{L^2(X1)}
      ≤||W_m||_{L^2(X1)}
      ≤M_2 η ||1_{[a0,τ_m]}w||_{L^2(X1)}.

The finite norm must be zero. Since τ_m↑τ a.s. by the assumed pathwise L^2 integrability, w=0 before τ. The stopped base-pair uniqueness used here is the uniqueness part of the source solution theory/Proposition 3.11; it also follows by localizing its finite-moment uniqueness as in that proposition. In particular, the argument does not require an a priori L^r bound for the comparison solution.

### 4. Apply the perturbation to a cutoff of the actual solution

Fix deterministic 0<a0<a<b<∞, r>2, and a smooth scalar χ on I=[a0,b] such that χ(a0)=0 and χ=1 on [a,b]. Let η be chosen as in Step 3. For each l,n,N, use the H-continuous stopped version from Step 1. On the F_{a0}-measurable event {σ_l>a0}, set τ to the minimum of b, σ_l and the first time t≥a0 at which ||u(t)||_H≥n or ||(I−P_N)u(t)||_H≥δ(n,η). If an initial bound fails, or σ_l≤a0, set τ=a0. These are stopping times, since the threshold functions are continuous adapted real processes. For t<τ the bounds in Step 2 apply. Values at single endpoints do not affect any integral.

Construct c,d,f0,g0 along û_l by (R) before τ and set all four equal to zero after τ and on paths with τ=a0. Define the full-interval progressive forcing

    f=1_{t<τ}(χ f0+χ' u),   g=1_{t<τ}χ g0.

The expression involving u uses its H-continuous version. Before τ, ||u||_H≤n and H→X0 continuously, so f and g are bounded by deterministic constants depending on l,n,N,χ (in fact l is unnecessary). Thus they belong to every finite L^p(Ω×I). The coefficients c,d have the bound η globally.

Step 3 constructs a zero-initial-value solution v_r on the **whole deterministic interval** I. This is crucial: a stopped process is not asserted to solve the unstopped equation after τ. Since r>2 and Ω×I has finite measure, v_r belongs also to L^2(Ω×I;X1).

For v_r, choose a fractional time exponent between 1/r and 1/2 and apply Proposition 2.1. It has a continuous X_{1−1/r,r} version, hence an H-continuous version, since X_{1−1/r,r} embeds continuously into H. Thus the comparisons below may use continuous versions at stopping times.

On [a0,τ], z=χu satisfies, by the product rule and scalar commutation with A,B,c,d,

    dz+Az dt=(cz+χ f0+χ'u)dt+((B+d)z+χ g0)dW,
    z(a0)=0.

It has pathwise L^2(X1) regularity, as does v_r. Their difference solves the homogeneous equation of Step 3 before τ, hence z=v_r there. Equality first holds a.e. and then for their H-continuous versions. Since v_r has the SMR^bullet_{r,0} time regularity, this proves the corresponding regularity of u on [a,b] on the event {τ=b}.

### 5. Remove all stopping conditions without anticipative choices

For a path with b<σ choose l with σ_l>b. Its H-continuous range on [a0,b] is compact. Choose n strictly larger than its H-norm supremum. By Step 1,

    sup_{t∈[a0,b]}||(I−P_N)u(t)||_H→0.

Thus for some N this supremum is strictly less than δ(n,η). For these indices τ=b. This proves that {b<σ} is covered by the **countable** union of {τ_{l,n,N}=b}. Each member was treated using adapted coefficients and deterministic constants. Choosing indices pathwise only proves that the already constructed countable events cover; it is never used to define an anticipative equation.

For every fixed θ∈[0,1/2), r>2 this proves u∈H^{θ,r}([a,b];X_{1−θ}) a.s. on {b<σ}. Taking rational a0,a,b gives local membership on (0,σ). Finite-interval embeddings H^{θ,q}→H^{θ,r} for q≥r extend this to all finite r≥2. These follow by interpolating the bounded inclusions L^q→L^r and W^{1,q}→W^{1,r} on the same finite interval.

For any θ>0 and 0<ε<θ choose an integer q>max(2,1/ε). The one-dimensional vector-valued Sobolev embedding gives H^{θ,q}(I;X_{1−θ})→C^{θ−1/q}(I;X_{1−θ})→C^{θ−ε}(I;X_{1−θ}). This proves the Hölder assertion, too. No θ=1/2 assertion is made.

As usual the parameterwise statements can be put on a common full-measure event. Take integer q, rational compact intervals and θ_k↑1/2. The mixed Sobolev interpolation identity for Hilbert scales,

    [L^q(I;X1), H^{θ_k,q}(I;X_{1−θ_k})]_λ
       = H^{λθ_k,q}(I;X_{1−λθ_k}),   0<λ<1,

with equivalent norms, gives all intermediate θ. This is the standard interpolation identity for vector-valued Bessel-potential spaces with Hilbert scale coefficients (apply a common extension operator on I, then complex interpolation of the time Bessel multiplier and the positive self-adjoint scale multiplier). Finite-exponent inclusions and the preceding Sobolev embedding give all r,ε. This final deterministic interpolation step is not an assertion that ordinary H^{θ_k,q} in a single fixed spatial space gives stronger spatial regularity; both the time and spatial scales are interpolated together.

This completes the endpoint argument subject to the checks below.

## Hostile referee checks

1. **Wrong theorem / fixed spatial-level obstruction:** the conclusion trades θ time derivatives for θ spatial derivatives. The 2509.07803 obstruction concerns W^{θ,2}(D(A^{1/2})) at a fixed spatial level and therefore does not contradict this conclusion.
2. **Critical coefficient not small:** the critical power of ||x−y||_1 is one, but its H-norm factor is δ^ρ and ρ>0; the source β<1 is essential. No positive interval-length gain is asserted.
3. **Compact embedding or commutation inadvertently assumed:** no finite-rank or compact embedding is needed; P_N may have infinite rank. Compactness is of one continuous path's image. P_N is used only in the nonlinear growth estimate, not to project the SPDE, so no commutation with A or B is assumed.
4. **Circular L^r estimate:** the L^r solution is constructed by contraction before comparison. Only stopped L^2 uniqueness identifies it with χu.
5. **Stopped process extended incorrectly:** all constructed linear solutions live on a deterministic interval, with coefficients and forcing extended by zero. χu is compared only before τ. The original B term is not switched off after τ.
6. **Random constants / anticipative cutoff:** constants are fixed for deterministic l,n,N; countable covering is performed afterwards.
7. **X1 adaptedness:** the spectral Cauchy-limit construction supplies the progressive representative before factorization.
8. **No initial spatial regularity:** χ(a0)=0 removes the original rough trace; χ'u is controlled in X0 by the stopped H bound.
9. **Moment assumption:** comparison uses only pathwise L^2 integrability, localized by its accumulated norm. All constructed L^r forcing is deterministically bounded.
10. **Unproved formal scope:** the Lean file checks only exponent and absorption algebra, not stochastic integration, interpolation, or the full theorem. Its execution result must be consulted separately.

## Boundary model: why a bounded Hilbert ball is not enough

Let X0=ℓ^2, J e_k=k^2 e_k, X1=D(J) with norm ||Jx||_2, and H=D(J^{1/2}). Fix β∈(1/2,1), a=2β−1, and ρ=1/a−1>0. Define

    F(x)=||J^β x||_2^{ρ+1} e_1,   G=0,   A=J,   B=0.

This is source-admissible at criticality: the real norm X_{β,1} controls ||J^β x||_2; the scalar mean-value inequality |s^{ρ+1}−t^{ρ+1}|≤(ρ+1)(s^ρ+t^ρ)|s−t| and the reverse triangle inequality give the source Lipschitz bound. Its global growth bound also implies (5.21). The linear Hilbert pair has all source SMR exponents by Theorem 3.13.

Take x_k=e_k/k. Exactly ||x_k||_H=1, ||x_k||_1=k, and ||J^β x_k||_2=k^a. Thus ||F(x_k)||_0=k and ||F(x_k)||_0/||x_k||_1=1. For any η<1, no constant C gives ||F(x)||≤η||x||_1+C on the entire H unit ball, since (1−η)k≤C would fail. The x_k are orthogonal unit vectors in H, so their set is not compact. This establishes the sharp distinction used in the proof: infinitesimal growth is localized by the small spectral tail of a compact path range, not merely by a bound on its Hilbert norm. This is a diagnostic example, not a counterexample to time regularization.

## Computational checks

endpoint_checks.py uses exact Fraction arithmetic for six critical exponent choices and 1,000 finite rank-one factorizations, including zero-input, zero-coefficient and zero-remainder bounds. Output is saved in endpoint_checks.json. All assertions passed; maximum reconstruction error was 5.671216916061934e−16. These checks test the elementary factorization and exponent formulas only.
