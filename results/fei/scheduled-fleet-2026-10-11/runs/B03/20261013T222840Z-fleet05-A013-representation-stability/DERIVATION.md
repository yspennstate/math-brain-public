# One shared data bit: coherent reference and a paid physical selector

All logarithms and reference costs are in bits. Author proof, pending independent reconstruction. This continues A013's compensated representation packet and consumes the exact gap of A012-DISJOINT-PRIVATE-MUX-ADMISSION@1. The lead's old monotonicity direction remains false by the preceding stage; this is a paid replacement reference, not a claim that its original queue's L,S,R decrease.

## 1. Hypotheses and calibration

Let y be one uniform physical bit, A and B disjoint private coordinate blocks, and z a fresh selector. Let g(y,A),h(y,B) be arbitrary Boolean signs; either branch may ignore some coordinates. Set F=(g+h)/2+z(g-h)/2. Supply normalized references Rg,Rh positive on the respective squared Fourier supports, with finite costs cg,ch. No bound on these terminal costs is assumed.

For g let a0=E g and a1=E yg; for h let b0=E h,b1=E yh. These are precisely the two shared-only Fourier coefficients, obtained from two conditional means per branch, not an arbitrary spectrum oracle. Calibrate Rg so its atoms empty and {y} have masses a0^2,a1^2. Its other atoms keep their original conditional law, multiplied by vg=1-a0^2-a1^2. If vg=0, the private remainder is zero. Define Rh similarly. KL disintegration over the three categories (empty, {y}, private remainder) proves calibration cannot increase CE. Its removed cost is the categorical divergence between the true and old category masses. Full conditional private debt remains.

## 2. Fixed complete output reference and exact terminal debt

For t=0,1 and selector frequency u=0,1 set

Q(u,t shared only)=(a_t+(-1)^u b_t)^2/4.

For a set T meeting A but not B use Q(u,T)=Rg_cal(T)/4; for a set meeting B but not A use Rh_cal(T)/4. Sets meeting both private blocks receive zero. All shared-frequency signs, selector bits, private ownership labels, and failure/normalization costs are included. Shared mass is (||a||^2+||b||^2)/2; private masses are vg/2 and vh/2, so Q sums to one. It is finite and fixed before sampling. Shared cancellation atoms of mass zero also have zero true mass.

Fourier expansion gives the identical formula for P_F with true private core probabilities in place of calibrated references. Thus

D(P_F||Q)=[D(P_g||Rg_cal)+D(P_h||Rh_cal)]/2,
CE_F=[cg_cal+ch_cal]/2+Delta,
Delta=H(F)-[H(g)+H(h)]/2=B_z+JS_z.

These identities retain both entire terminal bills. No core spectrum has been set equal to a free reference; only the two explicitly accessible shared-only coefficients are exact. Inf_z(F)=d=(1-E_y alpha(y)beta(y))/2, where alpha=E_A g, beta=E_B h. Every other physical coordinate has influence equal to half the sum of its influences in the two branches, including y once with this summed charge. Consequently I(F)=[I(g)+I(h)]/2+d.

For an explicit label ledger, the six sector masses are the four shared (u,t) probabilities and vg/2,vh/2 for private ownership. They coincide with the true sector masses. Their entropy is at most log2(6), with zero sectors omitted. In a private sector draw the selector-frequency bit uniformly (cost one bit), then the calibrated private conditional reference. Thus complete CE is H(sectors)+(vg+vh)/2 plus half each private conditional CE weighted by vg or vh. This chain rule includes all labels; the paid Delta comparison retains the corresponding terminal labels and does not try to charge a fixed log2(6) to a vanishing influence.

## 3. A common character exposes the one-bit Boolean constraint

For each value of y, choose c(y)=sign(alpha(y)+beta(y)), choosing +1 at a tie. This is an instance-fixed sign on one bit, so it is a constant or a signed character. Multiplying g,h and F by this same c simply translates all Fourier indices: B_z,JS_z,Delta and d are unchanged. This translation is used to prove a scalar bound, not to replace the output function or its physical y influence.

Put e(y)=(1-c(y)alpha(y))/2, f(y)=(1-c(y)beta(y))/2, s_y=e(y)+f(y). The choice of c gives 0<=s_y<=1. Conditional independence of the private cubes gives

d=E_y[e(y)+f(y)-2e(y)f(y)] >= E_y[s_y-s_y^2/2].

Let eta=E_y e, xi=E_y f, s=eta+xi. Then 0<=s<=1 and the translated shared empty coefficients are mu=1-2eta,nu=1-2xi. If s<=1/2, the TWO equiprobable row masses imply E s_y^2<=2s^2, so d>=s(1-s). If s>=1/2, s_y^2<=s_y gives d>=s/2>=1/4. This two-row estimate is the crucial use of one shared physical bit.

## 4. Erasure payment B_z<=4d

For any residual Fourier index T, the two parent-frequency masses are (a_T+b_T)^2/4 and (a_T-b_T)^2/4. Write E(A,B)=(A+B)h2(B/(A+B)). For the translated empty index,

E((mu+nu)^2/4,(mu-nu)^2/4)<=|mu^2-nu^2|/2=2|eta-xi|(1-s).

Here h2(t)<=2sqrt(t(1-t)); a full elementary verification is given in REVIEW_A012.md. Every other index has erasure at most its total mass, so together they contribute at most [(1-mu^2)+(1-nu^2)]/2. With t=|eta-xi|<=s,

B_z<=2s-s^2-t^2+2t(1-s).

