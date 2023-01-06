About
====

Mostly various python plotting scripts. Quite a range including some old scripts which are rarely used. For internal reference only.

Require installation of NumPy, Matplotlib, SciPy and Pandas.

Scipts of note
====

### Handling multiple datasets

for plotting manual legend entries:
```
multiple_legend.py
```

multiple things, including loading multiple repeats of data into a 2D array for mean+sd analyses:
```
PLOT_1D_dens.py
```

loading multiple data sets into a single 1D array:
```
PLOT_msd_2D.py
```

combining csv contact files into one array in bash
```
get_average_from_csv.sh
```

get and average data PMF data as 1D arrays, put into a 2D array and average (as per https://doi.org/10.1021/acs.jctc.9b00548)
```
PLOT_PMF_average.py
```

count number of columns, and plot each one as a separate line according to a cmap. This is a nice general time series plotting script.
```
PLOT_flip_count_col.py
```


### Densities and 2D plots

some cool matrix stuff
```
RMSD_2D.py
```

aligning densities for pseduo density plots
```
PLOT_meta_heatmap.py
```

nice 2D array plot
```
PLOT_dens_2D.py
```

Using MDanalysis to read multiple files and write a density file (as per https://doi.org/10.1038/s41467-021-25242-x)
```
site_occupancy.py
```

### Specific code of use

example of glob being used for finding all files in dir by extenion
```
analyse_rmsf.py
```

awk script for summing columns
```
combine_to_av2.sh
```

summing all columns of a file - a useful replacement for awk
```
column_stats.py
```

getting averages with grep
```
get_res.py
```

### Specific plotting files of note

plot residue contact maps (as per https://doi.org/10.7554/eLife.80988)
```
PLOT_contact.py
```

cylinder analysis in MDAnalysis - essentially a refined RDF analysis, as per https://doi.org/10.1101/2022.12.13.520211)
Some nice MDAanalysis syntax used
```
cylinder_CLA.py
```


