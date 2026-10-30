# A018 stage22: an original reference for arbitrarily wide shared-coordinate sources

Full FEI remains OPEN. A growing shared-coordinate source satisfies the rate4 cleaned original-reference contract at every physical restriction. This extends the previously certified five-bit source to arbitrarily many branches meeting at one physical coordinate. The analytic proof is below; independent review is pending. The new result concerns complete terminal costs. It does not pay a separate accumulated query-KL transaction account.

## exact target, quantifiers, hypotheses and units

All inputs are uniform independent physical 0/1 bits; chi_z=(-1)^z. All entropies and cross-entropies are in bits. Let g3 be negative exactly at000. For every finite integer r>=2 define

W_r(a,b_1,c_1,...,b_r,c_r)=product_{j=1}^r g3(a,b_j,c_j).

The coordinate a is shared, not copied. For EVERY partial physical assignment, let f be the restricted source, E its remaining essential coordinates (determined by actual edges), P its squared Fourier law on E, and R the marginal of the ORIGINAL P_Wr onto E. Then R is normalized, supports P, and

CE(P,R)<=4 I(f).

Cleanup means revealing all irrelevant remaining source coordinates and retaining every outcome, so the reference becomes its literal frequency marginal. It never means replacing the original law by the child's true law. Overall output sign changes are allowed, since squared spectra and influence do not change.

As an application, replace every five-bit E block in A019-UNBOUNDED-MIXED-ADAPTIVE-CLEANED-FRONTIER@1 by W_{r_j}, with arbitrary finite widths r_j>=2 on disjoint physical blocks. For all j>=5,k>=5, the SAME original balanced hierarchy and its literal debit U have initial margin>19/8 and complete expected terminal reserve>27/32 for every finite adaptive mixed padding/source policy with compulsory source cleanup at its admitted terminals. There is no bound on width or query count beyond finite dimension. Fresh u,mask,gate remain unqueried. Both q signs and all siblings are retained.

## sources actually read, revisions and theorem locators

Protocol2026-10-11-execution-v2 was read in full. Read current BOARD2026-10-27T10:15UTC, B04 lead v2, own STATUS/LEARNED/WORKLOG and stage21/20 results. The newer board supersedes the saved second-seed-query NEXT: A019's20261026T211700Z fleet04 run already handles unbounded mixed cleaned frontiers, and A016/A020 identify the missing ORIGINAL source supplier. Read their current reports and A019 CLAIMS; the original mixed-frontier statement hash is82362ae124b321eb8385a001db6c1a1f2d8f0f27790ef372e69c77d22e8b124f.

Read/indexed the designated campaign README,CURRENT_STATUS,registries,packet/status/actions,plan and supplemental campaign,claims,counterexamples,seeds,mapping,sources. Read the four local paper TXT versions; threshold38pp Proposition8.6 begins at line2425. No percolation theorem or new external literature claim is used. SOURCE_RECEIPTS.json pins actual source bytes and distinguishes reading from theorem verification. Current owner control remains FULL-FEI-ONLY. This explicit resumption governs despite historical campaign end dates.

The mandatory wake reported stale owner-model192.7h,state177.3h,dream49.7h; that warning was surfaced before relying on notes. No personal-context note is a mathematical premise. Brain/math-brain recall were read-only leads. The four legacy paper text extractions are not UTF8: their exact bytes are preserved and indexed through a lossless Latin1 mapping for navigation; no fresh paper theorem acceptance depends on that decoding. New research writes are confined to A018. The compiler was not admitted: memok returned1 with3.6GB physical/3.8GB commit free. No GPU,background job,git,mail,other-agent mutation or process intervention occurred.

## complete derivation or exact first unsupported line

1. ORIGINAL law. Put mu=2^-r. At a=1 the source is1; at a=0 it is a product of r two-bit point functions, each with mean1/2 and uniform squared spectrum. Therefore mean(W_r)=(1+mu)/2 and I(W_r)=(r+1-mu)/2. The full original coefficient at private frequency T!=empty and either a frequency has squared magnitude2^(-2r-2); the two T=empty squared coefficients are(1+mu)^2/4 and(1-mu)^2/4. These follow from physical branches, without independence of overlapping factors.

After projecting onto a plus ANY d private coordinates, the ORIGINAL reference is

R(0,empty)=(1+2mu+2^-d)/4,
R(1,empty)=(1-2mu+2^-d)/4,
R(e,T)=2^(-d-2) for T!=empty.

If a is projected out, it is instead

R(T)=delta_empty(T)/2+2^(-d-1).

