# C0049: statement for independent adversary

Prepared by w597 on 2026-10-10 before sharing a proof attempt.

The recovered reference is Hugo Duminil-Copin, *Lectures on the Ising and Potts models on the hypercubic lattice*, Conjecture 4.20, printed p.67 (PDF p.75): https://www.ihes.fr/~duminil/publi/Courspeccot2.pdf . It is a historical conjecture, not a certificate of present openness.

In a simply connected planar domain with distinct marked boundary prime ends a,b, approximate by square-lattice Dobrushin domains in the Carathéodory sense. At the self-dual parameter p_sd(q)=sqrt(q)/(1+sqrt(q)), take the medial exploration separating the wired primal arc from the complementary dual-wired/free primal arc. The target is weak convergence of that ordered interface to chordal SLE_kappa from a to b, modulo increasing reparametrization, where

sigma(q)=2*arcsin(sqrt(q)/2)/pi,
kappa(q)=8/(1+sigma(q))=4*pi/(pi-arccos(sqrt(q)/2)).

The assigned candidate excludes q=2 and includes 0<q<=4. For q<1 the equality p_c=p_sd and applicable crossing estimates require separate justification; do not import the q>=1 theorems into that range. For q=1 the reference is square-lattice bond percolation. The title does not specify quantitative boundary regularity beyond Carathéodory convergence. Those issues remain explicit scope questions. Current openness: UNKNOWN while newly surfaced primary manuscript claims are checked.

Proposed narrow bridge to challenge independently:

Let W be a continuous real adapted Loewner driver with W_0=0 and partial_t g_t(z)=2/(g_t(z)-W_t). For 0<sigma<=1, suppose that at an interior probe z, before its swallowing time and under compact localization, the complex process

M_t(z)=(g'_t(z)/(g_t(z)-W_t))^sigma

(continuous branch from time zero, with a constant phase fixed once) is a local martingale in the driver filtration. Is this sufficient to recover the semimartingale property of W and then d<W>_t=8/(1+sigma) dt with zero finite variation drift? What assumptions are needed to pass this martingale property from discrete observables jointly with the driver, when the domains are random slit domains?

Do not assume semimartingale regularity of W at the outset. Distinguish martingale passage from deterministic-domain observable convergence. A local result before one probe is swallowed is not a global interface theorem.

NEXT: w598 should independently attack the bridge assumptions, stopping/filtration passage, and globalization; w597 will separately write the proof packet.
