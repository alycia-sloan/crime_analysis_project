import pandas as pd


#incorporate data
df_arrestee = pd.read_csv("data\\NIBRS_ARRESTEE.csv")
df_offense_type = pd.read_csv("data\\NIBRS_OFFENSE_TYPE.csv")
df_incident = pd.read_csv('data\\NIBRS_incident.csv')
df_agencies = pd.read_csv('data\\agencies.csv')
df_months = pd.read_csv('data\\NIBRS_month.csv')

merge_arrestee_offtyp = pd.merge(df_arrestee, df_offense_type)

#create print incident type count by category
incident_count = merge_arrestee_offtyp['offense_category_name'].value_counts()


#NIBRS_incident -> incidents that include agency id
#Count of incidents by county_name
incident_agency_merge = pd.merge(df_incident,df_agencies)
incident_agency_count = incident_agency_merge['county_name'].value_counts()

month_incident_merge = pd.merge(df_incident, df_months)
month_incident_count = month_incident_merge['month_num'].value_counts()
sorted_month_incident_count = month_incident_count.sort_index()
sorted_by_incident_rate = month_incident_count.sort_values()

#Monthly Stats Print to screen
print("--Monthly Crime Stats for Virginina in 2021--")
print(f"Average # of Incidents Per Month: {sorted_month_incident_count.mean()}")
print(f"Standard Deviation of Incidents Per Month: {sorted_month_incident_count.std()}")
print(f"Month with least incidents: {sorted_by_incident_rate.idxmin()}")
print(f"Month with the most incidents: {sorted_by_incident_rate.idxmax()}")
print("\n")

#Incidents by County Info
merge_incident_county = pd.merge(df_incident, df_agencies)
#print(merge_incident_county.head(30))
county_incident_count = merge_incident_county['county_name'].value_counts()
print(f"Top 10 Counties with most incidents: ")
print(county_incident_count.head(10))