For s<=1/2 this concave quadratic increases in t on [0,s], yielding B_z<=4s(1-s)<=4d. For s>=1/2 use the general binary bound B_z<=1 and d>=1/4. The case d=0 is included: both branches are the same shared character and no private remainder survives.

## 5. JS payment and total selector constant

The scalar inequality ((1+x)ln(1+x)+(1-x)ln(1-x))/2<=1-sqrt(1-x^2) follows by differentiating: x/sqrt(1-x^2)-atanh(x) has nonnegative derivative and vanishes at zero. Applied separately to actual child coefficients u_T,v_T, it gives

JS_z<=(1/(2ln2))sum_T(|u_T|-|v_T|)^2
     <=(1/(2ln2))sum_T(u_T-v_T)^2=(2/ln2)d.

Therefore Delta<=(4+2/ln2)d<7d (strict when d>0, using ln2>2/3). The complete reference satisfies

CE_F<=[cg+ch]/2+(4+2/ln2)Inf_z(F).

If the supplied terminal references obey CE_g<=K I(g),CE_h<=K I(h), this yields CE_F<=max(K,4+2/ln2)I(F), with one use of every physical influence. The disjoint-private case is included by ignoring y; thus the selector constant also improves A012's stated 6+1/ln2 upper bound. No optimality is asserted.

## 6. Physical restrictions, tensor, activation and structural admission

Restricting y makes the two private branches disjoint. Restricting a private coordinate keeps at most this one shared bit. Restricting z selects one branch. All reference parameters must be recomputed from actual conditional means, with the incoming restricted branch references retained; parent CE payment alone does not supply a bound for arbitrary descendants. If the branch references come from hereditary structural certificates this recomputation is legitimate and their costs remain certified.

For explicit positive-cell covers, attach z=+1 to each positive cell of g and z=-1 to each positive cell of h. The cover has N=N_g+N_h gates and one added selector literal per gate (N added literal incidences); it uses only the one new physical selector z. Regard each conjunction as one regular threshold gate (M=1). A branch cell on t private bits plus y has density and clipped rarity pi=2^(-(t+2)) after attaching z. Feasible uniform gate weights lambda=1/N give original independent-root odds pi/N, root probability pi/(N+pi), and Lambda=sum_l log2(1+pi_l/N). Under any physical restriction delete inconsistent cells and remove all fixed literals from survivors. A surviving density doubles for each removed literal; for a remaining nonconstant conjunction this density is at most 1/2 and equals its clipped rarity pi. A fully satisfied zero-literal clause makes the child constant +1; no survivors makes it constant -1. Every constant child uses the point-mass vacuum reference, with no root cost, also when its surviving nonconstant clauses cover the entire cube. For nonconstant children, replace lambda by 1/N_child to give each root pi_l_child/(N_child+pi_l_child). No normalization contraction is asserted. The coherent spectral reference above is a different, explicitly paid replacement; its label/sector probabilities are Q itself, not these independent queue root probabilities.

For opposite shared-literal point activations G=1+A_r(g-1),H=1+B_s(h-1) with disjoint fresh private controllers and one common data y, selector z chooses G or H. Their support intersection is still at most y. A095's biased activation transfer, independently reconstructed in REVIEW_A012.md, and this interface yield

CE_F <= [p CE_g_cal+q CE_h_cal]/2
       +3[rp(1-Eg)+sq(1-Eh)] +(4+2/ln2)Inf_z(F).

This pays r,s controls and z once and retains both weighted terminal costs. Fresh activation at r=0 is simply the unchanged branch. Disjoint products tensor complete references and add cost/influence; sign flips preserve spectra. A finite literal/constant grammar allowing these operations and fresh-selector mux whose child support intersection has size at most one has complete reference CE<= (4+2/ln2) I. This statement uses the activation bound 6 below the new selector constant. It is hereditary under all physical restrictions by induction on the actual syntax. Arbitrary core terminals retain their supplied CE, with no automatic admission. Rarity cannot insert a nonmember opaque seed: fixing active controls and other tensor blocks recovers that seed, as in A012's audit. We assert no original-queue L,S,R bound for this grammar.

## 7. Sharp scope obstruction at a growing shared block

The dimension-free selector surcharge does not extend to arbitrary shared blocks, even with exact terminal references. Let m>=4 be even, g(Y)=b_m(Y) the quadratic bent sign, and h equal g except its value at zero is flipped. Let F=z?g:h. Physical selector disagreement d=2^-m. Every g coefficient has magnitude 2^(-m/2), and every difference (g-h)hat/2 has magnitude 2^-m. Thus writing a_T=(g+h)hat/2 and b_T=(g-h)hat/2,

|a_T|>=2^(-m/2)-2^-m,
(a_T^2+b_T^2)/b_T^2 >= (2^(m/2)-1)^2+1 >=2^(m-1).

The b-frequency contribution alone gives B_z>=sum_T b_T^2(m-1)=(m-1)d, and Delta>=B_z. Hence no fixed C can bound this interface by C d uniformly in shared width. Already m=6 certifies B_z>4d. This is an actual Boolean selector family and a local transfer obstruction, not an unbounded H/I family. It explains why the two-row character argument cannot be silently used at arbitrary shared width.

## Exact remaining line

The resolved interface is one shared physical data bit. The first unsupported extension is an influence-owned coherent-reference transfer for two or more shared bits that uses a paid common nonlinear Boolean phase or other grouped support reserve, rather than charging the selector alone. For growing shared width a selector-only constant is rigorously impossible. The shortest next action is to expose the first nonlinear common phase at two shared bits, keeping its inherited spectrum, calibration debt, actual root changes and both terminal costs in a single reserve.
