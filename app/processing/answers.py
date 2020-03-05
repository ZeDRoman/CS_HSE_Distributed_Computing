def idDoesntExists(product_id):
    return F"Object with id = {product_id} doesnt exist"


def idNotNumber():
    return "Id must be number"


def pageNotNumber():
    return "Page must be number"


def pageCountNotNumber():
    return "Page count must be number"


def idExists():
    return "Product with that id already exists"


def productCreated():
    return "Product is created"


def productEdited():
    return "Product is edited"


def productDeleted():
    return "Product is deleted"
