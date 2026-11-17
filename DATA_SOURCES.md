# Data sources and input locations

Paths are relative to the extracted archive. The input folder exists so the data
reader can locate the project root before the source files are added.

| Source | Source location | Required local file | Rows |
|---|---|---|---:|
| Hillstrom email challenge | https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html | papers/dss/r6/input/hillstrom.csv | 64,000 |
| Karlan and List charitable giving | https://doi.org/10.7910/DVN/27853 | papers/dss/r6/input/AER_merged.dta | 50,083 |
| Udacity promotion development cohort | https://github.com/udacity/DSND_Term2/tree/master/portfolio_exercises/Experiments/data | papers/dss/r6/sources/udacity/training.csv | 84,534 |
| Udacity external evaluation cohort | Same official repository | papers/dss/r6/sources/udacity/Test.csv | 41,650 |

The Karlan–List deposit is also linked by the implementing research organization:
https://poverty-action.org/study/effect-matching-ratios-charitable-giving-united-states.
The source project acquired AER_merged.dta from the research replication mirror
documented at https://github.com/vayalinkal/mhtexp2/blob/main/replication/readme.md
when the original deposit required a guestbook response. Follow the source's normal
access process. Row ordering affects the saved split identifiers.

Hillstrom inputs use recency, history, mens, womens, newbie, zip_code, channel,
segment and visit. Karlan–List inputs use treatment, gave, hpa, ltmedmra, freq,
years, mrm2 and dormant. Promotion inputs use ID, Promotion, purchase and V1–V7.
upgrade/data.py contains the exact loading and preprocessing rules. Promotion is
an educational benchmark; the other two sources are historical randomized studies.

The archive redistributes generated simulation records and aggregate evaluation
outputs, not original cohort records. Original data access and reuse conditions
remain those specified by the data providers. Research data and code are deposited
at https://github.com/pursuerswift/dss-joint-reallocation. No dataset DOI has been assigned.
