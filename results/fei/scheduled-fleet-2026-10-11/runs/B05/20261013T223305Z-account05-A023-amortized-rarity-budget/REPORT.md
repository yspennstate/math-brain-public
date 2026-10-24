# exact target, quantifiers, hypotheses and units

A023/B05 stage 3, run 20261013T223305Z-account05-A023-amortized-rarity-budget. Uniform physical Boolean signs, all entropy/KL in bits. Let U,V,W be compatible point indicators on disjoint control blocks of independently arbitrary widths R,T,L>=1, X one fair physical separator bit, and g an independent BALANCED Boolean core. The controller has three overlapping events:

    A=XU OR XV OR WUV, F=1+A(g-1).

Write p=2^-L, q=2^-R, r=2^-T, beta=q+r-qr, eta=pqr, pi=(beta+eta)/2 and e=beta-eta. The physical stopping policy queries X first, resolves WUV if X=0 or U OR V if X=1, and stops at a constant or at g. It retains terminal entropy pi H(g). Core entropy is not discarded even on very rare paths.

All-dimensional scoped result: every descendant control node is strictly K=4-good; the separator may be bad and is not assumed good. Its exact one-use odd-face price is c_X=Jrem+e I(g)/2, where J(B)=I(1-2B)/2 and

    d_X=e/2,
    Jrem=[(L+R+T)eta+R q(1-r)+T r(1-q)]/2,
    I_ctrl=J(A)=d_X+Jrem, I_terminal=pi I(g).

The stopping tree has Q_bad either zero or c_X, hence Q_bad<=I(F)-d_X. With H(g)<=C0 I(g), a marked separator reserve spent once proves H(F)<=max(5+2/ln2,C0+1)I(F). Without this terminal hypothesis, the exact upper ledger is

    H(F)<=(5+2/ln2)J(A)+pi H(g)+(e/2)I(g).

The complete genuine minority/KL bill plus terminal is <=5J(A)+pi H(g)+(e/2)I(g); with its separate 3mu/ln2 allowance it is <=(5+3/ln2)J(A)+pi H(g)+(e/2)I(g).

For g=z times the selector between any even-k>=4 bent sign and its flip at one vertex, g is balanced and H(g)/I(g)<3. This gives H(F)<8I(F), retained J+terminal<=5I(F), and full sufficient mismatch ledger<10I(F) uniformly in L,R,T,k. No repeated-child bank or universal FEI theorem is claimed. The new theorem extends the existing A023 overlap claim; it does not open a separate broad candidate.

# sources actually read, revisions and theorem locators

Read BOARD.md (2026-10-13 22:25 UTC), B05 STREAM_NOTES.md v2, own STATUS.md, and EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2. Lead direction remains the exact overlapping-control odd-face target; its remainder objection was already repaired in stage 2 and is not rederived as new work.

Consumed A021 run 20261013T214613Z REPORT.md, DERIVATION.md and CLAIMS.json: its new arbitrary-controller exposure, actual five-bit bad-root witness, and bounded four-control repair. Independently review only the witness and balanced-control entropy-transfer subclaims in REVIEW_A021_WITNESS.md; do not repeat the 680-controller census. Read A022 stage 3 REPORT.md (paired-access and retained sparse terminals), and A028 stage-2 DERIVATION.md (arbitrary-controller payment and its FEI-strength caveat). These informed the next gap and are not premises of the new theorem.

Own stage-2 OVERLAP_GOOD_NODE_PROOF.md and REPORT.md supply the exact good-node exposure rule and corrected review scope. The B05 lead's odd-face report sections 1-2 supply the intended currency; the required scalar/isoperimetric inequality is independently reconstructed below. No brain write, external messaging, Git, new paper premise or percolation hypothesis. out/source_receipts.json records local hashes and read scope; no source-file receipt is called an independent theorem audit.

# complete derivation or exact first unsupported line

## 1. Independent witness review before extending the mechanism

A021's actual controller is A=x1x2 OR x1x3 OR x0x2x3. Direct positive-literal truth tables, integer Walsh transforms and independent edge counts give pi=7/16, J(A)=3/4, d_x0=1/16 and face price I(F0F1)/2=1/4 for g=z. Its B-4d is exactly the source's rational prime-log expression, independently certified positive. The original fixed x0-first control order has Q_bad=1/4; x1-first has zero on this fixture.

