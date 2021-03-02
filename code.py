import itertools
import math


#returns true if intersection is open from a given street at a given time
# street['name']
# def is_intersection_open_from_street(street, inter, time):
#     inter = inter['streets']
#     period_time = 0
#     streets_arr = []
#     for i in inter:
#         streets_arr.append(i[0])
    
#     idx = streets_arr.index(street['name'])
#     starts_at_time = 0
#     for i in range(idx):
#         starts_at_time += inter[i][1]
#     ends_at_time = starts_at_time + inter[idx][1]
#     for i in inter:
#         period_time += i[1]
#     modulo_time = time % period_time
#     if modulo_time<ends_at_time and modulo_time >= starts_at_time:
#         return True
#     return False

def maping(value, rang):
    new = value*(rang-1)+1
    if value == 0:
        return 0
    return new

def do_stuff(inlines):
    """ Main function.
    Should return list of lines to be printed
    Or a list of lists of elements to be printed in each line
    """
    D, I, S, V, F = list(map(lambda x: int(x), inlines[0].split(' ')))
    
    streets = []
    streets_by_name = {}
    for i in range(1,S+1):
        start, end, name, time = inlines[i].split(' ')
        street = {
            'start': int(start),
            'end': int(end),
            'name': name,
            'time': int(time)
        }
        streets.append(street)
        streets_by_name[name] = street

    
    intersections = []
    for i in range(I):
        intersections.append({
            'id': i,
            'ingoing': []
        })
    
    for street in streets:
        intersections[street['end']]['ingoing'].append(street['name'])
    
    
    routes = []
    for i in range(S+1,S+V+1):
        car_array = inlines[i].split(' ')
        length = car_array[0]
        names = car_array[1:]
        route = {
            'length': int(length),
            'streets': list(map(lambda name: streets_by_name[name], names))
        }
        routes.append(route)
    # print(routes)

    max_route_len = 0
    sum_route_length = 0
    min_route_len = 999999
    for route in routes:
        sum_route_length += route['length']
        if max_route_len<route['length']:
            max_route_len = route['length']
        if min_route_len>route['length']:
            min_route_len = route['length']
    avg_route_len = sum_route_length/len(routes)

    ocupation = {}
    for street in streets:
        ocupation[street['name']] = 0
    for route in routes:
        streets = route['streets']
        for street in streets:
            ocupation[street['name']] = ocupation[street['name']] + 1
    
    # print(ocupation)
    
    inter = []
    for intersection in intersections:
        # print(intersections)
        ocupation_sum = 0
        intersec = {
            'id': intersection['id'],
            'streets': [] 
        }
        #TODO: period_duration
        period_duration = D/(max_route_len)
        if period_duration<len(intersection['ingoing']):
            period_duration = len(intersection['ingoing'])

        # period_duration = 2
        # max_ocupation = 0
        # for street in intersection['ingoing']:
        #     if max_ocupation < ocupation[street]:
        #         max_occupied_street = street
        #         max_ocupation = ocupation[street]
        # print(period_duration)
        for street in intersection['ingoing']:
            ocupation_sum += ocupation[street]
        for street in intersection['ingoing']: 
            # print(street)
            if ocupation_sum != 0:
                duration_for_street = ocupation[street]/ocupation_sum
                duration_for_street = math.floor(maping(duration_for_street,period_duration))
                if duration_for_street != 0:
                    intersec['streets'].append([street,int(duration_for_street)])
                # if ocupation[street] == max_ocupation:
                #     intersec['streets'].append([street,1])
        if len(intersec['streets']) != 0:
            inter.append(intersec)


    return inter

    # inter_by_id = {}
    # for intersect in inter:
    #     inter_by_id[intersect['id']] = intersect

    # routes_with_states = []
    # for i, route in enumerate(routes):
    #     routes_with_states.append({
    #         'id': i,
    #         'done': False,
    #         'progress': 0,
    #         'at_street': route['streets'][0],
    #         'streets': route['streets'],
    #         'at_street_index': 0
    #     })
    

    # #CALCULATING if street is open at given time

    # # sim

    # queue_for_streetname = {}
    # for street in streets:
    #     queue_for_streetname[street['name']] = []

    # for time in range(1, D):
    #     for route_with_state in routes_with_states:
    #         # calculate new state
    #         at_street = route_with_state['at_street']
    #         is_at_intersection = route_with_state['progress'] > route_with_state['at_street']['time']
    #         next_intersection = inter_by_id[route_with_state['at_street']['end']]
    #         is_next_intersection_open = is_intersection_open_from_street(at_street, next_intersection, time)

    #         # print("current street")
    #         # print(at_street['name'])
    #         # print("next intersection")
    #         # print(next_intersection['id'])
    #         # print("is_at_iuntersection?")
    #         # print(is_at_intersection)
    #         # print("is_intersection_open")
    #         # print(is_next_intersection_open)

    #         if not is_at_intersection:
    #             route_with_state['progress'] = route_with_state['progress'] + 1
    #         else:
    #             street_queue = queue_for_streetname[at_street['name']]
    #             street_has_no_queue = len(street_queue)==0
    #             if not street_has_no_queue:
    #                 print(street_queue)
    #                 is_first_in_queue = street_queue[-1]['i'] == route_with_state['i']
    #             else:
    #                 is_first_in_queue = False

    #             is_in_street_queue = any(route_with_state2['i'] == route_with_state['i'] for route_with_state2 in street_queue)
                


    #             if not is_in_street_queue:
    #                 queue_for_streetname[at_street['name']].append(route_with_state)


    #             if is_next_intersection_open and is_first_in_queue:
    #                 queue_for_streetname[at_street['name']].pop()

    #                 route_with_state['progress'] = 0
    #                 route_with_state['at_street_index'] = route_with_state['at_street_index'] +1
    #                 try:
    #                     route_with_state['at_street'] = route_with_state['streets'][route_with_state['at_street_index']]
    #                 except IndexError:
    #                     route_with_state['done'] = True
            


            

    #     #
    # print(routes_with_states)


    # return inter
    

    # print(streets)
    # print(routes)
    #[{'id': 0, 'streets': [['rue-de-londres', 10.0]]}, {'id': 1, 'streets': [['rue-d-amsterdam', 5.0], ['rue-d-athenes', 5.0]]}, {'id': 2, 'streets': [['rue-de-moscou', 10.0]]}, {'id': 3, 'streets': [['rue-de-rome', 10.0]]}]

    # [intersection, amount of incomming streets to coordinate, (streetname, time), (streetname, time), ... , (streetname, time)]
    #testoutput = list(map(lambda intersection: [intersection['id'] ,len(intersection['ingoing']), list(map(lambda streetname: streetname+' 1',intersection['ingoing']))], intersections))
    #print()
    #print(testoutput)
    # [[values],[values],----]
    # return inlines