# Active-label schedule repair

All logarithms and entropies are in bits. The cube is uniform. A finite deterministic singleton stopping tree queries no coordinate twice along a path. It may stop before computing the output; all terminal entropy and influence remain in the accounts. Let A be a fixed coordinate set containing every coordinate the tree can query. Write Pi for its physical transcript, S for the coherent root Fourier-square sample, Q(Pi) for the final queried set, W=S\Q for the actual terminal Fourier sample in original ambient labels, and D=S intersect Q. Define

    a=I_A(f)=sum_{i in A} Inf_i(f),
    R=I(f)-E I(f_leaf).

The coherent lift is the actual function-specific lift: at a query i and current retained frequency T, the probability of child b is childhat_b(T\{i})^2 divided by twice the sum of the two parent Fourier-square masses in that fiber. Zero-mass fibers are never sampled. Its transcript marginal is physical; its current frequency conditional on a node is the actual restricted Fourier law. This construction follows directly from the fair restriction identity hat(f_b)(U)=hat(f)(U)+b hat(f)(U union {i}).

## 1. Exact active cost and one normalized reference

For a fixed root sample S, the maps D -> W=S\D and W -> D=S\W are inverse. Both are deterministic given (S,Pi). Consequently

    e:=I(W;Pi|S)=H(W|S)=H(D|S).

This identifies the smallest schedule information required for this particular retained witness; recording query labels outside S is unnecessary. The root-Markov condition W -> S -> Pi holds if and only if e=0. This is a necessary and sufficient zero-injection condition, not a claim that no weaker hypotheses can yield some positive constant bound.

Each removed label is counted once, so E|D| equals the sum over internal nodes of reach times the current spectral marginal of the queried coordinate. This marginal is its actual physical influence under the uniform law. The restriction identity for influence telescopes, giving

    E|D|=R, E|S intersect A|=a,
    0<=R<=a, a-R=E I_A(f_leaf).

For 0<theta<1 define ONE conditional reference, at the root, on all subsets d of S intersect A:

    rho_theta(d|S)=theta^{|d|}(1-theta)^{|S intersect A|-|d|}.

The binomial theorem proves normalization for every S. Cross-entropy and conditional KL give the exact identity

    H(D|S)=-R log theta-(a-R)log(1-theta)
              - E_S KL(P(D|S)||rho_theta(.|S)).

Choosing theta=R/a yields the sharp universal bound

    e <= a h2(R/a).

The right side is defined to be zero when a=0. At R=0 or R=a the actual deletion set is respectively empty or all of S intersect A almost surely, so e=0; use the corresponding point-mass reference. This reference is a schedule code on (S,D). It is not asserted to generate the physical transcript or to supply the separate conditional-history bank H(Pi|W).

## 2. Repair with an explicit scope

A useful structural sufficient condition for e=0 is:

    every terminal restricted function is independent of all coordinates in A.

Equivalently E I_A(f_leaf)=0, hence R=a. This permits variable final query sets: unqueried coordinates in A need only be irrelevant at that leaf. Then W=S\A almost surely is a fixed projection of the root sample. Fixed final query sets are one special case. Another is adaptive short-circuit evaluation of controllers followed by stopping at the chosen data function.

For a quantitative repair allowing unfinished controller dependence, assume E I_A(f_leaf)<=kappa R for a fixed kappa>=0. Since a<= (1+kappa)R and t h2(1/t) is increasing for t>=1 (derivative -log(1-1/t)),

    e <= (1+kappa)h2(1/(1+kappa)) R.

The exact weaker scalar condition is a h2(R/a)<=K R; for fixed positive R its level sets are exactly bounded a/R. A smaller active cost can also be certified by the KL rebate in section 1. Neither a bounded reservoir nor zero injection is universal: A048's family violates both uniformly.

## 3. Conversion and the retained ledger

Put Y=f(X), o=I(Y;Pi), j=I(S;Pi), j_W=I(W;Pi), and Gamma_W=H(Pi|Y)-H(Pi|W)=j_W-o. The chain rule gives j_W<=j+e. Physical independence gives o<=R. For completeness, the uniform channel bound is j<=2R/ln(2): in each child Fourier fiber let amplitudes G,H and q=(G^2+H^2)/2. Its natural-unit mixture information is q g(z), z=(G^2-H^2)/(G^2+H^2), with g(z)=((1+z)ln(1+z)+(1-z)ln(1-z))/2. The series coefficients of g are 1/[2k(2k-1)], whereas those of 1-sqrt(1-z^2) are binom(2k,k)/[4^k(2k-1)]. The latter dominate because binom(2k,k)/4^k>=1/(2k), proved by induction. Hence q g(z)<=(|G|-|H|)^2/2<=(G-H)^2/2. Parseval gives J_v<=2 Inf_i(f_v)/ln(2); the coherent information chain telescopes to the claimed bound. The output bound follows from I(X_i;Y|history)<=H(Y|X_-i,history)=Inf_i(f_v), again summing reach weights.

