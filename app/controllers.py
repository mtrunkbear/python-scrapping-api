# from flask import Flask, render_template, request, redirect, session
from src.scrapping.coolblue import get_products
from main import application
import json
import os

absolute_path = os.path.dirname(__file__)


@application.route('/api/product/<product>', methods=['GET'])
def get_product_list(product):
    product_clases = {"microwaves": {"url": "https://www.coolblue.nl/en/microwaves/freestanding/solo-microwaves"},
                      "washers&dryers": {"url": "http://www.coolblue.nl/en/washer-dryer-combos/filter"}}
    data_path = "./storage/"+product+".json"
    if os.path.exists(data_path):
        with open(data_path, "r") as json_file:
            data = json.load(json_file)
    else:
        data = get_products(product_clases[product]["url"])
        write_data = json.dumps(data)
        with open(data_path, "w") as outfile:
            outfile.write(write_data)

    response = application.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response
