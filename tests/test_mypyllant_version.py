import re
from pathlib import Path


async def test_vaillantcloud_versions():
    """
    Make sure myVaillant library is set to the same versions in all important files
    """
    files = [
        Path(".").parent / "dev-requirements.txt",
        Path(".").parent / "custom_components/vaillantcloud/manifest.json",
    ]
    p = re.compile(r"myVaillant==(.*?)[\"\n]")
    matches = [re.findall(p, f.read_text()) for f in files]
    assert all(m == matches[0] for m in matches), (
        f"myVaillant versions are not the same in all files: {matches}"
    )
