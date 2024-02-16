from flask import Flask, render_template, request
import test
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # keywords = request.form['keywords']
        # products = scrape_ecommerce_site(keywords)
        response = test.get_products_summary()
        products = response.json()['data']['search']['products']
        list_products = []
        for item in products:
            try:
                product_name = item['item']['product_description']['title']
                product_price = item['price']['formatted_current_price']
            except:
                product_name = 'N/A'
                product_price = 'N/A'
            list_products.append({'name': product_name, 'price': product_price})
        # print(products)
        return render_template('index.html', products=list_products)
    # if request.method == 'POST':
    #     # keywords = request.form['keywords']
        # products = scrape_ecommerce_site(keywords)
    #     response = test.get_products_summary()
    #     products = response.json()['data']['search']['products']
    #     return render_template('index.html', products=products)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


