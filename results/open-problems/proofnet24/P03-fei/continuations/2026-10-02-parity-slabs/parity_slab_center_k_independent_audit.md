# Independent audit: spectral-center FEI for parallel slabs

2 October 2026. Verdict: **PASS for the final written theorem and its
stated finite-crossing and wide-gap union corollaries.** I found no
analytic gap. The independent audit treats the completed ordinary
parallel-slab theorem as its explicit upstream input and rereads that
proof and the disjoint-union proof in full. Research priority and external
peer review are not certified; unrestricted Boolean FEI is not proved.

Inputs read in full:

- `parity_modulated_slabs_center_candidate.md` and the stable final
  `parity_modulated_slabs_center_proof.md`;
- `stripe_extension_parallel_slabs_proof.md`;
- `stripe_extension_union_proof.md`;
- `verify_parity_slab_center_heat.py` and its complete result JSON;
- `parity_slab_local_minimum_obstruction.md`.

The checker was rerun with output redirected to
`parity_slab_center_k_rerun.json`. The full JSON matches the author's
expanded final result. The script hash and counts are saved in
`parity_slab_center_k_rerun_record.json`. No author proof, checker, or
original JSON was changed by this audit.

## 1. Exact entropy split and its universal bound

For f=A+x_iB, pointwise A^2+B^2=1 and B is zero or a sign. Consequently
P_S=Ahat(S)^2+Bhat(S)^2 is a probability law and sum P_S q_S=E B^2=I_i(f),
where q_S=Bhat(S)^2/P_S for positive P_S. The physical influence is
exactly E B^2, without an extra factor two.

For a coefficient pair (a,b), put P=a^2+b^2 and
r=(a+b)^2/(2P). The full entropy of that pair is
-P log_2(P)+P h_2(b^2/P). The average restricted coefficient entropy is
-P log_2(2P)+P h_2(r). Summing gives the final proof's exact formula

    Delta_i H = sum_S P_S[1+h_2(q_S)-h_2(r_S)].

This uses full entropy, including the empty Fourier set. Zero pairs are
omitted by continuity, so there is no zero-denominator problem.

The claimed binary entropy inequality is correct. In the series for
1-h_2((1+x)/2), all coefficients are positive and their sum is
(1/ln 2) sum_j[1/(2j-1)-1/(2j)]=1. For abs(x)<=1 each x^(2j)<=x^2,
which gives h_2(t)>=4t(1-t), including endpoints by continuity. The exact
identity r(1-r)=(1-2q)^2/4 therefore implies
1-h_2(r)<=4q(1-q)<=h_2(q). Hence

    Delta_i H <= 2 sum P_S h_2(q_S) <= 2h_2(I_i(f)),

the last step being concavity of h_2. Signs of a,b do not affect this
argument. In particular no unateness or threshold property is used here.

## 2. The edge-isoperimetric conversion is valid and fully proved

Let E be the minority output set, p=abs(E)/2^n<=1/2. Each coordinate-i
boundary edge has one minority endpoint, so there are at most abs(E)
such undirected edges. Its two directed endpoints give I_i(f)<=2p.
Likewise I(f)=2 abs(boundary E)/2^n, exactly the stated normalization.

The elementary induction for
abs(boundary E)>=abs(E) log_2(2^n/abs(E)) is correct. For section sizes
a0,a1, internal boundaries contribute their induction bounds and the
cross boundary is at least abs(a0-a1). With a=a0+a1 and
q=min(a0,a1)/a, this is

    a log_2(2^(n-1)/a)+a h_2(q)+a(1-2q).

Concavity gives h_2(q)>=2q on [0,1/2], so the expression is at least
a log_2(2^n/a). The empty section conventions and zero-dimensional base
are valid. It follows that I(f)>=2p log_2(1/p).

For 0<p<=1/4, monotonicity of h_2 up to one half gives
h_2(I_i)<=h_2(2p). The bound -(1-u)ln(1-u)<=u yields

    h_2(2p)<=2p[log_2(1/p)+log_2 e]
            <=4p log_2(1/p)<=2I(f),

