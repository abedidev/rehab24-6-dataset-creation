
# Preprocessing REHAB24-6 Rehabilitation Exercise Dataset

---

## Overview

This repository contains a Python script for processing, segmenting, and annotating rehabilitation exercise data. The script reads synchronized video and skeletal data (e.g., `.npy` files) and a CSV file containing metadata (e.g., `exercise_id`, `correctness`). It segments the data into individual repetitions based on the provided metadata and generates a structured output. 

The output includes:
1. Segmented `.npy` files for each repetition, named according to the metadata.
2. An annotated CSV file detailing information about each segmented repetition, including filenames, correctness labels, and other attributes.

This code has been developed with inspiration from the research paper *"REHAB24-6: Physical Therapy Dataset for Analyzing Pose Estimation Methods"* by Černek et al. The dataset described in the paper emphasizes temporal segmentation and correctness labeling for rehabilitation exercises, aligning with the functionality of this code.

---

## Features

- **Input Handling**: Processes unsegmented `.npy` files and metadata CSV files.
- **Temporal Segmentation**: Splits data into individual repetitions using start and end frames.
- **Dynamic Naming**: Outputs `.npy` files with meaningful names incorporating metadata (e.g., `correctness`, `exercise_subtype`).
- **CSV Output**: Generates a comprehensive CSV file with metadata for each segmented file.
- **Customizability**: Supports multiple camera views (`c17` and `c18`) and handles various exercises with subtypes.

---

## File Naming Convention

The segmented files are named as:
```
{video_id}_{camera}_{exercise_subtype}-{person_id}-rep{repetition_number}-{correctness}.npy
```

For example:
```
PM_000_c17_rightarm-1-rep1-1.npy
```

**Explanation**:
- `PM_000`: Video ID.
- `c17`: Camera view (horizontal or vertical).
- `rightarm`: Exercise subtype (space removed and converted to lowercase).
- `1`: Person ID.
- `rep1`: Repetition number.
- `1`: Correctness label (`1` for correct, `0` for incorrect).

---

## Output CSV Structure

The output CSV contains the following columns (in this order):
1. `file_name`: Name of the segmented `.npy` file.
2. `person_id`: ID of the person performing the exercise.
3. `exercise_id`: ID of the exercise.
4. `correctness`: Indicates if the repetition was correct (`1`) or incorrect (`0`).
5. Additional metadata columns from the input CSV (e.g., `video_id`, `repetition_number`, `first_frame`, etc.).

---

## Prerequisites

- **Python 3.x**
- Required libraries:
  - `numpy`
  - `pandas`
  - `os`

Install dependencies using:
```bash
pip install numpy pandas
```

---

## Usage

1. **Prepare Input Files**:
   - Place `.npy` files in folders named `Ex1`, `Ex2`, ..., `Ex6` corresponding to exercise IDs.
   - Prepare the metadata CSV file with columns such as `exercise_id`, `correctness`, `person_id`, `first_frame`, and `last_frame`.

2. **Run the Script**:
   Update the paths in the script for:
   - `base_input_folder`: Folder containing `Ex1`, `Ex2`, ..., `Ex6`.
   - `csv_path`: Path to the input metadata CSV file.
   - `base_output_folder`: Destination folder for segmented files.
   - `output_csv_path`: Destination path for the output CSV file.

   Execute the script:
   ```bash
   python segment_and_annotate.py
   ```

3. **Output**:
   - Segmented `.npy` files in folders named `Ex1-segmented`, `Ex2-segmented`, ..., `Ex6-segmented`.
   - A CSV file containing metadata for each segmented file.

---


## Acknowledgments

This work is inspired by the *REHAB24-6* dataset introduced in the paper *"REHAB24-6: Physical Therapy Dataset for Analyzing Pose Estimation Methods"* by Černek et al. The dataset is publicly available on Zenodo: [https://doi.org/10.5281/zenodo.13305825](https://doi.org/10.5281/zenodo.13305825).

For further inquiries or collaboration, feel free to contact the repository maintainers.
