rows = [
("T379","KEEP","asks the extension to partly rule-governed facts beyond Kalai-Vempala; we hold partial work (memory t379_learned_rule_costs_a_posterior_variance_2026_10_31)"),
("T382","CHECK_LIT","the landscape is mostly mapped (Weisz-Amortila-Szepesvari lower bound; TensorPlan for few actions; Wang-Wang-Kakade lower bound with a gap); read which of constant actions / gap / online vs planning is still open, then restate to that"),
("T391","REPLACE_OR_RESTATE","rates in the intrinsic dimension with step counts independent of d have several 2024 proofs (Tang-Yang; Azangulov-Deligiannidis-Rousseau; Potaptchik-Azangulov-Deligiannidis); confirm what the row still asks (ERM over a network class with matching lower bound in one theorem) - from memory, not yet read"),
("T407","KEEP","explicit target and the Omega(d^2/eps) question"),
("T408","RESTATE","kernel case including continuous groups is Tahmasebi-Jegelka (2023); keep only gradient-trained networks"),
("T409","KEEP","asks optimal complexity and a polynomial-time test, beyond the Fefferman-Mitter-Narayanan existence result"),
("T411","KEEP","explicit structured prior class and runtime model"),
("T418","CHECK_LIT","Vakili's COLT 2021 problem; GP-UCB bounds were improved in 2023-2025 (Whitehouse-Ramdas-Wu; later work claims near-optimality in some regimes); confirm whether the Matern case is closed")]
with open("STATEMENT_PASS.tsv", "a", encoding="utf-8", newline="\n") as f:
    for i, v, why in rows: f.write("\t".join([i, v, why, "2026-11-11 statement read, an agent"]) + "\n")
print(len(rows))
