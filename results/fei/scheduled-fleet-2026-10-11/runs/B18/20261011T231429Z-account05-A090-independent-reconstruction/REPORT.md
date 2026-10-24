# A090 independent reconstruction

## exact target, quantifiers, hypotheses and units

Verdicts: HOLDS for A096-UNIFORM-SINGLETON-HALF-TAX v1, including its uniform endpoint coefficient, and HOLDS for A087-CONTROL-TREE-LAMBDA-KL-IDENTITY v1. Full FEI remains OPEN. These are the two targets explicitly assigned by B18 STREAM_NOTES v1 (2026-10-11 22:45 UTC). Neither is a near-complete universal FEI theorem. Entropy and KL below are in bits, Fourier coefficients normalized. Finite dimensions are arbitrary in the analytic proofs.

A096: genuine Boolean sign children on any finite residual cube with an interior product law; singleton selector X has independent bias p in (0,1). M=H(S_X|S_residual), J=I(X;T) in the physical-child Fourier experiment. With r=min(p,1-p), delta=1-sqrt(1-r), prove J-M<=h2(r)-h2(delta), uniformly in all residual parameters. The limit of the supremum normalized by p log2(1/p) is 1/2.

A087: any balanced Boolean core g, k>=1 fresh fair point controls, q=2^-k, F=1+A_k(g-1), and the physical control-first stopping tree. Prove the exact one-sided logarithmic-charge/magnitude-KL identity and sum <=4kq, preserving terminal entropy qH(g) and terminal influence qI(g).

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json was read in full (revision 2026-10-11-execution-v2). Campaign README, CURRENT_STATUS, claim/obstruction/packet/next-action JSONs and FEI_100_agent_research_plan.tex were loaded; target contract is the paragraph A090, Independent reconstruction. The local BOARD and B18 STREAM_NOTES v1 determine the current assignment rather than the older registry snapshot.

The supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING were loaded. Original mathematical inputs actually used: sources/ERASURE_REDUCTION.md sections 1-6; sources/BLOCK_RESTRICTION_IDENTITY_2026-09-18.md sections 1-3; sources/LOG_ALLOCATION_CURATED.md sections 2,4-5. Relevant older runs B05 (20261011T193057Z), B09 (20261011T195500Z), B19 (20261011T195038Z) were loaded for scope/history. The two threshold txt versions and two percolation txt versions were loaded; threshold 38pp Proposition 8.6 is the relevant partial-Fourier/shared-data identity, rederived here. Percolation inputs are not needed for either proof. Text files contain non-UTF8 bytes and were read using cp1252 after the initial UTF8 decode failed; this caused no mathematical substitution.

Author CLAIMS.json exact statements were read first. RECONSTRUCTION.md was saved before opening either author's REPORT.md. Source hashes are in out/SOURCE_MANIFEST.json. The comparison is separate in RECONSTRUCTION_COMPARISON.md. No author code is used by the validator.

## complete derivation or exact first unsupported line

### 1. Independent two-dimensional proof of the singleton tax

Write a_T=hat G(T), b_T=hat H(T), with X=1 selecting G and X=0 selecting H. Define Q_T=p a_T^2+(1-p)b_T^2. Booleanity and Parseval ensure sum_T Q_T=1 and normalized physical child distributions. The two parent coefficients over T are

    c_T=p a_T+(1-p)b_T,
    d_T=sqrt(p(1-p))(a_T-b_T),
    c_T^2+d_T^2=Q_T.

For Q_T>0 the physical posterior X probability is z=p a_T^2/Q_T, and the spectral singleton probability is w=d_T^2/Q_T. Thus H(X|T)=sum Q_T h2(z) and M=sum Q_T h2(w). Zero packets disappear.

Let v=(sqrt(p)a_T,sqrt(1-p)b_T)/sqrt(Q_T), a real unit vector. The physical probabilities are the squared coordinates of v and the spectral probabilities those of Ov, where

    O=[[sqrt(p),sqrt(1-p)],[sqrt(1-p),-sqrt(p)]].

