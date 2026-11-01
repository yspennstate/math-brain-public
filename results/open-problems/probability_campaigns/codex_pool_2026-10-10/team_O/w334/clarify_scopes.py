from pathlib import Path

here=Path(__file__).resolve().parent
p=here/"P0193_PROOF.md"
s=p.read_text(encoding="utf-8")
s=s.replace("It changes the witness range from a > 2.302585 at that example to a > 1.316958 for the sufficient family.", "The previous single recorded witness is a = log(10), approximately 2.302585; the new sufficient family contains every a > arcosh(2), approximately 1.316958.")
p.write_text(s,encoding="utf-8")
p=here/"SMALL_CASES_PROOFS.md"
s=p.read_text(encoding="utf-8")
s=s.replace("This strengthens the already-recorded zero-speed special case to an explicit sublinear distance scale.", "This strengthens the already-recorded zero-speed special case to an explicit sublinear distance scale. The source P0039 compares the base Cayley walk with the walk on its infinite percolation clusters. Applying the bound to H=G and to every cluster proves both intrinsic speeds are zero in this growth regime.")
s=s.replace("The general positive-speed converse on exponential-growth Cayley clusters remains unresolved here. The direct implication from positive ambient speed to positive intrinsic speed follows from d_G<=d_H.", "The base-versus-cluster positive-speed equivalence for exponential-growth Cayley graphs remains unresolved here. The inequality d_G<=d_H compares two metrics on the same cluster walk and is not itself the source's conjecture.")
p.write_text(s,encoding="utf-8")
