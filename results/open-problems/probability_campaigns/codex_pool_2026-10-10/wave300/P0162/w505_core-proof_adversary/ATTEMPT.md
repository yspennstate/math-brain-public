# P0162 independent adversary derivation

Checkpoint 2026-10-10. Native worker w505. This section was saved before reading w504's ATTEMPT.md, CLAIMS.jsonl, or proof. w506 has now independently checked C001-C005 (INDEPENDENT_REVIEW_UPDATE.json). The C006 induction is checked only conditionally: its universal coordinate-selection premise remains unproved. Response-side served model identities are UNKNOWN. The complete FEI conjecture is not proved here. No novelty claim is made.

Use the uniform cube, Boolean functions with values in {-1,+1}, normalized Walsh coefficients, base-2 logarithms, and phi(t)=t log_2(1/t), phi(0)=0. The full target is a universal finite C such that H(f)=sum_S phi(fhat(S)^2) <= C I(f), where I(f)=sum_S |S| fhat(S)^2, for every dimension and every such Boolean f. Primary source: O'Donnell, Wright, Zhou, https://www.cs.cmu.edu/~odonnell/papers/fei.pdf; also the precise introductory statement in https://arxiv.org/html/2606.00246v1. Current global openness remains UNKNOWN pending the local solved/retired check.

## The strongest tempting induction input

For coordinate i write f(z,y)=g(z)+y h(z), with g=(f_++f_-)/2, h=(f_+-f_-)/2, and define

Delta_i(f)=H(f)-(H(f_+)+H(f_-))/2.

The exact influence identity is I(f)=I_i(f)+(I(f_+)+I(f_-))/2, with I_i(f)=||h||_2^2. A bound Delta_i(f)<=C I_i(f) would propagate FEI with the same C by induction. The quantifier over i is crucial: an all-coordinate bound is FALSE, as proved below. A uniform bound for at least one suitable coordinate in every nonconstant function would suffice, but is still an unproved input here.

## Exact local entropy identity

Put a=ghat(T), b=hhat(T), r=a^2+b^2, w=b^2/r for each T with r>0, and t=2ab/r. Then |t|<=1, and direct expansion gives

phi(a^2)+phi(b^2)-(phi((a+b)^2)+phi((a-b)^2))/2
 = r [h_2(w)+J(t)],

where h_2 is binary entropy and J(t)=((1+t)log_2(1+t)+(1-t)log_2(1-t))/2 = 1-h_2((1+t)/2) >= 0. A term with r=0 contributes zero. Summing gives Delta_i(f)>=0. More usefully each term is at least b^2 log_2(r/b^2), with that lower bound interpreted as zero when b=0. All identities are finite; no limit exchange, independence assumption, or conditional product is used.

## Explicit Boolean obstruction to all-coordinate induction

Fix m>=1. On x=(u,v) in F_2^m x F_2^m let B(u,v)=(-1)^(u dot v), N=2^(2m), A=2^m, and d(x)=1{x=0}. Add a selector y in {-1,+1} and set

F_m(x,y)=B(x)-(1-y)d(x).

This is Boolean: away from 0 it equals B, while at 0 it equals y. Its restrictions are F_+=B and F_-=B-2d. The normalized Walsh coefficients are

Bhat(alpha,beta)=N^(-1/2)(-1)^(alpha dot beta),
dhat(alpha,beta)=1/N.

The first identity follows by summing over v first: only u=beta survives; it is an exact finite character calculation. Thus a=Bhat-1/N and b=1/N. Every T satisfies

r/b^2=(sigma_T A-1)^2+1 >= (A-1)^2+1.

Also I_y(F_m)=sum_T b^2=1/N. The local entropy identity therefore proves

Delta_y(F_m)/I_y(F_m) >= log_2((2^m-1)^2+1),

which tends to infinity with m. Consequently there is NO universal C such that Delta_i(f)<=C I_i(f) for ALL Boolean f and ALL coordinates i. This is an obstruction to that particular sufficient lemma, not a counterexample to FEI.

For exact scalar verification, the numbers of positive and negative Walsh coefficients of B are k_+=(N+A)/2 and k_-=(N-A)/2. Hence

H(F_m)=k_+ phi((A-1)^2/N^2)+k_- phi((A+1)^2/N^2)+N phi(1/N^2),
H(F_+)=log_2 N,
H(F_-)=k_+ phi((A-2)^2/N^2)+k_- phi((A+2)^2/N^2).

