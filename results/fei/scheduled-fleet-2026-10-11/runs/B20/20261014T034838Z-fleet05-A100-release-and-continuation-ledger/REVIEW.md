# Binary remainder, loss ownership, and release scope

All information quantities here use bits. The row reference is the complete probability law r_i(T)=p_T+p_(T+i); it is marginalized into quotient cells, not conditioned on derivative support. This stage supplies no finite universal FEI constant.

## Independent review: A073-NONZERO-ERASURE-BINARY-REMAINDER v1

Let d>=2 be even, delta=2^-d, t=2^(-d/2). Tensoring the two-bit quadratic sign shows directly that b has Fourier coefficients sigma_T t. Their sum is b(0)=1, so their sign counts are N_+=(2^d+2^(d/2))/2 and N_-=(2^d-2^(d/2))/2. The two-bit gate q, negative only at (1,1), has coefficients (1,1,1,-1)/2. In F=b+1_zero(q-1), the four amplitudes for each core T are sigma_T t-delta/2, delta/2, delta/2, -delta/2. None vanishes. Thus both physical u,v rows have strictly positive actual erasure, not the zero-erasure parity-duplication mechanism.

Each row has e=delta/2. For a u query, residual partner occupancy v yields mu(T,0)=mu(T,1)=delta/2; r(T,0)=delta(1-sigma_T t+delta/2), r(T,1)=delta^2/2. Orthogonality/Parseval and the sign counts give complete reference cell masses (1-e,e), and derivative cell masses (1/2,1/2). Conditional on v=1 both core laws are uniform. Conditional on v=0 the derivative core is uniform and reference core weights are delta(1-sigma_T t+delta/2)/(1-delta/2). The KL chain rule therefore gives

D_full=D_binary+D0/2,
D0=sum_sigma N_sigma delta log2[(1-delta/2)/(1-sigma t+delta/2)],
L_u=e D0/2.

The same holds for v. Both sign counts are positive and the reference conditional distribution differs from the uniform derivative distribution, so strict Gibbs inequality gives D0>0. No independence of the reference partner and core is presumed.

The identity (2-3t)(1-2t)>=0 for 0<t<=1/2 proves every positive likelihood ratio <=7/5. Thus D0<=log2(7/5). The original rational margin follows exactly from 7^128<2^63 5^128, hence L/e<1/4-1/256. The sum of the two weighted remainders is delta D0/2<delta/4, and delta/4<=(1+delta)/20=Inf_(y1)/10, since delta<=1/4. This reserves that fraction solely for the remainder; it cannot also pay the surviving row cost.

Complete M/e=1+(1/2)log2((1-e)/e)-D0/2>d/2+3/4, because (1-e)/e=2^(d+1)-1>=2^d. Physical edge counting gives every core influence (1+delta)/2, so I=d/2+(d/2+1)delta. Entropy <=d+2 bits gives H/I<=2+4/d<=4. This independently reconstructs the full original source lemma without repairing its statement. Its already saved A098 review is full scope; this stage adds a separate A100 reconstruction. No universal quotient or available core reserve is established by this family.

## New quantitative refinement: a Jensen bound for the same conditional remainder

The exact source law gives weights w_sigma=N_sigma delta=(1+sigma t)/2. Concavity of log, retaining these actual unequal weights, yields

D0<=log2[(1-delta/2) sum_sigma w_sigma/(1-sigma t+delta/2)]
   =log2 R(delta),
R(delta)=(1+delta-3delta^2/4)/(1+delta^2/4).

For 0<delta<=1/4, R>1 and its derivative has numerator 1-2delta-delta^2/4>0. Hence R(delta)<=R(1/4)=77/65. The exact integer inequality 77^4<2*65^4 proves log2(77/65)/2<1/8. Moreover R(delta)<1+delta, and ln(1+delta)<delta, so

0<L_i/e_i<=log2 R(delta)/2<=log2(77/65)/2<1/8,
L_u+L_v<=delta log2 R(delta)/2<delta^2/(2 ln2),
L_u+L_v<delta/8<=Inf_(y1)/20.

This halves the original explicit uniform allowance and gives a quadratic-in-delta total remainder bound. It is a stronger scoped consequence, not a repair to the source lemma and not independent acceptance of an A100 theorem. The separate new claim requires external review. The reference normalizer and retained core row stay unchanged. A common independent spectator law multiplies both conditional laws and cancels exactly in their likelihood ratios; deleting it is legitimate, whereas absolute-degree merging may delete the required core likelihood ratio.

## Scope of new failed-route evidence

A001's fixed-low-degree/single-tail obstruction uses the full-support actual Boolean tensor of point defects. Its lost refund is exactly the within-tail conditional KL. A090's degree-only tribes obstruction, independently reviewed by A081/A031, is a distinct partition and distinct witness. These rule out their declared coarse quotients, not the complete reference or FEI. A096's partner-deletion witness loses between d-1 and d times local pair influence, while the opposite partner-retaining quotient is lossless. Its later positive-erasure extension above has a nonzero but small conditional remainder. Alphabet size alone bounds none of these losses.

A008's auxiliary t_u=1/2 substitution is corrected by its author erratum; with both endpoint orders the complete singleton draw is 1/4. The formal operator theorem always retained t_u and has A006/A007 unchanged-formal-statement reviews. Do not withdraw that theorem because a numerical/source example used the wrong factor, and do not accept unrecomputed evaluations using the old factor. A009's and A006's graph references already use 1/4.

A097's padded zero-point bank at 17/8 now has A094 full stated-scope acceptance. A094's all-vertex extension has a different optimal price because flips can destroy originally pivotal edges; it remains an author-proved new claim in this intake. The unpadded price-two certificate, padded zero-point certificate, and prospective arbitrary-location certificate must retain separate hypotheses. None closes arbitrary non-bent edits or a terminal reserve under repeated overlapping histories. A099 v4 assembles these fragments and the binary remainder but still lists both integrated audits pending.

The first unsupported universal line remains the signed-Boolean terminal-row lower bound sum_i e_i D(mu_i||r_i)>=sum_i e_i log2(1/e_i)-K I for one finite K. On a quotient route it requires an actual conditional partition and a nonoverlapping available terminal reserve paying all lost conditional KL plus the retained original row. The present quadratic remainder estimate pays only two specific losses and cannot allocate the same core fraction to every descendant or row.
