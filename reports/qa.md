# Executed QA report

Fictional process, synthetic data. Regenerate with `python3 scripts/run_qa.py`.

Result: **PASS**. 22 test methods; 15/15 requirements passed.

A requirement passes only when every linked test passes. Missing coverage and skipped tests fail the gate.

Source SHA-256: `febcaf8d7506b5117368192b93f118388f079b61a86d8c056ef797f8e7d2195e`

| Requirement | Result | Executed test methods |
| --- | --- | --- |
| R01 | PASS | test_cli_roundtrip, test_complete_claim_routes_to_adjuster, test_malformed_batch_is_rejected_before_any_write, test_sample_batch_and_disk_reopen |
| R02 | PASS | test_bad_field_types_are_reviewable, test_every_required_business_field_can_be_missing |
| R03 | PASS | test_policy_and_property_conflicts, test_policy_boundaries_are_inclusive, test_policy_snapshot_is_immutable_and_atomic |
| R04 | PASS | test_dates_and_chronology, test_policy_boundaries_are_inclusive |
| R05 | PASS | test_amount_boundaries_and_loss_types, test_bad_field_types_are_reviewable |
| R06 | PASS | test_bad_field_types_are_reviewable, test_each_loss_type_evidence |
| R07 | PASS | test_identical_retry_is_idempotent_even_on_later_day, test_two_connections_share_duplicate_protection |
| R08 | PASS | test_conflicting_reference_preserves_both_versions, test_duplicate_signal_and_distinct_claims, test_two_connections_share_duplicate_protection |
| R09 | PASS | test_complete_claim_routes_to_adjuster, test_conflicting_reference_preserves_both_versions, test_every_required_business_field_can_be_missing |
| R10 | PASS | test_cli_roundtrip, test_identical_retry_is_idempotent_even_on_later_day, test_review_is_audited_and_removes_only_pending_item, test_sample_batch_and_disk_reopen |
| R11 | PASS | test_cli_roundtrip, test_review_guards_and_each_action, test_review_is_audited_and_removes_only_pending_item |
| R12 | PASS | test_cli_roundtrip, test_review_is_audited_and_removes_only_pending_item, test_sample_batch_and_disk_reopen |
| R13 | PASS | test_malformed_batch_is_rejected_before_any_write, test_policy_snapshot_is_immutable_and_atomic, test_storage_failure_rolls_back_claims_and_audit, test_two_connections_share_duplicate_protection |
| R14 | PASS | test_all_linked_tests_must_pass, test_missing_failed_and_skipped_coverage_cannot_pass |
| R15 | PASS | test_options_arithmetic_and_sensitivity |
