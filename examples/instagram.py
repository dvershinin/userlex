from userlex.social_media import SocialMedia
message = """Hello baby how are you now can you add me in WhatsApp+639124267904 line: rachelplutdo"""
social_media = SocialMedia.parse(message)

for m in social_media:
    print("=================================")
    print(f"{m.PLATFORM_NAME}: {m.username}")
    if hasattr(m, "url"):
        print(f"URL: {m.url}")
