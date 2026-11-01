# Independent heat/entropy audit of the stripe extension

2 October 2026. I read the full current
[candidate](stripe_extension_parallel_slabs_candidate.md), the completed
[largest-weight LTF proof](../2026-10-02-largest-weight/largest_weight_ltf_fei_proof.md), the independent
[K audit](stripe_extension_k_independent_audit.md), and the exact endpoint
[certificate](stripe_endpoint_equality_counterexample.json).

**Verdict:** analytic PASS for all parallel two-crossing slabs under the
uniform cube, with arbitrary weights, bias and endpoint conventions, and
for at most m crossings under strict separation greater than twice the
largest absolute input weight. I found no further gap in the repaired
candidate. This is an internal analytic audit, not external peer review or
historical novelty certification. The result does not prove unrestricted
Boolean FEI or the corresponding theorem for arbitrary nearby crossings.

## 1. Exact split and the narrow interval case

For the split f=A+zB, the pointwise identity A²+B²=1 makes the pair spectrum
P_S=Ahat(S)²+Bhat(S)² a probability law. The exact coefficient-pair entropy
calculation gives

Δ_z H = Σ_S P_S[1+h₂(q_S)−h₂(r_S)] ≤ 2Σ_S P_S h₂(q_S),

because h₂(t)≥4t(1−t) and r(1−r)=(1−2q)²/4. This argument does not require
B to be nonnegative, so the signed stripe derivative is permitted.

When the exceptional interval has width strictly less than 2w, the two
restricted exceptional supports are disjoint. After setting the outside
label to +1, the exact identities are A=1−|B| and |B|=B². Thus, with
α=E B² and β=E B,

Ahat(∅)=1−α, Bhat(∅)=β, |β|≤α.

The nonempty pair mass is at most 2α. For α<1/2, put x=β²≤α²<1/4. The
empty-pair conditional entropy is at most

x log₂(1/x)+(log₂ e)x
≤2α² log₂(1/α)+(log₂ e)α²<2α.

The first monotonicity bound is valid because x log(1/x) increases through
x=1/e, which is beyond 1/4. The last inequality follows from
sup α ln(1/α)=1/e and α<1/2. Therefore the full conditional inclusion
entropy is at most 4α and Δ_z H≤8α. If α≥1/2, its trivial bound 1 suffices;
if α=0, the restrictions coincide and Δ_z H=0. No monotonicity of the
stripe function or either exceptional branch is used.

## 2. Strict separation and the signed stability estimate

After removing attained-score ties, a largest-weight edge has length 2w
in score space. Strict separation ensures it crosses at most one retained
crossing point. Therefore the pivotal slabs B_r are disjoint, the signed
derivative is B=Σ_r ε_r B_r, |B|=Σ_r B_r is an indicator, and

α=E B²=Σ_r α_r.

Each retained crossing defines a nonconstant halfspace. Its largest-weight
influence α_r is positive by the same established Keller–Klein input used
in the LTF proof. There is no division by an α_r that is zero.

The resampling argument applies to the union without replacing α by a
larger event probability. Conditional on the mask and original X, sum at
most m interval concentration bounds. The good/bad mask depends only on
the mask, which is independent of X. Consequently multiplying by |B(X)|
and averaging preserves E|B(X)|=α. With μ=(1−ρ)R, the bound is

α[3m√2/√μ+e^(−μ/8)] ≤ 6mα/√μ,

since sup sqrt(μ)e^(−μ/8)=2e^(−1/2) and m≥1. The trivial bound is α.
The sign does not cause difficulty:

0≤Stab_ρ(B)=Σ_S ρ^|S| Bhat(S)²≤E|B(X)||B(Y)|

for ρ≥0. Uniform-cube hypercontractivity also applies to signed B, and
||B||_(3/2)²=α^(4/3) because |B| is an indicator. This verifies the two
stability inputs in the candidate independently of positivity of B.

## 3. Common low-degree scale

For Q_S=Bhat(S)²/α, the concentration estimate gives
Q(K≤k)≤18m√(k/R), when R>0. Hypercontractivity gives
Q(K≤k)≤2^k α^(1/3). Write T=ln(1/α). If 1≤k≤T/(6 ln 2), the latter is
at most e^(−T/6). The maximum of sqrt(T)e^(−T/6) is sqrt(3)e^(−1/2),
so the candidate's bound 3√(k/T) is valid. If k>T/(6 ln 2), use the
trivial bound 1 and sqrt(6 ln 2)<3. Combining with M=max{1,R,T} proves

Q(K≤k)≤18m√(k/M), k≥1.

For real k use its integer floor when needed. The R=0 and T=0 cases do
not require either corresponding estimate. The empty atom is

Q_0=(EB)²/α≤α,

because |EB|≤E|B|=α. Equality need not hold, and the KL proof only uses
the inequality.

## 4. Full spectrum tail and rare densities

