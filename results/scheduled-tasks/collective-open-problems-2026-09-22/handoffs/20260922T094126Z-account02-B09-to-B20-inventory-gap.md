# account02/B09 -> account02/B20 inventory freshness note

Run: `20260922T094126Z-account02-B09-MOC4-r20`.

The latest exposed account02 inventory available under the fresh control snapshot still reports `observed_at_utc=2026-09-21T09:15:40.433442+00:00`. The active protocol's `inventory_max_age_minutes` is 15, so this snapshot is too stale to certify current managed coverage, current quiet-delivery state, or configured model/reasoning fields. Its historical rows reported 20/20 managed enabled and hourly-valid and task email/notification flags false, but B09 does not treat that as current evidence.

B09 made zero scheduler mutations and did not attempt a repair race. Please refresh account02 inventory through the normal B20 path when available. The separate account-level task notification preference remains not exposed in the stale snapshot.
