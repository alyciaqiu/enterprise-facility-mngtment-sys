# Enterprise Facility Management System

## Overview
By utilizing geospatial data generated from digital devices (identified via MAC addresses), the team designed a simulated enterprise facility management system that provides an all-in-one enterprise facility solution to help company combat two major challenges that could have a detrimental impact on a company's profitability - security and workflow management. Our solution combines security and maintenance management, offering a cost-effective and efficient way for companies to enhance their facility management processes and increase profitability.  

## Data Cleaning
1. Clean missing values and 00:00:00:00 all zero Mac Address
2. Delete observations outside the building
3. Intercept time to the exact second and keep one row per second
4. Remove mac address appears only once

Here are visualizations of how we do data cleaning:  

![Final Presentation Finders-3](https://github.com/alyciaqiu/enterprise-facility-mngtment-sys/assets/136132782/b300b111-85cb-4ef6-9173-61ca6f70a935)

To learn more, navigate to `data cleaning` directory and check `data_cleaning.ipynb`.

## Data Preparation

In order to build the Enterprise Facility Management System, we need to distinguish fixed and mobile devices in data records. First, we use the information of MacAddr to find the manufactory of all devices, and do the manual labeling to "Fixed", "Mobile" and "TBD" (To Be Decided) Three Types. Next, we use moving distance, moving speed and number of days appear and find thresholds for "TBD" Type to distinguish fixed and mobile devices. Then, for all data records with "Mobile" devices, we need to find thresholds to distinguish visitors, security guards and daytime workers. Last, we need to check all data records with "Fixed" devices, and delete some records that only appear one day in the whole dataset.

### Manual Labeling for All Manufactories to "Fixed", "Mobile" and "TBD" (To Be Decided) Three Types

With mac_vendor_lookup package, we can find the manufactory information for each MacAddr, then we search the product categories of these manufactories and manually label the Device type for each manufactory. For example, "Motorola Mobility LLC" is labeled as "Mobile" type, and "ALPSALPINE Co,.LTD" is labeled as "Fixed" type. For some manufactories, they have products both in the mobile category and fixed category, in that case, we labeled these as "TBD", which is to be decided and need other methods to distinguish in the next step.

To learn more, navigate to `data preparation/vendor` directory and check `find_vendor.py`.

### Distinguish Fixed Devices and Mobile Devices by Distance, Speed and Number of Days in "TBD" Type Devices

For each of these 1923 TBD devices, we calculate the distance and speed between every pair of points located at the same level and on the same date, and summarize the statistical indicators. We choose to use distance std, distance mean and speed median to set criteria. We draw the cumulative distribution chart to find the most reasonable threshold. 

A Fixed Device should:
- Appears more than 1 day in total
- Distance Standard deviation <= 2 
- Distance Mean <= 0.4
- Speed Median <= 0.05

Here are visualizations of how we set the threshold:  

![Final Presentation Finders-1](https://github.com/alyciaqiu/enterprise-facility-mngtment-sys/assets/136132782/8d2c15fb-6ac5-4638-afe6-34256cabb57c)

To learn more, navigate to `data preparation` directory and check `Distinguish_Fixed_Mobile.ipynb`.

### Distinguish Visitors, Security Guards and Daytime Workers on Mobile Devices 

- Visitors should: Appears less than 10 days in total
- Security Guards should: Appears at night (22:00-7:00) or on weekends
- Daytime Workers: Other mobile devices belong to Daytime Workers

Here are visualizations of how we set the threshold:

![Final Presentation Finders-2](https://github.com/alyciaqiu/enterprise-facility-mngtment-sys/assets/136132782/e3ea26e7-41fd-4d5a-b148-eb9b774276b8)

To learn more, navigate to `data preparation` directory and check `Distinguish_Employee_visitor_security_guard.ipynb`.

### Check Fixed Mobile 

Check all data records with the "Fixed" type. Explore and summarize the statistical data. Delete the data records with the "Fixed" type which only appears one day in the whole dataset.

To learn more, navigate to `data preparation` directory and check `Fixed Mobile Check.ipynb`.

## Solution

### Divide the building into a $k \times k$ grid
To access the location of a device in a systematic way, we defined a helper function that allows us to divide the building into a $k \times k$ grid and assigned a Zone ID to each zone defined.  

Here is a visualization of what the code will produce:  

![image](https://github.com/alyciaqiu/enterprise-facility-mngtment-sys/assets/129646186/3df5db38-4fe9-459b-8e22-ffc4ddb96def)  

To learn more, navigate to `solution` directory and check `grid.py`.

### Solution Demo 1: Safe Sphere
_Safe Sphere_, our security management system, detects and alerts any unauthorized access in real-time. When an unauthorized device enters a pre-defined security area, an email alert is sent to the nearest security guard, including a photo taken at the time of the incident.  

To learn more, navigate to `solution` directory and check `safe_sphere.ipynb`.

### Solution Demo 2: Smart Maintenance
_Smart Maintenance_, helps companies manage equipment issues more efficiently. Smart Maintenance automatically detects equipment anomalies and finds the appropriate personnel to solve the problem. Additionally, when multiple machines have issues, Smart Maintenance prioritizes and sends work orders accordingly.  

To learn more, navigate to `solution` directory and check `smart_maintenance.ipynb`.

### Send Alert Email
For example, alerting the Nearest Security Guard involves using the guard's mac id to identify them in our Employee Identity database. A Python function extracts key information to generate an alert email. Surveillance camera screenshots from secure areas are attached to provide visual context.

Here is a visualization of alerting the Nearest Security Guard:  

![Final Presentation Finders-4](https://github.com/alyciaqiu/enterprise-facility-mngtment-sys/assets/136132782/80e63c37-f7b1-4bc5-93e6-8bd3e64514f2)

To learn more, navigate to `solution/Send Alert Email` directory and check `Email to Security guard.ipynb` and `Email to Maintenance staff.ipynb`
