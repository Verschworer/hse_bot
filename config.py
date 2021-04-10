from datetime import datetime

token = '1730646081:AAFvPdA6xIKZ3KgB09nYwW23DHCjTyLBqtE'
feeds = {'meduza.io': 'https://meduza.io/rss/en/all'}

csv_news = \
    'news_' + str(datetime.now().replace(second=0, microsecond=0)) + '.csv'

csv_classified = \
    'classified_' + str(datetime.now().replace(second=0, microsecond=0)) + '.csv'

# connection = {'host': 'https://hse-educate.us-central1-a.c.propane-folio-306110.internal:9000',
#               'database': 'news'}
