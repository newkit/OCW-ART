# OCW Build Diary (docs/ART-PROJECT.md). DAY=YYYY-MM-DD (several: DAY="D1 D2");
# without DAY the tool picks its default days. The OCW checkout it reads:
# OCW_REPO, else `ocw_repo` in ocw-art.toml, else ../OCW.

# Python 3.11+ (tomllib): the system one, never the pyenv default (3.8).
PYTHON ?= $(firstword $(wildcard /usr/bin/python3.13 /usr/bin/python3.12 /usr/bin/python3.11 /usr/bin/python3) python3)
DIARY = $(PYTHON) diary.py

.PHONY: help deps ocw-repo fetch gather journal sheets render diary publish publish-videos collect check test \
	gallery gallery-preview gallery-publish gallery-deploy lfs-check lfs-budget lfs-commit lfs-push \
	install-timer uninstall-timer timer-status
.DEFAULT_GOAL := help

help: ## List the targets
	@grep -hE '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  %-16s %s\n", $$1, $$2}'

# ffmpeg (frames, scaling, the videos), git-lfs (the media in Git LFS, §2.8),
# zip, the Lato font; gh is checked, not installed (it needs a login).
DEPS_DEB = ffmpeg git-lfs zip unzip fonts-lato
DEPS_RPM = ffmpeg git-lfs zip unzip lato-fonts
deps: ## Check and install the tools (ffmpeg, git-lfs, zip; apt / dnf / brew hint), then `git lfs install`
	@missing=""; for t in ffmpeg ffprobe zip unzip flock; do command -v $$t >/dev/null || missing="$$missing $$t"; done; \
	  git lfs version >/dev/null 2>&1 || missing="$$missing git-lfs"; \
	  if [ -z "$$missing" ]; then echo "deps: ffmpeg, git-lfs, zip present"; \
	  elif command -v apt-get >/dev/null; then echo "deps: installing$$missing (apt)"; sudo apt-get install -y $(DEPS_DEB); \
	  elif command -v dnf >/dev/null; then echo "deps: installing$$missing (dnf)"; sudo dnf install -y $(DEPS_RPM); \
	  elif command -v brew >/dev/null; then echo "deps: missing$$missing - run: brew install ffmpeg git-lfs"; exit 1; \
	  else echo "deps: missing$$missing - install them with the system's package manager"; exit 1; fi
	git lfs install
	@$(PYTHON) -c 'import sys; sys.exit(sys.version_info < (3, 11))' || { echo "deps: needs Python 3.11+ ($(PYTHON))"; exit 1; }
	@if command -v gh >/dev/null && gh auth status >/dev/null 2>&1; then echo "deps: gh logged in"; \
	  else echo "deps: gh missing or not logged in (fetch and publish need it: gh auth login)"; fi

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

publish: ## Upload day zips, videos and SHA256SUMS to the release, then refresh the gallery (GALLERY=0: not)
	$(DIARY) publish $(DAY)
	$(if $(filter 0,$(GALLERY)),,$(DIARY) gallery publish --wait)

publish-videos: ## Upload only the videos and SHA256SUMS
	$(DIARY) publish --videos

collect: ## One run of the hourly collector now (yesterday and today; DAY=... for other days)
	bin/collect.sh $(DAY)

check: ## Fail if a tracked text file or a media name of build-history/ holds a private pattern (FIX=1 masks)
	$(DIARY) check-masked $(if $(FIX),--fix)

test: ## Unit tests (tests/: fixture archives and repositories, hermetic)
	$(PYTHON) -m unittest discover -s tests -p 'test_*.py'

# The gallery (§6): build-history/.work/gallery/site/, on GitHub Pages via the release.
MAX_MB ?= 900
PORT ?= 8000
gallery: ## Build the gallery locally (incremental; MAX_MB=900), then: make gallery-preview
	$(DIARY) gallery build --max-mb $(MAX_MB)
	@echo "Preview: make gallery-preview (http://127.0.0.1:$(PORT)/)"

gallery-preview: ## Serve the built gallery on http://127.0.0.1:8000/ (PORT=...)
	$(DIARY) gallery serve --port $(PORT)

gallery-publish: ## Build, upload the changed gallery zips to the release and deploy to GitHub Pages
	$(DIARY) gallery publish --max-mb $(MAX_MB) --wait

gallery-deploy: ## Only redeploy GitHub Pages from the gallery zips on the release
	$(DIARY) gallery deploy --wait

# Git LFS (§2.8): the day folders' pictures and videos, within the budget.
lfs-check: ## The LFS total, the budget (9 GiB) and the days left (also: make lfs-budget)
	$(DIARY) lfs-budget

lfs-budget: lfs-check

lfs-commit: ## Commit the days' media to LFS, one commit per day, within the budget (DAY=...; DRY=1)
	$(DIARY) lfs-commit $(if $(DRY),--dry-run) $(DAY)

lfs-push: ## Push the archive's commits (LFS objects first) and verify the LFS file list
	$(DIARY) lfs-push

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
