# Sharp relative-odds envelope fits the old full terminal reserve

All entropy/KL/CE are in bits. Author proof, exact checks and external review are distinguished. Full FEI remains OPEN. Same rate21/4, same original tangent/core prefix, same old1/64 debit and first shape charge as A027@9.

## 1. New scalar improvement of the consumed A029 envelope

For k in[0,1], lambda in[1/2,2], put ell=lambda*k/[1+(lambda-1)k]. Endpoints are fixed. Binary KL is

 d(k,lambda)=log2(1+(lambda-1)k)-k log2(lambda).

For k>0, ln(1+x)<=x implies d/k <=[lambda-1-ln(lambda)]/ln2. This convex function of lambda is largest at an endpoint. Its endpoint2 value exceeds its endpoint1/2 value because ln2<3/4. Consequently

 0<=d(k,lambda)<=c_* k,  c_*=1/ln2-1 <4/9.       (1)

The coefficient c_* is SHARP for arbitrary binary rows: at lambda2 and k->0, d/k->c_*. No optimality over actual full Boolean spectra is claimed. The strict rational majorant follows from the first3 positive atanh terms:

 ln2>2/3+2/81+2/1215=842/1215>9/13,

so c_*<4/9. Also ln2<25/36<3/4 using the first term and its geometric-tail bound. This analytically improves A029@4 section7's valid but looser1/2 envelope. It does not correct an error in that source.

## 2. All mixed histories, same original source/controller account

Consume/reconstruct A029@4 sections1,7-10, with A028@9's exact phase-channel accounting. For a disjoint physical binary mux, let T=W+gamma Da be the supplied ORIGINAL canonical source/controller KL account and S=Z+gamma Cvac>=0. References inherit through their OWN source/controller phase channels. Canonical full output KL is Dstar=T-S. At every occupied data row prescribe ANY adaptive lambda_t in[1/2,2], keeping the inherited nonempty controller shape and data marginal. The EXTRA row cost is C_v=sum_t q_t d(k_t,lambda_t). Formula(1) proves

 C_v<=c_* eta_v<=(4/9)eta_v (strict at the second comparison when eta_v>0),
 eta_v=sum_t q_t k_t=gamma Var(a).                 (2)

eta is a nonnegative physical supermartingale. DATA leaves it harmonic because gamma is harmonic; CONTROL releases gamma*ahat({i})^2, since Var(a)-average Var(a_child)=ahat({i})^2. Moreover eta<=I_controls(output), by Var(a)<=I(a) and physical product influence. No new source reference is issued.

Set c=4/9, Tnew=T+c eta, Snew=S+c eta-C_v>=0. Then Dtarget=Tnew-Snew exactly, and the release is Anew=A+c[eta-E eta_child]>=0. Every finite adaptive mixed stopping tree obeys

 complete entropy path + E FULL terminal CE
   =Hroot+Tnew_root-sum reach*Anew-E Snew
   <=Hroot+Troot+(4/9)eta_root.                    (3)

Replacing4/9 by c_* is valid in the analytic theorem. The rational majorant is used in finite certificates. At each node physically propagate the CURRENT target reference before reconstructing the next target. If its output erasure/outcome refunds total J>=0, raw target reset kappa equals sigma+J, sigma=E Dtarget_child-Dtarget_parent. Keep J and both full children; only signed sigma enters(3). Neither positive-part reset sums nor renewed descendant eta allowances are used. Adaptive row rules may vary at every history. This is the existing A029 proof with a sharper scalar coefficient, reconstructed rather than asserted as a new source-supplier theorem.

## 3. Why the improvement clears A027's exact bottleneck

Keep the literal A027@9 fixture and original allocation: u=D4, a=negative Maj3, core0 query followed by control0 on the surviving core branch. All3 original leaves remain. RootI=11/32; old unrelated debit1/64 is paid ONCE from the original core-decrement margin. Both controller children1/4,3/4 are retained. Selected OR2/D3 child has reach w=1/4 and original signed full account B_OR>1/64.

The first actual nonempty shape tilt theta in[0,1/8] uses ONE calibrated controller reference Ra=(Pa(empty),Var(a)nu_theta), with EXACT source references. Thus selected canonical Troot=d Da is precisely that first full-spectrum shape liability, and Sroot=0. Its original-root price is<=9/1792, leaving>19/1792 as proved in stage20. No change to shape reference or initial target is permitted here.

At selected root eta=(1/8)(3/4)=3/32. A029's looser eta/2 would cost w eta/2=3/256, EXCEEDING the previously certified remaining19/1792 by1/896. Hence simply importing that bound does not certify SAME-budget admission from the saved floor. This is failure of that sufficient floor, not proof the actual B_OR is insufficient.

The sharper envelope instead costs

 w*(4/9)*eta=1/96.

Therefore for ALL theta<=1/8 and EVERY finite adaptive mixed relative-odds history on the CURRENT reference,

 B_OR -first_shape_price -one_original_odds_allowance
   >1/64-9/1792-1/96=1/5376.                       (4)

The rate21/4, original tangent t=1/16, old1/64 debit, opposite controller child, constant core sibling and all earlier physical charges remain. The smaller reserve compared with19/1792 pays the strictly larger ALL-history odds class; it is not a revised estimate at the old no-reset scope. Queries may start with the next DATA coordinate as requested, and arbitrary later control/data reconstructions are included. The inherited controller reference has its own branch normalizers, usually different from output normalizers. No return to true shape is free.

## 4. Independent source review and limits

A029@4 section7's scalar identity, eta supermartingale and supplied T/S telescope are independently reconstructed at their stated scope. This is a scoped HOLDS review of that component, not blanket acceptance of its bundled old versions, all-width fixture estimates, or universal supplier assertions. Our improved coefficient and A027 same-account integration are NEW author contributions requiring A087/A094 review. A028@9 supplies an alternative posterior-channel admissibility condition; no claim makes all our relative targets admissible there. When true/reference source posteriors coincide, any posterior-channel target keeps original odds, whereas lambda2 can genuinely change them. The added eta allowance pays that real liability.

The first unsupported universal line remains an influence-priced ORIGINAL source/controller/core account Hroot+Troot for arbitrary Boolean inputs, and justification that the NECESSARY stopping-class target lies in bounded relative odds or has a separately source-paid excess. Formula(3) pays a nontrivial conditional target family, not those suppliers. The scalar coefficient is optimal only for binary-row domination, so improving it further cannot remove the need for an original account. NEXT must test one actually needed terminal-class reference against bounded relative odds and the posterior-channel image; if outside both, retain the exact excess KL and seek an unused original source for it. Another reset inside the class now closed by(3)-(4) should not be repeated.
