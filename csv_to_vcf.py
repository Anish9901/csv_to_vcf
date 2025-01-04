import pandas as pd

# Load the CSV file
file_path = 'contacts.csv'
contacts_df = pd.read_csv(file_path)


# Define a function to include all contact numbers in the VCF
def csv_to_vcf(row):
    vcf_entry = [
        "BEGIN:VCARD",
        "VERSION:3.0",
        f"N:{row['Full Name']};;;",
        f"FN:{row['Full Name']}",
    ]

    # Add all phone numbers with proper labels if they are not empty
    if not pd.isna(row['Primary Phone']):
        vcf_entry.append(f"TEL;TYPE=CELL:{row['Primary Phone']}")
    if not pd.isna(row['Work Phone']):
        vcf_entry.append(f"TEL;TYPE=WORK:{row['Work Phone']}")
    if not pd.isna(row['Home Phone']):
        vcf_entry.append(f"TEL;TYPE=HOME:{row['Home Phone']}")
    if not pd.isna(row['Other']):
        vcf_entry.append(f"TEL;TYPE=OTHER:{row['Other']}")

    vcf_entry.append("END:VCARD\n")
    return "\n".join(vcf_entry)


# Generate VCF data with all columns
vcf_entries = contacts_df.apply(csv_to_vcf, axis=1)

# Save to a new VCF file
vcf_file_path_complete = 'contacts.vcf'
with open(vcf_file_path_complete, 'w') as vcf_file_complete:
    vcf_file_complete.write("\n".join(vcf_entries))
