# Physical occupancy after one shared-data query

Use bits x in {0,1}, signs +/-1, uniform physical measure and base-two entropy. For m>=1 write t=2^-m, Z=AND(z_1,...,z_m), g(u,v)=(-1)^(u+v), h(u,v)=1-2uv, and F_m=g if Z and a, h if Z and not a and b, and +1 otherwise. There are m+4 coordinates. The same data u,v serve both arms.

The baseline tree resolves z in order, stops at its first zero, then queries a and, only on a=0, b. Its leaves retain g,h,+1. The new tree first queries u and follows this controller tree, except that at u=0,a=0 it stops without querying b: h(0,v)=+1. All new-tree queries are essential. Terminals are constants or characters on v, not artificially completed constants.

## 1. The normalized Bayes reference

For a fixed exposed value u=c let L_c be the terminal controller transcripts. Their conditional physical reaches r_l sum to one. Their residual Fourier-square laws q_l(w), w in {empty,{v}}, each sum to one. Define exactly ONE conditional mixture

    q_c(w)=sum_(l in L_c) r_l q_l(w).

This reference is normalized. On occupied columns, the reverse reference is

    rho_c(l|w)=r_l q_l(w)/q_c(w).

It equals the actual conditional posterior of the physical-transcript/surviving-spectrum joint. Thus its conditional KL against that joint is zero. This prices a posterior; it does not pay its entropy by influence. At any coarser occupied history prefix, let A be the total mass of the column, G its mass in that prefix and B its mass at a terminal. Then (G/A)(B/G)=B/A. An empty prefix has all atom masses zero, so no division is needed there. Physical reach probabilities, including the rare controller activation, occur exactly once.

BayesOccupancy.lean checks the rational binary-mixture normalization, this occupied-prefix product identity and the nonnegative empty-prefix implication. Finite-tree recursion and the spectral interpretation are proved here and checked exactly by Python; they are not Lean entropy theorems. No new target axiom is introduced.

## 2. Equal leaf weights are a different reference

For u=0, the leaves are m early controller failures, one parity character g(0,v), and the final a=0 constant. Thus |L_0|=m+2 and

    q_0({v})=t/2,        qbar_0({v})=1/(m+2),

where qbar is the normalized equal-leaf mixture. For u=1, there are m early failures and three active leaves: g(1,v), h(1,v), constant. Both nonconstant cores are characters on v. Consequently

    |L_1|=m+3, q_1({v})=3t/4, qbar_1({v})=2/(m+3).

These statements hold for every m, by their explicit leaf list. The actual conditional reaches of the early failures are 2^-j (j=1,...,m), and those of the active leaves are t/2,t/2 on u=0 and t/2,t/4,t/4 on u=1. The conditional average Bernoulli KL cost of replacing q_c by qbar_c is

    K_m = [D_Ber(t/2 || 1/(m+2)) + D_Ber(3t/4 || 2/(m+3))]/2.

Each qbar_c is itself normalized. The error is to identify it with the physical mixture, or to use qbar_c as the column denominator with the original physical atoms: that putative posterior sums to q_c(w)/qbar_c(w), rather than one. Alternatively, treating qbar honestly as a new marginal reference leaves the displayed KL term. This is not a claim that every possible reference transfer must pay this particular KL separately; a signed global accounting could retain it with a matching rebate.

## 3. An all-dimensional, exact KL obstruction

In natural units, for 0<p<=q<1,

    D_Ber(p||q) = p ln(p/q)+(1-p)ln((1-p)/(1-q))
                >= -p ln(q/p)+(1-p)(q-p).

The latter logarithm is the integral of 1/(1-x) from p to q, hence at least q-p. For our p>=t/2, q<=1, ln(q/p)<=ln(1/p)<m+1. Also q>=1/(m+3). Therefore

    D_Ber(p||q) >= q-p(m+3)
                >= 1/(m+3)-(3/4)t(m+3).

For m>=10, (3/4)(m+3)^2 2^-m <=1/2. At m=10 the inequality is exact rational arithmetic; its left side decreases because the next/current ratio is (m+4)^2/[2(m+3)^2]<1. This also guarantees q>=p for both branches. Converting to bits divides by ln2<1, so

    K_m > 1/[2(m+3)]  for all m>=10.

Direct pivotal counting gives

    I(F_m)=t(5m/8+2).

Each z-coordinate contributes (5/8)t: the other controllers are all one with probability 2t and the inner priority sign differs from +1 with probability 5/16. The a contribution is (5/8)t and the b contribution is t/8. Each data coordinate contributes (5/8)t. Hence

    K_m/I(F_m) > 2^m/[2(m+3)(5m/8+2)] -> infinity.

This is a reference-accounting obstruction on an actual Boolean family, not an FEI disproof. In fact H(F_m)<4I(F_m): its nonempty root spectral mass is v0=(5t/4)(1-5t/16), with t<=v0<=5t/4 for m>=1. Splitting off the empty atom and using at most 2^(m+4) remaining atoms gives H<=h2(v0)+v0(m+4). Since h2(x)<=x(log2(1/x)+log2(e)), log2(e)<2 and log2(1/v0)<=m, H<(5t/4)(2m+6)<4t(5m/8+2). The elementary binary entropy inequality follows from -(1-x)ln(1-x)<=x.

## 4. The signed ledger and every terminal bill

Let M be the sum of reach-weighted erased-sector entropies, J the sum of reach-weighted branch JS, L the expected terminal Fourier entropy, Hp the entropy of the physical transcript, W the actual surviving spectral mask, B=H(Pi|W), jW=I(W;Pi), and Sigma=Hp/2+M-J. The finite physical Fourier split gives H(root)=M+J+L. Conditional on a leaf, W has precisely its Fourier law, so H(Pi,W)=Hp+L. Consequently

    H(root)=L+2M+B/2+jW/2-Sigma.

The exact checker verifies this identity as a rational prime-log coefficient identity, not by approximate entropy subtraction. For the baseline, L=t/2 and expected terminal influence is 5t/4. For the essential data-first tree, L=0, expected terminal influence is 5t/8, Hp=3-3t/4 and P(W={v})=5t/8. Thus B=3-3t/4-h2(5t/8) ->3. Its signed residual tends to 3/2, cancelling B/2. M,J ->0 since H(root)->0 and M,J are nonnegative. The character leaves remain in the influence ledger despite their zero spectral entropy. Stopping them is not equivalent to erasing their influence.

All leaves are independent of the entire potentially queried set A={u,z_1,...,z_m,a,b}. Hence the coherent surviving label is the fixed projection S intersect {v}, with zero schedule injection, even though b is not always queried. The fixed-projection spectral marginal equals the physical mixture by iterating the quadratic Fourier row identity; the checker independently verifies it from the root truth table and every leaf spectrum. The baseline retains both shared data coordinates instead.

## 5. First unsupported universal line

For arbitrary unfinished shared-core trees, the one physical Bayes/occupancy reference has a signed cost that can be bounded by a universal multiple of a single exclusive influence ledger while retaining all terminal entropy and influence. The rational identities prove normalization and compatibility only. They do not compare this reference with A038's owned reserve after arbitrary interleaving, or establish that universal cost bound. Equal leaf weights cannot serve as a free substitute even on the explicit one-data-exposure family above.
