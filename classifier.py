import config
import turicreate as tc
import pandas as pd


def classified_write():
    """use model to classify target dataset by
     two classes FAKE/REAL, and write to db dataframe"""
    base = pd.read_csv(config.csv_news)
    model = tc.load_model('model_fake_or_real')
    target = tc.SFrame.read_csv(config.csv_news, verbose=False)\
        .remove_column('link').remove_column('date')
    classify = model.classify(tc.SFrame(target))
    classified = pd.DataFrame(classify)
    base['classified'] = classified['class']
    base['probability'] = classified['probability'].round(2)

    # return print(target, flush=True)
    return base.to_csv(config.csv_classified, index=False)

