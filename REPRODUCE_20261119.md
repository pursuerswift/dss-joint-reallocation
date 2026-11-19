# Reproduce the 19 November 2026 submission revision

Download DSS_v3_reproduction.zip, DSS_v3_update_20261119.zip and DSS_v3_frontiers_20261119.zip from this repository. Extract the original first, then the update, then the frontier archive into the same empty directory, replacing matching files. These archives jointly reproduce the reviewed self-contained local package. The archive merges the original reproduction material with revised algorithm code, the 18 November experiment and the current targeted experiment. Original cohort records are excluded; see DATA_SOURCES.md. Recorded package versions are preserved in run manifests and requirements-recorded.txt.

From the extracted root with a scientific Python environment:

```sh
python -m unittest discover -s experiments/upgrade_v3/tests -t experiments/upgrade_v3 -v
python experiments/upgrade_v3/run.py final_timing --config experiments/upgrade_v3/config/final_revision.json --run-id final_new
python experiments/upgrade_v3/run.py final_focus --config experiments/upgrade_v3/config/final_revision.json --run-id final_new --workers 4
python experiments/upgrade_v3/verify_results.py --run-id final_new
python experiments/upgrade_v3/final_outputs.py
```

Run timing alone before launching parallel simulations. final_outputs.py regenerates the submitted tables/interval figure from the included locked run submission_final_20261119. Change its RUN variable to regenerate from final_new. It also reads the included major_revision_20261118 strong-cost results. That older run can be reproduced using run.py revision --config experiments/upgrade_v3/config/major_revision.json --run-id major_new --workers 4.

The two solver APIs accept return_frontier=True and return (requested_plans, scalar_values). Values cover all integer upper bounds through max(caps); only explicitly requested individual plans are materialized. Type Flow is globally exact for the supplied objective; Stop is exact over score prefixes. Timing includes sorting, optimization and one final reconstruction for each method. Entire frontiers are in final_timing/frontiers.csv; pointwise MC intervals are in final_focus/contrasts.csv.

The original heatmap uses 20 draws per cell. Six highlighted cells extend those same draws to 100; do not pool them as independent confirmation experiments. All inputs, seed construction and measurement scopes are documented in config/final_revision.json and upgrade/final_revision.py. Historical training was not rerun in this revision.
