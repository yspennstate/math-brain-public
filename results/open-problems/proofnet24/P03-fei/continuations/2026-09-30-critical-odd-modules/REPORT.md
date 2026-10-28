# FEI: odd-module exclusion from entropy-decrement critical cores

Date: 2026-09-30. **Full FEI remains OPEN.** These are exact structural and transport lemmas, not a proof or disproof of FEI. No publication-priority claim is made.

## 1. Result and first unpaid implication

Call a Boolean function C-critical for coordinate restriction when every relevant physical coordinate satisfies `Delta_i H > C Inf_i`. The new useful restriction is the following. If a critical function is a balanced disjoint composition and one inner module is odd, its outer influence must be exponentially small on the inverse scale of every relevant influence inside that module:

    q < d^(-2) 2^(3/ln(2) - C/d).

An additional coarsening inequality says that the corresponding outer coordinate must itself have large erasure ratio:

    B_j(G)/q > C - 1/2 - (2/ln(2)) d.

These exclude diffuse odd modules whose outer occurrence is not sufficiently rare. They do not provide a generic decomposition of an arbitrary Boolean function. **Composition-prime critical cores are untouched.** The statement does not assume that all low-influence functions are tractable.

An exact companion construction shows that small variance, small total influence, and small maximum influence relative to variance can all coexist while preserving an arbitrary seed FEI ratio. The construction has explicitly affordable control coordinates, and therefore **does not preserve criticality**. This distinction is essential.

## 2. Current sources and correction boundary


Exact balanced disjoint-composition identities used here are already established in:

