# Joint Selection and Transfer Matching for Resource Reallocation at Fixed Capacity

Research data and analysis code accompanying the manuscript by Lei Tan, Wuhan Textile University.

## Download and reproduce

Download [DSS_v3_reproduction.zip](DSS_v3_reproduction.zip) and extract it into an empty directory. The archive contains **170 files** (approximately **4.2 MiB** compressed): analysis code, experiment configurations, complete result tables, random seeds, partition identifiers and figure-generation programs.

Follow [REPRODUCE.md](REPRODUCE.md) for test, analysis and plotting commands. The commands run from the extracted archive directory with Python 3.12. Recorded dependency versions are in [requirements-recorded.txt](requirements-recorded.txt).

```bash
python -m pip install -r requirements-recorded.txt
python -m unittest discover -s experiments/upgrade_v3/tests -t experiments/upgrade_v3 -v
python experiments/upgrade_v3/verify_results.py --run-id revision_v3_20261117
python experiments/upgrade_v3/verify_results.py --run-id expanded_v3
python papers/dss/v3_joint_reallocation/publication_figures.py
python papers/dss/v3_joint_reallocation/revision_figures.py
```

Core tests, result checks and regeneration of the six main figures use the included outputs. Rerunning historical model fitting requires the source inputs listed in [DATA_SOURCES.md](DATA_SOURCES.md).

## Research contents

| Evidence | Location within the ZIP | Manuscript display |
|---|---|---|
| Controlled compatibility experiment | `experiments/upgrade_v3/results/expanded_v3/coupling/` | Figure 3 |
| Complete structural grid | `experiments/upgrade_v3/results/joint_v3_20261117/mechanisms/` | Table 2, Figure 4 |
| Resource competition, score noise and exchange budgets | `experiments/upgrade_v3/results/revision_v3_20261117/conflict/` | Table 3, Figure 5 |
| Exact solver timings | `experiments/upgrade_v3/results/joint_v3_20261117/benchmark/` | Table 4, Figure 6 |
| Historical-cohort and benchmark evaluation | `experiments/upgrade_v3/results/expanded_v3/empirical/` | Tables 5–6 |
| Evidence-penalty path | `experiments/upgrade_v3/results/expanded_v3/penalty_path/` | Historical decision analysis |
| Broader simulations and scaling | `experiments/upgrade_v3/results/expanded_v3/simulate/` and `scale/` | Complete supporting results |

[FILE_INDEX.csv](FILE_INDEX.csv) lists every archive file. The full experimental grids are retained, including all evaluated cost, noise and exchange-budget conditions. The competition experiment contains 48 scenario cells, 1,440 repetitions and 5,760 paired budget evaluations.

## Original data and access

Historical analyses reuse the Hillstrom email challenge, the Karlan–List charitable-giving experiment and the Udacity promotion exercise. Original cohort records are obtained from their respective providers and are not redistributed here. The archive includes generated simulation results, aggregate historical outputs and saved partition identifiers. See [DATA_SOURCES.md](DATA_SOURCES.md) for exact input filenames, source links and preprocessing details.

## Version and citation

Research version: **v3, 2026-11-17**. Citation metadata is provided in [CITATION.cff](CITATION.cff). No DOI has been assigned. The repository contains research data and code; manuscript and submission correspondence are maintained separately.

Data-provider reuse conditions continue to apply to original datasets. No additional reuse licence has been selected for this deposit.