For any balanced g, the nonempty-core Fourier rows have controller coefficients multiplied by ghat(T); their erasure kernel is homogeneous of degree two. Summing ghat(T)^2 gives one, while the pure-control row is unchanged. Thus control-node B and d are precisely the dictator-core quantities. The face price depends on I(g), not only balance. REVIEW_A021_WITNESS.md records HOLDS for exactly this source-bound scope, without accepting A021's tensor-prefix or finite exhaustive conclusions. No source repair was supplied.

## 2. The three-event extension and actual coordinate partition

The separator controller children are A0=WUV and A1=U OR V, with A0 contained in A1. Their densities are eta and beta. The parent density is pi, not beta+eta. Every active history reaches the same g once, including histories where multiple event descriptions hold.

A point indicator of width m and density rho has J=m rho by directed-edge counting. Therefore J(A0)=(L+R+T)eta and J(A1)=R q(1-r)+T r(1-q). The separator influence is (beta-eta)/2=e/2 because a balanced g is negative on half the data cube. Each other physical controller coordinate has its half-averaged child influence. Hence

    I(F)=J(A)+pi I(g), J(A)=e/2+[J(A0)+J(A1)]/2.

The W-coordinate contribution to Jrem is L eta/2; the U block's is R[q(1-r)+eta]/2, and the V block's is T[r(1-q)+eta]/2. These are actual physical coordinate accounts, not independently credited boundaries of the three named events. The formulas are verified against direct edges in every frozen case.

## 3. Descendants are good; the separator is treated separately

In the X=0 child, the controller is one point conjunction WUV. Every queried control has a constant inactive child. For signed disagreement d, exact Fourier grouping gives Jsgn=d-d^2+d^2log2((1-2d+2d^2)/d^2), and B<=Jsgn+c d, c=1/ln2. Thus B/d<=1+c+2c/euler<4. Here euler denotes the exponential constant, distinct from the controller density e. Endpoints d=0 contribute zero. This is an actual binary erasure statement and does not equate magnitude mismatch to signed disagreement.

In the X=1 child, U OR V is the previous two-event fresh-block case with a=1. At a U-control node with remaining point probability rho=2^-j, mismatch is d=rho(1-r)/2. Fibers with nonempty remaining-U label have one zero child amplitude and contribute 2(1-rho)d exactly. Other fibers have mismatch rho d, total packet mass at most one, and contribution <=h2(rho d). Hence B/d<=2(1-rho)+rho log2(euler/(rho d)). Since (1-r)>=1/2>euler/8, this is strictly <2+2rho(1+j)<=4. After U fails the V nodes are again constant-child; after U succeeds stop immediately at g. No descendant bad-control face bill exists in either branch, in any widths.

The X separator itself is never priced by an assumed fresh-event lemma. The finite checks happen to find it good in the frozen domain; the theorem and reserve work even if it is bad outside that domain. Root-goodness in all widths is a separate unsupported strengthening.

## 4. Exact root face price and the first-revelation reserve

Let D=A1-A0. It is an indicator of density e, and F0F1=1+D(g-1). Balance gives I(F0F1)=e I(g)+J(D). Direct control edges yield

    J(D)=R q(1-r)+T r(1-q)+(L+R+T)eta=2Jrem.

For example, a U pivot changes D if V=0, or if V=1 and W=1; its probability contribution is q[(1-r)+p r]. The analogous V contribution and the W contribution prove the displayed identity. Equivalently, the cut edges of A0 and A1 are disjoint, so their symmetric-difference boundary adds exactly. Therefore c_X=Jrem+e I(g)/2. Since e/2<=pi, c_X<=Jrem+pi I(g)=I(F)-d_X. Since descendants are good, Q_bad is zero if the root is good and c_X if it is bad.

This is a one-use face account. Odd faces involving X are charged only when X is first revealed, since Q(f)=I(f0f1)/2+[Q(f0)+Q(f1)]/2. The identity follows by partitioning cube faces into those lying inside children and those projecting to cut edges of their product. Descendants cannot debit these same faces.

