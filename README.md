# Enterprise Facility Management System

## Overview
By utilizing geospatial data generated from digital devices (identified via MAC addresses), the team designed a simulated enterprise facility management system that provides an all-in-one enterprise facility solution to help company combat two major challenges that could have a detrimental impact on a company's profitability - security and workflow management. Our solution combines security and maintenance management, offering a cost-effective and efficient way for companies to enhance their facility management processes and increase profitability.  

## Data Exploration (希竹补充这个部分)

## Solution

### Divide the building into a $k \times k$ grid
To access the location of a device in a systematic way, we defined a helper function that allows us to divide the building into a $k \times k$ grid and assigned a Zone ID to each zone defined.  

Here is a visualization of what the code will produce:  

![image](https://github.com/alyciaqiu/enterprise-facility-mngtment-sys/assets/129646186/3df5db38-4fe9-459b-8e22-ffc4ddb96def)  

To learn more, nagivigate to `solution` directory and check `grid.py`.

### Solution Demo 1: Safe Sphere
_Safe Sphere_, our security management system, detects and alerts any unauthorized access in real-time. When an unauthorized device enters a pre-defined security area, an email alert is sent to the nearest security guard, including a photo taken at the time of the incident.  

To learn more, navigate to `solution` directory and check `safe_sphere.ipynb`.

### Solution Demo 2: Smart Maintenance
_Smart Maintenance_, helps companies manage equipment issues more efficiently. Smart Maintenance automatically detects equipment anomalies and finds the appropriate personnel to solve the problem. Additionally, when multiple machines have issues, Smart Maintenance prioritizes and sends work orders accordingly.  

To learn more, navigate to `solution` directory and check `smart_maintenance.ipynb`.
