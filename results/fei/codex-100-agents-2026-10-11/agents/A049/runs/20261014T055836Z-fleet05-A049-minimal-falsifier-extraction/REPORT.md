# exact target, quantifiers, hypotheses and units

Extract the smallest useful actual DATA-query certificate for A048's common-factor labelled-reserve obstruction, retaining the signed residual, both physical terminal spectra, one removed-influence account, and a normalized joint reference. Uniform independent cube bits; Boolean signs; entropy, cross-entropy and KL in bits. No named scoped theorem or full FEI is refuted.

Construction class: for any Boolean seed g on t effective bits w, let alpha=Pr(g=-1)>0 and take independent fair bits a,z,y. Write y for its sign (-1)^ybit and set

    h(a,w)=1+a(g(w)-1),
    G=z+(1-z)h=1+a(1-z)(g-1), F=yG.

The controller z chooses cores y and yh, each with probability 1/2. Query the physical CORE-data bit a and stop. At a=0 the two cores coincide and their duplicate label is contracted; at a=1 retain the distinct cores y and yg. Labels of opposite functions are not merged. Define R_lab=sum_j q_j log2(1/q_j) Var(core_j), kappa=R_lab(root)-average R_lab(child), D=H(F)-average H(F_child), and residual D-kappa.

The target is a strict rate-four failure kappa>4 Inf_a, together with D-kappa<0. We prove effective dimension six minimal within this stated construction class, separately for each failure. We also prove that kappa/Inf_a is unbounded along an actual all-essential Boolean family and that a common entropy-zero parity factor flips the signed residual while leaving the physical data-query entropy ledger unchanged. No minimum over arbitrary functions, representations, references or trees is claimed.

# sources actually read, revisions and theorem locators

Stage-start BOARD is supervisor 2026-10-14 05:52 UTC. Read its updated B10 and associated A039/A064/A092 entries; B10 notes remain v2, 2026-10-11 23:31Z. Read own STATUS and complete execution protocol revision 2026-10-11-execution-v2. Earlier campaign, registry and paper readings remain prior-stage provenance, not a fresh literature review.

Sources read this stage: A048 run20261014T022727Z PROOF, 'Exact general tensor transformation', 'All-essential sparse activation witness', 'Required signed cancellation'; A048 run20261014T052201Z PROOF and REPORT, activation criterion, retained seed bill and spectator-data boundary; A050 run20261014T033613Z PROOF, common-k normalized transport and its signed reset; A047 run20261014T044331Z REPORT, common-support and reference-only-row boundary; A092 run20261014T045641Z PROOF, four-bit conditional-reset falsifier and retained product-reference repair. SOURCE_RECEIPTS.json records paths and hashes. A092 has already minimized its different four-bit reset target, so we do not repeat that census. The saved NEXT concerned a real data reveal of A048's common-factor fixture; this stage follows it and incorporates the newly clarified KL boundary. No disagreement with the lead's scope direction; its original finite-block task was completed earlier.

# complete derivation or exact first unsupported line

## Arbitrary-seed reduction and signed common-factor change

Let I_g=I(g). Direct physical edges give

    Inf_a(F)=Inf_z(F)=alpha/2,
    I(F)=1+alpha+I_g/4,
    average I(F_child)=1+alpha/2+I_g/4.

Thus removed influence d=alpha/2, with the common parity's influence ONE retained at both terminals. The query is essential for every alpha>0; if g depends on every seed bit all root coordinates are essential. Both terminal functions are nonconstant because y remains.

Both distinct parent cores have mean zero, so R_lab(F)=1. At a=0 the contracted child has one label and reserve zero; at a=1 both distinct cores again have mean zero and reserve one. Hence kappa(F)=1/2 and kappa/d=1/alpha. For g=1-2*1_{w=0^t}, t>=1, alpha=2^-t and all variables are essential. Consequently kappa/d=2^t is unbounded. This is a data-query extension of the known shared-core reserve objection, not a refutation of its independent-core theorem.

Before multiplying by y, E h=1-alpha and E g=1-2alpha. The same contracted labels give

    R_lab(G)=alpha-alpha^2/2,
    average R_lab(G_child)=alpha(1-alpha),
    kappa(G)=alpha^2/2.

