import json
from collections import defaultdict
from app.models import Project, SubCategory


with open('data.json') as data_file:
    websites = json.load(data_file)


with open('website_cat.json') as data_file:
    sub_cats_temp = json.load(data_file)


sub_cats = defaultdict(list)


for s in sub_cats_temp:
    try:
        sub = SubCategory.objects.get(pk=s['category_id'])
        sub_cats[s['website_id']].append(sub)
    except:
        sub_cats[s['website_id']] = None


for website in websites:
    try:
        p = Project(title=website['name'], slogan=website['short_description'],
                    description=website['description'], url=website['url'],
                    image='https://www.famust.com/img/websites/{}.png'.format(website['id']))
        p.save()
        subs = sub_cats[website['id']]
        if subs:
            cats = [s.category for s in subs]
            p.sub_categories = subs
            p.categories = cats
    except Exception as e:
        print(e)
        pass