since log_2(1/p)>=2>log_2 e. For 1/4<=p<=1/2, concavity of
2p log_2(1/p) and its value one at both endpoints imply I(f)>=1;
h_2(I_i)<=1 then suffices. Constants are dealt with separately. Thus
h_2(I_i)<=2I(f), and the universal split bound

    Delta_i H(f)<=4I(f)

is valid for every Boolean f. It charges total influence of the function
being split, not the pivot's individual or centered influence.

## 3. Gluing applies to the centered arbitrary function

For any fixed coordinate set U of size b, reveal those coordinates in a
fixed order. At depth t, the expected remaining total influence is exactly
the sum of the original influences of coordinates not yet revealed,
so it is at most I(f). This stronger identity follows by averaging the
physical edge probabilities over the fixed coordinates.

The entropy telescoping identity holds even if some local entropy
increments are negative. Applying the preceding upper bound to every
conditional function, then averaging, gives

    H(f)<=E H(f|U)+4b I(f).

If all terminal restrictions obey ordinary FEI with constant C, their
average entropy is at most C E I(f|U)<=C I(f). This proves
H(f)<=(C+4b)I(f). Intermediate restrictions need not belong to the class
supplying C. This is the crucial valid reason gluing can be applied to
the character-centered function, which is not generally an ordinary slab.

## 4. A slab has at most fifteen original high-influence coordinates

Input sign changes preserve influences and permit positive weights;
zero weights have zero influence and can be deleted. Each slab or its
complement is determined by at most two monotone endpoint halfspaces
h1,h2 in that common orientation. On any cube edge, a change of slab
label requires a change of at least one halfspace label. Therefore
I_i(g)<=I_i(h1)+I_i(h2), without claiming equality.

For a monotone sign-valued Boolean halfspace, conditioning on all other
inputs gives hat(h)({i})=I_i(h): a pivotal edge has derivative one and
nonpivotal edges have derivative zero. Parseval yields
sum_i I_i(h)^2<=Var(h)<=1. Consequently

    sum_i I_i(g)^2<=2sum_i[I_i(h1)^2+I_i(h2)^2]<=4.

If b coordinates have I_i(g)>1/2, then b/4<sum_i I_i(g)^2<=4,
so b<16 and b<=15. The strict comparison is essential; coordinates with
influence exactly one half are deliberately not selected. A halfspace or
constant only improves this estimate.

Endpoint conventions cause no gap. For a single interval, inclusive or
exclusive endpoint predicates are each monotone halfspace predicates.
A singleton attained-score interval also uses two such nested predicates.
Alternatively moving boundaries into finite attained-score gaps preserves
the function. No assumption that a slab is monotone or unate is made.

## 5. Centering and the arbitrary-character conclusion

Multiplication by a character shifts every Fourier set by symmetric
difference with its support, so full entropy is unchanged. It changes
physical influence I_i to 1-I_i exactly on those support coordinates.
Thus the minimum influence over the character orbit is

    J(g)=sum_i min(I_i(g),1-I_i(g)),

attained by U={i:I_i(g)>1/2}. Set h=chi_U g. Then I(h)=J(g), H(h)=H(g),
and abs(U)<=15. Once all coordinates in U are assigned, the character
becomes a constant output sign and the remaining g is an ordinary slab
restriction. Every terminal h restriction therefore obeys the upstream
ordinary slab theorem with C_slab, even if the base class were not stated
as output-sign closed, because H and I are output-sign invariant.

Applying the generic gluing estimate to h proves

    H(g)<=(C_slab+4abs(U))J(g)<=(C_slab+60)J(g).

For any other character T, I(chi_Tg)>=J(g), which gives ordinary FEI
with the same constant for every such modulation. J=0 requires no
division: I(h)=0 makes h constant on the connected cube, and H(h)=0.
The gluing argument itself covers this case as well.

## 6. Finite-crossing and wide-gap union corollaries

