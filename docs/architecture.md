# Architecture

```text
OFFLINE   data/raw -> Data -> clean table -> Model -> saved model + scores

ONLINE    Dashboard (ready) <- HTTP + JSON -> API (Flask) <- loads - saved model
                                              ^
                                              | reads
                                price file (local only), clean table
```

Only the API loads the model. The same Flask app serves the dashboard at `/`.

## Parts, in the order you build them

| Part | Step | Takes in | Gives out |
| --- | --- | --- | --- |
| Data | 2 | `data/raw/launches_api.csv` | `data/processed/launches_clean.csv`, `quality_report.json` |
| Model | 3 | Clean table | `models/model.joblib`, `models/metrics.json`, `predict()` |
| Rules | 4 | A mission, a probability | Errors, certainty, price |
| API | 5 and 6 | A mission (JSON) | `/predict`, `/metrics`, your dashboard's endpoints |
| End-to-end test | 7 | All parts | Proof that they work together |

Endpoints: `docs/api.md`. Shared names: `src/common.py`. Change a contract only if the team agrees.

## C1. Clean table (Data to Model and API)

| Column | Type | Use |
| --- | --- | --- |
| `Class` | 0 or 1 | target |
| `PayloadMass` | number, kg, no blanks | input |
| `Orbit`, `LaunchSite` | text | input |
| `Block`, `Flights` | whole number | input |
| `Reused`, `GridFins`, `Legs` | True or False | input |
| `Date`, `Outcome`, `Serial`, `LandingPad`, `Longitude`, `Latitude` | as raw | kept |

Do not use `ReusedCount`: it includes reuses made after the launch.

`quality_report.json`: `{"rows_in", "rows_out", "missing_filled": {column: count}, "notes": []}`

## C2. Model to API

- `predict(mission, model_path)` returns a probability from 0 to 1.
- No saved model: raises `FileNotFoundError`.
- `metrics.json`: `{"accuracy", "baseline_accuracy", "confusion_matrix", "n_train", "n_test", "trained_at"}`

## C3. Price file

`config/prices.local.json`, never committed:

```json
{"reused_price_usd_million": <figure>, "other_price_usd_million": <figure>}
```
