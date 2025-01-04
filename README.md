# csv -> vcf(Virtual Contact File)

Convert your contact information stored in csv to vCard aka vcf(Virtual Contact File). This conversion enables users to easily import their contacts into platforms like iCloud, Google Contacts, or mobile devices.

## Usage
1. Create a virtualenv
    ```bash
    python3 -m venv env
    ```
2. Activate the virtualenv
    ```bash
    source env/bin/activate
    ```
3. Install `pandas`
    ```bash
    pip install pandas
    ```
4. Create `contacts.csv` in the following format:
    ```
    Full Name,Primary Phone,Work Phone,Home Phone,Other
    Lee Hernandez,887.760.3231x076,301.511.5265x01002,911-797-3466x60569,604-769-3287
    Gerald Robinson,(279)448-6547,001-653-398-3522,001-732-477-5636x789,693-241-9632
    ```
5. Run the `csv_to_vcf.py`
    ```
    python3 csv_to_vcf.py
    ```