Set D=diag(1,-1), D'=O^t D O. The two coordinate imbalances are Z=v^t Dv=2z-1 and W=v^t D'v=1-2w. By direct multiplication, (D+D')^2=4p Id and (D-D')^2=4(1-p) Id. For any choices of signs, the operator norm of +/-D +/-D' is at most 2sqrt(1-r). Therefore

    |Z|+|W|<=2sqrt(1-r).

For t=min(z,1-z), s=min(w,1-w), this gives t+s=1-(|Z|+|W|)/2>=delta. Both t,s lie in [0,1/2]. If t+s<=1/2, binary entropy subadditivity h2(t)+h2(s)>=h2(t+s), and monotonicity up to 1/2 imply >=h2(delta). Subadditivity follows, for example, by putting two disjoint events of probabilities t,s on one probability space, applying entropy subadditivity to their indicators, and then taking their union. If t+s>=1/2, concavity gives h2(t)+h2(s)>=2(t+s)>=1>=h2(delta). Consequently every packet satisfies

    h2(z)+h2(w)>=h2(delta).

Average Q_T and use J=h2(p)-H(X|T) to obtain

    J-M<=h2(r)-h2(delta).

This is a universal analytic proof, without dimension limits or continuum sampling. The geometric step applies to every real pair of amplitudes, not specifically Boolean amplitudes. Booleanity is used to identify normalized probability experiments, and not to sharpen the packet inequality.

Since delta=r/2+r^2/8+O(r^3), direct entropy expansion gives

    h2(r)-h2(delta)
    =(r/2)log2(1/r)+[(log2(e)-1)/2]r+O(r^2 log(1/r)).

This uniform upper bound permits taking suprema before p->0. For the matching lower bound take H=1 and G=(-1)^(y1*y2) on two fair bits. Its four Fourier magnitudes are 1/2 and its mean is 1/2. The residual mixture has Q_empty=1-3p/4 and three other masses p/4. Hence J=H(Q)-2p=(3p/4)log2(1/p)+O(p). At the empty packet d^2=p(1-p)/4, so its contribution to M is (p/4)log2(1/p)+O(p). The three other packets have total mass 3p/4 and singleton probability 1-p, contributing (3p/4)h2(p)=O(p^2 log(1/p)). Therefore J-M=(p/2)log2(1/p)+O(p). This actual Boolean pair proves the matching supremum lower bound. The more general fixed-pair expansion in A096's other claim is not independently accepted by this report; it is unnecessary for this endpoint proof.

### 2. Independent control-tree proof

At an active node with s>=1 remaining controls put u=2^-s. Every control-indicator Fourier coefficient has magnitude u. Because E g=0, the Fourier coefficients with empty core are 1-u at the empty set and +/-u at nonempty control sets; those with core T!=empty are +/-u ghat(T). Pair coefficients without/with the next queried control. The empty packet has a=1-u,b=+/-u. Every other packet has a=+/-b. Parseval gives the queried influence sum b^2=u; the empty packet accounts for u^2. (Direct physical check: the other s-1 controls are active with probability 2u, and a balanced g disagrees with 1 with probability 1/2.) Thus

    lambda_s=sum b^2 log2((a^2+b^2)/b^2)
      =u-u^2+u^2 log2((1-2u+2u^2)/u^2).

For the actual children G=1+A_(s-1)(g-1) and H=1, the G empty coefficient is 1-2u>=0 and H empty coefficient is 1. Their magnitude mismatch is ((1-2u)-1)^2/4=u^2. For every other packet Hhat=0, and magnitude mismatch is Ghat^2/4=b^2. Therefore magnitude mismatch e_T equals b_T^2 in each packet, not merely in the total. The magnitude-mismatch residual

    u[log2(1/u)-D2(e/u || Q)]
      =sum e_T log2(Q_T/e_T)

is exactly lambda_s. Here Q_T=a_T^2+b_T^2 is a probability law and e/u is another probability law. Endpoints at s=1 satisfy the same calculation; zero packets are omitted.

The reach probability of this active node is 2^-(k-s)=q/u. Consequently

    sum w_s lambda_s=q[k+A_k],
    A_k=sum_(s=1..k)2^-s[2s-1+log2(1-2^(1-s)+2^(1-2s))].

