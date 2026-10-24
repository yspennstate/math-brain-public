# A068 / B14 stage 4: parity-star geometry and a scoped collision payment

## exact target, quantifiers, hypotheses and units

Let h be a regular Boolean sign function on q uniform bits, in the accepted recovered sense: after fixed orientations it is monotone with a total desirability order. Choose any vertex-disjoint stars on its coordinate set, with centers j and leaves L_j; unused vertices are allowed. Define physical data monomials

    y_j(x)=x_j product_{i in L_j} x_i for a center j,
    y_i(x)=x_i otherwise.

Let z contain m independent uniform physical bits, and let a_i(z)=(-1)^Q_i(z), where every Q_i has F2 degree at most two, with arbitrary overlaps. For every finite q,m, including constant controls, define G(x,z)=h(y_i(x)a_i(z)). This stage proves a complete normalized reference R with

    H(G)<=Gamma_R(G)<=C_reg I(h)+2I_z(G)
                       <=C_reg I_x(G)+2I_z(G)<=C_reg I(G),
    C_reg=log2(4+e)+2log2(e*pi)<8.937.

All costs are in bits; all influences refer to the stated physical coordinates. The rank-reference dependency is A068-QUADRATIC-CONTEXT-RANK-REFERENCE v1 with its accepted recovered C001 source. Only the ordinary influence bound is extended here, not the centered min(influence,1-influence) refinement.

The physical core after a star need not be unate. The example MAJ3(x1,x1*x2,x3) is nonunate and fails every fixed-order, fixed-orientation predecessor-antichain geometry. Thus this is a rank reference for a class beyond those physical one-order hypotheses. It is a narrow extension of the original packet, not a universal FEI claim.

We also independently reconstruct A079-SHARP-QUADRATIC-TWO-PHASE-COLLISION v1 at the same-full-physical-cube scope. This provides a genuine one-node C019 payment with both terminal phase entropies retained. It does not pay arbitrary unequal physical-cell collisions or deletion of the fresh data tag in our star geometry.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-14 02:33 UTC (the omitted middle of the initial large output was separately read), B14 STREAM_NOTES.md v2 dated 2026-10-11 23:25 UTC, own STATUS.md and LEARNED.md, and EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2. The lead's cyclic q=5,7 and point-edit target was completed in stage3; this run resumes the next signed-identification gap rather than repeating those fixtures.

Read own stage1 REPORT.md, Sections 1-4, and use its precise reference definition and accepted dependency. Read A079's runs/20261014T000722Z-account05-A079-correlated-auxiliaries/DERIVATION.md in full and CLAIMS.json. Its source statement hash is 938777233a0b7fffcfbb415d033d99989abf54fea66bda2d6e32cc6eda6f12ef; its proof hash is 4375d67f0fd79bd6cc987a94eeff97ad2ada7f92c70a62f1ab8149a35eef3b09. No author code was imported. A034's updated run 20261013T235407Z has only a .final marker locally; its REPORT.md is absent. That access failure is recorded, not treated as a new theorem or substantive failure. Its STATUS still proposes the collision ledger, so no such ledger is assumed.

The recovered regular-rank dependency remains C001/current-threshold-paper.tex SHA256 5d87f625fbadad4aa9841416712b8193a869fa9dffcb4e9c200d2f39a62e6a10, as source-bound in A068 v1 and accepted at scope by A088. This run adds no paper audit, literature novelty claim, web search or brain write. out/SOURCES.json pins read artifacts. Prior baseline acceptance is reused rather than restarted.

## complete derivation or exact first unsupported line

### 1. An exact two-face influence reserve

For distinct core coordinates i,j, put

    P_ij=sum_{S containing i,j} hhat(S)^2.

The j-derivative d_j h has values in {0,sigma_j}, where sigma_j is its fixed unate sign. Fix all other coordinates and call its values at the two i endpoints a,b. Parseval on the derivative gives

    Inf_j(h)=E_rest[(a^2+b^2)/2],
    P_ij=E_rest[(a-b)^2/4],
    Inf_j(h)-2P_ij=E_rest[a b]>=0.

The equality identifies a physical reserve: the probability that j is pivotal at both i endpoints. It holds for every unate h, without regularity. Regularity is needed separately to pay the rank reference. For nonunate h, a b can be negative, so this argument cannot be iterated automatically after a shear.

### 2. Invertible physical labels and the complete rank reference

Use bit indicators for spectral subsets. Character substitution gives the label transform T(S):

    T_j=S_j for a star center j;
    T_i=S_i xor S_j for a leaf i of center j;
    T_i=S_i for unused vertices.

