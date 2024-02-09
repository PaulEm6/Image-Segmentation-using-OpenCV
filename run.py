# pylint: skip-file

import os
import subprocess
import pandas as pd

script_path_1 = os.path.join(os.getcwd(), "SLIC.py")

df = pd.DataFrame([], columns=['Moyenne de B', 'Moyenne de G', 'Moyenne de R'])

def explore_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            # Run an external script with the file_path as an argument
            if ("with" not in file_path) and ("image" not in file_path):
                print("Processing file: " + str(file_path))
                subprocess.run(["python", script_path_1, file_path])

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python /path/to/folder")
    else:
        folder_path = sys.argv[1]
        if os.path.exists(folder_path) and os.path.exists(script_path_1):
            csv_path = os.path.join(folder_path, "image.csv")
            df.to_csv(csv_path, mode='a', index=False)
            explore_folder(folder_path)
        else:
            print("Folder or script does not exist.")