The common parity leaves every root/child Fourier entropy, erased-sector M, coherent branch information J and the true D unchanged, because it only shifts Fourier labels by a deterministic parity frequency. It boosts kappa by (1-alpha^2)/2, and shifts the residual by its NEGATIVE. Exactly

    D = R_lab(root)-average R_lab(child)+(D-kappa).

No positive release can be removed from this equality independently of its signed companion. The fixed query set {a} also gives zero actual descendant-reference injection: W=S0\{a} is a deterministic root projection. This fixture has no schedule-information loophole.

## The entire seed spectrum cancels from the data decrement

Put phi(p)=-p log2 p, with phi(0)=0. At the root, empty-seed-frequency masses are (1-alpha/2)^2 and three copies of alpha^2/4. At the active child they are (1-alpha)^2 and alpha^2; the inactive child is a character and has entropy zero. For each nonempty seed Fourier coefficient c, the root has four masses c^2/16 and the active child has two masses c^2/4. In D their contribution is (c^2/2), whose sum is Var(g)/2=2alpha(1-alpha). Therefore, for EVERY seed, independently of its Fourier shape,

    D(alpha)=phi((1-alpha/2)^2)+3phi(alpha^2/4)
              -phi((1-alpha)^2)/2-phi(alpha^2)/2
              +2alpha(1-alpha).

This reduces the signed-reserve target to one scalar parameter without dropping the seed's retained terminal entropy. The finite census tests the identity against direct spectra; the second implementation reconstructs it from these masses and direct signed-character sums.

## Fixed six-variable circuit and exact signs

Choose t=3 and g=-1 only at w=000. In LSB bit order a,z,w0,w1,w2,y,

    F=(-1)^y * (1-2*1_{a=1,z=0,w0=w1=w2=0}).

There are no free parameters. The five-bit core is negative only at integer 1; F is this core on y=0 and its negative on y=1. The full 64-entry truth table is out/truth_table.txt and also in WITNESS.json. SHA256: 141ff6a13f2f29817ac0b0c7f5e50aaa6ad868107521d5f980209b5955a20548.

All five core-coordinate influences are 1/16, and parity influence is one. Thus I_root=21/16, mean terminal I=5/4 and d=1/16. Parent spectral masses on the full y-frequency row are 225/256 at core frequency empty and 1/256 at each other core frequency. Inactive child is y; active child is y times a four-bit point defect. Consequently

    H_root=8-(225/128)log2(15),
    mean H_terminal=3-(49/64)log2(7),
    D=5+(49/64)log2(7)-(225/128)log2(15).

The exact integer sandwich

    2^600 * 7^98 < 15^225 < 2^604 * 7^98

proves 9/32<D<5/16. Since kappa=1/2, the signed residual satisfies

    -7/32 < D-kappa < -3/16 <0,
    kappa=8d>4d, kappa-4d=1/4.

Before the parity factor kappa=1/128 and D-kappa>35/128>0. The common parity boosts the release by 63/128 and shifts the residual by -63/128; all true entropy costs remain unchanged. This is a rigorous sign flip under a harmless common Fourier character, after an essential data query and actual duplicate-core contraction.

The TRUE rate-four excess is also retained: D-4d lies strictly between 1/32 and 1/16. Cancelling the spurious inflated reserve does not by itself establish a rate-four local query price. For this finite fixture there is an explicit once-only child certificate: the active core has influence 1/2 and entropy H(h4)=6-(49/32)log2(7)<2, proved by 7^49>2^128. Its unused K4 slack is S_active=2-H(h4)>0; the inactive core has slack zero. Then

    S_active/2 - (D-4d) = 5/4-H_root >0,

the last sign proved by 15^225>2^864. Thus the actual small excess can be paid once from this specified active-core terminal surplus. The parity's four units of K4 slack are kept separately and are not used for that payment. This is an explicit finite owner check, not a source of arbitrary-seed child surplus or a new point-defect class theorem.

## Minimality in the declared class

If there are at most two effective seed bits, alpha belongs to {1/4,1/2,3/4,1}, or is zero and the data query is irrelevant. The scalar formula gives D(alpha)-1/2>0 in each nonzero case. Exact integer comparisons respectively are

    2^112 * 3^18 > 7^49,
    2^20 > 3^9,
    2^112 > 5^25 * 3^9,
    8 > 1.

