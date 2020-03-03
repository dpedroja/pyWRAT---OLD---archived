# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:48:44 2020

@author: dpedroja
"""
import pandas
import numpy
flow_table_df = pandas.read_csv('input_data/toy_basins_flow.csv')
basins = flow_table_df["BASIN"].tolist()
flows_to = flow_table_df["FLOWS_TO"].tolist()

# hucs_DF = pandas.read_csv("Modified_SFE_hucs.csv")
# basins = hucs_DF["HUC12"].tolist()
# flows_to = hucs_DF["TOHUC"].tolist()

# DICTIONARIES
flows_to_dictionary = {basins[k] : flows_to[k] for k, basin in enumerate(basins)}
index_dictionary = {basins[k] : [k] for k, basin in enumerate(basins)}

# Initialize empty basin x basin identity matrix
connectivity_matrix = numpy.identity(numpy.size(basins), dtype = int)
    
# outlet = 180101051001
outlet = "H"

for k, basin in enumerate(basins):
    while basin != outlet:
        connectivity_matrix[k][index_dictionary[flows_to_dictionary[basin]]] = 1
        basin = flows_to_dictionary[basin]
    print(connectivity_matrix)

# cm_df = pandas.DataFrame(connectivity_matrix)
# cm_df.index = basins
# cm_df.to_csv(".csv")

##########################################################################################################################

# Basin User table (1 for basin location of each user)
import pandas
import numpy

flow_table_df = pandas.read_csv('input_data/toy_basins_flow.csv')
basins = flow_table_df["BASIN"].tolist()
rip_user_df = pandas.read_csv('input_data/RiparianStatements.csv')
rip_user = rip_user_df["USER"].tolist()
user_location = rip_user_df["LOCATION"].tolist()
    
basin_use = {rip_user[i] : user_location[i] for i, user in enumerate(rip_user)}  
index_dictionary = {basins[k] : [k] for k, basin in enumerate(basins)}

user_matrix = numpy.zeros([numpy.size(rip_user), numpy.size(basins)])

for i, user in enumerate(rip_user):
    user_matrix[i][index_dictionary[basin_use[user]]] = 1
user_matrix = user_matrix.transpose()     

##########################################################################################################################

# User connectivity matrix (1 if user is upstream of basin)
user_connectivity = numpy.matmul(connectivity_matrix.transpose(), user_matrix)
