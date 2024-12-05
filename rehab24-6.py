import os
import numpy as np
import pandas as pd

# Paths
base_input_folder = '/home/ali/datasets/REHAB24-6/2d_joints'  # Replace with your folder path
base_output_folder = '/home/ali/datasets/REHAB24-6/2d_joints_segmented'  # Replace with your output folder path
csv_path = '/home/ali/datasets/REHAB24-6/Segmentation.csv'  # Replace with your CSV file path
output_csv_path = os.path.join(base_output_folder, 'annotations.csv')  # Replace with your output CSV file path

# Create segmented output folders
for i in range(1, 7):  # For Ex1 to Ex6
    os.makedirs(os.path.join(base_output_folder, f"Ex{i}-segmented"), exist_ok=True)

# Read the CSV file
csv_data = pd.read_csv(csv_path, delimiter=';')

# Cameras to process
cameras = ['c17', 'c18']

# List to store segmented file metadata
segmented_files_info = []

# Process each exercise ID
for exercise_id in range(1, 7):  # Exercise IDs 1 to 6
    # Filter rows based on the current exercise ID
    filtered_data = csv_data[csv_data['exercise_id'] == exercise_id]

    # Input and output folders for the current exercise ID
    input_folder = os.path.join(base_input_folder, f"Ex{exercise_id}")
    output_folder = os.path.join(base_output_folder, f"Ex{exercise_id}-segmented")

    # Process each row in the filtered data
    for _, row in filtered_data.iterrows():
        video_id = row['video_id']
        repetition_number = row['repetition_number']
        first_frame = row['first_frame']
        last_frame = row['last_frame']
        person_id = row['person_id']
        correctness = row['correctness']

        # Ensure exercise_subtype is a string, use "unknown" if missing
        exercise_subtype = str(row['exercise_subtype']).replace(' ', '').lower() if pd.notna(
            row['exercise_subtype']) else "unknown"

        for camera in cameras:
            # Construct the Numpy file name
            npy_file_name = f"{video_id}-{camera}-30fps.npy"
            npy_file_path = os.path.join(input_folder, npy_file_name)

            # Check if the Numpy file exists
            if os.path.exists(npy_file_path):
                # Load the Numpy file
                data = np.load(npy_file_path)

                # Extract frames for the repetition
                repetition_data = data[first_frame:last_frame + 1]

                # Save the extracted repetition data to the corresponding segmented folder
                output_file_name = f"{video_id}_{camera}_{exercise_subtype}-{person_id}-rep{repetition_number}-{correctness}.npy"
                output_file_path = os.path.join(output_folder, output_file_name)
                np.save(output_file_path, repetition_data)

                # Add metadata to the list
                segmented_files_info.append({
                    'file_name': output_file_name,
                    'person_id': person_id,
                    'exercise_id': exercise_id,
                    'correctness': correctness,
                    **row.to_dict()
                })
            else:
                print(f"File not found: {npy_file_path}")

# Create a DataFrame from the segmented files metadata
segmented_files_df = pd.DataFrame(segmented_files_info)

# Ensure proper column order
column_order = ['file_name', 'person_id', 'exercise_id', 'correctness'] + [col for col in csv_data.columns if
                                                                           col not in ['file_name', 'person_id',
                                                                                       'exercise_id', 'correctness']]
segmented_files_df = segmented_files_df[column_order]

# Save the metadata to a CSV file
segmented_files_df.to_csv(output_csv_path, index=False)


segmented_files_df['correctness'].to_numpy()
