# Requirements (today)

Your dashboard is for the **Finance Director**.

| ID | Requirement | Met when |
| --- | --- | --- |
| REQ-01 | Prepare a clean table with a landing label | No blanks except the landing pad. `Class` is only 0 or 1. A missing column stops the run and is named. |
| REQ-02 | Predict whether the first stage lands | A valid mission gets "lands" or "does not land". A wrong or missing value is named. |
| REQ-03 | Show probability and certainty | High: 80% or more, or 20% or less. Medium: 65% or more, or 35% or less. Otherwise low. |
| REQ-04 | Show the expected price | p x (reused price) + (1 - p) x (other price), in USD million. No price file: no price, and a message. |
| REQ-05 | Report model quality | Accuracy on the most recent launches, next to "always the most common answer". |
| REQ-06 | Work in a browser | The dashboard works with nothing to install for the user. |
| REQ-09 | Summarise the history | One screen: totals and landing rate by year, site and orbit. |

## Rules

- Landed = `Outcome` starts with `True` (ground pad, drone ship or ocean).
- Prices come from the customer brief and go only into `config/prices.local.json`.
- The customer has not confirmed the landing, certainty or price rules.
