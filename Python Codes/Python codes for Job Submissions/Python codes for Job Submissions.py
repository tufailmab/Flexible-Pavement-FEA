# Find this code instructins here in this repo: https://github.com/tufailmab/Abaqus-Batch-Submit-Job
# For Job Submission, you need this code to use:
import subprocess
import os

def submit_job(job_name):
    # Submit the ABAQUS job using the command prompt
    command = f"ABAQUS J={job_name}.inp cpus=2 int"
    print(f"Job '{job_name}' Submitted...")
    subprocess.run(command, shell=True)

def find_inp_file():
    # Search for the first .inp file in the current directory
    for file in os.listdir():
        if file.endswith(".inp"):
            return file.replace(".inp", "")  # Return the job name without the extension
    return None

def main():
    # Automatically search for the .inp file in the current directory
    job_name = find_inp_file()
    
    if job_name:
        # Submit the ABAQUS job if the .inp file is found
        submit_job(job_name)
    else:
        print("No .inp file found in the current directory.")

if __name__ == "__main__":
    main()

