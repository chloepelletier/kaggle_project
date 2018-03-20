import pandas as pd

submission_example = pd.read_csv('data/raw/sample_submission_nettebad.csv')

# test

submission_example.visitors_pool_total = result

submission_example.to_csv("data/processed/submission.csv")