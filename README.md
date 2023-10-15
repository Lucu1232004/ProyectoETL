# ProyectoETL
Proyecto Base de datos

# Traffic Accident Data Processing
This Python script is used to process a CSV file containing traffic accident data. Performs various cleaning and transformation operations on the data to prepare it for further analysis.

## Use

Make sure you have Python installed on your system before running this script. To run the code, follow these steps:

1. Download the CSV file containing the traffic accident data and save it to the same location as this script. Make sure the file name is "/Traffic_Crashes.csv".

2. Open a terminal or command line and navigate to the location of the script and CSV file.

3. Run the script using the following command:

4. The script will perform the following operations:

- Will remove the columns specified in the `columns_to_drop` list from the DataFrame.
- Will remove rows containing null values.
- Will convert the columns specified in the `integer_columns` list to integer values.
- Will trim any additional information after the "/" in the "CRASH_TYPE" column.
- It will map the numbers of the day of the week to their corresponding names.
- Will map month numbers to their corresponding names.
- Will reformat the "LOCATION" column so that it is in a more readable format.

5. The processed DataFrame will be saved in a new CSV file named "Traffic_converted.csv".

## Requirements

The script requires the `pandas` library, which is usually installed using pip. Make sure pandas is installed before running the script.

pip install pandas

## Grades

- Make sure the input CSV file has the correct name and location (default "/Traffic_Crashes.csv").
- The script will overwrite the output file "Traffic_converted.csv" if it already exists in the current location.

Feel free to modify the script based on your specific needs or data requirements.
