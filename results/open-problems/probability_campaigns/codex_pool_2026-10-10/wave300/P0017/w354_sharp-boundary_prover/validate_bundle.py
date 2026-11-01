"""Execute the integrator's pure parser without gate keys or store mutation."""
import ast
import json
import re
from datetime import datetime, timezone
from pathlib import Path

base = Path(__file__).resolve().parent
integrator = Path("~/math-brain-build/tools/integrate_drafts.py")
overlay = Path("~/math-brain-build/src/math_brain/overlay.py")
tree = ast.parse(integrator.read_text(encoding="utf-8"))
selected_functions = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in {"require", "parse_draft"}]
assert len(selected_functions) == 2
assignments = {}
for node in tree.body:
    if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
        name = node.targets[0].id
        if name in {"DRAFT_KINDS", "DRAFT_RELATIONS"}:
            # The parser uses only membership; enum-name strings preserve it exactly.
            assignments[name] = {ast.literal_eval(key): ast.literal_eval(key) for key in node.value.keys}
        elif name == "ALLOWED_LICENSE_PREFIXES":
            assignments[name] = ast.literal_eval(node.value)
regex = None
for node in ast.parse(overlay.read_text(encoding="utf-8")).body:
    if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "IDENTIFIER_RE" for target in node.targets):
        regex = ast.literal_eval(node.value.args[0])
assert regex is not None
environment = {"json": json, "Path": Path, "IDENTIFIER_RE": re.compile(regex), "PROOF_REQUIRED": {"lemma", "theorem"}, **assignments}
selected_module = ast.Module(body=selected_functions, type_ignores=[])
exec(compile(selected_module, str(integrator) + ":pure-parser-only", "exec"), environment)
extract = "# Pure parser copied from the live integrator; no imports or ingestion functions executed.\n" + "\n\n".join(ast.unparse(node) for node in selected_functions) + "\n"
(base / "VALIDATOR_EXTRACT.py").write_text(extract, encoding="utf-8")
file = base / "drafts" / "bundle_001.json"
payload, errors = environment["parse_draft"](file)
receipt = {"command": "python -X utf8 ~/brain_workers/w354/validate_bundle.py", "checked_at": datetime.now(timezone.utc).isoformat(), "file": str(file), "validator": str(integrator), "method": "actual require and parse_draft functions extracted with AST; actual license allowlist and identifier regex; enum-name equivalents used for membership only", "entries": len(payload.get("entries", [])), "relations": len(payload.get("relations", [])), "errors": errors, "store_opened": False, "gate_key_accessed": False, "mathematical_proof_check": False, "validated_payload": payload}
(base / "BUNDLE_VALIDATION.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps({key: value for key, value in receipt.items() if key != "validated_payload"}, indent=2))
raise SystemExit(bool(errors))
