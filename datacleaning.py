import pandas as pd

file_name = "job_descriptions.csv"

dataframe = pd.read_csv(file_name)

print("Sample dataset loaded successfully.")   

# --- 1. Keep only useful columns for demo ---
important_columns = ['Job Id', 'Job Title', 'Company', 'location', 'skills','Job Description', 'Responsibilities']

dataframe = dataframe[important_columns]

# --- 2. Drop duplicates & rows missing critical info ---

dataframe = dataframe.drop_duplicates(subset=["Job Id"])

dataframe = dataframe.dropna(subset=["Job Title", "Job Description"])

print("Sample dataset cleaned successfully.")   

# --- 3. Create search_text column for semantic search ---

def Join_Columns_into_One(row):
       
    job_info = [
        row.get("Job Title", ""),
        row.get("Job Description", ""),
        row.get("skills", ""),
        row.get("Responsibilities", "")
    ]

    # Create an empty list to store valid information
    valid_info = []
    
     # Loop through each piece of job information
    for info in job_info:
        # Check if the information is not empty/null
        if pd.notnull(info):
            # Convert the information to string and add it to valid_info
            valid_info.append(str(info))
    
    # Join all valid information with spaces between them
    combined_text = " ".join(valid_info)
    return combined_text

print("Selected columns merged successfully.")   

dataframe["search_text"] = dataframe.apply(Join_Columns_into_One, axis=1)

# --- 4. Sample smaller dataset for demo ---
final_dataframe = dataframe.sample(n=300, random_state=42)

final_dataframe.to_csv("300_job_descriptions_final.csv", index=False)

print("Sample dataset created successfully.")   

print(f"Original size: {len(dataframe)} rows")
print(f"Sampled size: {len(final_dataframe)} rows")

print("Saved to job_descriptions_demo.csv - Done")