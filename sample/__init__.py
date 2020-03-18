import core
import database


db_name = 'web_scraping'
tb_name = 'vnexpress_giao_duc'

database.create_database(db_name)
database.use_database(db_name)
database.create_table(tb_name)

data = core.get_article('list_news')

for x in data:
    values = {'title': x['title'], 'description': x['description'], 'url': x['url']}
    validated_val = {}
    validated_val['title'] = values['title'].replace("'", "''")
    validated_val['description'] = values['description'].replace("'", "''")
    validated_val['url'] = values['url'].replace("'", "''")

    database.insert_data(tb_name, validated_val)

database.show_data(tb_name)
output = database.fetch_data()

for x in output:
    print(x)

database.commit_db()

