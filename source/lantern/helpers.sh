#!/usr/bin/env bash

green()  { printf "\033[32m%s\033[0m" "$1"; }
yellow() { printf "\033[33m%s\033[0m" "$1"; }
red()    { printf "\033[31m%s\033[0m" "$1"; }
blue()   { printf "\033[34m%s\033[0m" "$1"; }
bold()   { printf "\033[1m%s\033[0m" "$1"; }

metrics_record() {
  mkdir -p "$HOME/.garden/metrics"
  echo "$(date '+%Y-%m-%d %H:%M:%S') $1" >> "$HOME/.garden/metrics/commands.log"
}

weave_heartbeat() {
    garden heartbeat
}


show_help() {
  echo "🌿 Garden — Available Commands"
  echo "  garden help"
  echo "  garden version"
  echo "  garden paths"
  echo "  garden init"
  echo "  garden status"
  echo "  garden profile [list|create|use|active]"
  echo "  garden log [write|show]"
  echo "  garden events [emit|show]"
  echo "  garden metrics [show|summary]"
  echo "  garden weave [start|stop|status|heartbeat]"
  echo "  garden inspect [profiles|logs|events|metrics|weave]"
  echo "  garden plugin [list|run]"
  echo "  garden palette"
}

show_version() { cat "$HOME/.garden/version.txt"; }
show_paths() { echo "Garden root: $HOME/.garden"; echo "Lantern: $HOME/.garden/lantern"; }
status_show() { echo "Garden status: OK"; }

profile_list() { ls "$HOME/.garden/profiles"; }
profile_create() { mkdir -p "$HOME/.garden/profiles/$1"; echo "Created profile: $1"; }
profile_use() { echo "$1" > "$HOME/.garden/profiles/active"; echo "Active profile: $1"; }
profile_active() { cat "$HOME/.garden/profiles/active"; }

log_write() { echo "$(date '+%Y-%m-%d %H:%M:%S') $1" >> "$HOME/.garden/logs/garden.log"; }
log_show() { cat "$HOME/.garden/logs/garden.log"; }

event_emit() { echo "$(date '+%Y-%m-%d %H:%M:%S') $1 $2" >> "$HOME/.garden/events/events.log"; }
event_show() { cat "$HOME/.garden/events/events.log"; }

metrics_show() { cat "$HOME/.garden/metrics/commands.log"; }
metrics_summary() { wc -l "$HOME/.garden/metrics/commands.log"; }

weave_start() {
 echo "$(date '+%Y-%m-%d %H:%M:%S') weave start" >> "$HOME/.garden/presence/threads/weave.log"
 echo "Weave started";
}
weave_stop() {
 echo "Weave stopped";
 echo "$(date '+%Y-%m-%d %H:%M:%S') weave stop" >> "$HOME/.garden/presence/threads/weave.log"
}
weave_status() {
 echo "Weave status: OK"; 
 echo "$(date '+%Y-%m-%d %H:%M:%S') weave status" >> "$HOME/.garden/presence/threads/weave.log"
}
weave_heartbeat() { 
 echo "❤️"; 
 echo "$(date '+%Y-%m-%d %H:%M:%S') weave heartbeat" >> "$HOME/.garden/presence/threads/weave.log"
}

inspect_profiles() { ls "$HOME/.garden/profiles"; }
inspect_logs() { ls "$HOME/.garden/logs"; }
inspect_events() { ls "$HOME/.garden/events"; }
inspect_metrics() { ls "$HOME/.garden/metrics"; }
inspect_weave() { echo "Weave inspection OK"; }

plugin_list() { ls "$HOME/.garden/plugins"; }
plugin_run() { "$HOME/.garden/plugins/$1"; }

palette_show() {
  echo "Garden Palette:"
  echo "  Green: growth"
  echo "  Yellow: attention"
  echo "  Red: error"
  echo "  Blue: calm"
}

