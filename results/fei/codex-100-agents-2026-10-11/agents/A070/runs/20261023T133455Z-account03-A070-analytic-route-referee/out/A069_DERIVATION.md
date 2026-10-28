# Inherited core invoices: exact order comparison and source boundary

## 1. Definitions and the nonnegative decrement

All entropies and cross entropies use base two. Let a,b be Boolean functions on a finite uniform cube Y. Put P=(P_a+P_b)/2, J=(I(a)+I(b))/2. Supply a strictly positive probability reference R on ALL subsets of Y. At every physical restriction use only the marginal of this ORIGINAL R: deleting a coordinate adds its two reference cells. Do not reset R to a new spectrum. Define B=CE(P,R). A complete physical core tree queries every coordinate on every path, including coordinates on which both current functions are constant. Adaptive coordinate selection and outcome dependence are allowed.

At a current node and queried i, write P_0(T)=P(T), P_1(T)=P(T+i), R_0(T)=R(T), R_1(T)=R(T+i). The mean of the two child spectra is the erasure P_0+P_1: this follows by squaring the actual restricted Fourier coefficients a_hat(T)+/-a_hat(T+i), and likewise for b. BOTH child references equal R'=R_0+R_1. Consequently

    D_i = B - (B_+ + B_-)/2
        = sum_T sum_e P_e(T) log2[(R_0(T)+R_1(T))/R_e(T)] >= 0.

No actual joint spectrum factors in this argument. It is a likelihood-ratio identity for a supplied inherited reference. Physical influence j_i is the mean of the two current i-influences. Fourier counting also gives

    J = j_i + (J_+ + J_-)/2.

For a complete tree let w_v=2^(-depth(v)), and let

    V_T = sum_v w_v (D_v-4j_v)_+,
    A_T = sum_v w_v min(D_v,4j_v).

At complete leaves B=0 and J=0: the sole surviving reference atom has mass 1, regardless of the two constant signs. Thus exact telescoping, with every physical child retained, gives

    sum_v w_v D_v = B_root,
    sum_v w_v j_v = J_root,
    V_T = B_root - A_T,
    0 <= A_T <= 4J_root,
    max(0,B_root-4J_root) <= V_T <= B_root.       (1)

These are expected-tree accounts, not a pathwise bank. Negative excesses are not deposited as fresh credit; A_T is an algebraic accounting identity.

## 2. Order comparison, including independent random seeds

For ANY two complete adaptive physical core trees T,U using this same original pair and reference,

    |V_T-V_U| <= 4J_root.                       (2)

The same interval holds for randomized trees chosen by an independent physical seed. Fixing that seed produces a deterministic complete core tree. Average (1) over the seed; its original law, rather than a favorable reweighted law, must be used. The previous stage's exact core-invoice conservation identifies these V invoices with actual paired-control invoices while its product-reference and stopping hypotheses hold. A control/private history may randomize the core order; it cannot turn a fixed-order invoice into an unchanged same-bank invoice. It only permits (2), with the additional 4J explicitly unpaid unless an original owner funds it.

This extension needs the previous stage's core-invoice identity at every allowed control history. If a different reference is installed, a control is queried outside that scope, coordinates are omitted at constant outputs, or a paid owner is reset, (2) is not a substitute for a new complete account.

## 3. Exact Boolean counterexample to unchanged order reuse; sharp constant

Take a=b=chi_x on TWO physical core bits x,z; z is irrelevant to the actual Boolean function, but it remains in the complete reference account. For any integer k>=1 put epsilon=2^-k and set

    R(empty)=epsilon/16, R({x})=1/16,
    R({z})=(15-2epsilon)/16, R({x,z})=epsilon/16.

All four masses are positive and sum to 1. B_root=4 and J_root=1. Put ell=log2(1+epsilon), so 0<ell<1.

Order x THEN z: first D=ell,j=1, and after either literal outcome the now-constant physical function still incurs the FULL inherited terminal continuation D=4-ell,j=0. Hence V_xz=4-ell.

Order z THEN x: first D=ell,j=0, and after either z outcome the literal query has D=4-ell,j=1. Hence V_zx=ell.

The difference is 4-2ell -> 4 = 4J as k tends to infinity. Thus the universal coefficient 4 in (2) is sharp EVEN FOR ONE DICTATOR WITH AN IRRELEVANT PHYSICAL COORDINATE. For k>=2, ell<=log2(5/4)<1/2, so the same original 5/8 allowance pays order zx and fails order xz, whose positive invoice exceeds 7/2. This does not contradict FEI, and does not refute the earlier fixed-relative-order nine-bit theorem. It refutes only an extension that reuses an unchanged fixed-order positive invoice after arbitrary reordering. Dropping the constant-node z query would erase the actual reference cost and is inadmissible here.

