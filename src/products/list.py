from src.products.router import router


@router.get('')
def get_products():

    return [{'id': 1}]
