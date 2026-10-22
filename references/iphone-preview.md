# Real iPhone capture

Design evidence must come from a real iPhone simulator or device. A web screenshot, desktop
screenshot or HTML mock is not iOS evidence.

## 1. Adapt this to your host app

RONGE does not assume a specific build tool. A typical flow:

```bash
# 1. build your web assets / native app
# 2. install on a booted iPhone simulator
# 3. launch, wait for the first paint
# 4. capture with simctl
xcrun simctl io <UDID> screenshot /tmp/ronge-ui-review/home.png
```

If your app uses Capacitor, a build/sync/install wrapper is usually:

```bash
npm run build
npx cap sync ios
# then build/install with your own Xcode or simulator script
```

Do not use a browser screenshot as a substitute. If the first launch is slow, wait 15–25 seconds
and retake before calling it a blank screen.

## 2. Preview isolation

Unfinished directions must not replace production UI. Use a build-time switch:

```bash
VITE_HOME_PREVIEW=1 VITE_HOME_DIRECTION=a npm run build
```

Production builds must keep the real entry point. Each direction is built and captured separately.

## 3. States to cover

| State | What to inspect |
|---|---|
| default / content | hierarchy, primary action, image position |
| quiet / empty | does it avoid fake content and still offer a next step? |
| edit | drag handles, tool shelf, empty slots, tab-bar overlap |
| loading | skeleton/copy is product-specific, not a white screen |
| error/offline | is there a way out, without pretending success? |
| logged out | is the guide clear without faking a session? |
| long content | title wraps, buttons stay reachable, image not clipped |
| large text | Dynamic Type does not break layout |
| dark mode | if supported, contrast and imagery still work |

## 4. Capture checks

- Brand is not hidden by the status bar or notch.
- The tab bar does not cut a card or image.
- Image edges are intentional: fade into paper at the top; do not hard-cut at the bottom.
- Primary action is in the thumb zone, at least 44pt.
- No permission dialog covers the page.
- Inspect the screenshot yourself with an image reader; do not trust the script's success alone.

## 5. Accessibility

- Body ≥ 11pt; captions ≥ 10pt; key old states remain readable.
- Dynamic Type: no truncation or overlapping controls at large sizes.
- Icon buttons have VoiceOver labels.
- Respect reduce-motion.
- Do not communicate good/bad with color alone; pair color with direction words.

## 6. Archive

- Store screenshots under `artifacts/<date>/<version>/`.
- Record path and score in your product memory.
- Never call a preview "shipped" or "production" without user confirmation.
