from app import app, render_template, request
from sqlalchemy import create_engine, text
from routes.admin import category

engine = create_engine("mysql+mysqlconnector://root:mysql@127.0.0.1/st89_pos")
# Test the connection
connection = engine.connect()


@app.get('/admin/product')
def product():
    module = 'product'
    return render_template('admin/product.html', module=module)


@app.get('/admin/get-product')
def getProduct():
    product_list = getProductList()
    category_list = category.getCategoryList()
    return {
        'product_list': product_list,
        'category_list': category_list,
    }


@app.post('/admin/create-product')
def createProduct():
    form_date = request.get_json()
    name = form_date['name']
    cost = form_date['cost']
    price = form_date['price']
    category_id = form_date['category_id']
    description = form_date['description']


    result = connection.execute(text(f"INSERT INTO `product` VALUES (NULL,'{name}','{cost}','{price}','{category_id}','{description}')"))
    connection.commit()
    return [name, description]


@app.post('/admin/delete-product')
def deleteProduct():
    form_date = request.get_json()
    product_id = form_date['product_id']

    result = connection.execute(text(f"DELETE FROM `product` WHERE id = '{product_id}'"))
    connection.commit()
    return [product_id]


@app.post('/admin/update-product')
def updateProduct():
    form_date = request.get_json()
    product_id = form_date['id']
    name = form_date['name']
    description = form_date['description']
    result = connection.execute(text(f"""
    UPDATE `product` 
    SET `name` = '{name}',
    `description` = '{description}' 
    WHERE
        id = '{product_id}'
    """))
    connection.commit()
    return [product_id, name, description]


def getProductList():
    result = connection.execute(text("""
                SELECT
                product.id,
                product.name,
                product.cost,
                product.price,
                category.`name` as category,
                product.description,
                category.`id` as category_id
            FROM
                product
                INNER JOIN category ON product.category_id = category.id
    	"""))
    recode = result.fetchall()

    data = []
    for item in recode:
        data.append(
            {
                'id': item[0],
                'name': item[1],
                'cost': item[2],
                'price': item[3],
                'category': item[4],
                'description': item[5],
                'category_id': item[6],
            }
        )
    connection.commit()
    return data


