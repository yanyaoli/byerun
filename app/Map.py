def getMapData(map_choice):

    from app.maps.cuit.hkg import hkg
    from app.maps.cuit.lqy import lqy
    from app.maps.cdutcm.wj import wj

    choice = map_choice

    if choice == "cuit_lqy":
        mapdata = lqy()
        return mapdata
    elif choice == "cuit_hkg":
        mapdata = hkg()
        return mapdata
    elif choice == "cdutcm_wj":
        mapdata = wj()
        return mapdata