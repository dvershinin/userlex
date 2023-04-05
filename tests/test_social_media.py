import fnmatch
import os

import pytest
import yaml

from userlex.social_media import SocialMedia


def get_yaml_files(root_dir):
    """Get all YAML files in a directory."""
    for root, dirnames, filenames in os.walk(root_dir):
        for filename in fnmatch.filter(filenames, '*.yml'):
            yield os.path.join(root, filename)


# cd to the tests directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))


@pytest.mark.parametrize(
    "yaml_file",
    get_yaml_files("profiles")
)
def test_social_media(yaml_file):
    """Test that social media profiles are parsed correctly."""
    with open(yaml_file, "r") as f:
        metadata = yaml.safe_load(f)
        media = SocialMedia.parse(metadata.get("text"))
        for profile in metadata.get("profiles"):
            found = False
            for m in media:
                if m.PLATFORM_NAME == profile.get("platform"):
                    assert m.username == profile.get("username")
                    if "url" in profile:
                        assert m.url == profile.get("url")
                    found = True
                    break
            assert found