Since no center is itself a leaf and leaves belong to one center, applying the same transform again returns S. Thus it is a bijection on all 2^q labels, preserving the uniform data cube. Expanding the actual Boolean function gives

    G=sum_S hhat(S) chi_{T(S)}(x) a_S(z),
    a_S=product_{i in S} a_i,
    Ghat(T(S),U)=hhat(S) ahat_S(U).

There is no coherent sum at a full Fourier index: the data label, including the fresh parity tag, decodes S. Therefore

    H(G)=H(h)+sum_S hhat(S)^2 H(a_S),
    I_z(G)=sum_S hhat(S)^2 I(a_S).

For a quadratic phase a_S, its squared Walsh law is uniform on an affine flat L_S of dimension r_S=rank B_S. Autocorrelation is a character on ker B_S and zero elsewhere, so Fourier inversion proves this fact. At least r_S physical Fourier coordinates vary fairly on that flat, giving H(a_S)=r_S<=2I(a_S). This is physical mean degree, not an invariant-energy replacement.

Index the latent core coordinates by the accepted desirability order. Let w_k be the spectral level mass of h and Z_k=sum_{|S|=k} product_{i in S} i^-2. Define

    R(T(S),U)=w_|S| [product_{i in S} i^-2 / Z_|S|]
                    *2^-r_S *1_{U in L_S}.

For each latent S the affine factor sums to one, the rank factor sums to one on a level, and the level masses sum to one. T is bijective, hence the whole reference is normalized and covers the entire G spectrum. Its expected cost is precisely the same latent data rank/level cost as in accepted A068 v1, plus sum_S hhat(S)^2 r_S. The recovered bound pays the former by C_reg I(h); the physical phase inequality pays the latter by 2I_z(G). No level, rank normalizer, branch prior or terminal core entropy is dropped.

### 3. Payment in output influence

A leaf physical spectral bit changes from S_i to S_i xor S_j, giving

    Inf_{x_i}(G)=Inf_i(h)+Inf_j(h)-2P_ij.

A center's physical influence is Inf_j(h); unused coordinates also keep their core influence. Control packets sum to one, so the formulas are unchanged by overlapping quadratic controls. Consequently

    I_x(G)=I(h)+sum_j sum_{i in L_j}[Inf_j(h)-2P_ij]>=I(h).

Combined with the complete-reference bound above, this proves the stated all-q/all-m theorem. Disjointness of the star vertices is substantive: if a leaf collects several centers, its indicator is a higher parity and the pair reserve alone no longer controls its weight.

### 4. An actual function outside physical one-order geometry

Take h=MAJ3, center coordinate2 and leaf coordinate1. Then G=MAJ3(x1,x1*x2,x3). Its second derivative equals +1 at (x1,x3)=(+,-) and -1 at (-,+), so no fixed orientation makes G unate. A direct Walsh transform has four coefficients of magnitude1/2, entropy2 and influence3/2.

There is also a short proof that no physical order has all predecessor pivotal fibers antichains. If coordinate1 is last, its pivotal support contains both x3 endpoints at x2=+, hence a comparable pair in every orientation. If coordinate3 is last, both x1 endpoints at x2=- are pivotal, again comparable. Thus coordinate2 must be last. If coordinate1 is second, at x2=+ it is pivotal for both values of its predecessor x3; if coordinate3 is second, at x2=- it is pivotal for both predecessor x1 values. Both cases fail. Exact enumeration of all6 orders and8 fixed orientations supplies explicit failing fibers in out/geometry.json. Even choosing an orientation separately on these failing full one-dimensional fibers cannot make them antichains.

The proof uses the invertible latent geometry and its two-face reserve to pay the rank reference. It does not silently reuse a physical predecessor-antichain estimate that the example violates.

### 5. Independent reconstruction of A079's actual two-phase collision

Let g0,g1 be actual quadratic signs on the same full physical n-bit cube and F(t,z)=g_t(z). Put a=(I(g0)+I(g1))/2, mu=E(g0g1), d=(1-mu)/2 and L=H(F)-(H(g0)+H(g1))/2. Direct Walsh transformation gives parent coefficients (ghat0(U)+ghat1(U))/2 and (ghat0(U)-ghat1(U))/2. The complete spectral law is normalized by Parseval, I(F)=a+d, and both terminal entropies remain in L's definition.

Write child affine Fourier support sizes M and RM, with R>=1 a power of4, and let u be the fraction of the smaller support in the intersection. Each intersection coefficient has the two masses (1+R^-1/2)^2/(4M) and (1-R^-1/2)^2/(4M). Summing their entropy and the two equal masses on every nonintersection atom independently yields

    L=2-u gamma_R,
    gamma_1=2,
    gamma_4=(9/8)log2(3)-1,
    gamma_16=(25/32)log2(5)+(9/32)log2(3)-2.

