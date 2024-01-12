def assign_zones(dataframe, x_min, x_max, y_min, y_max, k):
    """
    Divide a building into a k x k grid, and assign each zone a ZoneID.
    
    Args:
        dataframe (pandas.DataFrame): The input data frame with columns 
            ClientMacAddr, localtime, Site, Level, lat, and lng.
        x_min (float): The west most longtitudes coordinate.
        x_max (float): The east most longtitudes coordinate.
        y_min (float): The north most latitude coordinate.
        y_max (float): The west most latitude coordinates.
        k (int): Number of grid in a row/column.
    
    Returns:
        dataframe (pandas.DataFrame): A data frame with columns 
            ClientMacAddr, localtime, Site, Level, lat, lng, and ZoneID.
    """
    # Define the x and y boundaries of the grid
    x_step = (x_max-x_min)/k
    y_step = (y_max-y_min)/k

    # assign zone number for the given dataframe
    zone_num = 1
    for i in range(k):
        for j in range(k):
            x = x_min + i * x_step
            y = y_min + j * y_step
            mask = ((dataframe['lng'] >= x) & (dataframe['lng'] <= x + x_step) &
                    (dataframe['lat'] >= y) & (dataframe['lat'] <= y + y_step))
            dataframe.loc[mask, 'ZoneID'] = zone_num
            zone_num += 1
    dataframe['ZoneID'] = dataframe['ZoneID'].astype(int)
    return dataframe
