#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)
    """
    YOUR CODE HERE
    """
    # Insert locations on hash table
    # Insert locations on hash table
    
    for ticket in tickets: # for all the the ticket in the array of given tickets
        hash_table_insert(hashtable, ticket.source, ticket.destination) # insert into hash tables
    current = hash_table_retrieve(hashtable, "NONE") # get the first item for the route where key is NONE
    route[0] = current  # insert it into the first position on the route

    for i in range(0, length - 1):
        route[i] = current
        current = hash_table_retrieve(hashtable, current) # retrieve the value using the preceding ticket from the hastable
    return route