The all-k limit needs no numerical search: log2(1+epsilon)<=epsilon/ln2 and ln2>1/2 imply ell<2^(1-k). Also log2(5/4)<1/2 follows exactly from (5/4)^2<2.

## 4. Exact Bellman formulation; no free universal source

For fixed a,b,R define V_min,V_max over ALL complete adaptive core trees. They obey the finite recursions

    V_min(state)= min_i [(D_i-4j_i)_+ + (V_min(child+)+V_min(child-))/2],
    V_max(state)= max_i [(D_i-4j_i)_+ + (V_max(child+)+V_max(child-))/2],

with value 0 only after the entire core is exposed. Child choices are independent after the actual outcome. Thus an admissible source potential W satisfying W>=0 and W(state)>=(D_i-4j_i)_++avg W(children) for one permitted i at each state certifies a selected complete tree. A bound for every i certifies every order. This is an exact optimization interface, not a proof that W<=KJ exists.

In fact the arbitrary-source version is FEI-hard. On the diagonal a=b=f, (1) implies that ANY complete tree with V_T<=K I(f), using any inherited full reference, gives

    H(f) <= CE(P_f,R) = V_T + A_T <= (K+4) I(f).    (3)

The first inequality is Gibbs' inequality. Thus a universal bound for a supplied/arbitrarily chosen original source and selected complete invoice proves full FEI, up to 4. The new order comparison removes order as an additional dimension-dependent obstacle; it does not close the universal source problem.

Strict-positivity guard: if both cores are constant and there is at least one core coordinate, J=0 but every strictly positive full reference has B=-log2 R(empty)>0. Equation (1) then forces V=B on EVERY complete tree. Thus a multiplicative universal bound including constants is FALSE under mandatory strictly positive full references and full exposure. This is a reference/accounting obstruction, not an FEI counterexample.

The exact remedy for the abstract source interface is to permit nonnegative references R that dominate the actual root mixture P: P(S)>0 implies R(S)>0. Every identity above still holds with zero-mass terms omitted. This support condition survives EVERY physical restriction: if a child mixture is positive at T, its mean over both outcomes is P(T)+P(T+i)>0, hence the common inherited reference R(T)+R(T+i)>0. No child spectral support is assumed equal to its parent's. All full terminal costs remain. The strictly positive control wrapper is separate; extending a source hypothesis there requires this same finite-CE convention, not a free reset.

Conversely, conditional on FEI(C), choose the ORIGINAL support-dominating source R=P. For pairs, H((P_a+P_b)/2)<=mean H(P_a,P_b)+2J: Jensen-Shannon divergence is at most total variation, at most max(P_a(nonempty),P_b(nonempty)), at most I(a)+I(b)=2J. Thus B<= (C+2)J and EVERY complete adaptive tree has V<= (C+2)J. Constants have R=delta_empty and B=V=0. On the diagonal a=b=f the sharper conditional bound is V<=C I(f). Conversely ANY all-function source/selected-tree bound V<=K I(f) implies FEI(K+4) by (3). This is a quantified equivalence up to the displayed constants, NOT a solution of its still-unproved universal side. Strictly positive sources instead give arbitrarily small additive delta by mixing with a positive uniform law; this does not remove the constant-function obstruction to an exact multiplicative statement.

For completeness JS<=TV follows by decomposing the two laws into their common mass and disjoint remainders: a common Bernoulli flag of probability TV reveals at most one bit when the remainder is used, and reveals nothing otherwise. The TV bound using the vacuum is immediate by matching their common mass at the empty set. Finally P_f(nonempty)=Var(f)<=I(f). None of these statements needs a percolation estimate.

## 5. First unsupported line and shortest next step

The unsupported universal step is an ORIGINAL influence-priced reference/source admission for arbitrary indecomposable Boolean cores, or an independently proved Bellman supersolution that bounds the same complete positive invoice while keeping every old debit. Equations (1)-(3) identify its strength and prevent claiming an equivalent restatement as a solution. The useful new closure is sharp dimension-free order overhead, plus a two-bit actual Boolean falsifier of unchanged owner reuse. The next substantive mechanism must exploit Boolean coefficient relations to build the original source; another ordering, private-width sweep, or mandatory optional reset cannot pay this initial bill.
