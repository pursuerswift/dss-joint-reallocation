# Joint Selection and Transfer Matching for Resource Reallocation at Fixed Capacity

This repository contains the optimization code, paired simulation results and aggregate evaluations for three historical cohorts. The [figure and table guide](article/README.md) identifies the source of each display in the article.

To regenerate the values in Figure 3 and Table 7 directly from a clone, run:

~~~sh
python article/extract_results.py
~~~

For the full experiments, extract the following archives into the same directory in the order shown. Allow files from the second archive to replace matching files from the first.

1. [Solvers, simulations and historical evaluations](DSS_v3_reproduction.zip)
2. [Cost sensitivity, score noise and timing experiments](DSS_v3_update_20261119.zip)
3. [Complete scalar budget frontiers](DSS_v3_frontiers_20261119.zip)

The [reproduction guide](REPRODUCE.md) gives the commands for checking the results and rerunning the experiments. The [file index](FILE_INDEX.csv) lists the contents of the combined archives. For original cohort records, see [data sources and input paths](DATA_SOURCES.md).
