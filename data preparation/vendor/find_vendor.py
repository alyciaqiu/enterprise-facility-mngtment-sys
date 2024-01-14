import pandas as pd
from mac_vendor_lookup import MacLookup
import nest_asyncio

nest_asyncio.apply() # to solve runtime error: This event loop is already running

def find_vendor(df, output_path):
  """
    Divide a building into a k x k grid, and assign each zone a ZoneID.
    
    Args:
        df (pandas.DataFrame): The input data frame with columns 
            ClientMacAddr, localtime, Site, Level, lat, and lng.
        output_path (str): The path to output the vendor.csv
  """
  # Extract unique MAC addresses from df
  unique_macs = df['ClientMacAddr'].unique()
  # Create a list to store the manufacturer names or 'unknown'
  oui = []
  for mac in unique_macs:
      try:
          manufacturer = MacLookup().lookup(mac)
      except Exception:
          manufacturer = 'unknown'
      oui.append(manufacturer)
  # Combine the unique_macs and oui lists into a DataFrame
  vendor = pd.DataFrame(list(zip(unique_macs, oui)), 
                        columns=['ClientMacAddr', 'Manufacturer'])
  vendor.to_csv(output_path,index=False)
  print(f'Finished finding vendors. The output has been saved to {output_path}')


# run find_vendor to get full vendor list
output_path = './vendor.csv'
find_vendor(df, output_path) # Due to data privacy, we can't provide the df here
