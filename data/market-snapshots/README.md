# Real market snapshot — 20 November 2026

[Download the summary CSV](2026-11-20-summary.csv). It summarizes **450 real live-search results** collected through Kleinanzeigen Agent, with 50 returned for each of nine searches. Collection timestamps in the CSV are UTC; the searches took place on 20 November in Berlin local time.

| Search | Results | Numeric EUR prices | Median asking price in returned results |
| --- | ---: | ---: | ---: |
| iPhone 13 | 50 | 50 | €245 |
| iPhone 18 | 50 | 49 | €1,300 |
| PlayStation 5 | 50 | 46 | €550 |
| Volkswagen Golf | 50 | 49 | €7,980 |
| IKEA Kallax | 50 | 46 | €25 |
| Adidas Samba | 50 | 49 | €55 |
| Board games | 50 | 49 | €15 |
| Musical instruments | 50 | 49 | €280 |
| Mini- and Nebenjobs | 50 | 0 | Not available |

## Method and important limitations

- One live search per row, newest-first, first page only, maximum 50 results; filters and exact UTC capture time are in the CSV. Board games use the keyword `Brettspiel` in the Spielzeug category. Instruments and jobs use their category without a keyword. Phone and console searches use category filters; furniture and shoes use only the stated keyword.
- Medians are calculated from nonnegative numeric prices marked EUR in the response. Missing prices are excluded, never replaced by zero. No numeric job salaries were returned; an empty price is not zero pay.
- Values are **asking prices**, not verified sale prices. Results have not been manually verified or deduplicated; unrelated models, accessories, bundles, wanted ads, incomplete descriptions or incorrectly labelled listings can appear. In particular, a search for iPhone 18 does not prove that each result is an iPhone 18 device. Categories such as musical instruments contain very different products. These medians describe the returned rows only and are **not reliable market valuations**.
- The sample is neither random nor representative and offers no trend, historical comparison or claim about the whole platform. No listing text, seller names, contact information or individual records are republished here.

Source: [Kleinanzeigen Agent live search](https://kleinanzeigen-agent.de/dokumentation), based on Kleinanzeigen data. We publish only aggregate counts and medians here; the provider's [terms](https://kleinanzeigen-agent.de/agb) restrict certain redistribution of raw data. Check the source and rights before reuse. This project is independent and not affiliated with either service.
