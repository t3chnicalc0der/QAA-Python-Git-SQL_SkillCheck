# The controller contains functions that takes in data (such as Order Strings or ids) 
# and run the functions in the Service Object that interact with the DB
# The controller will typically convert String data into Order Objects that can be used with the Service functions

# The controller sends and collects data from the Service file, and pushes this data to the Runner which can display said data

# Not complete, but a suggestion of the process
def read_by_id(id):
    order = service.read_by_id(id)
    return order