For s>=1 the logarithm argument lies in [1/2,1]. Thus every bracket is nonnegative (the s=1 bracket is zero), and the bracket is <=2s-1. Since sum_(s>=1)2^-s(2s-1)=3, 0<=A_k<=3 and q(k+A_k)<=4kq. Consumed physical influence is exactly sum_s(q/u)u=kq. With probability q the terminal core is g and all other leaves are constant, so terminal entropy and influence are qH(g) and qI(g). No coordinate is reused on any physical path.

### 3. First unreconstructed universal implication

There is no unreconstructed line in either scoped target. The first missing line in a proposed universal conclusion is

    q H(g) <= C q I(g) uniformly over arbitrary balanced Boolean cores g.

After dividing by q>0 this is balanced FEI itself. It is not licensed by the proved control charges. Arbitrary f can be balanced as z*f on a fresh fair bit; its entropy is H(f), influence I(f)+1. Taking tensor powers before this balancing shows that a universal balanced bound implies H(f)<=C I(f) after division by tensor count and passage to that count's limit. Thus balanced FEI has full universal strength. The singleton tax supplies neither this terminal estimate nor a nonreusing influence payment for cumulative erasure. The authors' target statements explicitly preserve these limitations.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before execution. Command: python -X utf8 runs/20261011T231429Z-account05-A090-independent-reconstruction/code/check.py (cwd A090). All ordered pairs of two-bit Boolean cores, five fixed rational biases, 1,280 cases, no symmetry quotient. Every nonzero packet verifies parent Parseval and the rational form (1-t-s)^2<=1-r of the geometric bound. All 70 balanced three-bit truth tables with k=1,2,3, 210 cases, verify the actual character-sum coefficients, packetwise magnitude equality, queried influence and exact logarithmic formula using rational argument/coefficient dictionaries. Result: PASS, 21,810 exact assertions, 4,400 nonzero singleton packets, observed runtime 16.2770061 seconds; saved in out/CHECK.json. These checks certify identities at the frozen finite domain; the analytic proofs above establish arbitrary dimensions and all interior p. No floating-point sign was accepted, and no dimension was increased.

## proof dependencies and changed downstream conclusions

Both target versions are independently accepted at their stated scopes by A090. Upper singleton bound uses only normalized partial-Fourier probabilities, finite-dimensional quadratic-form geometry, binary entropy subadditivity and concavity. The endpoint lower bound uses the explicit two-bit Boolean pair, so A096's general fixed-pair theorem is not a proof dependency of this acceptance. The control identity uses direct character sums, Parseval, the KL definition and exact fair reach weights. None of the other agents' proofs is a mathematical premise of these reconstructions.

A061/C019 can consume the accepted control payment but must retain terminal qH(g). B09 can consume the singleton half-tax but still must pay conditional spectral entropy and total physical influence. Full FEI, universal stopping-tree selection and optimal finite-p singleton tax remain unproved.

## one next mathematical action and independent reviewer

Next: A099/A064 should provide a source-complete stopping-tree estimate of cumulative logarithmic cost PLUS terminal entropy by the same original physical influence, retaining arbitrary terminal cores. A094 (alternate A085) should challenge this reconstruction, especially the normalization of the physical experiment and the exact equality of signed and magnitude mismatch at s=1. This consumes the audited dependency directly rather than restarting a finite census.

## actual persistence receipts or precise save blocker

The local run contains REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, BLIND_RECONSTRUCTION.tex, RECONSTRUCTION.md, RECONSTRUCTION_COMPARISON.md, FROZEN_SPEC.json, code/check.py, out/CHECK.json, out/SOURCE_MANIFEST.json and out/RECEIPTS.json. STATUS.md, WORKLOG.md and LEARNED.md are saved inside A090 only. The SHA256 receipt manifest records local files; supervisor copy, mirror verification, index adoption and downstream use have not been performed by this agent.

## Universal bridge

This stage moves C019 stopping-tree payment by independently accepting the exact control-first charge <=4 times consumed control influence, with arbitrary balanced-core terminal entropy retained, and validates B18's singleton half-tax target without using the general fixed-pair derivation. It supplies no new universal constant: qH(g) remains full-FEI strength, and general cumulative erasure payment is unpaid. The shortest NEXT is a complete terminal-inclusive nonreusing tree inequality from A099/A064, since the audited identities now isolate precisely its missing bill; another class census would not address it.
