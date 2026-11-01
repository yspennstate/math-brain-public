# Compressed actual restriction certificate

Fix a Boolean core g on m variables, encoded by its full sign truth table, and s independent point controls. The actual function is F_s=1+A_s(g-1), A_s=1_{z=0}. Let N=2^m, L=N 2^s, and w_T be the integer Walsh transform of g (so ghat(T)=w_T/N). The actual normalized Fourier coefficients are

* w_T/L, for T nonempty and every control set U (multiplicity 2^s);
* (w_empty-N)/L, for T empty and U nonempty (multiplicity 2^s-1);
* (L+w_empty-N)/L at the all-empty index.

The first family permits zero w_T; all zero terms contribute zero. The squared masses sum to one by Parseval, checked in the executable before every spectrum use. Aggregating absolute integer coefficient numerators v by their multiplicities n_v gives

    H(F_s)=2(m+s) - (2/L^2) sum_v n_v v^2 log2(v).

This includes the coherent constant coefficient with its actual sign before squaring. It is not entropy of an incoherent branch mixture. At s=0 it reduces to the actual core spectrum.

If e_i is the integer number of disagreeing core edges in coordinate i, counting each edge once, then

    Inf_i(F_s)=2e_i/L,
    Inf_control(F_s)=(N-w_empty)/L.

These follow directly from the actual pivotal conditions. Every live control is interchangeable, and a control query has actual children +1 and F_{s-1}, each with probability 1/2. A core query has actual children 1+A_s(g_{i=0}-1) and 1+A_s(g_{i=1}-1). Thus every core/control interleaving stays in this state space; no projected real vector is used as a Boolean child. The identity I=d+average I(children) is checked exactly at every queried state. The state retains the remaining physical labels; least-original-label tie breaking is preserved despite exchangeable controls.

At each state the prescribed rule chooses among every relevant core coordinate and one representative of the exchangeable controls. min/max influence use exact rational influences. Greedy D/d compares outward rational intervals; overlapping intervals are accepted as ties ONLY when their exact rational prime-log expressions are identical. Equality of coefficient vectors is a sufficient identity, without assuming linear independence of logarithms. If overlapping intervals have unequal symbolic expressions the run fails rather than guesses a choice. This happened zero times in the completed run.

For each selected actual coordinate, compute D=H(F_s)-average H(actual children). Constant leaves have Q=0. Backward induction of

    Q=max(0,D-Cd+average Q(children))

is exactly the least nonnegative reserve for this fixed physical policy. The initial Q is distinct from the whole-path sum H-CI. A zero interval [0,0] rigorously certifies zero reserve for the entire prescribed continuation; a strictly positive lower endpoint certifies failure of the corresponding zero-reserve rule at that price. It does not refute a linearly funded reserve from the root influence.

# Rigorous numerical kernel

For integer v>=1 normalize v=2^j x with 1<=x<2. With z=(x-1)/(x+1), 0<=z<=1/3,

    ln(x)=2 sum_{h=0}^{27} z^(2h+1)/(2h+1)+R,
    0<=R<=2 z^57/[57(1-z^2)].

The same series encloses ln(2) by positive rational endpoints. Division by a positive denominator uses lower/upper reversal correctly. Add j to obtain log2(v), then round lower down and upper up to multiples of 2^-70. Entropy sums multiply by nonnegative exact integer weights; subtraction reverses interval endpoints. Averaging uses downward/upward integer rounding. Cd is exact rational and is separately rounded outwards. Addition, subtraction, averaging and positive part preserve enclosure. Thus every final pair of scaled integers in out/VALIDATION.json encloses the real Q, regardless of the displayed decimal summaries.

Rows contain the exact influences, root chosen physical coordinate, every visited nonconstant state's hash and physical labels, its entropy/decrement/reserve intervals, and the frozen constructor and command needed to regenerate its truth table. The raw replay uses a direct polynomial Boolean constructor and full physical truth tables, without the activation quotient. It shares the logarithm kernel and author, so this is representation-based self-validation, not external acceptance.

# Exact finite conclusions

Frozen primary domain: B05 k=2,4,6 with r=2k; AND of splice cores for (k,l)=(2,2),(2,4),(4,4), shared or independent selectors, r=0,2; five rules; C=4,32609/5000,8. There are 75 actual rule trees and 225 reserve values. At C=32609/5000, greedy-min-D-over-d and control-first have Q_root=0 for ALL fifteen functions. At C=4, greedy has Q_root=0 on all twelve AND functions, but positive reserve on all three B05 functions. The exact full output determines all other cases.

For B05 k=6, ordinary root influence is 883/262144, and Q_root/I at C=32609/5000 is in [0.0043362252,0.0043362253] for min-influence and selector-first, versus exactly zero for max-influence, greedy and control-first. Selector-first has Q_root/I in [0.0026621595,0.0026621596] even at C=8. The bad rule remains bad at a higher price than the successful rule needs. No all-k extrapolation of the finite zeros is made.

For the independent-selector AND(4,4), r=0, selector-first and min-influence have Q_root/I in [0.0493443360,0.0493443361] at C=32609/5000 and [0.0093929846,0.0093929847] at C=8, while greedy/control-first need zero at C=4. With one shared selector, the C=32609/5000 selector-first reserve remains positive, in [0.0271262190,0.0271262191], while it vanishes at C=8. This is actual physical reuse of one selector, not multiplication of independent selector budgets.

# Retained baseline and honest universal gap

The prior stage's RESERVE_AND_PREFIX_THEOREM.md and exact addressing prefix certificates are retained without a new claim of novelty: data-first addressing has exclusive queried influence 1 and unpaid stopped prefix at least a-C; rare activation and coded plateaux retain the full terminal influence. These prevent interpreting a cheap local query or a plateau as a paid terminal certificate. Prior directories missing protocol files are preserved as legacy inputs; this stage supplies source-bound adoption evidence rather than fabricating previous completed stages.

The finite comparisons remove B05 k=6 and these AND/shared-selector fixtures as falsifiers of the proposed greedy rule at C=32609/5000. They do not establish that greedy succeeds on every Boolean function, nor that its reserve is O(I) in all dimensions. First unsupported line: a dimension-independent owned bound on inherited child reserves at a non-point, overlapping controller query during unfinished core exposure. A062's arbitrary-core preservation result and A064's independent-point-priority payment leave exactly that terminal/core ownership obligation visible. The next search must test that update with actual child continuations, not repeat larger independent bent cores.
