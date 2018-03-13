#!/usr/bin/env python
# Generate annotation.csv from original assays file

import pandas

TEST_FILE = 'nirschl_upenn_heart_test_image_assay_metadata.txt'
TRAINING_FILE = 'nirschl_upenn_heart_training_image_assay_metadata.txt'


# Read the assays file
df1 = pandas.read_csv('experimentA/%s' % TEST_FILE, sep='\t')
df2 = pandas.read_csv('experimentA/%s' % TRAINING_FILE, sep='\t')
df = pandas.concat([df1, df2])

# Generate the dataset and image name columns
df['Dataset Name'] = df['Assay Name']
df.rename(index=str, columns={
    'Source Name': 'Image Name',
    'Characteristics [Ethnic/ Racial group]':
        'Characteristics [Ethnic or Racial group]'}, inplace=True)

# Reorder columns
cols = df.columns.tolist()
cols.insert(0, cols.pop(cols.index('Dataset Name')))
df = df[cols]

# Create annotation
df.to_csv('experimentA/idr0042-experimentA-annotation.csv', sep=',',
          index=False)