These are independently checked and saved with numerator/denominator products in REPRODUCTION.json. Thus no effective n=t+3<=5 has negative residual. At t=3 the displayed seed gives a negative residual, so six is minimal. The strict rate-four release failure also needs alpha<1/4; a nonempty event on at most two effective uniform bits has alpha>=1/4. Its minimum is therefore independently six. Dummy coordinates cannot evade either argument: suppressing them preserves alpha, all relevant laws, the reference scheme and the contracted reserve. The census includes all 278 truth tables at t=0..3 and finds exactly eight witnesses for each target, the eight single-negative-point seeds at t=3.

## One complete nonmatching joint reference, with inherited terminals

The main check first uses Q=P, proving the actual coherent lift and normalized inherited children exactly. This control has zero source, erasure, outcome and terminal KL. To avoid hiding an initial reference bank, the second implementation separately fixes a NONMATCHING reference Q uniform on all 32 core frequencies times the deterministic y frequency. It dominates P, is normalized, and has the same common parity kernel. No source-zero/reference-positive erased row occurs in this example; no fallback credit or common-support theorem is extended.

Erase the a frequency in P and Q, apply the SAME actual physical branch kernel K_b(T)=P_child_b(T)/(2P_erased(T)), and normalize the reference children. The reference predictions are (4/113,109/113), distinct from the physical (1/2,1/2). The inactive inherited reference is the actual parity point mass. The active inherited reference has core mass 49/1744 at empty and 113/1744 at each of the other 15 frequencies. Choose fresh inactive reference equal to its actual point mass and fresh active reference uniform on 16 core frequencies, each lifted by the unchanged parity law. All references are independently normalized.

Writing K_root for source KL, E for conditional erasure KL, O for outcome KL, K_B for average inherited-terminal KL, K_new for average chosen-terminal KL, and rho=K_new-K_B, the exact bills are

    K_root=-3+(225/128)log2(15),
    E=(225/128)log2(15)-(113/128)log2(113),
    O=-2-(1/2)log2(109)+log2(113),
    K_B=-1+(1/2)log2(109)-(15/128)log2(113),
    K_new=-1+(49/64)log2(7),
    rho=(49/64)log2(7)-(1/2)log2(109)+(15/128)log2(113).

Exact prime-log cancellation checks K_root=E+O+K_B=E+O+K_new-rho. The root cross-entropy is FIVE bits; average chosen-terminal cross-entropy is TWO bits, and the full inherited-terminal KL is retained before resetting. Conditional KL of the common parity is zero; the core KL above is not. The chosen uniform reference's three-bit cross-entropy decrement is not priced by the tiny removed influence here: its source/reference account must remain present. This concrete normalization and signed telescope make the ownership distinction explicit.

There is also a complete finite K4 certificate for THIS chosen full reference. The inactive/active terminal cross-entropies are 0 and4, physical influences1 and3/2, so their respective surplus values are4 and2, averaging3. The query's cross-entropy excess over4d is3-1/4=11/4. Spending that average full-terminal surplus once leaves3-11/4=1/4, exactly4I_root-CE_root=21/4-5. This is an alternative full-reference ledger including the parity influence; it does not add the earlier entropy-only core surplus as a second available reserve. The source, erased, outcome and inherited child KL above remain in the signed telescope. Neither finite ledger supplies a universal occupancy reference or an unused arbitrary source bank.

First unsupported universal line: an arbitrary seed's prescribed joint occupancy/Bayes reference and true selected-data excess are paid by a genuinely unused conditional source or certified child surplus under one influence budget, preserving both terminal bills and the signs of the reset. The displayed finite active point-core surplus closes this fixture only. Also unsupported is removing the construction/contraction assumptions from the six-variable minimality statement. Neither step is claimed.

# executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was saved before any computation: all 278 seeds t=0..3, no symmetry reduction, maximum six physical variables, memory estimate80MB and runtime limit60s. Pilot uses t<=1 plus the designated three-bit seed (seven cases). out/REFERENCE_SPEC.json preceded the separately coded scalar/reference reconstruction: one full witness, four scalar profiles and one normalized nonmatching reference, memory20MB/runtime60s. No expected >300MB job, memok-gated job, GPU, background process or automatic dimension increase occurred.

