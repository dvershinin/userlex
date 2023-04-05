from userlex.social_media import SocialMedia
message = "Hey, my instagram is @userlex, and my twitter is @userlex_"
social_media = SocialMedia.parse(message)
for m in social_media:
    print(m.username)
    print(m.url)
    print
