from . import room

list_of_rooms = []

def update_list(json_payload):
    payload = json_payload    
    raw_rooms = payload['rooms']
    global list_of_rooms
    list_of_rooms = []    
    for r in raw_rooms:            
        new_room = room.Room(r['name'], r['address'], r['capacity'], r['location'], r['office'])
        list_of_rooms.append(new_room)

def get_rooms(office):
    """
    Gets a office name and returns a list of 
    rooms from given office
    """
    office_to_check = office    
    response_list = []        
    for item in list_of_rooms:
        if item.office == office_to_check:
            response_list.append(item)    
    return response_list
    