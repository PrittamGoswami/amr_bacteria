
import os
import subprocess

def run_CARD_rgi(bacterial_genomes_directory, output_dir_path, num_threads):
    # Iterate through each sub-directory corresponding to a bacterium
    for bacteria in os.listdir(bacterial_genomes_directory):
        # Get the genome file of the bacterium
        genome_file = os.listdir(f"{bacterial_genomes_directory}/{bacteria}/")[0]
        input_file_path = f"{bacterial_genomes_directory}/{bacteria}/{genome_file}"
        
        # Create the sub-directory corresponding to the bacterium for saving results
        os.makedirs(f"{output_dir_path}/{bacteria}", exist_ok=True)
        output_file_path = os.path.join(output_dir_path, bacteria, genome_file.split("_genomic.fna")[0])
        
        # Run CARD RGI
        subprocess.run(
            [
                "rgi", "main",
                "--input_sequence", input_file_path,
                "--output_file", output_file_path,
                "-n", str(num_threads),
                "--include_loose",
                "--clean"
            ],
            check=True
        )
        
        # Remove JSON output files if they exist as they occupy too much space
        json_file = f"{output_file_path}.json"
        if os.path.exists(json_file):
            os.remove(json_file)
            print(f"Removed JSON file: {json_file}")
        
        print(f"BLAST search completed. Results saved to {output_file_path}")

# Directory where we want to save the RGI results
output_dir_path = "CARD_AMR_Prediction"

# Create the directory if it does not already exist
os.makedirs(output_dir_path, exist_ok=True)

# Number of threads to use
num_threads = "30"

# Directory contatining the bacterial genomes
bacterial_genomes_directory = "ncbi_complete_refseq_bacteria_dataset/Genomes/"
run_CARD_rgi(bacterial_genomes_directory, output_dir_path, num_threads)
