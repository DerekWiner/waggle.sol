// tests/waggle_ops_test.rs
// Unit tests for the Waggle.sol ritual and validation stub

use anchor_lang::prelude::*;
use waggle_ops::*;

#[tokio::test]
async fn test_check_manifest_valid() {
    let expected_hash = "YK4h0pepnRw5lFmxwA9-61ODxEbnlyCSFznH9DUfhyQ".to_string();

    let authority = Pubkey::new_unique();
    let ctx = Context::new(
        &mut ValidateAnchor { authority: Signer::new(&authority) },
        &[],
    );

    let result = waggle_ops::check_manifest_integrity(ctx, expected_hash);
    assert!(result.is_ok());
}

#[tokio::test]
async fn test_check_manifest_invalid() {
    let wrong_hash = "WRONGHASH123".to_string();

    let authority = Pubkey::new_unique();
    let ctx = Context::new(
        &mut ValidateAnchor { authority: Signer::new(&authority) },
        &[],
    );

    let result = waggle_ops::check_manifest_integrity(ctx, wrong_hash);
    assert!(result.is_err());
}

#[tokio::test]
async fn test_trigger_ritual() {
    let ritual = "test_ritual".to_string();
    let anchor = "test_anchor".to_string();

    let authority = Pubkey::new_unique();
    let ctx = Context::new(
        &mut Trigger { authority: Signer::new(&authority) },
        &[],
    );

    let result = waggle_ops::trigger_ritual(ctx, ritual, anchor);
    assert!(result.is_ok());
}
