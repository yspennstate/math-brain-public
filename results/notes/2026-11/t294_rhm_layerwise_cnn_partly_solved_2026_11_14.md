---
name: t294_rhm_layerwise_cnn_partly_solved_2026_11_14
description: "[PROVISIONAL] T294 Mossel / random hierarchy model: positive half partly solved, Ren-Dandi-Krzakala-Lee arXiv 2601.19756 prove layerwise-trained deep CNNs learn the RHM; joint training and the shallow/kernel lower bound open"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T12:51:20+02:00
  status: provisional
  evidence: ""
---

T294 on the top-200 list (Mossel's hierarchical generative models and the random hierarchy model of Cagnetta, Petrini, Tomasini, Favero and Wyart) is now partly solved on its positive side.

Ren, Dandi, Krzakala and Lee, "Provable Learning of Random Hierarchy Models and Hierarchical Shallow-to-Deep Chaining", arXiv:2601.19756 (v2): under mild conditions a deep convolutional network trained with gradient methods on ordinary input-label pairs learns the random hierarchy model efficiently. The proof trains layer by layer: if intermediate layers receive clean signal from the labels and the relevant features are weakly identifiable, layerwise training of each layer learns the target hierarchically. Authors checked against the arXiv record on 14 Nov 2026; only the abstract was read.

Still open: joint training of all layers, and the lower half of the question (bounded-depth algorithms and kernel methods need exponentially many samples).

Row text updated in src/rows_24.py (top200_probability_2026_10_14), STATUS_1114.tsv row T294, push 227.

How far to trust: abstract-level reading; the "mild conditions" were not checked against the row's parameters (vocabulary v, multiplicity m, depth L). Before calling it more than partial, read the theorem statement for the sample count and the conditions.