Summing over all projected-out original frequencies proves both formulas and normalization, including d=0. They contain the ORIGINAL mu, not the new branch mean. Since r>=2, mu<=1/4; every displayed mass is positive. No denominator is canceled on a zero row.

2. All physical cylinders. If a is fixed1, cleanup leaves a constant: R(empty)=1 and CE=I=0. If a is fixed0, each original private pair restricts to a two-bit point function, a signed literal, or a constant. After cleanup the branch L is, up to sign, a product of n2 two-bit point functions and n1 literals. Put t=n1+n2 and d=2n2+n1. Its influence is t. For t=0 the cleaned law is a point mass with cost0. For t>=1 all original marginal masses are at least2^(-d-1), hence

CE(P_L,R)<=d+1<=2t+1<=3t<=4I(L).

Now let a remain essential. The a=0 branch again is such an L and the a=1 branch is1. Write b=E L. Then I(f)=(1-b+t)/2. Its two private-empty true masses are(1+b)^2/4,(1-b)^2/4; their total is(1+b^2)/2. Total true mass at nonempty private frequencies is(1-b^2)/2, with original reference code length exactly d+2. If n1>0 then b=0; otherwise b=+/-2^-t.

For t>=2, |b|<=1/4 and d<=2t. Both original private-empty reference masses are at least1/8, so their code lengths are at most3. Thus

CE(P,R)<=3(1+b^2)/2+(d+2)(1-b^2)/2
        <=t+5/2+(1/2-t)b^2.

Subtracting this from4I gives

t-1/2-2b+(t-1/2)b^2 >= t-1 >=1.

Every sign is covered. This is an elementary rational comparison, not an extrapolation from the finite census.

The exceptional cases are explicit. A single literal has b=0,d=1, so CE<=3<4I=4. A single two-bit point function has d=2 and b=+/-1/2. Its original empty masses satisfy R(0,empty)>=5/16>1/4 and R(1,empty)>=3/16>1/8. Consequently the positive-mean case has

CE< (9/16)*2+(1/16)*3+(3/8)*4=45/16<3=4I,

and the negative-mean case has CE<53/16<5=4I. If t=0, L=1 makes the entire source constant and a must be removed. L=-1 gives a signed chi_a, with reference mass(1-mu)/2>=3/8 and CE<2<4I. These exhaust all cylinders, including constants and phase changes. This proves the all-r source contract.

3. A ghost cost independent of width. If only a=1 is revealed and all private coordinates are left, the true source is constant but the original projected mass at the empty set is alpha_r=(1+4^-r)/2. Its exact uncleaned ghost invoice is log2(2/(1+4^-r)), strictly between0 and1. There are2r irrelevant coordinates. After actual cleanup, the original reference has empty mass1 and cost0. At r=2 this is exactly A016's17/32 ghost row; at r=3 it is65/128. Charging every private coordinate independently loses this width-independent bound. This calculation does NOT claim that arbitrarily many separate ghost-bearing blocks are affordable without cleanup.

The previous ghost calculation has a sharp scope limit. Fix a=0; leave the first pair free; for j>=2 fix b_j=1 but leave c_j unqueried. The actual source is just the two-bit point function, with I=1 and four squared Fourier masses1/4. There are r-1 irrelevant coordinates within this ONE connected block. With d=r+1 remaining private coordinates, its original uncleaned reference is R_unc=delta_empty/2+U_d/2. Thus

CE_unc=(1/4)log2[2/(1+2^(-r-1))]+(3/4)(r+2).

Cleaning those ghosts gives R_cl=delta_empty/2+U_2/2 and CE_cl=(1/4)log2(8/5)+9/4. Their difference is

D=(3/4)(r-1)+(1/4)log2[5/(4(1+2^(-r-1)))] >(3/4)(r-1).

Consequently no constant per CONNECTED block bounds all ghost invoices in this enlarged family. For every r>=4, CE_unc>3(r+2)/4>4I. The first supplied physical witness is r4: its four supported reference masses are33/64,1/64,1/64,1/64. CE_unc>4 is exactly their product<2^-16, or33<256. This is an exact original-reference route obstruction, not an FEI counterexample. The source contract in section2 survives because it requires actual cleanup. A016's finite E block constant16/7 must not be transplanted to these unbounded connected blocks.

4. Transfer to the SAME balanced owner. Let G=product_{l=1}^j W_{r_l}, j>=5,r_l>=2, on disjoint blocks. Then its mean mu_G=product_l(1+2^-r_l)/2 <=(5/8)^j<1/8. At every cleaned source cylinder both actual spectra and ORIGINAL projected references tensor over these blocks, hence CE(P_g,R)<=4I(g), with no within-block tensor assumption.

