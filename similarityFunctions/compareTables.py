def compareTables(columns1 , columns2):

    if len(columns1) == 0 and len(columns2) == 0:
        return 0.5
    
    if len(columns1) == 0 or len(columns2) == 0:
        return 0.0
    
    
    intersection = columns1.intersection(columns2)
    union = columns1.union(columns2)

    similarity = len(intersection) / len(union)

    return similarity