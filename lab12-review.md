# Lab 12 — UiPath presentation and partner review

## Questions received as presenter — corrected answers

- **How is stock-based compensation treated?** GAAP operating expenses include SBC. The model adds it back in operating cash flow, then deducts an equal cash cost for dilution-offset repurchases, keeping shares constant. This counts its economic cost once. FY2026 SBC was $290.7M, about 18% of revenue, versus $358.2M in FY2025 and $372.0M in FY2024.
- **Do buybacks offset dilution?** Constant shares are a modeling approximation, not a verified share-by-share forecast. Equal repurchase and SBC dollars do not guarantee exact share neutrality. FY2026 cash repurchases were $329.1M; employee tax withholdings were separate. An explicit share schedule would require issuance, vesting, and repurchase-price assumptions.
- **Why this gross margin?** The model uses one blended GAAP gross-margin path of 82%, 81%, 80.5%, 80%, and 80%. Hosting costs and revenue mix support the expected decline. Software and services are not projected separately, and non-GAAP guidance is not substituted for GAAP modeled margins.
- **What is the revenue mix?** FY2026 revenue was approximately $606M licenses, $954M subscription services, and $50M professional services and other: approximately 38%, 59%, and 3%. License recognition can occur at a point in time, while SaaS and support are recognized over time. The filing attributes 85% of FY2026 revenue growth to existing customers, supporting—but not proving—the assumption that expansion can require less selling effort.

