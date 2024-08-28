import pandas as pd
import plotly.express as px

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
#print(incident_agency_count)


month_incident_merge = pd.merge(df_incident, df_months)
month_incident_count = month_incident_merge['month_num'].value_counts()
sorted_month_incident_count = month_incident_count.sort_index()
print(sorted_month_incident_count)
print("--Monthly Crime Stats--")
print(f"Average: {sorted_month_incident_count.mean()}")
print(f"Standard Deviation: {sorted_month_incident_count.std()}")