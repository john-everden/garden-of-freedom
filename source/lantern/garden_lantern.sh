#!/usr/bin/env bash

# ----------------------------------------
# Resolve script directory
# ----------------------------------------
SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)"


# ----------------------------------------
# Load helpers
# ----------------------------------------
. "$SCRIPT_DIR/helpers.sh"

# ----------------------------------------
# Parse command and arguments
# ----------------------------------------
COMMAND="$1"
SUBCOMMAND="$2"
ARG="$3"
ARG2="$4"


# ----------------------------------------
# FLOW: Command History Logging
# ----------------------------------------
echo "$(date '+%Y-%m-%d %H:%M:%S') $COMMAND $SUBCOMMAND $ARG $ARG2" >> "$HOME/.garden/history/commands.log"

# ----------------------------------------
# PRESENCE: Command Thread Logging   <--- ADD THIS BLOCK
# ----------------------------------------
echo "$(date '+%Y-%m-%d %H:%M:%S') $COMMAND $SUBCOMMAND" >> "$HOME/.garden/presence/threads/command.log"
"$SCRIPT_DIR/commands/graph_update" >/dev/null 2>&1


"$SCRIPT_DIR/commands/presence_loop" >/dev/null 2>&1




# ----------------------------------------
# Metrics recording
# ----------------------------------------
metrics_record "$COMMAND $SUBCOMMAND"

# ----------------------------------------
# Built‑in command router
# ----------------------------------------
case "$COMMAND" in
  "" | lantern | help)
    show_help
    ;;

  version)
    show_version
    ;;

  paths)
    show_paths
    ;;

  init)
    init_garden
    ;;

  status)
    status_show
    ;;

  profile)
    case "$SUBCOMMAND" in
      list) profile_list ;;
      create) profile_create "$ARG" ;;
      use) profile_use "$ARG" ;;
      active) profile_active ;;
      *) echo "Usage: garden profile [list|create|use|active]" ;;
    esac
    ;;

  log)
    case "$SUBCOMMAND" in
      write) log_write "$ARG" ;;
      show) log_show ;;
      *) echo "Usage: garden log [write|show]" ;;
    esac
    ;;

  events)
    case "$SUBCOMMAND" in
      emit) event_emit "$ARG" "$ARG2" ;;
      show) event_show ;;
      *) echo "Usage: garden events [emit|show]" ;;
    esac
    ;;

  metrics)
    case "$SUBCOMMAND" in
      show) metrics_show ;;
      summary) metrics_summary ;;
      *) echo "Usage: garden metrics [show|summary]" ;;
    esac
    ;;

  weave)
    case "$SUBCOMMAND" in
      start) weave_start ;;
      stop) weave_stop ;;
      status) weave_status ;;
      heartbeat) weave_heartbeat ;;
      *) echo "Usage: garden weave [start|stop|status|heartbeat]" ;;
    esac
    ;;

  inspect)
    case "$SUBCOMMAND" in
      profiles) inspect_profiles ;;
      logs) inspect_logs ;;
      events) inspect_events ;;
      metrics) inspect_metrics ;;
      weave) inspect_weave ;;
      *) echo "Usage: garden inspect [profiles|logs|events|metrics|weave]" ;;
    esac
    ;;

  plugin)
    case "$SUBCOMMAND" in
      list) plugin_list ;;
      run) plugin_run "$ARG" ;;
      *) echo "Usage: garden plugin [list|run]" ;;
    esac
    ;;

  palette)
    ~/.garden/lantern/commands/palette
    ;;

  *)
    # ----------------------------------------
    # EXTENDED COMMAND DISPATCH
    # ----------------------------------------
    if [ -x "$SCRIPT_DIR/commands/$COMMAND" ]; then
      shift
      exec "$SCRIPT_DIR/commands/$COMMAND" "$@"
    fi

    echo "Unknown command: $COMMAND"
    echo "Try: garden help"
    ;;
esac

"$SCRIPT_DIR/commands/graph_update" >/dev/null 2>&1
"$SCRIPT_DIR/commands/presence_loop" >/dev/null 2>&1
"$SCRIPT_DIR/commands/graph_update" >/dev/null 2>&1
"$SCRIPT_DIR/commands/presence_loop" >/dev/null 2>&1
"$SCRIPT_DIR/commands/rhythm_engine" >/dev/null 2>&1
"$SCRIPT_DIR/commands/cycle_engine" >/dev/null 2>&1
"$SCRIPT_DIR/commands/season_engine" >/dev/null 2>&1
"$SCRIPT_DIR/commands/era_engine" >/dev/null 2>&1
"$SCRIPT_DIR/commands/age_engine" >/dev/null 2>&1
"$SCRIPT_DIR/commands/aeon_engine" >/dev/null 2>&1
"$SCRIPT_DIR/commands/mythos_engine" >/dev/null 2>&1
"$SCRIPT_DIR/commands/cosmos_engine" >/dev/null 2>&1
"$SCRIPT_DIR/commands/meta_engine" >/dev/null 2>&1
