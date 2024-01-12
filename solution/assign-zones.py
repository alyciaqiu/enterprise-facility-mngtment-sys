def assign_zones(dataframe, x_min, x_max, y_min, y_max, k):
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
