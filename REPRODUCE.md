# Reproduce the experiments

Extract the three archives in the order listed on the repository homepage. Run these commands from the extracted directory with Python 3.12. Package versions are recorded in requirements-recorded.txt and in the run manifests. The article directory in the repository maps the published figures and tables to their source files.

## Verify the archived results

~~~sh
python -m unittest discover -s experiments/upgrade_v3/tests -t experiments/upgrade_v3 -v
python experiments/upgrade_v3/verify_results.py --run-id expanded_v3
python experiments/upgrade_v3/verify_results.py --run-id revision_v3_20261117
python experiments/upgrade_v3/verify_results.py --run-id submission_final_20261119
~~~

The checks cover solver optimality, capacity constraints, paired objectives, net-value arithmetic and stored cohort partitions. They run on the deposited files.

## Rerun the simulations and benchmarks

~~~sh
python experiments/upgrade_v3/joint_followup.py all --run-id joint_reproduced --workers 4
python experiments/upgrade_v3/coupling_experiment.py --run-id coupling_reproduced --workers 4
python experiments/upgrade_v3/run.py conflict --config experiments/upgrade_v3/config/revision_conflict.json --run-id conflict_reproduced --workers 4
python experiments/upgrade_v3/run.py revision --config experiments/upgrade_v3/config/major_revision.json --run-id sensitivity_reproduced --workers 4
python experiments/upgrade_v3/run.py final_timing --config experiments/upgrade_v3/config/final_revision.json --run-id timing_reproduced
python experiments/upgrade_v3/run.py final_focus --config experiments/upgrade_v3/config/final_revision.json --run-id focus_reproduced --workers 4
~~~

Run the timing benchmark on its own. Times include sorting, optimization and final plan reconstruction, and depend on the machine. The solver option return_frontier=True returns the requested plans and scalar values for each integer budget through the largest requested cap. The deposited timing run includes the full scalar frontiers. The six 100-repetition precision estimates share their first 20 draws with the corresponding heatmap cells.

## Rerun the historical evaluation

Obtain the four cohort files listed in DATA_SOURCES.md and place them at the indicated paths, preserving the original row order. Run the evaluation before the penalty-path analysis so that fitted scores are available.

~~~sh
python experiments/upgrade_v3/run.py all --config experiments/upgrade_v3/config/full.json --run-id historical_reproduced --workers 4
python experiments/upgrade_v3/penalty_path.py --run-id historical_reproduced
~~~

Saved split_ids.npz files contain partition identifiers. The accompanying design.json files record sample sizes and fitted model choices. The three promotion splits share one external test cohort. Transfer costs and incumbent lists are specified scenarios.

## Regenerate plots and tables

~~~sh
python papers/dss/v3_joint_reallocation/publication_figures.py
python papers/dss/v3_joint_reallocation/revision_figures.py
python experiments/upgrade_v3/revision_outputs.py
python experiments/upgrade_v3/final_outputs.py
~~~

These scripts read the deposited runs by default. To draw Figure 3 from the four method means, run python article/extract_results.py from the repository clone, then run xelatex figure_3.tex inside article/.
