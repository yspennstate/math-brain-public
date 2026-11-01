# Universal per-Fourier-set polarity connectivity and one-root forests

Let f be ANY nonconstant sign Boolean function on a finite uniform cube. Both complete signed prime-implicant tables, for f=+1 and f=-1, are fixed before sampling. For a nonempty A with fhat(A)!=0, form the two coordinate graphs on A: connect two vertices when some prime of the respective polarity contains both. Then

    if the positive graph is disconnected,
    the negative graph contains EVERY cross-pair between
    different positive components.                   (1)

In particular at least one of the two graphs is connected. This is a structural statement for actual Boolean Fourier support, not arbitrary subset laws or arbitrary incomplete gate dictionaries.

## Proof from an actual outside fiber

Let C_1,...,C_k be the positive components, k>=2. Every positive prime has its A-coordinates entirely in one C_c, or avoids A. The exact positive DNF of f therefore restricts, at each outside assignment z, to

    1_{f_z=+1}=h_0(z) OR h_1(x_C1;z) OR ... OR h_k(x_Ck;z),

where h_0 is constant on A and the other indicators have disjoint A-blocks. Some h_c may initially be constant. Since fhat(A) is the average over z of the full-A coefficient of f_z and is nonzero, there exists z for which that coefficient is nonzero. At this z, h_0=0 and

    f_z=1-2 product_c(1-h_c),
    fhat_z(A)=-2 product_c widehat{1-h_c}(C_c)!=0.

Thus every h_c is nonconstant and depends on EVERY coordinate of C_c. (Independence here is only the uniform product measure on the disjoint coordinate blocks.) Each such coordinate a has a false endpoint of a pivotal edge of h_c: h_c(x_c)=0 and flipping a gives1.

Choose any a in C_c and b in C_d with c!=d. Independently choose these false pivotal endpoints in blocks c,d and any false assignments in all other blocks, keeping outside assignment z. The full f value is -1, and flipping either a ALONE or b ALONE makes f=+1. At least one complete negative prime certificate holds at this false point: start with the full point conjunction and remove literals until minimal. EVERY negative certificate holding there must contain both a and b, since omitting either would also contain its true neighboring point. A negative prime therefore contains a,b, proving (1). The complete multipartite cross-graph is connected because k>=2.

No graph criterion is silently transferred between arbitrary gate tables. Completeness of BOTH actual signed prime tables, nonzero Boolean Fourier coefficient, and the chosen full outside fiber are the load-bearing hypotheses. Relevance of each A-coordinate is automatic from fhat(A)!=0, so no isolated uncovered vertex occurs.

## A connected table supplies an actual one-root partition forest

For any gate table with connected A-coordinate graph, start at one gate meeting A and assign to it all its A-coordinates. Until A is covered, connectivity supplies an unvisited gate meeting both the assigned union and an unassigned coordinate. Assign to it ALL fresh A-coordinates; choose its parent to be the already-used OWNER of one shared assigned coordinate, and use that coordinate as the attachment. Each gate is visited once, owns a nonempty subset, and each new parent precedes its child. There are at most |A| gates. The selected subsets partition A, and the parent tree from the first root reaches all gates. Hence the ownership graph has one source strongly connected component, and this is an ACTUAL one-root partition forest in the original queue. The same owned coordinate may parent several children: the original queue explicitly allows attachment MULTISETS. Its multiset/count probabilities remain part of the unpaid complete run cost; they are not omitted.

Therefore for EVERY f and EVERY nonempty Fourier-supported A, a one-root actual partition forest exists in at least one of the two ORIGINAL complete prime tables. Arbitrary fixed positive feasible weights and valid ordered covers make the prescribed finite run have positive probability. All gate names and subset/offspring probabilities still have to be paid.

## Fixed mixture, with the polarity label honestly paid

Fix Q_mix=(Q_+ + Q_-)/2 BEFORE seeing A. It is one original output subprobability with a fixed binary reference label, not a free post-observation retuning. The forest above is present in one summand and loses at most one bit of mass to that label. Under the actual squared Fourier law, the total nonempty label debit is Var(f)<=I(f), by Parseval I=sum |A| fhat(A)^2. This is a universal paid structural bridge: all Fourier sets can use a ONE-root forest with a paid polarity selector.

It does not prove a bounded full queue cross entropy, a paid root gate name/width, or a paid child-name/rank cost. In particular the root D of each original table stays attached to its own summand; different normalizers cannot be pooled as a free credit. BOTH_POLARITIES.md refutes selecting just ONE orientation globally. The fixed MIXTURE is genuinely broader, and (1) explains why the separated-component obstruction cannot rule it out on a Fourier-supported A. The remaining universal gap is a dimension-free complete label/rank/rarity payment in that fixed mixture.
