from flask import Flask, render_template, request
from config import Config
from models import db, Country

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            criteria = request.form['criteria']
            countries = Country.query.all()
            country_list = [{'name': c.name, 'area': c.area, 'population': c.population, 'density': c.density, 'gdp': c.gdp} for c in countries]
            sorted_countries = merge_sort(country_list, criteria)
            return render_template('index.html', countries=sorted_countries)
        return render_template('index.html', countries=[])

    return app

def merge_sort(data, criteria):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half, criteria)
        merge_sort(right_half, criteria)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][criteria] > right_half[j][criteria]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

    return data

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
