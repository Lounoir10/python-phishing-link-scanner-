def check_link(url):
    if not url.startswith("https://"):
        print("⚠️ Flag: Insecure link (missing https)!")
    elif "0" in url or "verify" in url:
        print("🚨 Flag: Suspicious lookalike domain or keyword!")
    else:
        print("✅ Link looks clean!")

#Test the function

check_link("http://micros0ft-login-verify.com/reset")

def check_link(url):
    if not url.startswith("https://"):
        print("⚠️ Flag: Insecure link (missing https)!")
    elif "0" in url or "verify" in url:
        print("🚨 Flag: Suspicious lookalike domain or keyword!")
    else:
        print("✅ Link looks clean!")


#Test the function
check_link("https://google.com")

def check_link(url):
    if not url.startswith("https://"):
        print("⚠️ Flag: Insecure link (missing https)!")
    elif "0" in url or "1" in url or "verify" in url:
        print("🚨 Flag: Suspicious lookalike domain or keyword!")
    else:
        print("✅ Link looks clean!")


#Test the function
check_link("https://paypa1-account.com/login")
