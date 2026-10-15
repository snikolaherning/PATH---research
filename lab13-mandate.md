# Lab 13 — Meridian Foundation Mandate

## Statement classifications — student's original wording

- S1 - Hard Constraint because a fixed time horizon and a rebalancing frequency are binding process rules (CFA 3d)
- S2 - Objective because its measurable, has a real return target, net of costs, and is judged over a defined rolling window
- S3 - Hard Constraint because it is a liquidity requirement with specific dollar amount
- S4 - Objective because its a relative yardstick that the policy portfolio is judged against
- S5 - Hard Constraint because it is a leverage and instrument prohibition
- S6 - Hard Constraint because it is a concentration limit that can be tested
- S7 - Hard Constraint because it is binding with a defined override
- S8 - Hard Constraint because it is a portfolio level liquidity floor
- S9 - Unverifiable Promise because there is no measure or breach consequence associated
- S10 - Missing because there is no risk objective and no optimization criteria

## AI review — separate from the student's classification

- S4 specifies a benchmark for comparison, not an explicit objective to outperform it or a requirement to hold 60/40. The student's initial classification is preserved above; their final IPS map below identifies it as the benchmark.
- S9 cannot be guaranteed by a holdings-only checker. Risk measurement and the response to a breach need clarification.
- S10 leaves the optimization criterion missing; absence of sector or ESG preferences does not itself require inventing constraints.
- The student's “CFA 3d” reference has not been independently verified and is not used as evidence for the checker.

## Checker scope

`mandate.py` uses USD millions and percentage weights. It checks totals, nonnegative weights, reserve eligibility, redemption liquidity and aggregated company exposure. It does not verify turnover, future returns, annual rebalancing, or calendar-year losses. Supplied instruments are the allowed universe; negative weights test only the observable long-only condition.

## Validation performed by AI

- Ran `python3 mandate.py`: reserve minimum computed as 3.0%.
- A: total 100.0, lowest weight 0.0, reserve 14.0, liquid 100.0, largest company 0.0; passes all five tests.
- B: total 100.0, lowest weight 0.0, reserve 1.0, liquid 85.0, largest company 9.0; fails three tests.
- C: total 100.0, lowest weight 0.0, reserve 2.0, liquid 100.0, largest company 8.0; fails one test.
- All measured values and verdicts matched the worksheet's known answer.
- Tested a separate copy of A with cash -2% and global equity 64%: only long-only failed, lowest weight -2.0%, reserve 10.0%. The saved original A remains unchanged.
- These are AI-executed checks, not a claim that the student independently ran or explained the code.

## Code quiz — student's answer

> Candidate B fails to limit because the code adds Acme's bonds and stock together to 9% exceeding the 8% limit even though on their own, stock and bond are under the cap

AI feedback: correct. The rule limits the combined exposure to an issuer, not each individual security.

## Candidate D — AI-proposed attack

- Portfolio: 100% cash; every other holding 0%.
- Question exposed: S2 requires CPI + 4% net over rolling five-year periods. The checker does not establish that an all-cash portfolio can meet that return objective. The CIO could reasonably reject it for inadequate expected real return. No cash-return or inflation forecast is supplied, so failure to meet S2 is a concern, not a proven future outcome.
- Student's two-sentence judgment, supplied after the AI-off instruction:

> Yes the objection holds because liquidity and concentration checks only show a portfolio is permissible, but S2 is a separate return objective, cash's historical returns fall well short of CPI + 4%. S2 supports this because "over rolling five year periods" makes it a test of realized returns over time, no holdings based compliance check can satisfy that

- AI qualification: “permissible” here means passing the five implemented checks, not full mandate approval. No historical cash-return series, period, inflation series or costs were supplied, so the historical-return claim is not independently established. The supported objection is that an all-cash portfolio has not been shown capable of meeting S2; current holdings alone cannot establish future rolling five-year performance.
- Execution result: D has total weight 100.0%, lowest weight 0.0%, reserve 100.0%, five-day liquidity 100.0%, and company exposure 0.0%; all five implemented checks pass. S9 remains “requires CIO clarification.”
- Phantom-partner exercise: the student reports that an out-of-class accommodation replaced the peer exchange. This is not recorded as an actual peer discussion.
- Phantom candidate: 100% Treasury 10-year notes, all other holdings zero. The supplied classifications imply reserve eligibility and five-day liquidity of 100%, no non-exempt company exposure, total weight 100%, and lowest weight 0%.
- Student's final judgment:

> A portfolio of 100% Treasury 10-year notes passes S3, because the table marks them reserve-eligible, but that only establishes they can be sold quickly, not at a stable price. Under S9, rising rates can push their prices down enough to threaten the 10% calendar-year loss limit, and since S9 has no defined measure or breach rule, compliance can’t be established either way until the CIO clarifies it.

## Question for the CIO — student's revised wording

> is the 10% calendar-year loss limit in S9 meant as an absolute guarantee that losses will never exceed 10%, or as a probability-based risk limit, such as a 5% chance of a worse year? An absolute guarantee would rule out any meaningful equity exposure and conflict directly with the CPI + 4% objective in S2, while a probability-based limit would become a testable constraint in the optimization that caps total portfolio risk and is checked against the return objective.

- AI qualification: the case does not establish exactly which allocations an absolute guarantee would rule out or prove that S2 is infeasible. Such a requirement would require assessing feasibility rather than assuming a feasible optimal portfolio exists. A probability-based limit needs an agreed return/loss definition, risk model, estimation period and monitoring/breach procedure; passing a model-based test is not a guarantee of realized losses.

## IPS and reflection — student's wording

- **IPS:** It’s a written guide that ties a portfolio to its purpose, where objectives (S2) state what the portfolio is trying to achieve and constraints (S3, S5–S8) set pass/fail limits it can’t cross on the way there.
- **Map:** The return objective is S2, the benchmark is S4, the operating constraints are S1, S3, S5, S6, S7, and S8, and the unresolved requirements are S9 and S10.
- **Suitability:** The checks only prove a portfolio is permissible, so one like all cash or all 10-year Treasuries can pass every check while missing CPI + 4% or exposing Meridian to the undefined loss risk in S9.
- **Uncertainty:** S9 was hardest because it reads like a hard constraint, but without a defined measure, risk model, or breach rule, it can’t be tested yet and has to go back to the CIO before optimization.

AI precision note: passing means passing the five implemented checks, not full mandate compliance. Missing the return objective is a possible outcome, not an established forecast. S7 explicitly permits turnover above 25% with committee approval.

## Submission and next-project preparation

- Lab evidence recorded: classifications with reasons, computed reserve minimum, known-answer checks, negative-weight probe, code explanation, candidate D and its judgment, phantom-partner critique, CIO question and design consequence, IPS map and reflection.
- Upload this file and `mandate.py` to GitHub and paste both links into the Lab 13 quiz. No upload has been performed here.
- After-lab preparation still to draft: the student's own Project 2 client mandate, stating its objective, hard constraints and one client question. This is distinct from the fictional Meridian case.
