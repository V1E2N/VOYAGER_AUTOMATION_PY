import pandas as pd



array_var =[1,2,3]
print(array_var[2])

getarray = int(input("Enter the data to stored in array "))
array_var.append(getarray)
print(array_var)
array_var.remove(array_var[3])
print(array_var)
#array_var.clear()
#print(array_var)
# Load the Excel file
file_path = 'D://filestream//fs.xlsx'
# Read the Excel sheet into a pandas DataFrame
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Convert the DataFrame to a list (array)
array_var= df.values.tolist()

# Print the array
print(array_var)
