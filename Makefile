# OCW Build Diary (ART-PROJECT.md). DAY=YYYY-MM-DD (several: DAY="D1 D2");
# without DAY the tool picks its default days. The OCW checkout it reads:
# OCW_REPO, else `ocw_repo` in ocw-art.toml, else ../OCW.

# Python 3.11+ (tomllib): the system one, never the pyenv default (3.8).
PYTHON ?= $(firstword $(wildcard /usr/bin/python3.13 /usr/bin/python3.12 /usr/bin/python3.11 /usr/bin/python3) python3)
DIARY = $(PYTHON) diary.py

.PHONY: help fetch gather journal sheets render diary publish publish-videos collect check test \
	install-timer uninstall-timer timer-status ocw-repo
.DEFAULT_GOAL := help

help: ## List the targets
	@grep -hE '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  %-16s %s\n", $$1, $$2}'

ocw-repo: ## Print the OCW checkout the tool reads
	@$(DIARY) ocw-repo

fetch: ## Download and unpack day zips from the release build-history (OCW-ART, else OCW's)
	$(DIARY) fetch $(DAY)

gather: ## Collect the day's images/videos/sounds/logs and write its journal
	$(DIARY) gather $(DAY)
	$(DIARY) journal $(DAY)

journal: ## Write the day's journal (journal.md/json, tokens.json; masked)
	$(DIARY) journal $(DAY)

sheets: ## Contact sheets of the day's media for writing days/DAY.toml
	$(DIARY) sheet $(DAY)

render: ## Render the day video(s) from days/*.toml
	$(DIARY) render $(DAY)

diary: ## Join all day videos into the diary video
	$(DIARY) diary

publish: ## Upload day zips, videos and SHA256SUMS to the release build-history of newkit/OCW-ART
	$(DIARY) publish $(DAY)

publish-videos: ## Upload only the videos and SHA256SUMS
	$(DIARY) publish --videos

collect: ## One run of the hourly collector now (yesterday and today; DAY=... for other days)
	./collect.sh $(DAY)

check: ## Fail if a tracked text file of build-history/ holds a private pattern (FIX=1 masks them)
	$(DIARY) check-masked $(if $(FIX),--fix)

test: ## Unit tests of diary.py, music.py, features.py and collect.sh (fixture archive, hermetic)
	$(PYTHON) -m unittest discover -s . -p 'test_*.py'

UNITS = ocw-art-collect.service ocw-art-collect.timer
USER_UNITS = $(HOME)/.config/systemd/user

install-timer: ## Install and start the hourly collector as a systemd user timer (this checkout)
	mkdir -p $(USER_UNITS)
	for u in $(UNITS); do sed 's|@REPO@|$(CURDIR)|g' systemd/$$u > $(USER_UNITS)/$$u; done
	systemctl --user daemon-reload
	systemctl --user enable --now ocw-art-collect.timer
	@echo "Art collector: hourly (make timer-status); to run without a login: sudo loginctl enable-linger $$USER"

uninstall-timer: ## Stop and remove the hourly collector's systemd user timer
	-systemctl --user disable --now ocw-art-collect.timer
	-systemctl --user stop ocw-art-collect.service
	rm -f $(USER_UNITS)/ocw-art-collect.service $(USER_UNITS)/ocw-art-collect.timer
	-systemctl --user daemon-reload

timer-status: ## The collector timer's next/last run and the last run's status file
	-systemctl --user list-timers --all 'ocw-art-*'
	@-systemctl --user --no-pager status ocw-art-collect.service 2>/dev/null | head -n 5
	@-grep -h '^ExecStart=' $(USER_UNITS)/ocw-art-collect.service 2>/dev/null | sed 's/^/Installed: /'
	@ocw=$$($(DIARY) ocw-repo); f=$$(ls -1 $$ocw/test-output/build-log/*/art.json 2>/dev/null | sort | tail -n 1); \
	  if [ -n "$$f" ]; then echo "Last run ($$f):"; cat "$$f"; else echo "No collector run yet ($$ocw/test-output/build-log/DAY/art.json)."; fi
