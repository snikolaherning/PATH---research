# Lab 07 — Asbury comparable-company valuation

## Represent — peer policy before valuation

### My response

1. AutoNation and Group 1 are candidates because they are publicly traded franchised vehicle retailers. Their shared revenue sources, including new and used vehicle sales, parts and service, and finance and insurance products, give them similar core business economics to Asbury.

2. Both are strong candidates, but neither is identical to Asbury. AutoNation's finance business may affect its risk, capital needs, and earnings mix. Group 1 needs a qualification because it operates in the United States and United Kingdom and acquired 54 Inchcape dealerships during 2024. These differences do not require exclusion, but they should be disclosed.

3. I would use AutoNation and Group 1 because their core operating characteristics are similar to Asbury's. I would treat AutoNation as a peer with a noted limitation and Group 1 as a qualified peer. Asbury is the target, so I would exclude it from its own peer set.

### Comparison policy

The peer set should include publicly traded franchised vehicle retailers with positive GAAP earnings and business models that meaningfully overlap with Asbury Automotive. Relevant similarities include new and used vehicle sales, parts and service operations, and finance and insurance products. Material differences in geography, acquisitions, financing activities, risk, and earnings definitions must be identified rather than hidden in the peer average.

### AutoNation

**Decision: Use, with a noted limitation.** AutoNation is a reasonable peer because its core dealership activities resemble Asbury's. Both companies sell new and used vehicles and earn meaningful revenue from parts, service, and finance and insurance products. AutoNation also operates AutoNation Finance, which can affect its risk, capital requirements, and earnings mix. This difference deserves attention but does not make the core business comparison unusable.

### Group 1 Automotive

**Decision: Qualify and use.** Group 1's franchised dealership operations fit Asbury's core business economics. However, Group 1 operates in both the United States and United Kingdom, while its acquisition of 54 Inchcape dealerships during 2024 affects the scale and composition of the earnings being compared. These geographic and acquisition differences require an explicit qualification.

### Asbury Automotive

**Decision: Exclude from the peer set.** Asbury is the valuation target and cannot be included in its own peer median. Its observed P/E may be shown separately for comparison, but it cannot determine the peer-implied valuation applied to Asbury.

### Conclusion before reviewing the multiples

AutoNation belongs in the peer set because its core operating model closely matches Asbury's. Group 1 also belongs, but its international exposure and acquisition activity make it a qualified peer. This decision is based on business evidence rather than which combination produces a preferred valuation result.

## Implement — worked-case calculation

The calculator is saved as `asbury_comps.py` and uses only Python's standard library. The editable input block identifies Asbury as the target and AutoNation and Group 1 as peers. The program deduplicates peers, excludes the target from its own peer set, rejects missing or nonpositive prices and diluted EPS, and retains full precision until display.

One manual calculation is:

`AutoNation implied Asbury price = (169.84 / 16.92) × 21.50 = $215.81`

The complete calculation produced:

| Result | Value |
| --- | ---: |
| AutoNation P/E | 10.037825× |
| Group 1 P/E | 11.450149× |
| Peer median P/E | 10.743987× |
| Asbury peer-implied minimum | $215.81 |
| Asbury peer-implied median | $231.00 |
| Asbury peer-implied maximum | $246.18 |
| Asbury peer-implied range | $215.81–$246.18 |
| Remove AutoNation | $246.18, a +$15.18 change |
| Remove Group 1 | $215.81, a −$15.18 change |

The P/E calculation values shareholders' earnings directly, so the model does not add cash or subtract debt.

### Run command

```bash
python3 asbury_comps.py
```

## Validate — reproduction and robustness checks

The calculator reproduced every result supplied in the lab:

| Validation check | Expected | Calculated | Result |
| --- | ---: | ---: | --- |
| AutoNation P/E | 10.037825× | 10.037825× | Pass |
| Group 1 P/E | 11.450149× | 11.450149× | Pass |
| Peer median P/E | 10.743987× | 10.743987× | Pass |
| Asbury peer-implied minimum | $215.81 | $215.81 | Pass |
| Asbury peer-implied maximum | $246.18 | $246.18 | Pass |
| Asbury at peer median | $231.00 | $231.00 | Pass |
| Remove Group 1 estimate | $215.81 | $215.81 | Pass |
| Change after removing Group 1 | −$15.18 | −$15.18 | Pass |

The program retains the unrounded P/E multiples when calculating implied prices and leave-one-out changes. It rounds only the displayed multiples and prices.

Additional tests confirmed that the calculator:

- removes a duplicate AutoNation observation;
- excludes Asbury if it is accidentally included in the peer list;
- labels zero, negative, or missing price and EPS inputs as not meaningful;
- reports a reference estimate and no range when only one valid peer remains; and
- reports no usable peers when none have meaningful inputs.

Removing Group 1 lowers the implied price from $231.00 to $215.81 because Group 1 has the higher P/E multiple. The unrounded change is displayed as −$15.18. With only AutoNation remaining, the output is a single reference estimate rather than a peer-implied range.

## Evolve — remove Group 1

### Prediction

I predicted that removing Group 1 would lower Asbury's estimated price because Group 1's P/E is higher, which tells us investors are paying more for its earnings. Removing a higher number would lower the dataset as a whole.

### Result

With both peers, the median P/E is 10.743987× and Asbury's median-implied price is $231.00. After removing Group 1, AutoNation's 10.037825× P/E produces an Asbury reference estimate of $215.81. The change from the original two-peer estimate is −$15.18, calculated with unrounded values.

## Reflect

Completed orally in class.
