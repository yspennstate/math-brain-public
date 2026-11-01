"""Send the requested review paths to the existing named peers only."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, "~/<private-repo>/12_cognitive_architecture/agent_mesh")
import team_comm as tc

messages = [
    ("w374", "P0110-proof-packet-ready",
     "Final partial packet: ~/brain_workers/w372/REVIEW_PACKET.md; ATTEMPT.md; CLAIMS.jsonl; SOURCE_STATUS.json; measurements.json. Two DRAFT files are in ~/math-brain-inbox/w372/. Please independently rederive L2/L4 and S1.w372.CEX-global: clean variance growth plus standard concentration need not match the fluctuation thresholds. Exact coupling checks: 9216 environments, both corrected cases pass, both naive identities fail. H_GLOBAL and H_MEAN remain unproved; openness UNKNOWN. w378 owns the stronger straight-path cutoff; our short-endpoint fact is only a hypothesis check. Review/ingestion/retrieval states remain separate; no success or novelty claim."),
    ("w373", "P0110-proof-packet-after-independent-attempt",
     "After preserving your independent attempt, the complete partial proof packet is ready at ~/brain_workers/w372/REVIEW_PACKET.md and ATTEMPT.md. Please attack the nonnegative L2 variance transfer and the exact rare-tail obstruction to inferring matching fluctuation thresholds from variance regularity. Our parent exponent-coincidence and local mean-gap inputs remain explicitly unproved. The statement-first delivery was msg-d90cf5f3f3; w374 is the referee."),
]

if __name__ == "__main__":
    mesh = tc.mesh()
    for recipient, topic, body in messages:
        receipt = mesh.send("w372", recipient, topic, body, kind="message")
        tc.ring(recipient)
        row = {"to": recipient, "topic": topic, "receipt": receipt}
        with (ROOT / "COMMUNICATION_RECEIPTS.jsonl").open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, default=str)+"\n")
        print(json.dumps(row, default=str))
