from userlex.social_media import SocialMedia


def test_social_media_instagram():
    media = SocialMedia.parse("Instagram: @userlex")
    assert len(media) == 1
    assert media[0].username == "userlex"
