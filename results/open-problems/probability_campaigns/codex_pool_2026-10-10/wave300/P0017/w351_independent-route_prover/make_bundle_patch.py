from pathlib import Path
ROOT=Path(__file__).resolve().parent
lines=(ROOT/"bundle_001.json").read_text(encoding="utf-8").splitlines()
live="~/math-brain-inbox/w351/bundle_001.json"
patch="--- a/"+live+"\n+++ b/"+live+"\n@@ -0,0 +1,"+str(len(lines))+" @@\n"+"".join("+"+line+"\n" for line in lines)
(ROOT/"patches"/"02_p0017_brain_draft.diff").write_text(patch,encoding="utf-8")
print("saved exact DRAFT diff; no live file edited")
