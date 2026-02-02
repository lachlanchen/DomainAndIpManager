#!/usr/bin/env python3
"""
Extract domains/IPs from screen-recorded traffic reports using OCR.

Dependencies:
- ffmpeg
- tesseract

Usage:
  python3 traffics/extract_youtube_traffic.py \
    --videos "traffics/ScreenRecording_02-03-2026 07-34-48_1.MP4" \
             "traffics/ScreenRecording_02-03-2026 07-36-29_1.MP4"
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from pathlib import Path

DOMAIN_RE = re.compile(r"\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b")
IP_RE = re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b")

YOUTUBE_SUFFIXES = [
    "googlevideo.com",
    "ytimg.com",
    "ggpht.com",
    "googleusercontent.com",
    "googleapis.com",
    "gstatic.com",
    "youtube.com",
    "youtu.be",
    "doubleclick.net",
    "app-analytics-services.com",
    "itunes.apple.com",
    "google.com",
    "google.cn",
    "google.com.hk",
    "google.com.sg",
]


def require_tool(name: str) -> None:
    if shutil.which(name) is None:
        raise SystemExit(f"Missing dependency: {name}")


def extract_frames(video: Path, out_dir: Path, fps: int) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        str(video),
        "-vf",
        f"fps={fps}",
        "-q:v",
        "2",
        str(out_dir / "frame_%04d.jpg"),
    ]
    subprocess.run(cmd, check=True)


def ocr_frames(frames: list[Path]) -> str:
    text_chunks = []
    for frame in frames:
        result = subprocess.run(
            ["tesseract", str(frame), "stdout", "--psm", "6"],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.stdout:
            text_chunks.append(result.stdout)
    return "\n".join(text_chunks)


def filter_domains(domains: set[str]) -> tuple[list[str], list[str]]:
    allowed = []
    suspicious = []
    for d in sorted(domains):
        if any(d == s or d.endswith("." + s) for s in YOUTUBE_SUFFIXES):
            allowed.append(d)
        else:
            suspicious.append(d)
    return allowed, suspicious


def valid_ip(ip: str) -> bool:
    try:
        parts = [int(p) for p in ip.split(".")]
    except ValueError:
        return False
    return len(parts) == 4 and all(0 <= p <= 255 for p in parts)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--videos", nargs="+", required=True, help="Input video files")
    ap.add_argument("--fps", type=int, default=1, help="Frames per second to OCR")
    ap.add_argument("--out", default="traffics", help="Output directory")
    ap.add_argument("--keep-frames", action="store_true", help="Keep extracted frames")
    args = ap.parse_args()

    require_tool("ffmpeg")
    require_tool("tesseract")

    out_dir = Path(args.out)
    frames_root = out_dir / "frames"
    if frames_root.exists():
        shutil.rmtree(frames_root)
    frames_root.mkdir(parents=True, exist_ok=True)

    all_domains: set[str] = set()
    all_ips: set[str] = set()

    for idx, video in enumerate(args.videos, 1):
        vpath = Path(video)
        if not vpath.exists():
            raise SystemExit(f"Video not found: {vpath}")
        fdir = frames_root / f"vid_{idx}"
        extract_frames(vpath, fdir, args.fps)
        frames = sorted(fdir.glob("frame_*.jpg"))
        text = ocr_frames(frames)

        all_domains.update(d.lower() for d in DOMAIN_RE.findall(text))
        all_ips.update(ip for ip in IP_RE.findall(text))

    clean_ips = sorted({ip for ip in all_ips if valid_ip(ip)}, key=lambda s: tuple(int(x) for x in s.split(".")))
    clean_domains, suspicious = filter_domains(all_domains)

    raw_md = out_dir / "youtube_traffic_extracted.md"
    clean_md = out_dir / "youtube_traffic_extracted_clean.md"
    suspicious_md = out_dir / "youtube_traffic_suspicious.md"

    raw_lines = ["# YouTube Traffic (OCR Extract)", "", "## Domains", ""]
    raw_lines += [f"- {d}" for d in sorted(all_domains)]
    raw_lines += ["", "## IPs", ""]
    raw_lines += [f"- {ip}" for ip in clean_ips]
    raw_md.write_text("\n".join(raw_lines) + "\n", encoding="utf-8")

    clean_lines = ["# YouTube Traffic (OCR Extract - Cleaned)", "", "## Domains", ""]
    clean_lines += [f"- {d}" for d in clean_domains]
    clean_lines += ["", "## IPs", ""]
    clean_lines += [f"- {ip}" for ip in clean_ips]
    clean_md.write_text("\n".join(clean_lines) + "\n", encoding="utf-8")

    suspicious_lines = ["# Suspicious / Non-YouTube Domains (OCR)", ""]
    suspicious_lines += [f"- {d}" for d in suspicious]
    suspicious_md.write_text("\n".join(suspicious_lines) + "\n", encoding="utf-8")

    if not args.keep_frames:
        shutil.rmtree(frames_root)

    print(f"Raw domains: {len(all_domains)}")
    print(f"Clean domains: {len(clean_domains)}")
    print(f"Suspicious domains: {len(suspicious)}")
    print(f"IPs: {len(clean_ips)}")
    print(f"Outputs:\n- {raw_md}\n- {clean_md}\n- {suspicious_md}")


if __name__ == "__main__":
    main()
