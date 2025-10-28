#### PREDICTING CRIME

## This map modelizes the crimes that took place yesterday. Based on this map we can predict the places under high crime risk for the next seven days. 
crimes_map = [
  ['.', '.', '.', '.', '.', '.', '.', '.'], 
  ['.', '.', 'X', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', '.', '.', '.', 'X', '.'],
  ['.', '.', '.', '.', '.', '.', '.', '.'],
  ['.', 'X', '.', '.', '.', '.', '.', '.'],
  ['.', '.', '.', '.', '.', '.', '.', '.'],
]

## Functions
def in_bounds(crimes_map, x, y):
    return 0 <= x < len(crimes_map) and 0 <= y < len(crimes_map[0])

def high_surveillance(crimes_map, x, y):  
  for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
    nx, ny = x + dx, y + dy
    if in_bounds(crimes_map, nx, ny) and crimes_map[nx][ny] == '.':
      crimes_map[nx][ny] = 'O'

def low_surveillance(crimes_map, x, y): 
  for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
     nx, ny = x + dx, y + dy
     if in_bounds(crimes_map, nx, ny) and crimes_map[nx][ny] == '.':
        crimes_map[nx][ny] = 'E'

def print_map(crimes_map):
    for row in crimes_map:
        print(' '.join(row))
    print()

## Algorithm
print("Initial crime map:")
print("Crimes scene detected. All cells above, right, left -- essentially next to the map are put under high risk of crimes for 7 days.")
print_map(crimes_map)

for x in range (len(crimes_map)):
  for y in range(len(crimes_map[0])):
    if crimes_map[x][y] == "X":
      high_surveillance(crimes_map=crimes_map, x=x, y=y)


print("Predicted high-risk zones:")
print_map(crimes_map)