Use k>=5,rho=2^-k,V=the ORIGINAL padding point,A=1_V(1-G)/2,p=rho(1-mu_G)/2,h=chi_u off A and chi_q on A. Let F=1 at fresh gate0,h*w at gate1, w=[-1,1,1,1] on two fresh bits. Supply ORIGINAL Qh=(Ph+delta_q)/2 and QF(e,T)=[Qh(Tcore)Pw(Tmask)+delta_empty(T)]/4 for EACH gate frequency. Every descendant inherits only a frequency marginal of this fixed normalized QF. Retain exactly A019's U=Lq+Econv:

Lq=log2((9+p^2)/8)/2+(p^2/8)log2((9+p^2)/(1+p^2)),
Econv=(1+p^2/4)[1-h2((1+p/2)^2/(2(1+p^2/4)))]/2.

Here0<=U<5/8 by the source's elementary logarithm/chi-square bound at p<1/64; no new debit is substituted.

After q and any mixed physical padding/source history, at an active leaf put kprime=remaining padding width,rho_leaf=2^-kprime,nu=E g,a_leaf=rho_leaf(1-nu)/2. Denote rho_leaf by s in the formulas below. Let L replicate source measures over all2/s remaining padding/u frequencies. Literal laws are

Pc=(1-2a_leaf)delta_u+(s^2/4)L[P_g+(1-2nu)delta_empty],
Qc=(1-2p)delta_u/2+delta_empty/2+(rho*s/8)L[R+(1-2mu_G)delta_empty].

The first is a signed algebraic decomposition when a_leaf>1/2; it is never used as a positive mixture. Retain coincident principal/empty atoms. Their reference floors are>1/4 and>=1/2, so their combined CE is<=2. Nonempty source rows contribute exactly

(s/2)[(1-nu^2)(k+kprime+3)+sum_{T!=empty}P_g(T)log2(1/R(T))].

Other empty-source rows have reference floor>3rho*s/32 and code length<k+kprime+4; all nonprincipal mass is<=2s. Thus CE_core<=2+2s(k+kprime+4)+(s/2)CE(P_g,R). The complete outer gate/mask code gives CE_F<=CE_core/2+3. Actual physical edges, for either q sign sigma, give

4I_F=6+2(kprime-1)a_leaf+s I(g)-sigma*a_leaf >=6-3s+s I(g).

Consequently the full terminal reserve satisfies

4I_F-CE_F-U >=2-U-s(k+kprime+7)+s[I(g)-CE(P_g,R)/4]
             >=2-U-s(k+kprime+7).

Failed-padding leaves have s=0 and retain the original principal floor. For EVERY finite adaptive physical leaf partition, s=Pr(V|leaf), so E s=rho and E(s*kprime)<=k*rho. This proves

E[4I_F-CE_F]-U >11/8-(2k+7)2^-k >=27/32.

The final bound holds since(2k+7)2^-k decreases for k>=5. Source cleanup is mandatory in the source-contract step. All outcomes,ghost cleanup children,old U and complete references remain. This is a terminal-functional proof; it makes no assertion of an additional accumulated query-KL transaction being free.

The root itself is eligible. The source contract includes the unrestricted root, so H(G)<=4I(G). The original code has CE_root<=H(h)/2+7/2, while H(h)<=h2(2p)+2p(k+2)+(rho/2)H(G). Hence4I_root-CE_root>=5/2+(k-2)p-h2(2p)/2+rho[I(G)-H(G)/4]>19/8. Here h2(2p)<h2(1/32)<1/4; the latter follows from31^31>2^152. This prevents inserting a hidden ineligible initial supplier.

First unsupported UNIVERSAL line: construct an analogous influence-priced ORIGINAL reference for a general indecomposable Boolean core with a necessary useful continuation, or pay its excess from one unused original account. The star source has a distinguished shared coordinate whose fixing separates all pairs; arbitrary overlapping cores need not. Nothing here proves H<=4I for every Boolean function, nor does an expected terminal margin alone pay all accumulated query-KL transactions.

## executed validation with domain, arithmetic, commands and outputs

Frozen specifications precede each job. Pilot: ALL243 assignments at r2,2471 exact assertions PASS,0.059s. Main: ALL2430 assignments at r2,3,28702 exact assertions PASS,0.894s. Every restricted truth table is constructed from physical bits, essential coordinates from edges, and original R from the full original spectrum. Exact original-row formulas, Parseval and spectral/edge influences are checked. Every rate4 sign is an integer-power comparison, with source truths,references and regenerable certificate hashes saved in SOURCE_CERTIFICATES.json. No floating signs or symmetry reduction.

