import pandas as pd
import argparse
import sys

def combine_results(input_file, output_file):
    # Load the entire workbook
    xls = pd.ExcelFile(input_file)
    
    # Create a list to store the combined data
    combined_data = []
    
    # Iterate through each sheet in the workbook
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        
        # Get all column names
        all_columns = list(df.columns)
        
        # Initialize variables for combining content
        current_component = None
        combined_content_dict = {}
        current_row_data = {}

        # Iterate through each row in the dataframe
        for idx, row in df.iterrows():
            component = row['ComponentName']
            field_name = row['MappedField']
            content = row['Content']
            
            # Convert content to string to avoid TypeError
            if pd.notna(content):
                content = str(content)
            else:
                content = ''
            
            # If a new component is encountered
            if pd.notna(component):
                if current_component is not None:
                    # Append the combined result for the previous component
                    for field, combined_content in combined_content_dict.items():
                        combined_data.append([current_row_data[col] for col in all_columns] + [current_component, field, combined_content.strip()])
                # Reset variables for the new component
                current_component = component
                combined_content_dict = {field_name: content}
                current_row_data = {col: row[col] for col in all_columns}
            else:
                # Continue combining content for the current component and field name
                if field_name in combined_content_dict:
                    combined_content_dict[field_name] += ' ' + content
                else:
                    combined_content_dict[field_name] = content
        
        # Append the last combined result
        if current_component is not None:
            for field, combined_content in combined_content_dict.items():
                combined_data.append([current_row_data[col] for col in all_columns] + [current_component, field, combined_content.strip()])
    
    # Create a dataframe from the combined data
    result_df = pd.DataFrame(combined_data, columns=all_columns + ['ComponentName1', 'MappedField1', 'Content1'])
    columns_to_drop = ['ComponentName', 'MappedField', 'Content','FieldName']
    result_df = result_df.drop(columns_to_drop, axis=1)
    
    new_names = {'ComponentName1': 'ComponentName', 'MappedField1': 'MappedField','Content1':'Content'}
    df = result_df.rename(columns=new_names)

    # Drop columns from result_df
    
    #print(df.info())
    # Save the combined results to a new Excel file
    df.to_excel(output_file, index=False)

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Combine data from multiple Excel sheets based on ComponentName.")
    parser.add_argument("input_file", help="Path to the input Excel file.")
    parser.add_argument("output_file", help="Path to the output Excel file.")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Run the combine function with user-specified files
    combine_results(args.input_file, args.output_file)
    print("Results combined successfully!")

if __name__ == "__main__":
    # Check if the script is being run in an interactive environment
    if hasattr(sys, 'ps1') or (hasattr(sys, 'argv') and len(sys.argv) > 1 and 'ipykernel_launcher' in sys.argv[0]):
        print("Interactive environment detected. Running with default arguments.")
        # You can specify default arguments for testing in an interactive environment
        combine_results('sample.xlsx', 'combined_results.xlsx')
    else:
        main()
