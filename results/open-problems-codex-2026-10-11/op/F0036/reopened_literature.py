from pathlib import Path
import json
p=Path('LITERATURE.md'); t=p.read_text(encoding='utf8')
t+='''
## Reopened attempt: newly checked published inputs (2026-10-12)

Direct shell/Python fetch: https://arxiv.org/pdf/math/0610625 (successful, arXiv v5 dated 13 June 2008, 58 PDF pages), saved as brownian_net_original.pdf and .txt. This is Sun–Swart, The Brownian net, Annals of Probability 36 (2008), no.3, 1153–1208, DOI 10.1214/07-AOP357. The source download is a new executed literature read, not a new all-service status search.

Checked verbatim primary assertions:

- Proposition 1.13 (Image set property), PDF p.14: “Let N be the Brownian net. Then, almost surely for all t ∈ [−∞,∞],” followed by equation (1.30), N ∩ Π_t = {π ∈ Π_t : π ⊂ ∪(N ∩ Π_t)}. Its inclusion of starting time minus infinity and quantifier over all paths are essential to the finite-segment grafting lemma in PROOF.md.
- Proposition 1.15(ii), PDF p.16: “N(∗,−∞) and −N(∗,−∞) are equal in law.” The minus sign denotes space-time rotation. PROOF.md uses (x,t)->(-x,-t), and swaps the left/right labels of the two witness curves. It does not need a separate unquoted spatial-symmetry theorem.
- Proposition 1.8 (Containment by left- and right-most paths), PDF p.10: “Let N be the Brownian net and let (Wl,Wr) be its associated left-right Brownian web. Then, almost surely, there exist no π ∈ N and l ∈ Wl such that l(s) ≤ π(s) and π(t) < l(t) for some σπ ∨ σl < s < t. An analogue statement holds for right-most paths.” This propagates local class bounds and supplies uniform spatial barriers.

Re-read Schertzer–Sun–Swart (2009), Special points of the Brownian net, arXiv:0806.2326, specifically:

- Equation (3.3), PDF p.31, in the proof of Proposition 3.6: equivalence of Law(N_T cap K) and Law(N_{-infinity} cap K) for deterministic compact K strictly later than T. The proof on pp.31–32 proves this intermediate assertion itself. This supplies the new approach's decisive null-event transfer; it was not used in the first attempt.
- Theorem 1.11(a),(b), PDF p.12, identifies extended representatives with true web representatives up to strong equivalence at separation points; Theorem 1.12(b), p.13, supplies the local sandwich for arbitrary outgoing net paths.
- The type-definition paragraph, PDF p.8, says subscript s means that incoming left-web paths belong to the left outgoing class and incoming right-web paths to the right outgoing class. This permits the canonical sandwich to use actual incoming l,r, exactly as required in Lemma 2.8.
- Proposition 2.6, PDF pp.22–23, identifies true separation points with separation points of incoming l and r.
- Lemma 2.8 and Proposition 2.9, PDF pp.24–25, give the relevant-separation definition and finite expected count for fixed time horizons. The reflected target box is strictly inside these horizons in the proof.
- Lemma 3.12, PDF p.36: “If z ∈ R² is a separation (resp. meeting) point of two paths π, π′ ∈ N, then z is of type (p, pp)_s (resp. (pp, p)).” It is applied only to paths started strictly before the fork, not merely to two paths born there.

These theorems do not individually state the exact F0036 answer. The reopened attempt's proposed full proof is a deduction from them, recorded in PROOF.md; it is not categorized as SOLVED_IN_LITERATURE. No novelty conclusion follows from these reads.
'''
p.write_text(t,encoding='utf8')
a=Path('search_log.json'); rows=json.loads(a.read_text(encoding='utf8')); rows.append({'service':'arxiv_direct_pdf_reopened','url':'https://arxiv.org/pdf/math/0610625','status':200,'date':'2026-10-12','pages':58,'purpose':'Check image property, backbone rotation, containment in the original Sun–Swart paper.'}); a.write_text(json.dumps(rows,indent=2),encoding='utf8')
