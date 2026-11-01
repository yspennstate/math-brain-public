# An erasure-entropy reformulation of FEI

Status: the identities and implications below have complete self-contained proofs. Their novelty is **unverified**. The dimension-free estimate in Section 4 is **OPEN**. This document does not prove FEI.

All logarithms denoted log_2 are in bits. Write ln for natural logarithms. Let f:{-1,1}^n -> {-1,1}, a_S=E[f chi_S], p_S=a_S^2, H(f)=-sum p_S log_2 p_S and I(f)=sum |S|p_S. Set 0 log 0=0. Let X be the random subset with probability p_S.

## 1. Exact identity

For i in [n], put

    B_i(f)=H(X_i | X_{-i}),   B(f)=sum_i B_i(f),
    Delta_i(f)=H(f)-[H(f_{i=+1})+H(f_{i=-1})]/2.

For each T not containing i let u=a_T, v=a_{T+i}, m=u^2+v^2. The restrictions have coefficients u+v and u-v. Their squared coefficient distributions q_+ and q_- have common average m. In particular m, as a function of T, is a probability distribution.

Define h(t)=-t log_2 t for t>=0 and E(r,s)=h(r)+h(s)-h(r+s). The chain rule gives

    B_i(f)=sum_T E(u^2,v^2).

The Jensen–Shannon divergence is

    JS(q_+,q_-)=sum_T [h(m)-h((u+v)^2)/2-h((u-v)^2)/2].

Adding these displayed expressions cancels h(m) term by term and proves

    Delta_i(f)=B_i(f)+JS(q_+,q_-).                         (1)

Consequently Delta_i>=B_i>=0. No independence of the spectral coordinates is assumed.

## 2. A uniform bound for the JS remainder

Let psi be the binary entropy. For z in [0,1], define

    d(z)=[(1+z) ln(1+z)+(1-z) ln(1-z)]/2.

We claim d(z)<=1-sqrt(1-z^2). Both sides vanish at zero, and their derivatives are atanh(z) and z/sqrt(1-z^2). The difference of these derivatives is nonnegative: it vanishes at zero and has derivative

    (1-z^2)^(-3/2)-(1-z^2)^(-1)>=0.

Integrate, then use continuity at z=1. Since

    1-psi((1+z)/2)=d(z)/ln 2,

the contribution of (u,v) to JS is at most

    [m-sqrt(m^2-4u^2v^2)]/ln 2
      =[u^2+v^2-|u^2-v^2|]/ln 2
      =(2/ln 2) min(u^2,v^2).

Summing proves

    0<=JS(q_+,q_-)<=(2/ln 2) sum_T min(p_T,p_{T+i})
                   <=(2/ln 2) min(Inf_i(f),1-Inf_i(f)).   (2)

The scalar constant 2/ln 2 is sharp in the limit v/u -> 0. Sharpness for the sum over Boolean spectra is not needed for any implication here.

Combining (1)-(2), with J(f)=sum_i min(Inf_i(f),1-Inf_i(f)), gives

    B(f)<=sum_i Delta_i(f)<=B(f)+(2/ln 2)J(f).             (3)

## 3. Relation to full entropy and tensor products

For any random binary vector, conditioning reduces entropy. In an arbitrary fixed coordinate order,

    H(X_i | X_{-i})<=H(X_i | X_1,...,X_{i-1}).

Summing and applying the chain rule proves B(f)<=H(f). For independent spectra p and q (equivalently a product f(x)g(y) on disjoint variables), conditional entropies add, so

    B(fg)=B(f)+B(g),   H(fg)=H(f)+H(g),
    I(fg)=I(f)+I(g),   J(fg)=J(f)+J(g).

Multiplication by a character chi_A translates the spectrum by XOR with A. B and H are unchanged, and choosing A={i:Inf_i(f)>1/2} gives I(f chi_A)=J(f). This proves that uniform bounds with I and with J are equivalent, with the same constant, for both B and H. It does not permit replacing physical coordinates by arbitrary linear combinations without changing the influence budget.