For each crossing halfspace let p_r be its minority density and
L_r=ln(1/p_r). The established LTF inputs have the physical bit-flip
normalization, unchanged by using its indicator rather than its sign.
Its largest normalized input weight is 1/sqrt(R+1). Hence

α_r≥c p_r min{1,√(L_r/(R+1))}, α_r≤2p_r.

The second inequality has the required direction: the minority endpoint
of a pivotal edge occupies full-cube probability α_r/2. In particular
L_r≤ln(2/α_r).

A change in the stripe function under noise implies a change across at
least one crossing halfspace. Union bounding their KOS noise bounds gives
the full spectral tail, and thus the remaining-coordinate pair tail,
at most A₀ u^(−1/2)Σ_r p_r√L_r. When 0<u<1, independent noise at
rate 1/2 gives nonconstant full spectral mass at most 4Σ_r p_r; the
displayed A₀ is larger than 4/sqrt(ln 2), so that regime is also covered.

The potentially remote crossing is handled by an α-weighted average,
not a maximum of its rarity. In detail,

Σ_r p_r√L_r
≤c^(−1)Σ_r α_r[√(R+1)+√L_r]
≤c^(−1)α[√(R+1)+√ln(2m/α)].

For λ_r=α_r/α, Cauchy–Schwarz gives
Σ λ_r sqrt(ln(2/α_r)) ≤ sqrt(ln(2/α)+Σ λ_r ln(1/λ_r)),
and the last entropy is at most ln m. Since R+1≤2M and
T+ln(2m)≤M[1+ln(2m)], this verifies exactly the stated Γ_m and
P(K≥u)≤Γ_m α√(M/u). The rare factor and scale agree with the low-degree
estimate; no interval small-set noise theorem is being assumed.

## 5. Dyadic KL and signed empty atom

Positive-degree bin j has lower endpoint M2^j and upper endpoint
M2^(j+1). Thus the P tail and Q low-degree bound give the claimed
P_j≤Γ_m α2^(−j/2) and Q_j≤18m sqrt(2)2^(j/2) for negative nonempty
bins. The negative-bin first moment is therefore uniformly bounded by
C_(−,m). Empty bins with upper endpoint below 1 are omitted legitimately.

With the candidate's reference law, nonnegativity of D(Qbin||Rref)
gives the lower bound on D(Qbin||Pbin), and data processing gives the
same lower bound on D(Q||P). The direction is correct. At the separate
empty atom q_*=Q_0≤α, its reference contribution is at least −q_*, while
the omitted baseline is at most q_* log₂(1/α)≤α log₂(1/α)≤(log₂ e)/e.
This proves the displayed D_m with the signed derivative. On every
positive Q mass, P_S≥α Q_S>0, so the denominator is never zero.

The included-bit entropy is exactly
α[log₂(1/α)−D(Q||P)]≤αD_m. The excluded-bit entropy is at most
α log₂ e by ln(1+t)≤t. The exact split inequality then gives
Δ_z H≤2(D_m+log₂ e)α. The statement is vacuous at α=0, where Q need
not be defined.

## 6. Endpoint repair and induction

The recorded equality obstruction is genuine. At weights (1,1/2,1/2)
and the open exceptional interval (−1,1), the largest-coordinate stripe
influence is 1/2 while each crossing halfspace influence is 3/4. At the
remaining score zero the two pivots cancel. Thus separation ≥2w with
arbitrary endpoint conventions does not justify α=Σα_r. This audit does
not extend the separated theorem to that endpoint condition.

The repaired strict statement avoids this obstruction. Since the full
attained score set is finite, each crossing can be moved into its
appropriate open adjacent gap while preserving the Boolean function.
A sufficiently small movement preserves a pre-existing strict separation
margin. For an arbitrary two-crossing interval there is no separation
constraint: moving both endpoints into gaps and avoiding the finitely
many hyperplanes b−a=2w_i preserves the truth table and produces either
the narrow or wide branch. Singleton score intervals can likewise be
represented by two distinct nearby endpoints around that attained score.
Infinite endpoints reduce to one-crossing LTFs or constants.

Restriction translates both endpoints or all crossing points together.
The interval class remains an interval class; a strict crossing separation
remains strict when the maximum remaining weight decreases. The exact
influence decomposition

I(f)=I_z(f)+[I(f⁺)+I(f⁻)]/2

therefore supplies the dimension induction with the same constant at every
node. Fewer retained crossings only improves the upper bound m. All
zero-weight, constant and zero-variable cases are already covered.

The candidate's optional remark that nonattained, equality-separated
crossing points have disjoint open pivotal intervals is correct as a local
representation observation. It is unnecessary for either final theorem;
the separated theorem should continue to use strict separation and the
parallel-slab theorem should continue to use the generic narrow/wide split.

## Final assessment

Every requested analytic step passes for the repaired scope. The original
nonstrict endpoint extension has an exact proof obstruction, retained in
the certificate; it should not appear as an unrestricted final theorem.
No additional signed-spectrum, rare-density normalization, KL, endpoint,
or restriction-induction gap was found.
