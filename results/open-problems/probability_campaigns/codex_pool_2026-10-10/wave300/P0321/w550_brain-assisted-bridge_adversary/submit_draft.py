"""Submit only the task-authorized author folder; never invoke an integrator."""
import json
import pathlib

root = pathlib.Path(__file__).resolve().parent
approved = pathlib.Path("~/math-brain-inbox/w550").resolve()
target = approved/"bundle_001.json"
part = approved/"bundle_001.part"
assert target.parent.resolve() == approved and part.parent.resolve() == approved
assert approved.name == "w550" and approved.parent.name == "math-brain-inbox"
validation = json.loads((root/"bundle_validation.json").read_text(encoding="utf-8"))
assert validation["entries"]==6 and validation["relations"]==7 and validation["all_new_nodes_concepts"]
if target.exists() or part.exists():
    raise SystemExit("Existing submission or partial file found; no overwrite performed.")
data = (root/"bundle_001.json").read_text(encoding="utf-8")
assert json.loads(data)["author_agent"] == "w550"
approved.mkdir(parents=True,exist_ok=True)
with part.open("x",encoding="utf-8") as out:
    out.write(data)
    out.flush()
part.rename(target)
assert json.loads(target.read_text(encoding="utf-8")) == json.loads(data)
workflow_path = root/"WORKFLOW_STATE.json"
workflow = json.loads(workflow_path.read_text(encoding="utf-8"))
workflow["submitted"] = {"state":"submitted_draft", "path":str(target), "entries":6, "relations":7,
                         "authorization":"explicit P0321 task names math-brain-inbox/w550", "complete_then_renamed":True}
workflow["model_provenance"] = {"path":"MODEL_PROVENANCE.json", "served_identity_verified":False}
workflow_path.write_text(json.dumps(workflow,indent=2),encoding="utf-8")
print(json.dumps({"submitted":str(target), "entries":6, "relations":7, "mathematical_review":"partial", "ingested":False, "integrator_run":False}))