Commands from A049, prefixed by this run's path: `python -X utf8 code/check.py --pilot`, `python -X utf8 code/check.py`, and `python -X utf8 code/reproduce.py`. Final pilot PASS seven cases/199 assertions in0.0312s; full PASS278 cases/11,468 assertions in0.7471s; final separate representation PASS98 assertions (runtime in REPRODUCTION.json). Main plus reproduction total11,566 assertions. Integer Walsh/Fraction laws, exact physical edges, complete normalized branch kernels and rational prime-log cancellation are used. Sign intervals use range-reduced 16-term atanh sums with geometric tail bounds and outward rounding to1e-9; final witness and minimum signs have exact integer-product certificates. Floating numbers appear only in timers and the expressly noncertifying diagnostic described below.

The initial pilot stopped at a proposed entropy interval that was too tight; no PASS was emitted. The exact formula and frozen domain were unchanged, the interval was corrected to9/32<D<5/16, and pilot/full checks completed. out/VALIDATION_REPAIR.md records this failure and correction. The second implementation imports no helper: it directly sums Fourier characters, reconstructs the scalar cancellation, checks all64 truth values and influences, and transports the declared nonmatching reference. This is internal different-representation reproduction, not an independent agent review. Each completed result was saved immediately in PILOT_CHECK.json, FULL_CHECK.json, WITNESS.json and REPRODUCTION.json. All artifacts are below20MB.

# proof dependencies and changed downstream conclusions

The proof is self-contained; proof_dependencies are empty. This is a compression and data-reveal verification of A048-COMMON-FACTOR-LABEL-RESERVE-OBSTRUCTION@1, not a new broad potential. A050-COMMON-CONDITIONAL-KERNEL-REPAIR@1 survives: the common parity kernel and its terminal bill are transported exactly. A047's common-support boundary is respected. A092's separate conditional-reset falsifier is not reproduced or renamed.

Downstream consequence: at an actual core-data reveal, duplicate-label contraction can release1/2 of a shared-core variance reserve with removed influence1/16 while the actual signed residual is negative. The complete joint reference does not remove the retained core KL or fund a repeated reset. A cancelled inflated reserve still leaves a strictly positive true rate-four excess; its one specific active-core surplus is checked, with no parity or source-bank reuse. Full FEI remains OPEN and no universal constant improves. The stream's review cap is respected by narrowing and verifying an existing mechanism rather than proposing another broad candidate.

# one next mathematical action and independent reviewer

NEXT: at the exposed opposite-priority gate already identified by A092, transfer its actual conditional likelihood/erasure statistic into the prescribed occupancy reference and name one unused child bank before charging both terminal costs; keep reference-only rows explicit. This moves from the scalar common-factor obstruction to the live nonmatching-reference ownership gap rather than repeats the completed six-bit extraction. A048 is the primary independent reviewer of this data-reveal compression; A050 or A092 should check the contraction convention and the complete normalized-reference ledger. Handoffs are local files only; no messages were sent.

# actual persistence receipts or precise save blocker

The four protocol files, scripts, frozen specifications, repair history, full truth table and exact outputs are saved in this assigned run. STATUS has exactly two lines; WORKLOG and LEARNED were appended. out/PERSISTENCE.json records local paths, byte counts and SHA256 values; SOURCE_RECEIPTS.json records read-only provenance. No local save blocker. Independent review, supervisor copies, canonical adoption, remote mirror verification and downstream use are pending or unverified, not claimed.

**Universal bridge:** This stage moves C024 history transfer and C019 stopping-tree payment by reducing the common-factor data-reveal obstruction to one six-bit circuit and one scalar alpha, proving effective dimension six minimal within the declared contracted-label family, and retaining a complete nonmatching source/erasure/outcome/terminal/reset KL telescope. The true rate-four excess survives cancellation and is paid only by this fixture's explicitly checked unused active-core surplus. The universal missing step is an owned conditional source/child bank for the actual nonmatching occupancy reference with both terminal bills. NEXT attacks that prescribed-reference likelihood and erasure at the existing opposite-priority gate, the shortest route because another unsigned reserve or matched-kernel-only calculation would leave the demonstrated ownership gap intact.