The total influence is I(F_m)=m+(2m+1)/N: each base coordinate has influence 1/2 in B, and flipping 0 changes its influence by +2/N in B-2d because B(0)=B(e_j)=1. Averaging restrictions gives 1/2+1/N for each of the 2m base coordinates, plus 1/N for y. The complete H/I ratio therefore does not grow like the defective Delta_y/I_y ratio.

In fact this entire family satisfies H(F_m)<=2 I(F_m), by an elementary bound, so the coordinate obstruction persists inside a class where FEI has a fixed constant. Let rho=1/N and n=2m. The selector-containing Fourier coefficients have total mass rho, and each of the two selector categories has at most N possible subsets. The Shannon chain rule thus gives H(F_m)<=log_2(N)+h_2(rho). Since -(1-rho)ln(1-rho)<=rho, h_2(rho)<=rho(n+log_2 e)<=2(n+1)rho for n>=2. Combining with 2 I(F_m)=n+2(n+1)rho proves the stated bound. Independent review remains pending.

## A general upper bound locating the missing logarithm

The exact local identity gives a rigorous but insufficient upper bound Delta_i(f)<=h_2(q)+4q(1-q), where q=I_i(f). Indeed sum_T r_T=1 and sum_T r_T w_T=q. Concavity gives sum_T r_T h_2(w_T)<=h_2(q). For |t|<=1, J(t)<=t^2: its even power series has positive coefficients J(t)=(1/ln2) sum_{k>=1} t^(2k)/(2k(2k-1)); the coefficient sum is J(1)=1, so every t^(2k)<=t^2. Continuity treats t=+/-1. Therefore sum_T r_T J(t_T)<=4 sum_T r_T w_T(1-w_T)<=4q(1-q), again by concavity. The endpoints q=0,1 both give Delta_i=0. A coordinate with q bounded below by a positive constant has a bounded Delta_i/q, but the hard regime q tending to zero retains h_2(q)/q. This bound is not claimed as new: the recalled F4 work already records a sharper high-influence estimate and a small-influence reduction.

## Measurements saved

Command: python -X utf8 ~/brain_workers/w505/verify_obstruction.py --gate cpu20s-n9.
The run completed in 0.522914s. Four exact truth-table families (m=1,2,3,4) passed Booleanity, normalization, the flat Walsh coefficients, sign counts, all-coordinate entropy-increment identities, and exact influence identities; direct character sums independently matched the transform for m<=3. All 276 Boolean functions of dimensions 1 through 3 passed the local identities. Closed-form scalar values for m=1..8 satisfy the proved lower bound. The selector ratio grows from 4.8676687468 at m=1 to 20.3280154117 at m=8. Exhaustive small-dimensional good-coordinate ratios are finite evidence only; the largest observed minimum ratio is 4.8676687468 and gives no all-dimensional upper bound.

## Owner prior-work boundary

The required guarded brain recall returned three FEI hits, read as primary memory pointers: fei_holds_for_linear_threshold_functions_rank_argument_2026_09_23; fei_opus_wave1_reduction_small_influences_gates_and_ltf_2026_09_23; fei_plateaued_constant_four_is_potapovs_theorem_not_ours_2026_09_30. The F4 summary already refutes universal per-coordinate erasure bounds (using a monotone majority perturbation), the maximal-influence selector, and the assertion that small influences make every coordinate good. Our bent-plus-point-flip derivation is a separate concrete witness and regression control, not a new resolution or a claim of the first known obstruction. The same summary gives stronger restriction constant lower bounds on record towers and reduces FEI to small-influence functions. The LTF memory explicitly states its result does nothing for full FEI. The public Potapov primary source treats plateaued functions, not every Boolean function. The percolation-crossing F0090 packet is another restricted class; we do not infer a full P0162 solution or audit its previously reviewed proof here.

## Hardest missing input and next proof step

The viable local candidate is: there exists a universal C such that every nonconstant Boolean f has a coordinate i of positive influence with Delta_i(f)<=C I_i(f). Its exact local expression is sum_T r_T[h_2(w_T)+J(t_T)] <= C sum_T b_T^2 for a suitably chosen coordinate. The Boolean identities g h=0 and g^2+h^2=1 hold pointwise; they do not give a coefficientwise bound on w_T. Establishing a usable coordinate choice or a noncircular amortization is the single hardest missing input in this route. Since Delta_i<=2 follows from the exact identity, this sufficient input localizes to functions all of whose influences are below a fixed tau (take tau=1/16); coordinates of influence at least tau cost at most 2/tau. w504's actual core proof is now audited in AUDIT_W504.md, including its positive base-coordinate family calculation and a harmless coefficient-sign correction. NEXT: attempt the suitable-coordinate estimate for arbitrary Boolean functions with every influence below 1/16; do not infer it from this large-base-influence family.
