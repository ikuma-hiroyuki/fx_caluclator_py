import argparse

import yfinance

parser = argparse.ArgumentParser(description="通貨ペアの為替計算を行います")
parser.add_argument("base", type=str, help="基準通貨(USD, JPYなど)")
parser.add_argument("conv", type=str, help="変換通貨(同上)")
parser.add_argument("price", type=int, help="基準通貨の金額")
args = parser.parse_args()

data = yfinance.download(f"{args.base}{args.conv}=X", period="1d", interval="1m", rounding=True, progress=False)
fx_price = data.Close[-1:].max() * args.price
print(f"{int(args.price)} {args.base.upper()} = {fx_price} {args.conv.upper()}")
