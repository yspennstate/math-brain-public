"""Run only the actual pure draft parser; never import or run the integrator."""
import ast
from enum import StrEnum
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
BUILD = Path("~/math-brain-build")


def selected_assignment(node, names):
    return isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id in names for t in node.targets)


def main():
    env = {"StrEnum": StrEnum, "json": json, "Path": Path, "re": re}
    models = ast.parse((BUILD / "src/math_brain/models.py").read_text(encoding="utf-8"))
    enums = [n for n in models.body if isinstance(n, ast.ClassDef) and n.name in ("ClaimKind", "EdgeKind")]
    exec(compile(ast.Module(enums, type_ignores=[]), "isolated-model-enums", "exec"), env)
    overlay = ast.parse((BUILD / "src/math_brain/overlay.py").read_text(encoding="utf-8"))
    identifier = [n for n in overlay.body if selected_assignment(n, {"IDENTIFIER_RE"})]
    assert len(identifier) == 1
    exec(compile(ast.Module(identifier, type_ignores=[]), "isolated-identifier-regex", "exec"), env)
    source_path = BUILD / "tools/integrate_drafts.py"
    tree = ast.parse(source_path.read_text(encoding="utf-8"))
    constants = {"DRAFT_KINDS", "DRAFT_RELATIONS", "PROOF_REQUIRED", "ALLOWED_LICENSE_PREFIXES"}
    nodes = [n for n in tree.body if selected_assignment(n, constants)
             or isinstance(n, ast.FunctionDef) and n.name in ("require", "parse_draft")]
    assert len(nodes) == 6
    exec(compile(ast.Module(nodes, type_ignores=[]), "isolated-integrator-parser", "exec"), env)
    payload, errors = env["parse_draft"](ROOT / "drafts/bundle_001.json")
    assert not errors, errors
    # Exact payload reconstruction from the supplied unified addition patch.
    patch = (ROOT / "patches/01_p0017_draft.diff").read_text(encoding="utf-8")
    reconstructed = "".join(line[1:] for line in patch.splitlines(keepends=True)
                            if line.startswith("+") and not line.startswith("+++"))
    assert reconstructed == (ROOT / "drafts/bundle_001.json").read_text(encoding="utf-8")
    hooks = [json.loads(line) for line in (ROOT / "HOOK_PROPOSALS.jsonl").read_text(encoding="utf-8").splitlines()]
    assert len(hooks) == 1 and len(hooks[0]["text"]) <= 300
    fire = "Ambient isotropy bounds every fiber's Poincare constant."
    silent = "Use conditional covariance to rescale each fiber and retain C_P inside the weighted expectation."
    assert re.search(hooks[0]["cue"], fire)
    assert not re.search(hooks[0]["cue"], silent)
    receipt = {"result": "PASS", "command": "python -B -X utf8 validate_integrator_schema.py",
               "source_parser": str(source_path), "function": "parse_draft",
               "execution_scope": "Only pure parser, require, exact enum/identifier definitions and four parser constants; no integrator imports, keys, signing or ingestion.",
               "entries": len(payload["entries"]), "relations": len(payload["relations"]),
               "errors": errors, "patch_payload_matches": True,
               "hook_controls": {"fire": fire, "silent": silent, "passed": 2},
               "is_mathematical_proof": False}
    (ROOT / "INTEGRATOR_SCHEMA_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
