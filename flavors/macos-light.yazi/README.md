<div align="center">
  <h1>macOS Light Flavor for <a href="https://github.com/sxyazi/yazi">Yazi</a></h1>
</div>

A Finder-inspired light flavor for Yazi: grayscale text only, `#a4b9c6` for active text, and pill-shaped tabs and status bar segments.

## Preview

![preview](preview.png)

## Requirements

A recent Yazi release with flavor support and a [Nerd Font](https://www.nerdfonts.com/) in your terminal, which draws the rounded pill ends.

## Installation

```sh
ya pkg add <your-github-user>/<your-repo>:macos-light
```

Or copy this folder to `~/.config/yazi/flavors/macos-light.yazi/`.

## Usage

Add this to `~/.config/yazi/theme.toml`:

```toml
[flavor]
light = "macos-light"
```

To follow the system appearance, use both flavors:

```toml
[flavor]
dark  = "macos-dark"
light = "macos-light"
```

## Palette

| Role | Color |
|------|-------|
| Background | `#ffffff` |
| Text | `#1d1d1f` |
| Secondary text | `#6e6e73` |
| Active text | `#a4b9c6` |
| Selection and pills | `#48484a` |
| Borders | `#d2d2d7` |

## License

Released under the MIT License. See [LICENSE](LICENSE).
