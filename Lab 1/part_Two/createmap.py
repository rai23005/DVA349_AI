
def createmap(edgelist):
    

    mapdirection={}

    for edge in edgelist:
        nodeA=edge["from"]
        nodeB=edge["to"]
        distance=edge["distance"]

        if nodeA not in mapdirection:
            mapdirection[nodeA]={}
        mapdirection[nodeA][nodeB]=distance
        
        if nodeB not in mapdirection:
            mapdirection[nodeB]={}
        mapdirection[nodeB][nodeA]=distance



    return mapdirection