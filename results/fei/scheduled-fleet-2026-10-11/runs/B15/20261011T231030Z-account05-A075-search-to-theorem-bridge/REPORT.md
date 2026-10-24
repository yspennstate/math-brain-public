# A075 — balanced composition, erasure collisions, and restriction extraction

## exact target, quantifiers, hypotheses and units

For arbitrary Boolean sign f on m uniform coordinates and a balanced Boolean sign g on n uniform coordinates, let F=f(g(x^(1)),...,g(x^(m))) on disjoint blocks. Entropy H is in bits, p_f(T)=fhat(T)^2, I_i is physical influence, I=sum I_i, B_i=H(S_i|S_-i), B=sum B_i. This stage proves exact H, I and B identities, specifies precisely when the B identity needs the no-level-1 hypothesis, and gives a constructive restriction-extraction implication for universal selectable-erasure constants. It also supplies a fully certified recursive Boolean family and an explicit failing restriction. Full FEI remains OPEN. This is a narrow reconstruction/repair of B15's supplied composition calibration, not a new broad universal inequality or a new exhaustive extremizer search.

## sources actually read, revisions and theorem locators

Protocol revision 2026-10-11-execution-v2 was read in full; report README, CURRENT_STATUS, registries, packet matrix, stream actions, campaign plan and earlier B05/B09/B19 reports were loaded and inspected. Supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and source notes were consulted. BOARD.md was read at stage start; B15 STREAM_NOTES.md v1, 2026-10-11 22:50 UTC directly supplies this target. The retired biased-grid census is not repeated. ERASURE_REDUCTION.md sections 1,2,4 supply the actual restriction identities and scalar JS bound, reconstructed below. A082 REPORT.md at run 20261011T221008Z-account05-A082-finite-inequalities was read for the point-defect constant and scope; only its witness is reconstructed here, not its n<=4 optimality theorem.

All four supplied paper texts are loaded with cp1252 decoding (the files are not UTF-8), and introductions and composition/restriction locators inspected. Their class theorems and percolation hypotheses are context, not premises of this proof. No claim of a full line-by-line paper audit or literature novelty is made. The saved source receipts identify actual file bytes, hashes and relevant excerpts. No external source or unreviewed campaign theorem is needed for the composition calculation.

## complete derivation or exact first unsupported line

Write phi(a,b)=-a log2(a)-b log2(b)+(a+b)log2(a+b), with continuous zero conventions. It is homogeneous, nonnegative, and strictly positive exactly when a,b>0. Put q(V)=ghat(V)^2. Since g is balanced, q(empty)=0. Expanding f in its Walsh basis gives, for an index U with nonempty block parts U_j and active-block set T,

    Fhat(U)=fhat(T) product_{j in T} ghat(U_j).

There is one term: inactive blocks contribute the constant 1, whereas an active block has no constant coefficient. Thus the spectral generative law is first T~p_f, then independent nonempty V_j~q for j in T. Its entropy and expected set size give, without any no-level-1 assumption,

    H(F)=H(f)+I(f)H(g),             I(F)=I(f)I(g),
    I_(j,i)(F)=I_j(f) I_i(g).                                      (1)

Fix coordinate i in inner block j. For each residual index with a nonempty remainder V in block j, both adjacent packets come from the same active outer block j. Homogeneity of phi, followed by summing the independent other blocks, gives I_j(f) times the V!=empty portion of B_i(g). The V=empty portion of B_i(g) is phi(q(empty),q({i}))=0. Residual indices with block j empty instead pair an inactive block and a singleton-active block. Consequently the exact formula is

    B_(j,i)(F)=I_j(f) B_i(g)
      + sum_{T subset [m]\{j}} phi(p_f(T), p_f(T union {j}) q({i})). (2)

The correction vanishes iff q({i})=0 or B_j(f)=0. This iff includes irrelevant outer coordinates. Summing proves

    B(F)=I(f)B(g)+sum_{j,i,T} phi(p_f(T),p_f(T+j)q({i})).           (3)

Therefore B(F)=I(f)B(g) iff, for every pair j,i, q({i})=0 or B_j(f)=0. Equivalently either g has no singleton Fourier mass or B(f)=0. This proves the lead's sufficient no-level-1 hypothesis is unnecessary for (1), sufficient but not necessary for (3), and cannot be dropped from (3) without a substitute. Counterexample: g(x)=x and f=AND2; B(g)=0 but F=f and B(F)>0. No incoherent mixture or shared-variable substitution is used.

