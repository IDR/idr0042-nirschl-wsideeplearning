#!/usr/bin/env python
# Generate filePaths tsv file with raw files

from glob import glob
import os
from os.path import join
import sys

BASE_DIRECTORY = "/uod/idr/filesets/idr0042-nirschl-wsideeplearning/"
ASSAYS = {
    "held-out_validation": "test",
    "training/fold_1": "training",
    "training/test_fold_1": "training",
}

if not os.path.exists(BASE_DIRECTORY):
    print("Cannot find the raw data directory. Exiting.")
    sys.exit(0)

# Determine base location for pattern files
metadata_dir = os.path.dirname(os.path.realpath(__file__))
filepaths_file = join(metadata_dir, "..", "experimentA",
                      "idr0042-experimentA-filePaths.tsv")

if os.path.exists(filepaths_file):
    os.remove(filepaths_file)
print("Creating %s" % filepaths_file)

# List all assay folders under base directory
for d in ASSAYS.keys():
    pngs = sorted([x for x in glob(join(BASE_DIRECTORY, d) + "/*")])

    with open(filepaths_file, 'a') as f:
        for png in pngs:
            f.write("Dataset:name:%s\t%s\n" % (ASSAYS[d], png))