Influence reserves must also be marked before descent. At rate K=5+2c, give each nonseparator physical control coordinate K times its expected influence. Reserve one unit of that rate exclusively for c_X's controller part; descendants get only K-1=4+2c. Their full erasure/recombination cost is within that remaining rate. Each terminal-core coordinate at rate C0+1 reserves one unit for the root's data face part; terminal entropy receives only C0. The actual data fraction consumed is e/(2pi)<=1; the leftover from this reserved unit is eta I(g), nonnegative. The separator's own influence is priced at K. Root charges are paid once from these named capacities. No reserve is recreated at child nodes. It would be invalid to apply the same one-unit reservation at every ancestor of an arbitrarily deep separator tree.

## 5. Entropy/KL telescope with all terminal cost included

For any actual split, Delta H=B+JS and JS<=2c mu<=2c d, with magnitude minority mu. This follows from the scalar inequality [(1+t)ln(1+t)+(1-t)ln(1-t)]/2<=1-sqrt(1-t^2): its difference has derivative t/sqrt(1-t^2)-artanh(t)>=0. Summing across packets gives the JS claim.

At the separator B_X<=4d_X+c_X irrespective of badness. For a good node this is immediate. Otherwise B<=h2(d)<=d log2(1/d)+c d<=c_X+4d, because the cube edge-isoperimetric inequality gives d log2(1/d)<=I(F0F1)/2. An elementary proof of that inequality is as follows: a set of m vertices spans at most m log2(m)/2 edges. Induct across a cube coordinate with child sizes a<=b; the new internal edges are at most a, and (a+b)log2(a+b)-a log2(a)-b log2(b)>=2a follows from h2(a/(a+b))>=2a/(a+b). The boundary therefore has at least m log2(2^n/m) edges, yielding the normalized influence assertion.

Summing the actual fair stopping tree gives

    H(F)<=(4+2c)J(A)+Q_bad+pi H(g)
         <=(4+2c)d_X+(5+2c)Jrem+pi H(g)+(e/2)I(g).

This is stronger than the stated uniform-rate upper ledger and displays which root-coordinate capacity is unspent. The entire pi H(g) is retained. If H(g)<=C0 I(g), the marked account proves H(F)<=max(5+2c,C0+1)I(F).

For the requested retained KL bill, define m_T=(|a_T|-|b_T|)^2/4, mu=sum m_T, Q_T=(a_T^2+b_T^2)/2, nu=m/mu, and Jminor=sum m_T log2(Q_T/m_T)=mu[log2(1/mu)-D2(nu||Q)]. Always Jminor<=B and mu<=d. Therefore J_tree+pi H(g)<=4J(A)+Q_bad+pi H(g)<=5J(A)+pi H(g)+(e/2)I(g). Its additive 3c sum mu allowance is at most 3c J(A), giving the full source ledger. No raw mu log term is substituted for Jminor, no KL reference is transferred across nodes, and terminal entropy is not omitted.

## 6. A nontrivial unbounded terminal family

Let b be any bent sign on even k>=4 bits, let b' flip b at one vertex v, and let h fairly select b or b'. Balance it by an independent sign z, so g=z h. Flatness gives I(b)=k/2. A one-point flip changes each data influence by 2delta b(v)b(v^i), delta=2^-k, and h's selector influence is delta. Thus I(g)=1+I(h)>=1+k/2-(k-1)delta, while H(g)=H(h)<=k+1. For k>=4 this ratio is <3. Its terminal certificate uses only a proved support/edge bound, not an unproved arbitrary-core estimate.

With c<81/56, 5+2c<8 and 5+3c<10 by exact rational arithmetic. Hence the full family has H(F)<8I(F), J+terminal<=5I(F), and full sufficient mismatch ledger<10I(F). L,R,T and k remain independent and unbounded. For fixed core and L, R=T going to infinity makes event density and total influence vanish; the same constants still apply. This is a three-event overlap extension of the existing first-revelation mechanism, not a claimed novel bound for bent cores themselves.

First unsupported universal line: the sum of marked separator reservations remains bounded per actual physical coordinate in arbitrary overlapping/deep controllers, with all terminals certified. The present one-separator reserve is not an arbitrary-depth potential. A021's balanced selector exposure shows precisely why repeating a residual J bank without consumption is invalid. No automatic maximal-influence policy, universal zero-badness statement, or full FEI follows here.

# executed validation with domain, arithmetic, commands and outputs

