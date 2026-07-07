# Example: App Permission Failure

This example shows how `figure-it-out` handles a common software problem without jumping straight to random fixes.

## Situation

A user says:

> The upload button used to work, but now the app says `Permission denied` when I try to upload a file.

## Opening declaration

- **Symptom, exact and literal:** Upload fails with `Permission denied`.
- **Pass/fail signal:** The same user can upload the same test file through the same app and receive a successful upload confirmation.
- **Broken or never worked:** Used to work.
- **System boundary:** Browser or client app, user account, upload API, storage backend, permission policy, file object.
- **Current evidence:** User reports a permission error. It is not yet known whether the denial is local, account-level, API-level, or storage-level.
- **Risk boundary:** Do not broaden permissions globally, expose other users' files, or disable authorization checks.
- **Budget:** Check cheap/reversible causes first before changing policy.

## Minimum viable model

```text
user → client app → upload request → API permission check → storage write → success/failure
```

Likely interfaces:

- user identity to client session
- client token to API
- API policy to storage permission
- file metadata to validation rules

## Attempt ledger

| Attempt | Hypothesis | Test/change | Prediction | Result | Moved? |
|---|---|---|---|---|---|
| 1 | Session token expired or wrong identity | Sign out/in and inspect current account | Same user identity should appear and fresh token may fix upload | Upload still fails | N |
| 2 | User lost role or group assignment | Compare user's role to known-good user | Broken user missing upload role | User missing `uploader` role | Y |
| 3 | Role removal was accidental | Restore only the missing role for that user | Upload succeeds without global policy change | Upload succeeds | Y |

## Blast-radius log

| Change | Original state | Undo |
|---|---|---|
| Re-authenticated user | Existing session | Sign out again if needed |
| Restored `uploader` role for one user | User lacked role | Remove role |

## Closing record

- **Cause:** User-specific role assignment was removed or failed to sync.
- **Fix:** Restored the user's `uploader` role.
- **Unnecessary changes avoided:** No global permission broadening, no storage policy changes, no admin bypass.
- **Reusable pattern:** When a permission failure affects one user but not a known-good user, compare identity, role, group, token, and policy differences before changing global access.
