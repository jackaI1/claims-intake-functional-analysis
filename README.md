I built a claim intake checker because I wanted to test whether my written process could catch missing and conflicting details before someone starts reviewing a claim.

It takes fictional home insurance claims, checks them against a small set of rules and puts anything incomplete or inconsistent in a queue for a person. A complete claim goes to an adjuster for the next step. It never approves coverage or payment. All sample claims, policies and business estimates are invented.

To try it, use Python 3.9 or later. There is nothing to install. From this folder, run:

```sh
python3 -m claims_intake --db demo.sqlite seed samples/policies.json
python3 -m claims_intake --db demo.sqlite submit samples/claims.json --as-of 2026-01-15
python3 -m claims_intake --db demo.sqlite queue
python3 -m claims_intake --db demo.sqlite summary
```

On a fresh database, the 12 sample claims produce 2 ready records and 10 needing review. Each flagged record shows what needs attention. Repeating the same submission returns the original records without creating copies. Use sample data only; I have not built the privacy and access controls needed for real claims.

## What I wanted to decide

I compared a manual checklist, a shared spreadsheet and rules-assisted intake. The [short decision note](docs/decision-summary.md) explains my recommendation, costs, risks and what would change the decision. At an assumed 1,000 submissions per month and 30% needing review, the assisted option estimates 95 handling hours per month versus 200 manually. These are planning assumptions, not measured savings.

I chose to build the assisted option so I could test the written requirements against actual results. The [functional analysis](docs/functional-analysis.md) includes the current and future process maps, people involved, inputs, business rules and limits. The [requirements template](docs/requirements-template.md) is reusable; the [completed catalogue](docs/requirements.json) holds the 15 requirements for this process.

## Follow a claim through review

The third sample record has a blank description. I can record a follow-up action using its internal record number:

```sh
python3 -m claims_intake --db demo.sqlite show 3
python3 -m claims_intake --db demo.sqlite review 3 --action request_information --reviewer DEMO-R01
python3 -m claims_intake --db demo.sqlite summary
```

Now 9 records remain pending. The original reasons remain stored, along with who recorded the action and when. Other actions are `refer_adjuster` and `close_duplicate`; closing as a duplicate requires a duplicate/conflict flag. Actions record triage, not a completed claim investigation. One action is allowed per flagged record. A corrected submission gets its own version for a person to compare; it does not silently clear previous flags.

The `show` command displays the submitted details, audit history, recorded review action and related record numbers. I can open those numbers with `show` too when I need to compare a conflict. Related numbers are navigation hints; they do not change earlier routing decisions.

To try my own synthetic examples, I copy [samples/claims.json](samples/claims.json), edit the details and submit the new file with an explicit evaluation date. The [data contract and rule table](docs/functional-analysis.md#data-contract) explain accepted fields. Amounts are whole cents, dates use YYYY-MM-DD and evidence labels stand in for documents. Remove the local `demo.sqlite` file when finished, or choose another database filename for a fresh run.

## How the pieces fit

The command line reads a JSON file, a plain text format for structured records. [core.py](claims_intake/core.py) checks the rules and stores results in SQLite, a database held in one local file. Each new submission stores its original contents, reasons and an audit event. A batch either saves completely or saves nothing. Exact retries return the original decision, while a changed submission under an existing reference or a possible repeated loss goes to review.

The queue is for pending work; the summary also counts records already reviewed. Policy snapshots stay fixed so a retry cannot quietly change the context of an earlier decision. The prototype scans existing records for duplicates and has no web service or customer login. I would need a representative pilot, policy integration, privacy controls and performance testing before using it beyond local synthetic data.

## Checks and reports

```sh
python3 scripts/run_qa.py
python3 -m unittest discover -v
python3 -m claims_intake.options
```

The [QA plan](docs/qa-test-plan.md) traces tests to every requirement. The runner executes all tests and regenerates [the requirement report](reports/qa.md), [sample results](reports/sample-run.json) and [option estimates](reports/options.json). A requirement fails if any linked test fails, is skipped or has no executed coverage. The option model is in [options.py](claims_intake/options.py) so I can change the volume or review-rate assumptions and recalculate.

GitHub Actions runs the same checks on Python 3.9 and 3.13, compares the generated reports with the committed copies and saves the reports with each run. The current suite has 22 test methods, including boundary and invalid-input subcases, and covers all 15 requirements. It checks real database persistence, rollback after a storage failure, duplicate handling, human actions and the command line. No external service is needed.