At any R, setting t=R^-1/2 gives
gamma_R=1+1/R+[(1+t)^2/4]log2[(1+t)^2/4]+[(1-t)^2/4]log2[(1-t)^2/4]+log2(R)/(2R).
Also L<=2 by the one-bit mixing entropy plus one-bit conditional selector entropy. Parseval gives |mu|<=u/sqrt(R).

If r_D is the polar rank of g0g1, then mu is zero or has magnitude2^-r_D/2, and |r0-r1|<=r_D<=r0+r1. For mu<=0, d>=1/2 and L<=4d. For mu=1, L=d=0. If mu=1/2, R=1 or4: R1 gives L<=4d; R4 forces u=1 and L=kappa/4, where kappa=12-(9/2)log2(3). If mu=1/4, R=1,4,16: respectively L/d<=4, L/d<=(8+kappa)/3<kappa, or L/d=(8/3)L16<75/16<kappa, with L16=4-(25/32)log2(5)-(9/32)log2(3)<225/128. Smaller positive mu gives d>=7/16 and L/d<=32/7<kappa. These exhaust all dimensions and prove L<=kappa d.

For the sharp whole bound, multiplying F by the selector character preserves entropy and a and reduces negative mu to |mu|. Each child pays entropy r_i<=2I(g_i), so H(F)<=2a+L. The ratio (2a+b)/(a+d) is bounded at the allowed minimum a or by its limit2, because its derivative has sign2d-b. At mu=1/2,R4 the minimum a=1/2 gives Cstar=(4+kappa)/3=16/3-(3/2)log2(3). The remaining rank cases give upper bounds12/5 (mu1/2,R1), 28/11 (mu1/4,R1), (32+kappa)/15 (mu1/4,R4), 481/176 (mu1/4,R16), and80/31 (smaller positive mu), all below Cstar.

At mu=0, rank sum>=4 gives8/3. Rank sum0 gives two disjoint characters, entropy2 and a>=1/2, hence ratio<=2. Rank sum2 gives one character and a disjoint affine plane, entropy3. If the character is nonempty then a>=1. Otherwise the plane excludes the origin: it has a fixed-one coordinate or at least three varying physical coordinates, so its mean weight is at least3/2 and a>=3/4. The ratio is then<=12/5. The |mu|=1 case is a single quadratic phase, possibly times the selector, with ratio<=2. Integer comparisons 3^5<2^8, 3^12>2^19 and5^10>2^23 imply 24/5<kappa<39/8, Cstar>44/15 and the L16 bound used above.

Equality is attained by g0=1, g1=(-1)^(z1*z2): a=1/2,d=1/4,H(F)=4-(9/8)log2(3). Thus the source theorem and constants hold at stated scope, with no repair supplied. With X=selector,Y=(z1,z2), its conditional entropy is2-(3/8)log2(3), exceeding2I_Y=1. The admitted distinct-label source (-1)^(x*t+t*z1*z2) restricts at x=0 to this actual witness. This is a real Boolean loss of conditional constant2, not an arbitrary unnormalized phase array.

The resulting certified C019 node payment is H(F)=L+(r0+r1)/2<=kappa d+2a. The sharper Cstar constant spends terminal rank slack once; it cannot be reused at descendants without a new argument. Here arbitrary unequal Fourier support sizes are covered; unequal physical partition cells and repeated collisions are not.

### 6. The precise remaining gap

A one-leaf star retains a fresh physical tag v: the two votes are x and x*v. Their spectral labels decode the two original votes. Fixing v merges the labels and creates exactly the signed two-row coefficients from stage3. The parent influence need not survive that deletion, and the inherited reference can cost one bit at zero output influence in the AND2 witness. The two-face reserve above prices retaining v, not deleting it.

First unsupported line: after deleting the tag with arbitrary nonconstant terminal cores, a cancellation-aware normalized output reference has cost paid by output influence using a single unused reserve. A079 handles two full-cube unit quadratic phases, not the unequal-amplitude regular-core packets of a general deletion. No uniform arbitrary collision closure, iterated-star closure, universal C018/C019/C020 payment or Boolean counterexample to FEI is claimed.

## executed validation with domain, arithmetic, commands and outputs

Before any computation, out/FROZEN_SPEC.json specified helper v1, exact domains, case counts, arithmetic, no symmetry reduction,45MB estimated memory,60-second pilot and180-second full cap with internal170-second guard. No memok-triggering job was used. Commands from A068:

    python -X utf8 runs/20261014T023317Z-account05-A068-antichain-beyond-one-order/code/check_stars.py --pilot
    python -X utf8 runs/20261014T023317Z-account05-A068-antichain-beyond-one-order/code/check_stars.py
    python -X utf8 runs/20261014T023317Z-account05-A068-antichain-beyond-one-order/code/check_geometry.py