## 4. Equivalence up to an explicit additive constant

Suppose, for every Boolean f in every dimension,

    B(f)<=K I(f).                                        (E_K)

Then (3) implies sum_i Delta_i <= (K+2/ln 2) I. If I>0, there is a coordinate with Inf_i>0 and

    Delta_i <= (K+2/ln 2) Inf_i.

Indeed irrelevant coordinates have Delta_i=0, and otherwise the contrary strict inequalities could be summed. Restrict on this coordinate. The elementary influence identity is

    I(f)=[I(f_+)+I(f_-)]/2+Inf_i(f).                      (4)

To prove (4), for every j!=i average the j-edge boundary indicators over x_i; the remaining i-boundary contributes Inf_i. Induction in dimension, with the constant case as base, now gives

    H(f)=[H(f_+)+H(f_-)]/2+Delta_i
        <=(K+2/ln 2)([I(f_+)+I(f_-)]/2+Inf_i)
        =(K+2/ln 2) I(f).

Conversely FEI with constant C implies B<=H<=CI. Therefore, if

    C_FEI=sup H(f)/I(f),   K_E=sup B(f)/I(f),

over nonconstant Boolean functions of all dimensions, then in the extended real sense

    K_E <= C_FEI <= K_E+2/ln 2.                           (5)

Thus finiteness of K_E is equivalent to FEI. The exact remaining task is to bound K_E, not to reprove this induction.

## 5. A one-sided logarithmic residual

Use h(r)+h(s)-h(r+s)=r log_2(1+s/r)+s log_2(1+r/s), with boundary values defined by continuity. Orient spectral edges from T not containing i to S=T+i. Define

    L(f)=sum_{S} p_S sum_{i in S} log_2(1+p_{S-i}/p_S),   (6)

where terms with p_S=0 are zero. Then log(1+t)<=t gives

    L(f)<=B(f)<=L(f)+I(f)/ln 2.                          (7)

The missing inequality can therefore be localized to the downward logarithmic ratios in (6). The upward terms are already paid by the influence. This preserves exact spectral adjacency and is not a replacement by marginal entropies.

An elementary global Jensen estimate loses the needed uniformity:

    L(f)<= I(f) log_2(1+(n-I(f))/I(f))
          = I(f) log_2(n/I(f)).                          (8)

To see this, weight each oriented edge (S,i) by p_S/I. The sum of its ratio contributions is at most (n-I)/I; missing edges with p_S=0 only reduce it. Concavity of log gives (8). This is a **failed closure route**: it discards the Boolean constraints.

## 6. The Boolean constraints that a successful argument must use

For every nonempty U,

    sum_S a_S a_{S xor U}=0,    sum_S a_S^2=1.             (9)

These follow by Fourier transforming f^2=1. Conversely, for a real vector a, (9) implies that its inverse Walsh transform takes values in {-1,1}. Thus an equivalent algebraic problem is to control (6) under these exact signed convolution constraints. A nonnegative arbitrary distribution p does not suffice.

For example independent Bernoulli(theta) spectral bits have B=n psi(theta), I=n theta, so B/I=psi(theta)/theta tends to infinity. These distributions generally cannot be squared Boolean spectra. In fact for n=1 the only Boolean spectra are point masses or their identical complements, immediately excluding a nontrivial Bernoulli law. Do not relax away (9) and expect a dimension-free result.

## 7. Prior art and scope

Coordinate restriction induction and the local binary-entropy expression are present in González–MacManus–Pereyra, arXiv:2606.00246v2, section 4 and Appendix B. Equations (1)-(5) are written here in conditional-entropy/Jensen–Shannon language, with all constants checked directly. The prior-art search has not established that the aggregate erasure formulation or the sharpened scalar constant is new. Ordinary chain rules, Jensen–Shannon divergence and tensorization are standard.

The proven reduction is a route to the original universal problem. It does not establish a new class satisfying FEI, improve a known universal bound, or constitute a solution.
