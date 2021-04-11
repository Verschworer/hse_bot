import turicreate as tc

dataSFrame = tc.SFrame('fake_or_real_news.csv')
dataSFrame.remove_column('X1')

model = tc.text_classifier.create(dataset=dataSFrame,
                                  target='label',
                                  features=['title', 'text'],
                                  validation_set=None)
model.save('model_fake_or_real')
