def loadfile(file_path):

    berlin52 = []
    reading_location = False

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            #börja läsa in raderna
            if line.startswith('NODE_COORD_SECTION'):
                reading_location = True
                continue

                #Färdig läst
            elif line == 'EOF':
                break   

            elif reading_location and line:
                parts = line.split()
                if len(parts) >= 3:
                    location_id = int(parts[0])
                    x = float(parts[1])
                    y = float(parts[2])
                    berlin52.append({'Location ID': location_id, 'x': x, 'y': y})
    
    return berlin52