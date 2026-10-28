# Parallel affine cosets: actual parity inputs, same original quota

Bits; actual Boolean truth tables on uniform independent physical inputs. Full FEI OPEN. The new result extends the A076v10 supplied-source history account from two points to two positive-dimensional parallel affine cosets, without a quota depending on their number of physical points. It uses A076v10's explicit additional ORIGINAL carrier quota96I0; the old bent-profile donor alone is NOT asserted to pay everything. Independent full-chain review remains pending.

## 1. Actual construction and ALL added physical influence

Let d>=5 be odd, take B=[Id|P] over F2 with m>=1 extra columns, and write shared physical bits as(x,z) in F2^d times F2^m. Set s=x+Pz. On a disjoint uniform private cube take arbitrary correlated Boolean profiles V,W. Start with central majority h(s), positive at weight<=d/2, and replace its values at s=0,e0 by V,W. Call this base function F0(s,y); the actual physical Boolean function is

 F(x,z,y)=F0(x+Pz,y).                            (1)

The two edit events E0,E1 are disjoint parallel affine cosets, EACH of size2^m, density e=2^-d. No formal spectral law substitutes for this truth-table definition. The map s is uniform because x is uniform. Fourier expansion gives

 Fhat(B^T a,T)=F0hat(a,T), all other rows zero.

B^T is injective. Consequently H(F)=H(F0), INCLUDING all private labels and the empty row. Physical influence is EXACTLY

 I_xi(F)=I_si(F0), I_yj(F)=I_yj(F0),
 I_zj(F)=Pr[F0(s,y)!=F0(s+P_j,y)].              (2)

Thus I(F)=I(F0)+sum_j directional_disagreement(P_j). Every new input's influence is nonnegative and explicitly counted. Coding can never create a larger H/I ratio by omitting those inputs. These root identities alone do NOT prove the history theorem below.

## 2. The complete mean bank uses CURRENT CODE RANK

After an arbitrary physical restriction, let the remaining shared columns be b_i, offset a, and r=rank{b_i}. The syndrome is uniform on a+span{b_i}. Each feasible target0/e0 has conditional mass p=2^-r, even though its physical fiber may contain many points. A target outside that affine image is dead. In quotient coordinates the surviving events are zero, one or two DISTINCT points; when both survive an invertible quotient change sends their difference to the first basis vector. This relabels Fourier rows and preserves all entropies. Let h_v be the ACTUAL coded carrier cofactor and use the actual remaining restricted private profiles.

Put U=p sum_live H(profile), R=r p sum_live Var(profile), and Xi=p sum_nonempty k(Vhat,What) if both targets live, otherwise0, with k=[g(a+b)+g(a-b)]/2-g(a)-g(b), g(t)=-t^2log2(t^2). The old collision bound -4p<=Xi<=0 is unchanged. Let E be the entropy sum of the COMPLETE empty-private Fourier sector of the actual physical function. Define

 Z=E+R-p sum_live g(mean profile)+1.

Direct quotient Fourier expansion proves EXACTLY

 H(F_v)=U+Xi+R+Z-1.                             (3)

This is the point identity with quotient rank r, NOT the number of remaining physical inputs. All physical null Fourier rows are retained as zeros. E>=0, R>=0, max g<1, and p times the number of live targets<=1 give Z>=0 at every descendant, including dead events and constants. The constant1 is retained on EVERY actual branch.

## 3. Physical query geometry and SAME collision owner

Keep the original unused B0>=4e after FIRST4e and oldD0, and C=(B0-Xi_root)/e. While both targets survive set K=pC+Xi. There are exactly three possible physical shared-query geometries:

* If removing a column preserves rank, both actual children have the same affine syndrome image as the parent. Their Fourier squared masses differ only by row labels; H,U,R,Xi,Z,K are unchanged. Actual query influence may be positive and is counted by(2); no false zero-influence claim is made.
* If rank drops by one and both targets lie in the same half-image, their mass doubles on that child and both die on its sibling. K and Xi are harmonic across both children. The true nonconstant carrier entropy on the dead sibling remains in E,Z,H.
* If rank drops and the targets separate, FREEZE K_parent in BOTH children and every later descendant. Xi_parent<=0 and both child Xi=0, so Delta Xi<=Delta K=0. The frozen source is not discarded when a later event dies.

With only one target live, K is already frozen; with no targets before separation it is0. Private queries preserve code geometry and satisfy Delta Xi=Delta K. The quotient representation proves the inherited private price12 with R based on rank (arbitrary carrier and means); no physical private influence is lost, since I_y=p sum_live I_y(profile).

