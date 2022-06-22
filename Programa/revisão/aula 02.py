from tank import Tank

tanks = {
    'a': Tank('Carla'),
    'b': Tank('CG'),
    'c': Tank('Matheus')
}

alive_tanks = len(tanks)

while alive_tanks > 1:
    for tank_name in sorted(tanks.keys()):
        print(tank_name, tanks[tank_name])
    
    first  = input('Who fires?').lower()
    second = input('Who at?').lower()

    try:
        first_tank  = tanks[first]
        second_tank = tanks[second]
    except KeyError as name:
        print('No such tank!', name)
        continue

    if not first_tank.alive or not second_tank.alive:
        print('One of those tanks is dead!')
        continue

    print('*'*30)

    first_tank.fire(second_tank)
    if not second_tank.alive:
        alive_tanks -= 1

    print('*'*30)