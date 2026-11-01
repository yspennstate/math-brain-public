# Source and scope check for the 2026-10-03 FEI continuation

Checked 3 October 2026 UTC.  This is a bounded primary-source check, not a
historical priority certificate.

* Klivans--O'Donnell--Servedio, *Learning Intersections and Thresholds of
  Halfspaces*, primary author manuscript, Theorems 18 and 21:
  <https://www.cs.columbia.edu/~rocco/Public/focs02.pdf>.  This supplies the
  physical bit-flip noise-sensitivity bounds used to obtain the established
  \(O(m\sqrt n)\) Fourier-entropy estimate for a product of \(m\) halfspace
  factors.
* Chakraborty--Kulkarni--Lokam--Saurabh, *Upper Bounds on Fourier Entropy*,
  primary ECCC revision 2, Theorem 4.5 and Corollary 4.8:
  <https://eccc.weizmann.ac.il/report/2013/052/revision/2/download/>.  This
  already contains the general noise-to-entropy framework and the
  \(O(\sqrt n)\) LTF entropy bound.  Those ingredients are credited, not
  claimed new.
* O'Donnell, *Analysis of Boolean Functions*, author-hosted manuscript,
  Section 11.5: <https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf>.
  The printed page 350 permits Berry--Esseen absolute constant \(0.56\) for
  independent nonidentical summands, matching the normalization used here.
* Wan--Wright--Wu, *Decision Trees, Protocols, and the Fourier
  Entropy-Influence Conjecture*, primary manuscript, Section 1.1 and Lemma
  1.5: <https://arxiv.org/pdf/1312.3003>.  Weak logarithmic FEI bounds and
  the empty-atom issue precede this work.  The elementary Gibbs proof in the
  continuation is included only to fix constants and normalization.
* The primary regular/random-LTF manuscript's Definition 9 and Corollary 10
  cover regular LTFs with normalized bias treated as an additional weight:
  <https://iuuk.mff.cuni.cz/~koucky/LBCAD/papers/random-ltf.pdf>.  The
  one-crossing case of the present finite-crossing results is therefore not
  new.
* O'Donnell--Wright--Zhou's primary symmetric-function FEI theorem covers
  every equal-weight score labeling:
  <https://www.cs.cmu.edu/~odonnell/papers/fei.pdf>.  The weighted classes in
  the present continuation are not inferred from that theorem, but its
  overlap is explicit.
* Two recent primary 2026 manuscripts were checked.  Potapov's
  <https://arxiv.org/abs/2609.21563> proves FEI for plateaued and partially
  bent functions and continues to describe general FEI as a conjecture.
  Gonzalez--MacManus--Pereyra's
  <https://arxiv.org/abs/2606.00246> proves different stopping-tree classes
  and likewise treats the unrestricted conjecture as open.  Neither source
  states the input-regular balanced finite-crossing theorem or the
  character-output unate-gate theorem recorded here.

Targeted searches of arXiv/ECCC for finite-crossing weighted scores,
character outputs of unate-gate combinations, and regular multi-threshold
score functions found no primary source stating the precise new restricted
consequences.  This negative search is weak evidence only.  It does not
establish priority, novelty, correctness, or publication readiness.

The completed statements in this continuation are restricted subsidiary
theorems.  They do not solve the full Boolean Fourier entropy--influence
conjecture, biased-product FEI, arbitrary irregular weighted finite
crossings, or a dimension-independent ordinary FEI theorem for arbitrary
shared-input unate-gate combinations.
