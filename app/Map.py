def getMapData(map_choice):
    from app.maps.hkg import hkg
    from app.maps.lqy import lqy
    choice = map_choice
    if choice == "龙泉驿":
        mapdata = lqy()
        return mapdata
    elif choice == "航空港":
        mapdata = hkg()
        return mapdata