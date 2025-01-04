import faker
import pandas as pd

# Initialize Faker
fake = faker.Faker()

# Generate fake contact information
fake_contacts = []
for _ in range(50):
    fake_contacts.append({
        "Full Name": fake.first_name() + ' ' + fake.last_name(),
        "Primary Phone": fake.phone_number(),
        "Work Phone": fake.phone_number(),
        "Home Phone": fake.phone_number(),
        "Other": fake.phone_number(),
    })

# Create a DataFrame
fake_contacts_df = pd.DataFrame(fake_contacts)

# Save to CSV
fake_contacts_csv_path = 'contacts.csv'
fake_contacts_df.to_csv(fake_contacts_csv_path, index=False)
