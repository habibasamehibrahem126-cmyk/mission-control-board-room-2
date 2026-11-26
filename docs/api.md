# Endpoints: Board Room

## GET /options  (already done)

`{"orbits": [...], "launch_sites": [...]}`

## POST /predict  (step 5)

Request: one mission.

```json
{"payload_mass_kg": 5500, "orbit": "GTO", "launch_site": "CCAFS SLC 40", "block": 5,
 "reused": true, "flights": 3, "grid_fins": true, "legs": true}
```

Answer (200):

```json
{"lands": true, "probability": 0.87, "certainty": "high", "price_usd_million": 73.0,
 "price_basis": "p x reused price + (1 - p) x other price", "price_note": null}
```

- Wrong input: status 422, `{"error": "invalid_input", "fields": {"payload_mass_kg": "must be a number above 0"}}`
- `predict` raises `FileNotFoundError`: status 503, `{"error": "no_model", "message": "No model is trained yet."}`
- No price file: `price_usd_million` is `null` and `price_note` says why.

## GET /metrics  (step 5)

The content of `models/metrics.json`. If the file does not exist: `{"note": "No model has been trained yet."}`

# Step 6: your dashboard

## GET /summary

Counted from the launch table. Read it with `load_launches(clean_path)`.

```json
{"launches": 90, "landed": 60, "landing_rate": 0.667,
 "by_year":  [{"year": 2013, "launches": 3, "landed": 0}],
 "by_site":  [{"site": "CCAFS SLC 40", "launches": 55, "landed": 33}],
 "by_orbit": [{"orbit": "GTO", "launches": 27, "landed": 14}]}
```

The numbers above are examples. JSON needs plain Python numbers: wrap pandas results in `int()` or `float()`.