Source: [UiPath FY2026 10-K](https://www.sec.gov/Archives/edgar/data/1734722/000173472226000012/path-20260131.htm), revenue discussion, financial statements, cash-flow reconciliation and repurchase disclosures. Model implementation and source locators: [Lab 10 analysis](lab10-uipath-proforma.md).

## Questions asked as reviewer — Apple

- **Where does revenue mix come from?** My partner cited the FY2025 10-K's Products and Services Performance table, separating iPhone, Mac, iPad, Wearables/Home/Accessories, and Services. Mac is only part of Apple's revenue.
- **Why is gross margin higher than last year?** My partner cited total gross margin increasing from 46.2% to 46.9%, discussing Services sales and mix, product costs and mix, and tariff pressure.
- **How do you treat buybacks?** My partner described using cash above a $30B floor for repurchases while keeping diluted shares fixed. This is a simplification; its valuation effect depends on how distributions and the share denominator are handled together.
- **Sensitivity question:** “If Services growth slows to mid-single digits, or the Google search payments are cut in half under regulatory pressure, how far does your price target fall, and does your rating still hold?” The numerical effect and whether the rating survives remain unresolved in this note. The next step is to run those cases with other inputs held fixed and compare value with the same dated market price.

Partner-cited source: [Apple FY2025 10-K](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm). The answers above are the student's report of the discussion, not an independent audit of the Apple model.

## Calculation check already recorded in Lab 11

- I previously reported checking Apple's sensitivity units and recomputing the differences: FY2030 gross margin fell from 49% to 46%; operating profit fell from approximately $189B to $173B; value fell from approximately $186 to $171 per share.
- The arithmetic supports a 3-percentage-point input change, approximately $16B less operating profit, and $15 less value per share. This averages approximately $5.3B and $5 per share per point over that range; it does not establish an exact marginal sensitivity.
- **Lab 12 joint source check:** We pulled Products and Services gross-margin data from Apple's FY2025 10-K and confirmed that the partner's historical blended gross margin tied to the reported figure. This supported the historical starting point, not the forecast margin or valuation. This is my report of our check; the Apple workbook has not been independently inspected here.
- **Follow-up calculation:** Recompute blended margin with a lower Services revenue share, then trace the change through profit, cash flow and valuation. No result for that new mix scenario is recorded; it is not claimed as completed.

## Feedback received about UiPath and my response

- **Additional question received:** “What evidence would move you off watch/defer, in either direction? What ARR growth or retention level would make you upgrade or drop it?”
- **My decision signals:** I would move toward considering a buy if cloud ARR growth holds near 19% and net retention rises above approximately 110%. I would drop UiPath from consideration if total ARR growth falls below 10% or net retention remains below approximately 105% for two straight quarters.
- **Qualification:** These are my judgment thresholds for revisiting the forecast, not modeled valuation breakpoints. Stronger expansion would be consistent with the AI thesis but would not establish that AI caused it. Before upgrading, I would need to translate the evidence into revenue, margins and cash flow and rerun valuation to establish upside. No completed scenario establishes that crossing the downside thresholds leaves value almost entirely supported by net cash and free cash flow. Cloud ARR and total ARR are distinct measures and neither translates directly into reported revenue growth.

- **Reported strength:** My partner identified recurring revenue and operating leverage as strengths. Qualification: high software margins do not mean almost all incremental sales become free cash flow; operating costs, taxes, working capital, investment, and required cash reserves still matter.
- **Reported improvement:** My partner questioned flat shares and potential dilution. The model already charges cash for dilution-offset repurchases, so it does not ignore SBC. The valid improvement is to investigate whether that proxy matches actual net issuance; the supplied 20–25% SBC and 3–5% annual dilution claims are not established by this model.

## My explain-back and feedback to the Apple partner

- **Conclusion:** My partner views Apple as fairly valued to modestly undervalued, with limited upside at the price used in their analysis. The exact market-price date and share basis are not recorded here, so this is their reported conclusion rather than an independently verified current-price comparison.
- **Driver:** The thesis is that high-margin Services growth offsets flat iPhone units and expands blended margins. Buybacks can support EPS through fewer shares, but the partner's constant-share model does not explicitly forecast that share-count benefit.
- **Limitation:** The thesis depends on Services margins holding; potential changes to App Store fees and Google payments were not fully stress-tested. Unequal sensitivity ranges also affect output comparisons.
- **Strength:** The segment-level build connects the revenue-mix and margin assumptions to the price target, making the mechanism easy to follow. Our historical blended-margin check supported its starting point.
- **Improvement:** Add downside cases for Services growth and Google payments, tracing each separately through cash flow and value. These are material risks to investigate; the existing results do not establish that they are the largest drivers. Explain the repurchase/constant-share convention consistently when interpreting EPS and value.

## What I will keep, revise, or investigate

- I will keep the SBC cash-cost treatment and blended gross-margin decline from 82% to 80%. I have corrected my written description; I have not changed or rerun the model.
- I will investigate whether assumed repurchases adequately offset actual share issuance. Any explicit dilution scenario must replace or reconcile the existing offset treatment to avoid counting the same cost twice.
- My supported conclusion remains **watch/defer**: the annual-base model gives $5.69 per share and the favorable SG&A case gives $7.31, versus the saved $12.68 market quote from September 24, 2026 at 3:01 p.m. EDT. These are USD values on the model's 537.037M-share basis, not an updated market-date valuation.
- SG&A remains my first research priority because it had the largest value span over the tested ranges and continued efficiency is uncertain. Customer expansion and cash conversion remain supporting evidence to monitor.
- The share-count question clarified that an economic SBC charge and a precise dilution forecast are different. My model has the former; the latter remains a limitation.

## Existing evidence

- [Peer comparison and saved earlier DCF reference](lab08-uipath-comps.md)
- [Pro-forma assumptions, history, sources and checks](lab10-uipath-proforma.md)
- [UiPath model](uipath_proforma.py)
- [Lab 11 sensitivity analysis](lab11-uipath-sensitivity.md)
- [Sensitivity results](lab11-sensitivity-results.md)
- [Presentation handout](Lab-11-UiPath-Presentation.pdf)

## Completion status

The review note now records the presenter answers, reviewer questions, reported joint source check, Apple explain-back, feedback and response. The unanswered Apple downside valuation is explicitly scoped as follow-up work; no new computation is claimed. No reverse DCF has been computed in these Lab 11 results; that gap remains disclosed. This note supports, rather than replaces, the required full presentation and reciprocal review. Upload it with working evidence links to GitHub after those activities are complete. No upload has been performed here.
