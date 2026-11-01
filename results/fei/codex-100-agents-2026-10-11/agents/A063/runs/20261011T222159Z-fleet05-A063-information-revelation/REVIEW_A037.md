# Independent reconstruction: A037 physical/spectral common lift v1

Target: A037-PHYSICAL-SPECTRAL-COMMON-LIFT v1, from runs/20261011T220010Z-fleet05-A037-conditional-credit-ledger/REPORT.md, Section P; claim statement SHA256 aa45c0dacad4b1897e4c2f62511ccd331caf0eb6dc7ecc88cddf5189e8cf2cdb.

Reviewer: A063. No repair or mathematical contribution to the reviewed version was supplied. The reconstruction in QUERY_INFORMATION_IDENTITY.tex uses actual child spectra first, verifies their average is the parent projection by direct Walsh Parseval, then constructs the conditional history law inductively. The independently written checker computes characters by direct summation and uses a rational joint law over root spectral sets and full physical histories. It does not reuse A037 code or outputs.

Verdict for the finite uniform-cube physical-lift statement: ACCEPT_AT_STATED_SCOPE, subject to the executed validation recorded in out/CHECK_RESULTS.json. The proof supplies all finite dimensions and finite adaptive block trees; the finite checks exercise singleton-refined blocks and two adaptive stopping policies. Each child's Boolean Parseval is essential for physical fairness. Zero parent fibers are unreachable. A policy that queried the current spectral label directly, rather than the physical history, would fail the stated hypothesis and is not covered.

The kernel depends only on the residual subset, so conditional data processing gives I(root S;next outcome|history)=J at that node. The ordinary transcript chain rule, with terminal posterior retained, gives sum p J=I(S;L). Combining this with the exact local decrement gives H(S|L)=sum p B+E H(leaf). Thus the root posterior is not the terminal residual spectrum. This is independently reconstructed without any influence-payment assumption.

The phase-blind obstruction also holds: f=[1,1,1,-1] and g=[1,1,-1,1] have uniform squared parent spectra, while the named bit-0 positive restrictions have constant versus character spectra. A single kernel depending only on squared parent data cannot produce both named child laws.

Scope: this review accepts no universal FEI payment, no arbitrary reoptimized witness compatibility, and no separate KL/channel-reset claim. A037-CONDITIONAL-CREDIT-CONSERVATION v1 is useful background but is not independently accepted here. The block coarsening refund in this A063 run is a separate extension awaiting A087/A094 review.