Frozen before execution: out/FROZEN_SPEC.json. Helper A023-separator-v1, 27 dictator-core roots for L,R,T=1,2,3; eight balanced bent4/point-flip roots at L,R,T=1,2; separate source witness and its balanced-core transfer. No symmetry quotient or dimension escalation, maximum actual truth-table dimension 13. Frozen runtime 60 seconds and memory estimate 120 MB; no >300 MB or heavy job was run.

Command from A023: `python -X utf8 runs\20261013T223305Z-account05-A023-amortized-rarity-budget\code\check_separator.py`.

PASS: 35 primary roots, 729 exact assertions, 110 unique spectral nodes, 38 saved exact sign certificates, 0.2201620000123512 seconds observed compute time. All 35 separator-first stopping trees have zero bad-control credit in this grid; the theorem does not infer that root-goodness holds outside it. Each tested descendant is good, and every queried/terminal influence and entropy partition is exact. Source witness replay confirms the bad x0 node and the source prime-log vector.

Arithmetic: actual sign tables, integer FWHT, direct edge-count Fraction influences and physical child-product face costs, rational prime-log representations of erasure and Jminor, and outward positive-series atanh intervals with a proved tail. Twenty-four terms suffice; the frozen 48-term fallback was not needed. Exact zero vectors are equality, not strict badness. Out/results.json is flushed after every root; out/witness.json and out/sign_certificates.json retain reviewable endpoints. No floating entropy sign, random sample, GPU, background job or imported A021 helper. Float runtime clocks are metadata only.

# proof dependencies and changed downstream conclusions

The new separator proof is self-contained, with the displayed two-event exposure reconstruction, direct boundary ownership, edge isoperimetry and JS scalar bound. It uses the earlier A023 theorem as a checked contextual interface; no faulty A021 remainder or arbitrary-controller FEI is a premise. The current existing overlap claim is extended as version 2 with its previous scope preserved through the exact prior source. B05's lead currency is reconstructed rather than accepted from numerical tests.

The source-bound A021 review is partial HOLDS only for the overlap witness and balanced-control transfer, with no repair contribution. The stream's pending-review cap is respected by consuming that objection and extending the existing scoped A023 packet, rather than opening another broad universal candidate. Shared registries are not edited.

Changed downstream conclusion: A021/A022/A028/A029/A064 can use a legitimate single owned separator reserve for an infinite three-event overlap family, even when a separator cannot be assumed good. The exact price decomposes into remaining-control and terminal-core fractions, and is deleted before child recursion. The old negative-remainder approval remains retracted. A general policy still has to prevent these reservations from accumulating across many separator ancestors.

# one next mathematical action and independent reviewer

Next: replace X by a multi-bit point separator and track the ACTUAL remaining one-unit reserve after each reached separator layer. Test whether bad layers can consume disjoint physical slack, or certify a growing reservation deficit with terminal entropy retained. Do not duplicate the A021 four-control census or assume that a one-root bound telescopes through repeated separators.

A087 should independently check the source witness, point-block boundary partition and reserved capacities; A094 should check the all-width descendant-good proof and terminal quantifiers. A029/A064 should consume the explicit reserve once rather than reuse residual J at descendants. Handoff is through saved artifacts; no tool messages were sent.

# actual persistence receipts or precise save blocker

Locally saved inside the assigned run: REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, SEPARATOR_RESERVE_PROOF.md, REVIEW_A021_WITNESS.md, code/check_separator.py and code/save_metadata.py, frozen spec, per-root results, independent witness/certificates, source receipts, schema check and artifact SHA256 receipts. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current. Every file is below 20 MB. Shared trees, other agents' folders and old runs remain read-only. No local save blocker; independent review, supervisor copying, remote mirrors and downstream adoption remain unverified.

**Universal bridge:** This stage moves C019/B05's localized odd-face payment past the known three-event bad-root obstruction by independently reconstructing it and proving an all-dimensional separator-first remedy with one reserve that is consumed before descent. The complete bound is Q_bad<=I(F)-d_X, H<8I on the unbounded balanced bent-surgery family, retained J+terminal<=5I and full sufficient mismatch ledger<10I. What remains is an ancestral ownership rule for repeated separators and a universal terminal certificate; root-goodness was not extrapolated from the finite zero ledger. NEXT turns the one-bit separator into the first repeated-revelation case and measures its exact remaining capacity, the shortest route toward universal amortization because it addresses the potential reuse itself rather than adding another finite family census.
