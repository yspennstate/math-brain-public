# Physical queries consume KL; terminal affordability alone does not pay it

All logarithms use bits. Full FEI remains open. This corrects the physical-transaction reading of A027 version 10, not its scalar bound or terminal functional.

## 1. Exact account and the omitted term

At node v let P_v be the actual Fourier law and R_v its current normalized covering reference. On physical query i, erase the spectral membership bit to obtain m_v(T)=P_v(T)+P_v(T+i). Use the true phase channel to lift the erased reference to raw child references and normalize each by its OWN positive mass. Denote those references R^inh_vb. Both actual input outcomes have probability 1/2. Define

    delta_v = D(P_v||R_v) - (1/2) sum_b D(P_vb||R^inh_vb).

By finite chain rule, delta_v is erased-pair conditional KL plus the outcome KL D((1/2,1/2)||Z), where Z are the two reference outcome masses summing to one. Thus delta_v>=0, including true-zero pairs with zero true weight. Coverage ensures each occupied child's normalizer is positive. For a rebuilt target R_vb the signed actual conversion is

    e_v = (1/2) sum_b [D(P_vb||R_vb)-D(P_vb||R^inh_vb)].

Writing sigma_v=(1/2)sum_b D(P_vb||R_vb)-D(P_v||R_v), the exact identity is e_v=sigma_v+delta_v. At actual reaches w_v, finite telescoping gives

    B_raw = CE(P_root,R_root) + sum_internal w_v e_v
          = H(P_root) + E_leaf D(P_leaf||R_leaf) + Qloss,
    Qloss = sum_internal w_v delta_v.                         (1)

This is the same-target transaction ledger. It does not describe a target-changing edit. No limit, entropy monotonicity, or infinite stopping argument enters.

A027 v10 DERIVATION equation (3) telescopes D=Tnew-Snew and its code verifies the terminal functional. Its code ALSO computes e=sigma+delta, then omits delta from the final bill. The statement that only sigma enters the complete physical transaction has the same scope error identified by A094 in A011 v5. The phrase 'complete entropy path + terminal CE' can correctly mean H_root+E D_leaf; it cannot simultaneously identify that quantity with root CE plus actual signed conversions.

## 2. An all-dimensional witness inside bounded odds

Let u=D_m be -1 only at the all-zero input, m>=2, let a be one fresh dictator control, and F=1+((1-a)/2)(u-1). Thus F is D_(m+1). Start with the TRUE root Fourier reference. Query core bit 0, a proper block. The inactive child is constant and retained; the active child is D_m, with m-1 remaining core coordinates and the controller. Its reach is 1/2. Rebuild only that child's sector odds by lambda=2, keeping its true data marginal and inherited controller shape. Query the controller next and retain both full terminal spectra, using their actual inherited references.

The rebuilt child has positive KL d. Indeed on every nonempty remaining data row the true controller-sector probability is 1/2, the prescribed probability is 2/3, and the row has positive mass. These rows exist since m-1>=1. Binary KL is strictly positive. Root and first-query KL are zero. Erasing the controller leaves exactly the unchanged true data marginal; therefore both reference outcome normalizers are 1/2 and both inherited child references are the TRUE child laws. The second query consumes all d. Hence

    E D_terminal=0,  Qloss=d/2>0,  B_raw=H(F)+d/2.

The lambda=1 boundary has d=0; lambda=1/2 gives the same strict separation. The m>=2 hypothesis is necessary for this particular nonempty-row proof: m=1 has a degenerate post-DATA sector and no tilt. Choosing m>=4 also places the original core bias at most 1/16, so the low-bias guard does not remove the counterexample. Terminal core biases are 0 or 2^(-(m-1)), at most 1/8 when m>=4. This refutes a ledger identification, not FEI or original-account solvency.

## 3. A strict counterexample to using the old envelope for the raw bill

Retain the LITERAL v10 selected D3/OR2 child, original controller reference shape tilt theta=1/8, and mode 1: at every positive depth multiply true sector odds by 1/2 on even data masks and by 2 on odd masks. At depth zero use lambda=1 exactly as v10. Query the three DATA coordinates in order, stopping at depth three or a constant. Every target satisfies the stated bounded-odds, inherited-shape and true-data-marginal conditions. Both complete siblings remain at each query.

The instrumented original checker certifies, in SELECTED-node units,

    B_raw-H_root - (T_root+(4/9)eta_root) > 1/128.              (2)

The full 300-policy replay has 12 strict violations of that envelope for B_raw, although its terminal-functional bound holds. These are finite counterexamples to the physical reading of that numerical envelope. The original GLOBAL B_OR still pays ALL 300 actual bills: its residual after (1/4)(B_raw-H_root), including the initial shape charge in the raw bill, is >3/10 in every tested policy. The old unrelated 1/64 debit remains in its original separate core-margin allocation. There is no contradiction with v10's much smaller 1/5376 FLOOR: that floor allocated a uniform sufficient shape/odds price, whereas this replay evaluates the much larger exact original B_OR and actual signed bookings. No infinite-policy affordability follows from these 300 cases.

## 4. Corrected conditional bridge and the first unpaid line

The unchanged v10 endpoint telescope yields

    E D_leaf=Tnew_root - sum w_v Anew_v - E Snew_leaf.

Combining it with (1) gives the corrected equality

    B_raw=H_root+Tnew_root - sum w_v Anew_v - E Snew_leaf + Qloss. (3)

Let M be the original unused quota minus H_root+Tnew_root, after ALL old debits and retained siblings. The SAME quota pays the raw transaction if and only if

    Qloss <= M + sum w_v Anew_v + E Snew_leaf.                 (4)

No positive-part deletion or renewed eta allowance is permitted. Equation (4) is an exact admission test; it is not a proof of that inequality for every useful policy. The scalar coefficient log2(e)-1<4/9, eta supermartingale, original tangent transport and v10 terminal functional remain valid. The claimed all-history PHYSICAL envelope and its specific 1/5376 physical residual are withdrawn pending (4). Version 11 narrows the same candidate rather than opening another broad result.

A028's current exact nodewise C<=Z+gamma Cvac test is likewise an endpoint affordability condition unless physical query losses are booked through the complete inherited account. A011 v6 has explicitly corrected its own scope and pays inherited descendants with nonpositive vacuum-calibration resets; its repair does not automatically pay bounded-odds reconstructions. A target outside a posterior-channel image is not, by itself, insolvent.

The first unpaid line is a bound for accumulated Qloss for a REQUIRED bounded-odds/terminal policy from this SAME unused original reserve. A separate universal unpaid line is an influence-priced ORIGINAL full reference for arbitrary Boolean cores. The shortest next action is to select that necessary policy or use inherited descendants when the application permits them, not to repeat optional odds examples or claim a new supplier.
