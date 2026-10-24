# exact target, quantifiers, hypotheses and units

A040/B08 stage 4, run 20261014T033148Z-account05-A040-credit-insufficiency-tests. Independently review A046-SEPARATOR-LAYER-CUTOFF-RESERVE@1 at full exact claim scope. All blocks are disjoint uniform point indicators and the core g is independent and balanced. For F=1+[WUV OR S(U OR V)](g-1), query S until failure or completion, then resolve the appropriate controller and stop at a constant or the same g. Entropy and logs are bits; influence and reaches are physical cube probabilities.

Verdict: **HOLDS without repair** for A046@1. It transports a valid M-unit reserve, M=min(s,m), m=ceil(log2(min(R,T)+2))+2; it does not transport a universally bounded one-unit reserve. A new source-bound insufficiency test proves its precise envelope still has V_s/I~log2(w), even with a genuinely truncated zero-drift prefix. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Read BOARD snapshot 2026-10-14 03:25 UTC, including current B08 and the A046/A098 handoff, B08 lead notes v2, own STATUS and execution protocol 2026-10-11-execution-v2 in full. B08's old minimum-ratio census direction remains superseded by A098's explicit duplicate retirement: A040 reviews transported per-coordinate ownership; A046 sharpens actual late-layer debits. These are distinct tasks, so no census or actual-badness search is duplicated.

Read A046 run 20261014T012528Z REPORT.md, PROOF.md and CLAIMS.json: source statement digest c4f09ea5b2a552f438fe64c85737ae4570e03f57453c63683f124dd3a245f2af. Read A025 run 20261014T002956Z PROOF.md, particularly paired rows and its already-closed unfiltered all-s obstruction. Read A098 run 20261014T024504Z REPORT.md's precise A040/A046 assignment and ownership warning. Own prior stage-3 REVIEW_A023 supplies the previously reconstructed isoperimetry, descendant goodness, JS and retained-terminal interface. Copied only our own arithmetic/Walsh prefix into this run. No A046/A025 author code was imported or executed. SOURCE_RECEIPTS pins the local bytes; hashes are not review verdicts.

# complete derivation or exact first unsupported line

The complete reconstruction is REVIEW_A046.md. For a j-bit point switch between arbitrary actual Boolean branches of disagreement gamma, the empty residual-selector Fourier row plus the nonempty rows gives

    B/d<=2+2^-k[log2(euler)-2+log2(1/gamma)+2k], k=j-1.

In this controller gamma=e/2>=2^{-(min(R,T)+1)}. Elementary dyadic bounds prove every j>m layer is strictly 4-good. For alpha=2^-s, eta=2^{-(L+R+T)}, e=q+r-qr-eta, JB=(L+R+T)eta, JC=R q(1-r)+T r(1-q), JD=JB+JC and pi=eta+alpha e, direct disjoint physical cuts yield

    I_sep=s alpha e,
    I_other=(1-alpha)JB+alpha JC,
    I_terminal=pi I(g), terminal entropy=pi H(g),
    c_j=2^-j[JD+(j-1)e+e I(g)].

Independently define V_j as the expected sum of future eligible faces, sum_{ell<=min(j,m)}2^{-(j-ell)}c_ell, rather than assuming the source formula. Evaluating that sum recovers its exact V_j. Its expected decrement is c_j at j<=m and zero earlier. No reserve is reopened. Thus Q_bad<=V_s<=M I and

    H(F)<=(4+2/ln2)(I_sep+I_other)+V_s+pi H(g).

The terminal-core hypothesis is retained. The source's additional root-spectral/output conversion discussion is outside the exact reviewed claim and is not independently accepted here.

**Per-coordinate owner audit.** A W-coordinate has actual influence (1-alpha)eta and envelope debit M alpha eta. A U-coordinate has actual influence (1-alpha)eta+alpha q(1-r) and debit M alpha[eta+q(1-r)]; V is symmetric. A native core coordinate of influence t has actual influence pi t and debit M alpha e t. A separator coordinate with ell bits remaining when queried has actual influence alpha e and debit max(M-ell,0)alpha e from earlier eligible faces. These debits sum exactly to V_s. Distinct first-revealed faces may still debit the same physical coordinate many times.

**Quantitative limitation of the transported envelope.** ENVELOPE_OBSTRUCTION.md proves an all-integer actual Boolean family: h>=2, w=2^h-2, m=h+2, s=2m, L=4m, R=T=w, g=z. Its cutoff is exactly m and s>m, so this is not simply the old unfiltered all-s rule. Exact physical formulas imply

    V_s/I(F_h)~m~log2(w),
    V_s/I(F_h)>=m/4 for every h>=4.

Each U/V coordinate and the core coordinate has envelope debit/influence~m; the last separator coordinate has exactly ratio m-1. No finite K pays this envelope by K I uniformly. This refutes only the proposed uniform extension of the conservative envelope, not A046's stated parameter-dependent theorem. No lower bound on actual bad-only cost or growing H/I is inferred.

First unsupported universal line: obtain a universally influence-paid ACTUAL bad-layer debit, exploiting its row coefficients rather than paying every eligible face, while retaining arbitrary terminal entropy and any prescribed reference/reset cost on one exclusive account. The previous positive-KL/terminal Theta(1/k) test remains a guard against silently dropping the terminal; it is not repeated as a new result.

# executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was saved before jobs; SPEC_ADDENDUM.json froze the finer per-coordinate checks on the unchanged domain before running those checks. No automatic dimension increase. Pilot: first physical root, 44 audit plus 24 helper assertions, PASS in 0.008579 seconds. Main physical domain: exactly ten actual roots, eight with s in {1,2}, L=1,R,T independently in {1,2}, g=z, and two at s=2,L=1,R=1,T=2 with balanced bent4 and bent4/vertex-flip selector cores. Largest truth table has 12 bits. PASS: 694 audit and 368 helper assertions, 0.734367 seconds.

The independent code checks integer Walsh spectra against direct flips, actual child-product faces, retained entropy and influence partitions, compensated TC and odd-face telescopes, cutoff/reserve signs and exact direct-sum identities. Every finite queried node happens to be good; no all-width zero-badness extrapolation is used. Arbitrary terminal scope comes from the analytic proof, not the dictator fixtures.

Rational account domain: s=1..10, L,R,T=1..4 independently, formal I(g) in {1,5/2,10}: 1,920 cases, 10,560 reserve-drift identities, 50,880 assertions, 2.5024985 seconds after the frozen owner addendum. The earlier 28,800-assertion pass motivated adding the explicit per-coordinate partition; this was a substantive new check, not a parameter expansion. Formal account cases are not called Boolean truth-table cases. Six separate obstruction controls h in {2,3,4,6,8,10} passed 168 rational assertions, 0.005427 seconds. Their formula family reaches 2,117 physical bits; no such truth table was constructed. Exact factorized edge accounts are justified in the proof. Total final nonpilot assertions: 52,110.

Commands from A040:

    python -X utf8 runs/20261014T033148Z-account05-A040-credit-insufficiency-tests/code/audit.py pilot
    python -X utf8 runs/20261014T033148Z-account05-A040-credit-insufficiency-tests/code/audit.py
    python -X utf8 runs/20261014T033148Z-account05-A040-credit-insufficiency-tests/code/audit.py accounts
    python -X utf8 runs/20261014T033148Z-account05-A040-credit-insufficiency-tests/code/audit.py obstruction
    python -X utf8 runs/20261014T033148Z-account05-A040-credit-insufficiency-tests/code/finalize.py

Arithmetic is integer/Fraction, exact prime-log entropy vectors and rational 24-term atanh intervals with proved tails and outward compact endpoints. No float sign, random sample, GPU or background process. Values printed as floating ratios during inspection are illustrative only. Jobs were sequential, all far below the 55-second cap. Estimated memory 110 MB physical/30 MB account; peak not measured, no >300 MB job or memok trigger.

# proof dependencies and changed downstream conclusions

CLAIMS preserves A046@1's exact statement/hypotheses/author/hash, adding a full independent HOLDS review without repair. Its proof is reconstructed from physical edge counts, Parseval, log-sum and the previously audited stopping entropy interface. The new narrow obstruction has its own exact statement, hypotheses and canonical statement-envelope hash; its only source-versioned dependency is the independently reconstructed A046 potential definition and physical accounts. No broad positive candidate is opened at the stream review cap.

Changed conclusion for A046/A025/A023/A064: the transported reserve is valid, but neither a larger fixed constant nor a finer per-coordinate split can make this SAME cutoff envelope universally influence-paid. In the concrete family, a late physical separator coordinate is requested m-1 times. Further progress must filter actual good rows, change the reserve, or use certified remaining slack. The known fixed-width unfiltered no-go is consumed rather than repeated. Shared registries and other agents' files remain untouched.

# one next mathematical action and independent reviewer

Consume A046's actual eligible-layer Fourier-row calculation and test whether it deletes or pays the growing U/core/last-separator requests proved here. Require a summable actual-bad debit and all terminal bills; do not enlarge the envelope-only grid. A087/A094 should independently review the new narrow obstruction and challenge the full A046 acceptance; A046/A025 are the immediate mathematical consumers. Handoff is through these saved sources, not an external message.

# actual persistence receipts or precise save blocker

Saved locally: four protocol files, REVIEW_A046.md, ENVELOPE_OBSTRUCTION.md, frozen spec/addendum, independent code and immediate per-case/rational outputs, source hashes, schema readback and artifact receipts. STATUS has exactly two lines; WORKLOG and LEARNED append this stage. Every file is below 20 MB. PROGRESS and PACKET_DELTA are byte-identical. No local blocker. Supervisor copying, shared adoption, mirrors, independent review of the new obstruction and downstream use remain unverified.

## Universal bridge

This stage moves C019 stopping-tree payment by independently closing the transported-reserve claim A046@1 and locating its exact residual insufficiency: its cutoff envelope has V/I~log2(w), including per-coordinate ratios~m and an exact m-1 last-coordinate request, despite zero early drift. The universal-constant improvement is zero; actual bad-only payment, prescribed reset/witness costs and arbitrary terminal admission remain open. NEXT consumes A046's distinct actual-row calculation against these exhausted capacities, the shortest route toward full FEI because a larger constant or another envelope census is now rigorously ruled out for this mechanism.