For a function with at most m genuine crossings and no extra isolated
point anomalies, each crossing can be represented by one monotone
threshold, with the tie convention chosen on the appropriate side.
The pivot union bound and Cauchy-Schwarz give

    sum_i I_i(g)^2<=m sum_r sum_i I_i(h_r)^2<=m^2.

Hence b<4m^2 and b<=4m^2-1 for m>=1. The spectral-center conclusion with
constant C_m+4(4m^2-1) is conditional on ordinary FEI for a
restriction-closed class with that C_m. The final proof correctly does
not supply this ordinary input for arbitrary nearby crossings. The
strictly separated class has the required existing input and retains
strict separation under restriction.

For at most r disjoint parallel intervals/rays whose separating gaps
are strictly wider than twice the largest input weight, no cube edge
joins distinct components. The audited union lemma gives ordinary FEI
with C_union=r C_slab+log_2(e)(1+1/e). Restriction translates all intervals
by the same fixed score shift and reduces the largest remaining weight,
so that strict wide-gap condition persists. Disappearing components only
reduce the number required.

There are at most 2r endpoint predicates, even for singleton components;
thus sum I_i(g)^2<=4r^2 and b<=16r^2-1. The constant
C_union+4(16r^2-1) follows exactly. Degenerate singleton components can
also be replaced by small intervals in attained-score gaps while retaining
the strict separating-gap margin. Complementing the output covers the
positive-set version. Constants are handled separately. No positive
lower bound on component width is needed, and no non-strict separation
claim has been introduced.

## 7. Upstream dependencies and preserved failed methods

The ordinary parallel-slab proof has been reread completely, including
the narrow-interval disjoint-support case, signed derivative
hypercontractivity, empty mass Q0<=alpha, resampling-mask independence,
common-scale conversion, and dyadic KL calculation. The earlier completed
independent slab audit remains its upstream analytic record. The
disjoint-union entropy proof and its exact boundary-additivity hypothesis
have also been reread; no joining edge is silently discarded.

The preserved two-bit middle-layer slab has I-Var=1 and J=0, so no
finite comparison I-Var<=constant*J can prove the new theorem on the
whole class. Its entropy is zero, so it is consistent with the theorem.

The separate local-minimum obstruction is correct. For odd N, the stated
two-endpoint slab has branches -M and M+2D; only the all-minus input
has equal branches, giving pivot influence 1-2^(-N). Multiplication by
the pivot character makes the old branches M and M+2D, preserving full
entropy and the average restricted entropy. The central-layer majority
coefficient formula, Vandermonde/log-concavity lower bound, and exact
even-degree contribution 2epsilon check out. Odd degrees give

    Delta/min(I_i,1-I_i)
       >=(N+3)/2-log_2[N(N+1)/2] -> infinity.

Thus a local largest-weight bound by the pivot's centered influence is
false even for slabs. The positive proof never invokes it: it uses total
influence of the centered conditional function and only a bounded number
of peeled coordinates. Both method failures remain separate artifacts.

## 8. Checker assessment and reproducibility

The expanded checker passed 65,814 Boolean functions and 262,948 pivots
through four variables, 3,951 slab instances through ten variables, and
61,396 character checks, including every character on the slab instances
through six variables. The entire rerun JSON equals the original.

Influence counts, exact character flip identities, Walsh coefficient
permutations, and Chow-square bounds use integer truth tables. The
maximum tested transform size is 2^20, so the int64 Walsh numerators stay
well within range. Entropies and the entropy inequalities use floating
logs with stated tolerances; those are finite consistency checks, not
exact entropy certificates or proofs of the dimension-independent result.
The analytic proof above is the justification for that theorem. Fraction
computations preserve the exact I-Var/J failures and local pivot
probabilities. No computation or anecdotal observation is substituted
for the written gluing, high-coordinate, or restriction arguments.

The audited result concerns ordinary parallel slabs and their arbitrary
characters, plus the explicitly conditional finite-crossing and proved
wide-gap subclasses. It does not cover arbitrary shared-input slab
circuits, all polynomial thresholds, all nearby finite crossings,
unrestricted FEI, or biased product measures.
