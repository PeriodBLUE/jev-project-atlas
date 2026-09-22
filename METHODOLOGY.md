# Methodology and scope

**English** · [简体中文](METHODOLOGY.zh-CN.md)

## Inclusion target

JEV Project Atlas tracks public GitHub projects directly related to TypeSafe AI's JEV / System One decision model, including:

- official resources, SDKs, adapters, and examples;
- applications, agents, MCP servers, CLIs, and domain tools that call JEV;
- independent open implementations of a JEV-compatible input/output shape;
- evaluation, observability, data, and research tools;
- framework integrations with concrete source evidence.

A repository does not enter the source-verified layer merely because “JEV” appears in its name, description, README, or topics.

## The two-layer data model

### 1. Source-verified

Every entry has at least one immutable commit link locating a JEV call, adapter, decision point, or compatible implementation. Pinning the commit keeps the evidence stable when a default branch changes.

Verification does **not** mean that we:

- ran or deployed the project;
- reproduced claimed performance, latency, or cost;
- completed a security, legal-license, or supply-chain audit;
- endorse the project's quality or production readiness.

### 2. Topic-discovered

The discovery layer collects all repositories returned for GitHub's `jev` topic. Topics are self-assigned and can include:

- genuine JEV projects awaiting review;
- projects that only mention a future JEV integration;
- unrelated topic noise;
- duplicate, archived, experimental, or low-information repositories.

The discovery layer is useful for recall, not ranking or recommendation.

## Refresh and deduplication

- Case-insensitive `owner/name` is the repository identity key.
- Verified projects are rendered by stars descending, then repository name ascending.
- GitHub Search is split into starred and zero-star partitions to avoid the 1,000-result cap.
- All snapshots use UTC dates; dynamic metrics represent only the latest refresh.

## What “complete” means

Completeness is an auditable target, not an absolute promise:

- the discovery layer covers repositories visible to anonymous users at refresh time;
- the verified layer covers public projects reviewed by the upstream source-evidence process;
- private, deleted, undiscovered, or untagged repositories cannot be guaranteed.

If something is missing, open an issue with the repository URL, the exact JEV integration point, and a one-line description.