- [F4 restriction/composition report](https://github.com/yspennstate/math-open-problems/blob/2fefba564fdaf0232db13ff468a89063ab29bc6c/proofnet24/P03-fei/continuations/2026-09-22-opus-team/F4-proof-attempt/REPORT.md), especially Theorems 3.1 and 4.1. This report already reduces FEI to tiny influences and gives genuine Boolean examples with all-coordinate decrement ratio above 7.05. It prohibits treating a proposed constant near four as established.
- [Shalev, On the Fourier Entropy Influence Conjecture for Extremal Classes](https://arxiv.org/abs/1806.03646): low-total-influence reductions are prior literature. The joint-smallness statement below is a parameter-combination admission test, not a novelty claim or a replacement of that work.

The independent current-sprint balanced regularization supplied by `advance_fei_amortization` is reconstructed in Section 6 rather than accepted on authority. The all-dimensional module proofs below are self-contained.

## 3. Definitions and scalar inequalities

All cubes are uniform. Outputs are in `{−1,1}`. Set

    H(f) = sum_S fhat(S)^2 log2(1/fhat(S)^2),
    Inf_i(f) = sum_(S contains i) fhat(S)^2,
    I(f) = sum_i Inf_i(f).

Write `Delta_i H = H(f) - [H(f_i^+)+H(f_i^-)]/2`. For a pair of Fourier amplitudes `(a,b)` define

    E(x,y) = x log2(1+y/x) + y log2(1+x/y),
    J(a,b) = 1/2 [(a+b)^2 log2((a+b)^2/(a^2+b^2))
                   +(a-b)^2 log2((a-b)^2/(a^2+b^2))].

Use continuous zero conventions. Grouping amplitudes across physical coordinate i gives the exact identity

    Delta_i H = B_i + JS_i,
    B_i = sum_R E(ahat_R^2,bhat_R^2),
    JS_i = sum_R J(ahat_R,bhat_R).

Here JS_i is the Jensen–Shannon divergence between the two normalized child squared Fourier laws. Each term is nonnegative.

The following scalar estimates will be used:

    E(x,y) <= y log2(e(x+y)/y),                         (3.1)
    sum_l E(x_l,y_l) <= E(sum_l x_l,sum_l y_l),          (3.2)
    J(a,b) <= (2/ln 2) min(a^2,b^2).                   (3.3)

For (3.1), use `x ln(1+y/x)<=y`. Equation (3.2) is homogeneous concavity, or the two log-sum inequalities. For a direct proof of (3.3), put `p=a^2+b^2`, `r=2|ab|/p` and

    k(r) = [(1+r)ln(1+r)+(1-r)ln(1-r)]/2.

Then `J=p k(r)/ln 2`. Since `k'(r)=atanh(r)<=r/sqrt(1-r^2)`, integration gives `k(r)<=1-sqrt(1-r^2)`. The derivative inequality follows by differentiating its two sides from zero: `(1-r^2)^(-1) <= (1-r^2)^(-3/2)`. Hence `p k(r)<=p-|a^2-b^2|=2 min(a^2,b^2)`.

## 4. Exact odd-module reduction and critical-core exclusion

Let

    F = G(g_1,...,g_m)

be a composition on disjoint variable blocks. Every child is balanced, `E g_l=0`. Suppose child `g_j` is odd under simultaneous negation of all its input coordinates. Fix a relevant physical coordinate i of that child. Write

    q = Inf_j(G)>0,   d = Inf_i(g_j)>0,   c = ghat_j({i}).

For outer residual indices T not containing j, put

    a_T = Ghat(T),   b_T = Ghat(T union {j}).

### Theorem 4.1: exact packets

    Inf_i(F) = qd,                                                (4.1)
    B_i(F) = sum_T E(a_T^2,c^2 b_T^2),                             (4.2)
    JS_i(F) = sum_T J(a_T,c b_T).                                  (4.3)

In particular,

    B_i(F) <= E(1-q,c^2 q),
    JS_i(F) <= (2/ln 2)c^2 q.                                    (4.4)

**Proof.** Balanced disjoint composition has coefficient factorization

    Fhat(union_l S_l) = Ghat(U) product_(l in U) ghat_l(S_l),
    U={l:S_l is nonempty}.

This gives (4.1). Oddness means the Fourier support of `g_j` contains only odd-cardinality sets. For every nonempty residual set R in its block, `ghat_j(R)` and `ghat_j(R union {i})` cannot both be nonzero. Thus at these packets one of the two parent amplitudes vanishes; both E and J vanish.

At empty residual set inside child j the amplitude pair is `(a_T,c b_T)`, multiplied by the other selected children’s Fourier coefficients. Homogeneity lets those factors be squared and summed. Each other balanced child contributes total squared nonempty Fourier mass one, yielding (4.2) and (4.3). Finally `sum a_T^2=1-q`, `sum b_T^2=q`; apply (3.2) and (3.3). This argument keeps all physical packets and does not drop an unnormalized child mass. QED.

### Theorem 4.2: influence-scale exclusion

    Delta_i H(F)/Inf_i(F)
      <= d [log2(1/(q d^2)) + 3/ln 2].                           (4.5)

**Proof.** The Boolean derivative `D_i g=(g_i^+-g_i^-)/2` takes values in `{−1,0,1}`. Therefore `|c|=|E D_i g|<=E|D_i g|=d`. Equations (3.1) and (4.4), with `1-q+c^2q<=1`, give

    Delta_i H(F) <= qc^2 [log2(1/(qc^2))+3/ln 2].

The function `u -> u[log2(1/(qu))+3/ln 2]` is increasing for `0<=u<=1`, because its derivative is `log2(1/(qu))+2/ln 2>0`. Substitute `c^2<=d^2`, then divide by qd. QED.

Thus any C-critical F containing this decomposition must satisfy

    q < d^(-2) 2^(3/ln 2-C/d).                                  (4.6)

For example, at C=100 and d=1/2 this forces `q<2^(-193.67...)`. For d much smaller, the exclusion is stronger. This is an outer occurrence constraint, not a proof that such q cannot occur.

If `c=0`, the exact identities give `Delta_i H(F)=0`, so the coordinate is immediately affordable. All statements require balanced children and oddness at the actual node of application. Arbitrary physical restrictions need not preserve those hypotheses.

## 5. Coarsening transfers large erasure to the outer gate

### Scalar lemma

For `a,b>=0`, `0<=t<=1`,

    E(a,t^2 b) <= t E(a,b) + (t/2)b.                             (5.1)

**Proof.** Boundary cases follow by continuity. Normalize b=1, write x=a/b, and use homogeneity:

    E(x,t^2)/t = E(x/t,t).

At fixed product, E is maximal at equal arguments and decreases with increasing imbalance. This elementary fact follows by differentiating `E(s exp(z),s exp(-z))`; for z>0 the derivative has the sign of `tanh(z) ln(2cosh(z))-z`, which is nonpositive. To see that sign directly, its negative is zero at z=0, tends to zero at infinity, and its derivative is `sech(z)^2[1-ln(2cosh(z))]`, with just one sign change.

If x>=1, passing from `(x,1)` to `(x/t,t)` increases imbalance, giving no positive difference. If 0<=x<=1, fixed-product maximization gives `E(x/t,t)<=2sqrt(x)`. Also `E(x,1)>=2x`: divide by `1+x` and use concavity of binary entropy above its chord on `[0,1/2]`. Consequently the difference is at most `2sqrt(x)-2x<=1/2`. QED.

Apply (5.1) to (4.2) with t=|c|:

    B_i(F) <= |c| B_j(G) + (|c|/2)q.

Using |c|<=d and (4.4) proves

    B_i(F)/Inf_i(F) <= B_j(G)/q + 1/2,                          (5.2)
    Delta_i H(F)/Inf_i(F)
       <= B_j(G)/q + 1/2 + (2/ln 2)d.                          (5.3)

Thus a C-critical F forces the corresponding outer erasure ratio to exceed `C-1/2-(2/ln 2)d`. The scalar constant one half is a convenient analytic bound, not asserted sharp. Numerical optimization suggested a smaller constant, but that optimization is neither used nor promoted to a theorem.

Equations (4.6) and (5.3) are compatible: an odd module can escape the first test only through a sufficiently rare outer occurrence, and the outer coordinate must also retain high erasure. No argument here eliminates composition-prime outer gates or charges repeated coarsening with an unjustified finite budget.

## 6. Joint-smallness transport, with an explicit affordable-coordinate certificate

### Activation ledger

Let h and g be balanced Boolean functions on disjoint blocks. Take r independent copies of g and set

    A=product_(j=1)^r (1+g_j)/2,  p=2^(-r),  F=1-A+Ah.

Then F is Boolean, equal to h when all controls are +1 and otherwise equal to +1. Exact identities are

    E F=1-p,    Var(F)=2p-p^2,
    I(F)=p[I(h)+r I(g)],                                       (6.1)
    max_i Inf_i(F)=p max(max_i Inf_i(h),max_i Inf_i(g)),         (6.2)
    H(F)=pH(h)+prH(g)+4pr-phi(p^2)+phi((1-p)^2),                (6.3)

where `phi(t)=t log2(1/t)`.

**Proof.** A control physical derivative affects F only when the other r−1 controls activate and h=−1, so its influence is `2^(-(r-1))*(1/2) Inf_i(g)=p Inf_i(g)`. Data influences are `p Inf_i(h)`. This proves (6.1)–(6.2), while the mean is immediate.

For the entropy identity, A has squared Fourier norm p. Its normalized squared Fourier distribution is a product of r laws, each placing probability 1/2 at the empty label and probability 1/2 on the nonempty spectrum of g. Thus its raw, unnormalized spectral entropy is

    sum_U phi(Ahat(U)^2)=p r[2+H(g)/2].

All nonempty pure-control coefficients of F are `-Ahat(U)`; its constant coefficient is `1-p`. All h-containing coefficients are the tensor product of the coefficients of A and h, and are disjoint from the pure-control labels because h is balanced. Add their raw entropies, remove the old pure-control empty atom p², and insert `(1-p)^2`. This proves (6.3). QED.

### Theorem 6.1: simultaneous smallness remains FEI-hard

For every nonconstant Boolean seed f with H(f)>0 there is a sequence F_k of genuine Boolean functions such that

    Var(F_k) -> 0,    I(F_k) -> 0,
    max_i Inf_i(F_k)/Var(F_k) -> 0,
    H(F_k)/I(F_k) -> H(f)/J >= H(f)/I(f),                       (6.4)

where `J=sum_i min(Inf_i(f),1-Inf_i(f))`.

**Proof.** Multiply f by a character to toggle each Fourier bit whose marginal exceeds 1/2. The resulting u has unchanged entropy, I(u)=J, and each influence at most 1/2. H(f)>0 implies J>0, because J=0 would force its squared Fourier law to be a point mass.

Let M be ternary majority. It is balanced and odd, with H(M)=2, I(M)=3/2 and every influence 1/2. Form the disjoint product

    G_k=M product_(l=1)^k u_l.

It is balanced, has H(G_k)=kH(f)+2, I(G_k)=a_k=kJ+3/2, and maximum influence at most 1/2. Let h_k be the depth-k balanced disjoint self-composition of G_k. Exact coefficient factorization and entropy chain rule give

    I(h_k)=a_k^k,
    H(h_k)=(kH(f)+2)(a_k^k-1)/(a_k-1),
    max Inf(h_k)<=2^(-k).

Let g_k be depth-k recursive ternary majority. Then

    I(g_k)=(3/2)^k,
    H(g_k)=4[(3/2)^k-1],
    max Inf(g_k)=2^(-k).

Use the activation ledger with `r=k^2`, `p=2^(-k^2)`, h=h_k and g=g_k. Then

    I(F_k)=2^(-k^2)[a_k^k+k^2(3/2)^k] -> 0,
    Var(F_k)=2^(-k^2)(2-2^(-k^2)) -> 0,
    max Inf(F_k)/Var(F_k) <= 2^(-k)/(2-2^(-k^2)) -> 0.

The entropy/influence ratio tends to H(f)/J: divide (6.3) by `p a_k^k`. The control terms vanish since `k^2(3/(2a_k))^k ->0`; the term `4k^2/a_k^k` vanishes; and the constant-atom correction divided by p is bounded and tends to `2/ln 2`. The data term tends to `(kH(f)+2)/(kJ+1/2) -> H(f)/J`. This proves (6.4).

Consequently, a finite uniform FEI constant on the class with all three quantities below any fixed epsilon>0 would imply full FEI with that same constant. The theorem asserts only bounded absolute total influence, not an exponential bound in ambient dimension of the type covered by Shalev's positive theorem.

### Why this is not a critical-core counterexample

Each g_k is odd. At the outer activation gate its coordinate influence is q=p, and each of its physical coordinates has d=2^(-k). Theorem 4.2 gives the explicit certificate

    Delta_i H(F_k)/Inf_i(F_k)
       <=2^(-k)[k^2+2k+3/ln 2] -> 0.                          (6.5)

Thus the construction introduces cheap physical coordinates. It cannot be offered as evidence that a high-C all-coordinate critical core survives the padding. The remaining critical-core problem requires structure beyond joint-smallness estimates.

## 7. Verification and independent audit

The accompanying `check.py` uses integer Walsh transforms before numerical entropy evaluation. It checks every arity-three outer Boolean gate, every odd three-variable child, and every relevant coordinate with the other children balanced dictators: **8,640 coordinate cases**. It checks the exact packet identities, improved JS bound, logarithmic exclusion bound and coarsening bound.

It also checks **1,248 activation cases** built from all balanced data functions through dimension three, all balanced controls through dimension two, and one or two control blocks, plus **57,491 scalar parameter cases**. All pass. Maximum identity error is `5.551115123125783e-16`; no positive inequality violation was recorded. The attached output includes asymptotic parameter evaluations for an AND_2 seed, with its known ratio two. None of these numerical checks proves the universal statements.

A separate reviewer reconstructed the odd-module factorization, normalization, absence of hidden packets, scalar Jensen–Shannon proof, monotonic substitution |c|<=d, and the scalar coarsening inequality. Its audit confirmed all those statements. The exact activation/asymptotic ledger is separately audited in `AUDIT.md`. No proof-assistant formalization or full FEI verification is claimed.

## 8. Remaining target

These results give a source-valid necessary condition and a paid-coordinate test for actual decomposable functions. To prove full FEI, a next argument must either find an affordable coordinate/block in **every composition-prime critical core**, or produce a physical decomposition/selection theorem with a fully paid, nonreusing entropy ledger. Neither follows from small influences, a small variance, the presence of a rare activation, or the existence of a useful module in selected examples.

**Full FEI remains open.**