For balanced nonconstant f with no singleton mass, define f^[0](x)=x and f^[d+1]=f composed with disjoint copies of f^[d]. Set a=I(f), h=H(f), b=B(f). The inner gates remain balanced and have no singleton mass for d>=1; the d=0 identity is immediate. Equations (1)-(3) imply

    I_d=a^d, H_d=h(1+a+...+a^(d-1)), B_d=b a^(d-1).              (4)

Thus for a>1, H_d/I_d -> h/(a-1) and B_d/I_d=b/a, for d>=1. Coordinate influence of a balanced nonconstant function sums to at least one since p(empty)=0. If a=1 and f has no singleton mass, there is a contradiction since then every nonempty supported set would have size>=2. More generally a balanced Boolean function with a=1 has h=0 and is a signed dictator. This handles the excluded denominator exactly.

The zero-erasure alternative also permits recursion despite singleton mass: if f and all recursively composed inner gates have B=0, every correction in (2) vanishes. A concrete example is M=Maj3=(x1+x2+x3-x1*x2*x3)/2. It has four probabilities 1/4, H=2, I=3/2, and every supported set has odd cardinality. Hence B=0. Its recursive functions M_d are odd under global input negation, so only odd Fourier degrees occur and B(M_d)=0. Formula (1) therefore gives for every d>=0,

    I(M_d)=(3/2)^d, H(M_d)=4((3/2)^d-1), B(M_d)=0.              (5)

Their H/I approaches 4, while every root coordinate has zero true erasure. This is a certified all-dimensional family with bounded ratio, not a counterfamily to FEI and not a new FEI class claim.

Here is a physically explicit restriction where all coordinates fail a finite erasure price. Write M_2=Maj3(Maj3(x1,x2,x3),Maj3(x4,x5,x6),Maj3(x7,x8,x9)). Fix

    x3=-1, x5=+1, x6=-1, x7=x8=x9=-1.

The three branches become AND2(x1,x2), x4, and -1. The root is AND3(x1,x2,x4), with output +1 only at +++. Its spectrum has p(empty)=9/16 and seven other probabilities 1/16. For every relevant i,

    I_i=1/4,
    B_i=phi(9/16,1/16)+3 phi(1/16,1/16),
    B_i/I_i=Kstar=4+(5/2)log2(5)-(9/2)log2(3).                 (6)

Thus every coordinate of this named restriction fails B_i<=K I_i whenever K<Kstar. The saved rational interval certifies 267/100<Kstar<107/40. For every d>2 it is also a restriction of M_d: inside every bottom majority gate fix two children to opposite constants, leaving the third child as a dictator, until the remaining formula has depth two. Constant subtrees are implemented by fixing their leaves uniformly. Then apply the six assignments above to the remaining nine representatives. This gives a deterministic physical restriction recipe for all d>=2. Sharpness beyond this particular witness is not asserted.

For clarity, a universal selectable-erasure principle quantifies over every Boolean residual, not merely the root of a family. Let c=2/ln2. Actual restrictions give

    Delta_i H = B_i + JS_i,       0<=JS_i<=c I_i,
    I(f)=I_i(f)+(I(f_+)+I(f_-))/2.                             (7)

The first equality follows packetwise by writing the child coefficients as u+v,u-v and cancelling entropy of u^2+v^2. For the scalar bound, d(z)=((1+z)ln(1+z)+(1-z)ln(1-z))/2 satisfies d(z)<=1-sqrt(1-z^2): differentiate, use atanh(z)<=z/sqrt(1-z^2), then integrate. With z=2|uv|/(u^2+v^2) this gives JS packet <=c min(u^2,v^2). Summing yields (7). The influence identity averages each remaining physical edge; it spends the queried coordinate once.

If every nonconstant Boolean residual has a relevant i with B_i<=K I_i, induction using (7) gives H<=(K+c)I. Hence any such universal K satisfies

    K >= sup_{f nonconstant} H(f)/I(f) - c.                   (8)

This is a necessary lower bound; it does not pay a universal K. It applies to the supremum of min_i B_i/I_i, distinct from the aggregate supremum of B/I. Applying (5) yields K>=4-c. The explicit hereditary witness (6) is stronger for this family: K>=Kstar is forced on its restriction closure.

There is also a constructive extraction theorem. Suppose a finite Boolean F has H(F)/I(F)>K+c, K>=0. Choose rationals k>K and C>k+c with H(F)>C I(F). Maintain the strictly positive potential P=H-C I at a physical residual. If every relevant i has B_i>k I_i, stop: this is the demanded failing residual. Otherwise choose the least relevant i with B_i<=k I_i. By (7), Delta_i H-C I_i<0, so

    (P(f_+)+P(f_-))/2=P(f)-Delta_i H+C I_i>0.

