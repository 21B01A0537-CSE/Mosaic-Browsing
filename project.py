import numpy as np
                                      
def mosaic_browse(r1, c1, r2, c2, motif, mosaic):
    count = 0
    result = []
    for i in range(r2 - r1 + 1):
        for j in range(c2 - c1 + 1):      
            sub_grid = np.array([row[j : j + c1] for row in mosaic[i : i + r1]])
            temp = (motif == 0)
            new_motif = np.copy(motif)
            new_motif[temp] = sub_grid[temp]
            count, result = compare(new_motif, sub_grid, i, j, count, result)
    print_output(count, result)    
    
def compare(new_motif, sub_grid, i, j, count, result):
    comparision = new_motif == sub_grid
    if comparision.all() == True:
        count += 1
        result.append([i + 1, j + 1])
    return count, result   
    
def print_output(matches, coord):
    print(matches)
    for k in coord:
        print(str(k[0]) + " " + str(k[1]))
        
def main():    
    r1, c1 = list(map(int, input().split()))
    motif = [] 
    for i in range(r1):
        motif.append(list(map(int, input().split())))
    
    r2, c2 = list(map(int, input().split()))
    mosaic = []
    for i in range(r2):
        mosaic.append(list(map(int, input().split())))
    
    motif = np.array(motif)
    mosaic = np.array(mosaic)

    mosaic_browse(r1, c1, r2, c2, motif, mosaic)

main()