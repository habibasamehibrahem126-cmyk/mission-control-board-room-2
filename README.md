# Mission Control: Board Room

## Set up (once)

1. `python -m venv .venv`
2. `.venv\Scripts\activate` (macOS or Linux: `source .venv/bin/activate`)
3. `pip install -r requirements.txt`
4. Copy `config/prices.example.json` to `config/prices.local.json` and fill in the two prices. Never commit it.

## Run

1. `python -m src.api.app`
2. Open http://127.0.0.1:5001
3. Restart after changing code (Ctrl+C stops). Reload the browser.

## Steps

Do them in order. Each step ends with a check, then your instructor reviews it.

| Step | You work on | Check |
| --- | --- | --- |
| 1. Set up | repository, Python, price file | The dashboard opens |
| 2. Clean the data | `src/data/prepare.py` | `python -m pytest tests/test_data.py` then `python -m src.data.prepare` |
| 3. Train the model | `src/model/train.py`, `src/model/predict.py` | `python -m pytest tests/test_model.py` then `python -m src.model.train` |
| 4. Write the rules | `src/api/rules.py` | `python -m pytest tests/test_rules.py` |
| 5. Core API | `src/api/app.py` | `python -m pytest tests/test_api.py` |
| 6. Dashboard API | `src/api/app.py` | `python -m pytest tests/test_dashboard.py` |
| 7. Whole product | `tests/test_end_to_end.py`, this README | `python -m pytest` |
| 8. Demo | nothing new | No panel says "Not built yet" |

## Save after each approved step

```text
git add .
git commit -m "Step 2: clean the data"
git push
```

## Team rules

- One laptop, one step at a time.
- A different person types at each step. The others read, check and suggest.
- Start the next step only after the review.