Consequently at EVERY physical node

 Delta H<=Delta U+release_R+Delta K+Delta Z.      (4)

The source-density bookkeeping mass p is harmonic until separation and frozen in both separating children. It gives K>=0 and E K_terminal>=B0-4e at every finite stopping frontier, with ORIGINAL physical reach. No new descendant donor is issued. Telescoping(4) retains all complete profile and wrapper terminal spectra.

## 4. Admission after the THREE already booked transactions

Define J={i!=0: row_i(P)=0}. Assume |J|>=3 when three old shared transactions are requested. The old prefix may have at most three distinct shared queries x_i with i in J, with arbitrary private interleavings/early guard and stopping. These reveal the actual original syndrome coordinate s_i=x_i. The remaining code stays surjective onto the corresponding coordinate cofactor. Thus the A076v9/A077/A078v3 old prices5,15,38 apply EXACTLY, as does the private price12. Let L be their pathwise shared debit, never erased; 0<=L<=58.

At this prefix every actual coded carrier cofactor is a Fourier-label lift of a symmetric threshold. Let I0=d binom(d-1,(d-1)/2)/2^(d-1)>=1, the ORIGINAL uncoded majority influence. The A076v10 threshold input H(h_v)<=9I0 is inherited with its external-paper dependency, not newly proved by finite tests here.

Crucially, for an affine coset E of conditional density p and rank r, its indicator has2^r Fourier rows of magnitude p. Therefore ||hat(1_E)||_1=1, independently of its physical fiber size. The complete mean-sector translation from the two cosets has Fourier l1 norm<=sum_live(1-mu)<=4. Since |g'|<=6 on[-1,1], |E-H(h_v)|<=24, R<=1 and the terminal subtraction is nonpositive. Therefore the SAME point bound holds:

 0<=Z<=H(h_v)+26<=35I0.

Allocate ONCE Q=96I0 at the ORIGINAL source, distinct from the original private bent allocation. Original physical x influence of F is at least I0 by the base edited-majority edge calculation; the added parity influences in(2) only increase it. At the prefix frontier set

 Lambda=Q-L-Z>=3I0                              (5)

and freeze Lambda on every later actual branch. It satisfies L+Z+Lambda=Q exactly, retaining all old bookings. After admission the suffix may query ANY remaining physical shared/private input, including arbitrary parity columns, oblique syndrome restrictions, separators and all guard/padding variables, and may stop anywhere. The carrier need no longer be a threshold; Z>=0 in section2 suffices. Combining the old prefix and(4),

 H(F_root)-E H(F_leaf)+E(R_leaf+K_leaf+Z_leaf+Lambda_leaf)
 <= U_root-E U_leaf+R_root+B0+96I0+12P_private,prefix. (6)

Expected Lambda>=3I0, and expected K>=B0-4e. This uses the SAME original allowance and the SAME diminished collision owner throughout. It asserts no arbitrary coded-prefix admission: a prefix exposing oblique syndrome constraints before admission lacks the stated hereditary threshold envelope and is outside(5).

The actual donor is V=y*bent_k(z), W=y[1-2*1{z=0,x1=...=xm=0}], even k>=4,m>=2 (padding m is distinct from the number of code columns). H(V)=k,I(V)=k/2+1 INCLUDING guard. Its single split5eI(V)=eH(V)+S has S=e(3k/2+5). Preserve FIRST4e and oldD0; B0=S-D0-4e is admitted if D0<=S-8e. The k4,padding2,oldD0=e fixture still has B0=6e and guaranteed2e remaining, before and after coding.

## 5. Universal obstruction of the l1 method

The gain is dependence on TWO affine masks rather than their2^(m+1) physical points. A universal extension still needs an influence-controlled non-affine mask budget or a different cancellation-sensitive mean-sector estimate. A plain inequality ||hat(1_E)||_1<=C I(1-2*1_E) is FALSE: take E where a canonical quadratic bent sign b on even k bits is+1. Its indicator has algebra norm (1+2^(k/2))/2 when Eb=+2^(-k/2), while I(b)=k/2. Indeed its empty coefficient is(1+2^(-k/2))/2, and each of its2^k-1 nonempty coefficients has magnitude2^(-k/2)/2. This exponential/linear separation is an ACTUAL Boolean mask, not a formal spectrum. It refutes only this sufficient l1-payment route, not FEI. The exact first unpaid universal line is a replacement sensitive to squared spectral mass/physical boundary, while retaining Q, old bookings, original K and both full terminals. Arbitrary original carrier quota and arbitrary inherited core/terminal FEI admission remain unpaid.
