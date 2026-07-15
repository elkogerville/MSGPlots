

def amuse_quantity_2_astropy(quantity, unit):
    astropy_quantity = quantity.as_astropy_quantity()
    try:
        return astropy_quantity.to(str(unit))
    except:
        unit = input('enter astropy unit: ')
        return astropy_quantity.to(unit)
