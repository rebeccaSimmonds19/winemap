import os
from os import environ
import shutil
from pyspark.sql import SparkSession
from pyspark.sql.functions import mean
from plotly.offline import plot
import argparse
from flask import Flask, render_template


app = Flask(__name__)


class WineMapGenerator:

    def __init__(self):
        server = "postgresql
        user = "user"
        password = "password"
        dbname = "wineDb"
        self.make(server,
                  user, dbname, password)

    def make(self, server, user, dbname, password):
        spark_session = SparkSession.builder.appName('winemap').getOrCreate()
        url = "jdbc:postgresql://{0}/{1}?user={2}&password={3}".format(
            server, dbname, user, password)
        df = spark_session.read.format("jdbc").options(
            url=url,
            dbtable="wine_reviews",
            driver="org.postgresql.Driver").load()
        table = (df.select('country', 'points')
            .groupBy('country').agg(mean('points'))
            .orderBy('avg(points)', ascending=False))
        country_cols = table.select('country').collect()
        countries = [country[0] for country in country_cols]
        point_cols = table.select('avg(points)').collect()
        points = [point[0] for point in point_cols]
        data = dict(type='choropleth',
                    locationmode='country names',
                    locations=countries,
                    colorscale='Jet',
                    z=points,
                    colorbar={'title': 'Average Rating'})
        layout = dict(geo={'scope': 'world'})
        choromap = dict(data=[data], layout=layout)
        plot(choromap, filename='map.html')


def make_template():
    # make the templates dir
    new_path = '/opt/app-root/src/templates'
    if not os.path.exists(new_path):
        os.makedirs(new_path)
        # move the file to the templates dir
        shutil.move('/opt/app-root/src/map.html', new_path)
    return render_template("map.html", title='Maps')

@app.route('/')
def index():
    WineMapGenerator()
    return make_template()


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
