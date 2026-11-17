# Joint selection and transfer matching reproduction archive

This archive accompanies the journal-formatted main manuscript. It contains
the optimizer, comparison methods, simulation and historical-evaluation programs,
complete result tables, configuration files, random seeds and figure sources.
Run commands from the directory containing this README with Python 3.12.
Recorded package versions are in requirements-recorded.txt and the run manifests.

## Inspect the evidence

- expanded_v3/coupling: the controlled compatibility experiment (Figure 3).
- joint_v3_20261117/mechanisms: the full structural grid (Table 2 and Figure 4).
- joint_v3_20261117/benchmark: compact type-flow and network-LP timings (Table 4).
- revision_v3_20261117/conflict: 48 resource-competition cells, four budgets,
  5,760 paired evaluations and 17,280 method rows (Table 3 and Figure 5).
- expanded_v3/empirical: cohort designs, candidate results, frozen adoption
  choices and held-out estimates (Tables 5 and 6).
- expanded_v3/penalty_path: all five penalty levels and adoption decisions.
- expanded_v3/simulate and scale: the broader evaluation and scaling experiments.

All result directories are below experiments/upgrade_v3/results/. Aggregated and
replicate tables contain every scenario, including score-noise settings and cases
where methods coincide. Budgets on the same population are paired evaluations.
The 23.0% headline refers to known benefits and strong specialist-resource competition.

## Run the core tests and check saved results

```text
python -m unittest discover -s experiments/upgrade_v3/tests -t experiments/upgrade_v3 -v
python experiments/upgrade_v3/verify_results.py --run-id revision_v3_20261117
python experiments/upgrade_v3/verify_results.py --run-id expanded_v3
```

These checks require no original cohort inputs. They examine solver optimality,
paired objectives, capacity constraints, net-value arithmetic and stored partitions.

## Regenerate the six main figures from the included outputs

```text
python papers/dss/v3_joint_reallocation/publication_figures.py
python papers/dss/v3_joint_reallocation/revision_figures.py
```

The plots are written to papers/dss/v3_joint_reallocation/figures/. Local layout
auditing is optional; it does not enter the data calculations or plot construction.
The manuscript source is distributed separately as DSS_v3_latex_source.zip.

## Rerun the controlled experiments

Use new run names to keep the supplied completed results available for comparison.

```text
python experiments/upgrade_v3/run.py conflict --config experiments/upgrade_v3/config/revision_conflict.json --run-id conflict_reproduced --workers 4
python experiments/upgrade_v3/joint_followup.py all --run-id joint_reproduced --workers 4
python experiments/upgrade_v3/coupling_experiment.py --run-id expanded_reproduced --workers 4
```

The timing experiment should run without other compute-intensive tasks. Its
elapsed times are observations on the recorded machine, not fixed expected values.
Figure scripts read the supplied published-run directories by default; after a
new run, change their RUN/root paths to the desired run before plotting it.

## Rerun the historical evaluation and broader experiments

Obtain the four input files listed in DATA_SOURCES.md and place them at the paths
shown there, retaining the original row order. Then run:

```text
python experiments/upgrade_v3/run.py all --config experiments/upgrade_v3/config/full.json --run-id expanded_reproduced --workers 4
python experiments/upgrade_v3/penalty_path.py --run-id expanded_reproduced
```

The original input records and record-level outcome/score arrays are not included.
Historical model fitting regenerates those arrays before the penalty-path analysis.
The supplied split_ids.npz files contain partition identifiers; design.json files
document source locations, sample counts and selected models. The three promotion
splits share an external test cohort. Historical costs are specified scenarios,
and incumbent lists are constructed policies. All 972 recorded adoption decisions
retain the incumbent allocation.
