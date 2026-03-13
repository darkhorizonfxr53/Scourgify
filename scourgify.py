import sys
import csv

def main():
    #1. Validate exactly 2 command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        #2. Open input to read and output to write
        #newline="" is recommended by CSV docs to prevent blank rows
        with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
            reader = csv.DictReader(infile) #Use csv.DictReader to *read* the csv file

            #Define new column headers
            new_headers = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames=new_headers) # Use csv.DictWriter to *make and write a new* csv file

            #Write the header row to the new file
            writer.writeheader()

            #Loop to run through the names to ogranize it
            for row in reader:
                #row["name"] is "Last, First"
                last, first = row["name"].split(", ")

                #Write cleaned data to the new file
                writer.writerow({
                    "first": first,
                    "last": last,
                    "house": row["house"]
                })

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()