Choose the child with larger P (break ties with +1). It has positive P. Each step fixes a new coordinate, and a constant residual has P=0, so the algorithm must stop before exhausting all coordinates. At its output every relevant i has B_i>k I_i>K I_i. Decisions for rational k,C are exact: Boolean squared coefficients are rational, and every entropy expression is a rational combination of prime logarithms; multiply denominators and compare the resulting positive integers. The rational choices exist by strict slack; a search over rational pairs with outward enclosures finds them. The algorithm is computable, not claimed polynomial-time or memory-efficient in arbitrary dimension. Applied to recursive families with limiting ratio rho, it works for every K<rho-c once d has certified positive initial slack. Our interval check certifies positive slack already for M_10 and K=1. Its 59049-bit truth table was not generated; this is an analytic parameter check. The explicit restriction (6) avoids such a computation altogether for K<Kstar.

The first unsupported universal line is a dimension-independent influence payment on all actual residuals of unrestricted Boolean functions. A top-level B/I composition invariant provides no such payment. Neither (8) nor a finite collection of extracted obstructions proves finiteness or divergence of the universal optimal K.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was saved before running code/check.py. The bounded domain is all 20 outer tables on one or two variables times all 78 balanced inner tables on one, two or three variables: 1560 cases. No symmetry reduction or randomness. At most six physical bits are enumerated per composition. Two additional recursive truth tables have 3 and 9 bits, followed by the displayed three-bit restriction. This bounded check is not an exhaustive n=5/6 search.

Command from A075: `python -X utf8 runs/20261011T231030Z-account05-A075-search-to-theorem-bridge/code/check.py`. Integer Walsh butterflies and Fraction coefficients produce exact prime-log representations. It checked (1), (2), physical coordinate influences and the iff collision criterion: 27,328 exact assertions passed in 4.265 seconds; 1,728 coordinate rows had positive collision corrections. Deeper recursion is analytic only. Estimated memory 40 MB; no >300 MB job, GPU, automatic dimension increase or heavy parallel job was started.

For x in [1,2], z=(x-1)/(x+1), the 48-term sum 2 sum_{k=0}^{47} z^(2k+1)/(2k+1) lies below ln(x), with remaining tail at most 2 z^97/(97(1-z^2)). Dyadic reduction, positive interval division and coefficient-sign-aware endpoint selection give rational outward log2 bounds. These certify (6)'s rational bracket and M_10's positive initial slack for K=1. VALIDATION.json preserves the exact endpoints, code hash, restriction and runtime. Runtime is observational; all decisive signs are exact. No independent external reproduction is claimed.

## proof dependencies and changed downstream conclusions

Only Walsh expansion, entropy chain rules and the reconstructed scalar bound (7) are mathematical premises. The A082 finite optimality theorem is not assumed; the identical witness constant is explicitly credited and re-derived. B15's calibration must retain the correction (2) whenever neither singleton-free inner spectrum nor outer zero erasure is available. A071/A074 can search restrictions rather than interpret root erasure invariance as hereditary easiness. A091 can reconstruct the collision correction. A026/A028 must retain terminal cost even when the current root has B=0. No claims are marked independently accepted, and shared registries were not edited. Given the B15 pending-claim cap, this is a repair/reconstruction of the lead's existing identity and scoped witness, not another broad candidate.

## one next mathematical action and independent reviewer

Next action: consume A071's certified n=5/6 seed when available; apply (2) and the positive-potential restriction algorithm to its recursive compositions, and identify the smallest actual residual whose selectable erasure exceeds the current finite witness constant. This uses one already found seed and its hereditary bottleneck, rather than restarting a broad census. Independent reviewers: A074 for truth-table restriction and prime-log certificate; A091 for the complete composition/restriction proof. Handoff is through these local saved artifacts; no message was sent.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, frozen specification, code and exact output are written in the assigned A075 run. Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated. out/MANIFEST.json records their byte counts and SHA256 hashes after the save. These receipts establish local persistence only; supervisor copying, registry adoption, Brain ingestion, independent acceptance and mirror verification remain unclaimed. All writes were confined to A075.

## Universal bridge

This stage moves C018 by making the lead's composition calibration exact, supplying the missing singleton-collision term, and turning H>(K+2/ln2)I into a constructive actual residual where every coordinate fails K. It also exhibits the AND3 hereditary bottleneck inside every recursive-majority depth>=2, despite zero root erasure, with exact price Kstar. It does not reduce the unknown universal upper constant or establish an unbounded-ratio family. What remains is a uniformly paid rule on unrestricted residuals, with full terminal entropy retained. Consuming a genuinely stronger seed and extracting its first hereditary obstruction is the shortest next step for this packet toward full FEI: it tests the universal local payment directly instead of adding another already covered class result.
