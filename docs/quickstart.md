# A18 Quickstart Guide

## 10. Android 14 Power Management Fix
Если пайплайн падает ночью:
1. Отключить "Battery Optimization" для Termux и Radio Bot.
2. `termux-wake-lock` — обязателен.
3. Перед запуском TTS: `termux-volume music 15`.

## Pipeline Flow
Telegram → TTS → AZ → FFmpeg → zeno.fm
