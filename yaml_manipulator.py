import re
from datetime import datetime, timedelta

def replace_expiry_dates(filename, days_to_add=30):
  """
  Finds and replaces expiry dates in a text file with fresh dates.

  Args:
    filename: The name of the text file.
    days_to_add: The number of days to add to the current date 
                 to create the new expiry date. Defaults to 365.
  """

  with open(filename, 'r') as f:
    file_content = f.read()

  # Define a regular expression pattern to match expiry dates
  # This pattern assumes dates are in the format YYYY-MM-DD
  # You might need to adjust this based on the actual format in your file
  pattern = r"(\d{4}-\d{2}-\d{2})"

  def replace_date(match):
    expiry_date_str = match.group(1)
    expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d")
    new_expiry_date = datetime.today() + timedelta(days=days_to_add)
    return new_expiry_date.strftime("%Y-%m-%d")

  # Find and replace all expiry dates
  new_file_content = re.sub(pattern, replace_date, file_content)

  with open(filename, 'w') as f:
    f.write(new_file_content)

# Example usage:
filename = 'whitelist.yaml'
replace_expiry_dates(filename) 

