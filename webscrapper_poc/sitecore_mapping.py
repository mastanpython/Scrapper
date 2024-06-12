import json
import pandas as pd

# Load the JSON configuration file
with open('configfinal.json', 'r') as f:
    config = json.load(f)

# Read the existing Excel file
excel_path = 'updated_sheet.xlsx'
sheets = pd.read_excel(excel_path, sheet_name=None)  # Read all sheets

# Ensure the sheets have the required columns and update mappings
for sheet_name, df in sheets.items():
    if 'ComponentName' not in df.columns or 'FieldName' not in df.columns:
        raise ValueError(f"The sheet '{sheet_name}' must contain 'ComponentName' and 'FieldName' columns.")
    
    # Create a function to get the mapped field
    def get_mapped_field(component, field):
        # Check sitecore_mappings first
        mapped_field = config.get('sitecore_mappings', {}).get(component, {}).get(field, "")
        if not mapped_field:
            # Check field_mappings if no mapping found in sitecore_mappings
            mapped_field = config.get('field_mappings', {}).get(field, "")
        return mapped_field

    # Apply the function to create the MappedField column
    df['MappedField'] = df.apply(lambda row: get_mapped_field(row['ComponentName'], row['FieldName']), axis=1)
    
    # Reorder columns to place MappedField after FieldName
    cols = df.columns.tolist()
    field_name_index = cols.index('FieldName')
    cols.insert(field_name_index , cols.pop(cols.index('MappedField')))
    df = df[cols]
    
    # Update the sheet in the sheets dictionary
    sheets[sheet_name] = df

# Save the updated DataFrames back to a new Excel file with multiple sheets
output_excel_path = 'updated_sheet1.xlsx'
with pd.ExcelWriter(output_excel_path) as writer:
    for sheet_name, df in sheets.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Mapping completed and the updated Excel file has been saved.")
