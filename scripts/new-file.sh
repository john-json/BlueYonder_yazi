#!/bin/sh

printf 'New file name (blank to cancel): ' > /dev/tty
IFS= read -r name < /dev/tty || exit 1
[ -n "$name" ] || exit 0

case "$name" in
  /*) target="$name" ;;
  *)  target="./$name" ;;
esac

if [ -e "$target" ] || [ -L "$target" ]; then
  printf 'Already exists: %s\nPress Enter to return.' "$name" > /dev/tty
  IFS= read -r answer < /dev/tty
  exit 1
fi

if [ ! -d "$(dirname "$target")" ]; then
  printf 'Parent directory does not exist.\nPress Enter to return.' > /dev/tty
  IFS= read -r answer < /dev/tty
  exit 1
fi

exec nvim -- "$target"
