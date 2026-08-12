import argparse
import ssl
from csv import writer
from pathlib import Path

import requests
from requests.adapters import HTTPAdapter

from python_stuff._paths import project_root

API_KEY = "540e2ca4-41e1-4186-8497-fdd67024ac44"
API_URL = (
    "https://data.moenv.gov.tw/api/v2/aqx_p_432"
    f"?api_key={API_KEY}&limit=1000&sort=ImportDate%20desc&format=JSON"
)
FIELDS = [
    ("county", "縣市"),
    ("sitename", "測站名稱"),
    ("aqi", "AQI"),
    ("status", "空氣品質"),
    ("o3_8hr", "O3_8h(ppb)"),
    ("o3", "O3(ppb)"),
    ("pm2.5", "PM2.5(μg/m3)"),
    ("pm10", "PM10(μg/m3)"),
    ("co_8hr", "CO_8h(ppm)"),
    ("so2", "SO2(ppb)"),
    ("no2", "NO2(ppb)"),
]


class _LenientSSLAdapter(HTTPAdapter):
    """Relax VERIFY_X509_STRICT only (keeps CA chain + hostname checks).

    Python 3.13+ enables ssl.VERIFY_X509_STRICT by default, which rejects
    GCA-issued government certificates lacking a Subject Key Identifier.
    """

    def init_poolmanager(self, *args, **kwargs):
        ctx = ssl.create_default_context()
        ctx.verify_flags &= ~ssl.VERIFY_X509_STRICT
        kwargs["ssl_context"] = ctx
        return super().init_poolmanager(*args, **kwargs)


_SESSION = requests.Session()
_SESSION.mount("https://", _LenientSSLAdapter())


def fetch_aqi() -> list[list[str]]:
    response = _SESSION.get(API_URL)
    response.raise_for_status()
    records = response.json()
    if isinstance(records, dict):
        records = records.get("records", [])
    return [[header for _, header in FIELDS]] + [
        [record.get(key) for key, _ in FIELDS] for record in records
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description="Download Taiwan AQI data to CSV")
    parser.add_argument(
        "--output", type=Path, default=project_root() / "outputs" / "AQI.csv"
    )
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open(mode="w", encoding="utf-8", newline="") as csv_file:
        writer(csv_file).writerows(fetch_aqi())
    print(f"Saved to {args.output}")


if __name__ == "__main__":
    main()
