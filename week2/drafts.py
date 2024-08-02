
def min(thing, bagWeight):
    thingPartials = (thing['value'] / thing['weight'])
    partials = thing['weight']
    count = 1

    if partials > bagWeight:
        return 0
    
    while partials <= bagWeight and partials + thing['weight'] <= bagWeight and count <= thingPartials:
        partials += thing['weight']
        count += 1
    
    return partials