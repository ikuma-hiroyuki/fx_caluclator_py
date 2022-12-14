import argparse

import requests

url = 'https://api.exchangerate.host/latest'

helpdoc = f"通貨ペアの為替計算を行います。{url}"
parser = argparse.ArgumentParser(description=helpdoc)
parser.add_argument("base", type=str, help="基準通貨(USD, JPYなど)")
parser.add_argument("conv", type=str, help="変換通貨(同上)")
parser.add_argument("price", type=float, help="基準通貨の金額")
args = parser.parse_args()

params = {
    "from": args.base.upper(),
    "to": args.conv.upper(),
    "amount": args.price,
}
request_url = 'https://api.exchangerate.host/convert'
responce = requests.get(request_url, params=params)
data = responce.json()

if data["success"]:
    result_price = data["result"]
    print(f"{args.price:,.2f} {args.base.upper()} = {result_price:,.2f} {args.conv.upper()}")
else:
    print("Failed.")
