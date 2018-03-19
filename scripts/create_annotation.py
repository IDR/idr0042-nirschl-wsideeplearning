#!/usr/bin/env python
# Generate annotation.csv from original assays file

import pandas
import os
from os.path import join

scripts_dir = os.path.dirname(os.path.realpath(__file__))
assays_file = join(
    scripts_dir, "..", "experimentA", "idr0042-experimentA-assays.txt")

# Read the assays file
df = pandas.read_csv(assays_file, sep='\t')

# Generate the dataset and image name columns
df['Dataset Name'] = df['Assay Name']
df.rename(index=str, columns={'Source Name': 'Image Name'}, inplace=True)

# Reorder columns
cols = df.columns.tolist()
cols.insert(0, cols.pop(cols.index('Dataset Name')))
df = df[cols]

# Create annotation
df.to_csv(
    join(scripts_dir, "..", "experimentA/idr0042-experimentA-annotation.csv"),
    sep=',', index=False)
