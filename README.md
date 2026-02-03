# DomainAndIpManager

Manage domain/IP lists for AI and GFW contexts, run DNS lookups, and export timestamped outputs. Includes CLI scripts and a GUI editor.

## Quick Start (GUI)
```bash
./start_gui.sh
```
Open `http://127.0.0.1:5000`.

## Demo
![Domain & IP Manager demo](demos/demo.png)

## CLI Usage
```bash
python3 code/nslookup_simplified.py
python3 code/nslookup_simplified_gfw.py
python3 code/nslookup_simplified_gfw_w_ai.py
python3 code/nslookup_simplified_gfw_wo_ai.py
python3 code/nslookup.py
```
Each script prints results to the terminal and writes `output/<script>_YYYYMMDD_HHMMSS.txt`.

## Data Files
Lists are line-delimited and stored under `data/`:
- `ai_*` for AI-only lists
- `gfw_*` for GFW lists
- `ai_gfw_*` for combined lists
- `gfw_wo_ai_*` for GFW without AI
- `non_gfw_*` for China-accessible (non-GFW) lists
- `default_*` for the legacy/default list

Example:
```
data/ai_domains.txt
data/ai_custom_ips.txt
data/ai_cidr.txt
data/ai_mask.txt
```

## Outputs
- GUI + CLI: `output/<script or gui>_YYYYMMDD_HHMMSS.txt`
- Sorting tools: `output/domain_and_ips_unique_sorted.txt` and `.json`

## Dependencies
```bash
pip install -r requirements.txt
```

## Notes
- One entry per line in data files.
- `*_mask.txt` controls CIDR mask (default is `32`, `default` list uses `24`).

## Donate

<div align="center">
<table style="margin:0 auto; text-align:center; border-collapse:collapse;">
  <tr>
    <td style="text-align:center; vertical-align:middle; padding:6px 12px;">
      <a href="https://chat.lazying.art/donate">https://chat.lazying.art/donate</a>
    </td>
    <td style="text-align:center; vertical-align:middle; padding:6px 12px;">
      <a href="https://chat.lazying.art/donate"><img src="figs/donate_button.svg" alt="Donate" height="44"></a>
    </td>
  </tr>
  <tr>
    <td style="text-align:center; vertical-align:middle; padding:6px 12px;">
      <a href="https://paypal.me/RongzhouChen">
        <img src="https://img.shields.io/badge/PayPal-Donate-003087?logo=paypal&logoColor=white" alt="Donate with PayPal">
      </a>
    </td>
    <td style="text-align:center; vertical-align:middle; padding:6px 12px;">
      <a href="https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400">
        <img src="https://img.shields.io/badge/Stripe-Donate-635bff?logo=stripe&logoColor=white" alt="Donate with Stripe">
      </a>
    </td>
  </tr>
  <tr>
    <td style="text-align:center; vertical-align:middle; padding:6px 12px;"><strong>WeChat</strong></td>
    <td style="text-align:center; vertical-align:middle; padding:6px 12px;"><strong>Alipay</strong></td>
  </tr>
  <tr>
    <td style="text-align:center; vertical-align:middle; padding:6px 12px;"><img alt="WeChat QR" src="figs/donate_wechat.png" width="240"/></td>
    <td style="text-align:center; vertical-align:middle; padding:6px 12px;"><img alt="Alipay QR" src="figs/donate_alipay.png" width="240"/></td>
  </tr>
</table>
</div>
