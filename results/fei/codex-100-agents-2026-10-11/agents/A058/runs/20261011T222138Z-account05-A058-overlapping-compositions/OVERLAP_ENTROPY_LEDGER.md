# Shared nonlinear gates with private sign anchors

All inputs have uniform product measure; Boolean means values in {-1,1}; entropy is in bits, with the empty Fourier atom included. Fix m,r >= 0, a Boolean outer gate F on m bits, and Boolean gates b_j on pairwise disjoint physical blocks z_j. The private bits x_1,...,x_m are disjoint from all these blocks. Let A be an arbitrary r by m binary matrix. Define

g_i(x,z) = x_i product_{j:A_ji=1} b_j(z_j),     f(x,z)=F(g_1,...,g_m).

There is no bound on column or row weight, biases, dimensions, or reuse. These are multiplicative, shared-input, non-selector compositions. Conditional on z the vector g is uniform, but that fact alone is insufficient to determine its Fourier entropy.

## Exact coefficient and physical influence ledger

Write a_T=Fhat(T), p_T=a_T^2, and U(T)=A 1_T over F_2. Since b_j^2=1 pointwise,

f(x,z)=sum_T a_T chi_T(x) product_{j:U_j(T)=1} b_j(z_j).

For a physical Fourier support (T,S_1,...,S_r),

fhat(T,S_1,...,S_r)=a_T product_j c_{j,U_j(T)}(S_j),

where c_{j,1}=bhat_j, and c_{j,0}(S)=1_{S=empty}. Distinct outer labels have distinct private supports T, so their amplitudes never interfere. This proves the coefficient formula directly; no disjoint-child composition identity is applied to g_i. The normalized squared law samples T~p, then conditionally independently samples S_j from bhat_j^2 when U_j(T)=1, and sets S_j=empty otherwise. Empty coefficients of biased b_j are retained.

Put d_j=Pr_p(U_j=1). Then

H(f)=H(F)+sum_j d_j H(b_j),
Inf_{x_i}(f)=Inf_i(F),
Inf_{z_j,k}(f)=d_j Inf_k(b_j),
I(f)=I(F)+sum_j d_j I(b_j).

Proof of entropy: the physical support reveals T exactly via its x coordinates. Apply the probability chain rule to the squared law just derived, then add the independent conditional block entropies. Proof of influence: weight that same law by the indicator that x_i or z_j,k lies in the support. This uses Parseval's Boolean influence identity. Thus every physical coordinate is counted once.

For a spatial proof of d_j, define the outer sign mask v_j with -1 at columns where A_ji=1 and +1 elsewhere. Orthogonality gives

d_j=(1-E_y[F(y) F(y*v_j)])/2=Pr_y(F(y) != F(y*v_j)).

Conditional on all physical inputs except a pivotal bit of b_j, flipping that bit applies precisely v_j to the uniform outer vector g. This independently reconstructs the influence formula. In particular d_j <= sum_{i:A_ji=1} Inf_i(F) by a telescoping path through those flips, but the exact d_j can be zero even when the displayed sum is arbitrarily large.

## Collision posterior, fully retained

Let q_u=sum_{T:U(T)=u}p_T. For q_u>0 the posterior is p(T|u)=p_T/q_u on that fiber. Set

B=sum_u q_u H(p(.|u)).

The exact ledger is

H(f)=H(q)+B+sum_j d_j H(b_j).

The collision fibers are those of the binary incidence map. The posterior B is a positive residual, not an available entropy rebate. Indeed H(q)+B=H(F). All posterior uncertainty is paid by the outer influence budget once an outer FEI bound is supplied. We never replace H(F) by H(q). Likewise repeated occurrences of b_j cancel pointwise before Fourier expansion: copying their spectra independently would be false. This is the structural mechanism controlling coherent overlap, rather than an assumed entropy-subadditivity inequality for overlapping products.

If H(F)<=C_0 I(F) and H(b_j)<=C_j I(b_j) for every j, then

H(f)<=max(C_0,C_1,...,C_r) I(f).

This constant has no read-count, overlap, bias, or arity loss. This is a conditional transfer theorem; an unconditional instance uses the explicitly proved two-bit gates below. All products on residual disjoint blocks are handled only after the exact Boolean cancellation is established.

## Explicit unbounded-overlap class, constant 2

Every Boolean gate on at most two bits satisfies H<=2 I. Proof: constants have (H,I)=(0,0); signed one-bit characters have (0,1); signed two-bit characters have (0,2); all remaining gates have three equal outputs and one exceptional output (or their complements), four Fourier probabilities 1/4, and (H,I)=(2,1). The truth-table classification exhausts 16 gates. Products of such gates on disjoint blocks satisfy H<=2 I by exact spectrum tensor additivity. Let F be any such disjoint product, and let each b_j be any such disjoint product on its own z_j. The anchored composition above then satisfies H(f)<=2I(f) for arbitrary incidence matrix A and arbitrarily large dimensions. This conclusion depends on no external unreviewed theorem.

For a genuinely nonlinear unbounded-read witness, let P(s,t) equal -1 only at s=t=-1. For k>=1 take F_k=product_{l=1}^k P(y_{2l-1},y_{2l}), let b be another copy of P on two shared physical bits, and set g_i=x_i b for all 2k private bits. All 2k children reuse the same nonlinear block. Every outer Fourier label has probability 4^{-k}; U(T)=|T| mod 2; d=1/2. Therefore

H(q)=1, B=2k-1, H(f_k)=2k+1, I(f_k)=k+1/2.

Thus H(f_k)=2I(f_k), while omitting the posterior misses 2k-1 bits and naively paying each shared occurrence would replace d=1/2 by sum_i Inf_i(F_k)=k. The collision fibers each have 2^{2k-1} equiprobable labels. These identities hold for every k, not just the finite validation range.

At the cancellation extreme, take F=product_{i=1}^{2k}y_i with the same g_i=x_i b. Then f=product_i x_i: d=0, H(f)=0, I(f)=2k, although the naive occurrence charge is 2k I(b). This prohibits identifying the d_j budget with the sum of child occurrences.

## Scope and exact universal gap

Private anchors are essential to this proof. Removing all x_i and trying to merge outer labels inside an incidence fiber gives coherent sums, not q_u; the resulting g vector need not be uniform and the coefficient law above is no longer valid. Even without that removal, permitting arbitrary outer F includes r=0, f=F. Permitting arbitrary shared b includes m=r=1, F(y)=y, f=x_1 b, with H(f)=H(b) and I(f)=1+I(b). Hence the transfer theorem alone does not prove full FEI or erase arbitrary terminal entropy. No selector-only increment estimate is asserted, so the bent-splice selector obstruction is not invoked as a premise or contradicted.

The shortest continuation is to replace one private anchor by an actual physical shared input and derive the resulting signed fiber coefficient and posterior/normalization correction. The very first missing line for such a generalization is a bound on entropy after that coherent fiber sum by a nonreused influence budget. The current proof is complete at its structural hypotheses; the generalized line is OPEN.
