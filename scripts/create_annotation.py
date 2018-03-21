#!/usr/bin/env python
# Generate annotation.csv from original assays file

import logging
import pandas
import os
from os.path import join

logging.basicConfig(level=logging.DEBUG)

scripts_dir = os.path.dirname(os.path.realpath(__file__))
assays_file = os.path.join(
    scripts_dir, "..", "experimentA", "idr0042-experimentA-assays.txt")
logging.info("Reading %s" % assays_file)

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
csv_file = os.path.join(
    scripts_dir, "..", "experimentA", "idr0042-experimentA-annotation.csv")
logging.info("Generating %s" % csv_file)
df.to_csv(csv_file, sep=',', index=False)