Independent representation audit: 19160 exact checks on ALL2430 saved assignments, using direct character sums,direct edges and one common original denominator, with no first-checker imports; 4.852s. It reconstructs physical truths and ORIGINAL marginals before rechecking each integer certificate. These are two implementations by this author, not independent-agent acceptance. The r2 subset independently reconstructs the unchanged finite source contract within A016-ADAPTIVE-OVERLAPPING-BLOCK-CLEANUP-AND-PADDING-CONTINUATION@1 only; it does not accept its other clauses.

The additional frozen ghost guard checks actual r2,3,4 physical parents/restrictions and their complete normalized references, plus63 fixed rational formula guards. Result: 142 exact assertions PASS in0.04s. It certifies the uncleaned rate4 failure by33<256, without a numerical logarithm. This extra job challenges the cleanup hypothesis; r4 is a deliberately frozen witness, not automatic dimension escalation.

Commands: python -B -X utf8 code/check_windmill.py --pilot; python -B -X utf8 code/check_windmill.py; python -B -X utf8 code/audit_certificates.py; python -B -X utf8 code/ghost_guard.py. Frozen memory estimate90MB; no job needs300MB. WindmillScalar.lean preserves the rational key inequality, but the fresh memok exit1 prevents a Mathlib compile. No Lean-checked rung is claimed. Rung: analytic proof plus exact finite certificates, new independent review pending. No external novelty claim is made.

Checks that could fail were challenged: one physical shared coordinate instead of copies; original mu versus child b; physical sign changes; constants; all t0/t1 exceptions; projected-out fixed bits versus ghosts; nonempty support; negative1-2a_leaf; full terminal reference normalization; and all-outcome posterior averaging. Removing cleanup has an actual positive-cost zero-influence counterexample in section3. Removing disjointness BETWEEN source blocks invalidates the tensorization step and is not allowed. No infinite limit or sum/integral interchange occurs.

## proof dependencies and changed downstream conclusions

The source contract and ghost formula are proved here directly. The application reconstructs the general-source clause of A019-UNBOUNDED-MIXED-ADAPTIVE-CLEANED-FRONTIER@1 from its explicit laws. Its source-byte hash is pinned; A016/A020's prior independent acceptance is source-reported, not newly certified by a status field. A016's finite r2 source contract receives a separate strictly scoped independent reconstruction without repair. New arbitrary-width source/application requires independent review. A094's query-KL objection remains in force for a different transaction interpretation; no claim silently crosses that boundary.

## one next mathematical action and independent reviewer

A016/A019/A020 should independently reconstruct the all-width projected-law formula,the t1 sign cases,and the unbounded within-block ghost invoice. Next test a connected source with TWO shared selectors and private branches coupled across both, seeking an all-cylinder ORIGINAL-reference contract or an exact failed cylinder; price actual cleanup, not the number of connected blocks. Preserve old U,both full terminals and query-KL scope. Do not repeat query-count tests or reuse the completed star contract as an arbitrary-core assumption.

## actual persistence receipts or precise save blocker

The four protocol files,code,finite certificates,frozen specs,source receipts and validation outputs are saved locally. PROGRESS and PACKET_DELTA are byte-identical with packet_ids[A018]; STATUS has two lines and rolling facts/worklog are updated. PERSISTENCE_RECEIPTS.json verifies exact schema fields,statement hashes and file sizes/hashes. Supervisor copying,registry adoption,remote mirrors and independent acceptance remain unverified. No git/brain write or outgoing message is performed; these remain the supervisor's route. No existing work was stopped and no detached job was launched.

## Universal bridge

This stage advances the ORIGINAL-source side of C024/C019 from one finite five-bit overlapping block to all widths of a physically connected shared-coordinate source, and supplies that source to every mixed cleaned frontier under the SAME original owner with reserve>27/32. It also refutes a width-independent per-connected-block ghost allowance by an actual I=1 family with invoice>3(r-1)/4. The proof replaces finite enumeration by an all-cylinder dimension-independent reference bound; source widths and shared-coordinate incidence may grow without bound. General interacting cores and accumulated-query-KL payment remain unpaid. The shortest NEXT is a two-shared-selector source with coupled branches and actual cleanup pricing: it tests whether original-law payment survives the first failure of one-coordinate separation, rather than enlarging an already closed finite query count.