Thus the corrected conversion for the actual descendant is

    o/2+[Gamma_W]_+/2=max(o,j_W)/2
       <=R/ln(2)+e/2
       <=R/ln(2)+a h2(R/a)/2.

Under the bounded-reservoir hypothesis the coefficient is 1/ln(2)+(1+kappa)h2(1/(1+kappa))/2. Under terminal independence of A it is exactly the surviving root-compatible allowance R/ln(2), despite adaptive short-circuit schedules.

In particular any B<=o/2+H(Pi|Y)/2 obeys B<=H(Pi|W)/2+R/ln(2)+e/2. Our earlier output-conditional tax theorem supplies such a B. Its full spectral ledger remains

    Hhat(f)=E Hhat(f_leaf)+2 M_T+H(Pi|W)/2+j_W/2-Dbar_T,

where Dbar_T=sum_v reach_v [h2(1/2)/2-(J_v-M_v)]. This follows from the previous output-conditioned ledger by the exact substitution Gamma_W=j_W-o; it never deletes terminal Fourier entropy. The FIRST UNSUPPORTED universal line is paying H(Pi|W)/2 together with signed erasure and terminal Fourier entropy from one nonduplicated influence budget. The normalized deletion reference pays only the added schedule conversion, within its stated reservoir budget.

## 4. Intended applications admitted and excluded

Admitted with e=0: any controller-first finite tree that leaves every controller irrelevant, with arbitrary overlapping or identical data coordinates in the terminal core functions. This includes two shared-control priority arms s,a,b selecting g(y), h(y), or a constant, where g,h use the SAME data y. Early stopping when an arm wins is permitted; ignored remaining controller bits are irrelevant. Arbitrary Boolean cores, signs, controller widths and control overlap are allowed for this conversion assertion. It does not prove their separate controller entropy or final-core entropy payment. Fixed-coordinate prefixes, and prefixes supplemented by a fixed data block until all coordinates in the overall queried block are terminally irrelevant, are admitted too.

Admitted with a dimension-independent positive price: any tree retaining at most kappa R active-block influence at its frontier, regardless of data overlap. Excluded without further work: revealing only the common bit while leaving arbitrarily wide private controllers active; arbitrary controller/data interleaving that leaves significant dependence on coordinates in A; raw descendant reset on A048's indexed-parity tree. No biased-product-law extension is claimed: the equality E|D|=R here uses uniform Fourier marginals.

## 5. Boolean sharpness of the reference bound

Independently reconstruct A048's family as follows. Set h_k=1-2*1_{all k bits equal 1}, and F=(product of r disjoint h_k)*(parity on m=2^r fresh coordinates indexed by r-bit strings). Query one fixed coordinate in each defect, then the parity coordinate indexed by the r outcomes B, and stop after its outcome C. Every query is essential: each first defect influence is d=2^{1-k}, and every parity influence is one. Take A to consist of the r first defect coordinates and ALL m parity labels. For one defect query the children are constant and h_{k-1}. The latter has total nonempty Fourier mass v=4*2^{-(k-1)}(1-2^{-(k-1)}). A spectral draw in the inactive branch is empty; in the active branch it is empty with probability 1-v, and the conditional law among nonempty frequencies is the same before and after the branch decision. Thus the channel information reduces to the empty/nonempty indicator and is j_k=h2(v/2)-h2(v)/2. Independent tensor factors give I(S;B)=r j_k. The parity query changes signs only, so C is fair independently of (S,B) in this lift and H(B|S)=r-r j_k. The root parity spectrum is the deterministic set of all m parity labels. Consequently W omits exactly the label indexed by B, recovers B, and has no dependence on C. Conditional on S the variable part of D is therefore a one-to-one encoding of B. This proves e=H(D|S)=r(1-j_k) directly. Actual influence telescoping gives

    a=m+rd, R=1+rd, e=r(1-j_k).

Terminal active-block influence is m-1 and full terminal influence is m-1+r(k-1)d; expected terminal Fourier entropy remains r H(h_{k-1})/2. For k=2r+2, r j_k<=2rd/ln(2)->0, hence e=r-o(1). Also a h2(R/a)=r+log2(euler_number)+o(1), using -ln(1-x)=x+O(x^2) as x->0 and r^2 d->0. Thus e/[a h2(R/a)]->1. No universal factor smaller than one can replace the reference bound, even for actual Boolean functions and essential physical queries. This proves sharpness of the new schedule capacity, not an unbounded Hhat/I family.