The pilot passed24,577 assertions in0.128 seconds. The full job passed1,861,859 assertions in77.389 seconds:1086 unate-star cases (4,14,104 unate functions on1,2,3 bits times1,3,10 stars);40,960 MAJ3 controlled-star cases (all16^3 tuples of two-bit quadratic phases times10 stars);16,724 independently rebuilt quadratic mux cases (all ordered pairs for n=0,1,2,3 plus64 frozen n4 fixtures). The mux check found976 exact selector-payment equalities and68 nonconstant sharp whole-function equalities. This includes ordered pairs, constants and negative correlations. No source code was imported and no floating entropy was used.

The integer truth-table FWHT is independently compared to packet coefficients and direct physical edge counts. The pair reserve is compared to both-endpoint pivot counts. Quadratic packet flat ranks and normalized references are checked exactly. For controlled MAJ3 the original positive reference masses are27/49,27/196,3/49,1/4; their product exceeds2^-12, proving the base expected cost<3 by an exact integer comparison. Since I_x=3/2 and mean rank<=2I_z, every controlled fixture certifies the stronger complete cost bound Gamma<2I_x+2I_z.

For A079 review, entropy is represented exactly as a rational linear combination of log primes from squared integer Walsh coefficients. Identically zero margins are recognized symbolically, avoiding interval error at equality. Other signs use20 terms of the atanh series after range reduction to[1,2), with tail2t^41/[41(1-t^2)], outward division by the ln2 interval, then outward rounding to denominator2^72. The computed inputs to entropy and influence are actual Boolean truth tables. Finite review alone is not the all-dimensional theorem: the rank/overlap case proof in Section5 supplies that bridge.

The separate out/GEOMETRY_SPEC.json froze48 order/orientation cases with10MB estimate and60-second cap before running. It passed50 exact assertions in0.002 seconds, saving every failing pivotal fiber. Total full-run plus geometry assertions:1,861,909. Outputs are out/pilot.json, out/validation.json and out/geometry.json.

## proof dependencies and changed downstream conclusions

The new parity-star theorem depends acyclically on accepted A068-QUADRATIC-CONTEXT-RANK-REFERENCE v1 and its explicitly accepted recovered C001 source; the new two-face influence reserve is proved here. It does not depend on A079. Its proper-class extension is pending independent review by A070/A088/A094.

A079 v1 is independently reconstructed without a substantive repair and is recorded with its original statement hash and source-bound review verdict HOLDS_AT_STATED_SCOPE. The author remains its contributor; A068 is a reviewer. Shared-registry adoption is pending. This source now supplies a paid same-cube quadratic collision dependency to A034 and B14, without overstating physical-cell closure or substituting it into general regular-core packets. The narrow geometric extension and the source review are distinct outcomes, not two new broad universal candidates.

## one next mathematical action and independent reviewer

Take the single-leaf star and expose/delete its fresh tag. Derive the actual conditional signed packet law and output-reference reset cost, then use one terminal-core reserve to pay the first nonconstant unequal-amplitude collision. Start with an arbitrary regular-core pair, keeping both terminal reference costs; use the independently reconstructed A079 bound only when the actual terminal packets are unit quadratic signs on the same full cube. A070/A088/A094 can review the star extension; A079/A034/A092 can consume the source-bound review. No message is sent.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json are saved in this run, with code/, frozen specifications, checkpoint and exact outputs. out/SCHEMA_CHECK.json verifies exact protocol field sets, two-line STATUS and compatibility equality; out/RECEIPTS.json pins local hashes and sizes. STATUS.md is current; WORKLOG.md is appended and LEARNED.md records the exact reserve and limits. Files remain below20MB. No other-agent folder, shared registry, source tree, brain, git repository or external service was modified. Independent review of the new extension, supervisor collection, registry adoption and mirror verification remain pending.

Universal bridge: this stage advances C020 whole-set witness cost by extending the accepted complete rank reference to every vertex-disjoint parity-star geometry over a regular core with arbitrary overlapping quadratic controls, at the unchanged C_reg data/2 control price, even for a physical function admitting no one-order predecessor-antichain geometry. It also consumes a fully reconstructed actual collision payment from A079: C019 selector decrement<=kappa Inf_selector with both quadratic terminal entropies retained. The unpaid bridge is deletion of the fresh tag when regular-core packets have unequal amplitudes or physical supports; no influence-paid cancellation refund is yet proved there. The next single-tag deletion is the shortest route toward full FEI because it attacks the exact loss of spectral-label injectivity protecting the present reference while preserving the terminal debts and a single physical influence account.

